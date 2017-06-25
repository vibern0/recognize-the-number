import tensorflow as tf
#

nn_learning_tax = 0.01
nn_inputs = 20 * 16
nn_outputs = 6
#
nn_hidden1 = 10 * 10
#
model_path_src = './nn/tmp/my_test_model'

def train(data_input, data_output):
    w1 = tf.Variable(tf.random_normal(shape=[nn_inputs, nn_hidden1]), name='w1')
    b1 = tf.Variable(tf.zeros([nn_hidden1]), name='b1')

    w2 = tf.Variable(tf.random_normal(shape=[nn_hidden1, nn_outputs]), name='w2')
    b2 = tf.Variable(tf.zeros([nn_outputs]), name='b2')

    # activation functions
    # see more https://www.tensorflow.org/api_guides/python/nn
    out1 = tf.sigmoid(tf.add(tf.matmul(data_input, w1), b1))
    out2 = tf.sigmoid(tf.add(tf.matmul(out1, w2), b2))

    error = tf.subtract(data_output, out2)
    mse = tf.reduce_mean(tf.square(error))

    # backpropagation method
    # see more https://www.tensorflow.org/api_guides/python/train
    train = tf.train.AdamOptimizer(nn_learning_tax).minimize(mse)

    # tf.Session(config=tf.ConfigProto(log_device_placement=True))
    # to check gpu using if there is one available
    saver = tf.train.Saver()
    sess = tf.Session()

    # tensorboard --logdir=./logs/log/
    tf.summary.scalar('mse', mse)
    merged = tf.summary.merge_all()
    writer = tf.summary.FileWriter('./logs/log', sess.graph)

    sess.run(tf.global_variables_initializer())

    err, target = 1, 0.01
    epoch, max_epochs = 0, 10000

    while err > target and epoch < max_epochs:
        epoch += 1
        summary, err, _ = sess.run([merged, mse, train])
        writer.add_summary(summary, epoch)

    # print(sess.run(w1))

    saver.save(sess, model_path_src)
    return [epoch, err]
