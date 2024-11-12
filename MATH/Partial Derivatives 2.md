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

**注意记号**：
$$
D_{j} = \frac{\partial}{\partial x_{j}}
$$
从函数到函数的映射

### Clairaut's Theorem

![8120188a619bbee70ab2ab66d71233d.png](https://s2.loli.net/2024/11/07/yeo9aOHWrGXvxbp.png)

关注简单的应用，记为
**对于高阶偏导，可以置换具体求偏导的过程变量，仍不改变最终结果**

**证明**：
**构建一个二阶差分，然后利用Mean Value Theorem进行化简，从两个顺序分别看求偏导的结果**

![2ee8ca604aa6f0c87e4fabc8ff16048.png](https://s2.loli.net/2024/11/11/EcHDvmj6WuqfUl2.png)


### Partial Differential Equations(PDE)
#### Laplace's Equation
![aeeabd11cd072d0b480f2cd05fc57e3.png](https://s2.loli.net/2024/11/11/1PJq3FrgiwbKvu7.png)

$\Delta$ 为Laplace算子

- **二维Laplace方程的解**：可以对特解采取线性组合
![985ad1d35f18aaa35e0f1b8ff3e7d3a.png](https://s2.loli.net/2024/11/11/hdAWtwbLxoym87V.png)

注意Harmonic Function的定义

- **具体的求解过程**

![e1d101b5be33a249f74d5553c891bec.png](https://s2.loli.net/2024/11/11/AT2CuoHPawZtzfY.png)
对于特殊情况，想考虑将最终映射可以分解为两个独立于 $x$ ,$y$ 函数的映射，然后独立求解

- **建立与复指数的联系**
![9b672c4938a305c4068685579ab16ed.png](https://s2.loli.net/2024/11/11/2ZwIWm6ec5phX1D.png)

**Complex Differentiable<->Holomorphic**


Example:利用复数确定什么样的多项式函数为Harmonic
![6598d4e4aeefab9067a67af0933a993.png](https://s2.loli.net/2024/11/12/MdYTqIiuF3mwBvC.png)

#### Wave Equation
![d0908c1a19437bfb39704374677f98b.png](https://s2.loli.net/2024/11/12/kbyxSMp7nCiAraK.png)


## Optimization
### Overview
**Types of Problems**
![aa12d207b1ed7a5c2ff2eeed4e5df63.png](https://s2.loli.net/2024/11/12/naZvfVE9bLw5S8j.png)

**Terminology**
- Optimization Problem:对于给定的实值函数，在定义域的确定子集 $S$ 上寻找其最值
- Feasible Solution: 对于任意属于可行域 $S$ 的元素 $x$, $S$ 为可行域(feasible region), $x$ 为 feasible solution
- Optimal Solution: 取最值时对应的元素
- Extremum: 最大值或最小值
- Local Extremum: 在可行域与其邻域交集中能够取最值的元素x
- Objective Function: 目标函数，待最优化的对象
- Constraints: 确定可行域的限制条件
- Constrained optimization: $S \subseteq D$  Unconstrained OptimizationL $S = D$
- Greedy Method:贪心算法，每一步都选取局部最优解->对于优化问题每一步都考虑梯度方向

### The Unconstrained Case

![a6cb18f2e28ec5ddb52c04de56b4e8a.png](https://s2.loli.net/2024/11/12/FWByNDMolXnqbje.png)
- 对于局部极值，如果函数在该点存在偏导，则其梯度为0
- **注意：critical point的梯度为0，但并不意味着cirtical point即对应局部极值，注意经过此点对contour进行parametrization非正交**

#### Quadratic Approxiamtion for Multivariable Functions
![9c9084b825d17977b78ff97c96068bc.png](https://s2.loli.net/2024/11/12/usipl1YDeAwbjSH.png)
- 利用一阶微分，及其对应的Jacobi Matrix或者Gradient对函数进行线性近似
- 利用二阶微分，考虑对函数进行二次近似（类比Talyor)

![0f3382581e3c49a9ce6b8535249b9ff.png](https://s2.loli.net/2024/11/12/4iIt1KTxsbOVzyG.png)


**推论：利用正定情况与否确定critical point是否能对应局部极值**

![a74dd6470f9c8cfb133429230c064cc.png](https://s2.loli.net/2024/11/12/DAZ9Vr54S32UBHM.png)
