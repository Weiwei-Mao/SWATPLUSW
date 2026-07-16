---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: read_mgtops.f90
note_file: read_mgtops.f90
subroutine: read_mgtops
module:
  - maximum_data_module
  - plant_data_module
  - mgt_operations_module
  - tillage_data_module
  - fertilizer_data_module
  - pesticide_data_module
  - time_module
calls: []
uses_variables:
  - fertilizer_data_module.f90#fertdb
  - fertilizer_data_module.f90#manure_db
  - maximum_data_module.f90#db_mx
  - mgt_operations_module.f90#chemapp_db
  - mgt_operations_module.f90#fire_db
  - mgt_operations_module.f90#grazeop_db
  - mgt_operations_module.f90#harvop_db
  - mgt_operations_module.f90#irrop_db
  - mgt_operations_module.f90#sched
  - mgt_operations_module.f90#sweepop_db
  - pesticide_data_module.f90#pestdb
  - plant_data_module.f90#pcomdb
  - plant_data_module.f90#pldb
  - plant_data_module.f90#transpl
  - tillage_data_module.f90#tilldb
  - time_module.f90#ndays
input_variables:
  - mgt_operations_module.f90#sched
reads: []
writes: []
purpose: ""
---

# read_mgtops

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `read_mgtops.f90`
- **Modules used**:
  - [[maximum_data_module.f90]]
  - [[plant_data_module.f90]]
  - [[mgt_operations_module.f90]]
  - [[tillage_data_module.f90]]
  - [[fertilizer_data_module.f90]]
  - [[pesticide_data_module.f90]]
  - [[time_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[mgt_read_mgtops.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[fertilizer_data_module.f90#fertdb]] - `fertilizer_db`
- [[fertilizer_data_module.f90#manure_db]] - `manure_database`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`
- [[mgt_operations_module.f90#chemapp_db]] - `chemical_application_operation`
- [[mgt_operations_module.f90#fire_db]] - `fire_operation`
- [[mgt_operations_module.f90#grazeop_db]] - `grazing_operation`
- [[mgt_operations_module.f90#harvop_db]] - `harvest_operation`
- [[mgt_operations_module.f90#irrop_db]] - `irrigation_operation`
- [[mgt_operations_module.f90#sched]] - `management_schedule`
- [[mgt_operations_module.f90#sweepop_db]] - `streetsweep_operation`
- [[pesticide_data_module.f90#pestdb]] - `pesticide_db`
- [[plant_data_module.f90#pcomdb]] - `plant_community_db`
- [[plant_data_module.f90#pldb]] - `plant_db`
- [[plant_data_module.f90#transpl]] - `plant_transplant_db`
- [[tillage_data_module.f90#tilldb]] - `tillage_db`
- [[time_module.f90#ndays]] - `integer, dimension (13)`

**Populated by file reads:**

- [[mgt_operations_module.f90#sched]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
