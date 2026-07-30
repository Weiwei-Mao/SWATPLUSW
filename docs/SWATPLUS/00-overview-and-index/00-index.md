---
type: overview
tags:
  - swat/overview
  - swat/index
title: SWAT+ documentation entrance
purpose: "Main reading entrance for the local SWAT+ notes"
---

# SWAT+ Documentation Entrance

Start here when you need to understand the local SWAT+ notes. This folder is
organized as a reading path, not as an exhaustive generated index. The goal is
to answer the main modeling questions first, then point to exact source,
input-file, and output-file notes when you need details.

> **Source version:** these notes track SWAT+ Revision 62 (`SWATPLUS/swatplus` submodule pinned at `cb442f7c`, 2026-07-06). When the source moves, refresh the baseline in [[08-osu-1hru-baseline-and-debug]].

## File Order

| Order | File | Topic | Use it for |
|---|---|---|---|
| 00 | [[00-index]] | Entrance | Main navigation page for this documentation set. |
| 01 | [[01-input-file-system]] | Input-file system | General map of `file.cio`, `object.cnt`, connect files, property files, databases, routing, and runtime state. |
| 02 | [[02-hru-input-chain]] | HRU input chain | Detailed HRU map for soil, topography, hydrology, plant community, management, snow, field, storage, and initial nutrient/carbon state. |
| 03 | [[03-spatial-object-input-chains]] | Other spatial objects | Object chains for HRU-LTE, RU, GWFLOW, aquifer, channel, reservoir, recall, exco, delivery ratio, outlet, SWAT-DEG channel, canal, pump, aquifer2D, herd, and water rights. |
| 04 | [[04-management-schedule-and-operations]] | Management operations | Detailed explanation of `landuse.lum`, `management.sch`, operation databases, manual operations, and auto operations. |
| 05 | [[05-online-documentation]] | External docs | Official and online SWAT+ documentation sections to compare or mirror. |
| 06 | [[06-code-logic-issues]] | Source logic issues | Working log of possible SWAT+ channel, routing, sediment, and water-quality code issues. |
| 07 | [[07-osu-1hru-input-inventory]] | Debug scenario inputs | Configured files, active objects, and record chains in the default one-HRU scenario. |
| 08 | [[08-osu-1hru-baseline-and-debug]] | Debug baseline | Reproducible build, run, breakpoint, and output checks for the default scenario. |

## Main Questions

| Question | Start with | Then use |
|---|---|---|
| How do SWAT+ input files connect to HRUs, channels, reservoirs, and other objects? | [[01-input-file-system]] | [[02-hru-input-chain]] for HRUs or [[03-spatial-object-input-chains]] for other objects. |
| For one HRU, which files define soil, plant, management, field, snow, and initial nutrient/carbon state? | [[02-hru-input-chain]] | [[hru.con]], [[hru-data.hru]], [[landuse.lum]], [[plant.ini]], [[management.sch]], [[soils.sol]], [[soil_plant.ini]], [[nutrients.sol]]. |
| What exactly does `management.sch` do? | [[04-management-schedule-and-operations]] | [[landuse.lum]], [[management.sch]], [[tillage.til]], [[fertilizer.frt]], [[pesticide.pes]], [[graze.ops]], [[harv.ops]], [[irr.ops]], [[chem_app.ops]], [[fire.ops]], [[sweep.ops]]. |
| What are the non-HRU spatial object chains, including SWAT-DEG channel, aquifer, RU, GWFLOW, canal, and pump? | [[03-spatial-object-input-chains]] | [[hyd_connect.f90]], [[hyd_read_connect.f90]], [[command.f90]], then object-specific `.con` notes. |
| Which channel or water-quality source blocks look logically unreasonable or inconsistent with theory? | [[06-code-logic-issues]] | [[sd_channel_sediment3.f90]], [[ch_rtmusk.f90]], [[ch_watqual4.f90]], and online theory notes. |
| Which file is opened by which reader? | [[01-input-file-system]] | [[file.cio]], then the matching source routine note under `01-source-routines/`. |
| Where is a source routine, module variable, input file, or output file documented? | The folders below | `01-source-routines/`, `02-modules-and-variables/`, `03-input-files/`, `04-output-files/`. |

## Reading Paths

### Input Files

1. Start with [[01-input-file-system]] for the general control pattern.
2. Use [[file.cio]] to confirm whether a filename is controlled by `file.cio`.
3. If the file is hardcoded, open the reader note and inspect its
   `inquire (file=...)` line.

### HRU And Management

1. Start with [[02-hru-input-chain]] for the HRU-only diagram.
2. Open [[04-management-schedule-and-operations]] when the question is about
   planting, harvest, tillage, fertilizer, irrigation, grazing, auto operations,
   or other scheduled events.
3. Open exact file notes such as [[hru.con]], [[hru-data.hru]],
   [[landuse.lum]], [[plant.ini]], [[management.sch]], [[soils.sol]],
   [[soil_plant.ini]], and [[nutrients.sol]].

### Other Spatial Objects

1. Start with [[03-spatial-object-input-chains]].
2. Use the object summary table to find the connect file and property file.
3. Open source anchors such as [[hyd_connect.f90]], [[hyd_read_connect.f90]],
   [[command.f90]], and object-specific readers.

### Exact Lookup

1. Use `01-source-routines/` for source routine notes.
2. Use `02-modules-and-variables/` for module and derived-type notes.
3. Use `03-input-files/` for exact input-file fields and reader links.
4. Use `04-output-files/` for output-file columns and writer links.

## Folder Structure

| Folder | Contents | Note type |
|---|---|---|
| `00-overview-and-index/` | Main entrance and hand-maintained learning maps | `type: overview` or `type: guide` |
| `01-source-routines/` | Program and subroutine notes, one per source file | `type: source` |
| `02-modules-and-variables/` | `*_module.f90` notes for derived types and global variables | `type: module` |
| `03-input-files/` | `file.cio` plus one note per input file | `type: input` |
| `04-output-files/` | `.out`, `.txt`, and other output file notes | `type: output` |

## Regenerate

After source updates, rerun the generator to refresh structured fields. Content
between USER-NOTES markers is preserved in source and module notes. Generated
input/output notes may be rewritten, so keep durable explanations in the
hand-maintained numbered overview notes or update the generator before
rerunning.

```bash
python "docs/_tools/gen_swat_notes.py"
```
