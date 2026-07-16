---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: readcio_read.f90
note_file: readcio_read.f90
subroutine: readcio_read
module:
  - input_file_module
  - output_path_module
calls:
  - init_output_path
reads:
  - file.cio
writes: []
purpose: ""
---

# readcio_read

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `readcio_read.f90`
- **Modules used**: [[input_file_module.f90]], [[output_path_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- `init_output_path`

**Called by** (live Dataview back-query):

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## File I/O
- **Reads**: `file.cio`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- use: `input_file_module`, `output_path_module`
- Line 17-109: Reads [[file.cio]]
- Line 112: line 32 of file.cio is the output path;if valid, initializes the output path(validating and creating directories as needed)
<!-- USER-NOTES-END -->
