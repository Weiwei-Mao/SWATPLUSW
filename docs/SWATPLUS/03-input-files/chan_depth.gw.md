---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: chan_depth.gw
ext: gw
cio_field: []
read_by:
  - gwflow_chan_read.f90
purpose: ""
---

# chan_depth.gw

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[gwflow_chan_read.f90]]

## File Structure
- [[gwflow_chan_read.f90]] source line 90: reads `header`
- [[gwflow_chan_read.f90]] source line 91: reads `header`

## Parameters
(No parameter table detected automatically. Check the reader routines above for manual interpretation.)
