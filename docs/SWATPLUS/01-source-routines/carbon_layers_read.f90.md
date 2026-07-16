---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: carbon_layers_read.f90
note_file: carbon_layers_read.f90
subroutine: carbon_layers_read
module:
  - carbon_module
calls: []
uses_variables:
  - carbon_module.f90#cb_n_layers
  - carbon_module.f90#cb_n_layers_explicit
input_variables: []
reads:
  - carbon_layers.prt
writes: []
purpose: ""
---

# carbon_layers_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `carbon_layers_read.f90`
- **Modules used**:
  - [[carbon_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by:**

- [[proc_bsn.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[carbon_module.f90#cb_n_layers]] - `integer`
- [[carbon_module.f90#cb_n_layers_explicit]] - `logical`

## File I/O
- **Reads**:
  - [[carbon_layers.prt]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- Line 26 Check [[carbon_layers.prt]]
- If it exist,
	- Read n_lyr, and set as cb_n_layer in [[carbon_module.f90]]
- End



<!-- USER-NOTES-END -->
