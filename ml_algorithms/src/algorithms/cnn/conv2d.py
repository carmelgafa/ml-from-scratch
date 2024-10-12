import torch

input_list = [[1, 6, 2],
        [5, 3, 1],
        [7, 0, 4]]
kernel_list = [[1, 2],
        [-1, 0]]

# manual valid cross correlation

# create an output list
output_list = []

# iterate through the kernel
for i in range(len(input_list)):
    for j in range(len(kernel_list)):
        output_list.append(input_list[i][j] * kernel_list[j][i])    

print(output_list)


# Input tensor (1 batch, 1 channel, 3x3 matrix)
input_tensor = torch.tensor([[input_list]], dtype=torch.float32)

# Kernel tensor (1 output channel, 1 input channel, 2x2 kernel)
kernel = torch.tensor([[kernel_list]], dtype=torch.float32)

# Perform 2D convolution with no padding and stride of 1 (valid correlation)
output_valid = torch.conv2d(input_tensor, kernel, stride=1, padding=0)
print(output_valid)

output_full = torch.conv2d(input_tensor, kernel, stride=1, padding=(1,1))
print(output_full)
