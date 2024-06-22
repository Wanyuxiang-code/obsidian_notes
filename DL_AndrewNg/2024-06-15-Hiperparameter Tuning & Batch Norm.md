---
title: 2024-06-15-Hiperparameter Tuning & Batch Norm
date: 2024-06-15
date modified: 2024-06-22
categories: DeepLearning
---

## 超参数调节(Hyperparameter Tuning)

### 参数重要性(直觉)

1. Learning Rate: $\alpha$
2. exponential parameter: $\beta$, number of hidden units, mini-batch size
3. number of layers, learning rate decay

### 调试过程

常见的调试方式：

- Use grid to choose parameters:  
将多参数以一定的范围轴划分，规则取点
- **Randomly choosing**  
在给定区域内随机去点->相比在网格范围内规则取点，随机化取样能够更好地探索模型对于不同的超参数的敏感程度，能够在节省训练时间的同时使出更多关键性参数与范围

### 随机调试执行细节

1. 调试范围一般由粗糙到精细：  
  在前期小范围样本调试过程中，我们有时能够发现更为关键的超参数区域，这是我们可以调节随机选取参数范围，更针对性地调节
  2. **随机取样轴有时采取对数轴，而非线性轴**:  
  超参数对于最终模型训练的影响很多时候并非线性变化，如果采取在线性轴上随机去点的方式可能会导致在真正对模型性能有影响的关键区域我们选取的测试参数较少  
  ->采取在对数轴上随机取点方式
  3. 根据具体的参数情况选取调试细节  
例如：当我们在0.9-0.999范围内调节参数 $\beta$ 时，我们可以考虑用1-$\beta$ 再在对数轴范围内取样（理论基础也是因为 $\frac{1}{1-\beta}$ 表示了指数平均的大概天数）

### 常见调试模式

1. Babysittinbg one model  
当现有算力只能支撑我们调试一个模型时，我们考虑从采取对一个模型进行超参数的精细调节
2. Training many models in parallel  
算力充足时我们可以在同样的数据集上同时调试多种模型，通过比较他们不同的损失函数择优选择

## Batch Norm

### 核心想法

通过对深层神经网络的每一层中的z都进行正则化，我们可以减少神经网络不同层之间的连接关系（因为正则化参数的均值和方差都可以经过训练得出），这样增强了模型在不同训练集上的稳定性。归一化使得即使因为训练集的输入发生了改变，但由于正则化这一步骤的存在，使得每层网络之间训练的独立性增强。  
同时batch norm由轻微的正则化效果，因为不同的mini-bacth的均值与方差均不同，所以在训练的过程中给模型增加了噪声，一定程度上减少了过拟合

### 具体实施

在mini-batch下，对每层网络的 $z^{l}$ 进行正则化并根据需求训练新的均值与方差参数  
总体正向传播训练框架：  
$A^{l-1}$ -> $Z^{l}$ -> $\tilde{Z^{l}}$ -> $A^{l}$  
正向传播过程：

$$
\begin{align}
& Z^{l} = W^{l}A^{l-1} + b^{l}   \\ 
& \mu = \frac{1}{t}\sum_{i=1}^{t}z^{i}  \\
& \sigma^{2} = \frac{1}{t}\sum_{i}(z^{i}-\mu)^{2} \\
& \tilde{Z^{l}} = \frac{Z^{l} - \mu }{\sqrt{ \sigma ^{2} + \epsilon}} \\
& \tilde{Z^{l}} = \beta ^{l}\tilde{Z^{l}} + \gamma ^{l} \\
& A^{l} = g^{l}(\tilde{Z^{l}})
\end{align}
$$

**Notice:由于我们对于整体训练对象进行了了正则化，所以 $b^{l}$ 作为偏置参数最终不会对结果有任何影响，所以我们可以直接将其删去或者默认设为0**

利用梯度下降更新 $d\beta$ 与 $d\gamma$ (也可采用momentum或Adam或RMSprop)

$$
\begin{align}
\beta = \beta -\alpha d\beta \\
\gamma = \gamma -\alpha d\gamma
\end{align}
$$

#### 不同Mini-Batch上 $\mu$ 与 $\sigma ^{2}$ 的计算

当我们采用mini-batch训练时，由于我们并没有遍历整个数据集，所以不同mini-batch的归一化时采用的均值方差不同 -> 我们采用指数加权平均的方式来寻找这些参数的均值

$$
\begin{align}
& v_{\mu} = \beta v_{\mu} +(1-\beta)\theta_{\mu}  \\
& v_{\sigma ^{2}} = \beta v_{\sigma ^{2}} + (1-\beta)\theta_{\sigma ^{2}}
\end{align}
$$

## Softmax回归

### 背景

在二分类问题中，通常我们的输出仅为0或1，但是当我们在实际问题中需要分类的对象多于两个，那么我们就需要调整神经网络最后一层的输出函数，使其输出对于不同所分类的概率

### Softmax激活函数

**Softmax得名原因：相比于hardmax之间输出hot-encoding向量（直接将最大输出概率可能设为1，其余均为0）**  
在最后一层中，通过用指数函数对其中向量进行加权：

$$
a^{l} = \frac{e^{z^{l}}}{ \sum_{i=1}^{t}e^{z_{i}}}
$$

Loss Function:

$$
\mathcal{L}(\hat{y},y) = -\sum_{i=1}^{t}y_{i}\ln(\hat{y_{i}})
$$

Cost Function:

$$
J = \frac{1}{m}\sum_{i=1}^{m}\mathcal{L}(\hat{y^{i}},y^{i})
$$

Derivative:

$$
dz^{L} = \hat{y} - y
$$