---
title: MATH 213 Collection
date: 2024-11-09
date modified: 2024-12-27
categories: MATH汇总
---

## 汇总表格

```dataview
table date
from #Math213
sort date
```

## 集萃

### 逻辑

**1. 命题**
- 命题不能是一个疑问句或者命令；
- **命题要么真要么假，不能涉及变量,命题一定能判断真假**  
逆命题 (converse),否命题 (inverse),逆否命题 (contrapositive)  
对于 $p\to q$
- converse: 条件结论交换 $q\to p$
- contrapositive: 条件结论交换并且同时取反 $\neg q\to \neg p$ (**注意逆否命题与原命题同真同假**)
- inverse: 条件结论同时取反 $\neg p\to \neg q$


**2. 逻辑连接词**  
![81819f3d30676bbc45ed3fda3d5fe88.png](https://s2.loli.net/2024/09/13/HehUVGDiEzQ9MWF.png)  
==重点领会 p->q==:(Not p; p implies q)

$$
p\to q \equiv \neg  p\cup q
$$

注意 p->q 准确应理解为 p 蕴含于 q (Not p; p implies q)  
![7689e29824a605738115c0dc3712d1f.png](https://s2.loli.net/2024/09/13/nruBSdofRc5i1H3.png)  
**Biconditional 的表述**
- p is necessary and sufficient for q（充分必要条件）
- if p then q, and conversely $(p\to q)\cap (q\to p)$
- p iff q

**3. 等价性**
- Tautology: 恒真
- Contradiction: 恒假
- Contigency: 既非恒真又非恒假  
**逻辑等价性**

$$
p \equiv q \text{ 或  } p   \leftrightarrow q
$$

证明:
- 利用 truth table
- 直接利用逻辑算符证明，证明两边的推出关系均成立  
**Boolean Logic**  
重点关注 De Morgan's Laws 与 Distributive Laws  
![38d16eddb67fb46f447ad7fb3266ef9.png](https://s2.loli.net/2024/12/27/IKvyJ4TSsNmx8wQ.png)  
![7c3fb119bbba3bd60b0149e10245960.png](https://s2.loli.net/2024/12/27/zs3p6AmDndja8xC.png)

**4. Predicate Logic & Quantified Statements 谓词逻辑与量化命题**

**谓词逻辑**
- 核心即为包含变量的论断（注意只有当变量的取值都确定时才能算命题）
- Domain: 所有变量可能取值的集合
- 真值集合即为所有使 P 为真的变量取值组合
- 命题函数 $P(x)$ 是一个含有变量 x 的表达式，当给 x 赋予具体的值时，$P(x)$ 成为一个命题  

**量化命题**  
**Types of quantified statements**
- Universal Quantifier 全称量词: $\forall$ For all x P(x)
- Existential Quantifier 存在量词: $\exists$ There exists an element x in the domain such that P(x)  
**Notice**: 当定义域为空集时, $\forall xP(x) \cup \exists xP(x)$ 均错误  
$\forall xP(x) \text{and}\  \exists xP(x)$ are propositions

![8cac60572318561c4151b3bb66c34c0.png](https://s2.loli.net/2024/09/14/VYQxC8oEpJczTIZ.png)

任意与存在的转化：

$$
\begin{align}
& \neg (\exists xP(x)) \equiv \forall x \neg P(x)  \\
& \neg(\forall x P(x)) \equiv \exists x\neg P(x)
\end{align}
$$

量词的顺序：
- 当量词的种类不同时，不能交换量词的顺序 (order matters)
- 当量词的种类相同时，可以交换量词的顺序 (order doesn't matter)

**5. 证明**  
![8a1cd8123bdb21e0111878ec9aba6db.png](https://s2.loli.net/2024/12/27/ZraBi4yxLp9tY3G.png)  
![cb1a99119d47bb29ddae6e0c276ff22.png](https://s2.loli.net/2024/12/27/Bcwtr7IJOaQFi2U.png)  
![c1f1e8a8158aa3c0c1931fecea709bf.png](https://s2.loli.net/2024/12/27/BzO9a1GLxwrJdHp.png)  
![1b61fd8347c094160d8ebbd5d75dd81.png](https://s2.loli.net/2024/12/27/6InOAeMTVmhdsyu.png)

![2794f37e697e23ee9b3ebe37583c33c.png](https://s2.loli.net/2024/12/27/wgCNW8I4tz6u1cT.png)

### 集合与函数

**1. 基本概念**
- 集合：一组无序的对象
- 集合的势 (cardinality)：集合中的元素个数
- 幂集 (power set)：集合所有子集的集合
- 元组 (tuple): 有序的集合
- 笛卡尔积 (Cartesian Product): 各集合元素的有序组合形式的多维组的集合
- 关系 (Relation): 笛卡尔积的子集  
![429c741f84b3908d6b90eeb24a34ef9.png](https://s2.loli.net/2024/12/27/oFdpnaHis8Gy23q.png)

**2. 单射、满射与双射**  
考虑函数 $f:A\to B$
- Injective, One-to-one 单射函数，不同的像对应不同的原像  
一个函数 f 单射当且仅当对于其值域中的所有 $x$ 和 $y$, 若 $f(x)=f(y)$, 则 $x=y$
- Surjective, Onto 满射函数，陪域中的每一个元素均有像与之对应  
一个函数称为满射，如果对于 $B$ 中的每一个元素 $b$ 均存在 $A$ 中的元素 $a$ 使得 $f(a)=b$
- Bijective, one-to-one correspondence 双射函数  
既为单射又为满射  
==证明双射 ->分别证明单射与满射即可==  
![c44a9da43b9349ded1c5ce5c9523068.png](https://s2.loli.net/2024/09/29/i4F3Xxa69GY1D5V.png)

**3. 逆函数与复合函数**  
![fb5cc75b19a4b4898a033e805db2791.png](https://s2.loli.net/2024/12/27/6rXcVJDF31nyhCw.png)

**4. 集合的势**

> [!tip] 总结
> 1. 可数集：集合为有限集或者为可数无限集（与正整数集的势相同，即集合中的元素可以按照一定顺序列举出来） 
>
>> 有理数集 $\mathbb{Q}$（可以考虑控制分子分母的和，然后逐项列举）, 代数集可数
>
> 2. 不可数集：集合中的元素不能按照一定顺序列举
>
>> 实数集 $\mathbb{R}$（考虑康托尔对角线）, 任意区间（可以与实数集建立双射）
>
>3. 证明集合的势相等：考虑构造相互的单射

### Complexity of Algorithms

**1. Growth Rate**  
![356444a770c5ba1a38afb80ab70e8c2.png](https://s2.loli.net/2024/12/27/oPNID7Wf5ZiBrcF.png)

常见函数的增长率估计  
![d056fedbaf9453662f37bf48384afe4.png](https://s2.loli.net/2024/10/11/8T6ZBCHq1YReWJD.png)  
注意 $\log(n!)$ 的量级  
证明：

$$
\begin{align}
& \text{On the one hand,}  \\
& \log(n!) = \sum_{k=1}^{n}\log(k) \leq n\log(n)  \\
& \text{On the other hand,} \\
& \log(n!) = \sum_{k=1}^{n}\log(k) \geq \log\left( \frac{n}{2}+1 \right) + \dots +\log(n) \geq \left( \frac{n}{2} \right)\log\left( \frac{n}{2} \right)
\end{align}
$$

**2. 常见算法**
- 计算多项式的值 Horner's Algorithm: $O(n)$  
![88aed10be9d2d106cb7a9a462945117.png](https://s2.loli.net/2024/10/11/yUhqbH56JojklGE.png)
- 插排：最坏情况为 $O(n^{2})$

### 数论：

- **带余除法记号与复杂度**  
divisor: 除数， dividend: 被除数， quotient 商，remainder 余数  

![d556cce7d0e770032e02af452b2653c.png](https://s2.loli.net/2024/10/16/hL3lQM5sHf1BZTq.png)

- **基本算法**  
[[Number Theory#Algorithm for Integer Operations]]
- **gcd 性质**  
基本内涵：从素因子最大公共幂次考虑；从两者最小正线性表示考虑
1. 辗转相除求 gcd(a,b)
- 不断重复重复带余除法的过程，记录每次的系数
- 从最终的余数向上回代，将 gcd 表示为原始 a,b 的线性组合
- 还可以利用 gcd 的线性表示解相应的不定方程/利用辗转相除求解逆

例如：  
![3dc96cb62f20e23777990d28e4f71b0.png](https://s2.loli.net/2024/12/02/lYQZuejgW1RDSHa.png)

- **中国剩余定理**  
![f159158e-f790-4369-8b5e-e1f9509f2c0c.png](https://s2.loli.net/2024/12/03/mBhQ2dzepiKrUAy.png)

