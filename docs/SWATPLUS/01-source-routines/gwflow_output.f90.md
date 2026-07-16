---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gwflow_output.f90
note_file: gwflow_output.f90
subroutine: gwflow_output_init
module:
  - gwflow_module
  - hydrograph_module
  - sd_channel_module
  - time_module
  - constituent_mass_module
  - basin_module
calls:
  - gwflow_write_celldef
  - gwflow_write_cell_array
reads:
  - gwflow.wbgroups
  - file_name_scalar
  - file_name(n
  - file_name(n
  - file_name(n
  - file_name(n
writes:
  - gwflow_basin_wb_day.txt
  - gwflow_basin_wb_mon.txt
  - gwflow_basin_wb_yr.txt
  - gwflow_basin_wb_aa.txt
  - gwflow_basin_heat_day.txt
  - gwflow_basin_heat_yr.txt
  - gwflow_basin_heat_aa.txt
  - gwflow_cell_wb_day.txt
  - gwflow_cell_wb_mon.txt
  - gwflow_cell_wb_yr.txt
  - gwflow_cell_wb_aa.txt
  - gwflow_cell_definition.txt
purpose: "this subroutine opens all gwflow output files and writes headers; (extracted from gwflow_read)"
---

# gwflow_output_init

> [!info] Summary
> this subroutine opens all gwflow output files and writes headers; (extracted from gwflow_read)

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gwflow_output.f90`
- **Modules used**: [[gwflow_module.f90]], [[hydrograph_module.f90]], [[sd_channel_module.f90]], [[time_module.f90]], [[constituent_mass_module.f90]], [[basin_module.f90]]
- **Subroutine calls**: 2 | **Files read**: 6 | **Files written**: 12

## Call Relationships
**This routine calls:**

- `gwflow_write_celldef`
- `gwflow_write_cell_array`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Writes**: `gwflow_basin_wb_day.txt`, `gwflow_basin_wb_mon.txt`, `gwflow_basin_wb_yr.txt`, `gwflow_basin_wb_aa.txt`, `gwflow_basin_heat_day.txt`, `gwflow_basin_heat_yr.txt`, `gwflow_basin_heat_aa.txt`, `gwflow_cell_wb_day.txt`, `gwflow_cell_wb_mon.txt`, `gwflow_cell_wb_yr.txt`, `gwflow_cell_wb_aa.txt`, `gwflow_cell_definition.txt`
- **Reads**: `gwflow.wbgroups`, `file_name_scalar` _(variable; see file.cio)_, `file_name(n` _(variable; see file.cio)_, `file_name(n` _(variable; see file.cio)_, `file_name(n` _(variable; see file.cio)_, `file_name(n` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
