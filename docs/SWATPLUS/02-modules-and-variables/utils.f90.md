---
type: module
tags:
  - swat/module
  - swat/to-read
file: utils.f90
note_file: utils.f90
module_name: utils
defines_types: []
defines_vars:
  - MAX_TABLE_COLS
  - MAX_NAME_LEN
  - MAX_LINE_LEN
  - header_cols
  - row_field
  - line
  - left_str
  - file_name
  - min_cols
  - titldum
  - nrow
  - lrow
  - ncols
  - nfields
  - start_row_numbr
  - start_data_row_numbr
  - unit
  - found_header_row
  - col_okay
  - file_exists
defines_subroutines:
  - init
  - left_of_delim
  - split_line
  - min_req_cols
  - min_header_cols
  - get_header_columns
  - get_row_fields
  - output_column_warning
defines_functions:
  - exp_w
  - to_lower
  - get_row_idx
  - get_col_count
  - get_num_data_lines
defines_procedures:
  - init
  - left_of_delim
  - split_line
  - min_req_cols
  - min_header_cols
  - get_header_columns
  - get_row_fields
  - output_column_warning
  - exp_w
  - to_lower
  - get_row_idx
  - get_col_count
  - get_num_data_lines
purpose: ""
---

# utils

> [!info] Module
> Defines derived types and module-level variables.

## Defined Types
(No type definitions detected.)

## Variables Defined
### MAX_TABLE_COLS

- **Type**: `integer, parameter`
- **Defined in source**: `utils.f90:4`

### MAX_NAME_LEN

- **Type**: `integer, parameter`
- **Defined in source**: `utils.f90:5`

### MAX_LINE_LEN

- **Type**: `integer, parameter`
- **Defined in source**: `utils.f90:6`

### header_cols

- **Type**: `character(MAX_NAME_LEN)`
- **Defined in source**: `utils.f90:11`
- **Source note**: array of header column names

### row_field

- **Type**: `character(MAX_NAME_LEN)`
- **Defined in source**: `utils.f90:12`
- **Source note**: array of data fields in a data row of data

### line

- **Type**: `character(len=MAX_LINE_LEN)`
- **Defined in source**: `utils.f90:13`
- **Source note**: character string used to read in lines from data table

### left_str

- **Type**: `character(len=:), allocatable`
- **Defined in source**: `utils.f90:14`
- **Source note**: portion of line left of comment delimiter '#'

### file_name

- **Type**: `character(len=:), allocatable`
- **Defined in source**: `utils.f90:15`
- **Source note**: name of the file being read

### min_cols

- **Type**: `character(len=:), allocatable`
- **Defined in source**: `utils.f90:16`
- **Source note**: string of minimum required column names

### titldum

- **Type**: `character (len=80)`
- **Defined in source**: `utils.f90:17`
- **Source note**: first line in data file that that will be ignored

### nrow

- **Type**: `integer`
- **Defined in source**: `utils.f90:18`
- **Source note**: data row number

### lrow

- **Type**: `integer`
- **Defined in source**: `utils.f90:19`
- **Source note**: row number of the of line in the raw input data file to be read next

### ncols

- **Type**: `integer`
- **Defined in source**: `utils.f90:20`
- **Source note**: number of header columns

### nfields

- **Type**: `integer`
- **Defined in source**: `utils.f90:21`
- **Source note**: number of data columns/fields in a data row

### start_row_numbr

- **Type**: `integer`
- **Defined in source**: `utils.f90:22`
- **Source note**: the number of the row in the file to start reading table data

### start_data_row_numbr

- **Type**: `integer`
- **Defined in source**: `utils.f90:24`
- **Source note**: The line number that the actual data starts.

### unit

- **Type**: `integer`
- **Defined in source**: `utils.f90:25`
- **Source note**: file unit number

### found_header_row

- **Type**: `logical`
- **Defined in source**: `utils.f90:26`
- **Source note**: flag to indicate if header row has been found

### col_okay

- **Type**: `logical, allocatable`
- **Defined in source**: `utils.f90:27`
- **Source note**: array used to track if warning message has already

### file_exists

- **Type**: `logical`
- **Defined in source**: `utils.f90:29`
- **Source note**: flag to indicate if file exists

## Subroutines Defined
### init

### left_of_delim

### split_line

### min_req_cols

### min_header_cols

### get_header_columns

### get_row_fields

### output_column_warning

## Functions Defined
### exp_w

### to_lower

### get_row_idx

### get_col_count

### get_num_data_lines

## Used By Source Routines

```dataview
LIST file.link
WHERE type = "source" AND contains(module, this.module_name)
```

<!-- USER-NOTES-START -->
## Notes
Use this section for type and variable meanings, units, and allowed values. This section is preserved when the generator is rerun.
<!-- USER-NOTES-END -->
