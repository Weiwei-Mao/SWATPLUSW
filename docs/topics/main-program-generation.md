---
title: Main-program template and generation
kind: knowledge
status: verified
created: 2026-07-10
updated: 2026-07-10
source_revision: cb442f7c05fc3bfc34349c446010f452d2737ca0
scenario: general
tags: [architecture, build, entry-point, cmake]
---

# Main-program Template and Generation

## Summary

The maintained SWAT+ program entry is [`src/main.f90.in`](../../SWATPLUS/swatplus/src/main.f90.in). It contains `program main`, initialization calls, simulation control, and shutdown logic. Upstream CMake generates `src/main.f90` from that template, but this workspace keeps the Visual Studio generated copy at `VSProj/SWAT/generated/main.f90` so `SWATPLUS/swatplus/src` can stay aligned with the online source tree.

Git tracks the template and ignores the generated file. A durable main-program change therefore belongs in `main.f90.in`, followed by regeneration.

## Verified generation path

```text
src/main.f90.in
    -> CMake configure_file(...) or VSProj/SWAT/generated/generate-main.ps1
    -> placeholder substitution
    -> generated main.f90
    -> compiler
```

[`CMakeLists.txt`](../../SWATPLUS/swatplus/CMakeLists.txt) sets the SWAT+ version from Git, gathers timestamp/compiler/platform values, and runs `configure_file(...)`. The resulting program text contains resolved values for placeholders such as:

- `@SWAT_VERSION@`
- `@TODAY@`
- `@YEAR@`
- `@ISO@`
- `@CMAKE_Fortran_COMPILER_ID@`
- `@CMAKE_Fortran_COMPILER_VERSION@`
- `@CMAKE_HOST_SYSTEM_NAME@`

[`SWATPLUS/swatplus/.gitignore`](../../SWATPLUS/swatplus/.gitignore) explicitly ignores upstream-generated `src/main.f90`. The root [`.gitignore`](../../.gitignore) ignores local Visual Studio output `VSProj/SWAT/generated/main.f90`.

## Visual Studio relationship

[`SWAT.vfproj`](../../VSProj/SWAT/SWAT.vfproj) references `.\generated\main.f90`, not the `.in` template. The generated file must exist before that project builds.

Copying or renaming `main.f90.in` exposes valid Fortran entry logic, but it is not equivalent to generation while `@...@` placeholders remain. The local Visual Studio workflow is:

```powershell
# Run from the workspace root.
PowerShell -ExecutionPolicy Bypass -File VSProj\SWAT\generated\generate-main.ps1
```

## Change guidance

- Edit `main.f90.in` for maintained changes.
- Regenerate `VSProj/SWAT/generated/main.f90` before compiling the Intel project if the template changes or the generated file is missing.
- Do not commit or independently maintain generated `main.f90`.
- If a breakpoint is needed in the executable source, set it in generated `main.f90` while remembering that the durable matching line is in the template.
- Recheck generated text after changing CMake version or compiler configuration.

## Evidence

| Claim | Evidence |
| --- | --- |
| The template contains the program entry | [`src/main.f90.in`](../../SWATPLUS/swatplus/src/main.f90.in) begins with `program main`. |
| Upstream CMake generates `main.f90` | [`CMakeLists.txt`](../../SWATPLUS/swatplus/CMakeLists.txt) calls `configure_file` for the template and upstream output. |
| Local Visual Studio generation stays outside source | [`generate-main.ps1`](../../VSProj/SWAT/generated/generate-main.ps1) writes `VSProj/SWAT/generated/main.f90`. |
| Generated main is not tracked | [`.gitignore`](../../.gitignore) ignores the local generated file; Git tracks only `src/main.f90.in`. |
| Visual Studio compiles the generated file | [`SWAT.vfproj`](../../VSProj/SWAT/SWAT.vfproj) includes `.\generated\main.f90`. |

## Related notes

- [Simulation control flow](simulation-control-flow.md)
- [Visual Studio and Intel Fortran](visual-studio-intel-fortran.md)
