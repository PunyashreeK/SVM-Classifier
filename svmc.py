# svmc.py
# This file contains few stuffs related to dataset.

import PATH_INFO


def load_kdd_cup_99_dataset_all():
    """
    This function will load the dataset of kdd cup 99 of intrusion detection
    from the file 'corrected'
    This will return a list consisting of different params.
    """
    lines = open(PATH_INFO.DATASET_DIR + 'corrected').readlines()

    dataset = []

    for line in lines:
        dataset.append(line.replace('\n', '').split(','))

    return dataset
    
    # End of Code
