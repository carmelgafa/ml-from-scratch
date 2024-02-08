import pandas as pd
import numpy as np

def multiply_matrix_by_vector(matrix, vector):
    # original data
    df_a = pd.DataFrame([[1,2,3],[4,5,6]])
    print(df_a, '\n')

    # multiplier vector
    df_b = pd.DataFrame([2,2,1])
    print(df_b, '\n')

    # multiply by a list - it works
    df_c = df_a*[2,2,1]
    print(df_c, '\n')

    # multiply by the dataframe - it works
    df_c = df_a*df_b.to_numpy().T
    print(df_c, '\n')

    #using a series - it works -- preferred
    df_c = df_a*df_b[0]
    print(df_c, '\n')



def matrix_difference():

    df_a = pd.DataFrame([[1,2,3],[4,5,6]])
    print(df_a, '\n')

    df_b = pd.DataFrame([[1,1,1],[1,1,1]])
    print(df_b, '\n')

    df_c = df_a - df_b
    print(df_c, '\n')
    
    
if __name__ == '__main__':
    #multiply_matrix_by_vector()
    matrix_difference()
