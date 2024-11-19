import torch
import torch.nn as nn
import numpy as np
import math

# 设置输入 Tensor
logits = torch.tensor([[0.1, 0.2, 0.7], [0.8, 0.1, 0.1], [0.2, 0.7, 0.1], [0.8, 0.1, 0.1]], dtype=torch.float)
labels = torch.tensor([2, 0, 1, 0])

# # 创建损失函数
# criterion = nn.CrossEntropyLoss()
#
# # 计算损失
# loss = criterion(logits, labels)
# print(f'计算得到的平均交叉熵损失: {loss.item()}')

def cross_entropy(input, target):
    all_loss = 0
    all_times = 0
    for label, values in zip(target, input):
        vals = values.numpy()
        for value in vals:
            
        print(label, values)


cross_entropy(logits, labels)

# soft_max1 = math.exp(0.7) / (math.exp(0.1) + math.exp(0.2) + math.exp(0.7))
# soft_max2 = math.exp(0.8) / (math.exp(0.8) + math.exp(0.1) + math.exp(0.1))
# soft_max3 = math.exp(0.7) / (math.exp(0.2) + math.exp(0.7) + math.exp(0.1))
# soft_max4 = math.exp(0.8) / (math.exp(0.8) + math.exp(0.1) + math.exp(0.1))
# print(soft_max1, soft_max2, soft_max3, soft_max4)
# print(np.log(soft_max1), np.log(soft_max2), np.log(soft_max3), np.log(soft_max4))
# print((np.log(soft_max1) + np.log(soft_max2) + np.log(soft_max3) + np.log(soft_max4)) / 4)