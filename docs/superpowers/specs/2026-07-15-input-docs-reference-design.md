---
title: Input documentation reference structure
status: superseded
created: 2026-07-15
scope: docs
superseded_by: 2026-07-15-io-docs-classification-design.md
---

# Input Documentation Reference Structure

## Goal

Reorganize the SWAT+ learning documentation so input-file knowledge has a clear home and can grow into a full SWAT+ input-file reference, including optional files that are not active in the current `Osu_1hru` scenario.

The current `docs/topics/` folder mixes conceptual notes, scenario notes, setup notes, and detailed input-file references. The new structure separates durable per-file references from broader conceptual notes.

## Target Structure

```text
docs/
  README.md
  model-structure.md
  tracing-guide.md
  input-files.md
  inputs/
    file-cio.md
    time-sim.md
    print-prt.md
    object-cnt.md
    codes-bsn.md
    parameters-bsn.md
    ...
  topics/
    simulation-control-flow.md
    main-program-generation.md
    qswat-hru-routing-unit.md
    osu-1hru-scenario.md
    ...
  internal/
    debug-inbox.md
```

## File Roles

`docs/input-files.md` is the top-level map of SWAT+ input files. It classifies files by domain, gives a short description, links to detailed pages in `docs/inputs/`, and marks whether each page is verified, partial, or not yet traced.

`docs/inputs/*.md` contains one detailed reference page per SWAT+ input file. These pages are file-centered and should explain the meaning of each parameter or column when known.

`docs/topics/*.md` remains for concepts and workflows that are not single input-file references, such as control flow, model architecture, QSWAT generation behavior, build setup, and scenario-specific debugging notes.

`docs/tracing-guide.md` remains the tracing guide. It should link to `docs/input-files.md` for the catalog and to specific `docs/inputs/*.md` pages when a traced input file is discussed.

## Per-Input Page Template

Each file in `docs/inputs/` should use this structure unless the file is too small to justify every section:

```md
# `example.ext`

## Purpose
## Role In SWAT+
## File Format
## Fields And Parameters
## Reader Path
## Internal Storage
## Defaults And Conversions
## Downstream Consumers
## Scenario Evidence
## Open Questions
## Related Files
```

Required front matter for substantive pages:

```yaml
---
title: example.ext input file
kind: input-reference
status: partial
created: YYYY-MM-DD
updated: YYYY-MM-DD
source_revision: <git-sha>
scenario: Osu_1hru
tags: [inputs]
---
```

## Naming Rules

Use lowercase, hyphen-separated Markdown filenames. Replace the dot in the input filename with a hyphen:

| Input file | Documentation page |
| --- | --- |
| `file.cio` | `inputs/file-cio.md` |
| `parameters.bsn` | `inputs/parameters-bsn.md` |
| `weather-sta.cli` | `inputs/weather-sta-cli.md` |
| `hru-data.hru` | `inputs/hru-data-hru.md` |
| `management.sch` | `inputs/management-sch.md` |

When multiple SWAT+ input files share a common extension but different roles, keep one page per actual file name, not one page per extension.

## Classification Groups

`docs/input-files.md` should classify files under these initial groups:

- Simulation and basin files
- Climate files
- Connection files
- Channel and SWAT-DEG channel files
- Reservoir and wetland files
- Routing unit files
- HRU files
- Recall, aquifer, and region files
- HRU hydrology, topography, and structural files
- Parameter database files
- Management operation files
- Land use and management files
- Calibration files
- Initial condition files
- Soil files
- Decision table files
- Constituents, salt, and optional module files
- Generated support and output-like files

The map should include optional files even when they are not active in `Osu_1hru`, but optional or untraced files must be clearly marked.

## Migration Plan

1. Create `docs/inputs/`.
2. Move existing file-specific topic notes into `docs/inputs/`:
   - `topics/file-cio.md` to `inputs/file-cio.md`
   - `topics/codes-bsn.md` to `inputs/codes-bsn.md`
   - `topics/parameters-bsn.md` to `inputs/parameters-bsn.md`
   - `topics/print-prt.md` to `inputs/print-prt.md`
   - `topics/object-cnt.md` to `inputs/object-cnt.md`
   - `topics/om-water-ini.md` to `inputs/om-water-ini.md`
3. Promote `topics/input-files-catalog.md` into `docs/input-files.md` and expand its role from scenario catalog to full input-file map.
4. Update links in `docs/README.md`, `docs/tracing-guide.md`, and migrated files.
5. Leave scenario-specific and conceptual files in `docs/topics/`.
6. Add stub pages only when they improve navigation. Stubs must be explicit about their status and avoid pretending untraced fields are known.

## Evidence Standards

Use these statuses consistently:

| Status | Meaning |
| --- | --- |
| `verified` | Supported by source code, scenario input, or reproducible runtime observation. |
| `partial` | Some reader paths or fields are known, but important consumers or defaults remain untraced. |
| `not traced` | The file is identified, but reader path or field meanings are not yet documented. |
| `optional` | The file is valid SWAT+ input but not active in the current scenario evidence. |
| `hypothesis` | Plausible but not yet supported by direct evidence. |

Per-file pages should distinguish raw file values from final runtime values when defaults or conversions are applied.

## Validation

After reorganization:

- `rg "topics/(file-cio|codes-bsn|parameters-bsn|print-prt|object-cnt|om-water-ini|input-files-catalog)" docs` should find no stale links.
- `rg "input-files-catalog" docs` should find no stale references unless a historical note explicitly mentions the old file.
- Every migrated page should still link to related notes with working relative paths.
- The docs README should describe the new boundary between `input-files.md`, `inputs/`, `topics/`, and `internal/`.
- Git status should not include unrelated local scenario artifacts.

## Non-Goals

- Do not fully document every SWAT+ input file in the first reorganization pass.
- Do not rewrite conceptual notes unless link updates or boundary clarifications are needed.
- Do not treat generated outputs as primary input references until their reader or writer role is traced.
