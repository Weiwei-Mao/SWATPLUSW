---
type: overview
tags:
  - swat/overview
  - swat/source
title: Source Reading Checklist
purpose: "Standard checklist for turning SWAT+ source reading into durable, evidence-backed notes."
status: verified
source_revision: "documentation workflow convention"
scenario: "general"
---

# Source Reading Checklist

Use this checklist when promoting a routine note from `swat/to-read` to `swat/read`.

## Required Questions

| Question | Evidence to capture |
|---|---|
| Who calls this routine? | caller note, `main`/controller path, or Dataview back-query |
| What input or output files does it touch? | exact filename, reader/writer line, file unit when useful |
| How is each input filename chosen? | `file.cio` field, hardcoded literal, module default, derived companion, or data-driven child filename |
| What state does it populate or mutate? | module, derived type, array, field, and object index |
| Who consumes that state later? | next routine, controller, equation routine, routing step, writer, or output aggregation |
| What is the smallest verified behavior? | breakpoint/watch value, scenario output signal, or source line evidence |

## Status Vocabulary

| Status | Meaning | Use when |
|---|---|---|
| `verified` | source path and important variables/files are traced | the note can be used as reference without rechecking the basic path |
| `partial` | entry path is known but consumers, units, or edge cases remain incomplete | the note is useful but not enough for model edits |
| `hypothesis` | interpretation is plausible but not yet backed by code evidence | the note contains a working theory |
| `superseded` | kept for history, but a newer note or source path replaced it | old interpretation should not guide new work |

Routine progress tags are separate from status:

| Tag | Meaning |
|---|---|
| `swat/to-read` | generated skeleton or not yet reviewed |
| `swat/in-progress` | currently being traced |
| `swat/read` | reviewed enough for current learning scope |

## Routine Note Pattern

Use this shape inside `USER-NOTES`:

```markdown
## Notes

- Role:
- Caller path:
- File mechanism:
- Populated state:
- Downstream consumers:
- Verification:
- Open questions:
```

Keep generated sections for structure. Put interpretation, assumptions, and source-reading observations in `USER-NOTES` so regeneration preserves them.

## Input File Mechanism Labels

| Label | Definition | Example |
|---|---|---|
| `file.cio-registered` | filename comes from a field populated by [[readcio_read.f90]] | `in_parmdb%plants_plt` -> [[plants.plt]] |
| `hardcoded` | filename is a literal in the reader | [[salt_hru.ini]] |
| `module-default` | filename is a default value on a module variable, not populated by `file.cio` | [[shade_factor.shf]] |
| `derived-companion` | reader derives a secondary filename from a registered file | [[carbon_lyr.bsn]] from [[carbon.bsn]] |
| `data-driven-child` | parent control file stores child filenames read at runtime | precipitation station files listed in [[pcp.cli]] |

## Before Editing Model Behavior

Before recommending or making a model-source change, trace:

1. Input/configuration: controlling file, field, value, and scenario.
2. Reader: routine that opens and parses the file.
3. Data structure: module, type, array, field, and index.
4. Orchestration: controller path from `main`, `time_control`, `command`, or an object controller.
5. Process calculation: smallest routine containing the equation or state transition.
6. Consumers/outputs: routing, mass balance, aggregation, writer, and output column.
7. Verification: breakpoint, watched value, output signal, or regression check.

Label unverified interpretation as `hypothesis` instead of presenting it as fact.
