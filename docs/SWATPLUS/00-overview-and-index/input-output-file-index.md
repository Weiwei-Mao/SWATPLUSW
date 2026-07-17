---
type: overview
tags:
  - swat/overview
  - swat/index
---

# Input/Output File Index

## Input Files

> [`file.cio`](file.cio.md) is the controlling input index. Other input-file notes live in `03-input-files/`.

```dataview
TABLE ext AS "Extension", read_by AS "Reader routines", cio_field AS "file.cio field"
FROM "docs/SWATPLUS/03-input-files"
WHERE type = "input"
SORT file ASC
```

## Output Files

```dataview
TABLE ext AS "Extension", written_by AS "Writer routines"
FROM "docs/SWATPLUS/04-output-files"
WHERE type = "output"
SORT file ASC
```

## Controlling Input File

- [[file.cio]] - control file that declares the input files and output path
- [[input-file-architecture]] - how readers locate input files and how file roles differ
- [[hardcoded-input-files]] - literal/default filenames outside the main file.cio list
- [[osu-1hru-input-inventory]] - configured and active inputs in the default debug scenario
