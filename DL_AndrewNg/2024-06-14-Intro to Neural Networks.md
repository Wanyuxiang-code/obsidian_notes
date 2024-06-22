---
title: 2024-06-14-Intro to Neural Networks
date: 2024-06-14
date modified: 2024-06-22
categories: DeepLearning
---

## 总体结构概览

Input layer -> Hidden Layer -> Output Layer

- Input layer:  
  输入的数据集，通常通过将原始数据表征为高维向量形式，再通过将不同的输入数据所对应的高位向量堆叠起来形成完整的矩阵。
- Hidden Layer:  
  隐藏层的含义，隐藏层中的节点数据并不直接包含在输入数据集中，而是通过参数的初始化与训练的反复迭代而形成。  
  **在无监督学习中目标结果也未在初始训练数据集中给出**
- Output Layer  
  输出层则负责训练的最终预测值，通常与目标结构相结合计算损失函数

## 计算框架

### 前向传播

前向传播的核心思路主要包括两层，先对前一层的激活值进行线性组合再加上偏移值，再通过对前一步所得到的结果施加激活函数实现非线性化。  
**Input $A^{l-1}$, output $Z^{l},A^{l}$**

#### Notation

- L:表示神经网络的层数
- $n^{l}$ 表示神经网络当前层的节点个数
- $a^{l}$ 表示当前层节点的激活值输出
- $w^{l}$ 表示当前层的权重矩阵,等价于

  $$

w^{T} = \begin{bmatrix}  
w_{1}, w_{2}, \dots, w_{n_{l-1}}  
\end{bmatrix}

$$
#### 线性组合激活值
在前一层激活值的基础上，我们对其进行线性变换，得到当前层的 $z^{l}$ 作为激活函数的输入值
$$

z^{l} = w^{l}a^{l-1} + b^{l}

$$
将其整体向量化以后，我们可以得到：
$$

Z^{l} = w^{l}A^{l-1} + b^{l}

$$
向量化即为将m个样本集所对应的高维向量堆叠成为矩阵
$$

\begin{align} \\  
&w^{l}\in \mathbb{R}^{n_{l}*n_{l-1}} \\  
&a^{l} \in \mathbb{R}^{n_{l}} \\  
&A^{l} \in \mathbb{R}^{n_{l}*m}  
\end{align}

$$
#### 利用激活函数实现非线性化
> [!Note] Why Activation Function
>  如果整个神经网络的中间层均采用线性函数，那么堆叠多层神经网络没有任何意义，因为均可用一次线性变化完成

> [!Important] 激活函数的种类
- Sigmoid Function:
$$

\begin{align}  
&\sigma(z) = \frac{1}{1+e^{-z}} \\  
&\frac{d}{dz}\sigma(z) =\sigma(z)(1-\sigma(z))  
\end{align}

$$
- Tanh Function:
基本上能够完全替代sigmoid function，事实上它即为sigmoid函数向下平移至关于原点对称的结果
$$

\begin{align}  
& \tanh(z) = \frac{e^{z} - e^{-z}}{e^{z} + e^{-z}} \\  
& \frac{d}{dz}\tanh z = 1-(\tanh z)^{2}  
\end{align}

$$
- ReLu Function(Rectified Linear Unit)
$$

g(z) = max(0,z)

$$
- ReLU函数的变体: PReLU（Parameterized ReLU)
通过增加线性项当参数为负时保留部分信息
$$

pReLU(x) = max(0,x) + \alpha min(0.x) 

$$
### 反向传播
完成正向传播的计算框架后，我们需要对随机初始化得到的参数进行进一步优化，而这一步则依赖于梯度下降实现，[[2024-06-12-Logistic Regression]]
为了实现梯度下降，最核心的步骤即为计算复合函数的导数，然后通过梯度下降实现对cost function的优化
**Cost Function：**
$$

J(W^{1},\dots,W^{L},b^{1},\dots,b^{L}) = \frac{1}{m}*\sum_{i=1}^{m}\mathcal{L}(\hat{y},y)

$$
计算框架：从J往前一直求所对应的W,b对应的偏导，在通过梯度下降完成一次迭代优化
**Input $dA^{l}$, Output $dZ^{l-1},dA^{l-1}$，同时得出的 $dW^{l},db^{l}$**

$$

\begin{align}  
&dZ^{l} = dA^{l}*g^{l'}(Z^{l}) \\  
&dW^{l} = \frac{1}{m}dZ^{l}A^{[l-1]T} \\  
&db^{l} = \frac{1}{m}np.sum(dz^{l},axis=1,keepdims=true) \\  
&dA^{l-1} = W^{[l]T}dZ^{l}  
\end{align}

$$
然后进行梯度下降即可
$$

\begin{align}  
&W^{l} = W^{l} -\alpha dW  
&b^{l} = b^{l} -\alpha db  
\end{align}

$$
## 为什么选用深层网络
深层网络能够通过隐藏层深度的逐级递增实现对输入数据的复杂特征的逐步学习，而相比之下浅层神经网络想要达到相同的学习效果可能需要呈指数级别增长的节点。

## 参数与超参数(Hyperparameters)
### 超参数
- 学习率
- 节点个数
- 迭代次数
- L
- $n^{l}$
- 激活函数种类
- 正则化与归一化选择等