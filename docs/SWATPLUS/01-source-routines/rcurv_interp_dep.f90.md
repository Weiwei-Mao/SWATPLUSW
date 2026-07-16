---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: rcurv_interp_dep.f90
note_file: rcurv_interp_dep.f90
subroutine: rcurv_interp_dep
module:
  - sd_channel_module
calls:
  - chrc_interp
reads: []
writes: []
purpose: "this subroutine interpolates between points on a rating curve given flow rate"
---

# rcurv_interp_dep

> [!info] Summary
> this subroutine interpolates between points on a rating curve given flow rate

## Basic Information
- **Type**: `subroutine`
- **Source file**: `rcurv_interp_dep.f90`
- **Modules used**: [[sd_channel_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `chrc_interp`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
