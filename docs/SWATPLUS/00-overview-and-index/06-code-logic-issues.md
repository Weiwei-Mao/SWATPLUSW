---
type: note
author: Wei Mao
tags:
  - swat/channel
  - swat/hru
  - swat/source-review
  - swat/water-quality
status: rough
source_revision: "SWAT+ Revision 62; SWATPLUS/swatplus cb442f7c05fc3bfc34349c446010f452d2737ca0"
---

# Possible SWAT+ Code Logic Issues

> Source version: SWAT+ Revision 62, `SWATPLUS/swatplus` commit `cb442f7c05fc3bfc34349c446010f452d2737ca0` (2026-07-06).

## Quick List

| Section                                              | File                       | What looks strange                                                                                                    |
| ---------------------------------------------------- | -------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| 1.1 Floodplain Deposition, Logic Error               | `sd_channel_sediment3.f90` | Flood duration appears to become constant, and `florate = 2 * ht1%flo - ave_rate` mixes volume and rate.              |
| 1.2 Bed Erosion Nutrients, Unit Error                | `sd_channel_sediment3.f90` | Bed erosion nutrient conversion is not consistent with bank erosion and may miss `/ 1000.`.                           |
| 1.3 Bed Erosion Not Added                            | `sd_channel_sediment3.f90` | Bed erosion is calculated, but the line adding it to `ht1` is commented out.                                          |
| 2.1 Muskingum Substeps                               | `ch_rtmusk.f90`            | Daily routing resets Muskingum `nsteps` and `substeps`, even though `sd_hydsed_init.f90` already calculated them.     |
| 2.2 Inflow Rate Under Substeps                       | `ch_rtmusk.f90`            | `inflo_rate = inflo / 86400.` seems wrong for subdaily or Muskingum substep routing.                                  |
| 3.1 Converting Concentration Back To Mass            | `ch_watqual4.f90`          | Final nutrient masses are calculated with `ht1%flo`, not `ht2%flo`.                                                   |
| 3.2 Algae Calculation                                | `ch_watqual4.f90`          | `alg_m` is used like a change or source term, but `wq_semianalyt` returns a final concentration.                      |
| 3.3 Algae Uptake Of NO3, NH4, And P                  | `ch_watqual4.f90`          | Algal nutrient uptake terms are calculated, but NO3 and NH4 updates do not consistently include those sinks.          |
| 3.4 Nitrogen Rates Multiplied By 2                   | `ch_watqual4.f90`          | `bc1_k` and `bc3_k` are multiplied by `2` after time-step scaling and temperature correction, without a clear reason. |
| 3.5 Organic N Missing Algae Respiration/Death Source | `ch_watqual4.f90`          | Organic N misses the algae respiration/death source shown in the theory docs.                                         |
| 3.6 Dissolved Oxygen And Algae                       | `ch_watqual4.f90`          | `alg_m_o2` is calculated but not used in the dissolved oxygen update; other DO source/sink terms look inconsistent.   |
| 4.1 Mineral N Pool Update After C/N Transformations  | `cbn_zhang2.f90`           | Net C/N transformation balance changes NO3/NH4 partitioning instead of updating total mineral N.                      |

These notes collect possible logic issues found while tracing SWAT+ source code. Most current items are in the SWAT-DEG channel path.

The code execution path starts as:

```text
main.f90 -> time_control.f90 -> command.f90
```

In `command.f90`, SWAT+ dispatches by spatial object type, such as `hru`, `hru_lte`, `ru`, `aqu`, and `chandeg`. For an HRU object, the model enters `hru_control.f90`. For a SWAT-DEG channel object (`chandeg`), the model enters `sd_channel_control3.f90`.

In this note, each numbered main section is a Fortran file or subroutine. Each subsection describes one possible logic issue found in that file. Sections 1-3 are connected to the `sd_channel_control3.f90` channel-control path. Section 4 is connected to `hru_control.f90`.

In the following routine, `ht1` is the incoming hydrograph for a spatial object, `ht2` is the outgoing hydrograph. For `swat-deg` object, `ht3` is used as a temporary concentration state for the water quality reactions.

## 1. sd_channel_sediment3.f90

Call path:

```text
command.f90 -> if spatial object is 'swat-deg' -> sd_channel_control3.f90 -> sd_channel_sediment3.f90
```

`sd_channel_sediment3.f90` is called in `sd_channel_control3.f90` before channel routing. It calculates floodplain deposition, bank erosion, and bed erosion. The result should affect the incoming channel hydrograph (`ht1`) (mainly flow and erosion) before `ch_rtmusk.f90` routes water through the channel.

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
flo_time = 2 * ht1%flo / ave_rate = 2 * ht1%flo / (ht1%flo / 86400.) = 2 * 86400
```

So `flo_time` is constant whenever `ht1%flo > 0`. That does not look like a real flood duration.

`flo_time` works out to `2 * 86400 = 172800` s, so it looks like a constant (about 2 days) regardless of the hydrograph. If that's right, `flo_time` is always `>= 86400`, the test `if (flo_time < 86400.)` at line 116 would never be true, and the "flood over within the day" branch would never run; only the `else` branch below would run.

Another line in the same block:

```fortran
121    florate = 2. * ht1%flo - ave_rate
```

This looks worse because `ht1%flo` is volume with unit m3, while `ave_rate` is m3/s. So this is probably a unit problem.

### 1.2 Bed Erosion Nutrients, Unit Error

For bed erosion:

```fortran
273    bed_ero%orgn = bed_ero%sed * sd_ch(ich)%n_conc                               ! tons * mg/kg = g, but bed_ero%orgn unit is kg
274    bed_ero%sedp = (1. - sd_ch(ich)%p_bio) * bed_ero%sed * sd_ch(ich)%p_conc
276    bed_ero%solp = sd_ch(ich)%p_bio * bed_ero%sed * sd_ch(ich)%p_conc
```

For bank erosion, the same file does include `/ 1000.`:

```fortran
224    bank_ero%orgn = bank_ero%sed * sd_ch(ich)%n_conc / 1000.
225    bank_ero%sedp = (1. - sd_ch(ich)%p_bio) * bank_ero%sed * sd_ch(ich)%p_conc / 1000.
227    bank_ero%solp = sd_ch(ich)%p_bio * bank_ero%sed * sd_ch(ich)%p_conc / 1000.
```

So the bed erosion conversion is not consistent with the bank erosion conversion.

This and 1.3 are worth reading together, since `bed_ero` does not appear to be added to the hydrograph.

### 1.3 Bed Erosion Not Added

The bed erosion block ends with:

```fortran
278    rto = bed_ero%flo / ht1%flo
279    !ob(icmd)%tsin(:) = (1. - rto) * ob(icmd)%tsin(:)
280    !ht1 = ht1 + bed_ero
```

So bed erosion is calculated, but it is not added to the channel hydrograph. Bank erosion and floodplain deposition do change `ht1`, but bed erosion does not. 

`bed_ero%flo` does not seem to be assigned anywhere, so `rto = bed_ero%flo / ht1%flo` at line 278 may always be 0.

It also seems that no deposition happens for bed erosion. For bank erosion, deposition is calculated as a constant percentage of the eroded amount:
```fortran
250    ch_dep%sed = sd_ch(ich)%wash_bed_fr * bank_ero%sed
```

## 2. ch_rtmusk.f90

Call path:

```text
command.f90 -> if spatial object is 'swat-deg' -> sd_channel_control3.f90 -> ch_rtmusk.f90
```

`ch_rtmusk.f90` is called after `sd_channel_sediment3.f90`. Its job is to route channel water from the incoming hydrograph (`ht1`) to the outgoing hydrograph (`ht2`) using Muskingum or variable-storage routing. It also updates channel and floodplain storage variables used during routing.

### 2.1 Muskingum Substeps

The Muskingum stability condition is:

```text
2 K X < delta_t < 2 K (1 - X)   ! Equation 7:1.4.8 in theoretical document of SWAT
```

Example from the `Osu_1hru` demo:

- ==Set `rte_cha = 1` in `codes.bsn`== to use Muskingum channel routing. `rte_cha = 0` uses the variable-storage method (default).
- During initialization, the path `main.f90 -> proc_cha.f90 -> sd_hydsed_init.f90` calculates the Muskingum parameters.
- In this example, `sd_hydsed_init.f90` needs 11 Muskingum substeps per day. That means each routing substep is about 2.18 hours.
- Later, when `ch_rtmusk.f90` runs, the block at lines 90-94 resets `nsteps` and `substeps` back to 1. That removes the 11 substeps calculated for stability.

In `sd_hydsed_init.f90`, the code calculates substeps to satisfy the stability condition:

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

The effect is important: if `sd_hydsed_init.f90` increased `substeps` to satisfy the Muskingum stability condition, this reset changes the routing time step back to the full daily step. Then `delta_t` may no longer satisfy `2 K X < delta_t < 2 K (1 - X)`. In that case the Muskingum coefficients can become inconsistent with the stability check, and the routed outflow may be numerically unreliable.

### 2.2 Inflow Rate Under Substeps

The subdaily routing loop is in `ch_rtmusk.f90`:

```fortran
98     dts = time%dtm / sd_ch(jrch)%msk%substeps * 60.

102    do ii = 1, sd_ch(jrch)%msk%nsteps
104        isubstep = isubstep + 1
105        ......
```

For the `Osu_1hru` Muskingum example above, `dts` is about 7854.5 seconds, or 2.18 hours. This is the Muskingum routing substep duration, not the full daily duration.

`ob(icmd)%tsin` is the model subdaily inflow array. For example, if SWAT+ runs with a 6-hour model time step, `tsin` has 4 values per day. `sd_ch(jrch)%msk%substeps` then divides each model time step into smaller Muskingum steps if needed for stability. For example, if Muskingum needs about 2.18 hours while the model time step is 6 hours, the code uses multiple substeps inside that 6-hour interval.

Inside this loop, the code calculates substep inflow:

```fortran
119    inflo = ob(icmd)%tsin(irtstep) / sd_ch(jrch)%msk%substeps

128    inflo_rate = inflo / 86400.

159    outflo_rate = outflo / dts
```

`inflo` is already the water volume for this Muskingum substep. Therefore the flow rate should use the substep duration:

```fortran
inflo_rate = inflo / dts
```

Using `/ 86400.` only makes sense if `inflo` is daily volume. Under subdaily or Muskingum substeps, it is not.

## 3. ch_watqual4.f90

Call path:

```text
command.f90 -> if spatial object is 'swat-deg' -> sd_channel_control3.f90 -> ch_watqual4.f90
```

`ch_watqual4.f90` is called inside `sd_channel_control3.f90` after flow routing, when there is channel inflow (`ht1%flo > 1.e-6`). It computes in-stream water quality reactions for nutrients, algae, CBOD, and dissolved oxygen. The routine converts hydrograph masses to concentrations, updates reaction concentrations, then writes masses back to the outgoing hydrograph (`ht2`).

### 3.1 Converting Concentration Back To Mass

At the beginning of the routine, incoming constituent mass is converted to concentration using the inflow volume:

```fortran
98    ht3%orgn = 1000. * ht1%orgn / ht1%flo     ! 1000 * kg / m3 = mg/L
99    ht3%sedp = 1000. * ht1%sedp / ht1%flo
...
```

At the end of the routine, the updated concentration is converted back to mass and stored in `ht2`:

```fortran
327    ht2%orgn = ht3%orgn * ht1%flo / 1000.
328    ht2%sedp = ht3%sedp * ht1%flo / 1000.
...
```

The questionable part is that the output mass is still scaled by `ht1%flo`. If `ht3` is the final concentration after channel reactions, and `ht2` is the routed output hydrograph, then the final load should normally be tied to the output water volume (`ht2`), instead of (`ht1`):

```fortran
ht2%orgn = ht3%orgn * ht2%flo / 1000.
```

### 3.2 Algae Calculation

The algae block seems to use `alg_m` as algae change during the time step, meaning growth minus respiration/death.

```fortran
205    factk = Theta(gra, thgra, wtmp) - Theta(ch_nut(jnut)%rhoq, thrho, wtmp)  ! growth rate - respiration or death rate, considered temperature adjustment
206    algcon = 1000. * ht3%chla / ch_nut(jnut)%ai0
207    alg_m1 = wq_semianalyt(tday, rt_delt, 0., factk, algcon, algin)          ! algae concentration after growth and respiration/death

209    alg_m = wq_semianalyt(tday, rt_delt, 0., factk, algcon, algin)
210    alg_m2 = alg_m - alg_m1
```

`wq_semianalyt(tres, tdel, term_m, prock, cprev, cint)` solves:

$$
\frac{dC}{dt} = \frac{Cin - C} {tres} + term_m + prock \cdot C
$$

Meaning of the inputs:

- `tres`: residence time in the reach, days
- `tdel`: calculation time step, days
- `term_m`: zero-order source/sink term, concentration per day
- `prock`: first-order reaction coefficient, 1/day
- `cprev`: concentration at the previous step
- `cint`: incoming concentration

Output:

- `wq_semianalyt`: updated concentration, `Cnew`, after transport plus zero- and first-order reactions
$$
C_{new} = \frac{a}{b}+(cprev-\frac{a}{b})\cdot e^{-bt}
$$
where $a = \frac{C_{int}}{tres}+term_m$, and $b=\frac{1}{tres}-prock$.

The function returns `Cnew`. It does not return `Cnew - cprev`. Therefore `alg_m` is a final concentration here, not delta algae. Since `alg_m1` and `alg_m` use the same inputs, `alg_m2 = alg_m - alg_m1` should always be zero.

This matters because `alg_m2` is used later in dissolved oxygen:

```fortran
266    alg_m_o2 = ch_nut(jnut)%ai4 * alg_m2 + ch_nut(jnut)%ai3 * alg_m1
```

The same issue appears in the settling calculation:

```fortran
220    algcon_out = wq_semianalyt(tday, rt_delt, alg_m, -alg_set, algcon, algin)
```

In `wq_semianalyt`, the third argument is the zero-order source/sink term. Passing `alg_m` there only makes sense if `alg_m` is a 0-order item, not the final concentration. 

### 3.3 Algae Uptake Of NO3, NH4, And P

The code calculates:

```fortran
214    alg_no3_m = -alg_m * (1. - f1) * ch_nut(jnut)%ai1
215    alg_nh4_m = -alg_m * f1 * ch_nut(jnut)%ai1
216    alg_P_m = -alg_m * ch_nut(jnut)%ai2
```

If `alg_m` really means algae change during this time step (algae growth minus algae respiration/death), this calculation is reasonable:

- `f1` partitions algal N uptake between ammonium and nitrate.
- `ai1` converts algae biomass demand to nitrogen demand.
- `ai2` converts algae biomass demand to phosphorus demand.
- the negative sign makes uptake a loss from the dissolved nutrient pools.

The real problem is in the later nutrient updates. The code computes possible algae uptake terms, but the final NO3 and NH4 updates do not consistently include algae growth uptake. `ht3nh3` and `ht3%no3` are final concentrations.

```fortran
281    ht3%nh3 = wq_semianalyt(tday, rt_delt, factm, 0., ht3%nh3, ammoin)    ! factm here is (organic N -> NH3) - (NH3 -> NO2), 0 order 

293    ht3%no3 = wq_semianalyt(tday, rt_delt, factm, 0., ht3%no3, ht3%no3)   ! factm here is NO2 -> NO3, 0 order
```

The ammonia and nitrate equations include nitrification/mineralization terms, but they do not subtract algal N uptake from `ht3%nh3` or `ht3%no3`. If algae growth consumes inorganic N, these updates should include that sink somewhere.

For soluble P, the update does include an algae-growth sink, but it is calculated separately.

### 3.4 Nitrogen Rates Multiplied By 2

The nitrogen block first temperature-corrects two reaction rates:

```fortran
248    bc1_k = Theta(ch_nut(jnut)%bc1, thbc1, wtmp) ! NH3 -> NO2, temperature correction
249    bc3_k = Theta(ch_nut(jnut)%bc3, thbc3, wtmp) ! Organic N -> ammonia, temperature correction
250    bc1_k = bc1_k * 2.
251    bc3_k = bc3_k * 2.
```

`bc1_k` controls ammonia oxidation to nitrite. `bc3_k` controls organic N hydrolysis to ammonia. The confusing part is that only these two rates are doubled after the `Theta` temperature correction.

The reader already scales the channel nutrient rates by the model time step:

```fortran
120    ch_nut(ich)%bc1 = ch_nut(ich)%bc1 / real(time%step)
122    ch_nut(ich)%bc3 = ch_nut(ich)%bc3 / real(time%step)
```

So the code already includes:

- time-step scaling in `ch_read_nut.f90`
- temperature correction through `Theta(...)`
- then an extra hard-coded `* 2.` in `ch_watqual4.f90`

### 3.5 Organic N Missing Algae Respiration/Death Source

The theoretical equation for organic N has three main terms:

```text
d(orgN)/dt = algae respiration/death source - organic N hydrolysis - organic N settling
```

Mapped to the code variables:

- algae source: `ai1 * Theta(rhoq, thrho, wtmp) * algcon`
- hydrolysis loss: `bc3`, organic N to ammonia
- settling loss: `rs4 / rchdep`

The current organic N block only includes the two loss terms:

```fortran
252    rs4_k = 0.
253    if (rchdep > 0.001) rs4_k = Theta(ch_nut(jnut)%rs4, thrs4, wtmp) / rchdep

255    bc3_m = wq_k2m(tday, rt_delt, -bc3_k, ht3%orgn, ht3%orgn)
256    factk = -rs4_k
257    factm = bc3_m
258    ht3%orgn = wq_semianalyt(tday, rt_delt, factm, factk, ht3%orgn, ht3%orgn)
```

Here:

- `bc3_m` is the organic N hydrolysis loss, converted from a first-order term to a zero-order `term_m` for `wq_semianalyt`.
- `factk = -rs4_k` is the organic N settling loss as a first-order term.

For `wq_k2m(t1, t2, tk, c1, c2)`, the idea is to make these two equations give the same final concentration over one time step:

$$
\begin{aligned}
&\frac{dC}{dt} = \frac{c2 - C} {t1} + tk \cdot C \\
&\frac{dC}{dt} = \frac{c2 - C} {t1} + tm
\end{aligned}
$$

Here `c1` is the initial concentration, `c2` is the incoming concentration, `t1` is residence time, `t2` is the calculation time step, `tk` has units of `1/time`, and `tm` has units of `concentration/time`.

So `wq_k2m` changes a first-order term (`tk * C`) into an equivalent zero-order term (`tm`) for this one step. It first solves the equation with `tk`, gets the final concentration, then calculates the `tm` that would give the same final concentration when `prock = 0`.

This explains what the function does, but it also raises a question. In many places it may be clearer to add all first-order terms into one `prock`, add all zero-order terms into one `term_m`, and solve once with `wq_semianalyt`. The current code sometimes converts one first-order process into `tm` using `wq_k2m`, then solves again with another first-order process. 

Back to the problem, the positive algae respiration/death source is not included in this update. Conceptually, that source would be something like:

```text
orgn_from_algae = ch_nut(jnut)%ai1 * Theta(ch_nut(jnut)%rhoq, thrho, wtmp) * algcon
```

This is not a proposed code fix yet.

### 3.6 Dissolved Oxygen And Algae

The dissolved oxygen equation should include these main terms:

```text
d(DO)/dt = reaeration rate * (O2 saturation concentration - current O2 concentration)
           - (algae photosynthesis rate - algae respiration rate) * algae
           - CBOD deoxygenation
           - sediment oxygen demand
           - oxygen uptake by NH4 oxidation to NO2
           - oxygen uptake by NO2 oxidation to NO3
```
Well, the code for solving this equation looks a bit messy.

The code calculates an algal oxygen term:

```fortran
266    alg_m_o2 = ch_nut(jnut)%ai4 * alg_m2 + ch_nut(jnut)%ai3 * alg_m1
```

where:

- `ai4` is oxygen uptake by algae respiration.
- `ai3` is oxygen production by algal photosynthesis.

Problems in this algal part:

- If `ai4` represents oxygen uptake by algae respiration, this term should reduce dissolved oxygen.
- `alg_m2` is always zero in the current code. See section 3.2: `alg_m1` and `alg_m` are calculated from the same `wq_semianalyt` call.
- `alg_m2` should probably represent algae growth during the time step, but the current calculation does not give that value.
- `alg_m_o2` is calculated, but it is not used later in the DO update.

The DO update is:

```fortran
268    factk = -rk2_k                                                ! reaeration rate
269    bc2_k = -Theta(ch_nut(jnut)%bc2, thbc2, wtmp)                 ! NO2 -> NO3 rate with temperature adjustment
270    bc1_m = wq_k2m(tday, rt_delt, factk, ht3%nh3, ammoin)         ! change first-order term to zero-order term
271    bc2_m = wq_k2m(tday, rt_delt, bc2_k, ht3%no2, ht3%no2)        ! NO2 -> NO3, from first-order to zero-order

!      rk1_m: CBOD deoxygenation, zero-order term
!      rk2_m: reaeration rate * saturation oxygen concentration, zero-order term
!      rs4_k: organic N settling rate, first-order term
!      bc1_m: NH4 -> NO2 term, but currently calculated using factk = -rk2_k
!      ai5:   oxygen uptake per unit NH4-N oxidation
!      bc2_m: NO2 -> NO3 term, zero-order term
!      ai6:   oxygen uptake per unit NO2-N oxidation

272    factm = rk1_m + rk2_m - rs4_k + bc1_m * ch_nut(jnut)%ai5 + bc2_m * ch_nut(jnut)%ai6
273    ht3%dox = wq_semianalyt(tday, rt_delt, factm, factk, ht3%dox, ht3%dox)
274    if (ht3%dox <0.) ht3%dox = 0.
```

The confusing parts are:

- The algal oxygen term is missing from `factm`, so algal oxygen production/uptake does not affect `ht3%dox`.
- CBOD consumes oxygen, but `rk1_m` is added in `factm`. It seems this should be a subtraction term.
- Sediment oxygen demand is calculated earlier as `rk4_s` and `disoxin`, but this DO update does not use `disoxin`. Instead, `factm` subtracts `rs4_k`, which is the organic N settling coefficient.
- `bc1_m` should represent oxygen uptake from NH4 oxidation to NO2, but it is calculated with `factk`, which was just set to the reaeration coefficient `-rk2_k`. The code already has `bc1_k` for NH4 to NO2 at line 248, but that coefficient is not used here.

## 4. cbn_zhang2.f90

This is an HRU-side issue. The call path is:

```text
command.f90 -> if spatial object is 'hru' -> hru_control.f90 -> cbn_zhang2.f90
```

In `hru_control.f90`, `cbn_zhang2` is called only when `bsn_cc%cswat == 2`, after surface residue decomposition and residue transfer:

```fortran
387    if (bsn_cc%cswat == 2) then
388        if (bmix_eff > 1.e-6 ) call mgt_biomix(ihru, bmix_eff)
389        !! compute surface residue decomposition for each plant in community
390        call cbn_surfrsd_decomp
391        !! compute soil residue (roots and tilled in) decomposition
392        call cbn_rsd_transfer
393        ! call cbn_rsd_decomp
394        !! compute mineralization and carbon pool transformations
395        call cbn_zhang2
396    end if
```

So this routine is used for dynamic soil carbon, nitrogen, and phosphorus pool transformations in regular HRUs.

### 4.1 Mineral N Pool Update After C/N Transformations

In `cbn_zhang2.f90`, organic carbon and nitrogen are stored in several pools:

![[Figure1.png|650]]

The organic pools transform into each other. Because each pool has its own C:N ratio, a C transfer can either release N or require extra N.

![[Figure2.png|650]]

The following are the C/N reactions between organic pools. The C/N transformation logic is controlled by supply and demand:

- N supply is released from the source organic pool.
- N demand is the N required by the receiving organic pool.
- If supply is larger than demand, extra N should be released to the mineral N pool.
- If demand is larger than supply, extra N should be immobilized from mineral N.
- If total available N is not enough, the ==C transformation rate== is reduced. (Note, the C transformation is based on N balance. And after calculation of C transformation, N transformation is calculated based on C:N ratio.)

The reduction factor is:

$$
reduc = \frac{N\ supply + NO3 + NH4}{N\ demand}
$$

After reduction, the code recalculates actual supply and demand:

```fortran
675    !total available n
676    sum = sum1 + sum2 + sum3 + sum4 + sum5
677    wmin = max(1.e-5, soil1(j)%mn(k)%no3 + soil1(j)%mn(k)%nh4 + sum)

679    !total demand for potential tranformaiton of som
688    trnn = cpn1 + cpn2 + cpn3 + cpn4 + cpn5

682    !supply - demand
683    rnmn = sum - trnn
```

So `rnmn` is the net N balance after the actual transformations:

- `rnmn > 0`: organic transformations release mineral N.
- `rnmn < 0`: organic transformations need mineral N immobilization.

Then we need update mineral N pools based on mineralization and immobilization. But the update block is:

```fortran
685    !     update
686    if (rnmn > 0.) then
687        min_n = Max(0., soil1(j)%mn(k)%no3 - rnmn)
688        soil1(j)%mn(k)%nh4 = soil1(j)%mn(k)%nh4 + min_n
689        soil1(j)%mn(k)%no3 = soil1(j)%mn(k)%no3 - min_n
690        ! print*, "2. in cbn_zhang2", k, soil1(j)%mn(k)%no3, min_n
691    end if
```

This does not look like mineralization or immobilization. If `rnmn > 0`, the code should add the released N to a mineral N pool, that is an extra source. Instead, it calculates `min_n` from the existing NO3 pool, adds that amount to NH4, and subtracts the same amount from NO3.

For example, if `NO3 = 10`, `NH4 = 1`, and `rnmn = 2`, the code gives:

```text
min_n = max(0, 10 - 2) = 8
NO3 = 10 - 8 = 2
NH4 = 1 + 8 = 9
```

The new mineral N (NO3 + NH4) should be 10 + 1 + 2 = 13. But under current method, total mineral N stays 11. No new mineral N is added, even though `rnmn > 0` means the organic transformations released N. Also, when `rnmn < 0`, there is no matching branch here to subtract immobilized N from the mineral pools.


## Still Reading

Comparing with other versions, such as SWAT-Carbon / SWAT-2012, to confirm the issues?
