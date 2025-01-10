import torch

# print(torch.__version__)
#
# scalar = torch.tensor(5)
# print(scalar)
#
# print(scalar.item())
#
# vector = torch.tensor([2, 2])
# print(vector)

# random_tensor = torch.rand(3, 5)
# print(random_tensor)
# print(random_tensor.ndim)
# print(random_tensor.shape)

# array = torch.arange(1, 20, 4)
# print(array)
# zero_like = torch.zeros_like(array, device="mps")
# print(zero_like)
# print(zero_like.device)

array = torch.arange(1, 41).reshape(2, 4, 5)
print(array)
print(array.permute((2, 0, 1)))