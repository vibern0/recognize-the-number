import tensorflow as tf
import numpy as np
import time
#
import neural
import test

test_success = 0
start = time.time()
target = 0.01
for x in range(0, 5):

    sess = tf.Session()
    [w1, w2, b1, b2, epoch, err] = neural.train(sess)
    print('epoch:', epoch, 'mse:', err)

    if err < target:
        test_success = test_success + 1

    test.test_neural(w1, w2, b1, b2, sess);
    sess.close()



print('time', time.time() - start)
print('success ', test_success)
