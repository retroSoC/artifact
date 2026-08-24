"""Generate the retroSoC SKY130 1024x32 single-port byte-write SRAM."""

import os


word_size = 32
num_words = 1024
write_size = 8

num_rw_ports = 1
num_r_ports = 0
num_w_ports = 0
num_spare_rows = 0
num_spare_cols = 0

tech_name = "sky130"
route_supplies = "ring"
check_lvsdrc = False
analytical_delay = True
uniquify = True

process_corners = ["TT", "SS"]
supply_voltages = [1.4, 1.8]
temperatures = [25, 100]
use_specified_corners = [
    ("TT", 1.8, 25),
    ("SS", 1.4, 100),
]

output_name = "sky130_sram_4kbyte_1rw_32x1024_8"
output_path = os.environ["OPENRAM_OUTPUT"].rstrip("/") + "/"
