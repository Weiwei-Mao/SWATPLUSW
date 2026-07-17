---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: rte_read_nut.f90
note_file: rte_read_nut.f90
subroutine: rte_read_nut
module:
  - channel_data_module
calls: []
uses_variables:
  - channel_data_module.f90#rte_nut
input_variables:
  - channel_data_module.f90#rte_nut
reads:
  - nutrients.rte
writes: []
purpose: "this subroutine reads data from the lake water quality input file (.lwq).; This file contains data related to initial pesticide and nutrient levels; in the lake/reservoir and transformation processes occurring within the"
---

# rte_read_nut

> [!info] Summary
> this subroutine reads data from the lake water quality input file (.lwq).; This file contains data related to initial pesticide and nutrient levels; in the lake/reservoir and transformation processes occurring within the

## Basic Information
- **Type**: `subroutine`
- **Source file**: `rte_read_nut.f90`
- **Modules used**:
  - [[channel_data_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_hru.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[channel_data_module.f90#rte_nut]] - `routing_nut_data`

**Populated by file reads:**

- [[channel_data_module.f90#rte_nut]]

## File I/O
- **Reads**:
  - [[nutrients.rte]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Check file [[nutrients.rte]], out of [[file.cio]]



<!-- USER-NOTES-END -->
