---
type: input
tags:
  - swat/input
file: hru.con
ext: con
cio_field: hru_con
read_by:
  - hyd_connect.f90
  - hyd_read_connect.f90
purpose: "Defines HRU object connectivity, including HRU metadata, receiving objects, hydrograph type routed, and routing fractions."
---

# hru.con

> [!info] Input File
> Declared in `file.cio` field `hru_con`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `hru_con`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.
- **Reader call**: `hyd_connect` calls `hyd_read_connect(in_con%hru_con, "hru     ", sp_ob1%hru, sp_ob%hru, hd_tot%hru, bsn_prm%day_lag_mx)` when `sp_ob%hru > 0`.
- **Object count**: the expected number of HRU rows is `sp_ob%hru`, read from [[object.cnt]].
- **Hydrograph slots**: `hd_tot%hru = 5`, so each HRU object allocates `ob(i)%hd(1:5)` for total, recharge, surface, lateral, and tile hydrographs.

## Reader Routines
- [[hyd_connect.f90]] dispatches the HRU connectivity reader using `in_con%hru_con`.
- [[hyd_read_connect.f90]] opens the file, skips the title and header lines, reads one HRU row per object, allocates object hydrograph arrays, and stores routing targets in `ob(i)%*_out` arrays.

## File Structure
1. Title/comment line: read and ignored as `titldum`.
2. Header line: read and ignored as `header`.
3. HRU data rows: one row for each HRU object.

Rows with no outflow groups use this structure:

```text
id name gis_id area lat lon elev hru wst cst ovfl rule out_tot
```

Rows with one or more outflow groups append four fields per outflow:

```text
id name gis_id area lat lon elev hru wst cst ovfl rule out_tot (obj_typ obj_id hyd_typ frac)...
```

The number of appended `(obj_typ obj_id hyd_typ frac)` groups must equal `out_tot`.

## Parameters
| Column | Fortran target | Meaning |
| ------ | -------------- | ------- |
| `id` | `ob(i)%num` | HRU object number from the connect file. |
| `name` | `ob(i)%name` | HRU object name. |
| `gis_id` | `ob(i)%gis_id` | GIS identifier. |
| `area` | `ob(i)%area_ha` | HRU area in hectares; also initializes `ob(i)%area_ha_calc` for HRUs. |
| `lat` | `ob(i)%lat` | Latitude. |
| `lon` | `ob(i)%long` | Longitude. |
| `elev` | `ob(i)%elev` | Elevation. |
| `hru` | `ob(i)%props` | HRU property/data pointer. |
| `wst` | `ob(i)%wst_c` | Weather station name; later crosswalked to `ob(i)%wst` by `search(wst_n, db_mx%wst, ob(i)%wst_c, ob(i)%wst)`. |
| `cst` | `ob(i)%constit` | Constituent data pointer. |
| `ovfl` | `ob(i)%props2` | Overbank/connectivity pointer. |
| `rule` | `ob(i)%ruleset` | Flow decision-table/ruleset name when used. |
| `out_tot` | `ob(i)%src_tot` | Number of outflow routing groups on this row. |
| `obj_typ` | `ob(i)%obtyp_out(isp)` | Receiving object type code for outflow group `isp`. |
| `obj_id` | `ob(i)%obtypno_out(isp)` | Receiving object number within `obj_typ`. |
| `hyd_typ` | `ob(i)%htyp_out(isp)` | Hydrograph type routed to the receiving object. |
| `frac` | `ob(i)%frac_out(isp)` | Fraction of the selected hydrograph routed to this receiving object. |

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

| `hyd_typ` | Slot | HRU hydrograph meaning |
| --------- | ---- | --------------------- |
| `tot` | 1 | Total flow |
| `rhg` | 2 | Recharge |
| `sur` | 3 | Surface runoff |
| `lat` | 4 | Lateral flow |
| `til` | 5 | Tile flow |

## Example
From the `Osu_1hru` reference data:

```text
id name    gis_id area lat      lon       elev      hru wst              cst ovfl rule out_tot
1  hru0001 1      10   35.65311 127.36763 350.96629 1   s35610n127290e  0   0    0    0
```

This row defines one HRU object with no direct outflow groups in `hru.con`; downstream routing is handled by other connect files and object relationships for that example.
