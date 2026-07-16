---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: hyd_connect.f90
note_file: hyd_connect.f90
subroutine: hyd_connect
module:
  - hydrograph_module
  - input_file_module
  - recall_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - ru_module
  - basin_module
calls:
  - hyd_read_connect
  - ru_read
  - ru_read_elements
  - aqu2d_read
  - overbank_read
  - dr_db_read
  - gwflow_chan_read
  - gwflow_read
  - exit
uses_variables:
  - basin_module.f90#bsn_prm
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#hcs1
  - constituent_mass_module.f90#hcs2
  - constituent_mass_module.f90#hcs3
  - constituent_mass_module.f90#hin_csz
  - constituent_mass_module.f90#obcs
  - hydrograph_module.f90#aqu
  - hydrograph_module.f90#dfn_sum
  - hydrograph_module.f90#dr
  - hydrograph_module.f90#exco
  - hydrograph_module.f90#hd_tot
  - hydrograph_module.f90#ich
  - hydrograph_module.f90#ob
  - hydrograph_module.f90#rcv_sum
  - hydrograph_module.f90#recall
  - hydrograph_module.f90#res
  - hydrograph_module.f90#ru_def
  - hydrograph_module.f90#ru_elem
  - hydrograph_module.f90#ru_seq
  - hydrograph_module.f90#sp_ob
  - hydrograph_module.f90#sp_ob1
  - input_file_module.f90#in_con
  - ru_module.f90#iru
  - ru_module.f90#ru
input_variables: []
reads: []
writes:
  - looping.con
purpose: "reads in the routing information from the watershed configuration; input file (.fig) and calculates the number of subbasins, reaches,; and reservoirs"
---

# hyd_connect

> [!info] Summary
> reads in the routing information from the watershed configuration; input file (.fig) and calculates the number of subbasins, reaches,; and reservoirs

## Basic Information
- **Type**: `subroutine`
- **Source file**: `hyd_connect.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[input_file_module.f90]]
  - [[recall_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[ru_module.f90]]
  - [[basin_module.f90]]
- **Subroutine calls**: 9 | **Files read**: 0 | **Files written**: 1

## Call Relationships
**This routine calls:**

- [[hyd_read_connect.f90]]
- [[ru_read.f90]]
- [[ru_read_elements.f90]]
- [[aqu2d_read.f90]]
- [[overbank_read.f90]]
- [[dr_db_read.f90]]
- [[gwflow_chan_read.f90]]
- [[gwflow_read.f90]]
- `exit`

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#hcs1]] - `constituent_mass`
- [[constituent_mass_module.f90#hcs2]] - `constituent_mass`
- [[constituent_mass_module.f90#hcs3]] - `constituent_mass`
- [[constituent_mass_module.f90#hin_csz]] - `constituent_mass`
- [[constituent_mass_module.f90#obcs]] - `all_constituent_hydrograph`
- [[hydrograph_module.f90#aqu]] - `hyd_output`
- [[hydrograph_module.f90#dfn_sum]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#dr]] - `hyd_output`
- [[hydrograph_module.f90#exco]] - `hyd_output`
- [[hydrograph_module.f90#hd_tot]] - `object_total_hydrographs`
- [[hydrograph_module.f90#ich]] - `integer`
- [[hydrograph_module.f90#ob]] - `object_connectivity`
- [[hydrograph_module.f90#rcv_sum]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#recall]] - `recall_hydrograph_inputs`
- [[hydrograph_module.f90#res]] - `hyd_output`
- [[hydrograph_module.f90#ru_def]] - `routing_unit_data`
- [[hydrograph_module.f90#ru_elem]] - `routing_unit_elements`
- [[hydrograph_module.f90#ru_seq]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[hydrograph_module.f90#sp_ob1]] - `spatial_objects`
- [[input_file_module.f90#in_con]] - `input_con`
- [[ru_module.f90#iru]] - `integer`
- [[ru_module.f90#ru]] - `ru_parameters`

## File I/O
- **Writes**:
  - [[looping.con]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
