---
type: module
tags:
  - swat/module
  - swat/to-read
file: channel_module.f90
note_file: channel_module.f90
module_name: channel_module
defines_types:
  - channel
  - ch_output
  - regional_output_channel
  - ch_header
  - ch_header_units
defines_vars:
  - bch_d
  - bch_m
  - bch_y
  - bch_a
  - chz
  - ch_hdr
  - ch_hdr_units
  - sed_ch
  - day
  - mo
  - day_mo
  - yrc
  - isd
  - id
  - name
  - flo_in
  - flo_out
  - evap
  - tloss
  - sed_in
  - sed_out
  - sed_conc
  - orgn_in
  - orgn_out
  - orgp_in
  - orgp_out
  - no3_in
  - no3_out
  - nh4_in
  - nh4_out
  - no2_in
  - no2_out
  - solp_in
  - solp_out
  - chla_in
  - chla_out
  - cbod_in
  - cbod_out
  - dis_in
  - dis_out
  - solpst_in
  - solpst_out
  - sorbpst_in
  - sorbpst_out
  - react
  - volat
  - setlpst
  - resuspst
  - difus
  - reactb
  - bury
  - sedpest
  - bacp
  - baclp
  - met1
  - met2
  - met3
  - sand_in
  - sand_out
  - silt_in
  - silt_out
  - clay_in
  - clay_out
  - smag_in
  - smag_out
  - lag_in
  - lag_out
  - grvl_in
  - grvl_out
  - bnk_ero
  - ch_deg
  - ch_dep
  - fp_dep
  - tot_ssed
purpose: ""
---

# channel_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `channel` |  |
| `ch_output` |  |
| `regional_output_channel` |  |
| `ch_header` |  |
| `ch_header_units` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `bch_d` |  |  |
| `bch_m` |  |  |
| `bch_y` |  |  |
| `bch_a` |  |  |
| `chz` |  |  |
| `ch_hdr` |  |  |
| `ch_hdr_units` |  |  |
| `sed_ch` |  |  |
| `day` |  |  |
| `mo` |  |  |
| `day_mo` |  |  |
| `yrc` |  |  |
| `isd` |  |  |
| `id` |  |  |
| `name` |  |  |
| `flo_in` |  |  |
| `flo_out` |  |  |
| `evap` |  |  |
| `tloss` |  |  |
| `sed_in` |  |  |
| `sed_out` |  |  |
| `sed_conc` |  |  |
| `orgn_in` |  |  |
| `orgn_out` |  |  |
| `orgp_in` |  |  |
| `orgp_out` |  |  |
| `no3_in` |  |  |
| `no3_out` |  |  |
| `nh4_in` |  |  |
| `nh4_out` |  |  |
| `no2_in` |  |  |
| `no2_out` |  |  |
| `solp_in` |  |  |
| `solp_out` |  |  |
| `chla_in` |  |  |
| `chla_out` |  |  |
| `cbod_in` |  |  |
| `cbod_out` |  |  |
| `dis_in` |  |  |
| `dis_out` |  |  |

*(Showing first 40 of 74 variables.)*

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
