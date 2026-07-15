---
title: QSWAT+ HRU and routing-unit relationship
kind: knowledge
status: partial
created: 2026-07-13
updated: 2026-07-13
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Robin
tags: [qswat, hru, routing-unit, connections, gis-routing]
---

# QSWAT+ HRU And Routing-Unit Relationship

## Summary

In the Robin project generated from the QSWAT+ workflow, each HRU is effectively wrapped by one routing unit.

The practical model is:

```text
HRU
    -> routing-unit element
    -> routing unit
    -> downstream channel / routing unit / aquifer
```

This is a generated-input convention, not a hard limitation of the SWAT+ Fortran engine. The engine can read routing units with one or more elements, but the Robin/QSWAT-generated input uses one HRU element per routing unit.

## Important Correction

Do not read this as:

```text
hru.con line N == rout_unit.con line N
```

That is not always true.

The exact bridge is:

```text
hru.con
    -> HRU id
gis_hrus
    -> HRU id belongs to LSU id
rout_unit_con
    -> routing unit with gis_id = LSU id
rout_unit.def
    -> routing unit id contains element id
rout_unit.ele
    -> element id is obj_typ = hru, obj_id = HRU id
rout_unit.con
    -> routing-unit output destinations and fractions
```

So the stable reading path is:

```text
hru.con
    -> rout_unit.ele
    -> rout_unit.def
    -> rout_unit.con
```

## Robin Example

From `D:\test\Robin\Scenarios\Default\TxtInOut`:

- `hru.con` has 173 HRUs.
- `rout_unit.con` has 173 routing units.
- `rout_unit.ele` has 173 elements.
- `hru.con` rows have `out_tot = 0`, so the HRUs do not directly define downstream routing in `hru.con`.

The routing is moved to the routing-unit files.

Example:

```text
hru.con:
  hru009

Robin.sqlite / gis_hrus:
  hru 9 belongs to lsu 12

rout_unit.con:
  rtu012 has gis_id 12

rout_unit.def:
  rtu012 uses element 9

rout_unit.ele:
  element 9 = hru009
```

Therefore:

```text
rtu012 is the routing unit that carries hru009.
```

But `rout_unit.con` row 2 is `rtu012`, which corresponds to `hru009`, not `hru002`.

The same local pair also shows the relationship between `hru009`, `hru010`, `rtu012`, and `rtu011`:

```text
hru009 is contained in rtu012.
hru010 is contained in rtu011.

rtu012 routes part of its output to rtu011.
```

The useful diagram is:

```text
hru009
  |
  v
rtu012 ---- surface 17%, lateral 100% ----> rtu011
                                             ^
                                             |
                                          hru010
```

A compact version is:

```text
hru009 -> rtu012 -> rtu011
hru010 -----------> rtu011
```

However, the arrows do not all mean the same thing:

- `hru009 -> rtu012` means `hru009` is an element/member of `rtu012`.
- `hru010 -> rtu011` means `hru010` is an element/member of `rtu011`.
- `rtu012 -> rtu011` means water/load is routed from `rtu012` to `rtu011`.

So for Robin, it is acceptable to say HRUs and routing units correspond one-to-one, but the correspondence is membership/wrapping, not direct downstream flow.

## What `rout_unit.con` Means In This Pattern

`rout_unit.con` tells where the routing unit sends different hydrograph components.

For Robin:

```text
rtu012:
  sdc 1 sur 0.83
  ru  1 sur 0.17
  ru  1 lat 1.00
  aqu 2 rhg 1.00
```

This means:

- the routing unit containing `hru009` sends 83% of surface runoff to SWAT-DEG channel 1;
- it sends 17% of surface runoff to routing unit 1;
- it sends 100% of lateral flow to routing unit 1;
- it sends 100% of recharge to aquifer 2.

The downstream routing unit 1 is `rtu011`, which contains `hru010`.

So for learning, we can say:

```text
hru009 is routed through rtu012.
rtu012 sends part of its output to rtu011.
rtu011 contains hru010.
```

This is clearer than saying directly that `hru009` routes to `hru010`, because the actual SWAT+ connection is routing-unit to routing-unit.

## QSWAT+ Code Evidence

The QSWAT+ plugin path checked was:

```text
C:\Users\wei.mao\AppData\Roaming\QGIS\QGIS4\profiles\default\python\plugins\QSWATPlus
```

Relevant files:

- `QSWATPlus/hrus.py`
- `QSWATPlus/DBUtils.py`
- `QSWATPlus/QSWATTopology.py`

QSWAT+ creates GIS/project database tables, especially:

- `gis_hrus`
- `gis_lsus`
- `gis_routing`

In `DBUtils.py`, `gis_hrus` stores each HRU with an `lsu` field. In `hrus.py`, QSWAT+ inserts HRUs into `gis_hrus` and writes routing relationships into `gis_routing`.

The QSWAT+ flow types are defined in `QSWATTopology.py`:

```text
tot = total hydrograph
rhg = recharge
sur = surface runoff
lat = lateral flow
til = tile flow
```

Inside `hrus.py`, QSWAT+ writes LSU routing such as:

```text
LSU -> channel / water body / downstream LSU
LSU -> aquifer through recharge
```

It also writes HRU routing into `gis_routing`, but the final Robin TxtInOut does not use `hru.con` outputs. Instead, the exported connection structure puts the active routing in `rout_unit.con`.

## Writer Boundary

The exact strings `hru.con` and `rout_unit.con` were not found in the local QSWAT+ plugin code path. The exported Robin files say:

```text
written by SWAT+ editor v4.0.0
```

So the safest statement is:

```text
QSWAT+ builds the project GIS/HRU/routing database.
SWAT+ Editor exports that database into TxtInOut files such as hru.con, rout_unit.def, rout_unit.ele, and rout_unit.con.
```

The one-HRU-per-routing-unit structure is still a result of this QSWAT+/Editor generated workflow.

## Debugging Guidance

When debugging a QSWAT-generated project, do not stop at `hru.con`.

Use this checklist:

1. Find the HRU row in `hru.con`.
2. Confirm `out_tot`.
   - If `out_tot = 0`, the HRU is not directly routing from `hru.con`.
3. Find the HRU id in `rout_unit.ele`.
4. Use the element id in `rout_unit.def` to find the routing unit.
5. Use that routing unit id in `rout_unit.con` to understand where the water goes.
6. If needed, compare against `gis_hrus.lsu` and `rout_unit_con.gis_id` in the project SQLite database.

For Robin, the SQLite check showed:

```text
gis_hrus.lsu == rout_unit_con.gis_id
```

for all HRUs.

## Mental Model To Keep

For the Robin/QSWAT-generated input:

```text
HRU calculates land-phase water and loads.
Each HRU is wrapped by one routing unit in this generated project.
Routing unit owns the connection logic.
Aquifer receives recharge from routing units.
SWAT-DEG channel receives routed surface/total flow from routing units.
```

For general SWAT+ source code:

```text
Routing units are flexible object aggregators.
They are not required by the Fortran engine to contain exactly one HRU.
```

## Evidence

- `D:\test\Robin\Scenarios\Default\TxtInOut\hru.con`
- `D:\test\Robin\Scenarios\Default\TxtInOut\rout_unit.con`
- `D:\test\Robin\Scenarios\Default\TxtInOut\rout_unit.def`
- `D:\test\Robin\Scenarios\Default\TxtInOut\rout_unit.ele`
- `D:\test\Robin\Robin.sqlite`
- `C:\Users\wei.mao\AppData\Roaming\QGIS\QGIS4\profiles\default\python\plugins\QSWATPlus\QSWATPlus\hrus.py`
- `C:\Users\wei.mao\AppData\Roaming\QGIS\QGIS4\profiles\default\python\plugins\QSWATPlus\QSWATPlus\DBUtils.py`
- `C:\Users\wei.mao\AppData\Roaming\QGIS\QGIS4\profiles\default\python\plugins\QSWATPlus\QSWATPlus\QSWATTopology.py`
- [`ru_read_elements.f90`](../../SWATPLUS/swatplus/src/ru_read_elements.f90): SWAT+ engine can resolve routing-unit elements of several object types.
- [`hyd_read_connect.f90`](../../SWATPLUS/swatplus/src/hyd_read_connect.f90): reads connection outputs such as object type, object id, hydrograph type, and fraction.

## Related Notes

- [`object.cnt` and SWAT+ object concepts](../inputs/simulation/object-cnt.md)
- [Input to output path](../tracing-guide.md)
