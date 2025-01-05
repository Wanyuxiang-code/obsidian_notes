---
title: MATH 241 Collection
date: 2024-11-09
date modified: 2025-01-03
categories: MATH汇总
tags: []
---

## 汇总表格

```dataview
table date
from #Math241 
sort date
```

## 集萃

- [[Coordinate System#Equational and Parametric Representation]]
- [[Coordinate System#Cylinders and Quadratic Surfaces]]
- [[Vector#Cross Product]]
- [[Vector Function#Basic Term]]
- [[Vector Function#Curvature 曲率]]
- [[Applications to Physics#Velocity, Speed and Acceleration]]
- [[Applications to Physics#Tangential and Normal Components of Acceleration]]
- [[Functions of Several Variables#Limit Computations]]
- [[Partial Derivatives 1#Further Concept]]
- [[Partial Derivatives 2#Theorem]]
- [[Partial Derivatives 2#Application-Error Propagation]]
- [[Partial Derivatives 2#Implicit Differentiation]]
- [[Partial Derivatives 2#Higher Derivatives]]

## Exam

### Mid3

考点汇总：
- 简单的重积分计算面积
- 简单的重积分计算体积（注意区域限制，如何将问题描述准确地转化为重积分，换元积分时注意雅可比矩阵的行列式勿遗漏）
- 计算 center of mass 相关的物理量
- 重积分技巧:  
费曼积分法  
无穷级数展开  
换元积分
- Parameter Integral  
将微分号移至积分号中  
适时使用洛必达
- critical point  
偏导均为 0，同时注意检验解出来的 critical point 是否满足函数条件，也不要轻易约去 0 的情况  
判断 critical point 的 extrema 情况 ->关注海塞矩阵的正定性
- 计算 Tangent Plane(多熟悉三维情况的计算)
- 隐函数确定偏导（注意记录一下结论和具体推导即可）
- 利用 Mean Value Theorem 证明某些函数可导
- 二次型简单总结

### Final

- 判断 Surface 是否 smooth
- 判断是否存在 global extrema(关注连续函数在紧集上一定能取到特值)
- 注意特征函数要定义在整个空间中，狄利克雷函数由于定义在 $[0,1]$ 上所以不是特征函数

Cheetsheet  
**1. 换元积分公式**  
特殊：极坐标，球坐标，柱坐标  
一般：Jacobian

**2. 物理**  
[[Multi-variables Integral#Application & Example]]  
Average Value  
Mass, Moments, Center of Mass, Moment of Inertia(转动惯量)

**3. Surface Integral**  
核心思想为利用切平面进行近似（考虑给定区域切向量所决定的切平面）  
特殊：f(x,y) 的 graph, Revolution Surface


**4. Lebesgue Integral**  
Step Function：多个 n 维区间特征函数的线性和
- 任意一个 Step Function 均可以表示为若干个 n 维==不交特征函数的线性和==  
函数的包络级数： $f(x)\leq \Phi(x)=\sum_{i=1}^{\infty}c_{i}\chi_{Q_{i}}(x)$ 对 $\forall x \in \mathbb{R}^{n}$ 要求 $Q_{i}$ 为 n 维开区间  

**勒贝格积分的性质**：  
![91bc1b465abb4fe338e5e091a5f7fd1.png](https://s2.loli.net/2024/12/02/AJaCuX1oIPwpneU.png)

**勒贝格测度的性质**  
$\mathbb{R}^{n}$ 的子集 A 的特征函数勒贝格可积 ->A 可测

![f4ba1397af6f458813544211ecde1c4.png](https://s2.loli.net/2024/12/02/GyAdmVaThOIwoQL.png)

> [!tip] Summary
> 1. 一系列可测集的交集仍为可测集
> 2. 当一系列可测集其测度之和小于无穷时，他们的并集可测。特别地，当这些可测集两两不交时，其并集的测度等于这些可测集的测度之和 (核心性质: $\sigma$ 可加性,注意满足无穷可加性)
> 3. $\mathbb{R}^{n}$ 中有界闭集可测
> 4. $\mathbb{R}^{n}$ 中有界开集可测
> 5. 存在有界集不可测
> 6. $\mathbb{R}^{n}$ 中所有可数集测度均为 0（可数集可以被枚举，我们可以在其枚举出的每一个元素周围定义足够小的区间）
> 7. 测度为 0 的集合子集仍为可测集
> 8. 每一个 $\mathbb{R}^{n}$ 有界开集均可以用可数个有界闭集覆盖

- 对于有界闭集，我们可以马上得出其可测，同时对于一些情况我们会发现其边界为 smooth hypersurface(测度为 0),即可将一个闭集上的积分问题转化到开集上


**5. Line Integral**  
对于 differential 1 form $\omega=f_{1}dx_{1}+\dots+f_{n}dx_{n}$ 若该微分形式连续 (每个函数 f 均连续)，其在 piece-wise $C^{1}-curve$ 上的线积分为

$$
\int_{\gamma}\omega=\int_{a}^{b}\omega(\gamma(t))(\gamma'(t))dt=\int_{a}^{b}\sum_{i=1}^{n}f_{i}(\gamma (t))\gamma_{i}'(t)dt
$$

联系向量场 $F=(f_{1},\dots ,f_{n})$,则可以表示为

$$
\int_{\gamma}\omega=\int_{a}^{b}F(\gamma(t))\cdot \gamma'(t)dt
$$

注意轨迹 winding number 的计算

注意散度与旋度的定义以及性质

**6. Gradient Field 的性质**

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

注意对于全微分的微分形式 $\omega$ 其定义域一定为开集（因为 $\omega(x)=df(x)$）  
庞加莱引理重点关注二维与三维形式

**7. Topology**  
simply-connected, connected

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

注意 simply-connected set 的重要例子  
注意重要反例 winding form 虽然满足 $d\omega=0$ 但是其定义域并非 star-shaped region,不能找到其整个二维平面内的 antiderivative

**8. Parametric Surface**
- Parametric Surface 的定义，微分同胚的定义，浸入的定义
- $\mathbb{R}^{n}$ 中由 d 个向量组成的平行多面体
- Gram Determinant

#### 重要定理

**1. 紧集、可积、极值**  
重要理论：定义在紧集上的连续函数均为一致连续，基于此可证在紧集上均可积（可以控制 Darboux Sum 的差值）  
- Improper Riemman Integral: 当函数在 $\mathbb{R}$ 上的每一个有界闭区间 (紧集) 上黎曼可积时，当且仅当其 improper 黎曼积分绝对收敛时，函数 f 在 $\mathbb{R}$ 上勒贝格可积


**2. 单调有界定理**  
[[Lebesgue Integral#Monotone Convergence Theorem]]  
对于一个不减的可积函数序列，且其积分存在一个独立于 k 的上界，那么该序列极限函数的积分即为 k 区域无穷时的积分结果  
==先满足函数的不减关系，再关注能否找到独立于 k 的函数积分的上界==

- 推论：  
考虑一个嵌套的可测集序列，记其嵌套集合的并集为 A,f 在 A 上可积当且仅当 f 在该嵌套集合列中每一个集合上均可积，且其绝对值积分有界。此时我们可以通过其嵌套序列的极限积分去计算 f 在 A 上的积分  
==先确定寻找到的可测集序列满足嵌套关系，再确认其于每个集合上可积，且其绝对值积分可以找到不取决于 k 的上界==

**3. 有界收敛定理**  
[[Lebesgue Integral#Bounded Convergence Theorem]]

> [!tip] 有界收敛定理  
> 若 $\mathbb{R}^{n}$ 上可积函数的序列处处收敛，且存在一个独立于 k 的可积函数 $\Phi\geq 0$ 满足对该序列中任意的函数均有 $|f_{k}(x)|\leq \Phi(x)$. 那么这个序列的极限函数可积，且有 $\int f=\lim_{ k \to \infty }\int f_{k}$  
> Notes
> - 又名支配收敛定理， $\Phi$ 为支配函数
> - 相比于单调有界定理，不要求严格的函数序关系，但是要求存在极限函数

**Parameter Integral**

> [!tip] Theorem
> 1. 关于 x 定义在 y 的积分上的函数 F($F(x)=\int_{Y}f(x,y)d^{n}y$ 连续条件:
>    - $x\to f(x,y)$ 对任意的 y 连续
>    - 存在可积函数 $\phi$ 可以控制 $|f(x,y)|$ 的上界
> 2. F 偏导的性质（即可将微分号移至积分内部）: $\frac{\partial F}{\partial x_{j}}(x)=\int_{Y} \frac{\partial f}{\partial x_{j}}(x,y)d^{n}y$ 满足所需的条件
>    - $x\to f(x,y)$ 对于任意的 y 一阶可微 (要求 $X$ 为开集 ->意味着可以对每个 x 找到一个紧的邻域)
>    - 存在可积函数 $\phi$ 可以控制 $|\frac{\partial f}{\partial x_{j}}(x,y)|$ 的上界 (由于可微与连续均为局部的性质，所以该要求可以弱化为对于每一个给定 x 在其邻域内可以找到函数 $\phi$ 控制上界)

证明连续且能把积分号移至微分号中
- 证明存在可积函数 $\phi(y)$ 能控制 $|f(x,y)|$ 的上界（可以弱化要求至对每一个 x 找到一个邻域满足条件）
- 证明 $x\to f(x,y)$ 对于任意的 y 一阶可微
- 证明存在一个可积函数 $\phi(y)$ 可以控制 $|\frac{\partial f}{\partial x_{j}}(x,y)|$ 的上界


特别地，在寻找函数控制上界时可以考虑利用 Monotone Convergence Theorem 的推论，先在局部区间上证明

**4. Fubini 定理**  
[[Lebesgue Integral#Fubini's Theorem]]

> [!tip] Fubini 定理  
> **1. 定理内容**  
> 函数 $f:\mathbb{R}^{m}\times \mathbb{R}^{n}\to \bar{\mathbb{R}}$ 可积，则积分式 $F(y)=\int_{\mathbb{R}^{m}}f(x,y)d^{m}x$ 对任意的 $y\in \mathbb{R}^{n}$ 均存在，且可以交换下式的积分顺序
>
> $$
> \int_{\mathbb{R}^{n}}F(y)d^{n}y=\int_{\mathbb{R}^{n}}(  \int_{\mathbb{R}^{m}}f(x,y)d^{m}x) d^{n}y = \int_{\mathbb{R}^{m}\times \mathbb{R}^{n}}f(x,y)d^{m+n}(x,y)
> $$
>
> **2. 核心**  
> 核心条件为验证 $f(x,y)$ 可积

**5. 局部可积函数及其性质**  
[[Lebesgue Integral#Locally Integrable Functions]]

> [!tip] 局部可积函数  
> 函数 $f$ 局部可积 ->对于任意的 $x \in\mathbb{R}^{n}$, 均存在一个对应的邻域使 $f$ 在邻域上可积。
> 1. 以下这些性质均等价:
> - f 局部可积
> - f 在 $\mathbb{R}^{n}$ 的每一个有界开集上可积
> - f 在 $\mathbb{R}^{n}$ 的每一个有界闭集（紧集）上可积
> - f 在以原点为球心，任意有限半径的球内均可积
> 2. 与 Globally Integrable 的比较
> - Globally Integrable 要求函数在整个定义域上积分均为有限
> - Locally Integrable 仅要求函数在定义域的任意有限区域内可积，函数可能在定义域的某些部分可能区域无穷，但是这些无穷大的区域测度为 0
> 3. 联系与转化  
> $f$ 局部可积且在范数有限 等价于 $f$ 全局可积
> 4. 任意连续函数 $f:\mathbb{R}^{n}\to \mathbb{R}$ 以及通过在测度为 0 的区域函数值为无穷的连续函数 $g:\mathbb{R}^{n}\to \bar{R}$ 均为局部可积

**6. 换元**  
[[Lebesgue Integral#Change of Variables]]

> [!tip] 换元理论  
> 对于开集 $U,V \subset \mathbb{R}^{n}$, 且映射 $T:U\to V$ 微分同胚，则有如下换元积分成立。
>
> $$
> \int_{U}f(T(x))|\det J_{T}(x)|d^{n}x=\int_{V}f(y)d^{n}y
> $$
>
> - 勒贝格测度与勒贝格积分在欧几里得变换下保持不变（ $T(x)=Tx+b$,其中 $T$ 为正交矩阵， $b$ 为平移向量）
> - 可以直接用换元积分进行体积的测度转换。特别低，对于线性变换，其体积的变化直接体现在线性变换矩阵的行列式上

注意球坐标、柱坐标、极坐标换元以及 Rotational Invariant 函数