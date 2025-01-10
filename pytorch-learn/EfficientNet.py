from torchvision.io import decode_image
from torchvision.models import EfficientNet, EfficientNet_B2_Weights
from torchvision import models

img = decode_image("kakaxi.jpg").unsqueeze(0)
weighets = EfficientNet_B2_Weights.DEFAULT

process = weighets.transforms()

print(img.shape)

img = process(img)
print(weighets.meta["categories"])
# model = models.efficientnet_b2(weights=weighets)
# model.eval()
#
# result = model(img).squeeze(0).softmax(0)
#
#
# print(result.shape)
# print(result.squeeze(0).shape)
#
# id = result.squeeze(0).argmax().item()
# score = result[id]
# category_name = weighets.meta["categories"][id]
# print(category_name)
# print(score)
# print(id)
# # print(weighets.meta["categories"])


