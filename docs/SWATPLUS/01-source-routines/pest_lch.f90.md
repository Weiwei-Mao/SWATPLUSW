---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: pest_lch.f90
note_file: pest_lch.f90
subroutine: pest_lch
module:
  - pesticide_data_module
  - basin_module
  - hru_module
  - soil_module
  - constituent_mass_module
  - output_ls_pesticide_module
  - organic_mineral_mass_module
calls: []
reads: []
writes: []
purpose: "this subroutine calculates pesticides leached through each layer,; pesticide transported with lateral subsurface flow, and pesticide; transported with surface runoff"
---

# pest_lch

> [!info] Summary
> this subroutine calculates pesticides leached through each layer,; pesticide transported with lateral subsurface flow, and pesticide; transported with surface runoff

## Basic Information
- **Type**: `subroutine`
- **Source file**: `pest_lch.f90`
- **Modules used**: [[pesticide_data_module.f90]], [[basin_module.f90]], [[hru_module.f90]], [[soil_module.f90]], [[constituent_mass_module.f90]], [[output_ls_pesticide_module.f90]], [[organic_mineral_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
