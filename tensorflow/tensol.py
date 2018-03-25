import tensorflow as tf

c = tf.constant('Hello, world!')

with tf.Session() as sess:

    print(sess.run(c))

# import tensorflow as tf
# device_name = tf.test.gpu_device_name()
# if device_name != '/device:GPU:0':
#   raise SystemError('GPU device not found')
# print('Found GPU at: {}'.format(device_name))