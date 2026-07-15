---
title: print.prt output control file
kind: input-reference
status: partial
created: 2026-07-13
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, output, print-prt]
---

# `print.prt` Output Control File

## Summary

`print.prt` controls which output files SWAT+ writes and at what reporting frequency. It does not choose physical process methods and does not usually change the model equations. It mainly controls reporting.

The file is read by [`basin_print_codes_read.f90`](../../../SWATPLUS/swatplus/src/basin_print_codes_read.f90) into `pco`, the basin print-control object.

Use this distinction:

```text
codes.bsn        -> model switches and method choices
parameters.bsn   -> numeric basin parameters
object.cnt       -> object counts
print.prt        -> output/reporting controls
```


## Official SWAT+ Reference

- Official page: [print.prt](https://swatplus.gitbook.io/io-docs/introduction-1/simulation-settings/print.prt).
- Official index note: This file controls which output files will be printed during the simulation.
- Official field metadata available: 5 field row(s); matched to 2 of 6 observed demo header field(s).
- Demo cross-check: local header and first data row are still used below to show how this scenario instantiates the official format.

## Reader Path

```text
file.cio
    -> in_sim%prt = "print.prt"
    -> proc_bsn
    -> basin_print_codes_read
    -> pco
```

`pco` is defined in [`basin_module.f90`](../../../SWATPLUS/swatplus/src/basin_module.f90) as `type basin_print_codes`.

In `proc_bsn`, this reader is called after basin codes, object counts, time settings, basin parameters, and parameter defaults:

```fortran
call basin_read_cc
call basin_read_objs
call time_read
time%dtm = 1440. / time%step
call basin_read_prm
call basin_prm_default
call basin_print_codes_read
```

## File Structure

The active `Osu_1hru` file has these blocks:

```text
title
daily-output date window and interval
average-annual interval count
special output format flags
other output flags
object/category output rows
```

The object/category rows use this shape:

```text
object_name    daily    monthly    yearly    avann
```

Each flag is usually:

```text
y = write this output frequency
n = do not write this output frequency
```

`avann` means average annual output.

## Top Block Meaning

| `print.prt` field | Stored field | Meaning |
| --- | --- | --- |
| `nyskip` | `pco%nyskip` | Number of simulation years skipped before output summarization. |
| `day_start` | `pco%day_start` | Julian day to start daily printing. |
| `yrc_start` | `pco%yrc_start` | Calendar year to start daily printing. |
| `day_end` | `pco%day_end` | Julian day to stop daily printing. |
| `yrc_end` | `pco%yrc_end` | Calendar year to stop daily printing. |
| `interval` | `pco%int_day` | Daily print interval. |
| `aa_int_cnt` | `pco%aa_numint` | Number of average-annual print intervals. If greater than zero, following values are read into `pco%aa_yrs`. |
| `csvout` | `pco%csvout` | Write CSV outputs if `y`. |
| `dbout` | `pco%use_obj_labels` | In source, this controls whether object rows are read by labels. Header name is historical/confusing. |
| `cdfout` | `pco%cdfout` | Write NetCDF outputs if `y`. |
| `soilout` | `pco%crop_yld` | Header name is historical/confusing; source stores this in crop-yield output control. |
| `mgtout` | `pco%mgtout` | Write management output if `y`. |
| `hydcon` | `pco%hydcon` | Write hydrograph connection output if `y`. |
| `fdcout` | `pco%fdcout` | Flow-duration curve output flag; source comment says not active. |

## Output Row Meaning

Each object row maps into a `print_interval` field in `pco`. A `print_interval` has:

```fortran
d  ! daily flag
m  ! monthly flag
y  ! yearly flag
a  ! average annual flag
```

Examples:

| Row name | Stored field | Meaning |
| --- | --- | --- |
| `basin_wb` | `pco%wb_bsn` | Basin water-balance output. |
| `basin_nb` | `pco%nb_bsn` | Basin nutrient-balance output. |
| `basin_ls` | `pco%ls_bsn` | Basin losses output. |
| `basin_pw` | `pco%pw_bsn` | Basin plant/weather output. |
| `region_wb` | `pco%wb_reg` | Region water-balance output. |
| `lsunit_wb` | `pco%wb_lsu` | Landscape-unit water-balance output. |
| `hru_wb` | `pco%wb_hru` | HRU water-balance output. |
| `hru_nb` | `pco%nb_hru` | HRU nutrient-balance output. |
| `hru_ls` | `pco%ls_hru` | HRU losses output. |
| `hru_pw` | `pco%pw_hru` | HRU plant/weather output. |
| `hru-lte_wb` | `pco%wb_sd` | HRU-LTE water-balance output. |
| `channel` | `pco%chan` | Regular channel output. |
| `channel_sd` | `pco%sd_chan` | SWAT-DEG/channel-LTE output. |
| `aquifer` | `pco%aqu` | Aquifer output. |
| `reservoir` | `pco%res` | Reservoir output. |
| `recall` | `pco%recall` | Recall object output. |
| `hyd` | `pco%hyd` | Hydrograph input/output output. |
| `ru` | `pco%ru` | Routing-unit output. |
| `pest` | `pco%pest` | Pesticide output families. |

The source supports more rows than the short `Osu_1hru` file shows, including salt, constituent, carbon, LSU carbon, and GWFLOW outputs.

## `Osu_1hru` Interpretation

The active file begins:

```text
nyskip day_start yrc_start day_end yrc_end interval
3      0         0         0       0       1
```

Meaning:

- skip the first 3 years for output summarization;
- daily print date window is not explicitly bounded by real dates in this file;
- daily interval is 1 if daily output is enabled.

The format flags are:

```text
csvout dbout cdfout
n      n     n
```

Meaning:

- no CSV output;
- no NetCDF output;
- `dbout/use_obj_labels = n`, so the fixed-order read path is used by the current source.

The other output flags are:

```text
soilout mgtout hydcon fdcout
n       y      n      n
```

Meaning:

- `mgtout = y`: management output is enabled;
- `hydcon = n`: hydrograph connection output is not enabled;
- `fdcout = n`: flow-duration output is not enabled.

Example object row:

```text
basin_wb    n    n    y    y
```

This means:

```text
daily basin water balance: no
monthly basin water balance: no
yearly basin water balance: yes
average annual basin water balance: yes
```

Most `Osu_1hru` rows are `n n n y`, meaning only average annual output is requested. `basin_wb` additionally requests yearly output.

## How Output Routines Use `pco`

Output routines check `pco` before writing. For example, basin output checks flags like:

```fortran
if (pco%wb_bsn%y == "y") then
  ! write yearly basin water balance
end if
```

Daily output also depends on runtime daily-print state such as `pco%day_print` and `pco%int_day_cur`, which are updated in `time_control.f90`.

So `print.prt` is a gate:

```text
model computes state
    -> output routine is called
    -> pco flags decide whether that state is written
```

## Debugging Notes

Useful breakpoints:

1. `basin_print_codes_read.f90`, after the top block reads, to inspect `pco%nyskip`, `pco%csvout`, `pco%mgtout`, and `pco%hydcon`.
2. `basin_print_codes_read.f90`, after object rows, to inspect specific print intervals such as `pco%wb_bsn`, `pco%wb_hru`, `pco%sd_chan`, or `pco%ru`.
3. An output routine, such as `basin_output.f90`, to see the final write gate.
4. `time_control.f90`, around daily/yearly/end-simulation logic, to see when `pco%day_print`, `time%end_yr`, and `time%end_sim` allow output.

## Evidence

- [`VSProj/SWAT/Osu_1hru/print.prt`](../../../VSProj/SWAT/Osu_1hru/print.prt): active scenario values.
- [`basin_print_codes_read.f90`](../../../SWATPLUS/swatplus/src/basin_print_codes_read.f90): reader and row mapping.
- [`basin_module.f90`](../../../SWATPLUS/swatplus/src/basin_module.f90): `type basin_print_codes`, `type print_interval`, and `pco`.
- [`basin_output.f90`](../../../SWATPLUS/swatplus/src/basin_output.f90): example downstream output gates.
- [`time_control.f90`](../../../SWATPLUS/swatplus/src/time_control.f90): daily/yearly/end-simulation output timing state.

## Related Notes

- [`file.cio` master input file](file-cio.md)
- [`codes.bsn` basin control codes](../basin/codes-bsn.md)
- [`parameters.bsn` basin parameters](../basin/parameters-bsn.md)
- [Tracing guide](../../tracing-guide.md)
