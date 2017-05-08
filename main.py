import tensorflow as tf

T, F = 1., 0.

train_in = [
 [T, T],
 [T, F],
 [F, T],
 [F, F],
]

train_out = [
 [F],
 [T],
 [T],
 [F],
]

w1 = tf.Variable(tf.random_normal([2, 2]), name='w1')
b1 = tf.Variable(tf.zeros([2]), name='b1')

w2 = tf.Variable(tf.random_normal([2, 1]), name='w2')
b2 = tf.Variable(tf.zeros([1]), name='b2')

out1 = tf.tanh(tf.add(tf.matmul(train_in, w1), b1))
out2 = tf.tanh(tf.add(tf.matmul(out1, w2), b2))

error = tf.subtract(train_out, out2)
mse = tf.reduce_mean(tf.square(error))

train = tf.train.GradientDescentOptimizer(0.01).minimize(mse)

sess = tf.Session()
sess.run(tf.global_variables_initializer())

err, target = 1, 0.01
epoch, max_epochs = 0, 10000

while err > target and epoch < max_epochs:
   epoch += 1
   err, _ = sess.run([mse, train])

print('epoch:', epoch, 'mse:', err)


t_train_in = [
    [T, T],
    [T, F],
    [F, T],
    [F, F],
]
t_out1 = tf.tanh(tf.add(tf.matmul(t_train_in, w1), b1))
t_out2 = tf.tanh(tf.add(tf.matmul(t_out1, w2), b2))
t_result = sess.run([t_out2])
print('res', t_result)

#variables_names =[v.name for v in tf.trainable_variables()]
#values = sess.run(variables_names)
#for k,v in zip(variables_names, values):
#    print(k, v)
