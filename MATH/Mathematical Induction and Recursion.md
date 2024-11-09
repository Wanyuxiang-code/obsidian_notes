---
title: Mathematical Induction and Recursion
date: 2024-11-01
date modified: 2024-11-09
categories: unlabeled
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
- 线性递归：

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
