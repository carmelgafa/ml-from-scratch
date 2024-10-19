from binaryclassification import *
from lr_utils import *
import matplotlib.pyplot as plt

def load_data_test():
    train_set_x_orig, train_set_y, test_set_x_orig, test_set_y, classes = load_dataset()

    index = 26
    plt.imshow(train_set_x_orig[index])

    # use instead if imshow
    image_data = train_set_x_orig[index, :, :, :]
    img = Image.fromarray(image_data, 'RGB')
    #img.show()

    print(classes[train_set_y[:, index]])
    print(classes[np.squeeze(train_set_y[:, index])].decode('utf-8'))

def sigmoid_function_test():

    # test sigmoid function
    print('sigmoid of [0, 2] is {}'.format(sigmoid(np.array([0, 2]))))

    dim = 5
    w, b = initialize_with_zeros(dim)
    print('w = {}'.format(w))
    print('b = {}'.format(b))

def feedforward_test():
    w = np.array([[1.], [2.]])
    b = 2.
    X = np.array([[1., 2., -1.],[3., 4., -3.2]])
    Y= np.array([[1, 0, 1]])

    grads, cost = propagate(w, b, X, Y)

    print('dw= {}'.format(grads['dw']))
    print('db= {}'.format(grads['db']))
    print('cost= {}'.format(cost))

def optimization_test():
    w = np.array([[1.], [2.]])
    b = 2.
    X = np.array([[1., 2., -1.],[3., 4., -3.2]])
    Y= np.array([[1, 0, 1]])

    params, grads, costs = optimize(w, b, X, Y, num_iterations=100, learning_rate=0.009, print_cost=True)

    w = params['w']
    b = params['b']
    dw = grads['dw']
    db = grads['db']

    print(f'w= {w}')
    print(f'b= {b}')
    print(f'dw= {dw}')
    print(f'db= {db}')

def prediction_test():
    w = np.array([[0.1124579],[0.23106775]])
    b = -.3
    X = np.array([[1., -1.1, -3.2],[1.2, 2., 0.1]])
    print('predictions={}'.format(predict(w, b, X)))

prediction_test()
#optimization_test()
#feedforward_test()
