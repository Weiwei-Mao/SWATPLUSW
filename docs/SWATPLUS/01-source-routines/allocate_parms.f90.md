---
type: source
subtype: subroutine
tags:
  - swat/source
  - swat/to-read
file: allocate_parms.f90
note_file: allocate_parms.f90
subroutine: allocate_parms
module:
  - hru_module
  - time_module
  - hydrograph_module
  - constituent_mass_module
calls:
  - zero0
  - zero1
  - zero2
  - zeroini
uses_variables:
  - hru_module.f90#bio_bod
  - hru_module.f90#biom
  - hru_module.f90#brt
  - hru_module.f90#bss
  - hru_module.f90#bss_ex
  - hru_module.f90#bz_perc
  - hru_module.f90#canstor
  - hru_module.f90#cbodu
  - hru_module.f90#chl_a
  - hru_module.f90#cklsp
  - hru_module.f90#clayld
  - hru_module.f90#cn2
  - hru_module.f90#cnday
  - hru_module.f90#cumei
  - hru_module.f90#cumeira
  - hru_module.f90#cumrai
  - hru_module.f90#cumrt
  - hru_module.f90#cvm_com
  - hru_module.f90#dormhr
  - hru_module.f90#doxq
  - hru_module.f90#epmax
  - hru_module.f90#fcoli
  - hru_module.f90#filterw
  - hru_module.f90#grayld
  - hru_module.f90#grz_days
  - hru_module.f90#gwsoiln
  - hru_module.f90#gwsoilp
  - hru_module.f90#gwsoilq
  - hru_module.f90#gwupcs
  - hru_module.f90#gwupsalt
  - hru_module.f90#hhqday
  - hru_module.f90#hhsedy
  - hru_module.f90#hhsurf_bs
  - hru_module.f90#hhsurfq
  - hru_module.f90#hru
  - hru_module.f90#htfac
  - hru_module.f90#i_sep
  - hru_module.f90#igrz
  - hru_module.f90#init_abstrc
  - hru_module.f90#irgwcs
  - hru_module.f90#irswcs
  - hru_module.f90#iseptic
  - hru_module.f90#isweep
  - hru_module.f90#itb
  - hru_module.f90#itill
  - hru_module.f90#lagyld
  - hru_module.f90#latno3
  - hru_module.f90#latq
  - hru_module.f90#latqcs
  - hru_module.f90#latqsalt
  - hru_module.f90#ndeat
  - hru_module.f90#nplnt
  - hru_module.f90#orgn_con
  - hru_module.f90#orgp_con
  - hru_module.f90#ovrlnd
  - hru_module.f90#ovrlnd_dt
  - hru_module.f90#par
  - hru_module.f90#perccs
  - hru_module.f90#percn
  - hru_module.f90#percsalt
  - hru_module.f90#phubase
  - hru_module.f90#phusw
  - hru_module.f90#plqm
  - hru_module.f90#pplnt
  - hru_module.f90#qdr
  - hru_module.f90#qstemm
  - hru_module.f90#ranrns_hru
  - hru_module.f90#rateinf_prev
  - hru_module.f90#rbiom
  - hru_module.f90#sagyld
  - hru_module.f90#sanyld
  - hru_module.f90#satexn
  - hru_module.f90#satexq
  - hru_module.f90#sed_con
  - hru_module.f90#sedmcs
  - hru_module.f90#sedminpa
  - hru_module.f90#sedminps
  - hru_module.f90#sedorgn
  - hru_module.f90#sedorgp
  - hru_module.f90#sedyld
  - hru_module.f90#sep_tsincefail
  - hru_module.f90#sepbtm
  - hru_module.f90#silyld
  - hru_module.f90#smx
  - hru_module.f90#sol_sumno3
  - hru_module.f90#sol_sumsolp
  - hru_module.f90#soln_con
  - hru_module.f90#solp_con
  - hru_module.f90#sstmaxd
  - hru_module.f90#stmaxd
  - hru_module.f90#surf_bs
  - hru_module.f90#surfq
  - hru_module.f90#surqcs
  - hru_module.f90#surqno3
  - hru_module.f90#surqsalt
  - hru_module.f90#surqsolp
  - hru_module.f90#swtrg
  - hru_module.f90#t_ov
  - hru_module.f90#tc_gwat
  - hru_module.f90#tconc
  - hru_module.f90#tilecs
  - hru_module.f90#tileno3
  - hru_module.f90#tilesalt
  - hru_module.f90#tillage_days
  - hru_module.f90#tillage_depth
  - hru_module.f90#tillage_factor
  - hru_module.f90#tillage_switch
  - hru_module.f90#translt
  - hru_module.f90#twash
  - hru_module.f90#uapd
  - hru_module.f90#ubnrunoff
  - hru_module.f90#ubntss
  - hru_module.f90#un2
  - hru_module.f90#uno3d
  - hru_module.f90#up2
  - hru_module.f90#urb_abstinit
  - hru_module.f90#urbqcs
  - hru_module.f90#urbqsalt
  - hru_module.f90#usle_cfac
  - hru_module.f90#usle_eifac
  - hru_module.f90#wetqcs
  - hru_module.f90#wetqsalt
  - hru_module.f90#wfsh
  - hru_module.f90#wnan
  - hru_module.f90#wrt
  - hru_module.f90#wtspcs
  - hru_module.f90#wtspsalt
  - hru_module.f90#yr_skip
  - hydrograph_module.f90#mhyd
  - hydrograph_module.f90#sp_ob
  - time_module.f90#time
input_variables: []
reads: []
writes: []
purpose: "this subroutine allocates array sizes"
---

# allocate_parms

> [!info] Summary
> this subroutine allocates array sizes

## Basic Information
- **Type**: `subroutine`
- **Source file**: `allocate_parms.f90`
- **Modules used**:
  - [[hru_module.f90]]
  - [[time_module.f90]]
  - [[hydrograph_module.f90]]
  - [[constituent_mass_module.f90]]
- **Subroutine calls**: 4 | **Files read**: 0 | **Files written**: 0

## Call Relationships
**This routine calls:**

- [[zero0.f90]]
- [[zero1.f90]]
- [[zero2.f90]]
- [[zeroini.f90]]

**Called by:**

- [[hru_read.f90]]

**Live Dataview back-query:**

```dataview
LIST file.link
WHERE type = "source" AND contains(calls, this.subroutine)
```

## Module Variables Referenced
- [[hru_module.f90#bio_bod]] - `real, dimension (:), allocatable`
- [[hru_module.f90#biom]] - `real, dimension (:), allocatable`
- [[hru_module.f90#brt]] - `real, dimension (:), allocatable`
- [[hru_module.f90#bss]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#bss_ex]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#bz_perc]] - `real, dimension (:), allocatable`
- [[hru_module.f90#canstor]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cbodu]] - `real, dimension (:), allocatable`
- [[hru_module.f90#chl_a]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cklsp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#clayld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cn2]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cnday]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cumei]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cumeira]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cumrai]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cumrt]] - `real, dimension (:), allocatable`
- [[hru_module.f90#cvm_com]] - `real, dimension (:), allocatable`
- [[hru_module.f90#dormhr]] - `real, dimension (:), allocatable`
- [[hru_module.f90#doxq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#epmax]] - `real, dimension (:), allocatable`
- [[hru_module.f90#fcoli]] - `real, dimension (:), allocatable`
- [[hru_module.f90#filterw]] - `real, dimension (:), allocatable`
- [[hru_module.f90#grayld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#grz_days]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#gwsoiln]] - `real, dimension (:), allocatable`
- [[hru_module.f90#gwsoilp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#gwsoilq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#gwupcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#gwupsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#hhqday]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#hhsedy]] - `real, dimension(:,:), allocatable`
- [[hru_module.f90#hhsurf_bs]] - `real, dimension (:,:,:), allocatable`
- [[hru_module.f90#hhsurfq]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#hru]] - `hydrologic_response_unit`
- [[hru_module.f90#htfac]] - `real, dimension (:), allocatable`
- [[hru_module.f90#i_sep]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#igrz]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#init_abstrc]] - `real, dimension(:), allocatable`
- [[hru_module.f90#irgwcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#irswcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#iseptic]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#isweep]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#itb]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#itill]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#lagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#latno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#latq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#latqcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#latqsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#ndeat]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#nplnt]] - `real, dimension (:), allocatable`
- [[hru_module.f90#orgn_con]] - `real, dimension (:), allocatable`
- [[hru_module.f90#orgp_con]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ovrlnd]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ovrlnd_dt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#par]] - `real, dimension (:), allocatable`
- [[hru_module.f90#perccs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#percn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#percsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#phubase]] - `real, dimension (:), allocatable`
- [[hru_module.f90#phusw]] - `real, dimension (:), allocatable`
- [[hru_module.f90#plqm]] - `real, dimension (:), allocatable`
- [[hru_module.f90#pplnt]] - `real, dimension (:), allocatable`
- [[hru_module.f90#qdr]] - `real, dimension (:), allocatable`
- [[hru_module.f90#qstemm]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ranrns_hru]] - `real, dimension (:), allocatable`
- [[hru_module.f90#rateinf_prev]] - `real, dimension (:), allocatable`
- [[hru_module.f90#rbiom]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sagyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sanyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#satexn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#satexq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sed_con]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedmcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#sedminpa]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedminps]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgn]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedorgp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sedyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sep_tsincefail]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#sepbtm]] - `real, dimension (:), allocatable`
- [[hru_module.f90#silyld]] - `real, dimension (:), allocatable`
- [[hru_module.f90#smx]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sol_sumno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sol_sumsolp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#soln_con]] - `real, dimension (:), allocatable`
- [[hru_module.f90#solp_con]] - `real, dimension (:), allocatable`
- [[hru_module.f90#sstmaxd]] - `real, dimension (:), allocatable`
- [[hru_module.f90#stmaxd]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surf_bs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#surfq]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#surqno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#surqsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#surqsolp]] - `real, dimension (:), allocatable`
- [[hru_module.f90#swtrg]] - `integer, dimension (:), allocatable`
- [[hru_module.f90#t_ov]] - `real, dimension (:), allocatable`
- [[hru_module.f90#tc_gwat]] - `real, dimension (:), allocatable`
- [[hru_module.f90#tconc]] - `real, dimension (:), allocatable`
- [[hru_module.f90#tilecs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#tileno3]] - `real, dimension (:), allocatable`
- [[hru_module.f90#tilesalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#tillage_days]] - `integer, dimension(:), allocatable`
- [[hru_module.f90#tillage_depth]] - `real, dimension(:), allocatable`
- [[hru_module.f90#tillage_factor]] - `real, dimension(:), allocatable`
- [[hru_module.f90#tillage_switch]] - `integer, dimension(:), allocatable`
- [[hru_module.f90#translt]] - `real, dimension (:), allocatable`
- [[hru_module.f90#twash]] - `real, dimension (:), allocatable`
- [[hru_module.f90#uapd]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ubnrunoff]] - `real, dimension (:), allocatable`
- [[hru_module.f90#ubntss]] - `real, dimension (:), allocatable`
- [[hru_module.f90#un2]] - `real, dimension (:), allocatable`
- [[hru_module.f90#uno3d]] - `real, dimension (:), allocatable`
- [[hru_module.f90#up2]] - `real, dimension (:), allocatable`
- [[hru_module.f90#urb_abstinit]] - `real, dimension (:), allocatable`
- [[hru_module.f90#urbqcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#urbqsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#usle_cfac]] - `real, dimension (:), allocatable`
- [[hru_module.f90#usle_eifac]] - `real, dimension (:), allocatable`
- [[hru_module.f90#wetqcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#wetqsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#wfsh]] - `real, dimension (:), allocatable`
- [[hru_module.f90#wnan]] - `real, dimension (:), allocatable`
- [[hru_module.f90#wrt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#wtspcs]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#wtspsalt]] - `real, dimension (:,:), allocatable`
- [[hru_module.f90#yr_skip]] - `integer, dimension (:), allocatable`
- [[hydrograph_module.f90#mhyd]] - `integer`
- [[hydrograph_module.f90#sp_ob]] - `spatial_objects`
- [[time_module.f90#time]] - `time_current`

<!-- USER-NOTES-START -->
## Notes
Use this section for line notes, key variables, and interpretation. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
