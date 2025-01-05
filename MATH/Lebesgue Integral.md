---
title: Lebesgue Integral
date: 2024-11-28
date modified: 2025-01-02
categories: Math241
tags: [Math241]
---

#Math241 

## Integration over $\mathbb{R}^{n}$

### Characteristic Function

**1. Definition**

![a32de50da714e19a034f22a52092fc6.png](https://s2.loli.net/2024/11/28/NF4i1gAtWPTsbkG.png)

**特征函数**
- 在给定空间内取值为 1，剩余取值为 0
- 注意特征函数定义在整个 $\mathbb{R}^{n}$ 上 ->狄利克雷函数并非特征函数

![3d3f8ee8a34784591f78e686d6923ba.png](https://s2.loli.net/2024/11/28/j3yY5qWSgUsud8G.png)


**2. 利用特征函数对于重积分定义域的自然延拓**

![9300a627d16f40e44f79435e67eba98.png](https://s2.loli.net/2024/11/28/1PcUNmeVXzJ94LH.png)

==基于特征函数，现在我们可以把重积分原有函数在整个空间中局部区域的积分转化为在整个空间上的积分，减少复杂性==

![1a2b2b66ba0b78260441222b77896a0.png](https://s2.loli.net/2024/11/28/CNJ16wPUEbSXBgy.png)

## The Lebesgue Integral

### General Intro of two approach

![5078df3cd5d2893936ab24cb8f11889.png](https://s2.loli.net/2024/11/28/LfPMXj6s8JNkiBz.png)
1. 测度论方法
2. L1- 半范数方法

### Step Functions

**1. Definition**

> [!tip] Summary
> - 基于区间长度定义 n 维区间的体积
> - 定义 Step Function(一定数量定义在 n 维区间上特征函数的线性和)
> - 定义 Step Function 的积分 ->自然考虑对应数量 n 维区间体积的线性和

![ec9052ec571b3fd99e7ac3a115513f0.png](https://s2.loli.net/2024/11/28/ZgOMQ69t4Lc8aiB.png)

**2. Theorem**

> [!tip] Theorem
> 1. 任意一个 Step Function 均可以表示为定义在若干个 n 维不交的区间上的特征函数的线性和
> 2. 如果 Step Function 存在多种表示形式，其积分的结果相同

![32030454533603f678b102d04c0ba8c.png](https://s2.loli.net/2024/11/28/AMTsXE4xRW7fzvt.png)

### L1-seminorm L1 半范数

![be69bebc685f0afcd75ba4a59c2c92d.png](https://s2.loli.net/2024/11/28/n2iUjHhQeDuxAb5.png)

==L1 半范数用于对恒大于等于 0 的函数 f 的横截面定义外测度==
- $O_{f}$ 表示函数在 $\mathbb{R}^{n+1}$ 为空间中的柱状体积
- L1 半范数的定义允许无限多可重合的覆盖区间 ->可定义无界的集合

### Definition

**1. 实数集上的算数扩展（考虑无穷的代数运算）**  
![6fce94cf48870c00ad5017ea8970a89.png](https://s2.loli.net/2024/11/28/QhLlGVPuoU4x9En.png)

**2. Enveloping Series 包络级数**

![d2cf60e0fffef8b39104fbfe608175e.png](https://s2.loli.net/2024/11/28/JQlcyxZYoDiGA4w.png)

==核心想法即为使用多个 n 维区间上的特征函数对函数 f(x) 实现覆盖，利用多个特征函数的线性和近似 f，并且通过取和估计 f 的覆盖范围==

- 每个 $Q_{i}$ 为 n 维开区间，且其对应的系数恒大于等于 0
- $f(x)\leq \Phi(x)$ 对所有 $x \in \mathbb{R}^{n}$ 恒成立
- 包络级数的内容即定义为对应 step function 的积分 $I(\Phi)=\sum_{i=1}^{\infty}c_{i}\text{vol}(Q_{i})$

**3. L1 半范数**  
![cae86f94b3ffbef8d30a52da160792c.png](https://s2.loli.net/2024/11/28/qm1TQcLjlgRxZuy.png)

==函数 f 的 L1 半范数是其包络级数的下确界==
- **$∥f∥_{1}$​ 是良定义的**：例如，当选择 $Q_{i}=(−i,i)$ 时，$\Phi(x)=+\infty$  是一个包络级数，因此包络级数总是存在。
- **性质**：$∥f∥_{1}$​ 满足所有“距离函数”的常规性质，但有两个例外：
    1. **$∥f∥_{1}=\infty$​ 是允许的（即 f 不绝对可积时）。
    2. $∥f∥_{1}=0$​  不一定意味着 $f(x)=0$ 对所有 $x$ 都成立。

**4. Cauchy Sequence->用于描述数列的收敛情况**

![e407c4d76143394fed0e66ae0e7170e.png](https://s2.loli.net/2024/12/02/auDXUH3WEOdqnsi.png)  
**柯西数列均收敛**

扩展到级数的情况 ->考虑利用绝对值收敛证明级数收敛  
![d465efe7cf7efe64f095e275bb26b44.png](https://s2.loli.net/2024/12/02/1VpwGeusFE9ojRm.png)


**5. Lebsegue Integral**

**勒贝格积分的核心即在于可以对函数 f 找到一个收敛的包络级数，最终使得函数的积分可以定义为包络级数的积分**

![d920904ebc6c058824b76b939af7337.png](https://s2.loli.net/2024/12/02/R2IjN7GlBvMxhEz.png)

**Remarks**  
![526797f29e16f9673d5f180ceb27f21.png](https://s2.loli.net/2024/12/02/alrV4AMYZD6LUIK.png)

### Example

**1. 证明狄利克雷函数勒贝格可积**

![17bbfcf2d6d0e116286be7ab69c8465.png](https://s2.loli.net/2024/12/02/LdXMylFEU7G1wtC.png)  
![4f72e11e17c50866579561116f4ec6c.png](https://s2.loli.net/2024/12/02/RODiHAKsChVUrW1.png)

证明核心：通过在离散的有理数附近取可以任意小的开区间建立狄利克雷函数的包络级数，同时我们可以该包络级数的积分任意小

### Elementary Properties of the Lebesgue Integral

![91bc1b465abb4fe338e5e091a5f7fd1.png](https://s2.loli.net/2024/12/02/AJaCuX1oIPwpneU.png)

> [!warning] 注意
> - f 可积可以推出|f|可积，但是|f|可积不一定能够推出|f|可积
> - 考虑两个函数乘积是否勒贝格可积时注意除了满足 f1,f2 本身可积，还需要满足**有界**

### Improper Riemman Integrals

- **Theorem**  
![734e92d8737107bf36918b95903e77b.png](https://s2.loli.net/2024/12/02/v7wjagAmhbtFQR5.png)

当函数在 $\mathbb{R}$ 上的每一个有界闭区间 (紧集) 上黎曼可积时，当且仅当其 improper 黎曼积分收敛时，函数 f 在 $\mathbb{R}$ 上勒贝格可积（**核心为关注其 improper 黎曼积分的收敛性**）

- **Example**  
![9f9b615796e8b0fac59b8700a235a95.png](https://s2.loli.net/2024/12/02/tjX7bpkc6TgNCiA.png)

## Lebesgue Measuere(勒贝格测度)

### Definition

![ed8900f14af50134055dab73d8a6ff4.png](https://s2.loli.net/2024/12/02/1xTozN5hKHgauMA.png)

- **可测**：我们称 $\mathbb{R}^{n}$ 的子集 A 可测，当且仅当其特征函数可积（measurable)
- **测度**：此时其特征函数的积分我们即记为集合 A 的测度或体积（measure/volume)

### Properties

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

![74d59dd0803b47a7675e8c96ed53706.png](https://s2.loli.net/2024/12/04/AcSzVael43C1Hxo.png)

### Cantor's Ternary Set 康托尔三分集

**Definition**  
![a98b6fd33cc78bbd22beadd3126d8a0.png](https://s2.loli.net/2024/12/04/aE7epdmVkDUvOsC.png)

### A Characterization of Sets of Measure Zero

**Theorem**: 测度为 0 的集合的等价表述  
![44c3668f3fbb1dd7dde248a15b1cb8e.png](https://s2.loli.net/2024/12/04/rY3qo4BH7NTXmvy.png)

**Example：$\mathbb{R}^{n}$ 中的光滑超曲面测度为 0**

![c261f4e90c34cb7536f898340bbb616.png](https://s2.loli.net/2024/12/04/rM69AzX1o3NGgcP.png)


直观解释：  
光滑超曲面 $S$ 是一个 $n-1$ 维的集合，在 $n$ 维的空间中没有足够的“厚度”来贡献非零的体积。可以将其类比为平面在三维空间中占据“零体积”，或者曲线在二维平面中占据“零面积”。

## Main Theorems of Lebesgue Integration

**性质几乎处处成立的定义 ->利用其否命题测度为 0 描述**

![9b9fc43f5900e3528b9fe731e16fd61.png](https://s2.loli.net/2024/12/04/bncqOFV2prGX1wR.png)


![1b7781ffb6ecc6eb9deb960bdd9932c.png](https://s2.loli.net/2024/12/04/J5evwzqsbl7Rrf2.png)

### Monotone Convergence Theorem

**单调有界定理**  
![e34072911df851c25d0982b5a162e7a.png](https://s2.loli.net/2024/12/04/V8kpxOzHljvQ4ge.png)

> [!tip] 单调有界定理  
> 给定一个定义在 $\mathbb{R}^{n}$ 上不减的可积函数序列，且序列中函数的积分有界。那么我们可以定义这个序列的极限函数 $f(x)=\lim_{ k \to \infty }f_{k}(x)$ ,同时我们可以交换这个序列上函数的积分与该极限函数的积分 $\int f=\lim_{ k \to \infty }\int f_{k}$
> 
> **单调有界定理描述了在特定条件下，如何将一列函数的积分极限与其点极限交换顺序**
> 
> Notes: 核心为可积函数序列不减，且有独立于 k 的上界
> - 该极限函数也被称为函数序列 $f_{k}$ 的 point-wise limit，因为对于每一个参数 x,我们可以单独验证其收敛性
> - 对于一个不减的函数序列，我们有其积分序列不减，那么其要么有界，要么趋于无穷
> - 可积函数必须处处有限

![9a1d8a2f19840a634c6858b32703c9b.png](https://s2.loli.net/2024/12/04/H57yXPce4dAC3Qs.png)

**Example**  
![da80f462cd160c5c02694d313b16053.png](https://s2.loli.net/2024/12/04/PO1Cl6Wi2DZUXLJ.png)

#### Corollary: Improper Lebesgue Integration

==考虑一个嵌套的可测集序列，记其嵌套集合的并集为 A,f 在 A 上可积当且仅当 f 在该嵌套集合列中每一个集合上均可积，且其绝对值积分有界。此时我们可以通过其嵌套序列的极限积分去计算 f 在 A 上的积分==  

![8a9a0464c83d57d44428fe21f299d9f.png](https://s2.loli.net/2024/12/04/eScLygOTMk6ruw2.png)  
先确定寻找到的可测集序列满足嵌套关系，再确认其于每个集合上可积，且其绝对值积分可以找到不取决于 k 的上界

**Example1**  
![dc3da560c9f0f79b6dee2145368a9c0.png](https://s2.loli.net/2024/12/04/9jBGrDv3bqQFWZI.png)  
![dec014548cb06ba3b6483a76567b47f.png](https://s2.loli.net/2024/12/04/3GQXxiYF5plOVt4.png)

**Example2: Gamma Function**  
![8be31834124adff832ea192735cb3be.png](https://s2.loli.net/2024/12/04/T4teayMQkgEx7nU.png)  
![4ac4152286485335a486f92dcb4cdc3.png](https://s2.loli.net/2024/12/04/E82dcMeHrubXCvL.png)  
![6bdffaf7e97d48a70b9b0026f9d171c.png](https://s2.loli.net/2024/12/04/MpGkY2yFw4ZInQm.png)

### Bounded Convergence Theorem

![ff20e47c6d3559635e28df715df5edf.png](https://s2.loli.net/2024/12/04/OVDyoBw12YkiKbd.png)

> [!tip] 有界收敛定理  
> 若 $\mathbb{R}^{n}$ 上可积函数的序列处处收敛，且存在一个独立于 k 的可积函数 $\Phi\geq 0$ 满足对该序列中任意的函数均有 $|f_{k}(x)|\leq \Phi(x)$. 那么这个序列的极限函数可积，且有 $\int f=\lim_{ k \to \infty }\int f_{k}$  
> Notes
> - 又名支配收敛定理， $\Phi$ 为支配函数
> - 相比于单调有界定理，不要求严格的函数序关系，但是要求存在极限函数

#### Parameter Integral

**引入参数，利用在对参数 y 范围内积分的基础上定义关于 x 的函数**
- 满足 Y 可测
- $y\to f(x,y)$ 在 $Y$ 上对任意的 $x \in X$ 可积  
![52dbef84105ed0707d73578ac3183c4.png](https://s2.loli.net/2024/12/05/sYWyLJGS7DRCvpQ.png)

==注意需要满足 f 可积==

> [!question] 如何利用 f 的性质研究函数 F 的连续性、可微性以及偏导?

![dbd372f6a14bb49605461e6b872800e.png](https://s2.loli.net/2024/12/05/AvfF3aCzhYgyISN.png)

> [!tip] Theorem
> 1. 关于 x 定义在 y 的积分上的函数 F($F(x)=\int_{Y}f(x,y)d^{n}y$ 连续条件:
>    - $x\to f(x,y)$ 对任意的 y 连续
>    - 存在可积函数 $\phi$ 可以控制 $|f(x,y)|$ 的上界
> 2. F 偏导的性质（即可将微分号移至积分内部）: $\frac{\partial F}{\partial x_{j}}(x)=\int_{Y} \frac{\partial f}{\partial x_{j}}(x,y)d^{n}y$ 满足所需的条件
>    - $x\to f(x,y)$ 对于任意的 x 一阶可微
>    - 存在可积函数 $\phi$ 可以控制 $|\frac{\partial f}{\partial x_{j}}(x,y)|$ 的上界 (由于可微与连续均为局部的性质，所以该要求可以弱化为对于每一个给定 x 在其邻域内可以找到函数 $\phi$ 控制上界)

![957657571c407f5e5555cbf06c7d693.png](https://s2.loli.net/2024/12/05/Ih7rcRSfNM2Uanv.png)


**Notes**  
![71133d4bbe3b68b19dbe438ac48c845.png](https://s2.loli.net/2024/12/05/cduL9G7S5A63Qxf.png)  
![aa7c3b8369e043dbffff281759019ee.png](https://s2.loli.net/2024/12/05/C2ItX9OwkZMSGAE.png)  
**Example**  
![7d0d88bf404717ae69ef79f18578b99.png](https://s2.loli.net/2024/12/05/PfuE2Dv1MFkVHci.png)

##### Feynman's Technique 费曼积分法

> [!danger] 重要技巧  
> 费曼积分法的核心即为为积分式引入新的参数，通过考察其引入新的参数后微分的情况，再得到最终的积分式

**Example1**  
![db6e7d6a7c2d12e19814dee52cb57a6.png](https://s2.loli.net/2024/12/05/r7cZpWoXmUvePqK.png)  
![9c4d97667a91d846e8d9f2f9ea63dd0.png](https://s2.loli.net/2024/12/05/t9SeF6nC4fMhKJ2.png)  
![6ccc5c3f7a325ab380380a696fee206.png](https://s2.loli.net/2024/12/05/EkLMuePSG7qA1To.png)  
![828399a1212f41ab7e0311634a96947.png](https://s2.loli.net/2024/12/05/9xtK4izCbE5wdFG.png)  
![6ad16603ce0134cc8ff79a4bdf7eeb9.png](https://s2.loli.net/2024/12/05/NdM2zV5QltWoh7L.png)  
![37f66a0934d498676ce46c73541e3c6.png](https://s2.loli.net/2024/12/05/uXQEIaLBqJgh9Oj.png)

**Example2: Dirchlet's Discontinuous Integral 狄利克雷积分**  
==可以作为勒贝格可积函数的反例==  
![2e1bf0f4c7428fce0324c19e8e64dbb.png](https://s2.loli.net/2024/12/05/GHhwrqIA9BO8ZTc.png)

### Fubini's Theorem

![11fafc6b6aefadcf43ae92d18279401.png](https://s2.loli.net/2024/12/05/spWkeAmOt9DHZVJ.png)  
**通过不断利用 Fubini 定理，将 n 维重积分不断降维，其中对不同维数积分顺序的选取是任意的**

#### Application

- **Example1**  
![9a9f473dc311cd6ccb3c3956b896f8c.png](https://s2.loli.net/2024/12/05/kymhPYIv7oewW6D.png)

**为了应用 Fubini 定理，需要满足 f 的可积性 ->相比于之前的证明，我们考虑用圆面约束**  
![a7c638a38e56324c8eef957d58decda.png](https://s2.loli.net/2024/12/05/SpbMnP1otCkGAce.png)

- **Example2->求解 n 维球的体积**  
![065c741686f1eff65dde75b713312a0.png](https://s2.loli.net/2024/12/05/8VNsEbUAn9JyPFj.png)

- *通过 Fubini 定理，我们将 n 维情况递归到了 n-1 维的情况*
- *进一步地，我们研究递归关系 ->引入相关引理*


![45f9e3fea11c1d5663f244bc7b57c4b.png](https://s2.loli.net/2024/12/05/xJ2TVfiGUwtzD9l.png)

![9c24548794f121b594881cb5f3cc59b.png](https://s2.loli.net/2024/12/05/9q6Ce71fjuaJlYz.png)

![c3b0fe55586bf19e3db8591e54ed7e9.png](https://s2.loli.net/2024/12/05/2JKHDVceGn1OtTQ.png)

当 n=5 时，n 维球的体积有最大值

#### Locally Integrable Functions

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

![8eaef9db734ce900cace4caff3571b4.png](https://s2.loli.net/2024/12/05/sBK3LpU5STfjwqm.png)

![6e535ab6b8075b382c09ec48abf8ea1.png](https://s2.loli.net/2024/12/09/O6ZLgcAI95et42b.png)

**Tonelli Theorem**  
![ae45fee12be91aa1786fba3e75207df.png](https://s2.loli.net/2024/12/09/oEiLgjD4hnRNbSZ.png)

相比于 Fubini 定理，Tonelli 定理不要求函数绝对勒贝格可积，只要求函数为非负可测函数

### Change of Variables

==为单元微积分中的换元积分在多元微积分中的泛化==

**单元微积分中的换元积分**

![acb3ff9d622dc170c06107563cb220f.png](https://s2.loli.net/2024/12/09/gVfCALJ4Ke1zOsX.png)  
换元积分可以扩展到各种形式的区间：
- 非闭，非有界
- $g'$ 在端点处不存在

> [!tip] 微分同胚概念（Diffeomorphism)  
> 考虑由 $U\to V$ 的映射 $T$ ,其中 $U,V \subset \mathbb{R}^{n}$ ,T 满足
> - T 为双射
> - T 与其逆映射 $T^{-1}$ 均为连续可微的映射 ( $C^{1}$-maps)（ $T^{-1}$ 可微的条件可改写为 $J_{T}(x)$ 满秩

![13ee6aeda3b4b48e62160349ca1713c.png](https://s2.loli.net/2024/12/09/8d4vibhFPIe9Vc1.png)

> [!tip] 换元理论  
> 对于开集 $U,V \subset \mathbb{R}^{n}$, 且映射 $T:U\to V$ 微分同胚，则有如下换元积分成立。
>
> $$
> \int_{U}f(T(x))|\det J_{T}(x)|d^{n}x=\int_{V}f(y)d^{n}y
> $$
>
> - 勒贝格测度与勒贝格积分在欧几里得变换下保持不变（ $T(x)=Tx+b$,其中 $T$ 为正交矩阵， $b$ 为平移向量）
> - 可以直接用换元积分进行体积的测度转换。特别低，对于线性变换，其体积的变化直接体现在线性变换矩阵的行列式上

![0d6858ddc941b4505b42d462cd8a4e4.png](https://s2.loli.net/2024/12/09/BgHnjvEY6X9SLW2.png)

**Notes**  
![79cc52ad6195491a3177b2f25fa4d4f.png](https://s2.loli.net/2024/12/09/LwIupPCrcYXdxoh.png)  
![32706990a1032bfbaea063900a959e4.png](https://s2.loli.net/2024/12/09/rKydmYBSU8tkl4Q.png)

### Applications

其中极坐标，球坐标，柱坐标在之前均有涉及  
[[Multi-variables Integral#Application & Example]]

#### Polar Coordinates

![20fbea8aaa283318e055b6b25b98b60.png](https://s2.loli.net/2024/12/09/ZNFbOGYLis6pR49.png)  
![1add4229a9ace59e35f3697e3d87f5f.png](https://s2.loli.net/2024/12/09/GcXzkIxCLTEa68p.png)

**Example**：Gauss Integral  
![b5cb80807e513fa248db3c6a906d03f.png](https://s2.loli.net/2024/12/09/JcOv6DfGzTydier.png)

#### Spherical Coordinates

![17681bb5a7e0982f1bfcbd27a7b10cf.png](https://s2.loli.net/2024/12/09/BHyPxlRGpwDrLYs.png)  
![adc7f8c3a11b4fb1e86218c145f1a53.png](https://s2.loli.net/2024/12/09/UVZ5TGgbyLQ7OPB.png)

#### Rotation-Invariant Functions

**函数值仅由其到原点的距离即 (length function 的取值) 确定**

![da54dd66d3abbb7d3a742b0afe6730c.png](https://s2.loli.net/2024/12/09/K4IFUqDSXadArEV.png)

**由对应极坐标换元以及球坐标换元的结果即可积出相应的系数**


==泛化情况==  
![84a7c8aa5e5d4c930815324030a828b.png](https://s2.loli.net/2024/12/09/At6Dacx2nVU51bS.png)

**Example1**  
![51baf1b6e528fe1d4755d8384f14c67.png](https://s2.loli.net/2024/12/10/A4TE6Y7jyZ9GVFH.png)

**Example2**  
![d4c1e3098a9c9f2e7bfc7d8759da9cb.png](https://s2.loli.net/2024/12/10/XRsjBxb3KuSItQC.png)
