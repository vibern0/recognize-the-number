import tensorflow as tf
import numpy as np
import time
#
from dataset.train import *
import convert
import neural
import test

class NeuralNetwork:
    def __init__(self):
        test_success = 0
        start = time.time()
        target = 0.01

        print('desfrdgthygju', len(data_input))

        [to_train, to_verify, to_test, res_to_train, res_to_verify] = convert.dataset_matrix_to_lists(data_input, data_output, 75, 15, 15)



        for x in range(0, 1):
            [epoch, err] = neural.train(to_train, res_to_train)
            print('epoch:', epoch, 'mse:', err)
            if err < target:
                test_success = test_success + 1
            test.test_neural(epoch, to_test, res_to_train);

        print('time', time.time() - start)
        print('success ', test_success)

    def __del__(self):
        pass
