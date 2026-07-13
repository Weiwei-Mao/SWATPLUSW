---
title: Simplified SWAT+ learning documentation structure
kind: design
status: approved
created: 2026-07-13
updated: 2026-07-13
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: general
tags: [documentation, information-architecture, learning]
---

# Simplified SWAT+ Learning Documentation Structure

## Goal

Make the documentation easy to enter and read without losing the detailed
technical knowledge and investigation history already recorded. A learner
should encounter one main entrance, two short companion documents, and direct
links to deeper topic notes only when more detail is useful.

## Reader path

The normal reading path will contain exactly three documents:

1. `docs/README.md` - the single learning entrance, overall mental model,
   reading order, current learning status, and direct links to detailed topics.
2. `docs/model-structure.md` - program entry, initialization, time control,
   object dispatch, and the responsibility of major code areas.
3. `docs/input-output.md` - the path from configuration and input readers,
   through stored state and model processes, to aggregation and output.

The root `README.md` remains outside this learning path. It will be shortened
to the project purpose, workspace map, essential setup/configuration, and one
prominent link to `docs/README.md`.

## Final folder structure

```text
README.md
AGENTS.md

docs/
|-- README.md
|-- model-structure.md
|-- input-output.md
|-- topics/
`-- internal/
```

`topics/` contains detailed, source-backed model notes that a main document
links to at the point where the detail matters. It has no intermediate index
files and remains flat until the number of notes makes grouping necessary.

`internal/` contains project-maintenance material such as dated journals,
designs, and authoring templates. It is not part of the normal learning path.
Its files use descriptive prefixes such as `journal-`, `design-`, and
`template-`, so additional subdirectories and index files are unnecessary.

## Content migration

The existing detailed notes move into `docs/topics/` without losing their
metadata or technical content:

| Current file | Destination |
| --- | --- |
| `knowledge/architecture/main-program-generation.md` | `topics/main-program-generation.md` |
| `knowledge/architecture/simulation-control-flow.md` | `topics/simulation-control-flow.md` |
| `knowledge/inputs/file-cio.md` | `topics/file-cio.md` |
| `knowledge/debugging/osu-1hru-scenario.md` | `topics/osu-1hru-scenario.md` |
| `knowledge/debugging/visual-studio-intel-fortran.md` | `topics/visual-studio-intel-fortran.md` |
| `knowledge/reference/deepwiki-swatplus.md` | `topics/deepwiki-swatplus.md` |

Existing journals, approved designs, and templates move into
`docs/internal/`. Their filenames gain a role prefix when the role is not
already obvious. The empty category indexes under `knowledge/`, `traces/`,
and `decisions/` are removed after their durable rules are incorporated into
`AGENTS.md`, `docs/README.md`, or the corresponding templates.

The current untracked `docs/Debugging.md` contains only a `Main.f90` heading.
It will be preserved verbatim as `docs/internal/draft-debugging.md`, clearly
separating the user draft from verified learning material. The unrelated
untracked simulation output files under `VSProj/SWAT/` remain untouched.

## Main-document responsibilities

### `docs/README.md`

This is a readable introduction rather than a directory catalog. It explains
the purpose of the knowledge project, gives the compact execution mental
model, points to the two companion documents, lists current verified and
partial understanding, and links directly to detailed topic notes. It also
states that a missing topic is an area still to be learned rather than an
invitation to fill gaps with inference.

### `docs/model-structure.md`

This document answers: where does execution begin, how is a normal simulation
controlled, which major object types are dispatched, and where should a
learner look next? It summarizes verified structure and links to detailed
topic notes for exact source routines, generation details, and debugger
evidence.

### `docs/input-output.md`

This document answers: how does configuration enter the model, where is it
stored, how does it reach calculations, and how are results accumulated and
written? The current input-reader knowledge is explicitly marked partial.
Processes and outputs that have not yet been traced are presented as learning
targets, not verified facts.

## Navigation and maintenance rules

- The root `README.md` links to only one documentation entrance:
  `docs/README.md`.
- `docs/README.md` links to the two companion documents and directly to every
  current detailed topic.
- Companion documents link to topic notes in context; topic notes link back to
  the relevant companion document rather than to category indexes.
- New durable technical knowledge becomes a focused file in `docs/topics/`.
- Dated learning history and documentation-process material belongs in
  `docs/internal/` and is not added to the required reading path.
- `AGENTS.md` retains the evidence/status workflow but is updated for the new
  paths and for the fact that the current workspace root is a Git repository.
- Repeated explanations are replaced by a short summary plus one link to the
  authoritative detailed note.

## Verification

The reorganization is complete only when:

1. The `docs/` root contains the three reader documents and only the
   `topics/` and `internal/` support folders.
2. A reader can move from root `README.md` to `docs/README.md`, then understand
   the major code structure and input-to-output flow without opening an
   internal record.
3. Every substantive existing knowledge note remains reachable through one of
   the three reader documents.
4. All local Markdown links resolve after the moves.
5. Topic metadata and distinctions among `verified`, `partial`, and
   `hypothesis` remain intact.
6. Statements that the workspace root is not a Git repository are corrected.
7. No Fortran source, Visual Studio project, scenario input, generated output,
   or unrelated untracked file is modified.

## Scope boundary

This work changes documentation structure, navigation, and duplicated wording
only. It does not change SWAT+ behavior, scientific content, build settings,
scenario configuration, or the pinned source revision.
