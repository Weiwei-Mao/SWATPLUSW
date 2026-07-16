---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_snutc.f90
note_file: header_snutc.f90
subroutine: header_snutc
module:
  - hydrograph_module
  - soil_nutcarb_module
  - output_path_module
calls:
  - open_output_file
uses_variables:
  - hydrograph_module.f90#sp_ob
  - soil_nutcarb_module.f90#orgc_hdr
  - soil_nutcarb_module.f90#orgc_units
  - soil_nutcarb_module.f90#totc_hdr
  - soil_nutcarb_module.f90#totc_units
input_variables: []
reads: []
writes:
  - hru_orgc.txt
  - hru_totc.txt
  - basin_totc.txt
purpose: ""
---

# header_snutc

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_snutc.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[soil_nutcarb_module.f90]]
  - [[output_path_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 3

## Call Relationships
**This routine calls:**

- [[output_path_module.f90#open_output_file]]

**Called by:**

(No static callers detected.)

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[soil_nutcarb_module.f90#orgc_hdr]] - `organic_carbon_header`
- [[soil_nutcarb_module.f90#orgc_units]] - `organic_carbon_units`
- [[soil_nutcarb_module.f90#totc_hdr]] - `total_carbon_header`
- [[soil_nutcarb_module.f90#totc_units]] - `total_carbon_units`

## File I/O
- **Writes**:
  - [[hru_orgc.txt]]
  - [[hru_totc.txt]]
  - [[basin_totc.txt]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
