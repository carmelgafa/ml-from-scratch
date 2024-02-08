import numpy as np
import matplotlib.pyplot as plt
import h5py
import scipy
from scipy import ndimage

def sigmoid(z):
    """
    Compute the sigmoid of z

    Arguments:
    z - A scalar or numpy vector

    Returns:
    s - the sigmoid of z
    """
    s = 1 / (1 + np.exp(-z))
    return s

def initialize_with_zeros(dim):
    """
    Creates a vector for W initialized to 0 and creates b, initialized to 0

    Arguments:
    dim - the size of the weight vector, or the number of features to the system

    Returns:
    w - Initialized weight vecor of shape(dim,1)
    b - initialized bias, scalar
    """
    w = np.zeros((dim, 1))
    b = 0

    assert w.shape == (dim, 1)
    assert isinstance(b, float) or isinstance(b, int)

    return w, b

def propagate(w, b, X, Y):
    """
    Implement feed forward step, calculate cost function and its gradient
    
    Arguments:
    w - weights, a numpy array. In the image case it will be of shape (num_px * num_px * 3, 1)
    b - the scalar bis to the neuron
    X - input data with shape (num_px * num_px * 3, number fo examples)
    Y - 'true' label vecor size (1, number of examples)

    Returns:
    Cost - negative log likelihood cost of logistic regression
    dw - derivative of cost w.r.t. w; same shape of w
    db - derivative of cost w.r.t. b; same shape of b
    """

    number_of_examples = X.shape[1]

    #forward propagation
    A = sigmoid(np.dot(w.T, X) + b)
    cost = np.sum(-(Y * np.log(A) + ((1-Y) * np.log(1-A))), axis=1)/ number_of_examples

    #backward propagation
    dw = np.dot(X, (A-Y).T) / number_of_examples
    db = np.sum(A-Y) / number_of_examples

    assert dw.shape == w.shape
    assert db.dtype == float

    cost = np.squeeze(cost)

    assert cost.shape == ()

    grads = {'dw' : dw,
             'db' : db}
    return grads, cost

def optimize(w, b, X, Y, num_iterations, learning_rate, print_cost=False):
    """
    optimizes w and b using gradient descent

    Argument:
    w - weights, numpy array of shape (number _of_input_features, 1)
    b - bias, scalar
    X - data numpy array of shape (num_px*num_px*3, number_of_examples)
    Y - 'true' label vector, numpy array of shape (1, number_of_examples)
    num_iterations - number of iterations of g.d.
    learning_rate - learning rate of g.d.
    print_cost - print the loss every 100 steps

    Returns:
    params - dictionary containing w and b
    grads - dictionary containing dw and db
    costs - list of all the costs computed
    """
    costs = []

    for i in range(num_iterations):

        grads, cost = propagate(w, b, X, Y)

        dw = grads['dw']
        db = grads['db']

        w = w - (learning_rate * dw)
        b = b - (learning_rate * db)

        if i%100 == 0:
            costs.append(cost)
            if print_cost == True:
                print('print cost after iteration {}: {}'.format(i, cost))

    params = {'w': w, 'b': b}
    grads = {'dw': dw, 'db': db}

    return params, grads, costs

def predict(w, b, X):
    """
    predict label 0 or 1 using learned linera rlogistic regression parameters

    Arguments:
    w - weights, numpy array of shape (number _of_input_features, 1)
    b - bias, scalar
    X - data numpy array of shape (num_px*num_px*3, number_of_examples)

    Returns:
    Y_prediction - numpy array containg predictions for X
    """
    number_of_examples = X.shape[1]

    Y_prediction = np.zeros((1, number_of_examples))

    w = w.reshape(X.shape[0], 1)

    A = sigmoid(np.dot(w.T, X) + b)

    for i in range(A.shape[1]):
        if A[0,i] >= 0.5:
            Y_prediction[0,i] = 1
        else:
            Y_prediction[0,i] = 0

    return Y_prediction