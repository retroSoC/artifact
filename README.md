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
