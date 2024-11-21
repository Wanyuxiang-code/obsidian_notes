---
title: Jointly Distributed Random Variables
date: 2024-11-18
date modified: 2024-11-20
categories: ECE313
tags: [ECE313]
---

#ECE313 

## Basic

### Joint Cumulative Distribution Functions

**Definition**  
![bff02b435ece6d2d0de448774b1c549.png](https://s2.loli.net/2024/11/18/4bn85AGeYRkvJpi.png)  
利用图像定义，我们有：  
![1503fa10d7d5b3301a4b512a6165ae1.png](https://s2.loli.net/2024/11/18/5bGxn2kKNPfdYQB.png)  
对于分布在一个区域内的联合概率分布，我们有：  
![f3c3492e824e5a30980a40112c00c16.png](https://s2.loli.net/2024/11/18/NBjpJaStQh4u2wi.png)  
**Proposition**  
![eba27925179fb3e2818611b8d432acd.png](https://s2.loli.net/2024/11/18/LVwJUKhjobAZSB8.png)  
![5ee3ace9ddc3dfd44cfa2260ad901e2.png](https://s2.loli.net/2024/11/18/Fi2ahmwd1qRASZz.png)  
**Properties**  
![884243101b5c07d10fe48659d4b8b6f.png](https://s2.loli.net/2024/11/18/TitVqR6yr1EJclz.png)

### Joint Probability Mass Functions & Density Functions

**离散型随机变量 -Joint Probability Mass Functions**  
考虑在同一个概率空间中的离散型随机变量 $X,Y$ ，其联合概率质量函数:

$$
P_{X,Y}(u,v) = P(X=u,Y=v)
$$

同时结合全概率定理，我们可以由联合概率质量函数导出分别的概率质量函数

$$
P(X=u) =\sum_{j}P(X=u,Y=v_{j}) 
$$

这等价于

$$
p_{X}(u) =\sum_{j}p_{X,Y}(u,v_{j})
$$

在这种情况下 $p_{X},p_{Y}$ 被称为 联合概率质量函数 $p_{X,Y}$ 的 marginal pmfs,另外 conditional pmfs 由如下 joint pmf 定义:

$$
P_{Y|X}(v|u_{0}) = P(Y=v |X=u_{0}) = \frac{P_{X,Y}(u_{0},v)}{P_{X}(u_{0})}
$$

**连续型随机变量 -Joint Probability Density Function**  
对于分布在同一个概率空间中的连续性随机变量 $X,Y$, 其联合概率密度函数 $f_{X,Y}$ 满足 :

$$
F_{X,Y}(u_{0},v_{0}) = \int_{-\infty}^{u_{0}}\int_{-\infty}^{v_{0}}f_{X,Y}(u,v) dudv
$$

对于具体区域 $R$ 内，我们有

$$
P\{(X,Y)\in R\} = \int \int_{R}f_{X,Y}(u,v)dudv
$$

Marginal pdfs:

$$
f_{X}(u) = \int_{-\infty}^{\infty}f_{X,Y}(u,v)dv =\int_{-\infty}^{\infty}f_{Y}(v)f_{X|Y}(u|v)du  
$$

$$
f_{Y}(v) = \int_{-\infty}^{\infty}f_{X,Y}(u,v)du = \int_{-\infty}^{\infty}f_{X}(u)f_{Y|X}(v|u)du  
$$

Conditional pdf:

$$
f_{Y|X}(v|u_{0}) = \frac{f_{X,Y}(u_{0},v)}{f_{X}(u_{0})}
$$

- **期望**

$$
E[g(X,Y)] = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}g(u,v)f_{X,Y}(u,v)dudv 
$$

$$
\begin{align}
& E[X] = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}uf_{X,Y}(u,v)dudv  \\
& E[Y] = \int_{-\infty}^{\infty}\int_{-\infty}^{\infty}vf_{X,Y}(u,v)dudv
\end{align}
$$

同时还有

$$
E[aX+bY+c] = aE[X] + bE[Y]+c
$$

$$
E[Y|X=u] = \int_{-\infty}^{\infty}vf_{Y|X}(v|u)dv 
$$

注意 $E[Y|X=u]$ 可以视为关于 $u$ 的函数，则 $E[Y|X]$ 可以视为关于 $X$ 的函数
- **性质**  
![13221c6b53a88f3155acc1551059283.png](https://s2.loli.net/2024/11/19/1aGZdqTXAvrPWO8.png)
- **Uniform Joint pdfs**  
![31f18ceb8e55440261b69c35f9c9b3d.png](https://s2.loli.net/2024/11/19/1VFIcl6BuiJCLsH.png)
