"""week 2 of andrew ng ml course"""
from numpy import matrix

def test_multivariate_regression():
    """test function to implement multivariate linear regression using matrices"""
    testing_data = matrix([[1, 2, 3, 4, 90], [4, 3, 2, 1, 78], [2, 3, 4, 1, 45]])
    testing_data_size = testing_data.shape

    print(testing_data_size[1])


    print(testing_data/5)

test_multivariate_regression()
