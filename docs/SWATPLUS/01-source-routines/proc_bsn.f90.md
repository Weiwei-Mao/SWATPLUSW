---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
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
reads: []
writes: []
purpose: ""
---

# proc_bsn

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `proc_bsn.f90`
- **Modules used**: [[time_module.f90]], [[output_path_module.f90]]
- **Subroutine calls**: 11 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[readcio_read.f90]]
- `open_output_file`
- [[basin_read_cc.f90]]
- [[basin_read_objs.f90]]
- [[time_read.f90]]
- [[basin_read_prm.f90]]
- [[basin_prm_default.f90]]
- [[basin_print_codes_read.f90]]
- [[co2_read.f90]]
- [[carbon_bsn_read.f90]]
- [[carbon_layers_read.f90]]

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- use: `time_module`, `output_path_module`
- Line 12: call [[readcio_read.f90]]
- Line 15: call `open_output_file(9000, "files_out.out")`
- Line 18: call `open_output_file(9001, "diagnostics.out", 8000)` -- unit 9001, recl 8000
- Line 21: call `open_output_file(9004, "area_calc.out", 80000)` -- unit 9004, recl 80000
- Line 23: call [[basin_read_cc.f90]]
<!-- USER-NOTES-END -->
