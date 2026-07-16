---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: recall_read_salt.f90
note_file: recall_read_salt.f90
subroutine: recall_read_salt
module:
  - hydrograph_module
  - input_file_module
  - organic_mineral_mass_module
  - constituent_mass_module
  - maximum_data_module
  - time_module
  - exco_module
calls: []
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#rec_salt
  - constituent_mass_module.f90#recoutsaltb_a
  - constituent_mass_module.f90#recoutsaltb_d
  - constituent_mass_module.f90#recoutsaltb_m
  - constituent_mass_module.f90#recoutsaltb_y
  - constituent_mass_module.f90#recsaltb_a
  - constituent_mass_module.f90#recsaltb_d
  - constituent_mass_module.f90#recsaltb_m
  - constituent_mass_module.f90#recsaltb_y
  - time_module.f90#time
input_variables:
  - constituent_mass_module.f90#rec_salt
reads:
  - salt_recall.rec
  - rec_salt(i
writes: []
purpose: ""
---

# recall_read_salt

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `recall_read_salt.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[input_file_module.f90]]
  - [[organic_mineral_mass_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[maximum_data_module.f90]]
  - [[time_module.f90]]
  - [[exco_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 2 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

(No static callers detected.)

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#rec_salt]] - `recall_salt_inputs`
- [[constituent_mass_module.f90#recoutsaltb_a]] - `constituent_mass`
- [[constituent_mass_module.f90#recoutsaltb_d]] - `constituent_mass`
- [[constituent_mass_module.f90#recoutsaltb_m]] - `constituent_mass`
- [[constituent_mass_module.f90#recoutsaltb_y]] - `constituent_mass`
- [[constituent_mass_module.f90#recsaltb_a]] - `constituent_mass`
- [[constituent_mass_module.f90#recsaltb_d]] - `constituent_mass`
- [[constituent_mass_module.f90#recsaltb_m]] - `constituent_mass`
- [[constituent_mass_module.f90#recsaltb_y]] - `constituent_mass`
- [[time_module.f90#time]] - `time_current`

**Populated by file reads:**

- [[constituent_mass_module.f90#rec_salt]]

## File I/O
- **Reads**:
  - [[salt_recall.rec]]
  - `rec_salt(i` _(variable; see [[file.cio]])_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
