---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: res_read_saltdb.f90
note_file: res_read_saltdb.f90
subroutine: res_read_saltdb
module:
  - input_file_module
  - maximum_data_module
  - reservoir_data_module
  - res_salt_module
  - constituent_mass_module
calls: []
reads:
  - salt_res
writes: []
purpose: "this subroutine reads reservoir water quality parameters for salt ions"
---

# res_read_saltdb

> [!info] Summary
> this subroutine reads reservoir water quality parameters for salt ions

## Basic Information
- **Type**: `subroutine`
- **Source file**: `res_read_saltdb.f90`
- **Modules used**: [[input_file_module.f90]], [[maximum_data_module.f90]], [[reservoir_data_module.f90]], [[res_salt_module.f90]], [[constituent_mass_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 1 | **Files written**: 0

## Call Relationships
(No call statements; leaf node.)

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `salt_res` _(variable; see file.cio)_

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
