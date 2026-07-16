---
type: module
tags:
  - swat/module
  - swat/to-read
file: organic_mineral_mass_module.f90
note_file: organic_mineral_mass_module.f90
module_name: organic_mineral_mass_module
defines_types:
  - organic_mass
  - organic_mixing_mass
  - clay_mass
  - sediment
  - mineral_nitrogen
  - mineral_phosphorus
  - plant_residue
  - soil_profile_mass
  - plant_community_mass
  - mineral_mass
  - organic_mineral_mass
  - animal_herds
  - fertilizer_mass
  - organic_mineral_hydrograph
  - spatial_object_hydrographs
  - recall_organic_mineral_inputs
  - routing_unit_elements_hydrographs
  - channel_surface_elements_hydrographs
defines_vars:
  - orgz
  - tot
  - surf_rsd
  - hact
  - hsta
  - hs
  - hp
  - microb
  - str
  - lig
  - nonlig
  - meta
  - man
  - water
  - mix_org
  - clay
  - mnz
  - mix_mn
  - mpz
  - mix_mp
  - tot_org
  - seq_org
  - surf_org
  - org_flx_tot
  - soil_prof_tot
  - soil_prof_root
  - soil_prof_rsd
  - soil_prof_srsd
  - soil_prof_hact
  - soil_prof_hsta
  - soil_prof_hs
  - soil_prof_hp
  - soil_prof_microb
  - soil_prof_seq_hs
  - soil_prof_seq_hp
  - soil_prof_seq_microb
  - soil_prof_str
  - soil_prof_lig
  - soil_prof_nonlig
  - soil_prof_meta
  - soil_prof_sstr
  - soil_prof_slig
  - soil_prof_smeta
  - soil_prof_man
  - soil_prof_water
  - soil_org_z
  - soil_prof_somc
  - soil_prof_mn
  - soil_prof_mp
  - soil_mn_z
  - soil_mp_z
  - bsn_org_soil
  - bsn_org_pl
  - bsn_org_rsd
  - decomp
  - photo_decomp
  - transfer
  - pl_burn
  - rsd_meta
  - rsd_str
  - rsd_tot
  - tot_com
  - ab_gr_com
  - leaf_com
  - stem_com
  - root_com
  - seed_com
  - pl_yield
  - pl_mass_up
  - pl_residue
  - harv_seed
  - harv_leaf
  - harv_stem
  - harv_left
  - graz_plant
  - graz_seed
  - graz_leaf
  - graz_stem
  - leaf_drop
  - abgr_drop
  - stem_drop
  - seed_drop
  - plt_mass_z
  - hum
  - hum_act
  - min
  - herd_mass
  - org
  - org_frt
  - hin
  - hin_sur
  - hin_lat
  - hin_til
  - hin_aqu
  - hins
  - hin_ssur
  - hin_slat
  - hin_stil
  - hdep_m
  - hdep_y
  - hdep_a
  - o_m1
  - o_m2
  - o_m3
  - pmin_m1
  - pmin_m2
  - pmin_m3
  - nmin_m1
  - nmin_m2
  - nmin_m3
  - name
  - filename
purpose: ""
---

# organic_mineral_mass_module

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
| Type | Notes |
|---|---|
| `organic_mass` |  |
| `organic_mixing_mass` |  |
| `clay_mass` |  |
| `sediment` |  |
| `mineral_nitrogen` |  |
| `mineral_phosphorus` |  |
| `plant_residue` |  |
| `soil_profile_mass` |  |
| `plant_community_mass` |  |
| `mineral_mass` |  |
| `organic_mineral_mass` |  |
| `animal_herds` |  |
| `fertilizer_mass` |  |
| `organic_mineral_hydrograph` |  |
| `spatial_object_hydrographs` |  |
| `recall_organic_mineral_inputs` |  |
| `routing_unit_elements_hydrographs` |  |
| `channel_surface_elements_hydrographs` |  |

## Module-Level Variables
| Variable | Type | Meaning |
|---|---|---|
| `orgz` |  |  |
| `tot` |  |  |
| `surf_rsd` |  |  |
| `hact` |  |  |
| `hsta` |  |  |
| `hs` |  |  |
| `hp` |  |  |
| `microb` |  |  |
| `str` |  |  |
| `lig` |  |  |
| `nonlig` |  |  |
| `meta` |  |  |
| `man` |  |  |
| `water` |  |  |
| `mix_org` |  |  |
| `clay` |  |  |
| `mnz` |  |  |
| `mix_mn` |  |  |
| `mpz` |  |  |
| `mix_mp` |  |  |
| `tot_org` |  |  |
| `seq_org` |  |  |
| `surf_org` |  |  |
| `org_flx_tot` |  |  |
| `soil_prof_tot` |  |  |
| `soil_prof_root` |  |  |
| `soil_prof_rsd` |  |  |
| `soil_prof_srsd` |  |  |
| `soil_prof_hact` |  |  |
| `soil_prof_hsta` |  |  |
| `soil_prof_hs` |  |  |
| `soil_prof_hp` |  |  |
| `soil_prof_microb` |  |  |
| `soil_prof_seq_hs` |  |  |
| `soil_prof_seq_hp` |  |  |
| `soil_prof_seq_microb` |  |  |
| `soil_prof_str` |  |  |
| `soil_prof_lig` |  |  |
| `soil_prof_nonlig` |  |  |
| `soil_prof_meta` |  |  |

*(Showing first 40 of 112 variables.)*

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
