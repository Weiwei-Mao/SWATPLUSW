---
type: module
tags:
  - swat/module
  - swat/to-read
file: time_module.f90
note_file: time_module.f90
module_name: time_module
defines_types:
  - time_current
defines_vars:
  - cal_sim
  - cal_adj
  - yrs_print
  - ndays
  - ndays_leap
  - ndays_noleap
  - ndmo
  - time
  - time_init
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# time_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### time_current

- **Defined in source**: `time_module.f90:16`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day_print` | `character (len=1)` | 17 |  |
| `day` | `integer` | 18 | current day of simulation |
| `mo` | `integer` | 19 | current month of simulation |
| `mo_start` | `integer` | 20 | starting month |
| `yrc` | `integer` | 21 | current calendar year |
| `yrc_start` | `integer` | 22 | starting calendar year |
| `yrc_end` | `integer` | 23 | ending calendar year |
| `yrs` | `integer` | 24 | current sequential year |
| `day_mo` | `integer` | 25 | day of month (1-31) |
| `end_mo` | `integer` | 26 | set to 1 if end of month |
| `end_yr` | `integer` | 27 | set to 1 if end of year |
| `end_sim` | `integer` | 28 | set to 1 if end of simulation |
| `end_aa_prt` | `integer` | 29 | set to 1 if end of simulation |
| `day_start` | `integer` | 30 | beginning julian day of simulation |
| `day_end_yr` | `integer` | 31 | ending julian day of each year |
| `day_end` | `integer` | 32 | input ending julian day of simulation |
| `nbyr` | `integer` | 33 | number of years of simulation run |
| `step` | `integer` | 34 | number of time steps in a day for rainfall, runoff and routing 0 = daily; 1=increment(12 hrs); 24=hourly; 96=15 mins; 1440=minute; |
| `dtm` | `real` | 36 | time step in minutes for rainfall, runoff and routing |
| `days_prt` | `real` | 37 | number of days for average annual printing for entire time period |
| `yrs_prt` | `real` | 38 | number of years for average annual printing for entire time period |
| `yrs_prt_int` | `real` | 39 | number of years for average annual printing for printing interval- pco%aa_yrs() |
| `num_leap` | `integer` | 40 | number of leap years in simulation for average annual printing |
| `prt_int_cur` | `integer` | 41 | current average annual print interval |
| `yrc_tot` | `integer` | 42 |  |

## Variables Defined
### cal_sim

- **Type**: `character (len=29)`
- **Defined in source**: `time_module.f90:6`

### cal_adj

- **Type**: `real`
- **Defined in source**: `time_module.f90:7`

### yrs_print

- **Type**: `real`
- **Defined in source**: `time_module.f90:8`

### ndays

- **Type**: `integer, dimension (13)`
- **Defined in source**: `time_module.f90:9`

### ndays_leap

- **Type**: `integer, dimension (13)`
- **Defined in source**: `time_module.f90:10`

### ndays_noleap

- **Type**: `integer, dimension (13)`
- **Defined in source**: `time_module.f90:11`

### ndmo

- **Type**: `integer, dimension (12)`
- **Defined in source**: `time_module.f90:12`
- **Source note**: cumulative number of days accrued in the

### time

- **Type**: `time_current`
- **Defined in source**: `time_module.f90:44`

### time_init

- **Type**: `time_current`
- **Defined in source**: `time_module.f90:45`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
(No functions detected.)

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
