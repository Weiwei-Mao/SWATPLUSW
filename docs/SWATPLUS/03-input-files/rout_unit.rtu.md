---
type: input
tags:
  - swat/input
file: rout_unit.rtu
ext: rtu
cio_field: ru
read_by:
  - ru_read.f90
purpose: "Defines routing-unit parameter records and text pointers to routing-unit definition, delivery-ratio, topography, and field data."
---

# rout_unit.rtu

> [!info] Input File
> Declared in `file.cio` field `ru`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `ru`
- **Reader**: [[ru_read.f90]]
- **Used with**: [[rout_unit.con]], [[rout_unit.def]], [[rout_unit.ele]], and optionally [[rout_unit.dr]]
- **Format style**: SWAT+ text input; list-directed Fortran reads.

`rout_unit.rtu` is the routing-unit parameter/pointer file. It does not define where the routing unit sends water; that is handled by [[rout_unit.con]]. It also does not list the HRUs/elements inside the routing unit; those are handled by [[rout_unit.def]] and [[rout_unit.ele]].

The file gives each routing unit a name and four text pointers:

```text
id  name  define  dlr  topo  field
```

In the code, these four pointer fields are read into `ru(i)%dbsc`, whose type is `ru_databases_char` in [[ru_module.f90]]:

```fortran
character(len=16) :: elem_def
character(len=16) :: elem_dr
character(len=16) :: toposub_db
character(len=16) :: field_db
```

Only `topo` and `field` are resolved directly inside [[ru_read.f90]]. The `define` and `dlr` names are stored in `ru(i)%dbsc%elem_def` and `ru(i)%dbsc%elem_dr`, but the active element membership and per-element delivery ratio are read separately by [[ru_read_elements.f90]] from [[rout_unit.def]] and [[rout_unit.ele]].

## Reader Routines
- [[ru_read.f90]]

## File Structure
- [[ru_read.f90]] source line 40: reads `titldum`
- [[ru_read.f90]] source line 42: reads `header`
- [[ru_read.f90]] source line 45: reads `i` while counting records
- [[ru_read.f90]] source line 220: reads `titldum`
- [[ru_read.f90]] source line 222: reads `header`
- [[ru_read.f90]] source line 227: reads `i`
- [[ru_read.f90]] source line 230: reads `k`, `ru(i)%name`, `ru(i)%dbsc`

The first pass counts the records. The second pass rereads each row and stores it by row `id`:

```fortran
read (107,*,iostat=eof) k, ru(i)%name, ru(i)%dbsc
```

Because `ru(i)%dbsc` is a derived type with four character fields, the input row after `name` must provide exactly these four values in order:

```text
define  dlr  topo  field
```

## Parameters
| Parameter | Type | Units | Meaning | Source | Reader line |
|---|---|---|---|---|---:|
| `id` / `k` | `integer` | none | Routing-unit parameter index. This value indexes `ru(id)`. It should normally match the routing-unit object id used in [[rout_unit.con]]. | `ru_read.f90:24` | [[ru_read.f90]]:230 |
| `name` | `character(len=16)` | none | Routing-unit parameter name stored as `ru(id)%name`. In examples this is often a short name such as `rtu01`. | [[ru_module.f90#ru]] | [[ru_read.f90]]:230 |
| `define` | `character(len=16)` | none | Text pointer stored as `ru(id)%dbsc%elem_def`. It names the routing-unit element definition conceptually, but current membership is actually read from [[rout_unit.def]] by [[ru_read_elements.f90]]. | [[ru_module.f90#ru_databases_char]] | [[ru_read.f90]]:230 |
| `dlr` | `character(len=16)` | none | Text pointer stored as `ru(id)%dbsc%elem_dr`. Current per-element delivery-ratio names are read from the `dlr` column in [[rout_unit.ele]] and xwalked to `dr_db`/`delratio.del`. | [[ru_module.f90#ru_databases_char]] | [[ru_read.f90]]:230 |
| `topo` | `character(len=16)` | none | Name of a topography database record. [[ru_read.f90]] compares this with `topo_db(:)%name`, stores the matched index in `ru(id)%dbs%toposub_db`, and [[time_conc_init.f90]] later uses the matched slope and slope length to compute routing-unit time of concentration. | [[ru_module.f90#ru_databases_char]]; [[topography_data_module.f90#topo_db]] | [[ru_read.f90]]:234 |
| `field` | `character(len=16)` | none | Name of a field database record. [[ru_read.f90]] compares this with `field_db(:)%name`, stores the matched index in `ru(id)%dbs%field_db`, and copies field length, width, and angle into `ru(id)%field`. | [[ru_module.f90#ru_databases_char]]; [[topography_data_module.f90#field_db]] | [[ru_read.f90]]:242 |

## Companion Files

Routing units use several files together:

| File | Reader | Role |
|---|---|---|
| [[rout_unit.con]] | [[hyd_read_connect.f90]] through [[hyd_connect.f90]] | Creates the routing-unit hydrologic object and defines its outgoing routing links after `out_tot`. |
| [[rout_unit.rtu]] | [[ru_read.f90]] | Stores routing-unit names and database pointers. |
| [[rout_unit.ele]] | [[ru_read_elements.f90]] | Lists element records that can be used inside routing units, including `obj_typ`, `obj_id`, element fraction, and delivery-ratio name. |
| [[rout_unit.def]] | [[ru_read_elements.f90]] | Defines which element ids belong to each routing unit. |
| [[rout_unit.dr]] | `file.cio` field `ru_dr` | Routing-unit delivery-ratio support file in the routing-unit file group. |

## Code Use

After [[ru_read.f90]] reads `rout_unit.rtu`, it resolves only two of the four pointer names:

- `topo` -> `ru(id)%dbs%toposub_db`
- `field` -> `ru(id)%dbs%field_db`, plus copied field dimensions in `ru(id)%field`

Then [[time_conc_init.f90]] uses the matched `topo` and `field` records:

- `topo_db(ith)%slope_len` and `topo_db(ith)%slope` are used for overland/channel timing.
- `ru(id)%field%length` is used as channel length in the routing-unit time of concentration calculation.

Membership and delivery-ratio behavior comes from the companion files, not from the `define` and `dlr` fields in this reader:

- [[rout_unit.def]] says which element ids belong to routing unit `id`.
- [[rout_unit.ele]] says what each element is (`hru`, `hlt`, `ru`, `cha`, `res`, `exc`, `dr`, `out`, or `sdc`), the object id, its fraction, and its delivery-ratio name.
- [[dr_ru.f90]] handles delivery-ratio names such as `calc`, `0`, `full`, or `1`; named delivery ratios are xwalked in [[ru_read_elements.f90]] through `dr_db`.

## Example: Osu_1hru

`Osu_1hru` has one routing-unit row:

```text
id  name   define  dlr   topo        field
1   rtu01  rtu001  null  toportu011  fld011
```

Interpretation:

| Field | Value | Meaning |
|---|---|---|
| `id` | `1` | Stores this record in `ru(1)`. |
| `name` | `rtu01` | Routing-unit parameter name. |
| `define` | `rtu001` | Stored in `ru(1)%dbsc%elem_def`; the active member list is in [[rout_unit.def]]. |
| `dlr` | `null` | Stored in `ru(1)%dbsc%elem_dr`; the actual element delivery-ratio value is from [[rout_unit.ele]]. |
| `topo` | `toportu011` | Matched to `topo_db(:)%name` for routing-unit slope/slope length. |
| `field` | `fld011` | Matched to `field_db(:)%name` for routing-unit field/channel length. |

The same example connects the files like this:

```text
rout_unit.rtu:  id 1 uses define name rtu001
rout_unit.def:  routing unit rtu001 contains element 1
rout_unit.ele:  element 1 is hru 1 with frac 1 and dlr 0
rout_unit.con:  routing unit 1 sends total flow to sdc 1 and recharge to aqu 1
```
