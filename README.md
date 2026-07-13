# SWAT+ Code Learning Workspace

This workspace is for learning the SWAT+ Fortran source, recording verified model knowledge, and locating the exact maintained source files for future changes.

The durable learning entry is [`docs/README.md`](docs/README.md). Start there for the model structure, input/output path, and detailed topic notes.

## Workspace Map

| Path | Role |
| --- | --- |
| [`SWATPLUS/swatplus/`](SWATPLUS/swatplus/) | SWAT+ source used as the object of study. |
| [`SWATPLUS/swatplus/src/`](SWATPLUS/swatplus/src/) | Authoritative Fortran source. |
| [`VSProj/SWAT/SWAT.slnx`](VSProj/SWAT/SWAT.slnx) | Visual Studio solution for Intel Fortran debugging. |
| [`VSProj/SWAT/Osu_1hru/`](VSProj/SWAT/Osu_1hru/) | Small one-HRU input scenario used for first traces. |
| [`docs/`](docs/README.md) | Main learning notes and internal records. |

The Visual Studio project links source files from `SWATPLUS/swatplus/src`; it is not a separate maintained source copy.

## Essential Setup

Fetch the source submodule after cloning:

```powershell
git submodule update --init --recursive
```

Generate `src/main.f90` before building if it is missing. Git tracks [`src/main.f90.in`](SWATPLUS/swatplus/src/main.f90.in); CMake generates ignored `src/main.f90` from that template.

```powershell
Set-Location SWATPLUS/swatplus
cmake -B build -D CMAKE_Fortran_COMPILER=ifx -D CMAKE_BUILD_TYPE=Debug
```

Open [`VSProj/SWAT/SWAT.slnx`](VSProj/SWAT/SWAT.slnx) and use:

| Setting | Value |
| --- | --- |
| Configuration | `Debug` |
| Platform | `x64` |
| Compiler | Intel `ifx` |
| Debug working directory | `$(SolutionDir)Osu_1hru` |

The shared project already records preprocessing and multi-processor compilation for `Debug|x64`. Recheck Visual Studio property pages when changing configuration, platform, compiler, or scenario.

## Rules That Matter

- Durable changes to the program entry belong in `SWATPLUS/swatplus/src/main.f90.in`, followed by regeneration of `main.f90`.
- Do not edit generated build outputs such as `.obj`, `.mod`, `__genmod.f90`, executables, or files under `VSProj/SWAT/x64/`.
- Use `Osu_1hru` for small step-by-step traces, but confirm that the object or option being studied is active in that scenario.
- Record durable findings through [`docs/README.md`](docs/README.md), not by expanding this root README.
