---
title: Counting
date: 2024-11-16
date modified: 2024-11-19
categories: Math213
tags: [Math213]
---

#Math213 

## Counting 

### Basic

**Basic Counting Rules**

- **Product Rule**：计数过程可以分解为一个彼此依赖序列计数过程，前项计数过程中的元素均与后项有关  
![8056cf59d1afa612d4bdaeeb1d0a220.png](https://s2.loli.net/2024/11/16/LohZdNgSO6ICP2i.png)
- **Sum Rule**: 计数过程可以分解为一系列独立的计数过程  
![b4678841d422202963d4b315af7b450.png](https://s2.loli.net/2024/11/16/AhybjeNJZX3zCWv.png)

- **容斥原理**：Principle of Inclusion-Exclusion

$$
|\cup_{i=1}^{n}S_{i}| = \sum_{i}|S_{i}|-\sum_{i<j}|S_{i}\cap S_{j}|+\sum_{i<j<k}|S_{i}\cap S_{j}\cap S_{k}|+\dots+(-1)^{n-1}|S_{1}\cap\dots \cap S_{n}|
$$

- **The Division Rule**

![4051e2d2ad04b1fd70e8129cebb7716.png](https://s2.loli.net/2024/11/16/cpblwdh6kHSY54J.png)

- **抽屉原理**： Pigeonhole Principle  
![5dca018e09e39599ab4fadf88d6a92a.png](https://s2.loli.net/2024/11/16/pEKwZUXCdTzuBqD.png)  
泛化后的抽屉原理：  
![6f37cd2339ab2bd96173906b919361a.png](https://s2.loli.net/2024/11/16/r5TVBIniOLl4KpE.png)

### Permutation and Combination

**Permutation**: 考虑不同对象的有序排列

$$
P(n,r) = n(n-1)\dots(n-r+1) = \frac{n!}{(n-r)!}
$$

**Combination**: 考虑不同对象的选取

$$
C(n,r) = \frac{P(n,r)}{r!} = \frac{n!}{(n-r)!r!}
$$

### Combinatorial Proof

**算两次**  
**Definition**
- 利用计数原理考虑对同一计数事件从不同角度考虑，得出等式的两边
- 利用构造双射证明等式两边相等 (核心为分别证明双射与满射)

![17451c7a75156ed44c19db127293574.png](https://s2.loli.net/2024/11/19/GiqZcz8xeYFW1Vp.png)  
![3221470c840ac1557eea0f7f4492296.png](https://s2.loli.net/2024/11/19/NTxIF7p54KE2Umq.png)

### Identity and Property

**二项式定理**

$$
(x+y)^{n}= \sum_{j=0}^{n}x^{n-j}y^{j} = C_{n}^{0}x^{n} + \dots + C_{n}^{n}y^{n}
$$

推论：

$$
\begin{align}
& \sum_{k=0}^{n}C_{n}^{k} = 2^{n}  \\
& \sum_{k=0}^{n}(-1)^{k}C_{n}^{k} = 0  \\
& \sum_{k=0}^{n}2^{k}C_{n}^{k}=3^{n}
\end{align}
$$

**Pascal's Identity**: 常用于组合数的裂项化简等

$$
C_{n+1}^{k} = C_{n}^{k} + C_{n}^{k-1}
$$

推论：

$$
C_{n+1}^{r+1} = \sum_{j=r}^{n}C_{j}^{r}
$$

**三项式系数：Trinomial Coefficient**

$$
\begin{pmatrix}
n  \\
k_{1} \ k_{2} \ k_{3}
\end{pmatrix} = \frac{n!}{k_{1}!k_{2}!k_{3}!}
$$

其中 $k_{1}+k_{2}+k_{3}=n$
