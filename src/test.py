import tensorflow as tf
import numpy as np
#
from dataset.train import *
import confusion

# round'n'round
def round_results(array_results):
    #
    matrix_result = np.zeros((len(array_results), len(array_results[0])), np.float)
    for line in range(0, len(array_results)):
        for column in range(0, len(array_results[0])):
            matrix_result[line][column] = round(array_results[line][column])

    return matrix_result

def test_neural(epoch):
    matrix_res = [[]]

    with tf.Session() as sess:
        saver = tf.train.import_meta_graph('tmp/my_test_model.meta')
        saver.restore(sess,tf.train.latest_checkpoint('./tmp'))
        graph = tf.get_default_graph()
        w1 = sess.run(graph.get_tensor_by_name("w1:0"))
        b1 = sess.run(graph.get_tensor_by_name("b1:0"))
        w2 = sess.run(graph.get_tensor_by_name("w2:0"))
        b2 = sess.run(graph.get_tensor_by_name("b2:0"))

        # test it now bitch!
        t_out1 = tf.sigmoid(tf.add(tf.matmul(tin, w1), b1))
        t_out2 = tf.sigmoid(tf.add(tf.matmul(t_out1, w2), b2))
        t_result = sess.run([t_out2])

        # round vector output
        # dataset vector output
        # use rounded value and dataset value for matrix position
        # and add one

        # demo matrix
        matrix_res = [
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0]
        ]

        # debug stuff
        # print('result', t_result)

        # print(round_results(t_result[0]))
        # print(t_result)

        rounded_results = round_results(t_result[0])
        matrix_res = confusion.build_matrix_array(matrix_res, tout, rounded_results)

        # do the harlem shake
        confusion.confusion_matrix_graphic(matrix_res)
