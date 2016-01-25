# main.py
# This is the entry point of the program.

import column_name_index
import svmc

dataset = svmc.load_kdd_cup_99_dataset_all()

for item in dataset:
    print item[column_name_index.protocol_type]
