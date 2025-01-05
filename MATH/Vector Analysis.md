---
title: Vector Analysis
date: 2024-12-08
date modified: 2024-12-17
categories: Math241
tags: [Math241]
---

#Math241 

## Vector Fields and Differential Forms

### Vector Fields

**1. Definition**

>[!tip] Definition  
> A Vector Field is a mapping $F:D\to \mathbb{R}^{n}$ with domain $D \subset \mathbb{R}^{n}$  
> 向量场即为对 n 维空间中的每一个点赋上一个 n 维向量

**2. Example**  
![b6c175cf6332acee8ca70bf60ae0a57.png](https://s2.loli.net/2024/12/10/9Jni1rpFDylaZTX.png)

==注意 Gradient Field 定义，核心即为向量场对应的向量函数可以表示为一个函数的 gradient，在这种情况下，该向量场为保守向量场，其路径积分仅与起点与终点有关==

![c068c4849d13d72e1e9b289c82b3aa1.png](https://s2.loli.net/2024/12/10/TRV2c8I7CXqyKMH.png)

### Differential 1-Form

 回顾 Linear Form

![938a02063df9ec7347d42b158f522a6.png](https://s2.loli.net/2024/12/10/U9M1liJdYfnGEyw.png)

**Linear Form 即为对 n 维向量进行点乘，从 $\mathbb{R}^{n}$ 到 $\mathbb{R}$ 的线性映射**

#### Definition

> [!tip] 对偶空间 $(\mathbb{R}^{n})*$
> 1. 基本定义  
>    给定一个向量空间 $V$,其对偶空间 $V^{*}$ 为 $V$ 上所有线性映射的集合。因此， $V*$ 中的元素为将 $V$ 中的每一个元素映射到实数的一个函数，且满足线性条件
> 2. $\mathbb{R}^{n}$ 的对偶空间  
>    当 $V=\mathbb{R}^{n}$ 时， $\mathbb{R}^{n*}$ 表示的是从 $\mathbb{R}^{n}$ 到 $\mathbb{R}$ 所有线性函数的集合，这些线性函数通常被称为线性泛函。  
>    记 $\mathbb{R}^{n}=\{x=(x_{1},\dots,x_{n})\}$, 那么一个线性泛函可以表示为
>
>    $$
>    \phi(x) = \sum_{i=1}^{n}a_{i}x_{i}
>    $$
>
>    其中 $x \in \mathbb{R}^{n}$

![e401991be482e2d89a53a386ef85ec4.png](https://s2.loli.net/2024/12/10/EkQTOeuIiJgZDql.png)

**Differential 1-Forms 即为对定义域中的每一个向量都找到一个线性泛函，为从定义域到其对偶空间的映射；也可以理解为一个向量场,对定义域中的每一个元素都有一个对应的向量进行映射**

![ab8d5a4b2b58a1d02428570a70880ac.png](https://s2.loli.net/2024/12/10/l7QDg2HwZfEyFju.png)

#### Standard Representation

![a710c3b8ecea5d51bce6bd45aed4a35.png](https://s2.loli.net/2024/12/10/9S6vbaBIkoAhmtn.png)

#### Complex Differential 1-Forms

![61355cbd376a8225eb066d1b072387a.png](https://s2.loli.net/2024/12/10/Obl7uL8nAzQ23wI.png)


![5ebf02520198ddf7da256503abb6907.png](https://s2.loli.net/2024/12/10/Wa6dvmc5gHi4ZN3.png)

## Line Integrals

**Motivation**  
研究 Line Integral 的 Motivation 来源于物理中希望沿某一条确定的路径在空间中积分得到做功

**Tagged Partition**  
即为带标记的划分，常用在进行黎曼积分类似的分段积分中，用于标记区间中的元素  
![69db61228365c304d4bc9b4d1062e46.png](https://s2.loli.net/2024/12/10/WAaND3OBnp1mseP.png)

### Definition  

![b92983c98ef75fd0093384ce2e1c0ff.png](https://s2.loli.net/2024/12/10/cQC62RbvgMO48ue.png)

### Properties of Line Integrals

- Some Terminology  
![62ce9bfe8bbaf0179369c4a27391edb.png](https://s2.loli.net/2024/12/12/qvBV3NrcZYOG57m.png)

- **将曲线轨迹参数化后积分**  
**Theorem**  
![27172342bb491b294ddd7cdccc4bcf8.png](https://s2.loli.net/2024/12/12/rY7XTo8jcHvI1pZ.png)


- **线性: Linearity**  
![468847361f11170531c382c137ddcbe.png](https://s2.loli.net/2024/12/12/Kkv3fix6Rg5mH4h.png)

- **Composition of Paths(将路径不同段相加)**  
![a48d79783eeb814217c052ab27c38d5.png](https://s2.loli.net/2024/12/12/CP2mE7vATQjKSG3.png)

- **重新参数化**  
![89569f93b2465f26a7051f1323904d8.png](https://s2.loli.net/2024/12/16/ngl2JVy57pLDO8I.png)  
注意从不同的方向对 Line Integral 在一条给定的曲线上积分的得到结果可能正负相反（例如交换起点与终点）

#### Example

- **Winding Curve**  
==考虑利用 Normalized Curve 绕原点的圈数考虑 Line Integral 的值==  
![2b685edc423f03c39b978906566760b.png](https://s2.loli.net/2024/12/16/s1J9PeG7amytBfl.png)  
为了计算绕行的重数，我们引入**Winding Number(绕数)**  
![7a073264165f29b59952491de63dac6.png](https://s2.loli.net/2024/12/16/xZrPcWIpBhAYkig.png)  
![5994e7461290bd3a5b6788899cb6278.png](https://s2.loli.net/2024/12/16/Ov7qAkfVRjrLKMG.png)

## Fundamental Theorem for Line Integrals

==Gradient Field(Conservative Field) 的性质==

> [!tip] Exact Differential 1-Form（全微分 1- 形式）  
> **1. 定义**  
> 对于一个 Differential 1-form $\omega:D\to (R^{n})^{*}$, 当存在一个函数 $f:D\to \mathbb{R}^{n}$ 满足 $\omega=df$ 或表述为其对应的 Vector Field 为 Gradient Field, 那么我们称改 Differential 1-Form 为 exact(全微分)  
> **2. 必要形式（闭形式）**  
> 在给定区域内，如果 $\omega$ 为全微分，则其外微分 (exterior derivative) 必须为零：
>
> $$
> d\omega=0
> $$
>
> **3. 充分条件 Poincare's Lemma(庞加莱引理)**  
> 如果区域 $U$ 是单连通 (simply connected),并且 $d\omega=0$, 则 $\omega$ 为全微分形式  
> **4. 性质**
> - 保守性：沿任意路径的线积分只取决于路径的起点与终点
>
>   $$
>   \int_{C}F \cdot dr=f(B)-f(A)
>   $$
>
>  - 路径无关性：如果向量场为全微分的，那么在场内的路径积分是路径无关的 (Path-Independent)->这意味着闭合路径的积分为零
>  - 零旋度 (Curl-Free Property)
>
>    $$
>    \nabla \times F=0
>    $$

![7489c432351380678812b7d55ef5268.png](https://s2.loli.net/2024/12/12/Hhv6FyERncT8iDQ.png)  
**Proof**: 通过其 Gradient Field 的性质，参数后以后将其转化为单元函数 ->利用微积分基本定理

### Corollary

![ae84fc95b31c2f8aabb538373d851a4.png](https://s2.loli.net/2024/12/12/3HcT4so2SqaUQWi.png)

### Converse of the Corollary

==Independence of path implies exactness==

**Oberservations**  
![480d215019e42ef91e3ba9e05720b70.png](https://s2.loli.net/2024/12/12/M7lDSwo5b92COy6.png)  
==Connected Subsets（连通子集）->该子集不能够被划分为非空的不交开集==


**Theorem**  
![67b70855b8a121cd06db4468224cc68.png](https://s2.loli.net/2024/12/12/SFcCsi2lVZ1Uqhk.png)  
**对于定义在连通开集上的连续微分 1 形式，它为全微分当且仅当其积分与路径无关**

**Example->通过 $\omega$ 的形式通过积分找到其反函数**  
![07916de94b0f9ff1c168e1344ed83bb.png](https://s2.loli.net/2024/12/16/enib67p2ZTuyIBa.png)

## Locally Exact 1-Forms

**Definition**  
![a49b6d3f09f567198bcca5004756ba0.png](https://s2.loli.net/2024/12/16/9oEjBbLh6pswRF1.png)

**Locally Exact->考虑 $\omega$ 在对应的邻域范围内为全微分形式**

**Proposition: Locally Exact 的必要条件 ->考虑 Clairaut's Theorem**

==关注函数对应的偏导是否相等==

![c7e515af23b0e5705503a09044689ce.png](https://s2.loli.net/2024/12/16/ECAyM8cdwmNOTYz.png)

**简单的例子**  
![4e585f8bb3498052f65e6c886c69068.png](https://s2.loli.net/2024/12/16/OYZF1CTIKyvQXzN.png)

### Curl and Divergence

散度 (Divergence) 与旋度 (Curl)

**Definition**  
![5a0e8ddb995d17158f69ec3ec794d7c.png](https://s2.loli.net/2024/12/16/Ro2OstGFCdlTUP6.png)  
简单的记忆方式:
- 旋度理解为：向量场与 Gradient 算子的叉乘，旋度仍然为三维的向量场
- 散度理解为：向量场与 Gradient 算子的点乘，散度则为实值函数

![f8123df6de1abbac76b91eb1d0dc689.png](https://s2.loli.net/2024/12/16/sdwLoAtx6QcONVD.png)  
![bf3fa6044478254512d14a4e6627207.png](https://s2.loli.net/2024/12/16/ILQ3iYzqsu7AVkC.png)

**散度与旋度的性质**

![6012e086638f0596c6a38f88413c409.png](https://s2.loli.net/2024/12/16/tLpXgC8914fo2Bh.png)

### Poincare's Lemma

#### Topology Related Concept

![e7bad69a6451267d7522089cfe651fd.png](https://s2.loli.net/2024/12/16/IUCGn2JitfhVWSz.png)

> [!tip] Topology Terms  
> **1. 凸集**  
> 一个集合被称为凸集如果对于集合中的任意两个点 $x,y\in S$, 连接着两个点的线段全位于该集合中。这意味着:
>
> $$
> \lambda x+(1-\lambda)y \in S,\lambda \in[0.1]
> $$
>
> **2. Star-Shaped Set（星形集）**  
> 一个集合被称为星形集，如果存在一个点 $x_{0}\in S$,使得从该点到集合中任意点 $y\in S$ 的线段都位于该集合中  
> 从几何直观上，星形集允许局部的凹陷，但必须存在一个“星心”(也可以有多个)  
> **3. Simply Connected Set**  
> 一个集合是单连通的，如果对于任何闭合曲线都可以连续收缩成一个点而不离开集合  
> **4. Not-Simply Connected Set（非单连通集）**  
> 一个集合是非单连通的，如果至少存在一个“洞”，使得一些闭合曲线无法在该集合内连续收缩成一个点 

![4b85095d5c9910e41cad728e52a3449.png](https://s2.loli.net/2024/12/16/OuAUhr5j6EKmvId.png)

#### Theorem

![e33ff0665e1e2e644179aad30d10a15.png](https://s2.loli.net/2024/12/16/Kq4FMilbk6QjzJG.png)  
![f44ad02822e500ffbea763d41aea80c.png](https://s2.loli.net/2024/12/16/EUYA3WeIV9Jui6F.png)

**证明**  
![18e63aa2cebca1f20fb52a42a9e0580.png](https://s2.loli.net/2024/12/16/fX9PBv6Le1KTGyl.png)

**将 Star-Shaped Region 推广的 Simply Connected Region**

==对于 Locally Exact Continuous Differetial 1-Form,如果两路径同伦，则其 Line Integral 相等==

![84d33cb8348e1613300b45e0c578c7f.png](https://s2.loli.net/2024/12/16/xQuNE8pb9MgzhrI.png)

#### Example

![91a90891dd41ed8b32d23ff6523c2a0.png](https://s2.loli.net/2024/12/16/mNWScyrZRpY4sVO.png)

![1c41ee408b0b03d950ad4f2aaf0ecea.png](https://s2.loli.net/2024/12/16/1DPdBbrh8zYAoER.png)

**注意由于我们在 Star-Shaped Region 内对 x 轴负半轴上的点上进行积分得出的结果不同 ->该函数的 anti-derivative 不能扩展到整个二维平面内**


![acaed3a39acf58312f78c928ff5f6ba.png](https://s2.loli.net/2024/12/16/mGRA6JBXFdwcPeg.png)
