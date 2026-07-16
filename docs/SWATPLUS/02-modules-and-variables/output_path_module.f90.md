---
type: module
tags:
  - swat/module
  - swat/to-read
file: output_path_module.f90
note_file: output_path_module.f90
module_name: output_path_module
defines_types: []
defines_vars:
  - out_path
defines_subroutines:
  - init_output_path
  - open_output_file
defines_functions:
  - get_output_filename
defines_procedures:
  - init_output_path
  - open_output_file
  - get_output_filename
purpose: ""
---

# output_path_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
(No type definitions detected.)

## Variables Defined
### out_path

- **Type**: `character(len=256)`
- **Defined in source**: `output_path_module.f90:6`

## Subroutines Defined
### init_output_path

### open_output_file

## Functions Defined
### get_output_filename

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
