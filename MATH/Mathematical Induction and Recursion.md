---
title: Mathematical Induction and Recursion
date: 2024-11-01
date modified: 2024-11-20
categories: Math213
tags: [Math213]
---

#Math213 

## Mathematical Induction

![73e7bc415cd73f4b20dc8558050f2fb.png](https://s2.loli.net/2024/11/01/kQ63Vno4d2TNBSU.png)  
![11f1c642da709d3e6e049d8b49e13c1.png](https://s2.loli.net/2024/11/01/dzAFpWyP5LNCEYi.png)  
**注意**：
- 归纳奠基（选择最小满足命题的正整数）
- 假设，并利用前向假设证明后项命题

## Recursion

### Towers of Hanoi Problem 汉诺塔

- **Description**  
![55c08305814ed59f4ab22bfd44425ce.png](https://s2.loli.net/2024/11/06/KuRazkEiJl2DjH4.png)
- **Algorithm**  
![8096ed1687ec4d5c855e995a6108152.png](https://s2.loli.net/2024/11/06/HmrV8JfQcUdy72S.png)  
**注意汉诺塔核心即为考虑到最后的情况必有 n-1 plate 在第二块，1 一个最大的 plate 在第一堆，这样即可将问题化归为 n-1 的情况，调用递归函数**

- **Idea**  
**递归的数学核心可视为反向数学归纳法，当我们确定了递归最终可以结束（即确定归纳法的奠基），再寻找到将问题递归的方式，即可形成完整的递归链条**  
![ed9f40028a5155d90f9fc645cb13877.png](https://s2.loli.net/2024/11/06/JW1FXwmxHQoYpSl.png)
- **Running Time**: 利用操作次数表示

$$
\begin{align}
& M(n)\text{ denotes the number of disk moves needed for n disks} \\
& M(1) = 1 \\
& M(n+1) = 2M(n)+1 \\

\end{align}
$$

### Recurrence

- **递归函数或方程定义**  
![74ff750aaa76154e106353b257f49db.png](https://s2.loli.net/2024/11/06/9GvHiaNkup8W7fD.png)
- **核心**  
Basic Step（初始情况）  
Recursive Step（递归过程）

### Linear Recurrences

**相关概念**
- **线性递归**：

$$
a_{n} = f(a_{n-1},\dots ,a_{n-k}) = s_{1}a_{n-1}+\dots+s_{k}a_{n-k}+f(n) \text{ 其中对应的s与f(n)均为实数}
$$

- 线性齐次递归 (Linear Homogeneous Relation)：  
在线性递归的基础上要求递归表达式中无多余的常数，即 $f(n)=0$
- 线性递归的阶数或度数 (order/degree)  
当前项与最远项之间的差距

**一阶线性递归**
- **定义**

$$
T(n) = f(n)T(n-1)+g(n)
$$

**First Order**: 递归表达式只出现前一阶情况  
**Linear**: 出现的递归式均为一次

![d3269386e6b24206d4ccee917503feb.png](https://s2.loli.net/2024/11/08/qrv6O84jXbsaHtu.png)  
**Theorem**

$$
\sum_{i=1}^{n}ix_{i}^{i} = \frac{nx^{n+2}-(n+1)x^{n+1}+x}{(1-x)^{2}}
$$

**齐次线性递归特征根方程**

n 阶齐次线性递推数列（简称线性递推数列）是指形如：

$$
a_{n}=c_{1}a_{n-1}+c_{2}a_{n-2}+⋯+c_{n-1}a_{n}+c_{n}a_{0} ​
$$

的数列，其中 $c_{1},c_{2},\dots,c_{n}$ ​为常数系数，且是齐次的，即右边没有常数项。  
**特征根方程的求解**
- 将递推数列的系数代入特征方程，得到一个关于 r 的多项式。
- 求解该多项式，得到所有的特征根 $r_{1},\dots ,r_{n}$  
- 结合 n 个初始项得到最终表示（如果初始项不足可能会有非唯一解）  
 **特征根的情况及其对应解法**
- **不同的特征根**（重根的次数为 1）：若特征方程有 n 个不同的根 $r_{1},\dots,r_{n}$ ​，则通解为：

$$
a_{n} = A_{1}r_{1}^{n} + A_{2}r_{2}^{n}+\dots A_{n}r_{n}^{n}
$$

- **有重根的情况**：若特征方程有某个重根 r，重根的情况需要考虑不同阶数的 $r^{n}$ 乘以多项式。若重根 r 的重数为 k，则通解的一部分是：

$$
(A_{1}+A_{2}n+\dots A_{k}n^{k-1})r^{n}
$$

**线性非齐次递归**  
形如:

$$
a_{n} = \sum_{i=1}^{k}c_{i}a_{n-i} + F(n)
$$

解决思路: 考虑先关注与之相关的齐次线性递归方程

### Growth Rate of Solutions to Recurrences

#### DIvide and conquer algorithms

**Problem Form**  
![124672e37e2709232322d1df14681d4.png](https://s2.loli.net/2024/11/16/jMN82EKiTzZl1Cx.png)

**Binary Search**  
![f40fbf5fe1e1e50a112b8861a73814b.png](https://s2.loli.net/2024/11/16/e4IZgy9hzkQO7SD.png)  
![8eb864339694cb7c1d7ae74805c002f.png](https://s2.loli.net/2024/11/16/C69FxEoDQKH7ruc.png)

#### Growth Rate Type

**Theorem**  
![000b36fd5e267a8fdf3bdf6ba431160.png](https://s2.loli.net/2024/11/16/xqUAc49FR7Kmiet.png)

$$
T(n) = a^{\log_{2}n}T(1)+n\sum_{i=0}^{\log_{2}n-1}\left( \frac{a}{2} \right)^{i}
$$

$$
n\sum_{i=0}^{\log_{2}n-1}\left( \frac{a}{2} \right)^{i} = \frac{n\left(  1-\left( \frac{a}{2} \right)^{\log_{2}n} \right)}{1-\frac{a}{2}}
$$
