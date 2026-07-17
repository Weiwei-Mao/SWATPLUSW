---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: object_read_output.f90
note_file: object_read_output.f90
subroutine: object_read_output
module:
  - input_file_module
  - hydrograph_module
  - maximum_data_module
calls: []
uses_variables:
  - hydrograph_module.f90#dr
  - hydrograph_module.f90#exco
  - hydrograph_module.f90#fp_hdr
  - hydrograph_module.f90#hyd_hdr
  - hydrograph_module.f90#hyd_hdr_time
  - hydrograph_module.f90#mobj_out
  - hydrograph_module.f90#ob_out
  - hydrograph_module.f90#plt_hdr
  - hydrograph_module.f90#res
  - hydrograph_module.f90#sol_hdr
  - hydrograph_module.f90#sp_ob1
  - input_file_module.f90#in_sim
  - maximum_data_module.f90#db_mx
input_variables:
  - hydrograph_module.f90#ob_out
reads:
  - in_sim%object_prt
  - ob_out(i
writes: []
purpose: ""
---

# object_read_output

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `object_read_output.f90`
- **Modules used**:
  - [[input_file_module.f90]]
  - [[hydrograph_module.f90]]
  - [[maximum_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 2 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hydrograph_module.f90#dr]] - `hyd_output`
- [[hydrograph_module.f90#exco]] - `hyd_output`
- [[hydrograph_module.f90#fp_hdr]] - `flood_plain_header`
- [[hydrograph_module.f90#hyd_hdr]] - `hyd_header`
- [[hydrograph_module.f90#hyd_hdr_time]] - `hyd_header_time`
- [[hydrograph_module.f90#mobj_out]] - `integer`
- [[hydrograph_module.f90#ob_out]] - `object_output`
- [[hydrograph_module.f90#plt_hdr]] - `plant_header`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#sol_hdr]] - `sol_header`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[input_file_module.f90#in_sim]] - `input_sim`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

**Populated by file reads:**

- [[hydrograph_module.f90#ob_out]]

## File I/O
- **Reads**:
  - [[object.prt]]
  - `ob_out(i` _(variable; see [[file.cio]])_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

	- for example: 1 hru 5 sur hru5_surface.out
	- Line 1, export hru with id 5, export surface runoff to file hru5_surface.out




<!-- USER-NOTES-END -->
