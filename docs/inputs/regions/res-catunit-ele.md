---
title: res_catunit.ele input file
kind: input-reference
status: not traced
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: source-default
tags: [inputs, stub]
---

# `res_catunit.ele`

## Purpose

Input file for regions; source slot ele_res.

## Role In SWAT+

This page is a source-aligned input-reference stub for `res_catunit.ele`. It exists so `docs/inputs/` has a durable categorized page for each known SWAT+ input file or input-file family.

Scenario status: Not selected by the current `Osu_1hru` `file.cio`; treat as optional or source-default until traced in a scenario.

## File Format

Not yet traced. Add the header lines, data layout, column meanings, units, and required/optional fields after the reader path is inspected.

## Reader Path

- Source inventory: input_file_module.f90 default slot.
- Source slot: ele_res
- Reader routine: not yet traced in this page.

## Fields And Parameters

Not yet documented. Do not infer parameter meanings from names alone; trace the reader and storage type first.

## Defaults And Conversions

Not yet traced.

## Downstream Consumers

Not yet traced.

## Scenario Evidence

Not selected by the current `Osu_1hru` `file.cio`; treat as optional or source-default until traced in a scenario.

## Open Questions

- Which reader opens this file in the current source revision?
- Which module, derived type, or array stores each parsed field?
- Which calculations or output writers consume the parsed values?

## Related Files

- [SWAT+ input files map](../../input-files.md)
- [SWAT+ tracing guide](../../tracing-guide.md)
