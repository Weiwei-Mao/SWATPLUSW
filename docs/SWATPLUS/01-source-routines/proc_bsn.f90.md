---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/read
file: proc_bsn.f90
note_file: proc_bsn.f90
subroutine: proc_bsn
module:
  - time_module
  - output_path_module
calls:
  - readcio_read
  - open_output_file
  - basin_read_cc
  - basin_read_objs
  - time_read
  - basin_read_prm
  - basin_prm_default
  - basin_print_codes_read
  - co2_read
  - carbon_bsn_read
  - carbon_layers_read
uses_variables:
  - time_module.f90#time
input_variables: []
reads: []
writes:
  - files_out.out
  - diagnostics.out
  - area_calc.out
purpose: ""
---

# proc_bsn

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `proc_bsn.f90`
- **Modules used**:
  - [[time_module.f90]]
  - [[output_path_module.f90]]
- **Subroutine calls**: 11 | **Files read**: 0 | **Files written**: 3

## Call Relationships
**This routine calls:**

- [[readcio_read.f90]]
- [[output_path_module.f90#open_output_file]]
- [[basin_read_cc.f90]]
- [[basin_read_objs.f90]]
- [[time_read.f90]]
- [[basin_read_prm.f90]]
- [[basin_prm_default.f90]]
- [[basin_print_codes_read.f90]]
- [[co2_read.f90]]
- [[carbon_bsn_read.f90]]
- [[carbon_layers_read.f90]]

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[time_module.f90#time]] - `time_current`

## File I/O
- **Writes**:
  - [[files_out.out]]
  - [[diagnostics.out]]
  - [[area_calc.out]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- use:
	- [[time_module.f90]]
	- [[output_path_module.f90]]
- Line 12: call [[readcio_read.f90]]
- Line 15: call [[output_path_module.f90#open_output_file]]; opens [[files_out.out]] (unit 9000)
- Line 18: call [[output_path_module.f90#open_output_file]]; opens [[diagnostics.out]] (unit 9001, recl 8000)
- Line 21: call [[output_path_module.f90#open_output_file]]; opens [[area_calc.out]] (unit 9004, recl 80000)
- Line 23: call [[basin_read_cc.f90]]
- Line 24: call [[basin_read_objs.f90]]
- Line 25: call [[time_read.f90]]
- Line 28: time%dmt, time step in minutes for rainfall, runoff and routing
- Line 31: call [[basin_read_prm.f90]]
- Line 32: call [[basin_prm_default.f90]], set default parameters of [[basin_module.f90#bsn_prm]], [[hru_module.f90#hru_module#uptake]]
- Line 33: call [[basin_print_codes_read.f90]]
- Line 34: call [[co2_read.f90]], read atmosphere co2 input if it is available
- Line 35: call [[carbon_bsn_read.f90]]
- Line 36: call [[carbon_layers_read.f90]]
- End
- Line 12 [[readcio_read.f90]] is the file.cio parser: it reads file.cio and fills the in_* vars (in_sim, in_cli, in_init, …) that every later reader looks up by name. That's what makes "file.cio-registered" files work. co2 (L34) and carbon_layers (L36) do the opposite — names hardwired in code. More: [[input-file-architecture]].
<!-- USER-NOTES-END -->
