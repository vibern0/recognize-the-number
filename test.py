import tensorflow as tf
import numpy as np
#
import dataset
import confusion

# round'n'round
def round_results(array_results):
    #
    matrix_result = np.zeros((len(array_results), len(array_results[0])), np.float)
    for line in range(0, len(array_results)):
        for column in range(0, len(array_results[0])):
            matrix_result[line][column] = round(array_results[line][column])

    return matrix_result

def test_neural(w1, w2, b1, b2, sess):
    matrix_res = [[]]

    # test it now bitch!
    t_out1 = tf.sigmoid(tf.add(tf.matmul(dataset.train_in, w1), b1))
    t_out2 = tf.sigmoid(tf.add(tf.matmul(t_out1, w2), b2))
    t_result = sess.run([t_out2])

    # round vector output
    # dataset vector output
    # use rounded value and dataset value for matrix position
    # and add one

    # demo matrix
    matrix_res = [
        [5, 0],
        [0, 5]
    ]

    # debug stuff
    # print('result', t_result)

    print(round_results(t_result[0]))

    # do the harlem shake
    # confusion.confusion_matrix_graphic(matrix_res)
