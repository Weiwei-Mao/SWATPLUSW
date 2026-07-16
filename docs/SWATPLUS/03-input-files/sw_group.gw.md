---
type: input
tags:
  - swat/input
  - swat/auxiliary-input
file: sw_group.gw
ext: gw
cio_field: []
read_by:
  - gwflow_read.f90
purpose: ""
---

# sw_group.gw

> [!info] Input File
> Referenced directly by source code or by a default file-name constant outside the main `file.cio` list.

## Overview
- **Declared in `file.cio` field**: not listed directly; referenced by source code or a default file-name constant.
- **Format source**: generated from Fortran `open`/`read` statements and module/type comments.
- **Format style**: SWAT+ text input; most readers use list-directed Fortran reads.

## Reader Routines
- [[gwflow_read.f90]]

## File Structure
- [[gwflow_read.f90]] source line 2282: reads `header`
- [[gwflow_read.f90]] source line 2283: reads `header`
- [[gwflow_read.f90]] source line 2288: reads `'`, `iostat=eof) split_line_buf`
- [[gwflow_read.f90]] source line 2300: reads `header`
- [[gwflow_read.f90]] source line 2301: reads `header`
- [[gwflow_read.f90]] source line 2303: reads `') split_line_buf`

## Parameters
(No parameter table detected automatically. Check the reader routines above for manual interpretation.)
