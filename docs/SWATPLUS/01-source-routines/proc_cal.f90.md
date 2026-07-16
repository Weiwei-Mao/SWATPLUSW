---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: proc_cal.f90
note_file: proc_cal.f90
subroutine: proc_cal
module:
  - hydrograph_module
  - calibration_data_module
calls:
  - cal_parm_read
  - cal_parmchg_read
  - pl_read_regions_cal
  - pl_read_parms_cal
  - cal_conditions
  - calsoft_read_codes
  - lcu_read_softcal
  - ls_read_lsparms_cal
  - aqu_read_elements
  - ch_read_elements
  - res_read_elements
  - rec_read_elements
  - ch_read_orders_cal
  - ch_read_parms_cal
  - cal_allo_init
uses_variables:
  - calibration_data_module.f90#cal_hard
  - calibration_data_module.f90#cal_soft
input_variables: []
reads: []
writes: []
purpose: ""
---

# proc_cal

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `proc_cal.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[calibration_data_module.f90]]
- **Subroutine calls**: 15 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[cal_parm_read.f90]]
- [[cal_parmchg_read.f90]]
- [[pl_read_regions_cal.f90]]
- [[pl_read_parms_cal.f90]]
- [[cal_conditions.f90]]
- [[calsoft_read_codes.f90]]
- [[lcu_read_softcal.f90]]
- [[ls_read_parms_cal.f90]]
- [[aqu_read_elements.f90]]
- [[ch_read_elements.f90]]
- [[res_read_elements.f90]]
- [[rec_read_elements.f90]]
- [[ch_read_orders_cal.f90]]
- [[ch_read_parms_cal.f90]]
- [[cal_allo_init.f90]]

**Called by:**

- [[main.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[calibration_data_module.f90#cal_hard]] - `character (len=1)`
- [[calibration_data_module.f90#cal_soft]] - `character (len=1)`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
