# OpenRAM Artifact Configurations

This directory owns the reviewed OpenRAM input configurations used by the
artifact workflows. Generated Verilog, Liberty, layout, and netlist views are
published as release assets and must not be committed here.

`sky130_sram_4kbyte_1rw_32x1024_8.py` defines the byte-write, single-port
SKY130 macro consumed by retroSoC. It generates only the TT 1.8 V/25 C and SS
1.4 V/100 C Liberty corners used by the synthesis and STA flows.
