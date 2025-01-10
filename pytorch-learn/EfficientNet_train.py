import torch
from torchvision.io import decode_image
from torchvision.models import EfficientNet_B2_Weights
from torchvision import models, datasets
from torch import nn, optim
from torch.utils.data import DataLoader


device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
weights = EfficientNet_B2_Weights.DEFAULT
model = models.efficientnet_b2(weights=weights).to(device)

# don't need to train all params just the last one
for param in model.parameters():
    param.requires_grad = False

# check one class, the output is yes or no
model.classifier[1] = nn.Linear(in_features=model.classifier[1].in_features, out_features=2, bias=True).to(device)
print(model.classifier[1])

loss = nn.CrossEntropyLoss()
optimize = optim.Adam(model.parameters(), lr=0.001)

train_data = datasets.ImageFolder("train", transform=weights.transforms())
train_loader = DataLoader(train_data, batch_size=32, shuffle=True)

model.train()
for epoch in range(10):
    for inputs, labels in train_loader:
        inputs, labels = inputs.to(device), labels.to(device)
        optimize.zero_grad()
        outputs = model(inputs)
        loss_value = loss(outputs, labels)
        loss_value.backward()
        optimize.step()

    print(f"epoch is {epoch}, train loss is {loss_value}")
    model.eval()
    with torch.no_grad():
        inputs, labels = next(iter(train_loader))
        inputs, labels = inputs.to(device), labels.to(device)
        outputs = model(inputs)
        loss_value = loss(outputs, labels)

    print(f"epoch is {epoch}, test loss is {loss_value}")

torch.save(model, "model2.pt")

