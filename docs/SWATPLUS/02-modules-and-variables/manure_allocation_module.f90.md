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
  - bal_d
  - bal_m
  - bal_y
  - bal_a
  - manure_amt
  - tot
  - mallo_hdr
  - mallo_hdr_units
  - mois_typ
  - manure_typ
  - ob_typ
  - dtbl
  - right
  - name
  - rule_typ
  - day
  - mo
  - day_mo
  - yrc
  - itrn
  - trn_typ
  - trn_num
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

# manure_allocation_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `manure_demand_amount` |  |
| `source_manure_output` |  |
| `manure_source_objects` |  |
| `manure_demand_objects` |  |
| `manure_allocation` |  |
| `mallo_header` |  |
| `mallo_header_units` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `manure_amtz` |  |  |
| `malloz` |  |  |
| `bal_d` |  |  |
| `bal_m` |  |  |
| `bal_y` |  |  |
| `bal_a` |  |  |
| `manure_amt` |  |  |
| `tot` |  |  |
| `mallo_hdr` |  |  |
| `mallo_hdr_units` |  |  |
| `mois_typ` |  |  |
| `manure_typ` |  |  |
| `ob_typ` |  |  |
| `dtbl` |  |  |
| `right` |  |  |
| `name` |  |  |
| `rule_typ` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `itrn` |  |  |
| `trn_typ` |  |  |
| `trn_num` |  |  |
| `src1_obj` |  |  |
| `src1_typ` |  |  |
| `src1_num` |  |  |
| `trn1` |  |  |
| `s1out` |  |  |
| `s1un` |  |  |
| `src2_typ` |  |  |
| `src2_num` |  |  |
| `trn2` |  |  |
| `s2out` |  |  |
| `s2un` |  |  |
| `src3_typ` |  |  |
| `src3_num` |  |  |
| `trn3` |  |  |
| `s3out` |  |  |
| `s3un` |  |  |

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
