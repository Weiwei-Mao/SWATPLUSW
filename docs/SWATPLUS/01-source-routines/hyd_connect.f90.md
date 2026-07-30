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

- Line 63-124, set spatial_object type of this simulation. 
	- defined in [[hydrograph_module.f90#spatial_objects]],
	- Read in [[basin_read_objs.f90]], from file [[object.cnt]]
	- Below is Osu_1hru demo

|        | objs | hru | hru_lte | routing | gwflow | aquifer | chan | reservoir | recall (point sink/source) | export coeff | delivery ratio | canal (None) | pump (None) | outlet | swat-deg | None | None | None |
| ------ | ---- | :-: | :-----: | :-----: | :----: | :-----: | :--: | :-------: | :------------------------: | :----------: | :------------: | :----------: | :---------: | :----: | :------: | :--: | :--: | :--: |
| sp_ob  | 4    |  1  |         |    1    |        |    1    |      |           |                            |              |                |              |             |        |    1     |      |      |      |
| sp_ob1 | 0    |  1  |         |    2    |        |    3    |      |           |                            |              |                |              |             |        |    4     |      |      |      |

- Line 126-129, call [[hyd_read_connect.f90]],read connect file for hrus, [[hru.con]]
	- [[hydrograph_module.f90#hd_tot]], default defined as the table below
	- The function of subroutine [[hyd_read_connect.f90]] is to read [[hydrograph_module.f90#ob]], object connection, ob will read in sequence, ob(1), ob(2)...

| Object type | `hd_tot` value | Hydrograph slot meanings |
| ----------- | -------------- | ------------------------ |
| `hru` | 5 | 1=total; 2=recharge; 3=surface; 4=lateral; 5=tile |
| `hru_lte` | 5 | 1=total; 2=recharge; 3=surface; 4=lateral; 5=tile |
| `ru` | 5 | 1=total; 2=recharge; 3=surface; 4=lateral; 5=tile |
| `gwflow` | 1 | 1=total |
| `aqu` | 2 | 1=return flow; 2=deep perc |
| `chan` | 3 | 1=total; 2=recharge; 3=overbank |
| `res` | 2 | 1=total; 2=recharge |
| `recall` | 1 | 1=total |
| `exco` | 2 | 1=surface; 2=groundwater |
| `dr` | 2 | 1=surface; 2=groundwater |
| `pump` | 1 | 1=total |
| `outlet` | 1 | 1=total |
| `chandeg` | 3 | 1=total; 2=recharge; 3=overbank |
| `aqu2d` | 2 | 1=return flow; 3=deep perc |
| `herd` | 1 | |
| `wro` | 1 | |

- Line 131-134, call [[hyd_read_connect.f90]],read connect file for hru_lte
- Line 136-141, call [[hyd_read_connect.f90]],read connect file for [[rout_unit.con]]
	- out_tot means the number of routing/output connection groups
	- Obj_typ, types of the output, hru/hlt/ru/aqu/cha/res/exc/dr/out/sdc
	- Hyd_typ, 1, tot, total; 2, rhg, recharge; 3, sur, surface runoff; 4, lat, lateral flow; 5, til, tile flow
	- Example of osu_1hru, 100% of routing unit total flow -> swat-deg channel, with id 1
	- 100% of routing unit recharge -> aquifer, with id 1

| obj_typ | obj_id | hyd_typ | frac |
| ------- | ------ | ------- | ---- |
| sdc     | 1      | tot     | 1.0  |
| aqu     | 1      | rhg     | 1.0  |
- Line 139, call [[ru_read.f90]] to read file [[input_file_module.f90#in_ru]] %ru. 
- Line 140, call [[ru_read_elements.f90]] to read file [[rout_unit.ele]] and [[rout_unit.def]]
	- `rout_unit.con`Creates the routing-unit hydrologic object and defines where its output goes.
	- `rout_unit.rtu`Gives routing-unit parameter/database pointers, especially `topo` and `field`.
	- `rout_unit.def`Says which element IDs are inside each routing unit.
	- `rout_unit.ele`Defines each element ID: object type, object id, fraction, delivery ratio.
	- Example from osu_1hr
	- rout_unit.def:  RU 1 contains element 1, routing unit object ID
	- rout_unit.ele:  element 1 = hru 1, frac 1.0,  element ID, based on rout_unit.def
	- rout_unit.rtu:  RU 1 uses topo toportu011 and field fld011, routing unit object ID
	- rout_unit.con:  RU 1 routes total flow to sdc 1, recharge to aqu 1, routing unit object ID
	- *dlr* in element file, it cannot affect flow, but sediment, and other things like N
		- 0/calc, calculate by the model, from hru -> delivery to routing unit, 
		- 1/full, 100%
	- *dlr* in rout_unit.rtu is not used.
- Line 149-153, call [[hyd_read_connect.f90]] to read file [[aquifer.con]]
	- Line 146, call [[aqu2d_read.f90]] to read file [[input_file_module.f90#in_link]] %aqu_cha, if gwflow is available
- Then channels
- Then reservoirs
- Then recalls
- Then export coefficients
- Then delivery ratio, this is separate from *dlr* in routing unit input files
- Then outlets
- Line 181-184, SWAT-deg, read file [[chandeg.con]]
- Then gwflow
- Line 193-213,
	- Before this block: RU 2 knows it contains HRU 9.
	- After this block: HRU 9 also knows it belongs to RU 2. RU 2 has counted HRU 9 as one defining object.
- Line 215-294, 
	- This block translates file routing codes into internal ob() object numbers, counts each receiver's number of incoming connections, and translates hyd_typ text into hydrograph slot number.
- Line 296-354, allocation
- Line 356-403, writes the actual incoming source, hydrograph type, and fraction into each receiver.
- Check all connection, find which object can run first, and avoid loop
- Write calculated and input drainage areas for all objects except hru in file [[area_calc.out]]
- End

<!-- USER-NOTES-END -->
