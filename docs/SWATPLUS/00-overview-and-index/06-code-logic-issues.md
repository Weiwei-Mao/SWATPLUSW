---
type: note
tags:
  - swat/channel
  - swat/source-review
  - swat/water-quality
status: rough
---

# Possible Channel Code Issues

## Quick List

| File | What looks strange |
|---|---|
| `sd_channel_sediment3.f90` | Floodplain deposition uses `flo_time = 2 * ht1%flo / ave_rate`, which becomes constant. |
| `sd_channel_sediment3.f90` | `florate = 2 * ht1%flo - ave_rate` mixes volume and rate. |
| `sd_channel_sediment3.f90` | Bed erosion nutrient conversion is not consistent with bank erosion. |
| `sd_channel_sediment3.f90` | Bed erosion is calculated, but the line adding it to `ht1` is commented. |
| `ch_rtmusk.f90` | Daily branch resets Muskingum `nsteps` and `substeps`, even though `sd_hydsed_init.f90` already calculated them. |
| `ch_rtmusk.f90` | `inflo_rate = inflo / 86400.` seems wrong for subdaily/substep routing. |
| `ch_watqual4.f90` | Final nutrient masses are calculated with `ht1%flo`, not `ht2%flo`. |
| `ch_watqual4.f90` | Algae calculation uses `alg_m` as `term_m`, but `alg_m` is a concentration. |
| `ch_watqual4.f90` | `bc1_k` and `bc3_k` are multiplied by `2` without a clear reason. |
| `ch_watqual4.f90` | Organic N misses the algae respiration/death source shown in the theory docs. |
| `ch_watqual4.f90` | `alg_m_o2` is calculated but does not appear in the dissolved oxygen update. |

## 1. sd_channel_sediment3.f90

This subroutine tries to calculate bank erosion, bed erosion, and deposition.

### 1.1 Floodplain Deposition, Logic Error

The block starts by calculating average daily flow:

```fortran
104    ave_rate = ht1%flo / 86400.     ! m3/s average daily flow rate
```

Then, if overbank flow exists:

```fortran
109    flo_time = 2. * ht1%flo / ave_rate
```

But since `ave_rate = ht1%flo / 86400`, this becomes:

```text
flo_time = 2 * 86400
```

So `flo_time` is constant whenever `ht1%flo > 0`. That does not look like a real flood duration.

Plugging in `ave_rate`, `flo_time` works out to `2 * 86400 = 172800` s — so it looks like a constant (about 2 days) regardless of the hydrograph. If that's right, `flo_time` is always `>= 86400`, the test `if (flo_time < 86400.)` at line 116 would never be true, and the "flood over within the day" branch would never run — only the `else` branch below.

Another line in the same block:

```fortran
121    florate = 2. * ht1%flo - ave_rate
```

This looks worse because `ht1%flo` is volume with unit m3, while `ave_rate` is m3/s. So this is probably a unit problem unless one of the variable meanings is different from the comments.

If this is a unit problem, it would also propagate: the same `florate` is used in the `flovol_ob` denominator at line 122, so it would affect the overbank flood volume estimate too.

### 1.2 Bed Erosion Nutrients, Unit Error

For bed erosion:

```fortran
273    bed_ero%orgn = bed_ero%sed * sd_ch(ich)%n_conc                               ! tons * mg/kg = g, but bed_ero%orgn unit is kg
274    bed_ero%sedp = (1. - sd_ch(ich)%p_bio) * bed_ero%sed * sd_ch(ich)%p_conc
276    bed_ero%solp = sd_ch(ich)%p_bio * bed_ero%sed * sd_ch(ich)%p_conc
```

For bank erosion, the code uses `/ 1000.` in the nutrient calculation. Here it does not.

If `n_conc`/`p_conc` are in mg/kg (as the inline comment assumes) and the nutrient fields are stored in kg, then `sed [t] * conc [mg/kg]` gives grams, and the missing `/1000` would leave `bed_ero%orgn`/`%sedp`/`%solp` about 1000x too large — but the units of `n_conc` and the storage fields need confirming before trusting that. This and 1.3 are worth reading together, since `bed_ero` does not appear to be added to the hydrograph.

### 1.3 Bed Erosion Not Added

The bed erosion block ends with:

```fortran
278    rto = bed_ero%flo / ht1%flo
279    !ob(icmd)%tsin(:) = (1. - rto) * ob(icmd)%tsin(:)
280    !ht1 = ht1 + bed_ero
```

So bed erosion is calculated, but it is not added to the channel hydrograph. Bank erosion and floodplain deposition do change `ht1`, but bed erosion does not. It also seems that no deposition happens for bed erosion.

From a read of the code, the erosion depth does get used (`ebtm_m` feeds `ch_morph%d_yr` at line 269), but the sediment/nutrient mass (`sed`/`orgn`/`sedp`/`solp`) does not appear to be added to `ht1` anywhere — worth confirming it isn't used in a later routine. Also `bed_ero%flo` does not seem to be assigned anywhere, so `rto = bed_ero%flo / ht1%flo` at line 278 may always be 0.

For bank erosion, deposition is calculated as a constant percentage of the eroded amount.
```fortran
250    ch_dep%sed = sd_ch(ich)%wash_bed_fr * bank_ero%sed
```

## 2. ch_rtmusk.f90

### 2.1 Muskingum Substeps

The Muskingum stability condition is:

```text
2 K X < delta_t < 2 K (1 - X)   ! Equation 7:1.4.8 in theoretical documentation
```

In `sd_hydsed_init.f90`, the code calculates substeps to satisfy this condition:

```fortran
173    !! Muskingum numerical stability -Jaehak Jeong, 2011
174    detmax = 2.* xkm * (1.- bsn_prm%msk_x)
175    det = time%dtm / 60.      !hours
176    sd_ch(i)%msk%substeps = 1
178    !! Discretize time interval to meet the stability criterion
179    if (det > detmax) then
180        sd_ch(i)%msk%substeps = Int(det / detmax) + 1
181    end if
185    sd_ch(i)%msk%nsteps = time%step * sd_ch(i)%msk%substeps
```

In the current local `ch_rtmusk.f90`, the daily reset block is:

```fortran
90    !! set for daily time step
91    if (time%step == 1) then
92        sd_ch(jrch)%msk%nsteps = 1
93        sd_ch(jrch)%msk%substeps = 1
94    end if
```

It will overwrite the prepared `sd_ch(jrch)%msk%nsteps` and `sd_ch(jrch)%msk%substeps`.

`time%step` appears to be steps-per-day (line 185 multiplies it by `substeps`), so `== 1` likely means a daily run. The reset also looks redundant with `sd_hydsed_init`, which already forces `substeps = 1` for the daily/simple case at lines 182-184 (`if rte == 0 .and. step <= 1`). A case worth checking: if init kept `substeps > 1` for stability and `ch_rtmusk` still forces 1, those stability substeps would be lost — but whether daily routing actually needs them is something to confirm.

### 2.2 Inflow Rate Under Substeps

Inside the routing loop:

```fortran
97     dts = time%dtm / sd_ch(jrch)%msk%substeps * 60.

119    inflo = ob(icmd)%tsin(irtstep) / sd_ch(jrch)%msk%substeps

128    inflo_rate = inflo / 86400.

159    outflo_rate = outflo / dts
```

`inflo` is already the water volume for this Muskingum substep. Therefore the flow rate should use the substep duration:

```fortran
inflo_rate = inflo / dts
```

Using `/ 86400.` only makes sense if `inflo` is daily volume. Under subdaily or Muskingum substeps, it is not.

In units, `inflo [m3/substep] / dts [s/substep]` would give m3/s; dividing by `86400 [s/day]` instead looks inconsistent with how `outflo_rate` is computed (`/ dts`, line 159) in the same loop. Since `inflo_rate` feeds the rating-curve lookup at line 129, this could affect the depth/velocity used downstream — worth checking what the author intended here.

## ch_watqual4.f90

### Converting Concentration Back To Mass

At the start, the routine converts incoming mass to concentration:

```fortran
98    ht3%orgn = 1000. * ht1%orgn / ht1%flo
99    ht3%sedp = 1000. * ht1%sedp / ht1%flo
...
```

At the end, it converts concentration back to mass:

```fortran
327    ht2%orgn = ht3%orgn * ht1%flo / 1000.
328    ht2%sedp = ht3%sedp * ht1%flo / 1000.
...
```

This looks wrong because `ht1` is inflow and `ht2` is outflow. If `ht3` is the
final concentration after channel reactions, then the final mass should probably
use `ht2%flo`:

```fortran
ht2%orgn = ht3%orgn * ht2%flo / 1000.
```

Need to double check whether the code intentionally treats water quality as
reacting on inflow volume instead of outflow volume. But for routing output,
`ht2%flo` is the more natural volume.

### Algae Calculation

The algae block does this:

```fortran
205    factk = Theta(gra, thgra, wtmp) - Theta(ch_nut(jnut)%rhoq, thrho, wtmp)
206    algcon = 1000. * ht3%chla / ch_nut(jnut)%ai0
207    alg_m1 = wq_semianalyt(tday, rt_delt, 0., factk, algcon, algin)

209    alg_m = wq_semianalyt(tday, rt_delt, 0., factk, algcon, algin)
210    alg_m2 = alg_m - alg_m1
```

`alg_m1` and `alg_m` have exactly the same inputs, so `alg_m2` is always zero.

Then:

```fortran
220    algcon_out = wq_semianalyt(tday, rt_delt, alg_m, -alg_set, algcon, algin)
```

This is the main issue: `alg_m` is a concentration, but it is passed as
`term_m`. In `wq_semianalyt`, `term_m` should be concentration per time.

If growth, respiration, and settling happen together, a cleaner equation is:

```fortran
k_total = Theta(gra, thgra, wtmp) - Theta(ch_nut(jnut)%rhoq, thrho, wtmp) - alg_set
algcon_out = wq_semianalyt(tday, rt_delt, 0., k_total, algcon, algin)
```

If the author wanted two steps, then the first step result should become the
next `cprev`, not `term_m`.

### Algae Uptake Of NO3, NH4, And P

The code calculates:

```fortran
214    alg_no3_m = -alg_m * (1. - f1) * ch_nut(jnut)%ai1
215    alg_nh4_m = -alg_m * f1 * ch_nut(jnut)%ai1
216    alg_P_m = -alg_m * ch_nut(jnut)%ai2
```

This also looks wrong because `alg_m` is final algae concentration, not algae
growth during the time step.

The theory docs describe uptake as algal growth demand:

```text
nutrient uptake = algae growth rate * algae concentration * nutrient fraction
```

So something like this is closer to the theory:

```fortran
alg_growth_m = Theta(gra, thgra, wtmp) * algcon
alg_no3_m = -(1. - f1) * ch_nut(jnut)%ai1 * alg_growth_m
alg_nh4_m = -f1 * ch_nut(jnut)%ai1 * alg_growth_m
alg_p_m = -ch_nut(jnut)%ai2 * alg_growth_m
```

Maybe net algae change should be used instead, but `-alg_m` is not right either
way.

Also, these variables are calculated but do not seem to be used later in the
nitrogen equations.

### Nitrogen Rates Multiplied By 2

The nitrogen block has:

```fortran
248    bc1_k = Theta(ch_nut(jnut)%bc1, thbc1, wtmp) ! NH3 -> NO2
249    bc3_k = Theta(ch_nut(jnut)%bc3, thbc3, wtmp) ! Organic N -> ammonia
250    bc1_k = bc1_k * 2.
251    bc3_k = bc3_k * 2.
```

I do not see why only these two rates are doubled.

`Theta` already applies temperature correction. `ch_read_nut.f90` already scales
these rates by `time%step`. The theory docs do not show a factor of `2` here.

So this looks like either:

- old calibration tuning,
- an undocumented unit correction,
- or just a hard-coded mistake.

### Organic N Missing Algae Respiration/Death Source

The organic N block uses:

```fortran
255    bc3_m = wq_k2m(tday, rt_delt, -bc3_k, ht3%orgn, ht3%orgn)
256    factk = -rs4_k
257    factm = bc3_m
258    ht3%orgn = wq_semianalyt(tday, rt_delt, factm, factk, ht3%orgn, ht3%orgn)
```

This includes:

- organic N hydrolysis to ammonia,
- organic N settling.

But the theory docs also have organic N generated from algal respiration/death:

```text
organic N source = algae N fraction * algae respiration/death rate * algae
```

So this term seems missing:

```fortran
orgn_from_algae = ch_nut(jnut)%ai1 * Theta(ch_nut(jnut)%rhoq, thrho, wtmp) * algcon
```

Need to check units before writing any fix, but conceptually the source term is
not in the current code.

### Dissolved Oxygen And Algae

The code calculates:

```fortran
266    alg_m_o2 = ch_nut(jnut)%ai4 * alg_m2 + ch_nut(jnut)%ai3 * alg_m1
```

where:

- `ai4` is oxygen uptake by algae respiration,
- `ai3` is oxygen production by algal photosynthesis.

But `alg_m_o2` is not used in the DO equation:

```fortran
272    factm = rk1_m + rk2_m - rs4_k + bc1_m * ch_nut(jnut)%ai5 + bc2_m * ch_nut(jnut)%ai6
273    ht3%dox = wq_semianalyt(tday, rt_delt, factm, factk, ht3%dox, ht3%dox)
```

Also, because `alg_m1` and `alg_m` are identical, `alg_m2` is zero anyway.

This part needs another pass against the DO theory equation.

## Still To Add

- More checks in `ch_watqual4.f90` for nitrogen, phosphorus, and oxygen.
- Exact links to the online theory pages.
- Simple numerical tests for each suspicious block.
