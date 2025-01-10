import torch
from torchvision.io import decode_image
from torchvision.models import EfficientNet_B2_Weights
from torchvision import models, datasets
from torch import nn, optim
from torch.utils.data import DataLoader


model = torch.load("model2.pt")

img = decode_image("gold_fish.jpg").unsqueeze(0)
weighets = EfficientNet_B2_Weights.DEFAULT
process = weighets.transforms()
img = process(img).to(device="mps")
model.eval()

# result = model(img)
# print(result)

result = model(img).squeeze(0).softmax(0)

id = result.squeeze(0).argmax().item()
score = result[id]
print(id)
print(score)

