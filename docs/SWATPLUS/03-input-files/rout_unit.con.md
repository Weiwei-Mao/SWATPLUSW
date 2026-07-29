---
type: input
tags:
  - swat/input
file: rout_unit.con
ext: con
cio_field: ru_con
read_by:
  - hyd_connect.f90
  - hyd_read_connect.f90
purpose: "Defines routing-unit object connectivity, including routing-unit metadata, the rout_unit.rtu pointer, outgoing object links, hydrograph type routed, and routing fractions."
---

# rout_unit.con

> [!info] Input File
> Declared in `file.cio` field `ru_con`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `ru_con`
- **Object count source**: `object.cnt` field `rtu`, stored as `sp_ob%ru`.
- **Reader call**: [[hyd_connect.f90]] calls `hyd_read_connect(in_con%ru_con, "ru      ", sp_ob1%ru, sp_ob%ru, hd_tot%ru, bsn_prm%day_lag_mx)` when `sp_ob%ru > 0`.
- **Companion readers**: immediately after the connect-file read, [[hyd_connect.f90]] calls [[ru_read.f90]] for [[rout_unit.rtu]] and [[ru_read_elements.f90]] for [[rout_unit.def]] and [[rout_unit.ele]].
- **Hydrograph slots**: `hd_tot%ru = 5`, so each routing-unit object allocates total, recharge, surface, lateral, and tile hydrographs.
- **Format style**: SWAT+ text input; list-directed Fortran reads.

`rout_unit.con` creates the active routing-unit object shell and defines where
each routing unit sends its hydrographs. It does not define which HRUs or other
objects are inside the routing unit; membership is read from [[rout_unit.def]]
and [[rout_unit.ele]]. It also does not define the routing-unit topography or
field parameters; the `rtu` column points to the matching row in
[[rout_unit.rtu]], which then points to [[topography.hyd]] and [[field.fld]].

## Reader Routines
- [[hyd_connect.f90]] assigns the global `ob()` object-number range for routing units, then dispatches the common connect-file reader.
- [[hyd_read_connect.f90]] opens `rout_unit.con`, skips the title and header lines, reads one row for each active routing unit, allocates object hydrograph arrays, and stores outgoing routing groups in `ob(i)%*_out` arrays.
- [[hyd_connect.f90]] later resolves each `obj_typ`/`obj_id` group to a global receiving object number and converts `hyd_typ` to an integer hydrograph slot.

## File Structure
1. Title/comment line: read and ignored as `titldum`.
2. Header line: read and ignored as `header`.
3. Routing-unit data rows: one row for each routing unit counted by `object.cnt` field `rtu`.

Rows with no outflow groups use this structure:

```text
id name gis_id area lat lon elev rtu wst cst ovfl rule out_tot
```

Rows with one or more outflow groups append four fields per outflow:

```text
id name gis_id area lat lon elev rtu wst cst ovfl rule out_tot (obj_typ obj_id hyd_typ frac)...
```

The number of appended `(obj_typ obj_id hyd_typ frac)` groups must equal
`out_tot`.

## Parameters
| Column | Fortran target | Meaning |
| ------ | -------------- | ------- |
| `id` | `ob(i)%num` | Routing-unit object number from the connect file. This should normally match the local routing-unit number and the related [[rout_unit.rtu]] row. |
| `name` | `ob(i)%name` | Routing-unit object name. |
| `gis_id` | `ob(i)%gis_id` | GIS identifier. |
| `area` | `ob(i)%area_ha` | Routing-unit area in hectares; also initializes `ob(i)%area_ha_calc` for routing units. |
| `lat` | `ob(i)%lat` | Latitude. |
| `lon` | `ob(i)%long` | Longitude. |
| `elev` | `ob(i)%elev` | Elevation. |
| `rtu` | `ob(i)%props` | Routing-unit property pointer. In normal projects this points to the same local routing-unit record in [[rout_unit.rtu]]. |
| `wst` | `ob(i)%wst_c` | Weather station name; later crosswalked to `ob(i)%wst` by `search(wst_n, db_mx%wst, ob(i)%wst_c, ob(i)%wst)`. |
| `cst` | `ob(i)%constit` | Constituent data pointer for pesticides, pathogens, metals, salts, and custom constituents. |
| `ovfl` | `ob(i)%props2` | Secondary generic property pointer. For routing units this is stored by the common reader; companion RU membership is still controlled by [[rout_unit.def]] and [[rout_unit.ele]]. |
| `rule` | `ob(i)%ruleset` | Flow-control decision-table/ruleset name when used. |
| `out_tot` | `ob(i)%src_tot` | Number of outgoing routing groups on this row. |
| `obj_typ` | `ob(i)%obtyp_out(isp)` | Receiving object type code for outgoing group `isp`. |
| `obj_id` | `ob(i)%obtypno_out(isp)` | Receiving object number within `obj_typ`. |
| `hyd_typ` | `ob(i)%htyp_out(isp)` | Hydrograph type routed to the receiving object. |
| `frac` | `ob(i)%frac_out(isp)` | Fraction of the selected hydrograph routed to this receiving object. Fractions are applied to each listed `hyd_typ`, so a row can route different hydrograph types with `frac = 1.0` in separate groups. |

## Routing Codes
`obj_typ` is resolved later in [[hyd_connect.f90]] to a global `ob()` index.

| `obj_typ` | Receiving object |
| --------- | ---------------- |
| `hru` | HRU |
| `hlt` | HRU-LTE |
| `ru` | Routing unit |
| `gwflow` | GWFLOW object |
| `aqu` | Aquifer |
| `cha` | Channel |
| `res` | Reservoir |
| `exc` | Export coefficient object |
| `dr` | Delivery ratio object |
| `out` | Outlet |
| `sdc` | SWAT-deg channel |

`hyd_typ` is converted to an integer hydrograph slot in [[hyd_connect.f90]].

| `hyd_typ` | Slot | Routing-unit hydrograph meaning |
| --------- | ---- | ------------------------------- |
| `tot` | 1 | Total flow |
| `rhg` | 2 | Recharge |
| `sur` | 3 | Surface runoff |
| `lat` | 4 | Lateral flow |
| `til` | 5 | Tile flow |

## Companion Files
Routing units are split across one connect file and three routing-unit files:

| File | Reader | Role |
| ---- | ------ | ---- |
| [[rout_unit.con]] | [[hyd_read_connect.f90]] through [[hyd_connect.f90]] | Creates active routing-unit objects and stores outgoing links after `out_tot`. |
| [[rout_unit.rtu]] | [[ru_read.f90]] | Stores routing-unit names and database pointers for definition name, delivery-ratio name, topography, and field data. |
| [[rout_unit.def]] | [[ru_read_elements.f90]] | Defines which element ids belong to each routing unit. |
| [[rout_unit.ele]] | [[ru_read_elements.f90]] | Defines each element id as an object reference, fraction, and delivery-ratio name. |

Important alignment rule: in this source branch [[rout_unit.rtu]] fills `ru(:)`
by local routing-unit number rather than through a separate property database
array. Keep the `rout_unit.con` `id`/`rtu` value aligned with the
corresponding [[rout_unit.rtu]] row.

## Demo Examples
### Ames_sub1

`Ames_sub1` is the no-routing-unit example. In both
`VSProj/SWAT/Ames_sub1` and `SWATPLUS/swatplus/refdata/Ames_sub1`:

```text
object.cnt: rtu = 0
file.cio connect row:      hru.con null null ...
file.cio routing_unit row: null null null null
```

Because `sp_ob%ru = 0`, [[hyd_connect.f90]] does not call the routing-unit
connect reader, and the demo has no `rout_unit.con`, `rout_unit.rtu`,
`rout_unit.def`, or `rout_unit.ele` input files. Use this demo when tracing a
project that routes directly through HRUs without an RU aggregation layer.

### Osu_1hru

`Osu_1hru` is the one-routing-unit example. In both
`VSProj/SWAT/Osu_1hru` and `SWATPLUS/swatplus/refdata/Osu_1hru`:

```text
object.cnt: rtu = 1
file.cio connect row:      ... rout_unit.con ...
file.cio routing_unit row: rout_unit.def rout_unit.ele rout_unit.rtu null
```

Its `rout_unit.con` row is:

```text
id name   gis_id area lat      lon       elev      rtu wst              cst ovfl rule out_tot obj_typ obj_id hyd_typ frac    obj_typ obj_id hyd_typ frac
1  rtu001 1      10   35.52014 127.32787 113.51276 1   s35610n127290e  0   0    0    2       sdc     1      tot     1.00000 aqu     1      rhg     1.00000
```

Interpretation:

| Field/group | Value | Meaning |
| ----------- | ----- | ------- |
| `id` / `name` | `1` / `rtu001` | Creates routing-unit object 1. |
| `area` | `10.0000` | Routing-unit area is 10 ha and initializes calculated area for this RU. |
| `rtu` | `1` | Points to local [[rout_unit.rtu]] row 1, where `rtu01` points to `rtu001`, `toportu011`, and `fld011`. |
| `wst` | `s35610n127290e` | Weather station name used by the common object shell. |
| `cst`, `ovfl`, `rule` | `0`, `0`, `0` | No constituent pointer, secondary pointer, or flow-control rule is active. |
| `out_tot` | `2` | Two outgoing hydrograph groups follow. |
| group 1 | `sdc 1 tot 1.00000` | Route 100 percent of total RU flow to SWAT-deg channel 1. |
| group 2 | `aqu 1 rhg 1.00000` | Route 100 percent of RU recharge to aquifer 1. |

The companion files complete the RU definition:

```text
rout_unit.rtu: id 1 uses define name rtu001
rout_unit.def: routing unit rtu001 contains element 1
rout_unit.ele: element 1 is hru 1 with frac 1 and dlr 0
```
