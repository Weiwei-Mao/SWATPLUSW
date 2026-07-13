---
title: object.cnt and SWAT+ object concepts
kind: knowledge
status: partial
created: 2026-07-13
updated: 2026-07-13
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [inputs, object-cnt, objects, routing]
---

# `object.cnt` And SWAT+ Object Concepts

## Summary

`object.cnt` is the basin object inventory file. It tells SWAT+ how many model objects exist by type, so the code can allocate arrays, assign object index ranges, read connection files, and execute the correct object controllers.

It does not define the detailed physical properties or all routing links. Those details are mostly in connection and definition files such as `hru.con`, `rout_unit.con`, `rout_unit.def`, `rout_unit.ele`, `aquifer.con`, `recall.con`, and `chandeg.con`.

## Reader Path

```text
file.cio
    -> in_sim%object_cnt = "object.cnt"
    -> proc_bsn
    -> basin_read_objs
    -> bsn and sp_ob
```

[`basin_read_objs.f90`](../../SWATPLUS/swatplus/src/basin_read_objs.f90) reads:

1. title line;
2. header line;
3. one basin/object-count data line into `bsn` and `sp_ob`.

The `do` wrapper in this reader should not be interpreted as a supported multi-record basin format. The normal file has one active data line. Adding multiple data lines is not a valid way to define multiple basins.

After reading, the routine allocates object arrays:

```fortran
allocate (ob(sp_ob%objs))
allocate (obcs(sp_ob%objs))
allocate (obcs_alloc(sp_ob%objs), source = 0)
allocate (obom(sp_ob%objs))
```

## Field Meaning

| `object.cnt` column | Stored field | Meaning |
| --- | --- | --- |
| `name` | `bsn%name` | Basin/project name. |
| `ls_area` | `bsn%area_ls_ha` | Landscape area, apparently hectares. |
| `tot_area` | `bsn%area_tot_ha` | Total basin area, apparently hectares. |
| `obj` | `sp_ob%objs` | Total number of spatial/command objects. |
| `hru` | `sp_ob%hru` | Number of full HRU objects. |
| `lhru` | `sp_ob%hru_lte` | Number of HRU-LTE objects. |
| `rtu` | `sp_ob%ru` | Number of routing-unit objects. |
| `mfl` | `sp_ob%gwflow` | Number of GWFLOW objects/cells; may be adjusted if GWFLOW is active. |
| `aqu` | `sp_ob%aqu` | Number of aquifer objects. |
| `cha` | `sp_ob%chan` | Number of regular channel objects. |
| `res` | `sp_ob%res` | Number of reservoir objects. |
| `rec` | `sp_ob%recall` | Number of recall objects. |
| `exco` | `sp_ob%exco` | Number of export-coefficient objects. |
| `dlr` | `sp_ob%dr` | Number of delivery-ratio objects. |
| `can` | `sp_ob%canal` | Number of canal objects. |
| `pmp` | `sp_ob%pump` | Number of pump objects. |
| `out` | `sp_ob%outlet` | Number of outlet objects. |
| `lcha` | `sp_ob%chandeg` | Number of SWAT-DEG channel objects. |
| `aqu2d` | `sp_ob%aqu2d` | 2D aquifer count; source marks it not currently used. |
| `hrd` | `sp_ob%herd` | Herd count; source marks it not currently used. |
| `wro` | `sp_ob%wro` | Water-rights count; source marks it not currently used. |

The same `spatial_objects` type is used for both counts (`sp_ob`) and first object indices (`sp_ob1`). In `object.cnt`, these values are counts.

## `Osu_1hru` Object Inventory

The active data line is:

```text
Osu  10  10  4  1  0  1  0  1  0  0  0  0  0  0  0  0  1  0
```

This means:

- basin name: `Osu`;
- landscape area: `10`;
- total area: `10`;
- total objects: `4`;
- active object types:
  - one full HRU;
  - one routing unit;
  - one aquifer;
  - one SWAT-DEG channel.

The simple object graph is:

```text
HRU 1
    -> routing unit 1
        -> SWAT-DEG channel 1
        -> aquifer 1 through recharge
```

## Object Concepts

### `ihru`

`ihru` is not a separate object type. It is a Fortran index variable meaning “current HRU number.” In `command.f90`, when the active object is a full HRU, the code sets:

```fortran
ihru = ob(icmd)%num
call hru_control
```

So `ihru` tells `hru_control` which HRU is being simulated.

### HRU-LTE

HRU-LTE is a simplified/lightweight HRU object. It is selected through the `lhru` count in `object.cnt`, stored as `sp_ob%hru_lte`, read by `hru_lte_read`, and simulated by `hru_lte_control`.

Use this mental model:

```text
full HRU     -> detailed land process path through hru_control
HRU-LTE      -> simplified land process path through hru_lte_control
```

### Routing unit

A routing unit groups one or more landscape elements and combines/routes their outputs before sending them to downstream objects.

It is partly physical and partly computational:

- physical side: it has area, topography/field references, and represents a landscape routing area;
- computational side: it aggregates HRU/HRU-LTE/export-coefficient outputs and applies fractions/delivery ratios.

It is not merely a connection line, but it is also not a physical storage body like a reservoir.

### Recall object

A recall object is an externally supplied hydrograph/load time series. It can represent measured inflow, point-source discharge, upstream boundary flow, diversion, or another manually supplied input.

In `command.f90`, recall objects write their current time-step hydrograph into the object hydrograph array, so downstream objects can receive it like other routed water/load sources.

### Export-coefficient object

An export-coefficient object generates loads from coefficient data instead of a full process simulation. It is useful when a source is represented by average/exported loading behavior rather than detailed HRU process equations.

In routing-unit logic, export-coefficient output can be scaled by area/fraction and routed with other object outputs.

### Delivery-ratio object

A delivery-ratio object modifies incoming flow/load before passing it downstream. Conceptually it represents attenuation, retention, or partial delivery between source and receiving object.

In `command.f90`, the delivery-ratio object applies the configured delivery-ratio data to its incoming hydrograph.

### Regular channel vs canal

A regular channel object represents a natural stream/reach in the drainage network. It routes streamflow and can simulate channel storage, sediment, water quality, and related processes.

A canal object represents managed/artificial water conveyance. It belongs more to water-allocation and diversion behavior, with canal geometry, operation timing, seepage/losses, and groundwater/canal interactions.

Short version:

```text
channel = natural stream network
canal   = artificial managed water-transfer structure
```

### Pump object

A pump object represents water extraction/transfer, especially groundwater pumping or water-allocation pumping. It is a mechanism for moving/removing water, not a storage body.

### Outlet object

An outlet object is a receiving or terminal point in the object graph. It is commonly used where routed water leaves the modeled area or where output is collected.

### SWAT-DEG / `chandeg` / `sdc`

SWAT-DEG channel objects are the active channel-degradation channel type in this scenario. They are counted in `object.cnt` under `lcha`, stored as `sp_ob%chandeg`, referred to as `sdc` in connection files, and defined by `chandeg.con`.

They route channel flow and include sediment/morphology behavior such as bank erosion, bed erosion, deposition, and degradation.

## Debugging Notes

Useful watch variables:

- `sp_ob`: object counts from `object.cnt`;
- `sp_ob1`: first object index for each object type after `hyd_connect`;
- `ob(icmd)%typ`: active object type inside `command`;
- `ob(icmd)%num`: object number within that type;
- `ob(icmd)%obj_out`: downstream object index mapping;
- `ob(icmd)%hd`: current object hydrograph values.

When stepping through `command.f90`, first identify `ob(icmd)%typ`. That tells you which controller is active.

## Evidence

- [`VSProj/SWAT/Osu_1hru/object.cnt`](../../VSProj/SWAT/Osu_1hru/object.cnt): active scenario object counts.
- [`basin_read_objs.f90`](../../SWATPLUS/swatplus/src/basin_read_objs.f90): reader and allocation.
- [`hydrograph_module.f90`](../../SWATPLUS/swatplus/src/hydrograph_module.f90): `type spatial_objects`, `sp_ob`, `sp_ob1`, and object arrays.
- [`hyd_connect.f90`](../../SWATPLUS/swatplus/src/hyd_connect.f90): assigns first object indices and reads connection files by object type.
- [`command.f90`](../../SWATPLUS/swatplus/src/command.f90): dispatches object controllers by `ob(icmd)%typ`.
- [`ru_control.f90`](../../SWATPLUS/swatplus/src/ru_control.f90): routing-unit aggregation and delivery-ratio behavior.
- [`hru_lte_module.f90`](../../SWATPLUS/swatplus/src/hru_lte_module.f90), [`hru_lte_read.f90`](../../SWATPLUS/swatplus/src/hru_lte_read.f90), [`hru_lte_control.f90`](../../SWATPLUS/swatplus/src/hru_lte_control.f90): HRU-LTE data and control path.
- [`sd_channel_module.f90`](../../SWATPLUS/swatplus/src/sd_channel_module.f90), [`sd_channel_control3.f90`](../../SWATPLUS/swatplus/src/sd_channel_control3.f90): SWAT-DEG channel behavior.

## Related Notes

- [`file.cio` master input file](file-cio.md)
- [`codes.bsn` basin control codes](codes-bsn.md)
- [Input to output path](../input-output.md)
