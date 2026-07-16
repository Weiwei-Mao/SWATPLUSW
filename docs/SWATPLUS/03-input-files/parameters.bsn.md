---
type: input
tags:
  - swat/input
file: parameters.bsn
ext: bsn
cio_field: parms_bas
read_by:
  - basin_read_prm.f90
purpose: ""
---

# parameters.bsn

> [!info] Input File
> Declared in `file.cio` field `parms_bas`. See [[file.cio]] for the controlling file map.

## Overview
- **Declared in `file.cio` field**: `parms_bas`
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[basin_read_prm.f90]]

## File Structure
- [[basin_read_prm.f90]] source line 20: reads `titldum`
- [[basin_read_prm.f90]] source line 22: reads `header`
- [[basin_read_prm.f90]] source line 24: reads `bsn_prm`

## Parameters
| Parameter                | Type      | Units    | Meaning                                                                                                                                                                                     | Source                       |               Reader line | Osu_1hru |
| ------------------------ | --------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------- | ------------------------: | -------- |
| `bsn_prm%evlai`          | `real`    | none     | leaf area index at which no evap occurs                                                                                                                                                     | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 3        |
| `bsn_prm%ffcb`           | `real`    | none     | initial soil water cont expressed as a fraction of fc                                                                                                                                       | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0        |
| `bsn_prm%surlag`         | `real`    | days     | surface runoff lag time (days)                                                                                                                                                              | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 1        |
| `bsn_prm%adj_pkr`        | `real`    | none     | peak rate adjustment factor in the subbasin                                                                                                                                                 | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 1        |
| `bsn_prm%prf`            | `real`    |          | peak rate factor for peak rate equation                                                                                                                                                     | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 1        |
| `bsn_prm%spcon`          | `real`    |          | not used                                                                                                                                                                                    | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0        |
| `bsn_prm%spexp`          | `real`    |          | not used                                                                                                                                                                                    | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 1        |
| `bsn_prm%cmn`            | `real`    |          | rate factor for mineralization on active org N - 0.0003 -> 0.003                                                                                                                            | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0        |
| `bsn_prm%n_updis`        | `real`    |          | nitrogen uptake dist parm                                                                                                                                                                   | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 20       |
| `bsn_prm%p_updis`        | `real`    |          | phosphorus uptake dist parm                                                                                                                                                                 | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 20       |
| `bsn_prm%nperco`         | `real`    |          | nitrate perc coeff (0-1) 0 = conc of nitrate in surface runoff is zero 1 = perc has same conc of nitrate as surf runoff                                                                     | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0.1      |
| `bsn_prm%pperco`         | `real`    |          | phos perc coeff (0-1) 0 = conc of sol P in surf runoff is zero 1 = percolate has some conc of sol P as surf runoff                                                                          | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 10       |
| `bsn_prm%phoskd`         | `real`    |          | phos soil partitioning coef                                                                                                                                                                 | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 175      |
| `bsn_prm%psp`            | `real`    |          | phos availability index                                                                                                                                                                     | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0.4      |
| `bsn_prm%rsdco`          | `real`    |          | residue decomposition coeff                                                                                                                                                                 | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0.05     |
| `bsn_prm%percop`         | `real`    |          | pestcide perc coeff (0-1)                                                                                                                                                                   | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0.5      |
| `bsn_prm%msk_co1`        | `real`    |          | calibration coeff to control impact of the storage time constant for the reach at bankfull depth                                                                                            | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0.75     |
| `bsn_prm%msk_co2`        | `real`    |          | calibration coefficient used to control impact of the storage time constant for low flow (where low flow is when river is at 0.1 bankfull depth) upon the Km value calculated for the reach | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0.25     |
| `bsn_prm%msk_x`          | `real`    |          | weighting factor control relative importance of inflow rate and outflow rate in determining storage on reach                                                                                | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0.2      |
| `bsn_prm%nperco_lchtile` | `real`    |          | n concentration coeff for tile flow and leach from bottom layer                                                                                                                             | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0.5      |
| `bsn_prm%evrch`          | `real`    |          | reach evaporation adjustment factor                                                                                                                                                         | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0.6      |
| `bsn_prm%scoef`          | `real`    |          | channel storage coefficient (0-1)                                                                                                                                                           | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 1        |
| `bsn_prm%cdn`            | `real`    |          | denitrification exponential rate coefficient                                                                                                                                                | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 1.4      |
| `bsn_prm%sdnco`          | `real`    |          | denitrification threshold frac of field cap                                                                                                                                                 | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 1.3      |
| `bsn_prm%bact_swf`       | `real`    |          | frac of manure containing active colony forming units                                                                                                                                       | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0.15     |
| `bsn_prm%tb_adj`         | `real`    |          | adjustment factor for subdaily unit hydrograph basetime                                                                                                                                     | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0        |
| `bsn_prm%cn_froz`        | `real`    |          | parameter for frozen soil adjustment on infiltraion/runoff                                                                                                                                  | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0        |
| `bsn_prm%dorm_hr`        | `real`    |          | time threshold used to define dormant (hrs)                                                                                                                                                 | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0        |
| `bsn_prm%plaps`          | `real`    | mm/km    | precipitation lapse rate: mm per km of elevation difference                                                                                                                                 | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0        |
| `bsn_prm%tlaps`          | `real`    | deg C/km | temperature lapse rate: deg C per km of elevation difference                                                                                                                                | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0        |
| `bsn_prm%nfixmx`         | `real`    |          | max daily n-fixation (kg/ha)                                                                                                                                                                | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 20       |
| `bsn_prm%decr_min`       | `real`    |          | minimum daily residue decay                                                                                                                                                                 | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0.01     |
| `bsn_prm%rsd_covco`      | `real`    |          | residue cover factor for computing frac of cover                                                                                                                                            | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0.3      |
| `bsn_prm%urb_init_abst`  | `real`    |          | maximum initial abstraction for urban areas when using Green and Ampt                                                                                                                       | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 1        |
| `bsn_prm%petco_pmpt`     | `real`    |          | PET adjustment (%) for Penman-Montieth and Preiestly-Taylor methods                                                                                                                         | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 1        |
| `bsn_prm%uhalpha`        | `real`    |          | alpha coeff for est unit hydrograph using gamma func                                                                                                                                        | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 5        |
| `bsn_prm%eros_spl`       | `real`    |          | coeff of splash erosion varying 0.9-3.1                                                                                                                                                     | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 1        |
| `bsn_prm%rill_mult`      | `real`    |          | rill erosion coefficient                                                                                                                                                                    | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0.7      |
| `bsn_prm%eros_expo`      | `real`    |          | exponential coefficient for overland flow                                                                                                                                                   | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 1.2      |
| `bsn_prm%c_factor`       | `real`    |          | scaling parameter for cover and management factor for overland flow erosion                                                                                                                 | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0.03     |
| `bsn_prm%ch_d50`         | `real`    |          | median particle diameter of main channel (mm)                                                                                                                                               | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 50       |
| `bsn_prm%co2`            | `real`    |          | co2 concentration at start of simulation (ppm)                                                                                                                                              | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 1.57     |
| `bsn_prm%day_lag_mx`     | `integer` |          | max days to lag hydrographs for hru, ru and channels non-draining soils                                                                                                                     | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0        |
| `bsn_prm%igen`           | `integer` |          | random generator code: 0 = use default numbers 1 = generate new numbers in every simulation                                                                                                 | [[basin_module.f90#bsn_prm]] | [[basin_read_prm.f90]]:24 | 0        |
