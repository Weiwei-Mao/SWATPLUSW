---
type: input
tags:
  - swat/input
file: recall.rec
ext: rec
cio_field: recall_rec
read_by: []
purpose: "file.cio recall field value; no direct reader opening in_rec%recall_rec was located in the current source."
---

# recall.rec

> [!info] Input File
> Declared in `file.cio` field `recall_rec`. No direct `open(file=in_rec%recall_rec)` reader was located in the current source.

## Overview
- **Declared in `file.cio` field**: `recall_rec`
- **Source status**: placeholder/unused in the current traced path. [[recall_read.f90]] / `recalldb_read` opens hardcoded [[recall_db.rec]] instead.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
(No direct reader located. The active recall database reader is `recalldb_read` in [[recall_read.f90]], which reads [[recall_db.rec]].)

## File Structure
(No line-level read structure detected automatically.)

## Parameters
(No parameter table detected automatically. Check the reader routines above for manual interpretation.)
