''' # convert the shit ou of here! '''

# only 6bits
import numpy as np


def convert_binary_to_int(binary_value):

    result = (binary_value[5] * 1
              + binary_value[4] * 2
              + binary_value[3] * 4
              + binary_value[2] * 8
              + binary_value[1] * 16
              + binary_value[0] * 32)

    if result < 36 and result > -1:
        return result
    else:
        return 0


def dataset_matrix_to_lists(matrix_data_input, matrix_data_output, p_train, p_test):

    to_train = []
    to_test = []

    res_to_train = []
    res_to_test = []

    for d in range(0, len(matrix_data_input)):

        # print('ptrain', p_train)

        to_train = to_train + matrix_data_input[d][0 : 30]
        to_test = to_test + matrix_data_input[d][30 : 39]

        res_to_train = res_to_train + matrix_data_output[d][0 : 30]
        res_to_test = res_to_test + matrix_data_output[d][30 : 39]

    return [to_train, to_test, res_to_train, res_to_test]
