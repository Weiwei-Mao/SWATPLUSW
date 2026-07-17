---
type: overview
tags:
  - swat/overview
  - swat/index
---

# Module And Variable Index

## All Modules

```dataview
TABLE defines_types AS "Defined types", defines_vars AS "Module-level variables"
FROM "docs/SWATPLUS/02-modules-and-variables"
SORT file ASC
```

## Functional Domain Tags

Add domain tags while reading so modules can be browsed by process area. Suggested values:

`swat/domain-control` `swat/domain-hydrology` `swat/domain-sediment` `swat/domain-nutrients` `swat/domain-climate`
`swat/domain-channel` `swat/domain-reservoir` `swat/domain-groundwater` `swat/domain-plant` `swat/domain-calibration` `swat/domain-utility`

## Browse Modules By Domain

```dataview
TABLE file, defines_types
FROM "docs/SWATPLUS/02-modules-and-variables"
WHERE contains(tags, "#swat/domain-hydrology")
```
