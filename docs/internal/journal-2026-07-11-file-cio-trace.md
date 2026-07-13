---
title: file.cio trace — first step
kind: journal
status: partial
created: 2026-07-11
updated: 2026-07-11
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: Osu_1hru
tags: [journal, file-cio, inputs, reader]
---

# 2026-07-11 - file.cio trace, first step

## Goal

Begin the first end-to-end SWAT+ trace: understand what `file.cio` is, how it is read, and where its contents are stored — the entry point to the whole input system.

## Actions

- Workspace housekeeping completed first: docs converted to workspace-relative paths, upstream source registered as a git submodule (pinned `cb442f7`), `.gitignore` added, `GEMINI.md` removed, `main.f90` generated (no cmake on the machine, so via equivalent placeholder substitution), branch merged to `main` and pushed to `origin`.
- Inspected [`Osu_1hru/file.cio`](../../VSProj/SWAT/Osu_1hru/file.cio) directly (32 lines).
- Grepped `src/` for `file.cio` to locate the reader.

## Observations

- **Verified**: `file.cio` is a flat section->filename manifest; each line is a lowercase section keyword followed by filename slots (`null` = unused). The full `Osu_1hru` mapping is recorded in the canonical note.
- **Verified**: the reader is in [`readcio_read.f90`](../../SWATPLUS/swatplus/src/readcio_read.f90) — L19 `!! read file.cio`, L20 `inquire(...)`, L22 `open(107,file="file.cio")`.
- **Partial**: the storage type is *likely* in [`input_file_module.f90`](../../SWATPLUS/swatplus/src/input_file_module.f90) (L5 header comment `!! file.cio input file`), but the type definition and parse loop have not been read yet.

## Corrections

- None this session for this topic.

## Promoted records

- Created topic note [`topics/file-cio.md`](../topics/file-cio.md) (status `partial`).

## Next session

Read `readcio_read.f90` in full: how it matches each section keyword, how many filename slots it reads per section, and which field of which derived type in `input_file_module.f90` receives them. Then follow one filename (e.g. `time.sim`) from this structure into its own reader — that closes input -> reader -> structure -> consumer for the first trace.
