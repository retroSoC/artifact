# artifact
artifacts for various open-source EDA tools

## Hazard3 RISC-V GNU Toolchain

The **Build and Release Hazard3 RISC-V GNU Toolchain** workflow builds a
bare-metal `riscv32-unknown-elf` GCC/Newlib artifact for Hazard3 development.
It follows Hazard3's multilib recommendation, adds the complete standard ISA
profiles used by retroSoC and Hazard3's default configuration, and publishes a
SHA-256 checksum with each archive.

The archive extracts a `riscv/` directory. Add `riscv/bin` to `PATH` to use
`riscv32-unknown-elf-gcc`. The artifact supports standard RISC-V extensions
only; Hazard3-specific `Xh3bextm` and `Xh3irq` instructions still require a
patched toolchain or explicitly encoded assembly.

## SKY130 OpenRAM SRAM

The **Build and Release SKY130 OpenRAM SRAM** workflow generates a single-port
`1024 x 32` SRAM with byte-write support. The release contains generated
Verilog, Liberty, LEF, GDS, SPICE, LVS SPICE, configuration, datasheet, source
manifest, licenses, and checksums. Generated macro views are release artifacts
and are not committed to this repository. OpenRAM's required spare row expands
the physical address port to 11 bits; the consuming logical wrapper fixes the
high bit low and exposes addresses 0 through 1023.

The macro is intended for open-source simulation, synthesis, and development
STA. OpenRAM DRC/LVS is not a release gate for this artifact, so the generated
physical views are not foundry signoff evidence.
