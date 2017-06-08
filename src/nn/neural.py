import tensorflow as tf
#
from dataset.train import *

nn_learning_tax = 0.01
nn_inputs = 5 * 7
nn_outputs = 4
#
nn_hidden1 = 20
#
model_path_src = './nn/tmp/my_test_model'

def train():
    w1 = tf.Variable(tf.random_normal(shape=[nn_inputs, nn_hidden1]), name='w1')
    b1 = tf.Variable(tf.zeros([nn_hidden1]), name='b1')

    w2 = tf.Variable(tf.random_normal(shape=[nn_hidden1, nn_outputs]), name='w2')
    b2 = tf.Variable(tf.zeros([nn_outputs]), name='b2')

    # activation functions
    # see more https://www.tensorflow.org/api_guides/python/nn
    out1 = tf.sigmoid(tf.add(tf.matmul(tin, w1), b1))
    out2 = tf.sigmoid(tf.add(tf.matmul(out1, w2), b2))

    error = tf.subtract(tout, out2)
    mse = tf.reduce_mean(tf.square(error))

    # backpropagation method
    # see more https://www.tensorflow.org/api_guides/python/train
    train = tf.train.AdamOptimizer(nn_learning_tax).minimize(mse)

    # tf.Session(config=tf.ConfigProto(log_device_placement=True))
    # to check gpu using if there is one available
    saver = tf.train.Saver()
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    err, target = 1, 0.01
    epoch, max_epochs = 0, 10000

    while err > target and epoch < max_epochs:
        epoch += 1
        err, _ = sess.run([mse, train])

    # print(sess.run(w1))

    saver.save(sess, model_path_src)
    return [epoch, err]
