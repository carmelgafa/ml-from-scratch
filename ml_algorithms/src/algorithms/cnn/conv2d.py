'''a manual implementation of 2D convolution'''

#pylint: disable = E0401
import torch
import numpy as np


def conv2d_manual(
    input_matrix:list,
    kernel_matrix:list,
    bias:list=None,
    padding:tuple[int, int]=(0,0))->np.ndarray:
    '''perform 2D cross-correlation on a 2D input matrix and a 2D kernel matrix'''

    # Convert lists to numpy arrays for easier manipulation
    input_matrix = np.array(input_matrix)
    kernel_matrix = np.array(kernel_matrix)
    if bias is not None:
        bias_matrix = np.array(bias)

    if padding != (0,0):
        input_matrix = pad_matrix(input_matrix, padding)

    # Get dimensions of input and kernel
    input_rows, input_cols = input_matrix.shape
    kernel_rows, kernel_cols = kernel_matrix.shape

    # Output dimensions after cross-correlation
    output_rows = input_rows - kernel_rows + 1
    output_cols = input_cols - kernel_cols + 1

    # Create an output matrix of zeros
    output_matrix = np.zeros((output_rows, output_cols))

    # Perform cross-correlation
    for i in range(output_rows):
        for j in range(output_cols):
            # Extract the sub-matrix from the input for the current position
            sub_matrix = input_matrix[i:i+kernel_rows, j:j+kernel_cols]

            # Compute the element-wise multiplication and sum the result
            output_matrix[i, j] = np.sum(sub_matrix * kernel_matrix)
            if bias is not None:
                output_matrix[i, j] += bias_matrix[i, j]

    return output_matrix

def pad_matrix(matrix:np.ndarray,padding:tuple[int, int]=(0,0))->np.ndarray:
    '''pads a numpy 2D matrix with zeros'''

    rows, cols = matrix.shape

    row_padding = padding[0]
    col_padding = padding[1]

    padded_matrix = np.zeros(
        (rows+2*row_padding, cols+2*col_padding), dtype=matrix.dtype)
    padded_matrix[row_padding:rows+row_padding, col_padding:cols+col_padding] = matrix
    return padded_matrix


def conv2d_manual_test(
    input_matrix:list,
    kernel_matrix:list,
    bias_valid:list,
    bias_full:list)->tuple[np.ndarray, np.ndarray]:
    '''tests the manual implementation'''

    output_valid = conv2d_manual(input_matrix, kernel_matrix, bias_valid)

    output_full = conv2d_manual(input_matrix, kernel_matrix, bias_full, padding=(1,1))

    return output_valid, output_full


def conv2d_torch_test(
    input_matrix:list,
    kernel_matrix:list,
    bias_valid:list,
    bias_full:list)->tuple[torch.Tensor, torch.Tensor]:
    '''tests pytoch valid and full cross correlation'''
    # Input tensor (1 batch, 1 channel, 3x3 matrix)
    input_tensor = torch.tensor([[input_matrix]], dtype=torch.float32)

    # Kernel tensor (1 output channel, 1 input channel, 2x2 kernel)
    kernel_tensor = torch.tensor([[kernel_matrix]], dtype=torch.float32)

    # Bias valid tensor
    bias_valid_tensor = torch.tensor([[bias_valid]], dtype=torch.float32)

    # Bias full tensor
    bias_full_tensor = torch.tensor([[bias_full]], dtype=torch.float32)

    # Perform 2D convolution with no padding and stride of 1 (valid correlation)
    output_valid = torch.conv2d(
        input_tensor, kernel_tensor, stride=1, padding=0) + bias_valid_tensor

    output_full = torch.conv2d(
        input_tensor, kernel_tensor, stride=1, padding=(1,1)) + bias_full_tensor

    return output_valid, output_full

if __name__ == '__main__':

    input_list = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    kernel_list = [
        [1, 0],
        [0, -1]]


    bias_valid_list = [
        [1, 2],
        [3, 4]]

    bias_full_list = [
        [1, 2, 3 , 4],
        [4, 5, 6, 7],
        [7, 8, 9, 10],
        [10, 11, 12, 13]]


    # print(cross_correlation(input_list, kernel_list))
    o_valid_torch, o_full_torch = conv2d_torch_test(
        input_list, kernel_list, bias_valid_list, bias_full_list)

    o_valid_manual, o_full_manual = conv2d_manual_test(
        input_list, kernel_list, bias_valid_list, bias_full_list)

    print(np.subtract(o_valid_torch.detach().numpy(), o_valid_manual))
    print(np.subtract(o_full_torch.detach().numpy(), o_full_manual))
