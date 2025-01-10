import torch
import torch.nn as n

# print(torch.mps.is_available())
# print(torch.mps.current_allocated_memory())

# a = torch.arange(0, 100).unsqueeze(dim=1)
# b = 3 * a + 5
# print(a[:10])
# print(b[:10])


print(torch.tensor(3, dtype=torch.float16))
print(torch.mean(torch.tensor([2, 3, 5], dtype=torch.float16)))