---
title: 2024-06-19-Computations in DeepLearning
date: 2024-06-19
date modified: 2024-06-19
categories: DeepLearning
---

## Layer and Block

### 定义

> [!Important] Concept  
> 块可以描述单个层、由多个层组成的组件或者模型本身。使用块进行抽象可以将块组合成更大的组件。本质上为对多层进行进一步封装与模块化设计。

### 自定义块

> 块的基本功能
> 1. 将输入数据作为前向传播的参数
> 2. 通过前向传播计算输出，同时关注输入到输出维度的变化
> 3. 计算输出关于输入的梯度(Automatic Differentiation)
> 4. 存储和访问前向传播计算所需的参数
> 5. 初始化模型参数

使用Python的类设计块

```python
import torch
import torch.nn as nn
import torch.nn.Functional as F
class MLP(nn.Module):
	def __init__(self):
		super().__init__()
		self.hidden = nn.Linear(20,256)
		self.out = nn.Linear(256,10)
	def forward(self, X):
		return self.out(F.relu(self.hidden(X)))
# 实例化
net = MLP()
net(X)
```

#### 顺序块

利用`nn.Sequential`  
手动实现:

```python
class MySequential(nn.Module):
	def __init__(self, *args):
		super().__init__()
		for idx, module in enumerate(args)
		# 将module保存在Module类的成员
		# _module的类为有序字典
		self._modules[str(idx)] = module
	def forward(self, X):
		for block in self._modules.values():
			X = block(X)
		return X
# 利用自己定义的Sequential构造神经网络
net = MySequential(nn.Linear(20, 256), nn.ReLU(), nn.Linear(256, 10))
net(X)
```

#### 在前向传播函数中执行代码

我们可以在前向传播中执行代码，使神经网络的结构不仅仅是线性，还可以加入控制流等模块  
例如我们希望执行:

$$
f(x,w) = cw^{T}x \ (其中c为不被梯度下降更新的参数)
$$

```python
class FixedHiddenMLP(nn.Module):
	def __init__():
		super().__init__()
		self.rand_weight = torch.rand((20,20), requires_grad=False)
		self.linear = nn.Linear(20,20)
	def forward(self, X):
		X = self.linear(X)
		X = F.relu(torch.mm(X, slef.rand_weight) + 1)
		X = self.linear(X)
		while X.abs().sum() > 1:
			X /= 2
		return X.sum()
```

## 参数管理

### 参数访问

当利用通用`Sequential`类定义模型时，我们可以通过索引来访问模型的任意层，此时模型的每一层都可用有序字典查看  
`print(net[2].state_dict())`  
输出  
`OrderedDict([('weight', tensor([[-0.0427, -0.2939, -0.1894,  0.0220, -0.1709, -0.1522, -0.0334, -0.2263]])), ('bias', tensor([0.0887]))])`

**可以通过向自定义层定义的参数中加入`nn.Parameters`来将自己定义的参数加入参数管理，进而可以通过module定义的method访问**

#### 目标参数

Pytorch中每个参数都表示为参数类的一个实例，其时一个复合的对象，包括值、梯度和额外信息等。有时我们需要显式地访问参数的值，有时我们呢则需要访问参数类的实例  
`print(net[2].bias) #访问参数类的实例`  
`print(net[2].bias.data) #访问参数的值`

#### 一次性访问所有参数

利用Pytorch中的`parameters`或`named_parameters`方法访问所有参数

```python
for name, param in net[0].named_parameters
	print(f"{name}: {param})
```

对于彼此嵌套的块，我们向访问多层嵌套的列表一样用索引访问即可

### 参数初始化

#### 内置初始化方法

```python
def init_normal(m):
	if type(m) == nn.Linear
		nn.init_normal_(m.weight, mean=0, std=0.01)
		nn.init.zeros_(m.bias)
net.apply(init_normal)
# 常见的方法还有nn.init.constant_, nn.init.xavier_uniform_等
```

#### 自定义初始化方法

直接在内置的初始化方法上修改即可

## 参数绑定

我们可以定义一个共享的参数层，然后用它的参数来设置另外一层的参数

```python
share = nn.Linear(8,8)
net = nn.Sequential(nn.Linear(4,8), nn.ReLU(), shared, nn.ReLU(), share, nn.ReLU())
```

好处：

- 对于图像识别中的CNN，共享参数使网络能够在图像中的任何地方而不是仅在某个区域中查找给定的功能。
- 对于RNN，它在序列的各个时间步之间共享参数，因此可以很好地推广到不同序列长度的示例。
- 对于自动编码器，编码器和解码器共享参数。 在具有线性激活的单层自动编码器中，共享权重会在权重矩阵的不同隐藏层之间强制正交。

## 读写文件

### 加载和保存张量

对于单个张量，我们可以用load和save函数分别读写它们，同时为我们需要读写的张量提供名称

```python
import torch
from torch import nn
from torch.nn import functional as F

x = torch.arange(4)
torch.save(x, 'x-file')
x2 = torch.load('x-file')
# 读写张量列表
y =troch.zeros(4)
torch.save([x,y], 'x-files')
x2, y2 = torch.load('x-files')
# 还可以读取或写入字符串映射到张量的字典
mydict = {'x':x, 'y':y}
torch.save(mydict, 'mydict')
mydict2 = torch.load('mydict')

```

## 加载和保存模型参数

调用框架的内置函数来保存整个模型的参数

```python
class MLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.hidden = nn.Linear(20, 256)
        self.output = nn.Linear(256, 10)

    def forward(self, x):
        return self.output(F.relu(self.hidden(x)))

net = MLP()
X = torch.randn(size=(2, 20))
Y = net(X)
# 保存模型的参数
torch.save(net.state_dict(), 'mlp.params')
# 恢复模型时，直接实例化模型的备份，再读取保存的参数
clone = MLP()
clone.load_state_dict(torch.load('mlp.params'))
```