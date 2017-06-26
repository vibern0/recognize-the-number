from PIL import Image
import tensorflow as tf
import numpy as np

meta_graph_src = './nn/tmp/my_test_model.meta'
checkpoint_src = './nn/tmp'

# round'n'round
def round_results(array_results):
    #
    matrix_result = np.zeros((len(array_results), len(array_results[0])), np.float)
    for line in range(0, len(array_results)):
        for column in range(0, len(array_results[0])):
            matrix_result[line][column] = round(array_results[line][column])

    return matrix_result

def convert_binary_to_int(binary_value):

    result = binary_value[5] * 1 + binary_value[4] * 2 + binary_value[3] * 4 + binary_value[2] * 8 + binary_value[1] * 16 + binary_value[0] * 32

    if result < 36 and result > -1:
        return result
    else:
        return 0

class Transform:
    def __init__(self):
        # open image
        col = Image.open("transform/numbers/6.jpg")

        # resize image
        col = col.resize((20, 16), Image.ANTIALIAS)

        # make it black and white
        gray = col.convert('L')
        bw = gray.point(lambda x: 0 if x<128 else 255, '1')

        # get transformed data
        pixels = list(bw.getdata())
        width, height = bw.size

        # make a matrix
        mat_pixels = [pixels[i * width:(i + 1) * width] for i in xrange(height)]

        # update values
        mat_pixels = [[1. if mat_pixels[i][g] == 0 else 0. for g in xrange(width)] for i in xrange(height)]
        for h in range(0, len(mat_pixels)):
         	print(mat_pixels[h])

        pixels = [1. if pixels[g] == 0 else 0. for g in xrange(len(pixels))]
        pixels = [pixels]

        with tf.Session() as sess:
            saver = tf.train.import_meta_graph(meta_graph_src)
            saver.restore(sess,tf.train.latest_checkpoint(checkpoint_src))
            graph = tf.get_default_graph()
            w1 = sess.run(graph.get_tensor_by_name("w1:0"))
            b1 = sess.run(graph.get_tensor_by_name("b1:0"))
            w2 = sess.run(graph.get_tensor_by_name("w2:0"))
            b2 = sess.run(graph.get_tensor_by_name("b2:0"))

            # test it now bitch!
            t_out1 = tf.sigmoid(tf.add(tf.matmul(pixels, w1), b1))
            t_out2 = tf.sigmoid(tf.add(tf.matmul(t_out1, w2), b2))
            t_result = sess.run([t_out2])

            print(t_result)
            print(t_result[0])
            print(t_result[0][0])
            print(t_result[0][0][0])
            rounded_results = round_results(t_result[0])
            print('result : ', rounded_results)

        # for h in range(0, len(pixels)):
        # 	print(pixels[h])

        # test with trained neural network

    def __del__(self):
        pass
