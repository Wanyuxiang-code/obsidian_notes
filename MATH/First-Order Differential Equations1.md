---
title: First-Order Differential Equations1
date: 2025-02-19
date modified: 2025-03-12
categories: Math285
tags: [Math285]
---

#Math285 

## Method of Integrating Factors

![3387257bd8e94e9bc364eff02591b2e.png](https://s2.loli.net/2025/03/12/P96M8yLCw1NQ3vq.png)


**一阶线性微分方程**  
**1. 形式**

$$
\frac{dy}{dt} + p(t)y =g(t)
$$

or

$$
P(t) \frac{dy}{dt} + Q(t)y =G(t)
$$

**2. 求解 ->寻找 integrating Factor**

- Case1: $p(t)$ 为常数 $a$ ，对应的 integrating factor 需满足 $\frac{d\mu}{dt}=a\mu$ ，确定指数函数即可

![00d2fc44717d110cc1c2ce93f7bf11d.png](https://s2.loli.net/2025/02/21/ExuoaSmXj1986WP.png)
- Case2: 一般形式，考虑寻找到满足条件的 integrating factor $\mu(t)$  
![57e47f133a378eb332de2c78b59ddd3.png](https://s2.loli.net/2025/02/21/LsmdyYjEVZRMpkJ.png)  
**Notice**
- 有些函数并非在整个实数集上一直连续，求解对应的解时需要注意定义域范围（由 initial value 确定）
- 有些积分式无法用初等函数求解，注意根据初值选取合适的积分下限化简

## Linear 1st Order Equation

==Slides Version==  
**线性一阶微分方程**

$$
y' = a(t)y + b(t)
$$

当 $b(t)=0$ 时即为齐次

### Homogeneous case

![d5ec11c02e711e62226bd55f56c0ab5.png](https://s2.loli.net/2025/02/25/i4scj2gh5qNS1zQ.png)

**证明考虑直接构造对应函数为常数**

![b73fb13169f7a87114ca258f45a39e0.png](https://s2.loli.net/2025/02/25/ESDMGsnR1fbkgjA.png)

### Inhomogeneous Case

**非齐次的情况考虑在齐次的情况基础上乘上一个函数进行构造**

![5156552d7c96339e7261a01a7dba7fc.png](https://s2.loli.net/2025/02/25/nF59RgdQrG3xpH2.png)


**非齐次解的情况即为考虑齐次解 + 非齐次情况的特解**

> [!question] 如何获取所有解 ->在积分求特解时添加常数（其实等价于用齐次解 + 特解，其中齐次解前有一个待定的常数）

$$
y_{p}(t) = e^{A(t)}(c+\int_{t_{0}}^{t}(b(s)e^{-A(t)})
$$

### Example

**依次找到 associated homogeneous equation solution, particular solution, general solution 即可**

![37b206c10bd36f5e12c0784ce1e95f5.png](https://s2.loli.net/2025/02/25/dIMCwxGWHe2gpQt.png)  
![e14496679e88188e7cf7d5d448718ac.png](https://s2.loli.net/2025/02/25/fYiKUu7P8m513nk.png)  
![86bedac5847e30901f697c5030f8e6a.png](https://s2.loli.net/2025/02/25/ex8qOfQvsm3cuX4.png)

![a49a787c691c79cbc499fe3c1899a14.png](https://s2.loli.net/2025/02/25/uxn2FPhc5oqUmT9.png)


![503c44ee4f135f3404724a5661ec4a2.png](https://s2.loli.net/2025/03/12/dmJOQHiphbXfDZ3.png)

## The Linear Algebra Aspect

我们考虑一组定义在给定定义域 $I$ 上的函数，他们满足线性操作上的封闭性

$$
\begin{align}
& (f+g)(t) = f(t)+ g(t) \\
& (cf)(t) = cf(t)
\end{align}
$$

同时这个抽象的线性空间的零向量即为 all-zero function $I\to \mathbb{R},t\to 0$

**Definition**  
![f48d32e5c4eef5eacc249f3e066330d.png](https://s2.loli.net/2025/03/12/nYvkuASQqxLRC1O.png)

>[!example] Remark
>- $\mathbb{R}^{n}$ 与 $\mathbb{R}^{I}$ 的区别在于 $\mathbb{R}^{I}$ 有无穷维，对应的标准基数量有无穷多
>- 经过类比，我们有 $\mathbb{R}^{I}$ 的标准基可以写为
>
>$$
>\delta_{s}(t) = 1 \text{ if } t = s \text{ else } 0
>$$
>
>- 但是任意基的线性组合并不能构成 spanning set
>- 我们主要关注 $\mathbb{R}^{I}$ 的子空间 $C^{\infty}(I)$ ,其中所有函数均无穷可微

### Cases Analysis

#### 1st Order Homogeneous Case

$y'(t) = a(t)y$ 的解构成 $\mathbb{R}^{I}$ 中的一维线性子空间（每一组解均为特解形式乘常数）
 
![e7a119c95706b870e6a2d9be6e5789b.png](https://s2.loli.net/2025/03/12/eNgtIbnVrJRc3TD.png)

#### 1st Order Inhomogeneous Case

$y'(t) =a(t)y+b(t)$ 构成 $\mathbb{R}^{I}$ 中的一维仿射空间（Line），满足对其的仿射组合的封闭性  
其中任意两元素相减后即回到齐次情况 ->一维的线性子空间

![848e82ec6921fa74c8542f468d6f27b.png](https://s2.loli.net/2025/03/12/hrJfmU7RbWnzsHO.png)

#### 2nd Order Case

$y''+y=0$ 构成 $\mathbb{R}^{\mathbb{R}}$ 二维的线性子空间, 其基为 $\sin,\cos$, 在给定 $y(0),y'(0)$ 的情况下可以对应一个唯一的双射 (IVP)



![9717bc31287cc167fb323c16c5fbaba.png](https://s2.loli.net/2025/03/12/ZrQckWLFDn9VuKT.png)

### Theorem

> [!question] 如何判断一组函数线性独立

$f_{1},f_{2},\dots f_{n}$ 线性独立等价于

$$
\lambda_{1}f_{1} + \lambda_{2}f_{2}+\dots \lambda_{n}f_{n} = 0
$$

没有平凡解

**证明考虑数学归纳法**  
![9099945d87597f8bae5b24a9a37dcb3.png](https://s2.loli.net/2025/03/12/gPU1rsBVAQeEvHD.png)

### Complex First-Order Linear Equations

**Definition**  
一阶复系数线性微分方程具有如下形式：

$$
z'(t) = a(t)z(t)+b(t)
$$

其中 $a,b: D\to C$  
我们将实虚部分离，可以得到

$$
\begin{align}
& z(t) =x(t) + iy(t)  \\
& a(t) = a_{1}(t) + i a_{2}(t) \\
& b(t) = b_{1}(t) + i b_{2}(t)
\end{align}
$$

原式等价为

$$
\begin{align}
& x'(t) = a_{1}(t)x(t) - a_{2}(t)y(t) + b_{1}(t) \\
& y'(t) = a_{2}(t)x(t) a_{2}(t)y(t) + b_{2}(t)
\end{align}
$$

**General Solution**  
![c4a47bc2ccc7e6dc644ed082e0f0bd5.png](https://s2.loli.net/2025/03/12/dpe9BJNTKSZ8H4O.png)

![c1bd7b442630d4ae80af04625abbae6.png](https://s2.loli.net/2025/03/12/CQA1bdKL8aBmNnv.png)

> [!tip] 对于某些实系数 ODE，我们也可以通过引入复数进行解决

**Complexification of real ODE's**  
![a4e4dcfdec7500964e007095b38fd21.png](https://s2.loli.net/2025/03/12/APhCuU5F4EfTIDs.png)  
![24fa75729394a142cdaba09ad43d957.png](https://s2.loli.net/2025/03/12/jEUAzTxpuFcnm4s.png)

### Analogy with Linear Recurring Sequences

**先类比线性递归的多种求解方式**

![95c2e52f78f7fd487e9a6084d65f436.png](https://s2.loli.net/2025/03/12/v2aUQysoDkCbXfN.png)  
![6a50083738f32e5bcee4c7907e8210c.png](https://s2.loli.net/2025/03/12/BEmqjZU2Qgk7D5w.png)

- **类比 1**：先考虑齐次解再加上特解的情况
- **类比 2**：在齐次情况下乘上一个待定的函数

![bcc1f9378b7772736365ef212ff1d80.png](https://s2.loli.net/2025/03/12/H5zahn1WbxGUqgt.png)


