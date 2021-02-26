"""Test execution scripts"""
from LinearRegression import UnivariateLinearRegression

def execute_linear_regression():
    """executes linear regression test"""
    linear_regression = UnivariateLinearRegression(0.05)
    linear_regression.train('data.dat')
    print(linear_regression.get_y_value(3))

execute_linear_regression()
