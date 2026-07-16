---
type: module
tags:
  - swat/module
  - swat/to-read
file: mgt_operations_module.f90
note_file: mgt_operations_module.f90
module_name: mgt_operations_module
defines_types:
  - irrigation_operation
  - puddle_operation
  - filtstrip_operation
  - fire_operation
  - grwaterway_operation
  - bmpuser_operation
  - bmpuser_operation1
  - chemical_application_operation
  - harvest_operation
  - grazing_operation
  - streetsweep_operation
  - management_ops
  - management_schedule
defines_vars:
  - irrop_db
  - pudl_db
  - filtstrip_db
  - fire_db
  - grwaterway_db
  - bmpuser_db
  - chemapp_db
  - harvop_db
  - harvop
  - hkop
  - grazeop_db
  - graze
  - sweepop_db
  - sweepop
  - mgt
  - mgt1
  - mgt2
  - sched
defines_subroutines: []
defines_functions: []
defines_procedures: []
purpose: ""
---

# mgt_operations_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### irrigation_operation

- **Defined in source**: `mgt_operations_module.f90:5`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=40)` | 6 |  |
| `amt_mm` | `real` | 7 | mm \|irrigation application amount |
| `eff` | `real` | 8 | \|irrigation in-field efficiency |
| `surq` | `real` | 9 | frac \|surface runoff ratio |
| `dep_mm` | `real` | 10 | mm \|depth of application for subsurface irrigation |
| `salt` | `real` | 11 | mg/kg \|concentration of total salt in irrigation |
| `no3` | `real` | 12 | mg/kg \|concentration of nitrate in irrigation |
| `po4` | `real` | 13 | mg/kg \|concentration of phosphate in irrigation |

### puddle_operation

- **Defined in source**: `mgt_operations_module.f90:17`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=40)` | 18 |  |
| `wet_hc` | `real` | 19 | mm/h \|hydraulic conductivity of upper layer of soil after puddling |
| `sed` | `real` | 20 | ppm \|sediment concentration after puddling |
| `orgn` | `real` | 21 | ppm \|organic N concentration after puddling |
| `sedp` | `real` | 22 | ppm \|organic P concentration after puddling |
| `no3` | `real` | 23 | ppm \|NO3-N concentration after puddling |
| `solp` | `real` | 24 | ppm \|mineral (soluble P) concentration after puddling |
| `nh3` | `real` | 25 | ppm \|NH3 concentration after puddling |
| `no2` | `real` | 26 | ppm \|NO2 concentration after puddling |

### filtstrip_operation

- **Defined in source**: `mgt_operations_module.f90:30`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=40)` | 31 |  |
| `vfsi` | `integer` | 32 | \|on/off flag for vegetative filter strip |
| `vfsratio` | `real` | 33 | \|contouring USLE P factor |
| `vfscon` | `real` | 34 | \|fraction of the total runoff from the entire field |
| `vfsch` | `real` | 35 | \|fraction of flow entering the most concentrated 10% of the VFS. which is fully channelized |

### fire_operation

- **Defined in source**: `mgt_operations_module.f90:40`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=40)` | 41 |  |
| `cn2_upd` | `real` | 42 | \|change in SCS curve number II value |
| `fr_burn` | `real` | 43 | \|fraction burned |

### grwaterway_operation

- **Defined in source**: `mgt_operations_module.f90:47`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=40)` | 48 |  |
| `grwat_i` | `integer` | 49 | none \|On/off Flag for waterway simulation |
| `grwat_n` | `real` | 50 | none \|Mannings"s n for grassed waterway |
| `grwat_spcon` | `real` | 51 | none \|sediment transport coefficant defined by user |
| `grwat_d` | `real` | 52 | m \|depth of Grassed waterway |
| `grwat_w` | `real` | 53 | none \|width of grass waterway |
| `grwat_l` | `real` | 54 | km \|length of Grass Waterway |
| `grwat_s` | `real` | 55 | m/m \|slope of grass waterway |

### bmpuser_operation

- **Defined in source**: `mgt_operations_module.f90:59`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=40)` | 60 |  |
| `bmp_flag` | `integer` | 61 |  |
| `bmp_sed` | `real` | 62 | % \| Sediment removal by BMP |
| `bmp_pp` | `real` | 63 | % \| Particulate P removal by BMP |
| `bmp_sp` | `real` | 64 | % \| Soluble P removal by BMP |
| `bmp_pn` | `real` | 65 | % \| Particulate N removal by BMP |
| `bmp_sn` | `real` | 66 | % \| Soluble N removal by BMP |
| `bmp_bac` | `real` | 67 | % \| Bacteria removal by BMP |

### bmpuser_operation1

- **Defined in source**: `mgt_operations_module.f90:70`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=40)` | 71 |  |
| `bmp_flag` | `integer` | 72 |  |
| `surf_flo` | `real` | 73 | % \| Surface Flow removal by BMP |
| `surf_sed` | `real` | 74 | % \| Surface Sediment removal by BMP |
| `surf_pp` | `real` | 75 | % \| Surface Particulate P removal by BMP |
| `surf_sp` | `real` | 76 | % \| Surface Soluble P removal by BMP |
| `surf_pn` | `real` | 77 | % \| Surface Particulate N removal by BMP |
| `surf_sn` | `real` | 78 | % \| Surface Soluble N removal by BMP |
| `surf_bac` | `real` | 79 | % \| Surface Bacteria removal by BMP |
| `sub_flo` | `real` | 80 | % \| Subsurface Flow removal by BMP |
| `sub_sed` | `real` | 81 | % \| Subsurface Sediment removal by BMP |
| `sub_pp` | `real` | 82 | % \| Subsurface Particulate P removal by BMP |
| `sub_sp` | `real` | 83 | % \| Subsurface Soluble P removal by BMP |
| `sub_pn` | `real` | 84 | % \| Subsurface Particulate N removal by BMP |
| `sub_sn` | `real` | 85 | % \| Subsurface Soluble N removal by BMP |
| `sub_bac` | `real` | 86 | % \| Subsurface Bacteria removal by BMP |
| `tile_flo` | `real` | 87 | % \| Tile Flow removal by BMP |
| `tile_sed` | `real` | 88 | % \| Tile Sediment removal by BMP |
| `tile_pp` | `real` | 89 | % \| Tile Particulate P removal by BMP |
| `tile_sp` | `real` | 90 | % \| Tile Soluble P removal by BMP |
| `tile_pn` | `real` | 91 | % \| Tile Particulate N removal by BMP |
| `tile_sn` | `real` | 92 | % \| Tile Soluble N removal by BMP |
| `tile_bac` | `real` | 93 | % \| Tile Bacteria removal by BMP |

### chemical_application_operation

- **Defined in source**: `mgt_operations_module.f90:97`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=40)` | 98 |  |
| `form` | `character (len=40)` | 99 | \|solid; liquid |
| `op_typ` | `character (len=40)` | 100 | \|operation type-spread; spray; inject; direct |
| `app_eff` | `real` | 101 | \|application efficiency |
| `foliar_eff` | `real` | 102 | \|foliar efficiency |
| `inject_dep` | `real` | 103 | mm \|injection depth |
| `surf_frac` | `real` | 104 | \|surface fraction-amount in upper 10 mm |
| `drift_pot` | `real` | 105 | \|drift potential |
| `aerial_unif` | `real` | 106 | \|aerial uniformity |

### harvest_operation

- **Defined in source**: `mgt_operations_module.f90:110`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=40)` | 111 |  |
| `typ` | `character (len=40)` | 112 | none \|grain;biomass;residue;tree;tuber |
| `hi_ovr` | `real` | 113 | (kg/ha)/(kg/ha) \|harvest index target specified at harvest |
| `eff` | `real` | 114 | none \|harvest efficiency: fraction of harvested yield that is removed the remainder becomes residue on the soil surface |
| `bm_min` | `real` | 116 | kg/ha \|minimum biomass to allow harvest |

### grazing_operation

- **Defined in source**: `mgt_operations_module.f90:122`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=40)` | 123 |  |
| `fertnm` | `character (len=40)` | 124 |  |
| `manure_id` | `integer` | 125 | fertilizer number from fertilizer.frt |
| `eat` | `real` | 126 | (kg/ha)/day \|dry weight of biomass removed by grazing daily |
| `tramp` | `real` | 127 | (kg/ha)/day \|dry weight of biomass removed by trampling daily |
| `manure` | `real` | 128 | (kg/ha)/day \|dry weight of manure deposited |
| `biomin` | `real` | 129 | kg/ha \|minimum plant biomass for grazing |

### streetsweep_operation

- **Defined in source**: `mgt_operations_module.f90:134`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=40)` | 135 |  |
| `eff` | `real` | 136 | none \|removal efficiency of sweeping operation |
| `fr_curb` | `real` | 137 | none \|availability factor, the fraction of the curb length that is sweepable |

### management_ops

- **Defined in source**: `mgt_operations_module.f90:143`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 144 |  |
| `op` | `character(len=40)` | 145 | operation code 4-digit char name plnt; autoplnt - plant harv; autoharv - harvest only kill; autokill - kill hvkl; autohk - harvest and kill till; autotill - tillage irr; autoirr - irrigation fert; autofert - fertlizer pest; pestauto - pesticide application graz; autograz - grazing burn; autoburn - burn swep; autoswep - street sweep prtp - print plant vars skip - skip to end of the year |
| `mon` | `integer` | 160 |  |
| `day` | `integer` | 161 |  |
| `jday` | `integer` | 162 |  |
| `year` | `integer` | 163 |  |
| `husc` | `real` | 164 |  |
| `op_char` | `character(len=40)` | 165 |  |
| `op_plant` | `character (len=40)` | 166 |  |
| `op1` | `integer` | 167 |  |
| `op2` | `integer` | 168 | \|none \|plant number in community for hu scheduling |
| `op3` | `real` | 169 | \|none \|application amount (mm or kg/ha) |
| `op4` | `integer` | 170 | \|none \|fert and pest type-point to fert and pest db |

### management_schedule

- **Defined in source**: `mgt_operations_module.f90:176`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character(len=40)` | 177 |  |
| `num_ops` | `integer` | 178 |  |
| `num_autos` | `integer` | 179 |  |
| `first_op` | `integer` | 180 |  |
| `mgt_ops` | `management_ops` | 181 |  |
| `auto_name` | `character(len=40), dimension (:), allocatable` | 182 |  |
| `auto_crop` | `character(len=40), dimension (:), allocatable` | 183 |  |
| `auto_crop_num` | `integer` | 184 |  |
| `num_db` | `integer, dimension (:), allocatable` | 185 |  |
| `irr` | `integer` | 186 |  |

## Variables Defined
### irrop_db

- **Type**: `irrigation_operation`
- **Defined in source**: `mgt_operations_module.f90:15`

### pudl_db

- **Type**: `puddle_operation`
- **Defined in source**: `mgt_operations_module.f90:28`

### filtstrip_db

- **Type**: `filtstrip_operation`
- **Defined in source**: `mgt_operations_module.f90:38`

### fire_db

- **Type**: `fire_operation`
- **Defined in source**: `mgt_operations_module.f90:45`

### grwaterway_db

- **Type**: `grwaterway_operation`
- **Defined in source**: `mgt_operations_module.f90:57`

### bmpuser_db

- **Type**: `bmpuser_operation`
- **Defined in source**: `mgt_operations_module.f90:95`

### chemapp_db

- **Type**: `chemical_application_operation`
- **Defined in source**: `mgt_operations_module.f90:108`

### harvop_db

- **Type**: `harvest_operation`
- **Defined in source**: `mgt_operations_module.f90:118`

### harvop

- **Type**: `harvest_operation`
- **Defined in source**: `mgt_operations_module.f90:119`

### hkop

- **Type**: `harvest_operation`
- **Defined in source**: `mgt_operations_module.f90:120`

### grazeop_db

- **Type**: `grazing_operation`
- **Defined in source**: `mgt_operations_module.f90:131`

### graze

- **Type**: `grazing_operation`
- **Defined in source**: `mgt_operations_module.f90:132`

### sweepop_db

- **Type**: `streetsweep_operation`
- **Defined in source**: `mgt_operations_module.f90:140`

### sweepop

- **Type**: `streetsweep_operation`
- **Defined in source**: `mgt_operations_module.f90:141`

### mgt

- **Type**: `management_ops`
- **Defined in source**: `mgt_operations_module.f90:172`

### mgt1

- **Type**: `management_ops`
- **Defined in source**: `mgt_operations_module.f90:173`

### mgt2

- **Type**: `management_ops`
- **Defined in source**: `mgt_operations_module.f90:174`

### sched

- **Type**: `management_schedule`
- **Defined in source**: `mgt_operations_module.f90:188`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
(No functions detected.)

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
