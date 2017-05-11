import tensorflow as tf
#
import seaborn as sn
import pandas as pd
import matplotlib.pyplot as plt
#
import numpy as np
#
import time

# 0., 0., 0., 0., 0.
# 0., 1., 1., 0., 0.
# 1., 0., 0., 1., 0.
# 1., 0., 0., 1., 0.
# 1., 0., 0., 1., 0.
# 0., 1., 1., 0., 0.
# 0., 0., 0., 0., 0.

# 0., 0., 0., 0., 0.
# 0., 0., 0., 0., 0.
# 0., 0., 0., 0., 0.
# 0., 0., 0., 0., 0.
# 0., 0., 0., 0., 0.
# 0., 0., 0., 0., 0.
# 0., 0., 0., 0., 0.


train_in = [
    [
        0., 0., 0., 0., 0.,
        0., 1., 0., 0., 0.,
        1., 0., 1., 0., 0.,
        1., 0., 1., 0., 0.,
        1., 0., 1., 0., 0.,
        0., 1., 0., 0., 0.,
        0., 0., 0., 0., 0.
    ],
    [
        0., 0., 0., 0., 0.,
        0., 1., 1., 0., 0.,
        1., 0., 0., 1., 0.,
        1., 0., 0., 1., 0.,
        1., 0., 0., 1., 0.,
        0., 1., 1., 0., 0.,
        0., 0., 0., 0., 0.
    ],
    [
        0., 0., 0., 0., 0.,
        0., 0., 1., 0., 0.,
        0., 1., 0., 1., 0.,
        0., 1., 0., 1., 0.,
        0., 1., 0., 1., 0.,
        0., 0., 1., 0., 0.,
        0., 0., 0., 0., 0.
    ],
    [
        0., 0., 0., 0., 0.,
        0., 0., 1., 1., 0.,
        0., 1., 0., 0., 1.,
        0., 1., 0., 0., 1.,
        0., 1., 0., 0., 1.,
        0., 0., 1., 1., 0.,
        0., 0., 0., 0., 0.
    ],
    [
        0., 0., 0., 0., 0.,
        0., 0., 0., 1., 0.,
        0., 0., 1., 0., 1.,
        0., 0., 1., 0., 1.,
        0., 0., 1., 0., 1.,
        0., 0., 0., 1., 0.,
        0., 0., 0., 0., 0.
    ],
    [
        0., 0., 0., 0., 0.,
        0., 1., 0., 0., 0.,
        1., 1., 0., 0., 0.,
        0., 1., 0., 0., 0.,
        0., 1., 0., 0., 0.,
        0., 1., 0., 0., 0.,
        0., 0., 0., 0., 0.
    ],
    [
        0., 0., 0., 0., 0.,
        0., 1., 0., 0., 0.,
        1., 1., 0., 0., 0.,
        0., 1., 0., 0., 0.,
        0., 1., 0., 0., 0.,
        1., 1., 1., 0., 0.,
        0., 0., 0., 0., 0.
    ],
    [
        0., 0., 0., 0., 0.,
        0., 0., 1., 0., 0.,
        0., 1., 1., 0., 0.,
        0., 0., 1., 0., 0.,
        0., 0., 1., 0., 0.,
        0., 0., 1., 0., 0.,
        0., 0., 0., 0., 0.
    ],
    [
        0., 0., 0., 0., 0.,
        0., 0., 1., 0., 0.,
        0., 1., 1., 0., 0.,
        0., 0., 1., 0., 0.,
        0., 0., 1., 0., 0.,
        0., 1., 1., 1., 0.,
        0., 0., 0., 0., 0.
    ],
    [
        0., 0., 0., 0., 0.,
        0., 0., 0., 1., 0.,
        0., 0., 1., 1., 0.,
        0., 0., 0., 1., 0.,
        0., 0., 0., 1., 0.,
        0., 0., 0., 1., 0.,
        0., 0., 0., 0., 0.
    ],
    [
        0., 0., 0., 0., 0.,
        0., 0., 0., 1., 0.,
        0., 0., 1., 1., 0.,
        0., 0., 0., 1., 0.,
        0., 0., 0., 1., 0.,
        0., 0., 1., 1., 1.,
        0., 0., 0., 0., 0.
    ],
]

train_out = [
    [0.],
    [0.],
    [0.],
    [0.],
    [0.],
    [1.],
    [1.],
    [1.],
    [1.],
    [1.],
    [1.],
]

def confusion_matrix_graphic(array):
    df_cm = pd.DataFrame(array, index = [i for i in 'AB'],
                      columns = [i for i in 'AB'])
    plt.figure(figsize = (10,7))
    sn.heatmap(df_cm, annot=True)
    # Display matrix
    plt.matshow(array)
    plt.show()

test_success = 0
start = time.time()
# test training and result 5 times
for x in range(0, 5):

    w1 = tf.Variable(tf.random_normal([35, 20]), name='w1')
    b1 = tf.Variable(tf.zeros([20]), name='b1')

    w2 = tf.Variable(tf.random_normal([20, 1]), name='w2')
    b2 = tf.Variable(tf.zeros([1]), name='b2')

    # activation functions
    # see more https://www.tensorflow.org/api_guides/python/nn
    out1 = tf.sigmoid(tf.add(tf.matmul(train_in, w1), b1))
    out2 = tf.sigmoid(tf.add(tf.matmul(out1, w2), b2))

    error = tf.subtract(train_out, out2)
    mse = tf.reduce_mean(tf.square(error))

    # backpropagation method
    # see more https://www.tensorflow.org/api_guides/python/train
    train = tf.train.AdamOptimizer(0.01).minimize(mse)

    # tf.Session(config=tf.ConfigProto(log_device_placement=True))
    # to check gpu using if there is one available
    sess = tf.Session()
    sess.run(tf.global_variables_initializer())

    err, target = 1, 0.01
    epoch, max_epochs = 0, 10000

    while err > target and epoch < max_epochs:
        epoch += 1
        err, _ = sess.run([mse, train])

    print('epoch:', epoch, 'mse:', err)

    if err < target:
        test_success = test_success + 1

    # test results
    """output_array = np.zeros((2, 2), dtype=np.float32)
    t_train_in = [
        [1., 1.],
        [1., 0.],
        [0., 1.],
        [0., 0.],
    ]"""
    t_out1 = tf.sigmoid(tf.add(tf.matmul(train_in, w1), b1))
    t_out2 = tf.sigmoid(tf.add(tf.matmul(t_out1, w2), b2))
    t_result = sess.run([t_out2])

    print('result', t_result)

    """for y in range(0, 5):
        t_out1 = tf.tanh(tf.add(tf.matmul(t_train_in, w1), b1))
        t_out2 = tf.tanh(tf.add(tf.matmul(t_out1, w2), b2))
        t_result = sess.run([t_out2])

        # add to graph
        if t_result[0][0] < 0.5:
            print("v")
            output_array[0][0] = output_array[0][0] + 1
        else:
            output_array[0][1] = output_array[0][1] + 1

        if t_result[0][3] < 0.5:
            output_array[0][0] = output_array[0][0] + 1
        else:
            output_array[0][1] = output_array[0][1] + 1

        ##
        if t_result[0][1] > 0.5:
            output_array[1][1] = output_array[1][1] + 1
        else:
            output_array[1][0] = output_array[1][0] + 1

        if t_result[0][2] > 0.5:
            output_array[1][1] = output_array[1][1] + 1
        else:
            output_array[1][0] = output_array[1][0] + 1"""


        # output_array = output_array + t_result[0]
        # print('res', t_result[0][0])
        # print('res', t_result)
        # print('res2', t_result[0] + t_result[0])

    #confusion_matrix_graphic(output_array)

    """confusion_matrix_graphic(
            [[33,2,0,0,0,0,0,0,0,1,3],
            [3,31,0,0,0,0,0,0,0,0,0],
            [0,4,41,0,0,0,0,0,0,0,1],
            [0,1,0,30,0,6,0,0,0,0,1],
            [0,0,0,0,38,10,0,0,0,0,0],
            [0,0,0,3,1,39,0,0,0,0,4],
            [0,2,2,0,4,1,31,0,0,0,2],
            [0,1,0,0,0,0,0,36,0,2,0],
            [0,0,0,0,0,0,1,5,37,5,1],
            [3,0,0,0,0,0,0,0,0,39,0],
            [0,0,0,0,0,0,0,0,0,0,38]])"""

    # variables_names =[v.name for v in tf.trainable_variables()]
    # values = sess.run(variables_names)
    # for k,v in zip(variables_names, values):
    #     print(k, v)

print('time', time.time() - start)
print('success ', test_success)
