---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_path.f90
note_file: header_path.f90
subroutine: header_path
module:
  - basin_module
  - reservoir_module
  - output_ls_pathogen_module
  - constituent_mass_module
  - output_path_module
calls:
  - open_output_file
uses_variables:
  - basin_module.f90#bsn
  - basin_module.f90#pco
  - basin_module.f90#prog
  - constituent_mass_module.f90#cs_db
  - output_ls_pathogen_module.f90#pathb_hdr
input_variables: []
reads: []
writes:
  - hru_path_day.txt
  - hru_path_day.csv
  - hru_path_mon.txt
  - hru_path_mon.csv
  - hru_path_yr.txt
  - hru_path_yr.csv
  - hru_path_aa.txt
  - hru_path_aa.csv
purpose: ""
---

# header_path

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_path.f90`
- **Modules used**:
  - [[basin_module.f90]]
  - [[reservoir_module.f90]]
  - [[output_ls_pathogen_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[output_path_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 8

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
- [[basin_module.f90#pco]] - `basin_print_codes`
- [[basin_module.f90#prog]] - `character(len=80)`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[output_ls_pathogen_module.f90#pathb_hdr]] - `output_pathbal_header`

## File I/O
- **Writes**:
  - [[hru_path_day.txt]]
  - [[hru_path_day.csv]]
  - [[hru_path_mon.txt]]
  - [[hru_path_mon.csv]]
  - [[hru_path_yr.txt]]
  - [[hru_path_yr.csv]]
  - [[hru_path_aa.txt]]
  - [[hru_path_aa.csv]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
