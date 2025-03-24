---
title: "Introduction to ODE's"
date: 2025-02-18
date modified: 2025-02-21
categories: Math285
tags: [Math285]
---

#Math285

## Introduciton

### Basic Terminology

> [!tip] 基本概念  
> **1. ODE 常微分方程**  
> n 阶常微分方程形如
>
> $$
> F(t,y,y',\dots,y^{n})=0
> $$
>
> 其中 F 的定义域 $D\subset \mathbb{R}\times \mathbb{R}^{m}\times\dots \times \mathbb{R}^{m}$, n 阶即微分出现的最高次数为 n.  
> n 阶常微分方程的解为函数 $f:I\to \mathbb{R}^{m}$, f 定义在 $I \subset \mathbb{R}$,且 n 解可微，满足 $F(t,f(t),f'(t),\dots,f^{(n)}(t))=0$  
> **2. IVP 初值问题**  
> 给定微分方程后，我们可以在给定初始条件 (initial condition) 的情况下可以进一步确定微分方程在该情况下对应的解  
> **3. Explicit Form and Implicit Form**  
> 对于 n 阶常微分方程，  
> Explicit Form:
>
> $$
> y^{(n)} = G(t,y,y',\dots,y^{(n-1)})
> $$
>
> 对应的 Implicit Form:
>
> $$
> F(t,y,\dots,y^{(n)})=y^{(n)}-G(t,y,\dots,y^{(n-1)})
> $$
>
> **4. Maximal Solution**  
> 在给定初始条件下，能够存在并且定义在最大可能的区间上的解

#### Ordinary Differential Equation(ODE)

![29ac4cfa05aa117a5613988b61eeb8b.png](https://s2.loli.net/2025/02/18/PloGZ5tT3Qu2wjx.png)

#### Initial Value Problem(IVP)

![8cec95e7c91b46919de2956974ef485.png](https://s2.loli.net/2025/02/18/ablSTNpnmcAB4eJ.png)  
![c9c1cd76b54c804d79a3a98d8581482.png](https://s2.loli.net/2025/02/18/dz1koHL8nyu35lV.png)

### Classification

**1. ODE 与 PDE（常微分方程与偏微分方程）**

- 常微分方程（ODE, Ordinary Differential Equation）  
**定义**：常微分方程是指未知函数依赖于一个自变量，并且方程中包含该函数及其导数。常微分方程中的未知函数只与一个自变量（通常是时间）有关。

- 偏微分方程（PDE, Partial Differential Equation）

**定义**：偏微分方程是包含未知函数及其**偏导数**的方程，且未知函数依赖于两个或多个自变量。它描述的是多维度空间中的变化关系。


**2. Systems of Differential Equations**

**定义**：系统的微分方程是指多个未知函数及其导数组成的微分方程组。这些方程系统的解通常需要一起求解。系统中的每个方程描述一个或多个变量随时间（或其他自变量）的变化关系。

**3. 微分方程的阶数（Order）**  
**定义**：微分方程的阶数是指方程中最高阶导数的阶数。阶数反映了方程描述的是系统的动态过程的复杂程度。

**4. 线性与非线性微分方程（Linear and Nonlinear）**

- 线性微分方程（Linear Differential Equations）  
**定义**：线性微分方程是指方程中的未知函数及其导数以 **线性** 方式出现，即它们的指数是 1，不涉及乘积、平方或其他非线性项。  
**形式**：线性常微分方程的一般形式为：

$$
a_{0}(t)y^{(n)}+a_{1}(t)y^{(n-1)}+\dots+a_{n}(t)y=g(t)
$$

- 非线性微分方程（Nonlinear Differential Equations）

**定义**：非线性微分方程是指方程中未知函数及其导数的关系是非线性的，即方程包含未知函数及其导数的乘积、平方或其他非线性项。

### Ten Examples & Solutions

![8759b7b8b4c5d14afb6e915b0e49ab6.png](https://s2.loli.net/2025/02/19/hes3N9Af8g5kC1U.png)  
![aa3a0aa23973f971728bd5559751010.png](https://s2.loli.net/2025/02/19/uzCkhJgwj6iH8tf.png)

1.因变量 y 与自变量 t 已经充分解耦，直接积分即可得到  
![3dca073d824ac308fdf2eab1fef1aae.png](https://s2.loli.net/2025/02/19/SONymPbWhuDZwCk.png)

2.先猜出答案为指数形式，然后用对应函数形式为常数证明所有解  
![7ea1e4e3f3a26ffbbff619ab82919ef.png](https://s2.loli.net/2025/02/19/m784cFZseJ9gktE.png)  
3.4.5. 均为形如指数函数的形式，同时可以转化为线性齐次的形式  
![4e22d5bd95dc948410c7d05e507f773.png](https://s2.loli.net/2025/02/19/sFMpAmayk8jXbzE.png)

![a416a108154a6faf01628ca9cf00d8e.png](https://s2.loli.net/2025/02/19/ThCZ3SRvA4iJUbE.png)

6.注意 autonomous ODE 自洽常微分方程 ->可以通过平移获得多组解

$$
y' = G(y)
$$ 

G 不取决于 t->可以进行平移  
![03d7c5af5bd02e4b38a51f09da4359b.png](https://s2.loli.net/2025/02/19/G3bwyx6O8spcS4T.png)  
![e1d4296f4d20f0bff1aa027e0a524a6.png](https://s2.loli.net/2025/02/19/8PjimFz3Uw1rNIv.png)

![f97bd0f6620d7d8d75c096bcacbd316.png](https://s2.loli.net/2025/02/19/C3mpRIHArWMd9lD.png)  7.  可以直接将因变量与自变量分离，同时利用平移性  
![e26e2bd9403f3e8ef246c42308643fe.png](https://s2.loli.net/2025/02/19/JQXRsSBA2OK6dIH.png)8.  特殊形式的 ODE **Exact Form** $f_{x}dx +f_{y}dy = 0$ （利用庞加莱引理验证）  
考虑联系 241 中的 Exact Form 以及 Vector Field,将 x,y 参数化  
**注意无解的情况 ->critical point**  
![8028cb4b020ebb58b144685f67d434f.png](https://s2.loli.net/2025/02/21/ckfLO6haYJSepCU.png)  
![db6c55b627d26ef63ae34f382323f42.png](https://s2.loli.net/2025/02/21/AREZFNyqxgWtvb3.png)  
9.$y'=-\frac{x}{y}$
- 直接考虑分离 x,y 积分即可
- 参数后注意到该形式也为 exact,可以直接找到 antiderivative 的 contour  
![ba4c3c016343f80e385eb4b4764cb56.png](https://s2.loli.net/2025/02/21/8dgntaT1lNSXUv9.png)

10.$y''+y=0$  
解决思路：
- 先考虑 $\sin,\cos$ 的特解情况，同时利用特殊值注意到对任意一个 IVP 都有唯一解
- 构造常函数 $(y^{2}+y'^{2})$ ，同时利用线性对特解差分，将得到的差分解的形式对应项代入证明所有解的情况

![e0e5dbb0f15249f6d0d7477a78aac0f.png](https://s2.loli.net/2025/02/21/npI4ocwebyiSQd1.png)  
![0467518189872e840cfa6c642317bbd.png](https://s2.loli.net/2025/02/21/7h5LNxnJrTqKQCB.png)

## Modeling with Initial Value Problems

### Falling Objects

![29dfebfcc477a684a2b95f6f9880772.png](https://s2.loli.net/2025/02/21/dBGJDjx5ma1MpLQ.png)

### Oscillating pendulum

![d89c00c720f63dfde3e4a39f5373fe8.png](https://s2.loli.net/2025/02/21/Tj6gvBJwVI4K8bA.png)

### Predator-Prey Models

![16484989fb4b7544335b05863a29fe0.png](https://s2.loli.net/2025/02/21/2KSlJ6nudt7LoEx.png)

### Heat Conduction

![edf37f48b1d61f2475aec3fbc755815.png](https://s2.loli.net/2025/02/21/mIGwE7vF8g9sQBX.png)

### Vibrating String

![726bb238e1e392459217be000d997e7.png](https://s2.loli.net/2025/02/21/LhAeKvmBViEzJXM.png)
