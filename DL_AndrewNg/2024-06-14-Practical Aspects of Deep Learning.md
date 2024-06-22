---
title: 2024-06-14-Practical Aspects of Deep Learning
date: 2024-06-14
date modified: 2024-06-22
categories: DeepLearning
---

## 数据集分类

为了不断优化我们所采用的深度学习框架，我们需要在实践过程中根据反馈结果不断迭代优化我们的算法或者超参数的选择，这就需要我们对所使用的数据有提前规划。  
深度学习所采用的数据集在用途上可划分为三类，分别是：训练集(train sets),验证集(dev sets),测试集(test sets)

### 开发集（Dev Set）

**定义**：  
开发集，也称为验证集（Validation Set），是从训练数据中分离出来的一部分数据，用于在模型开发过程中进行模型选择和参数调优。  
**用途**：
- **模型选择**：在开发集上评估不同模型的性能，以选择最佳模型。
- **参数调优**：在开发集上调整模型的超参数（如学习率、正则化参数等），以找到最佳超参数组合。
- **过拟合检测**：通过监控开发集上的性能，可以检测模型是否过拟合训练数据。  
**特征**：
- 开发集用于模型开发阶段。
- 开发集上的性能用于指导模型和超参数的选择。
- 开发集的大小通常较小，但应足够代表数据的多样性。

### 测试集（Test Set）

**定义**：  
测试集是从训练数据中完全独立的一部分数据，用于在模型开发完成后对模型进行最终评估。  
**用途**：
- **最终评估**：在测试集上评估模型的性能，以获得对模型在未见数据上的泛化能力的客观估计。
- **比较模型**：在测试集上比较不同模型的性能，以选择最优模型用于实际应用。  
**特征**：
- 测试集用于模型开发完成后的最终评估阶段。
- 测试集上的性能用于报告模型的最终性能。
- 测试集的大小应足够大，以提供可靠的性能评估。

**Notice:测试集旨在为训练的模型提供unbiased evaluation,如果我们不需要unbiased evaluation，我们可以直接省去测试集，直接利用dec sets衡量模型在现有训练集下的有效性**  
**在大数据时代，训练集所占的比重远远大于开发集与测试集**

## Bias & Variance(偏差与方差)

> [!Important] Understanding Bias & Variance  
> Bias:
>
> >Bias 强调的是已训练好的模型对于训练集与测试集中数据拟合的能力，若拟合能力弱我们则称模型的bias较高,常常对应的是underfitting状态
>
> Variance
>
> >Variance强调的是已训练好的模型在训练集与测试集中bias大小的差异，如果差异较大，则称variance较高，常常对应的是over fitting状态

### 处理策略

1. High Bias:
   - 改进算法
   - 扩大网络规模
2. High Variance:
   - 增大数据集
   - 正则化(Regularization)

### 正则化（Regularization)

正则化的核心想法为通过平衡随着训练层数指数增大或减小的权重对于最终结果的影响，以避免过拟合的状态

#### 添加正则化参数 $\lambda$

- L2正则化：引入权重矩阵的欧几里得范数平方

$$
J(W,b) = \frac{1}{m}\sum_{i=1}^{m}\mathcal{L}(\hat{y},y) + \frac{\lambda}{2m}\sum_{l=1}^{L}||W_{l}||_{2}^{2}
$$

其中 $||W||^{2}_{2}$即为矩阵中所有元素的平方和（该范数也被称为Frobenius norm),$\lambda$则需要根据实际训练情况不断进行调整优化

- L1正则化： 引入权重矩阵的欧几里得1阶范数

$$
J(W,b) = \frac{1}{m}\sum_{i=1}^{m}\mathcal{L}(\hat{y},y) + \frac{\lambda}{m}\sum_{l=1}^{L}||W_{l}||_{1}
$$

**原理**  
关注添加正则化参数后对梯度下降更新参数的影响：

$$
W = W - \alpha dW' = W - \alpha\left( dW + \frac{\lambda}{m}W \right) = \left( 1-\frac{\alpha\lambda}{m} \right)W - \alpha dW
$$

我们发现通过引入正则化参数，权重不断衰减，而权重的不断衰减则简化了原本复杂的神经网络，随着 $\lambda$的增大，神经网络逐渐向线性网络转化，降低过拟合

#### Drop out 正则化（随即失活）

利用drop out 防止过拟合的核心即为通过引入随即失活概率，让每一层的节点以一定概率随机变为0，简化原有神经网络的复杂结构，避免过拟合  
**实现**

```python
dl = np.random.rand(al.shape[0],al.shape[1])
al = np.multiply(al,dl)
al /= keep-prob
# Another way
def dropout(x, dropout):
	assert 0 <= dropout <=1
	if dropout == 1:
		return torch.zeros_like(X)
	if dropout = 0:
		return X
	mask = (torch.rand(x.shape) > dropout).float()
	return mask*x/(1.0 - dropout)
```

通过keep-prob参数来控制保持不失活的概率，同时注意让部分失活后的向量除以保持概率以维持均值期望不变  
反向传播时从后往前依次执行dropout  
**注意：每一层的keep-prob参数可相互独立，可根据具体需求针对性调整，比如对于较复杂的层适当减小keep-prob**

**缺点：Cost Function J 现在是不良定义，我们通过直接观察J的数值变化来确定我们迭代的有效性** -> 再开始用drop out之前先保证J随迭代次数的增加单调递减

#### Data Augmentation

在输入的数据有限的情况下,我们可以通过对原有数据进行适当微调作为补充,如翻转,旋转,等比例缩放等.

#### Early Stopping

Early Stopping的核心想法为绘制训练集与测试集随着迭代次数bias变化的曲线,在两者发散的时候停止迭代,如果此时的bias较小,那么我们可以获得bias较小且variance也较小的模型  
**缺陷:将对bias与variance优化的过程融合在一起,使得我们不能够独立地分别优化这两者**

## 加快训练速度

### 归一化输入(Normalizing Inputs)

#### 将均值调整为0

调整均值为0核心思路即为通过对数据整体减去均值,使得得到的新数据均值为0

$$
\begin{align}
\mu = \frac{1}{m}\sum_{i=1}^{m}x^{i} \\
X = X - \mu
\end{align}
$$

#### 归一化方差

将方差调为0可以避免输入数据中过大或者过小值对于整体权重的过分影响,同时是最终的cost function关于各个参数较为均衡,避免梯度下降时过快或过慢以致难以获得最小值

$$
\sigma ^{2} = \frac{1}{m}\sum_{i=1}^{m}(x^{i})^{2}
$$

$$
x^{i} = \frac{x^{i}}{\sigma}
$$

### 权重初始化

如果权重的初始值在一开始被设置的偏大或者偏小将会导致我们的最终结果随网络深度的增加呈指数级的增大或减小,这就需要我们在初始化权重时选择合适地范围.  
**防止梯度爆炸或者梯度消失**  
**核心思路: 根据该层网络节点的数量来调整权重的初始的大小**  
假设权重与输入彼此独立，进行线性变化后，我们会有输出的均值为：

$$
\begin{align}
E_{[o_{i}]} & = \sum_{j=1}^{n_{in}}E[w_{ij}x_{j}]  \\
& =\sum_{j=1}^{n_{in}}E[w_{ij}]E[x_{j}]  \\
& = 0  \\
Var[o_{i}] &=  E[o_{i}^{2}] - (E[o_{i]}])^{2}  \\
& = \sum_{j=1}^{n_{in}}E[w_{ij}^{2}x_{j}^{2}]  \\
& = \sum_{j=1}^{n_{in}}E[w_{ij}]^{2}E[x_{j}]^{2}  \\
& = n_{in}\sigma ^{2}\gamma ^{2}
\end{align}
$$

 `Xavier初始化`: 将权重根据输入层与输出层的维数初始化，尽量保持中间值的方差稳定性，防止出现梯度消失与爆炸

$$
\sigma = \sqrt{ \frac{2}{n_{in} + n_{out}} }
$$

> [!important] 根据激活函数调整缩放比例

- ReLu函数: $\frac{2}{n}$
- tanh函数: $\frac{2}{n ^{l-1} + n ^{l}}$

### 梯度检验(Gradient Checking)

#### 梯度数值逼近

利用二阶差分进行梯度数值逼近效果好于一阶差分:

$$
d\theta = \frac{f(\theta+\epsilon)-f(\theta-\epsilon)}{2\epsilon}
$$

该估计式的精度为O($\epsilon ^{2}$),而一阶差分则为O($\epsilon$)

#### 检验

通过比较估计的梯度与实际反向传播计算出来的梯度,判断计算过程是否正确  
**如何描述近似程度?**

$$
\frac{||d\theta_{appro} - d\theta||_{2}}{||d\theta_{appro}||_{2}+||d\theta||_{2}}
$$

一般我们取 $\epsilon$ 为 $10^{-7}$, 当计算结果为 $10^{-7}$ 及更小说明我们的梯度下降大概率没问题,但当计算结果大于 $10^{-5}$ 时我们需要更仔细地检查

#### 注意

- 梯度检验仅用于debug
- 注意如果使用了正则化,注意计算时包括正则项
- 不适用于drop out
- 随机初始化权重