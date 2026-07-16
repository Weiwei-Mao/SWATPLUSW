---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_yield.f90
note_file: header_yield.f90
subroutine: header_yield
module:
  - basin_module
  - hydrograph_module
  - output_path_module
calls:
  - open_output_file
uses_variables:
  - basin_module.f90#bsn
  - basin_module.f90#bsn_yld_hdr
  - basin_module.f90#pco
  - basin_module.f90#prog
  - hydrograph_module.f90#sp_ob
input_variables: []
reads: []
writes:
  - yield.out
  - yield.csv
  - basin_crop_yld_yr.txt
  - basin_crop_yld_aa.txt
purpose: ""
---

# header_yield

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_yield.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[hydrograph_module.f90]]
  - [[output_path_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 4

## Call Relationships
**This routine calls:**

- [[output_path_module.f90#open_output_file]]

**Called by:**

- [[proc_open.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn]] - `basin_inputs`
- [[basin_module.f90#bsn_yld_hdr]] - `basin_yld_header`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[basin_module.f90#prog]] - `character(len=80)`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`

## File I/O
- **Writes**:
  - [[yield.out]]
  - [[yield.csv]]
  - [[basin_crop_yld_yr.txt]]
  - [[basin_crop_yld_aa.txt]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
