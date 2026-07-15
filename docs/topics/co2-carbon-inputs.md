---
title: CO2 and carbon input readers
kind: knowledge
status: partial
created: 2026-07-13
updated: 2026-07-13
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, basin, co2, carbon]
---

# CO2 and Carbon Input Readers

## Summary

These three readers are called during basin setup after `codes.bsn`, `object.cnt`, `time.sim`, `parameters.bsn`, parameter defaults, and `print.prt` have already been read.

```text
proc_bsn
    -> co2_read
    -> carbon_bsn_read
    -> carbon_layers_read
```

Their roles are different:

| Reader | Main function |
| --- | --- |
| `co2_read` | Builds the annual atmospheric CO2 series used by the simulation and writes `co2.out`. |
| `carbon_bsn_read` | Reads dynamic soil-carbon parameters, but only when `codes.bsn` has `carbon = 2`. |
| `carbon_layers_read` | Optionally controls how many soil layers are printed in per-layer carbon output files. |

The source routine is named `carbon_bsn_read`, not `carbon_basin_read`.

## Input Files

| File | Reader | How it is selected | Required? |
| --- | --- | --- | --- |
| `co2_yr.dat` | `co2_read` | Fixed filename; not listed in `file.cio`. | Optional. If missing, the model uses `bsn_prm%co2`. |
| `carbon.bsn` or another basin carbon filename | `carbon_bsn_read` | Third slot of the `file.cio` basin section, stored as `in_basin%carbon_bsn`. | Required only when `codes.bsn` `carbon = 2`. |
| `carbon_lyr.bsn` | `carbon_bsn_read` | Derived from `carbon.bsn`: `carbon.bsn` -> `carbon_lyr.bsn`. | Required only when `codes.bsn` `carbon = 2`. |
| `carbon_layers.prt` | `carbon_layers_read` | Fixed filename; not listed in `file.cio`. | Optional. If missing, default output-layer behavior is used. |

## `co2_read` And `co2_yr.dat`

`co2_read` always runs. It creates the array `co2y(time%nbyr)`, one CO2 value for each simulation year, and writes the resolved series to `co2.out`.

### Format

```text
title/comment line
number_of_year_records
header line
year_1  co2_ppm_1
year_2  co2_ppm_2
...
```

Example shape:

```text
annual atmospheric CO2
3
year co2
2000 369.5
2001 371.0
2002 373.1
```

### Runtime logic

- If `co2_yr.dat` is missing, every simulation year uses `bsn_prm%co2`.
- `bsn_prm%co2` comes from `parameters.bsn`, then may be changed by `basin_prm_default`.
- If the simulation starts before the first CO2 file year, the first file value is used until the yearly record begins.
- If the simulation continues after the last CO2 file year, the last available CO2 value is held constant.
- If the whole CO2 file period is before the simulation start, the last file value is used for all simulation years.

For `Osu_1hru`, no `co2_yr.dat` is present. The scenario therefore uses `bsn_prm%co2`. In `parameters.bsn`, `co2 = 1.57`, but `basin_prm_default` resets values below `100` to `400`. So the expected resolved annual CO2 value is `400 ppm`.

## `carbon_bsn_read`, `carbon.bsn`, And `carbon_lyr.bsn`

`carbon_bsn_read` only matters when dynamic carbon is active:

```text
codes.bsn carbon column
    -> bsn_cc%cswat
    -> if bsn_cc%cswat /= 2, carbon_bsn_read returns immediately
```

For `Osu_1hru`, `codes.bsn` has `carbon = 0`, so this reader returns immediately. The third basin slot in `file.cio` is also `null`. That is acceptable only because dynamic carbon is off; if `carbon = 2`, that slot would need a real filename such as `carbon.bsn`.

### `carbon.bsn` format

```text
title/comment line
header line
one data row with 28 values
```

The row is positional. The values are read into these groups:

| Group | Values |
| --- | --- |
| Organic pool fractions | `frac_seq`, `frac_hum_microb`, `frac_hum_slow`, `frac_hum_passive` |
| Water/temperature coefficients | `prmt_21`, `prmt_44`, `tmpf`, `watf`, `tn`, `top`, `tx` |
| Tillage/manure/residue controls | `till_eff_days`, `man_rtof`, `bio_consf`, `till_consf`, `photo_degrade_factor` |
| Biological/tillage mixing | `bmix_a`, `bmix_b`, `bmix_c`, `tillmix_a`, `tillmix_b`, `tillmix_c` |
| Residue decomposition tunables | `n_act_frac`, `cnr_cap`, `cnr_ref`, `cpr_cap`, `cpr_ref` |
| Initialization method flag | `mathers_method`, where `1` enables the Mathers humus-slow initialization method. |

### `carbon_lyr.bsn` format

`carbon_lyr.bsn` travels with `carbon.bsn`. If `file.cio` names the basin carbon file `foo.bsn`, the layer file becomes `foo_lyr.bsn`.

```text
title/comment line
header line
layer_id  hp_rate  hs_rate  microb_rate  meta_rate  str_rate  microb_top_rate  hs_hp  a1co2  asco2  apco2  abco2
...
```

The current source expects one row per carbon layer group in `carbdb`. At this revision, that array has two entries:

| `layer_id` | Meaning |
| --- | --- |
| `1` | Top carbon layer group. |
| `2` | Subsurface carbon layer group. |

The rate fields populate `carbdb(layer_id)`. The allocation/CO2 fraction fields populate `org_allo(layer_id)`.

## `carbon_layers_read` And `carbon_layers.prt`

`carbon_layers_read` is not a carbon-process parameter reader. It is an optional output-control reader for per-layer carbon output.

### Format

```text
title/comment line
header line
n_layers
```

If the file exists and `n_layers >= 1`, the reader sets:

```text
cb_n_layers = n_layers
cb_n_layers_explicit = true
```

If the file is missing, the routine returns silently. Later output initialization can choose a default, normally based on the largest HRU soil-layer count. The fallback value in `carbon_module` is `7`.

## Debugging Notes

Useful watches:

| Watch | Why |
| --- | --- |
| `bsn_prm%co2` | Final defaulted CO2 value from `parameters.bsn`. |
| `co2y` | Annual CO2 array actually used by simulation years. |
| `bsn_cc%cswat` | Carbon model switch from `codes.bsn`. |
| `in_basin%carbon_bsn` | File name for dynamic carbon basin parameters. |
| `cb_n_layers` | Number of soil layers requested for carbon output. |
| `cb_n_layers_explicit` | Whether `carbon_layers.prt` explicitly set the layer count. |

Useful breakpoints:

1. `basin_prm_default.f90`, after the CO2 default check, to confirm final `bsn_prm%co2`.
2. `co2_read.f90`, after `allocate (co2y(...))`, to inspect the annual CO2 series.
3. `carbon_bsn_read.f90`, first executable line, to see whether `bsn_cc%cswat` causes an immediate return.
4. `carbon_layers_read.f90`, after the `inquire`, to see whether `carbon_layers.prt` exists.

## Evidence

- [`co2_read.f90`](../../SWATPLUS/swatplus/src/co2_read.f90): annual CO2 file/default logic and `co2.out` writer.
- [`carbon_bsn_read.f90`](../../SWATPLUS/swatplus/src/carbon_bsn_read.f90): dynamic carbon file reader and `carbon = 2` gate.
- [`carbon_layers_read.f90`](../../SWATPLUS/swatplus/src/carbon_layers_read.f90): optional carbon layer output-control reader.
- [`carbon_module.f90`](../../SWATPLUS/swatplus/src/carbon_module.f90): carbon state, `carbdb`, `org_allo`, and `cb_n_layers`.
- [`input_file_module.f90`](../../SWATPLUS/swatplus/src/input_file_module.f90): `in_basin%carbon_bsn` field and default filename.
- [`codes.bsn`](../../VSProj/SWAT/Osu_1hru/codes.bsn): `Osu_1hru` carbon switch.
- [`parameters.bsn`](../../VSProj/SWAT/Osu_1hru/parameters.bsn): `Osu_1hru` basin CO2 input value.
- [`co2.out`](../../VSProj/SWAT/Osu_1hru/co2.out): resolved annual CO2 output from the current run.

## Related Notes

- [`codes.bsn` basin control codes](../inputs/basin/codes-bsn.md)
- [`parameters.bsn` basin parameters](../inputs/basin/parameters-bsn.md)
- [`print.prt` output controls](../inputs/simulation/print-prt.md)
- [Input to output path](../tracing-guide.md)
