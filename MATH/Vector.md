---
title: Vector
date: 2024-09-14
date modified: 2024-11-09
categories: Math241
tags:
  - Math241
---

#Math241 

## Length and Cross Product

### Definition and Property

![933c205ce76903edb7031a0083cac02.png](https://s2.loli.net/2024/09/14/eT4JC7WjmhgMcDo.png)
- Bilinear Form(Symmetric)
- Positive Definite
- Associative Law
- Distributive Law

### Orthogonality 正交

![5f47e1307c6ac2d40092f1600725014.png](https://s2.loli.net/2024/09/14/UGzDPWSO2byLlNg.png)

### Length

![7605b5fc09ed1d3d1c927be532bc4b1.png](https://s2.loli.net/2024/09/14/zvVs7Xk1dnJ5BoP.png)

#### Cauchy-Schwarz Inequality

- 向量形式

$$
a,b \in \mathbb{R}^{n}, |a \cdot b| \leq|a||b|
$$

- 展开式

$$
(a_{1}b_{1}+\dots a_{n}b_{n})^{2} \leq (a_{1}^{2}+\dots+a^{2}_{n})(b_{1}^{2}+\dots+b_{n}^{2})
$$

- 导出三角不等式

$$
d(a,b) \leq d(a,c) + d(c,b)
$$

- 复数形式  
![d66817192dfb466d55966f57482cda2.png](https://s2.loli.net/2024/09/14/zBRIwrhgMu7pFVt.png)
- 证明：
  1. 判别式法：引入一个二次函数即可
  2. 直接利用 Lagrange 恒等式即可  
![91fbc5b2d3536ebceb1444789d10785.png](https://s2.loli.net/2024/09/14/9vud1UZjyHDnmft.png)

$$
|a|^{2}|b|^{2}-(a \cdot b)^{2}=|a\times b|^{2}
$$

### Determinant

#### Permutation

![cca3008c1af99799d11860e36ee0e9d.png](https://s2.loli.net/2024/09/19/mkoFnO7AJaI3Sez.png)

#### Property

详见线代  
![7f9595055db2bad5bfca05bee993fd8.png](https://s2.loli.net/2024/09/19/4ZMTEhlLR9e6boz.png)

**Geometric Property**  
![59974c8e5e91789b202d1ce7957572c.png](https://s2.loli.net/2024/09/19/3b4rCqF7JTxKVmE.png)

### Cross Product

在空间 $\mathbb{R}^{n}$ 中，我们可以定义 n-1 个向量的叉乘，这些向量叉乘的结果为一个垂直于这 (n-1) 个向量的向量  
三维向量的叉乘：  
![9dfdca191600269586eac86a294d51d.png](https://s2.loli.net/2024/09/14/9CJpZWt2AefqOML.png)

#### Property

![bc3c3dcfe1bfabf7b2ebbdea32f2cfe.png](https://s2.loli.net/2024/09/14/sBkAyQuWJcYiNHf.png)  
![b2df7e4ecafd7c9f2e4d0f9d734fa1a.png](https://s2.loli.net/2024/09/14/Fp4zEVuhmfHsjgr.png)  
![fc10431f950b2bfaee0726496b5766c.png](https://s2.loli.net/2024/09/14/7C8KLXsMphdkWOf.png)  
**特别注意性质 5、6**
- 5 可以利用混合积的计算意义 ->体积理解 $\det(a,b,c)=(a\times b)\cdot c$
- 6 考虑记住 triple cross product

#### Triple Product

$$
a \cdot (b \times c) = \begin{vmatrix}
a_{1} \ a_{2} \ a_{3}  \\
b_{1} \ b_{2} \ b_{3}  \\
c_{1} \ c_{2} \ c_{3} 
\end{vmatrix}
$$

**几何意义：由向量 a,b,c 扩展出的平行六面体的体积,为三边向量张出的四面体的六倍**  
$V =|a \cdot (b \times c)|$  
推论: 当 V=0 时，说明向量 a,b,c 共面（行列式为 0，线性相关）  
**Vector Triple Product**:  
$a \times (b \times c)$

平行六面体：parallelepiped  
棱锥体：pyramid($\frac{1}{6}$ 的混合积)

## 常用计算

### 基本转换

- Line:

$$
\begin{align}
& a +\mathbb{R}b \iff \begin{bmatrix}
x_{0} \\
y_{0} \\
z_{0} \\
\end{bmatrix} + t\begin{bmatrix}
a \\
b \\
c \\
\end{bmatrix} \text{ 点加方向向量} \\
& \frac{x-x_{0}}{a}=\frac{y-y_{0}}{b}=\frac{z-z_{0}}{c} \text{ symmetric form}
\end{align}
$$

由两个平面求交线得到：
1. 直接求对应线性方程组的通解
2. 考虑对两平面法向量做叉乘也可

- Plane:  
方程形式

$$
a(x-x_{0})+b(y-y_{0})+c(z-z_{0})=0
$$

其中：

$$
\begin{align}
&\begin{bmatrix}
a \\
b \\
c \\
\end{bmatrix} \text{即为平面的法向量}  \\
& \begin{bmatrix}
x_{0} \\
y_{0} \\
z_{0}
\end{bmatrix} \text{即为平面偏离原点的距离} \\
\end{align}
$$

参数形式：

$$
\begin{align}
a+\mathbb{R}b+\mathbb{R}c \text{点+两个方向向量}
\end{align}
$$

向量形式：

$$
n \cdot r = n \cdot r_{0}
$$

### 具体计算

- 点与直线的距离  
确定点与直线上一点的向量，然后考虑其向直线的方向向量做投影

$$
d(P,l)=\vec{b}-\frac{\vec{b}\cdot \vec{a}}{|a|^{2}}\vec{a}
$$

- 点与平面的距离  
确定点与平面上一点，考虑对平面的法向量做叉乘  
在 $\mathbb{R}^{3}$ 中，我们有以下结果:  
![a76693f8b35df4acaccc18df01779ce.png](https://s2.loli.net/2024/09/18/TevmDWLjVsGqFRX.png)

- 直线与直线之间的距离  
**注意一面直线既不平行也不相交**  
表示形式:

$$
l_{1}: a_{1}+\mathbb{R}b_{1} \text{ , } l_{2}:a_{2}+\mathbb{R}b_{2}
$$

考虑直线之间的距离即为考虑直线对应向量的最小值,即可转化为求点到平面的距离：

$$
d(l_{1},l_{2})=min(a_{1}-a_{2}-(\lambda_{1}b_{1}+\lambda_{2}b_{2}))
$$

- 平面与平面之间的距离  
转化为平面与点之间的距离或  
![011233d8fe9cce43eebfc38f89202fe.png](https://s2.loli.net/2024/09/18/21DVLwMrJXybIZo.png)


