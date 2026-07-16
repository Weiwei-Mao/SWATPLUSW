---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_mgt.f90
note_file: header_mgt.f90
subroutine: header_mgt
module:
  - basin_module
  - output_path_module
calls:
  - open_output_file
uses_variables:
  - basin_module.f90#bsn
  - basin_module.f90#mgt_hdr
  - basin_module.f90#mgt_hdr_unt1
  - basin_module.f90#pco
  - basin_module.f90#prog
input_variables: []
reads: []
writes:
  - mgt_out.txt
purpose: ""
---

# header_mgt

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_mgt.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[output_path_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 1

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
- [[basin_module.f90#mgt_hdr]] - `mgt_header`
- [[basin_module.f90#mgt_hdr_unt1]] - `mgt_header_unit1`
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[basin_module.f90#prog]] - `character(len=80)`

## File I/O
- **Writes**:
  - [[mgt_out.txt]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
