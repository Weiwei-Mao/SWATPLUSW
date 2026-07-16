---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: fcgd.f90
note_file: fcgd.f90
subroutine: fcgd
module:
  - carbon_module
calls: []
uses_variables:
  - carbon_module.f90#org_con
input_variables: []
reads: []
writes: []
purpose: ""
---

# fcgd

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `fcgd.f90`
- **Modules used**:
  - [[carbon_module.f90]]
- **Subroutine calls**: 0 | **Files read**: 0 | **Files written**: 0

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
- [[carbon_module.f90#org_con]] - `organic_controls`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
