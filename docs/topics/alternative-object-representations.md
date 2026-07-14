---
title: Alternative object representations
kind: knowledge
status: partial
created: 2026-07-14
updated: 2026-07-14
source_revision: 5b3705b300d95ebe4914119f056548446bdc208f
scenario: general
tags: [objects, architecture, hru, channel, groundwater]
---

# Alternative Object Representations

## Summary

Some SWAT+ object types are best understood as alternative model representations for the same broad physical system. They are not different physical things; they are different levels or styles of process representation.

The clean pairs we currently recognize are:

| Physical system | Simpler / lumped representation | Detailed / stronger representation |
| --- | --- | --- |
| Land unit | `hru_lte` / `hlt` | `hru` |
| Stream channel | `cha` | `sdc` / SWAT-DEG channel |
| Groundwater / aquifer | `aqu` | `gwflow` |

The first two pairs are high-confidence. The groundwater pair is useful as a mental model, but less exact: `gwflow` is not always a direct one-to-one replacement for every lumped `aqu` setup.

## Land Unit: `hru_lte` And `hru`

Both represent land-area response.

| Object type | Meaning |
| --- | --- |
| `hru_lte` / `hlt` | Simplified land response model. |
| `hru` | Full HRU process model. |

Full HRU uses detailed soil, plant, management, nutrient, carbon, erosion, and constituent process paths.

HRU-LTE keeps a compact land water balance and simplified production/loss response. It uses state such as:

- soil water storage;
- available water capacity;
- porosity;
- curve number;
- simple plant growth;
- simple shallow/deep groundwater storage;
- simplified sediment yield.

Important simplifications in HRU-LTE:

| Part | HRU-LTE simplification |
| --- | --- |
| Soil | Uses lumped storage and simplified texture properties instead of full layer-by-layer soil process state. |
| Plant | Usually one plant type with simplified biomass, LAI, and yield growth. |
| Management | Uses simplified grow-start/grow-end decision-table actions. |
| Nutrients | Most detailed N/P cycling is not simulated; several nutrient outputs are set to zero. |
| Sediment | Uses a simplified MUSLE-style sediment calculation. |
| Groundwater | Uses internal simple shallow/deep storage terms instead of the full groundwater object behavior. |

Practical mental model:

```text
physical land unit
    -> hru_lte  simplified/lumped
    -> hru      detailed/full process
```

## Stream Channel: `cha` And `sdc`

Both represent a stream or river reach.

| Object type | Meaning |
| --- | --- |
| `cha` | Regular channel representation. |
| `sdc` / SWAT-DEG channel | More detailed channel degradation/aggradation representation. |

Regular channel is the simpler/standard channel model. SWAT-DEG is used when the channel representation needs more detailed channel sediment and morphology behavior, including bed degradation, bank erosion, floodplain deposition, and changing channel/floodplain storage.

Practical mental model:

```text
physical stream reach
    -> cha  regular/simple channel representation
    -> sdc  detailed SWAT-DEG channel representation
```

Connection files show the selected representation by object type:

```text
hru001 -> ru001 -> cha001 -> outlet001
hru001 -> ru001 -> sdc001 -> outlet001
```

These two examples should not be read as different kinds of physical watercourse. They are alternative process representations for a stream reach.

## Groundwater / Aquifer: `aqu` And `gwflow`

This pair is conceptually useful but less exact than the HRU and channel pairs.

| Object type | Meaning |
| --- | --- |
| `aqu` | Lumped aquifer object. |
| `gwflow` | More spatial/detailed groundwater-flow representation. |

Use this mental model carefully:

```text
groundwater system
    -> aqu     lumped aquifer representation
    -> gwflow  spatial groundwater-flow representation
```

Unlike `hru_lte`/`hru` and `cha`/`sdc`, this is not always a simple either-or replacement. The exact relationship depends on the configured groundwater files, aquifer objects, routing, and whether the scenario activates `gwflow`.

## What Not To Include In This Category

Do not force every object into this same pattern.

| Object comparison | Why it is not the same kind of pair |
| --- | --- |
| `cha` vs `canal` | Natural stream reach vs managed/artificial conveyance. Related water movement, different physical role. |
| `res` vs wetland/floodplain storage | Both store water, but reservoir and wetland/floodplain are different physical systems. |
| `recall` vs simulated upstream objects | `recall` is an external time series, not a physical process representation of the same object. |
| `exco` vs HRU process simulation | Export coefficient is a simplified loading method, not a full land-unit object replacement. |
| `dr` vs routing/process object | Delivery ratio is an attenuation/transfer method, not a physical object by itself. |

## Debugging Rule

When tracing a scenario, first identify the object type in `object.cnt` and connection files. The object type tells you which representation is active.

Useful source entry points:

| Representation | Main source path |
| --- | --- |
| `hru` | `hru_control.f90` |
| `hru_lte` | `hru_lte_control.f90` |
| `cha` | regular channel readers and channel routines; note that some regular-channel dispatch is currently commented in `command.f90` |
| `sdc` / SWAT-DEG | `sd_channel_read.f90`, `sd_hydsed_init.f90`, and SWAT-DEG channel control paths |
| `aqu` | aquifer readers/control paths |
| `gwflow` | `gwflow_read` and GWFLOW channel/connectivity paths |

Do not assume a file exists just because the object type exists in the source. Confirm the active scenario uses that object count and connection file.

## Related Notes

- [`object.cnt` and SWAT+ object concepts](object-cnt.md)
- [QSWAT+ HRU and routing-unit relationship](qswat-hru-routing-unit.md)
- [SWAT+ model structure](../model-structure.md)
