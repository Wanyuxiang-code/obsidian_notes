---
title: Partial Derivatives 2
date: 2024-11-05
date modified: 2024-11-09
categories: Math241
tags:
  - Math241
---
#Math241 

## Mean Value Theorem and its friends

### Theorem

![857e0f79cabc1a5e287bade3ef66a27.png](https://s2.loli.net/2024/11/05/ifDGbwpNJKuBmSo.png)

**通过构造一个单变量函数 $\phi$ 构造从 $[0,1]$ 到对应 f 路径内点的映射，结合一维的 Mean Value Theorem**  
注意起点与终点所遍历的点都需位于定义域内

### Integral Version

![9a81bcfd521d81373eaa74db49b7080.png](https://s2.loli.net/2024/11/05/CaszcnFo9lXpTJN.png)

### Another Theorem

![b1bdbb4c2b0557cee7a6269983b1129.png](https://s2.loli.net/2024/11/05/KSDvOsbjnaZCV5c.png)
- 注意 Path-Connected 并不一定意味着 D 中没有 holes, 表示的是对于定义域中任意两个点，都可以找到一条连续的路径历经定义域中的点将其相连
- 证明只需考虑 m=1 的情况（因为各分项均为常数，同理）
- 证明利用 Mean Value Theorem 的积分形式，不失一般性考虑一个 smooth 的函数  
![8be46319e6723c331f116a3cfb5a27b.png](https://s2.loli.net/2024/11/05/z4tCxGhNdsQ5mul.png)

### Intermediate Value Theorem 介值定理

![d122379be45e756827869cd2b0d5433.png](https://s2.loli.net/2024/11/05/SypiJLlOTWnNZYR.png)  
**注意介值定理的泛化表述告诉我们对于一个连续的函数，从一个连续的区间可映射到另一个连续的区间**

### Path-Connected and Connected

![03aadb241ec8fd19fea085c10be2d42.png](https://s2.loli.net/2024/11/05/ghf9aiO1zBlZ4ow.png)

### Application-Error Propagation

![8648f45904dc0686f15765a356f7225.png](https://s2.loli.net/2024/11/05/2OPJLjWADacufBl.png)

**利用 Mean Value Theorem 将模糊的小 o 表示转化为精确的数值**  
Mean Value Theorem 可直接将对应增量的结果转化为 ->起点与终点线段上某点的导数

**实际应用中往往用于控制上界，因为往往只能控制住误差的上界**

求解过程中：
- ==关注对应每个变量误差的上界==
- ==每个对应变量偏导在对应超矩形范围内的上界（绝对值）==  
![9a4271b31f39df37b61da8df5343633.png](https://s2.loli.net/2024/11/05/wPbO2KWxdAnIpqR.png)

**误差分析的 Example: 注意课本没有涉及 Mean Value Theorem，通过考虑 Mean Value Theorem 对上界进行更好的估计**  
![7086493b43e1f772c3a060dbde82a65.png](https://s2.loli.net/2024/11/05/qrMBNOKCioklJ1x.png)  
![e79102d68fe814e3f62fe6869b73c37.png](https://s2.loli.net/2024/11/05/8t7K1sneucQa4Ah.png)

#### Relative Error

**Approximate Form**(考试时哪种形式？)  
![19f9c296469fdad9126277a0da15a65.png](https://s2.loli.net/2024/11/05/vn3bkGBTKMEjAaI.png)

将整体写成 $\frac{\Delta x_{j}}{x_{j}}$ 的形式更容易看出相对误差

**Rigorous Estimate**  
![ec4590f9f0b81f1fde653a9e3a7bdd5.png](https://s2.loli.net/2024/11/05/9CGpX5sQohYzVLr.png)

#### Floating-point Numbers

**Definition**  
![b21d64bf447939b0b2c617a88275847.png](https://s2.loli.net/2024/11/07/tvp3wIXVDYjizn7.png)  
**Precision** when taking standard arithmetic functions   
对于减法，浮点运算不是良定义的，因为无法控制其相对误差的上界

## Implicit Differentiation

![4b66433bec5afe1335e19a1190aadae.png](https://s2.loli.net/2024/11/07/TBs61umh4EiazOe.png)

**之前在利用 Chain Rule 研究 gradient 与 countour hypersurface 时，我们发现两者的垂直关系，现在我们可以利用这一关系，确定之前隐式定义的从 (n-1) 维到 (n) 维的参数化的映射**

### Example

给定

$$
F(x,y,z)= x^{3}+y^{3}+z^{3}+3xyz 
$$

我们考察其的 Coutour

$$
F(x,y,z) =1
$$

在添加了一个限制条件后，我们即可以对原有的三维自由变量进行降维（考虑自由度的变化），因此，我们可以找到一个映射 g 对原有三维变量进行 Parametrization

$$
F(x,y,g(x,y)) = 1
$$

那么我们可以根据 Chain Rule 考察我们隐式定义的映射的偏导情况  
![3e3c9631cbf85c75a6d09581624cd86.png](https://s2.loli.net/2024/11/07/e2pGmx6AwU5aMlh.png)

**进一步地，我们考察这个隐式定义的函数的定义域的情况**
- 为什么会有定义域的问题？->考虑到对曲面参数化的过程中，有时会出现无法满足函数定义的情况，那么我们需要对整体参数化的函数定义域进行一个划分或者邻域的限制，使其可以满足条件  
![efdca5660f94bc223685ca030fc0039.png](https://s2.loli.net/2024/11/07/4IvXt9Aaj36iWSQ.png)
- Implicit Function Theorem

![de23692f735ddc943747c1c8dfd6ba5.png](https://s2.loli.net/2024/11/07/isc5lIam1CkdGhU.png)

## Higher Derivatives

**考虑高维的微分时，将对于每一个变量求偏导视作一个映射或算子，输入为函数，输出也为函数**  
![8a03e459e8fa59c7f22d4d54f155673.png](https://s2.loli.net/2024/11/07/zDTwvKt7UpVJgiA.png)

### Clairaut's Theorem

![8120188a619bbee70ab2ab66d71233d.png](https://s2.loli.net/2024/11/07/yeo9aOHWrGXvxbp.png)

**对于高阶偏导，可以置换具体求偏导的过程变量，仍不改变最终结果**
