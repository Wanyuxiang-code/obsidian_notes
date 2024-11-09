---
title: Discrete-type Random Variables 2
date: 2024-10-10
date modified: 2024-11-09
categories: ECE313
tags:
  - ECE313
---
#ECE313 

## Maximum Likelihood Parameter Estimation 最大似然估计

**Definition**  
利用特定的概率分布（未知参数）对现实情境建模，我们可以得到随机变量 $X=k$ 的概率似然估计 $p_{\theta}(k)$, 对于观察结果 k 的最大似然估计即为使 $p_{\theta}(k)$ 最大的参数 $\theta$ 的值， 记为

$$
\hat{\theta}_{ML}(k)
$$

**Situation**
- Parameter Estimation: 给定 k,对于 $\theta$ 最大化似然估计
- Guessing Game: 给定 $\theta$ ，相对于 k 最大化似然估计  
**Strategy**  
核心即为明确哪些参数为固定，哪些参数待优化，然后转换视角，再进行最优化

## Markov and Chebychev inequalities and confidence intervals

### Markov Inequality

在已知均值时，估计给定随机变量取值的概率 (**注意随机变量需要非负**)  
![acdd000ca40bbcb54a59f36003f7a45.png](https://s2.loli.net/2024/10/10/nzOSafVlTgZip7h.png)

证明：即将小于 c 的部分全部放缩为 0  
![636dcd17706c4f54a9a62c5536c3957.png](https://s2.loli.net/2024/10/10/4Ibiq7ytvDLzQmR.png)

### Chebychev Inequality

利用方差估计分布的均匀性  
![bb620ba54c64a0e838e0bdd24b71486.png](https://s2.loli.net/2024/10/10/GPhtcqgKvrS4IMb.png)  
证明即为：在 Markov Inequality 中将 Y 取为 $|X-\mu|^{2}$ , c 取为 $d^{2}$ 

### Confidence Interval

**Background**:  
利用小样本对实际情境进行建模，将其模拟为二项分布，我们有

**注意 $\hat{p}$ 为 sample probability**, 为随机变量； $p$ 是真正的概率，非随机变量

![949c225a7f6c5ee1f06ee30fc2d74cf.png](https://s2.loli.net/2024/10/10/9BoNaQ6irtwxsJz.png)

**注意 p 并非随机，但是在真实实验开始前无法确定，但该区间为随机区间**  
对于 Confidence Interval 我们应确定其具体的值 ->要求对未知的 $p(1-p)$ 进行放缩,$p(1-p)\leq 0.25$  
![5d5b40be30f5bf4f5cb7330948d7ca6.png](https://s2.loli.net/2024/10/10/V7QkON82m3zCBYh.png)  
![f312aba5aefc1aec1b1ed5a6e283412.png](https://s2.loli.net/2024/10/10/M6mCfPd8NptbanX.png)

## The Law of Total Probability and Bayes Formula

全概率定律与贝叶斯定理

### Law of Total Probability

![db770a85b082ddf56c18822b83d57e2.png](https://s2.loli.net/2024/10/10/UXueFVCr6L8Kgfo.png)

即我们可以对整个概率空间进行划分，然后在划分的基础上对其他事件进行分类（在某些情况下可以理解为对全集采取一定的分类标准）

### Bayes Formula

![ef8e5e155e04515cec192ba3248aad3.png](https://s2.loli.net/2024/10/10/XtH3cVQWE5DT47o.png)  
![24027916f050056d144a29355171fde.png](https://s2.loli.net/2024/10/10/T5IPu1fCO8rbnKe.png)

利用全概率定律计算均值  
![21adde9be7d6e0364c60e7e1502b9f5.png](https://s2.loli.net/2024/10/10/svM23UxYbJwN7Ze.png)  
![da0f92ba41500a6f167c0c003cd1323.png](https://s2.loli.net/2024/10/10/SqxobgehvfRZciI.png)

## Binary Hypothesis with discrete-type observation

![ba5186e333deded972038d4d672231f.png](https://s2.loli.net/2024/10/21/OsmUtnkeFIxXgZf.png)  
**综述**：  
每一种假设对应离散型随机变量不同的概率密度函数，最终构成一个似然矩阵。注意两种假设互斥，但不一定成立，系统最终的输出结果根据确定的 decision rule 既可能 $H_{1}$ 也可能为 $H_{0}$  
表示 Decision Rule: 在似然矩阵对应的项下划线



最终观察结果有四种：  
![4ccac4c444e2c2571e567e75fcdaff4.png](https://s2.loli.net/2024/10/21/JrixY1sQOzcnjwP.png)  
![99e36e2f8cca0bf54c065b87a543303.png](https://s2.loli.net/2024/10/21/zL3UAStG62qeyXu.png)  
**利用条件概率给出定义**：即为似然矩阵中相应行中没有划线的项

$$
\begin{align}
& p_{false alarm} = P(\text{declare H1 true| H0})  \\
& p_{miss} = P(\text{declare H0 true| H1})
\end{align}
$$

如何确定 Decision Rule -> 衡量不同 rules 对 p(false alarm) 与 p(miss) 的影响

$$
p_{e} = \pi_{0}p_{false alarm} +\pi_{1}p_{miss}
$$

### Maximum Likelihood decision rule

**Definition**:  
The ML decision rule declares the hypothesis which **maximizes the probability (or likelihood) of the observation**. Operationally, the ML decision rule can be stated as follows: Underline the **larger entry** in each column of the likelihood matrix.

**利用 likelihood ratio test(LRT) 定义**：  
即定义一个 ratio，然后根据 ratio 和 1 的关系决定

![21fd2717df54db5247ac4dbfc25b38d.png](https://s2.loli.net/2024/10/21/f2ln7L8qocjiWJS.png)

![8bbd155545dcf37760b4a37a00a5bae.png](https://s2.loli.net/2024/10/21/965VXZnDMwIclfF.png)

### Maximum a posteriori probability(MAP) decision rule

**Definition**:  
首先引入先验概率（prior probabilities), 分别记为：

$$
\begin{align}
& \pi_{1} = P(H_{1}) \\
& \pi_{0} = P(H_{0})
\end{align}
$$

有了先验概率以后，结合观测结果我们得到联合概率：

$$
P(H_{i}, X = k) = \pi_{i}p_{i}(k)
$$

这样我们即可得到联合概率矩阵（似然矩阵的每一行乘对应的先验概率）

再根据后验概率 (posteriori probability) 的大小确定 decision rule(后验概率记为确定观测结果后的条件概率)

$$
P(H_{1} | X=k) \ P(H_{0} | X=k)
$$

**利用 LRT 表述**：  
![fd4164229bbef0ffcd1cf8565fd7a05.png](https://s2.loli.net/2024/10/21/EvPszUG65aOb4wT.png)
 
 MAP 能够最小化 P(error)

## Reliability

### Union Bound

![cb0ddc9ac7138d4de5363bd34966e76.png](https://s2.loli.net/2024/10/22/EJ5gZHsroGLPDX3.png)  
**利用容斥原理即可证明**：

$$
P(A) + P(B)-P(A \cup B) = P(AB)
$$

- 当 P(A) 与 P(B) 概率都很小且相互独立时上界比较准确
- 当 P(A) 与 P(B) 概率都很大时不容易得到有效的估计  
注意:

$$
P(AB) \leq min\{P(A),P(B)\}
$$

推广到 m 个事件，我们有：  
![7b58262c49d4c400d2e3caf53b2a70d.png](https://s2.loli.net/2024/10/22/ftcYVeNmvbH1yDB.png)

### Network outage probability

**概念**：  
Network outage is said to occur if **at least one link fails along every s -> t path**(s 为起点，t 为终点,即无法形成通路）, where an s -> t path is a set of links that connect s to t: Let F denote the event of network outage. We will find P(F) for each of the ve networks, and then apply the union bound to get a simple upper bound to P(F) for networks B through E:  
![765a270f3c3a9a78e2c657f0fbd0cdc.png](https://s2.loli.net/2024/10/22/rzMgaRbiYGfABjQ.png)  
计算时可以考虑适当分类，或将复杂情况递归到简单情形解决（例如将阶段与阶段间化简），或者将复杂情况与简单情况比较进行计算

![bfd50b1ef10e5b2e79f2bf1e8ad2988.png](https://s2.loli.net/2024/10/22/qznU2OjIVeoMuJ5.png)

**通过枚举每条 link 的状态也可计算**

### Distribution of the capacity of a flow network

**Definition**  
The capacity of an s->t flow network is the maximum flow rate from scto t: The capacity is random because of the possible link failures. We will compute the pmf of the capacity of each of the two networks.

**注意**:  
Capacity flow 取的是最大值，同时要关注后续的 PATH 能否承载之前的大容量，需所有途径的管线都能满足

### Analysis of an array code

**利用奇偶校验检查错误，对于 4bit 以上的错误可能无法检测**  
估计上界的方法：
- 考虑将所有的事件变为 4bit 事件出错的并集，用 union bound 估计  
![b9145fa614747124a4237de4542191e.png](https://s2.loli.net/2024/10/22/Ksy1B8TwOWqQzkR.png)
- 考虑将所有事件变为选择两行两列事件的并集再加上 6bit 以上的错误  
![d39f87a4934fb13b8e9be4983588eb0.png](https://s2.loli.net/2024/10/22/jZGiPS5epdoAb7y.png)

### Reliability of a single backup

**通过用几何分布估计均值来粗略估计**  
![74680034857a5dadb9a90ed8eaacda8.png](https://s2.loli.net/2024/10/22/ZtAQ5Hu1xgkC4Rn.png)

