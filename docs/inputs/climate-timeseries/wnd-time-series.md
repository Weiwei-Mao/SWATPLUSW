---
title: *.wnd input file
kind: input-reference
status: not traced
created: 2026-07-15
updated: 2026-07-15
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: source-default
tags: [inputs, stub]
---

# `*.wnd`

## Purpose

Wind-speed time-series file named by a wind gauge manifest.

## Role In SWAT+

This page is a source-aligned input-reference stub for `*.wnd`. It exists so `docs/inputs/` has a durable categorized page for each known SWAT+ input file or input-file family.

Scenario status: Reached indirectly through climate manifest files when those manifests name matching time-series files.

## File Format

Not yet traced. Add the header lines, data layout, column meanings, units, and required/optional fields after the reader path is inspected.

## Reader Path

- Source inventory: climate manifest target.
- Source slot: not an `input_file_module.f90` field or not yet mapped
- Reader routine: not yet traced in this page.

## Fields And Parameters

Not yet documented. Do not infer parameter meanings from names alone; trace the reader and storage type first.

## Defaults And Conversions

Not yet traced.

## Downstream Consumers

Not yet traced.

## Scenario Evidence

Reached indirectly through climate manifest files when those manifests name matching time-series files.

## Open Questions

- Which reader opens this file in the current source revision?
- Which module, derived type, or array stores each parsed field?
- Which calculations or output writers consume the parsed values?

## Related Files

- [SWAT+ input files map](../../input-files.md)
- [SWAT+ input to output path](../../tracing-guide.md)
