# Guild: a simple build system

## Wish list
- Interface for users is YAML
- Code is written in Python
- Support cache
- Easily add any toolchain
- Run stuff (like compile) lightly sandboxed
- Run stuff on remote machines
- Support to download dependencies

## Guidelines
- Dont check in binaries
- Unit test functionality
- Run all tests through easily callable script to enable easy CI
- Keep code simple
- Dont overoptimize at the expense of maintainability and readability
- Avoid non-standard python libraries

## Current support
- Python version: 3.10.12
