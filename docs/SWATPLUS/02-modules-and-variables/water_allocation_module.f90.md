---
type: module
tags:
  - swat/module
  - swat/to-read
file: water_allocation_module.f90
note_file: water_allocation_module.f90
module_name: water_allocation_module
defines_types:
  - transfer_source_objects
  - transfer_receiving_objects
  - outside_basin_objects
  - water_transfer_objects
  - source_output
  - water_allocation
  - water_treatment_use_data
  - outside_basin_source
  - outside_basin_receive
  - aquifer_loss
  - water_transfer_data
  - water_canal_data
  - transfer_object_output
  - water_allocation_output
  - wallo_header
  - wallo_header_units
defines_vars:
  - rcv
  - walloz
  - tot
  - wallo_hdr
  - wallo_hdr_units
  - typ
  - conv_typ
  - dtbl_lim
  - comp
  - trn_typ
  - trn_typ_name
  - right
  - dtbl_src
  - name
  - rule_typ
  - org_min
  - pests
  - paths
  - hmets
  - salts
  - constit
  - descrip
  - filename
  - init
  - w_sta
  - dtbl
  - day
  - mo
  - day_mo
  - yrc
  - itrn
  - trn_num
  - rcv_typ
  - rcv_num
  - src1_obj
  - src1_typ
  - src1_num
  - trn1
  - s1out
  - s1un
  - src2_typ
  - src2_num
  - trn2
  - s2out
  - s2un
  - src3_typ
  - src3_num
  - trn3
  - s3out
  - s3un
purpose: ""
---

# water_allocation_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `transfer_source_objects` |  |
| `transfer_receiving_objects` |  |
| `outside_basin_objects` |  |
| `water_transfer_objects` |  |
| `source_output` |  |
| `water_allocation` |  |
| `water_treatment_use_data` |  |
| `outside_basin_source` |  |
| `outside_basin_receive` |  |
| `aquifer_loss` |  |
| `water_transfer_data` |  |
| `water_canal_data` |  |
| `transfer_object_output` |  |
| `water_allocation_output` |  |
| `wallo_header` |  |
| `wallo_header_units` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `rcv` |  |  |
| `walloz` |  |  |
| `tot` |  |  |
| `wallo_hdr` |  |  |
| `wallo_hdr_units` |  |  |
| `typ` |  |  |
| `conv_typ` |  |  |
| `dtbl_lim` |  |  |
| `comp` |  |  |
| `trn_typ` |  |  |
| `trn_typ_name` |  |  |
| `right` |  |  |
| `dtbl_src` |  |  |
| `name` |  |  |
| `rule_typ` |  |  |
| `org_min` |  |  |
| `pests` |  |  |
| `paths` |  |  |
| `hmets` |  |  |
| `salts` |  |  |
| `constit` |  |  |
| `descrip` |  |  |
| `filename` |  |  |
| `init` |  |  |
| `w_sta` |  |  |
| `dtbl` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `itrn` |  |  |
| `trn_num` |  |  |
| `rcv_typ` |  |  |
| `rcv_num` |  |  |
| `src1_obj` |  |  |
| `src1_typ` |  |  |
| `src1_num` |  |  |
| `trn1` |  |  |
| `s1out` |  |  |
| `s1un` |  |  |

*(Showing first 40 of 50 variables.)*

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
