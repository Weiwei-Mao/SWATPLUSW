---
type: overview
tags:
  - swat/overview
  - swat/debug
  - swat/baseline
title: Osu_1hru Baseline And Debug Guide
purpose: "Reproducible build, run, breakpoint, and output checks for the default one-HRU debug scenario."
status: verified
source_revision: "cb442f7c05fc3bfc34349c446010f452d2737ca0"
scenario: "VSProj/SWAT/Osu_1hru"
baseline_date: "2026-07-16"
---

# Osu_1hru Baseline And Debug Guide

This is the default short feedback loop for learning or changing SWAT+. It ties a source revision and executable to one known scenario, a controller path, and a small set of output signals.

## Current Verification State

| Check | State | Evidence |
|---|---|---|
| Scenario inputs | verified | 71 distinct non-`null` filenames in `file.cio`; all 71 exist. See [[osu-1hru-input-inventory]]. |
| Current source Debug rebuild | verified | Visual Studio 18.7 plus Intel Fortran 2026.1 linked `Debug|x64` with 0 errors and 0 warnings on 2026-07-16. |
| Repeated Debug run | verified | Two independent temporary scenario copies completed with exit code `0`. |
| Golden output baseline | verified | Both runs printed revision `cb442f7...`, contained no unresolved build placeholders, and produced identical payload hashes. |

This baseline is accepted for the source revision and scenario named in frontmatter. Refresh it deliberately when either changes.

## Scenario Contract

| Setting | Value | Source |
|---|---|---|
| Simulation period | 2010-01-01 through 2023-12-31, 14 years | [`time.sim`](../../../VSProj/SWAT/Osu_1hru/time.sim) |
| Warm-up/output skip | first 3 years | [`print.prt`](../../../VSProj/SWAT/Osu_1hru/print.prt) |
| Printed water balance period | 2013 through 2023 | `nyskip = 3` plus annual/average-annual selections |
| Spatial area | 10 ha | [`object.cnt`](../../../VSProj/SWAT/Osu_1hru/object.cnt) |
| Active object counts | 1 HRU, 1 routing unit, 1 aquifer, 1 SWAT-deg channel | [`object.cnt`](../../../VSProj/SWAT/Osu_1hru/object.cnt) |
| Conventional channel/reservoir/recall/outlet counts | 0 | [`object.cnt`](../../../VSProj/SWAT/Osu_1hru/object.cnt) |
| CSV/database/CDF output | disabled | [`print.prt`](../../../VSProj/SWAT/Osu_1hru/print.prt) |
| Management output | enabled | [`print.prt`](../../../VSProj/SWAT/Osu_1hru/print.prt) |

## Build Before Debugging

1. Check for an existing SWAT process before rebuilding:

   ```powershell
   Get-Process -Name SWAT -ErrorAction SilentlyContinue
   ```

   If Visual Studio owns the process, stop that debug session normally. A running executable can lock both `SWAT.exe` and scenario output files.

2. Generate the Visual Studio main program from the tracked template:

   ```powershell
   Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
   .\VSProj\SWAT\generated\generate-main.ps1 -CompilerId IntelLLVM -CompilerVersion 2026.1.0
   ```

   Durable entry-program changes belong in [`main.f90.in`](../../../SWATPLUS/swatplus/src/main.f90.in), not in the generated copy.

3. Open [`SWAT.slnx`](../../../VSProj/SWAT/SWAT.slnx), select `Debug|x64`, and build in Visual Studio. The project currently verifies these Debug settings: `ifx`, preprocessing, no optimization, debug information, traceback, interface warnings, bounds checks, stack checks, and multi-processor compilation.

4. Set the debugger working directory to `$(SolutionDir)Osu_1hru`. This is a user-specific Visual Studio setting and is not stored in the shared `.vfproj`.

The old Intel `.vfproj` format is not buildable with bare MSBuild on this machine (`MSB4075`). Use Visual Studio or `devenv.com` with the Intel Fortran integration installed.

## Running Outside Visual Studio

The Debug executable dynamically depends on Intel and Microsoft debug runtime DLLs. On the verified machine, prepending the oneAPI compiler `bin` directory resolved the Intel DLLs:

```powershell
$intelBin = 'C:\Program Files (x86)\Intel\oneAPI\compiler\2026.1\bin'
$env:PATH = $intelBin + ';' + $env:PATH
Push-Location .\VSProj\SWAT\Osu_1hru
& ..\x64\Debug\SWAT.exe
$LASTEXITCODE
Pop-Location
```

Expected completion signals:

- process exit code `0`;
- `Execution successfully completed` in the console and `simulation.out`;
- `files_out.out` lists the files actually opened for output;
- no `forrtl: severe` message.

Do not use elapsed time as a strict assertion. The verified one-HRU run took less than one second after startup, but machine load and Debug instrumentation vary.

## Breakpoint Ladder

Use this sequence to move from orchestration to process state without stepping through every reader:

| Stop | Why | Useful watches |
|---|---|---|
| generated `main.f90`, calls to `proc_bsn`, `proc_db`, and `proc_read` | separate basin controls, shared databases, and scenario readers | `db_mx`, `sp_ob`, `cs_db%num_tot` |
| [`time_control.f90`](../../../SWATPLUS/swatplus/src/time_control.f90), daily loop and `call command` | establish date, print/reset flags, and daily forcing | `time%yrc`, `time%day`, `time%yrs`, `time%end_mo`, `time%end_yr`, `time%end_sim` |
| [`command.f90`](../../../SWATPLUS/swatplus/src/command.f90), object dispatch | see which active object path the connection graph selects | `icmd`, `ob(icmd)%typ`, `ob(icmd)%num`, `ob(icmd)%area_ha` |
| [`hru_control.f90`](../../../SWATPLUS/swatplus/src/hru_control.f90), immediately after `j = ihru` | inspect the active HRU and its database/management links | `ihru`, `j`, `iob`, `iwst`, `ires`, `isched` |
| `hru_control`, after weather assignment | connect climate forcing to land-phase state | `w%precip`, `surfq(j)`, `latq(j)`, `soil(j)%phys(:)%st` |
| `command`, routing unit/aquifer/SWAT-deg channel cases | follow HRU output through routing, groundwater, and the receiving channel | `ob(icmd)%hin`, `ob(icmd)%hd(1)%flo`, `iru`, `iaq`, `isdch` |

For this scenario, the relevant dispatch types are HRU, routing unit, aquifer, and SWAT-deg channel (`chandeg`). Always verify `ob(icmd)%typ`; do not assume that object order remains fixed after editing connection files.

## Golden Behavioral Baseline

The repeated runs used this executable:

| Property | Value |
|---|---|
| Path | `VSProj/SWAT/x64/Debug/SWAT.exe` |
| Build timestamp | 2026-07-16 22:48:21 |
| SHA-256 | `D5AB5F6A5BE160E3BCB33189F4CEEC833993362FC304B77FD00933D7861F45D5` |
| Run location | two fresh temporary copies of `VSProj/SWAT/Osu_1hru` |
| Exit codes | `0`, `0` |
| Run date | 2026-07-16 |

The payload hashes exclude each output's first three metadata/header lines, join the remaining lines with LF, and append one final LF. This avoids invalidating numerical payloads solely because the generated program banner changes.

| Output payload | SHA-256 |
|---|---|
| `basin_wb_yr.txt` | `A8CEE45E08B13ABB40307EDE1448B26042C647E3A329CE1387C94B8BA13B63A0` |
| `basin_wb_aa.txt` | `19DB3381BA56607095699C803CBD146A788969017A4DD0D2DF7EF2836802A64E` |
| `hru_wb_aa.txt` | `36D7397FF8FC4DDDDBCFC234EFE9A2673A3CCC5F73CAFC37BCA71295DE2A3467` |
| `aquifer_aa.txt` | `BF581E917F9C7EBC06EB863F8A677339CBD1B78D02C996FECE2EBEB3F8A685B2` |
| `ru_aa.txt` | `0F63C19F3CC2F4349887BB8CAA54C9A1B37E50C150F31E3098673135A6E52021` |
| `channel_sd_aa.txt` | `F7606C27F769BC392A26B39E7492CE8FA7F2641D4D643C4068B6065FF883509F` |
| `mgt_out.txt` | `9C711E5F33272B69F54746AFFD9AE6CAFD7CE927C7E730E23A938AAAF75EFC28` |

Useful numerical anchors from the average-annual outputs are:

| Signal | Printed value |
|---|---:|
| Basin precipitation | 1174.592 mm |
| Basin surface runoff generation | 1135.332 mm |
| Basin percolation | 362.931 mm |
| Basin ET | 621.058 mm |
| Aquifer recharge | 362.931 mm |
| Aquifer flow | 338.418 mm |

`mgt_out.txt` also shows active fertilizer, manure, tillage, paddy irrigation, planting, and weir-reset operations. These are useful event breakpoints when studying management behavior.

## Refresh This Baseline

1. End any existing SWAT debug process normally so it does not lock the executable or outputs.
2. Regenerate `VSProj/SWAT/generated/main.f90` and rebuild `Debug|x64` successfully.
3. Confirm the runtime banner contains the expected source revision and no unresolved `@...@` placeholders.
4. Run two fresh scenario copies and confirm their payload hashes match each other.
5. Compare against the hashes above. Investigate numerical differences; accept changed hashes only after the source/input cause is understood.
6. Update `source_revision`, executable metadata, hashes, numerical anchors, and `baseline_date` together.
