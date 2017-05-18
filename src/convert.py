import numpy as np

# convert the shit ou of here!
# only 4bits
def convert_binary_to_int(binary_value):

    if binary_value[0] == 0. and binary_value[1] == 0. and binary_value[2] == 0. and binary_value[3] == 0.:
        return 0

    elif binary_value[0] == 0. and binary_value[1] == 0. and binary_value[2] == 0. and binary_value[3] == 1.:
        return 1

    elif binary_value[0] == 0. and binary_value[1] == 0. and binary_value[2] == 1. and binary_value[3] == 0.:
        return 2

    elif binary_value[0] == 0. and binary_value[1] == 0. and binary_value[2] == 1. and binary_value[3] == 1.:
        return 3

    elif binary_value[0] == 0. and binary_value[1] == 1. and binary_value[2] == 0. and binary_value[3] == 0.:
        return 4
