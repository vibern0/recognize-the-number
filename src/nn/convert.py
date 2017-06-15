import numpy as np

# convert the shit ou of here!
# only 6bits
def convert_binary_to_int(binary_value):

    return binary_value[5] * 1 + binary_value[4] * 2 + binary_value[3] * 4 + binary_value[2] * 8 + binary_value[1] * 16 + binary_value[0] * 32
