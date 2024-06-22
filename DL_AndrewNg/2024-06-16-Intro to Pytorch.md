---
title: 2024-06-16-Intro to Pytorch
date: 2024-06-16
date modified: 2024-06-19
categories: DeepLearning
---

## 利用Pytorch的基本框架

- 确定训练数据集
- 实现对训练数据集的遍历
- 搭建神经网络架构
- 定义损失函数
- 定义优化函数
- 更新参数
- 量化模型性能

## 确定训练数据集

Pytorch为数据提供的相关包：

```Python
import torch
from torch import nn
from torch.utils.data import DataLoader
from torchvision import datasets
from torchvision.transforms import ToTensor
```

### 从Pytorch自带的数据包导入数据

- `root` is the path where the train/test data is stored  
root默认为相对路径，可修改为绝对路径
- `train` specifies training or test dataset  
train参数为布尔类型，确定当前数据集是用作训练集还是测试集
- `download=True` downloads the data from the internet if it’s not available at `root`.
- `transform` and `target_transform` specify the **feature and label transformations**  
transform: 执行将数据文件的原始转换

```python
# Download training data from open datasets.
training_data = datasets.FashionMNIST(
    root="data",
    train=True,
    download=True,
    transform=ToTensor(),
)

# Download test data from open datasets.
test_data = datasets.FashionMNIST(
    root="data",
    train=False,
    download=True,
    transform=ToTensor(),
)
```

访问数据集中具体的样本：直接利用index索引即可  
`training_data[index]`

### 导入自己的数据集

自定义的数据集一定需要包括三个函数，分别实现数据集的初始化,自定义数据集的父类为`Dataset`：  
`__init__,__len__,__getitem__`

```python
import os
import pandas as pd
from torchvision.io import read_image

class CustomImageDataset(Dataset):
    def __init__(self, annotations_file, img_dir, transform=None, target_transform=None):
        self.img_labels = pd.read_csv(annotations_file)
        self.img_dir = img_dir
        self.transform = transform
        self.target_transform = target_transform

    def __len__(self):
        return len(self.img_labels)

    def __getitem__(self, idx):
        img_path = os.path.join(self.img_dir, self.img_labels.iloc[idx, 0])
        image = read_image(img_path)
        label = self.img_labels.iloc[idx, 1]
        if self.transform:
            image = self.transform(image)
        if self.target_transform:
            label = self.target_transform(label)
        return image, label
```

1. `__init__`函数  
`__init__`在实例化一个数据集对象时被调用，类似于constructor. 我们需要确定的参数包括annotation file,对应具体数据的存储路径，以及数据的转换类型  
Annotation file 对应的csv文件类似：

```python
tshirt1.jpg, 0
tshirt2.jpg, 0
......
ankleboot999.jpg, 9
```

2. `__len__`确定数据集的大小
3. `__getitem__`在给定索引时返回数据集中对应的张量形式并返回

## 实现对训练数据集的遍历

检索 `Dataset` 数据集的特征，并一次标记一个样本。在训练模型时，我们通常希望以“mini-batch”的形式传递样本，在每个时期重新洗牌数据以减少模型过拟合，并使用 Python `multiprocessing` 来加快数据检索速度。  
利用 `DataLoader` 来迭代数据集中的数据,接受的参数包括数据集，batch_size以及是否需要随机打乱原有数据

```python
from torch.utils.data import DataLoader
train_dataloader = DataLoader(training_data, batch_size=64, shuffle=True)
test_dataloader = DataLoader(test_data, batch_size=64, shuffle=True)
```

迭代并获取每个批次的数据：

```python
train_features, train_labels = next(iter(train_dataloader))
```

## 搭建神经网络架构

导入基本包：  
`from torch import nn`  
确定训练设备:

```python
device = (
	"cuda"
	if torch.cuda.is_available()
	else "mps"
	if torch.backends.mps.is_available()
	else "cpu"
)
```

我们自定义的神经网络结构可以直接继承pytorch定义的`nn.Module`,且可直接调用父类中的`__init__` 进行初始化。我们只需定义前向传播函数，然后就可以对每一层进行前向传播

```python
class NeuralNetwork(nn.Module):
    def __init__(self):
        super().__init__()
        # flatten函数将高维张量压平成一维
        self.flatten = nn.Flatten()
        # Sequential将神经网络多个层按简单顺序排列
        self.linear_relu_stack = nn.Sequential(
            nn.Linear(28*28, 512),
            nn.ReLU(),
            nn.Linear(512, 512),
            nn.ReLU(),
            nn.Linear(512, 10),
        )

    def forward(self, x):
        x = self.flatten(x)
        logits = self.linear_relu_stack(x)
        return logits
# 创建神经网络的实例
model = NeuralNetwork().to(device)
```

参考补充:  
[Torch.nn API]([torch.nn — PyTorch 2.3 documentation](https://pytorch.org/docs/stable/nn.html))

### 访问参数

神经网络中的许多层都是参数化的，即具有相关的权重和偏差，这些权重和偏差在训练期间得到优化。子类化 `nn.Module` 会自动跟踪模型对象中定义的所有字段，并使所有参数都可以使用模型 `parameters()` 或 `named_parameters()` 方法访问。  
例：

1. 使用 `model.parameters()` 方法  
`model.parameters()` 方法返回一个包含模型所有参数的迭代器。你可以使用 for 循环遍历迭代器，访问每个参数。  

```python
for param in model.parameters():
	print(f"Value: (param}")
```

2. 使用 `model.named_parameters()` 方法  
`model.named_parameters()` 方法返回一个包含参数名称和参数值的迭代器。你可以使用 `for` 循环遍历迭代器，访问每个参数的名称和值。

```python
for name, param in model.named_parameters():
	print(f"Layer: {name} | Value: {param}")
```

## 定义损失函数

损失函数集合: [Loss Function](https://pytorch.org/docs/stable/nn.html#loss-functions)

## 优化策略

[Torch.optim](https://pytorch.org/docs/stable/optim.html)

```python
def train_loop(dataloader, model, loss_fn, optimizer):
    size = len(dataloader.dataset)
    # Set the model to training mode - important for batch normalization and dropout layers
    # Unnecessary in this situation but added for best practices
    model.train()
    for batch, (X, y) in enumerate(dataloader):
        # Compute prediction and loss
        pred = model(X)
        loss = loss_fn(pred, y)

        # Backpropagation
        loss.backward()
        optimizer.step()
        optimizer.zero_grad()

        if batch % 100 == 0:
            loss, current = loss.item(), batch * batch_size + len(X)
            print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")


def test_loop(dataloader, model, loss_fn):
    # Set the model to evaluation mode - important for batch normalization and dropout layers
    # Unnecessary in this situation but added for best practices
    model.eval()
    size = len(dataloader.dataset)
    num_batches = len(dataloader)
    test_loss, correct = 0, 0

    # Evaluating the model with torch.no_grad() ensures that no gradients are computed during test mode
    # also serves to reduce unnecessary gradient computations and memory usage for tensors with requires_grad=True
    with torch.no_grad():
        for X, y in dataloader:
            pred = model(X)
            test_loss += loss_fn(pred, y).item()
            correct += (pred.argmax(1) == y).type(torch.float).sum().item()

    test_loss /= num_batches
    correct /= size
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")
```