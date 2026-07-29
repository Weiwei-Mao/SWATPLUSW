---
type: reference
tags:
  - swat/reference
  - swat/documentation
  - swat/to-mirror
---

# SWAT+ Online Documentation

URL: https://swatplus.gitbook.io/io-docs

Accessed: 2026-06-03

Status: Link collected; local searchable mirror still needed.

The site includes SWAT+ input/output documentation and theoretical documentation. SWAT+ is one of the primary target models for this project, so the local mirror should preserve the next-level page titles rather than only the top section names.

## Priority Input-File Sections To Mirror

- SWAT+ Input Files
  - Input File Format
  - Master File (`file.cio`)
  - Simulation Settings
  - Climate
  - Basin
  - Landscape Units
  - Routing Units
  - Hydrologic Response Units
  - Hydrology
  - Soils
  - Landuse and Management
  - Decision Tables
  - Management Practices
  - Structural Practices
  - Databases
  - Aquifers
  - GWFlow
  - Channels
    - `channel-lte.cha`
      - `id`
      - `name`
      - `ini`
      - `hyd`
      - `nut`
    - `initial.cha`
    - `hyd-sed-lte.cha`
    - `nutrients.cha`
      - `name`
      - `plt_n`
      - `plt_p`
      - `alg_stl`
      - `ben_disp`
      - `ben_nh3n`
      - `ptln_stl`
      - `ptlp_stl`
      - `cst_stl`
      - `ben_cst`
      - `cbn_bod_co`
      - `air_rt`
      - `cbn_bod_stl`
      - `ben_bod`
      - `bact_die`
      - `cst_decay`
      - `nh3n_no2n`
      - `no2n_no3n`
      - `ptln_nh3n`
      - `ptlp_solp`
      - `q2e_lt`
      - `q2e_alg`
      - `chla_alg`
      - `alg_n`
      - `alg_p`
      - `alg_o2_prod`
      - `alg_o2_resp`
      - `o2_nh3n`
      - `o2_no2n`
      - `alg_grow`
      - `alg_resp`
      - `slr_act`
      - `lt_co`
      - `const_n`
      - `const_p`
      - `lt_nonalg`
      - `alg_shd_l`
      - `alg_shd_nl`
      - `nh3_pref`
  - Reservoirs and Ponds
  - Wetlands
  - Initialization
  - Constituents
    - `constituents.cs`
  - Point Sources and Inlets
  - Connectivity
    - `'object'.con`
    - `aqu_cha.lin`
    - `chan_surf.lin`
  - Water Allocation
  - Calibration

## Priority Output-File Sections To Mirror

- SWAT+ Output Files
  - Output File Format
  - Debugging Outputs
  - Soil
  - Management
  - Flow Duration Curve
  - Water Balance
  - Nutrient Balance
  - Losses
  - Plant and Weather
  - Channel
  - Aquifer
  - Reservoir
  - Recall
  - Hydrographs
  - Routing Unit
  - Pesticides
  - Object Outputs

## Priority Theory Sections To Mirror

- Theoretical Documentation
  - Section 1: Climate
  - Section 2: Hydrology
    - Chapter 2:1 Surface Runoff
    - Chapter 2:2 Evapotranspiration
    - Chapter 2:3 Soil Water
    - Chapter 2:4 Groundwater
  - Section 3: Nutrients/Pesticides
    - Chapter 3:1 Nitrogen
    - Phosphorus
    - Pesticides
    - Bacteria
    - Carbon
  - Section 4: Erosion
    - Sediment
    - Nutrient Transport
    - Pesticide Transport
    - Bacteria Transport
    - Water Quality Parameters
  - Section 5: Land Cover/Plant
  - Section 6: Management Practices
  - Section 7: Main Channel Processes
    - Water Routing
    - Sediment Routing
    - In-Stream Nutrient Processes
    - In-Stream Pesticide Transformations
    - Bacteria Routing
    - Heavy Metal Routing
  - Section 8: Water Bodies
    - Impoundment Water Routing
    - Sediment In Water Bodies
    - Nutrients In Water Bodies
    - Pesticides In Water Bodies
    - Bacteria In Water Bodies
  - References

Recommendation: create a local Markdown or HTML mirror of at least the channel, constituent, nutrient, erosion, hydrology, and water-body pages before detailed source-grounded comparison work. A local copy is needed for reliable `rg` searching, offline lookup, stable quoting, and linking evidence to source-code traces.
