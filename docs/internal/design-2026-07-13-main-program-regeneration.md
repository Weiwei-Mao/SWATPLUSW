---
title: SWAT+ main-program regeneration
kind: design
status: approved
created: 2026-07-13
updated: 2026-07-13
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: general
tags: [build, cmake, main-program, versioning]
---

# SWAT+ Main-program Regeneration Design

## Goal

Regenerate `SWATPLUS/swatplus/src/main.f90` from the maintained
`main.f90.in` template with truthful version, compiler, timestamp, and host
values, and strengthen the existing canonical knowledge note with a concise
description of the relationship between the two files.

## Source identity

The workspace pins SWAT+ commit
`cb442f7c05fc3bfc34349c446010f452d2737ca0`. The official upstream history
places that commit two commits after tag `62.0.0`, so its descriptive version
is `62.0.0-2-gcb442f7`.

The configured personal fork does not publish the upstream tag refs. CMake
would therefore fall back to `unknown` if allowed to run `git describe --tags`
against only that fork. The regeneration will pass
`-DTAG=62.0.0-2-gcb442f7` explicitly so the generated banner identifies the
actual source revision.

## Documentation design

Update the existing canonical note
`docs/knowledge/architecture/main-program-generation.md`; do not create a
duplicate topic note. Add a concise relationship statement explaining that:

- `main.f90.in` is the tracked, maintained source template and the only file
  in which durable main-program edits belong.
- CMake reads the template, replaces its `@...@` build placeholders, and
  writes the ignored generated file `main.f90`.
- The Fortran compiler and Intel `/fpp` preprocessing compile the generated
  file but do not perform CMake placeholder substitution.
- Visual Studio references `main.f90`, so regeneration must precede its
  build whenever the template or build metadata changes.

Update the note's `updated` date and evidence without changing unrelated
knowledge records or indexes; the canonical note is already indexed.

## Generation design

Run the project's existing CMake configure rule from
`SWATPLUS/swatplus`, using an out-of-source Debug configuration, Intel `ifx`,
and the explicit descriptive tag. CMake remains the only generator; no manual
editing of `main.f90` is permitted.

The expected data flow is:

```text
main.f90.in + TAG + CMake compiler/host/time variables
    -> configure_file(...)
    -> main.f90
    -> Visual Studio Intel Fortran build
```

If the current shell cannot discover `ifx`, use the installed Visual Studio
CMake and Intel oneAPI environment rather than inventing compiler metadata.
If CMake cannot complete configuration, stop with the original generated file
preserved and report the missing environment component.

## Verification

The result is acceptable only when all of the following hold:

1. `main.f90.in` is unchanged.
2. `main.f90` contains `62.0.0-2-gcb442f7` and contains no unresolved
   `@...@` placeholders.
3. Differences between the template and generated file are limited to the
   intended placeholder substitutions.
4. The `Debug|x64` Intel Visual Studio project rebuilds successfully.
5. Running the small `Osu_1hru` scenario writes a `simulation.out` banner with
   the resolved version and compiler metadata.
6. Unrelated tracked and untracked workspace files remain untouched.

## Scope boundary

This work changes build metadata and documentation only. It does not change a
scientific equation, model input, object selection, simulation process, or
scenario configuration.
