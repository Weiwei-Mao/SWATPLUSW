---
title: om_water.ini initial organic-mineral water state
kind: input-reference
status: partial
created: 2026-07-14
updated: 2026-07-15
source_revision: 5b3705b300d95ebe4914119f056548446bdc208f
scenario: Osu_1hru
tags: [inputs, initialization, water-quality, channels, wetlands]
---

# `om_water.ini` Initial Organic-Mineral Water State

## Summary

`om_water.ini` defines named initial organic-mineral water states. It is read once during model initialization by `om_water_init.f90`.

This file does not define object connections, routing, or process equations. It is a small database of named starting conditions. Other initialization files point to one of these names when a channel, reservoir, wetland, or similar water-storage object needs an initial water-quality state.

For the `Osu_1hru` debug scenario, `om_water.ini` contains one all-zero record named `no_init`. That name is referenced by `initial.cha`, so the channel initialization can resolve its `org_min` field without an unresolved-name error.

## Where It Is Selected

`file.cio` selects the file in the `init` section:

```text
init              plant.ini         soil_plant.ini    om_water.ini ...
```

The filename is stored in:

```fortran
in_init%om_water
```

The reader is:

```text
SWATPLUS/swatplus/src/om_water_init.f90
```

The routine is called early from `main.f90.in`, before the main simulation loop.

## Format

The file has:

```text
title/comment line
header line
record_1
record_2
...
```

Each data record has a name followed by values matching the `hyd_output` type:

```text
name  flo  sed  orgn  sedp  no3  solp  chl_a  nh3  no2  cbn_bod  dis_ox  san  sil  cla  sag  lag  grv  tmp
```

The `Osu_1hru` file:

```text
name                       flo           sed          orgn          sedp           no3          solp         chl_a           nh3           no2       cbn_bod        dis_ox           san           sil           cla           sag           lag           grv           tmp             c
no_init                0.00000       0.00000       0.00000       0.00000       0.00000       0.00000       0.00000       0.00000       0.00000       0.00000       0.00000       0.00000       0.00000       0.00000       0.00000       0.00000       0.00000       0.00000       0.00000
```

The trailing `c` header in this scenario appears to be extra text. The reader reads the data line into `om_init_name(ichi), om_init_water(ichi)`, where `om_init_water` is a `hyd_output` value. The active `hyd_output` fields end at `temp`.

## Column Meaning

These fields come from `type hyd_output` in `hydrograph_module.f90`.

| Column | Meaning | Unit in code |
| --- | --- | --- |
| `name` | Name used by other init files to select this record. | text |
| `flo` | Initial water volume. | `m^3` |
| `sed` | Sediment. | metric tons |
| `orgn` | Organic nitrogen. | kg N |
| `sedp` | Organic phosphorus attached to sediment. | kg P |
| `no3` | Nitrate nitrogen. | kg N |
| `solp` | Mineral/soluble phosphorus. | kg P |
| `chl_a` | Chlorophyll-a. | kg |
| `nh3` | Ammonia nitrogen. | kg N |
| `no2` | Nitrite nitrogen. | kg N |
| `cbn_bod` | Carbonaceous biochemical oxygen demand. | kg |
| `dis_ox` | Dissolved oxygen. | kg |
| `san` | Detached sand. | tons |
| `sil` | Detached silt. | tons |
| `cla` | Detached clay. | tons |
| `sag` | Detached small aggregates. | tons |
| `lag` | Detached large aggregates. | tons |
| `grv` | Gravel. | tons |
| `tmp` | Water temperature. | degrees C |

## Reader Behavior

`om_water_init.f90` checks whether `in_init%om_water` exists and is not `"null"`.

If the file is missing or set to `"null"`:

```fortran
allocate (om_init_water(0:0))
allocate (om_init_name(0:0))
```

If the file exists:

1. The routine counts the number of data records.
2. It stores that count in `db_mx%om_water_init`.
3. It allocates:

   ```fortran
   om_init_water(0:imax)
   om_init_name(0:imax)
   ```

4. It reads each record:

   ```fortran
   read (105,*,iostat=eof) om_init_name(ichi), om_init_water(ichi)
   ```

## How Other Files Use It

Other initialization files do not copy all the numeric columns directly. They usually store a name such as `no_init`, then the model crosswalks that name to a record number in `om_init_name`.

For the `Osu_1hru` scenario:

```text
initial.cha
name       org_min
initcha1   no_init
```

During channel reading, the model matches:

```fortran
ch_init(isp_ini)%org_min == om_init_name(ics)
```

and stores the selected index:

```fortran
sd_init(isp_ini)%org_min = ics
```

Later, SWAT-DEG channel initialization copies the selected state:

```fortran
tot_stor(ich) = om_init_water(iom_ini)
```

Wetland initialization follows the same general pattern:

```fortran
wet(iihru) = om_init_water(init_om)
```

## Debugging Interpretation

For a normal small scenario, `om_water.ini` is often a zero/default lookup table. Its practical role is to let other init files say:

```text
use this named initial organic-mineral water condition
```

For `Osu_1hru`, `no_init` means:

```text
start channel organic-mineral water state from zero/default values
```

If a channel, reservoir, or wetland references a name that is not present in `om_water.ini`, the relevant crosswalk may remain zero or write a warning depending on the object reader. That can lead to default initialization rather than the intended water-quality state.

## Current Trace Status

Verified:

- `file.cio` selects `om_water.ini` through the `init` section.
- `om_water_init.f90` reads names and `hyd_output` values into `om_init_name` and `om_init_water`.
- `initial.cha` in `Osu_1hru` references `no_init`.
- SWAT-DEG channel initialization can copy `om_init_water(iom_ini)` into channel storage.

Still partial:

- Reservoir and aquifer behavior should be traced separately for a scenario that actually activates those objects.
- The exact output signal affected by nonzero `om_water.ini` values still needs a controlled test.
