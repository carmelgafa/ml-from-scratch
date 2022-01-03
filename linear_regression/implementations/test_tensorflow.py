"""Test excercises for tensorflow"""
import tensorflow as tf
import numpy as np
import seaborn as plt

def variable_test():
    state = tf.Variable(0, name='counter')
    new_value = tf.add(state, tf.constant(1))
    update = tf.assign(state, new_value)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())

        print('starting loop...')
        print(sess.run(state))
        for _ in range(5):
            sess.run(update)
            print(sess.run(state))
            print(update.name)

def fetch_test():
    input1 = tf.constant(1.0)
    input2 = tf.constant(3.0)
    input3 = tf.constant(6.0)

    interval = tf.add(input1, input3)
    mul = tf.multiply(interval, input2)

    with tf.Session() as sess:
        sess.run(tf.global_variables_initializer())
        result = sess.run([mul, interval])
        print(result)

def numpy_to_tf_test():
    a = np.zeros((3, 4))
    ta = tf.convert_to_tensor(a)
    with tf.Session() as sess:
        print(sess.run(ta))

def placeholder_test():
    """use of feed_dict, mapping from placeholder variables to concrete values"""
    input1 = tf.placeholder(tf.float32)
    input2 = tf.placeholder(tf.float32)

    output = tf.multiply(input1, input2)

    with tf.Session() as sess:
        print(sess.run([output], feed_dict={input1:[5.], input2:[2.]}))

def scope_test():
    with tf.variable_scope('foo'):
        v = tf.get_variable('v', [1])
        print(v.name)
        with tf.variable_scope('bar'):
            v = tf.get_variable('v', [1])
            print(v.name)
            tf.get_variable_scope().reuse_variables()
            g = tf.get_variable('v', [1])

def linear_regression_test():
    X_data = np.arange(100, step=0.1)
    Y_data = X_data + 20 * np.sin(X_data/10)

    plt.regplot(x=X_data, y=Y_data, scatter=True)



#variable_test()
#fetch_test()
#numpy_to_tf_test()
#placeholder_test()
#scope_test()
linear_regression_test()
