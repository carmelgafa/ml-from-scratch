import numpy as np
import seaborn as sns
import tensorflow as tf
import matplotlib as plt

X_data = np.arange(100, step=0.1)
Y_data = X_data + 20 * np.cos(X_data/10)

sns.jointplot(x=X_data, y=Y_data)

# define data and batch size
n_samples = 1000
batch_size = 100

X_data = np.reshape(X_data, (n_samples, 1))
Y_data = np.reshape(Y_data, (n_samples, 1))

# define placeholders for input
X = tf.placeholder(tf.float32, shape=(batch_size, 1))
Y = tf.placeholder(tf.float32, shape=(batch_size, 1))

# define variables
with tf.variable_scope('linear-regression'):
    W = tf.get_variable('weights', (1, 1),
                        initializer=tf.random_normal_initializer())

    b = tf.get_variable('bias', (1,),
                        initializer=tf.constant_initializer(0.0))

    y_pred = tf.matmul(X, W) + b

    loss = tf.reduce_sum((Y - y_pred)**2 / n_samples)

    # optimizer and minization criteria used
    opt_operation = tf.train.AdamOptimizer().minimize(loss)

    with tf.Session() as sess:
        # initialize all variable
        sess.run(tf.global_variables_initializer())
        # gradient decent 55 steps
        for _ in range(500):
            # select random minibatch
            indices = np.random.choice(n_samples, batch_size)

            x_batch, y_batch = X_data[indices], Y_data[indices]
            #dont care the output of the optimizer
            _, loss_val = sess.run([opt_operation, loss], feed_dict={X:x_batch, Y:y_batch})
