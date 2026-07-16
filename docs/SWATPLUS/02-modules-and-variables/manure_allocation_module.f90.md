---
type: module
tags:
  - swat/module
  - swat/to-read
file: manure_allocation_module.f90
note_file: manure_allocation_module.f90
module_name: manure_allocation_module
defines_types:
  - manure_demand_amount
  - source_manure_output
  - manure_source_objects
  - manure_demand_objects
  - manure_allocation
  - mallo_header
  - mallo_header_units
defines_vars:
  - manure_amtz
  - malloz
  - mallo
  - mallo_hdr
  - mallo_hdr_units
defines_subroutines: []
defines_functions:
  - mallout_add
  - mallo_div_const
defines_procedures:
  - mallout_add
  - mallo_div_const
purpose: ""
---

# manure_allocation_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
### manure_demand_amount

- **Defined in source**: `manure_allocation_module.f90:8`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `mallo_obj` | `integer` | 9 |  |
| `src_obj` | `integer` | 10 |  |
| `app_t_ha` | `real` | 11 |  |
| `app_method` | `integer` | 12 |  |

### source_manure_output

- **Defined in source**: `manure_allocation_module.f90:17`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `stor` | `real` | 18 | current manure stored - tons |
| `prod` | `real` | 19 | mannure produced - tons |
| `withdr` | `real` | 20 | manure withdrawal from all demand objects - tons |

### manure_source_objects

- **Defined in source**: `manure_allocation_module.f90:25`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `num` | `integer` | 26 | source object number |
| `mois_typ` | `character (len=3)` | 27 | wet or dry |
| `manure_typ` | `character (len=25)` | 28 | points to fertilizer.frt |
| `lat` | `real` | 29 | latitude |
| `long` | `real` | 30 | longitude |
| `stor_init` | `real` | 31 | initial storage - tons |
| `stor_max` | `real` | 32 | maximum storage - tons |
| `prod_mon` | `real, dimension (12)` | 33 | average monthly manure produced - tons/month |
| `fertdb` | `integer` | 34 | fertilizer database number (fertilizer.frt) |
| `bal_d` | `source_manure_output` | 35 | daily amount - storage, produced, withdrawn from the source - tons |
| `bal_m` | `source_manure_output` | 36 | monthly amount - storage, produced, withdrawn from the source - tons |
| `bal_y` | `source_manure_output` | 37 | yearly amount - storage, produced, withdrawn from the source - tons |
| `bal_a` | `source_manure_output` | 38 | ave annual amount - storage, produced, withdrawn from the source - tons |

### manure_demand_objects

- **Defined in source**: `manure_allocation_module.f90:42`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `num` | `integer` | 43 | demand object number |
| `ob_typ` | `character (len=10)` | 44 | hru (for application) or muni (treatmentb) or divert (interbasin diversion) |
| `ob_num` | `integer` | 45 | number of the object type |
| `dtbl` | `character (len=25)` | 46 | decision table name for manure/fert application |
| `right` | `character (len=2)` | 47 | manure right (sr -senior or jr - junior right |
| `dtbl_num` | `integer` | 48 |  |
| `manure_amt` | `manure_demand_amount` | 49 |  |
| `withdr` | `real, dimension(:), allocatable` | 50 | daily amount withdrawn from each source |
| `withdr_m` | `real, dimension(:), allocatable` | 51 | amount withdrawn from each source |
| `withdr_y` | `real, dimension(:), allocatable` | 52 | amount withdrawn from each source |
| `withdr_a` | `real, dimension(:), allocatable` | 53 | amount withdrawn from each source |

### manure_allocation

- **Defined in source**: `manure_allocation_module.f90:57`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `name` | `character (len=25)` | 58 | name of the water allocation object |
| `rule_typ` | `character (len=25)` | 59 | rule type to allocate water |
| `src_obs` | `integer` | 60 | number of source objects |
| `trn_obs` | `integer` | 61 | number of demand objects |
| `tot` | `source_manure_output` | 62 | total demand, withdrawal and unmet for entire allocation object |
| `src` | `manure_source_objects` | 63 | dimension by source objects |
| `trn` | `manure_demand_objects` | 64 | dimension by demand objects |

### mallo_header

- **Defined in source**: `manure_allocation_module.f90:68`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character(len=6)` | 69 |  |
| `mo` | `character(len=6)` | 70 |  |
| `day_mo` | `character(len=6)` | 71 |  |
| `yrc` | `character(len=6)` | 72 |  |
| `itrn` | `character(len=8)` | 73 |  |
| `trn_typ` | `character(len=16)` | 74 |  |
| `trn_num` | `character(len=16)` | 75 |  |
| `src1_obj` | `character(len=12)` | 76 |  |
| `src1_typ` | `character(len=12)` | 77 |  |
| `src1_num` | `character(len=12)` | 78 |  |
| `trn1` | `character(len=15)` | 79 | ha-m \|demand - muni or irrigation |
| `s1out` | `character(len=15)` | 80 | ha-m \|withdrawal from source 1 |
| `s1un` | `character(len=12)` | 81 | ha-m \|unmet from source 1 |
| `src2_typ` | `character(len=12)` | 82 |  |
| `src2_num` | `character(len=12)` | 83 |  |
| `trn2` | `character(len=15)` | 84 | ha-m \|demand - muni or irrigation |
| `s2out` | `character(len=15)` | 85 | ha-m \|withdrawal from source 2 |
| `s2un` | `character(len=12)` | 86 | ha-m \|unmet from source 2 |
| `src3_typ` | `character(len=12)` | 87 |  |
| `src3_num` | `character(len=12)` | 88 |  |
| `trn3` | `character(len=15)` | 89 | ha-m \|demand - muni or irrigation |
| `s3out` | `character(len=15)` | 90 | ha-m \|withdrawal from source 3 |
| `s3un` | `character(len=12)` | 91 | ha-m \|unmet from source 3 |

### mallo_header_units

- **Defined in source**: `manure_allocation_module.f90:95`

| Field | Type | Source line | Meaning |
|---|---|---:|---|
| `day` | `character (len=8)` | 96 |  |
| `mo` | `character (len=8)` | 97 |  |
| `day_mo` | `character (len=8)` | 98 |  |
| `yrc` | `character (len=8)` | 99 |  |
| `itrn` | `character (len=8)` | 100 |  |
| `trn_typ` | `character (len=16)` | 101 |  |
| `trn_num` | `character (len=16)` | 102 |  |
| `src1_obj` | `character (len=12)` | 103 |  |
| `src1_typ` | `character (len=12)` | 104 |  |
| `src1_num` | `character (len=8)` | 105 |  |
| `trn1` | `character (len=15)` | 106 | ha-m \|demand - muni or irrigation |
| `s1out` | `character (len=15)` | 107 | ha-m \|withdrawal from source 1 |
| `s1un` | `character (len=9)` | 108 | ha-m \|unmet from source 1 |
| `src2_typ` | `character (len=15)` | 109 |  |
| `src2_num` | `character (len=15)` | 110 |  |
| `trn2` | `character (len=15)` | 111 | ha-m \|demand - muni or irrigation |
| `s2out` | `character (len=15)` | 112 | ha-m \|withdrawal from source 2 |
| `s2un` | `character (len=15)` | 113 | ha-m \|unmet from source 2 |
| `src3_typ` | `character (len=15)` | 114 |  |
| `src3_num` | `character (len=15)` | 115 |  |
| `trn3` | `character (len=15)` | 116 | ha-m \|demand - muni or irrigation |
| `s3out` | `character (len=15)` | 117 | ha-m \|withdrawal from source 3 |
| `s3un` | `character (len=15)` | 118 | ha-m \|unmet from source 3 |

## Variables Defined
### manure_amtz

- **Type**: `manure_demand_amount`
- **Defined in source**: `manure_allocation_module.f90:14`

### malloz

- **Type**: `source_manure_output`
- **Defined in source**: `manure_allocation_module.f90:22`

### mallo

- **Type**: `manure_allocation`
- **Defined in source**: `manure_allocation_module.f90:66`
- **Source note**: dimension by water allocation objects

### mallo_hdr

- **Type**: `mallo_header`
- **Defined in source**: `manure_allocation_module.f90:93`

### mallo_hdr_units

- **Type**: `mallo_header_units`
- **Defined in source**: `manure_allocation_module.f90:120`

## Subroutines Defined
(No subroutines detected.)

## Functions Defined
### mallout_add

### mallo_div_const

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
