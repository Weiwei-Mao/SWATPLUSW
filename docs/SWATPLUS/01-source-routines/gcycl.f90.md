---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: gcycl.f90
note_file: gcycl.f90
subroutine: gcycl
module:
  - climate_module
  - basin_module
  - maximum_data_module
  - conditional_module
calls: []
uses_variables:
  - basin_module.f90#bsn_prm
  - climate_module.f90#idg
  - climate_module.f90#rnd2
  - climate_module.f90#rnd3
  - climate_module.f90#rnd8
  - climate_module.f90#rnd9
  - climate_module.f90#rndseed
  - climate_module.f90#rndseed_cond
  - maximum_data_module.f90#db_mx
input_variables: []
reads: []
writes: []
purpose: "This subroutine initializes the random number seeds. If the user; desires a different set of random numbers for each simulation run,; the random number generator is used to reset the values of the"
---

# gcycl

> [!info] Summary
> This subroutine initializes the random number seeds. If the user; desires a different set of random numbers for each simulation run,; the random number generator is used to reset the values of the

## Basic Information
- **Type**: `subroutine`
- **Source file**: `gcycl.f90`
- **Modules used**:
  - [[climate_module.f90]]
  - [[basin_module.f90]]
  - [[maximum_data_module.f90]]
  - [[conditional_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[cli_wgnread.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[basin_module.f90#bsn_prm]] - `basin_parms`
- [[climate_module.f90#idg]] - `integer, dimension (:), allocatable`
- [[climate_module.f90#rnd2]] - `real, dimension (:), allocatable`
- [[climate_module.f90#rnd3]] - `real, dimension (:), allocatable`
- [[climate_module.f90#rnd8]] - `real, dimension (:), allocatable`
- [[climate_module.f90#rnd9]] - `real, dimension (:), allocatable`
- [[climate_module.f90#rndseed]] - `integer, dimension (:,:), allocatable`
- [[climate_module.f90#rndseed_cond]] - `integer`
- [[maximum_data_module.f90#db_mx]] - `data_files_max_elements`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
