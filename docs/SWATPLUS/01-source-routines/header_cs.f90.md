---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: header_cs.f90
note_file: header_cs.f90
subroutine: header_cs
module:
  - hydrograph_module
  - constituent_mass_module
  - output_path_module
calls:
  - open_output_file
uses_variables:
  - constituent_mass_module.f90#cs_db
  - constituent_mass_module.f90#cs_hmet_solsor
  - constituent_mass_module.f90#cs_path_solsor
  - constituent_mass_module.f90#cs_pest_solsor
  - constituent_mass_module.f90#cs_salt_solsor
  - constituent_mass_module.f90#csin_hyd_hdr
  - constituent_mass_module.f90#csout_hyd_hdr
input_variables: []
reads: []
writes:
  - hydin_pests_day.txt
  - hydin_pests_day.csv
  - hydin_paths_day.txt
  - hydin_paths_day.csv
  - hydin_metals_day.txt
  - hydin_metals_day.csv
  - hydin_salts_day.txt
  - hydin_salts_day.csv
  - hydin_pests_mon.txt
  - hydin_pests_mon.csv
  - hydin_paths_mon.txt
  - hydin_paths_mon.csv
  - hydin_metals_mon.txt
  - hydin_metals_mon.csv
  - hydin_salts_mon.txt
  - hydin_salts_mon.csv
  - hydin_pests_yr.txt
  - hydin_pests_yr.csv
  - hydin_paths_yr.txt
  - hydin_paths_yr.csv
  - hydin_metals_yr.txt
  - hydin_metals_yr.csv
  - hydin_salts_yr.txt
  - hydin_salts_yr.csv
  - hydin_pests_aa.txt
  - hydin_pests_aa.csv
  - hydin_paths_aa.txt
  - hydin_paths_aa.csv
  - hydin_metals_aa.txt
  - hydin_metals_aa.csv
  - hydin_salts_aa.txt
  - hydin_salts_aa.csv
  - hydout_pests_day.txt
  - hydout_pests_day.csv
  - hydout_paths_day.txt
  - hydout_paths_day.csv
  - hydout_metals_day.txt
  - hydout_metals_day.csv
  - hydout_salts_day.txt
  - hydout_salts_day.csv
  - hydout_pests_mon.txt
  - hydout_pests_mon.csv
  - hydout_paths_mon.txt
  - hydout_paths_mon.csv
  - hydout_metals_mon.txt
  - hydout_metals_mon.csv
  - hydout_salts_mon.txt
  - hydout_salts_mon.csv
  - hydout_pests_yr.txt
  - hydout_pests_yr.csv
  - hydout_paths_yr.txt
  - hydout_paths_yr.csv
  - hydout_metals_yr.txt
  - hydout_metals_yr.csv
  - hydout_salts_yr.txt
  - hydout_salts_yr.csv
  - hydout_pests_aa.txt
  - hydout_pests_aa.csv
  - hydout_paths_aa.txt
  - hydout_paths_aa.csv
  - hydout_metals_aa.txt
  - hydout_metals_aa.csv
  - hydout_salts_aa.txt
  - hydout_salts_aa.csv
purpose: ""
---

# header_cs

> [!info] Summary
> TBD

## Basic Information
- **Type**: `subroutine`
- **Source file**: `header_cs.f90`
- **Modules used**:
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
  - [[output_path_module.f90]]
- **Subroutine calls**: 1 | **Files read**: 0 | **Files written**: 64

## Call Relationships
**This routine calls:**

- [[output_path_module.f90#open_output_file]]

**Called by:**

(No static callers detected.)

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[constituent_mass_module.f90#cs_db]] - `constituents`
- [[constituent_mass_module.f90#cs_hmet_solsor]] - `sol_sor`
- [[constituent_mass_module.f90#cs_path_solsor]] - `sol_sor`
- [[constituent_mass_module.f90#cs_pest_solsor]] - `sol_sor`
- [[constituent_mass_module.f90#cs_salt_solsor]] - `sol_sor`
- [[constituent_mass_module.f90#csin_hyd_hdr]] - `constituents_header_in`
- [[constituent_mass_module.f90#csout_hyd_hdr]] - `constituents_header_out`

## File I/O
- **Writes**:
  - [[hydin_pests_day.txt]]
  - [[hydin_pests_day.csv]]
  - [[hydin_paths_day.txt]]
  - [[hydin_paths_day.csv]]
  - [[hydin_metals_day.txt]]
  - [[hydin_metals_day.csv]]
  - [[hydin_salts_day.txt]]
  - [[hydin_salts_day.csv]]
  - [[hydin_pests_mon.txt]]
  - [[hydin_pests_mon.csv]]
  - [[hydin_paths_mon.txt]]
  - [[hydin_paths_mon.csv]]
  - [[hydin_metals_mon.txt]]
  - [[hydin_metals_mon.csv]]
  - [[hydin_salts_mon.txt]]
  - [[hydin_salts_mon.csv]]
  - [[hydin_pests_yr.txt]]
  - [[hydin_pests_yr.csv]]
  - [[hydin_paths_yr.txt]]
  - [[hydin_paths_yr.csv]]
  - [[hydin_metals_yr.txt]]
  - [[hydin_metals_yr.csv]]
  - [[hydin_salts_yr.txt]]
  - [[hydin_salts_yr.csv]]
  - [[hydin_pests_aa.txt]]
  - [[hydin_pests_aa.csv]]
  - [[hydin_paths_aa.txt]]
  - [[hydin_paths_aa.csv]]
  - [[hydin_metals_aa.txt]]
  - [[hydin_metals_aa.csv]]
  - [[hydin_salts_aa.txt]]
  - [[hydin_salts_aa.csv]]
  - [[hydout_pests_day.txt]]
  - [[hydout_pests_day.csv]]
  - [[hydout_paths_day.txt]]
  - [[hydout_paths_day.csv]]
  - [[hydout_metals_day.txt]]
  - [[hydout_metals_day.csv]]
  - [[hydout_salts_day.txt]]
  - [[hydout_salts_day.csv]]
  - [[hydout_pests_mon.txt]]
  - [[hydout_pests_mon.csv]]
  - [[hydout_paths_mon.txt]]
  - [[hydout_paths_mon.csv]]
  - [[hydout_metals_mon.txt]]
  - [[hydout_metals_mon.csv]]
  - [[hydout_salts_mon.txt]]
  - [[hydout_salts_mon.csv]]
  - [[hydout_pests_yr.txt]]
  - [[hydout_pests_yr.csv]]
  - [[hydout_paths_yr.txt]]
  - [[hydout_paths_yr.csv]]
  - [[hydout_metals_yr.txt]]
  - [[hydout_metals_yr.csv]]
  - [[hydout_salts_yr.txt]]
  - [[hydout_salts_yr.csv]]
  - [[hydout_pests_aa.txt]]
  - [[hydout_pests_aa.csv]]
  - [[hydout_paths_aa.txt]]
  - [[hydout_paths_aa.csv]]
  - [[hydout_metals_aa.txt]]
  - [[hydout_metals_aa.csv]]
  - [[hydout_salts_aa.txt]]
  - [[hydout_salts_aa.csv]]

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
