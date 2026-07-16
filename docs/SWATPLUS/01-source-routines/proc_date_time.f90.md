---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: proc_date_time.f90
note_file: proc_date_time.f90
subroutine: proc_date_time
module:
  - time_module
calls:
  - date_and_time
  - cli_petmeas
  - cli_pmeas
  - cli_tmeas
  - cli_smeas
  - cli_hmeas
  - cli_wmeas
  - cli_wgnread
uses_variables: []
input_variables: []
reads: []
writes: []
purpose: ""
---

# proc_date_time

> [!info] Summary
> Weather input

## Basic Information
- **Type**: `subroutine`
- **Source file**: `proc_date_time.f90`
- **Modules used**:
  - [[time_module.f90]]
- **Subroutine calls**: 8 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `date_and_time`
- [[cli_petmeas.f90]]
- [[cli_pmeas.f90]]
- [[cli_tmeas.f90]]
- [[cli_smeas.f90]]
- [[cli_hmeas.f90]]
- [[cli_wmeas.f90]]
- [[cli_wgnread.f90]]

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
(No module-level variable references detected.)

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Line 13-17: write exactly time in cmd and [[simulation.out]] (unit 9003)
- Line 19-22, call [[cli_petmeas.f90]], potential evapotranspiration
- Line 24-26: call [[cli_pmeas.f90]], precipitation
- Line 27-30: call [[cli_tmeas.f90]], temperature, maximum and mimimum
- Line 31-34: call [[cli_smeas.f90]], solar radiation
- Line 35-38: call [[cli_hmeas.f90]], relative humidity
- Line 39-42: call [[cli_wmeas.f90]], wind
- Line 43-46: call [[cli_wgnread.f90]], weather stations
- End



<!-- USER-NOTES-END -->
