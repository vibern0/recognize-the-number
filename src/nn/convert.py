import numpy as np

# convert the shit ou of here!
# only 6bits
def convert_binary_to_int(binary_value):

    return binary_value[5] * 1 + binary_value[4] * 2 + binary_value[3] * 4 + binary_value[2] * 8 + binary_value[1] * 16 + binary_value[0] * 32


def dataset_matrix_to_lists(matrix_data_input, matrix_data_output, p_train, p_verify, p_test):

    to_train = []
    to_verify = []
    to_test = []

    res_to_train = []
    res_to_verify = []
    # res_to_test = []

    p_train = 30
    p_verify = 4
    p_test = 5

    for d in range(0, len(matrix_data_input)):

        print('ptrain', p_train)

        to_train = to_train + matrix_data_input[d][0 : p_train]
        to_verify = to_verify + matrix_data_input[d][p_train : p_verify]
        to_test = to_test + matrix_data_input[d][p_verify : 38]



        res_to_train = res_to_train + matrix_data_output[d][0 : p_train]
        res_to_verify = res_to_verify + matrix_data_output[d][p_train : p_verify]
        # res_to_test = res_to_test + matrix_data_output[d][p_verify : 38]

    return [to_train, to_verify, to_test, res_to_train, res_to_verify]
