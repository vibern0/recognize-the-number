import tensorflow as tf
#
import dataset

def train(sess):
    w1 = tf.Variable(tf.random_normal([35, 20]), name='w1')
    b1 = tf.Variable(tf.zeros([20]), name='b1')

    w2 = tf.Variable(tf.random_normal([20, 1]), name='w2')
    b2 = tf.Variable(tf.zeros([1]), name='b2')

    # activation functions
    # see more https://www.tensorflow.org/api_guides/python/nn
    out1 = tf.sigmoid(tf.add(tf.matmul(dataset.train_in, w1), b1))
    out2 = tf.sigmoid(tf.add(tf.matmul(out1, w2), b2))

    error = tf.subtract(dataset.train_out, out2)
    mse = tf.reduce_mean(tf.square(error))

    # backpropagation method
    # see more https://www.tensorflow.org/api_guides/python/train
    train = tf.train.AdamOptimizer(0.01).minimize(mse)

    # tf.Session(config=tf.ConfigProto(log_device_placement=True))
    # to check gpu using if there is one available
    # sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    err, target = 1, 0.01
    epoch, max_epochs = 0, 10000

    while err > target and epoch < max_epochs:
        epoch += 1
        err, _ = sess.run([mse, train])

    return [w1, w2, b1, b2, epoch, err]
