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
reads: []
writes: []
purpose: ""
---

# proc_date_time

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `proc_date_time.f90`
- **Modules used**: [[time_module.f90]]
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

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
