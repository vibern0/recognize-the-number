import tensorflow as tf
#
import dataset
import confusion

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
    print('result', t_result)

    # do the harlem shake
    # confusion.confusion_matrix_graphic(matrix_res)
