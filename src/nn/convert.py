import numpy as np

# convert the shit ou of here!
# only 6bits
def convert_binary_to_int(binary_value):

    result = binary_value[5] * 1 + binary_value[4] * 2 + binary_value[3] * 4 + binary_value[2] * 8 + binary_value[1] * 16 + binary_value[0] * 32

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

        for a in range(0, 5):
            to_train = to_train + [sum(matrix_data_input[d][a].astype(float).tolist(), [])]
            res_to_train = res_to_train + [matrix_data_output[d][a]]

        to_test = to_test + [sum(matrix_data_input[d][5].astype(float).tolist(), [])]
        res_to_test = res_to_test + [matrix_data_output[d][5]]

        for a in range(6, 10):
            to_train = to_train + [sum(matrix_data_input[d][a].astype(float).tolist(), [])]
            res_to_train = res_to_train + [matrix_data_output[d][a]]

        to_test = to_test + [sum(matrix_data_input[d][10].astype(float).tolist(), [])]
        res_to_test = res_to_test + [matrix_data_output[d][10]]

        for a in range(11, 15):
            to_train = to_train + [sum(matrix_data_input[d][a].astype(float).tolist(), [])]
            res_to_train = res_to_train + [matrix_data_output[d][a]]

        to_test = to_test + [sum(matrix_data_input[d][15].astype(float).tolist(), [])]
        res_to_test = res_to_test + [matrix_data_output[d][15]]

        for a in range(16, 20):
            to_train = to_train + [sum(matrix_data_input[d][a].astype(float).tolist(), [])]
            res_to_train = res_to_train + [matrix_data_output[d][a]]

        to_test = to_test + [sum(matrix_data_input[d][20].astype(float).tolist(), [])]
        res_to_test = res_to_test + [matrix_data_output[d][20]]

        for a in range(21, 25):
            to_train = to_train + [sum(matrix_data_input[d][a].astype(float).tolist(), [])]
            res_to_train = res_to_train + [matrix_data_output[d][a]]

        to_test = to_test + [sum(matrix_data_input[d][25].astype(float).tolist(), [])]
        res_to_test = res_to_test + [matrix_data_output[d][25]]

        for a in range(26, 30):
            to_train = to_train + [sum(matrix_data_input[d][a].astype(float).tolist(), [])]
            res_to_train = res_to_train + [matrix_data_output[d][a]]

        to_test = to_test + [sum(matrix_data_input[d][30].astype(float).tolist(), [])]
        res_to_test = res_to_test + [matrix_data_output[d][30]]

        for a in range(31, 35):
            to_train = to_train + [sum(matrix_data_input[d][a].astype(float).tolist(), [])]
            res_to_train = res_to_train + [matrix_data_output[d][a]]

        to_test = to_test + [sum(matrix_data_input[d][35].astype(float).tolist(), [])]
        res_to_test = res_to_test + [matrix_data_output[d][35]]

        for a in range(36, 38):
            to_train = to_train + [sum(matrix_data_input[d][a].astype(float).tolist(), [])]
            res_to_train = res_to_train + [matrix_data_output[d][a]]

        to_test = to_test + [sum(matrix_data_input[d][38].astype(float).tolist(), [])]
        res_to_test = res_to_test + [matrix_data_output[d][38]]

    return [to_train, to_test, res_to_train, res_to_test]
