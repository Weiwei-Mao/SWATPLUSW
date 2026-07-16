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
uses_variables:
  - input_file_module.f90#in_aqu
  - input_file_module.f90#in_basin
  - input_file_module.f90#in_cha
  - input_file_module.f90#in_chg
  - input_file_module.f90#in_cli
  - input_file_module.f90#in_con
  - input_file_module.f90#in_cond
  - input_file_module.f90#in_delr
  - input_file_module.f90#in_exco
  - input_file_module.f90#in_herd
  - input_file_module.f90#in_hru
  - input_file_module.f90#in_hyd
  - input_file_module.f90#in_init
  - input_file_module.f90#in_link
  - input_file_module.f90#in_lum
  - input_file_module.f90#in_ops
  - input_file_module.f90#in_parmdb
  - input_file_module.f90#in_path_hmd
  - input_file_module.f90#in_path_pcp
  - input_file_module.f90#in_path_slr
  - input_file_module.f90#in_path_tmp
  - input_file_module.f90#in_path_wnd
  - input_file_module.f90#in_rec
  - input_file_module.f90#in_regs
  - input_file_module.f90#in_res
  - input_file_module.f90#in_ru
  - input_file_module.f90#in_sim
  - input_file_module.f90#in_sol
  - input_file_module.f90#in_str
  - input_file_module.f90#in_watrts
input_variables:
  - input_file_module.f90#in_aqu
  - input_file_module.f90#in_basin
  - input_file_module.f90#in_cha
  - input_file_module.f90#in_chg
  - input_file_module.f90#in_cli
  - input_file_module.f90#in_con
  - input_file_module.f90#in_cond
  - input_file_module.f90#in_delr
  - input_file_module.f90#in_exco
  - input_file_module.f90#in_herd
  - input_file_module.f90#in_hru
  - input_file_module.f90#in_hyd
  - input_file_module.f90#in_init
  - input_file_module.f90#in_link
  - input_file_module.f90#in_lum
  - input_file_module.f90#in_ops
  - input_file_module.f90#in_parmdb
  - input_file_module.f90#in_path_hmd
  - input_file_module.f90#in_path_pcp
  - input_file_module.f90#in_path_slr
  - input_file_module.f90#in_path_tmp
  - input_file_module.f90#in_path_wnd
  - input_file_module.f90#in_rec
  - input_file_module.f90#in_regs
  - input_file_module.f90#in_res
  - input_file_module.f90#in_ru
  - input_file_module.f90#in_sim
  - input_file_module.f90#in_sol
  - input_file_module.f90#in_str
  - input_file_module.f90#in_watrts
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
- **Modules used**:
  - [[input_file_module.f90]]
  - [[output_path_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 1 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[output_path_module.f90#init_output_path]]

**Called by:**

- [[proc_bsn.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[input_file_module.f90#in_aqu]] - `input_aqu`
- [[input_file_module.f90#in_basin]] - `input_basin`
- [[input_file_module.f90#in_cha]] - `input_cha`
- [[input_file_module.f90#in_chg]] - `input_chg`
- [[input_file_module.f90#in_cli]] - `input_cli`
- [[input_file_module.f90#in_con]] - `input_con`
- [[input_file_module.f90#in_cond]] - `input_condition`
- [[input_file_module.f90#in_delr]] - `input_delr`
- [[input_file_module.f90#in_exco]] - `input_exco`
- [[input_file_module.f90#in_herd]] - `input_herd`
- [[input_file_module.f90#in_hru]] - `input_hru`
- [[input_file_module.f90#in_hyd]] - `input_hydrology`
- [[input_file_module.f90#in_init]] - `input_init`
- [[input_file_module.f90#in_link]] - `input_link`
- [[input_file_module.f90#in_lum]] - `input_lum`
- [[input_file_module.f90#in_ops]] - `input_ops`
- [[input_file_module.f90#in_parmdb]] - `input_parameter_databases`
- [[input_file_module.f90#in_path_hmd]] - `input_path_hmd`
- [[input_file_module.f90#in_path_pcp]] - `input_path_pcp`
- [[input_file_module.f90#in_path_slr]] - `input_path_slr`
- [[input_file_module.f90#in_path_tmp]] - `input_path_tmp`
- [[input_file_module.f90#in_path_wnd]] - `input_path_wnd`
- [[input_file_module.f90#in_rec]] - `input_rec`
- [[input_file_module.f90#in_regs]] - `input_regions`
- [[input_file_module.f90#in_res]] - `input_res`
- [[input_file_module.f90#in_ru]] - `input_ru`
- [[input_file_module.f90#in_sim]] - `input_sim`
- [[input_file_module.f90#in_sol]] - `input_soils`
- [[input_file_module.f90#in_str]] - `input_structural`
- [[input_file_module.f90#in_watrts]] - `input_water_rights`

**Populated by file reads:**

- [[input_file_module.f90#in_aqu]]
- [[input_file_module.f90#in_basin]]
- [[input_file_module.f90#in_cha]]
- [[input_file_module.f90#in_chg]]
- [[input_file_module.f90#in_cli]]
- [[input_file_module.f90#in_con]]
- [[input_file_module.f90#in_cond]]
- [[input_file_module.f90#in_delr]]
- [[input_file_module.f90#in_exco]]
- [[input_file_module.f90#in_herd]]
- [[input_file_module.f90#in_hru]]
- [[input_file_module.f90#in_hyd]]
- [[input_file_module.f90#in_init]]
- [[input_file_module.f90#in_link]]
- [[input_file_module.f90#in_lum]]
- [[input_file_module.f90#in_ops]]
- [[input_file_module.f90#in_parmdb]]
- [[input_file_module.f90#in_path_hmd]]
- [[input_file_module.f90#in_path_pcp]]
- [[input_file_module.f90#in_path_slr]]
- [[input_file_module.f90#in_path_tmp]]
- [[input_file_module.f90#in_path_wnd]]
- [[input_file_module.f90#in_rec]]
- [[input_file_module.f90#in_regs]]
- [[input_file_module.f90#in_res]]
- [[input_file_module.f90#in_ru]]
- [[input_file_module.f90#in_sim]]
- [[input_file_module.f90#in_sol]]
- [[input_file_module.f90#in_str]]
- [[input_file_module.f90#in_watrts]]

## File I/O
- **Reads**:
  - [[file.cio]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.

- use:
	- [[input_file_module.f90]]
	- [[output_path_module.f90]]
- Line 17-109: Reads [[file.cio]]
- Line 112: [[output_path_module.f90#init_output_path]], line 32 of [[file.cio]] file is the output path;
	- if valid, initializes the output path (validating and creating directories as needed)
- End
<!-- USER-NOTES-END -->
