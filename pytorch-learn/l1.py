import pandas as pd
import torch
from torch.nn.functional import relu
import numpy as np

class_enum = {"Iris-setosa": 0, "Iris-versicolor": 1, "Iris-virginica": 2}


# reverse the class
def reverse_class(x):
    if x == 0:
        return "Iris-setosa"
    elif x == 1:
        return "Iris-versicolor"
    else:
        return "Iris-virginica"


data = pd.read_csv("iris.data", names=["sepal length", "sepal width", "petal length", "petal width", "class"])

data.replace(class_enum, inplace=True)

# print(data.tail())
#
# print(data.shape)
#
# print(data.iloc[:, 4].value_counts())
# print(data.head())

class Model (torch.nn.Module):
    def __init__(self):
        super(Model, self).__init__()
        self.l1 = torch.nn.Linear(4, 32)
        self.l2 = torch.nn.Linear(32, 16)
        self.l_out = torch.nn.Linear(16, 3)

    def forward(self, x):
        x = relu(self.l1(x))
        x = relu(self.l2(x))
        x = self.l_out(x)
        return x


model = Model()
loss = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.01)

print(data)
np.random.shuffle(data.values)
print(data)

for i in range(50):
    optimizer.zero_grad()
    y_pred = model.forward(torch.FloatTensor(data.iloc[:, 0:4].values))
    l = loss(y_pred, torch.LongTensor(data.iloc[:, 4].values))
    l.backward()
    optimizer.step()
    print(f'index is {i}, loss is {l}')