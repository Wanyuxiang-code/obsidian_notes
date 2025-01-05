---
title: Relations & Graphs
date: 2024-11-27
date modified: 2024-12-29
categories: Math213
tags: [Math213]
---

#Math213 

## Relation

### Basic

**定义**：  
给定两个非空集合 $A$ 和 $B$ ，它们的笛卡尔积 $A\times B$ 是所有有序对 $(a,b)$ 的集合，其中  
$a\in A,b\in B$.

$$
A \times B= \{(a,b)|a\in A,b\in B\} 
$$

一个**Relation**  $R$  是笛卡尔积 $A \times B$ 的子集： $R \subseteq A \times B$

#### Binary Relation

**Definition**  
![7a501838204dd8b9e23264bf21870d2.png](https://s2.loli.net/2024/11/29/PmS5iFu2lLoYeG9.png)  
==Binary Relation 定义在两个集合之间，Relation 可以定义在多个集合之间==

#### Relation on the set

**Definition**:  
定义在集合 A 上的 relation 即为从集合 A 到其本身的 relation

![6a34520849b10d5ed9ea8935ad843df.png](https://s2.loli.net/2024/11/29/v4xjACTD7gcE2Qh.png)

#### Number of Binary Relations

先分析笛卡尔积的势，再考虑其所有子集的数量  
![9111633712b4d170793085a4d37b390.png](https://s2.loli.net/2024/11/29/vWUcoiNTEdIlCty.png)

#### Representation

- **Use Arrows**  
![15b97a2e078dfb2aa09055d1df850f0.png](https://s2.loli.net/2024/11/29/jyvCBQmH1OZh2eA.png)


- **Use Table**  
![e94742bad398d231608447d2cbc2747.png](https://s2.loli.net/2024/11/29/1uR9B2VJQrz7Hg5.png)

- **Zero-One Matrix** ->Represent Binart Relation  
![a998182e5dbf3a4b4a43fd7c0c9fe6b.png](https://s2.loli.net/2024/12/04/SV3PxBRukiZX271.png)  
![209216ba04fedaca561994426eeb27e.png](https://s2.loli.net/2024/12/04/r1VmawHeNnOtoW8.png)

==Join and Meet==  
Join—取并集，有 1 记为 1  
Meet—取交集，全 1 记为 1

==Composite of Relations==  
**Boolean Product 直接用矩阵乘法理解即可**

利用 Boolean Product 可以直接得到两个 Relation 的复合

![37737b088190208a478a8fa80542d73.png](https://s2.loli.net/2024/12/04/gnreiKRSsqIV7L8.png)



![e92d24a1ef87817eac1ad8ffc6ae4de.png](https://s2.loli.net/2024/12/04/dArBQR2yUTwIlDH.png)

### Properties of Relations

#### Reflexive Relation

**对于集合 A 的任意一个元素 a,均有 $(a,a)\in R$ , R 为定义的 relation**

从 Relation Matrix 上看即为其主对角线上的元素均为 1  
![e154de73bf680d231286a374726d45b.png](https://s2.loli.net/2024/11/29/nGWgcadfDQoUwmS.png)

#### Irreflexive Relation

**对于集合 A 的任意一个元素 a，均有 $(a,a)\not\in R$ ，R 为定义的 Relation**

**注意 Irreflexive 与 Reflexive 并非互斥的关系，可以既不为 reflexive 也不为 irreflexive**

Relation Matrix 的主对角线上均为 0

![0d1c66161115a1abc5e395e3fe9b733.png](https://s2.loli.net/2024/11/29/8XfTcaRrQjbMIvm.png)

#### Symmetric Relation

![5c2e2aafeb9dc102964b6c8db0c76fa.png](https://s2.loli.net/2024/11/29/u1nLFfxchPTJp94.png)  
**对于任意的 $(a,b)\in R$ 均有 $(b,a)\in R$**

**表现在 Relation Matrix 上为 Relation Matrix 本身为对称**

#### Antisymmetric Relation

![d215bc1206b9b924e6b2c071440ca2c.png](https://s2.loli.net/2024/11/29/vBR7iHWlDwaG3eU.png)

**除了对角线上元素，对于任意 $(a,b)\in R$ 均有 $(b,a)\not\in R$**

#### Transitive Relation

**传递性 Relation**  
![fddca499548f30bd129ef49bc86a518.png](https://s2.loli.net/2024/11/29/JIgKY1AuaqeksM8.png)

#### Combining Relations

**Relation 本身即为集合，因此可以对其利用集合的操作包括:   union, intersection, difference 等等去组合不同的 relation**  
![83469af2812438705f6dbe7a2b184dd.png](https://s2.loli.net/2024/11/29/bxcl279jOvFgDJo.png)

#### Composite of Relations

**多个 Relation 的复合**  
![9424541eb2f80b19f1ef9923ca18170.png](https://s2.loli.net/2024/11/29/zgxGU7J9Z1yl5aA.png)  
**注意复合的顺序 ->左手边的 Relation 作为复合映射的第二个映射**

**利用矩阵角度可以直接考虑经过矩阵乘法后的非零项**  
![39d830a74eb4d3845decb5ea8cc50c0.png](https://s2.loli.net/2024/11/29/PJmFYE9aj5iL1fs.png)

### Power of a Relation

- **Definition**  
同一集合的多次复合  
![5dfc1c194a44b9bac1fd658b91edd8f.png](https://s2.loli.net/2024/12/04/c4tSpYanUiNDQWj.png)

- **Transitive Relation and Power of a Relation**  
![a99a6e00bd7821b3ecc301b2fb3dfe1.png](https://s2.loli.net/2024/12/04/O7exSv6VUPbBCdA.png)

### n-ary Relations

- **Definition**  
涉及多个集合 Cartesian Product 的子集  
![8a5a0e52b51c7c6cf97a7283f502b2f.png](https://s2.loli.net/2024/12/04/oZzfnh2dueVBYDp.png)

对于 Functional Domain, 其中任意一个元素均最多对应 Relation 中的一个 n 维元组

- **Relational Databases**  
关系数据库即为 n 元关系

![5556cdbbc4754ec65a09803a61dc2d3.png](https://s2.loli.net/2024/12/04/oZNks9ESAY5MO8X.png)  
==Composite Key: 将不同的 domain 组合起来，其组合对应的 n 元组唯一==

![e58fa7f51f406f4716e5824ffe45560.png](https://s2.loli.net/2024/12/04/OWSt8nc5K7ZIxhw.png)

### Operator

**Selection Operator**  
根据满足某个特定条件对原有 Relation 进行筛选  
![7b6f12d899d637eb0af82a140160e6c.png](https://s2.loli.net/2024/12/04/CLjvAdhRmnlp826.png)  
**Projection Operator**  
根据要求删减原有 Relation 的某些维度  
![7f724530db3e83e0755544bc0b2a941.png](https://s2.loli.net/2024/12/04/tkehfaH7rUK6M2b.png)

**Join Operator**  
将不同的 Relation 拼接形成新的 relation(将能够满足 transitive 进行拼接的拼接起来)  
![e0251a3114b28b8f91b7b8293b5105f.png](https://s2.loli.net/2024/12/04/lWjXFhpRybu4TnL.png)

### Closure of Relations

**Definition**  
![d18f7779bd915a319eead49f166a0df.png](https://s2.loli.net/2024/12/04/5nyLAIrDufiFBe6.png)


- **Reflexive Closure**  
R 的 Reflexive Closure 为满足通过增补元素使 R 满足 Reflexive 性质的最小 Relation  

![ace3850728b1d9892a6fbae9dd1b948.png](https://s2.loli.net/2024/12/04/MsxVLCTRH9QnGg8.png)  
==类似地，我们可以定义 reflexive closures, symmetric closures 与 transitive closures==

- **Transitive Closure**  
![7a57f50dee5a05f1e6a11a3c3804ce2.png](https://s2.loli.net/2024/12/07/sRmdxK5y1NWbpVc.png)

### Equivalence Relation 等价关系

**1. 等价关系**

> [!tip] Definition  
> A relation R on a set A is called an **Equivalence Relation** when R is transitive, symmetric and reflexive.  
> 同时满足传递性，对称型，自反性

**Example**
- 整数上的同余关系  
![4dc7272eafc4ed838fe7bb4d3bd02d6.png](https://s2.loli.net/2024/12/12/AlvrcBNECXWL2Z1.png)

**2. 等价类**

等价类包括给定元素在等价关系下相关的所有元素的集合  
![1f1b671914c9c59978abfb1c0a5e5f3.png](https://s2.loli.net/2024/12/12/X4ED6dxQNytVJSz.png)

**Theorem**  
在等价关系下，我们有以下关系等价
- $(a,b)\in R$
- $[a]=[b]$ 元素 a,b 等价类相等
- $[a]\cap[b]$ 非空集  
![840433e86fe348e118e14d2bc87e784.png](https://s2.loli.net/2024/12/12/2mCsfnoxD1cyzZB.png)  
![7f466e02fad6437558eec112249adab.png](https://s2.loli.net/2024/12/12/VptbvZ8BqDzisgE.png)

**3. 划分**  
![89aae85fd71a566ebb8fa26bae86d9a.png](https://s2.loli.net/2024/12/12/HSq89hCQapFPefB.png)  
给定集合可以被划分为一系列不交非空集合的并集

**等价类与划分**->我们可以按照等价类对集合进行划分  
![bb9f5fc1417f427d97ce974b914512f.png](https://s2.loli.net/2024/12/12/lAfsuzPbqGRMT42.png)  
**对于任意一个在集合上的划分，我们都可以将其中的集合作为其对应的等价类 ->当且仅当元素 $a,b$ 都属于同一个划分的子集时，我们有 $(a,b)\in R$**

### Partial Ordering & Total Ordering

![b62786d7fe4bf2e4f720b47c3457fd7.png](https://s2.loli.net/2024/12/13/I4Y1WOxpNtvSHil.png)

#### 偏序关系

**Definition**  
偏序关系需要满足的性质
- 自反性
- 反对称性
- 传递性  
我们可以将集合 $S$ 以及定义在其上的偏序关系 $R$ 一起叫做偏序集 (partially ordered set), 记为 $(S,R)$  
![c999074437b1e05c944c9887ae1695c.png](https://s2.loli.net/2024/12/12/CI5c4msftZDwM7V.png)

**Comparability 可比性**

==在偏序集中，当且仅当元素 a,b 之间有偏序关系才有可比性，否则元素 a,b 不可比==  
![a9da6fd18b5da0a0e9844eb8b2688ea.png](https://s2.loli.net/2024/12/12/lGzsCEZrIpMhun2.png)

#### 全序关系

全序集又称 totally ordered or linearly ordered set. 对应的关系称为 total order 与 linear order

对于全序集，其中的任意两个元素均具有可比性

![cf9683976eb6bec740d6bf672639150.png](https://s2.loli.net/2024/12/12/4UoDMLwBymc1QCt.png)

**Well-Ordered Set 良序集**  
良序集为特殊的全序集，需要满足以下条件
- 其对应的偏序关系为全序（集合 S 中任意元素均具有可比性）
- S 的任意一个非空子集均具有唯一最小元素  
![62d94ee7a6d67da05000ba8ae31e027.png](https://s2.loli.net/2024/12/12/KQNTHJql1mpMGf2.png)

#### Lexicographic Ordering 字典序

给定两个有序集 $A_{1},A_{2}$,其字典序定义在其笛卡尔积 $A_{1}\times A_{2}$ 上，对于其笛卡尔积中的元素他们的比较关系通过如下确定:
- 优先比较第一个分量
- 如果第一个分量相等比较第二个分量  
![84c6cf11084b0c6237183c34d341aeb.png](https://s2.loli.net/2024/12/12/NqKGXufJBTt91P3.png)

#### Hasse Diagram 哈斯图

**Hasse Diagram 是一种图形表示法，用于直观显示偏序集中的元素及其偏序关系 ->Hasse Diagram 通过删除冗余的比较关系（包括自环、传递性）来简化偏序关系的表示**

![82694794f1bacc8aad35b4239433506.png](https://s2.loli.net/2024/12/12/7OU1eqEQCH6dg3w.png)

**构造 Hasse Diagram 的过程**
- 删除每一条自环边
- 删除传递性边 ->如果 $a\leq b,b\leq c$,则不直接连接 a,c
- 垂直排列：按照偏序关系的级别垂直排列，较小的元素位于下方，较大元素位于上方

#### Max(Min) & Greatest(Least) & bound

- Maximal and Minimal Elements

**在偏序集中的 Maximal 或 Minimal 元素即为找不到其他元素与之具有 $\prec$ 或 $\succ$ 的元素**

![4dc273ccca93638dc09885fb24051be.png](https://s2.loli.net/2024/12/13/uPISelTtMyopg89.png)


- Greatest and Least Element

**Greatest 与 Least Elements 即为偏序关系中对任意其他元素都有 $\succ$ 或 $\prec$ 关系的元素**  
![20681aba40810c5cd70907b15f46643.png](https://s2.loli.net/2024/12/13/jvru8ZGlfOkycRK.png)

- Upper and Lower bound  
![f1652a3b8779fd484f9a57cff5be929.png](https://s2.loli.net/2024/12/13/iYSBcNoauH72hmg.png)



- **在偏序集中的 Maximal 或 Minimal 元素即为找不到其他元素与之具有 $\prec$ 或 $\succ$ 的元素
- **Greatest 与 Least Elements 即为偏序关系中对任意其他元素都有 $\succ$ 或 $\prec$ 关系的元素** 
- **上界下界：与偏序集子集 A 中的任意元素均有偏序关系（大于/小于）**

#### Lattices

**注意偏序关系中的 Lattice 即为对于关系中任意一对元素均有最小上确界与最大下确界**

![23acb99c2b5f51a5c7ecfc40f8d8ca1.png](https://s2.loli.net/2024/12/13/P9ERZ6y4G8IYozM.png)

## Graph

### Basic

**1. Definition**  
![27c4674cc791fa466e05a5202e487b2.png](https://s2.loli.net/2024/12/13/zSoHiBXqwmlbjyn.png)  
**子图 Subgrph**  

![29c8f96398f6203dd64574f7f97c8b6.png](https://s2.loli.net/2024/12/13/azqSsAwJVk86rK3.png)  
==proper subgraph->非 Graph 本身的子图==

**图的并集**  
![e35fd62133e12f53430d7dcf857d9da.png](https://s2.loli.net/2024/12/13/othBw8FK9WITksE.png)


**2. 简单分类**

> [!tip] 图的简单分类
> 1. Simple graph, Multigraph, Pseudograph
> - Simple graph: 图中每一条边都连接不同的节点，且没有两条边连接同一对节点
> - Multigraph: 图中存在多条边连接同一对节点
> - Pseudograph: 图中可能存在自环或者多条边连接同一对节点或者节点与自己本身
> 2. Directed and Undirected Graph
> - Directed Graph: 图中的边为有向边
> - Undirected Graph: 图中的边为无向边

![e45fee2d4e832888a6c20644530de7e.png](https://s2.loli.net/2024/12/13/iYqrw8lxkN5Dedh.png)

![d05e8b3cc754ff1ca79a50cf34de074.png](https://s2.loli.net/2024/12/13/brAyBzaT6wfY9u1.png)

**3. 特殊图**

- 完全图：简单图中任意两个节点均有边相连  
![76623c2b273189e1f95a68734c072b3.png](https://s2.loli.net/2024/12/13/mGX9VoeDBkOzhdE.png)
- Cycle: 节点依次相连形成环  
![186b0483ad7f54914367070573a383a.png](https://s2.loli.net/2024/12/13/GI9YSV4ZuNF1fms.png)
- Wheel: 在 Cycle 的基础上增加一个与所有点相连的的点  
![0b3d9bbec421321027cbee7a92d843f.png](https://s2.loli.net/2024/12/13/R3QPi6nHfpMuKhJ.png)

- N-dimensional Hypercube  
![f6acdc703afeb0abe96b945267ba89f.png](https://s2.loli.net/2024/12/13/Zkt3dKYO81cDibS.png)

### Undirected Graph

![5734c99262b2f5cf7c0a7e2701747f4.png](https://s2.loli.net/2024/12/13/FJ2SsQkoy7DtPdT.png)
- 相邻：无向图中存在边相连的节点
- 邻域：记无向图中与顶点 $v$ 相邻的的节点的集合记作它的邻域 $N(v)$
- 节点的度：无向图中节点的图即为与其相连的边的数量（注意需排除自环给节点贡献两条边的情况）

**边与节点度的关系**  
![d3b435c0630cfd613f91a6503614a34.png](https://s2.loli.net/2024/12/13/L5ThnezJa6KMutE.png)

### Directed Graph 有向图  

![6ebd9cd875a491bd1bb5ea46c4ed2fc.png](https://s2.loli.net/2024/12/04/wnP4XSgvREaYslz.png)  
![62065caefd9cb83ad32273eae24fbba.png](https://s2.loli.net/2024/12/04/sfEWa92LdkTReCU.png)

> [!tip] Summary  
> Reflexive: 节点均有自环  
> Irreflexive: 节点均无自环  
> Symmetric: 边均为双向  
> Antisymmetric: 无双向边

- **节点的出度与入度**  
![0f09b323657cfe4784d2df80df6f429.png](https://s2.loli.net/2024/12/13/nXcbiHYsExg9h6F.png)

==有向图中，出度和等于入度和==  
![62b7daf913a5ba221e05780139ea277.png](https://s2.loli.net/2024/12/13/CYsx1KBVFlR3mjc.png)

#### Paths in Directed Graphs

**Definition**

路：在有向图中从起点至终点沿着边的方向形成的路径

路的起点与终点相同 ->circuit/cycle(回路)


![f6545966b6ddc1c9b8b2f5eba676013.png](https://s2.loli.net/2024/12/07/WNv1bnCFzPq9JjO.png)

**Theorem**  
从 $a$ 至 $b$ 长度为 n 的路存在当且仅当 $(a,b)\in \mathbb{R}^{n}$  
![e8f4c7e210fde2346f90d0650c83f51.png](https://s2.loli.net/2024/12/07/GMkgVwClEYDy9Kf.png)

#### Connectivity

![1f69a730c92230f0d362b84ccfd5826.png](https://s2.loli.net/2024/12/07/u2npI6JaNyVXLcG.png)  
![c8d0e7c0f0b5bf8f185154cb0c2da67.png](https://s2.loli.net/2024/12/07/iDwNUqcCXQFjdJS.png)


**Theorem**

==传递闭包即为将有向图中所有能够通过路相连的节点均相连==  
![6c28615ba52e3a96caa29dab1565fc4.png](https://s2.loli.net/2024/12/07/9S4HRwF61OB2V5J.png)

![79e3b284a66cca618a105e2998ce4d5.png](https://s2.loli.net/2024/12/07/yd1Gbk7wtTFxEvQ.png)  
**进一步地，我们建立传递闭包与 0-1 矩阵的联系**

![87571acb45f4875a548ffb3a8fe7cb9.png](https://s2.loli.net/2024/12/07/ujt9C2fzKDgiVlx.png)

### Bipartite Graphs

- **二部图：二部图中的任意一条边均连接图中存在的两不交分割的两个节点**  
![e34f79a19b6c3ac4dcb4abee2592e10.png](https://s2.loli.net/2024/12/13/4hfakiIp2vXTBR9.png)
- **完全二部图：图 G 的分割 $V_{1},V_{2}$ 任意一对节点均有边相连**  
![5d3fe490012ba2127b3f155a8325031.png](https://s2.loli.net/2024/12/13/tl8PCYyK2asZbH4.png)
- **Bipartite Graphs and Matchings**  
![f0580a574e36934e2ccc45898dd1cfc.png](https://s2.loli.net/2024/12/13/ms4fKqUASg5ZoYX.png)  
==Matching 为图中边的一个集合，其中没有两条边共享一个同一个顶点==

**Maximum Matching and Complete Matching（最大匹配与完全匹配）  
![dc1bc6e444c4bf5ff53b1cd25a3861c.png](https://s2.loli.net/2024/12/13/7G15cz3wYHZb2r8.png)
- 最大匹配：覆盖边数最多的匹配
- 完全匹配：从二部图的分割 $V_{1}$ 到 $V_{2}$ 的完全匹配为 $V_{1}$ 中的每一个顶点都在 M 中出现
- 完美匹配：将二部图中所有顶点两两配对，对于两个分割均为完全匹配

**霍尔婚配定理**  
![61064a80c31641b16866e966b89117e.png](https://s2.loli.net/2024/12/13/OFcPjW95lv8stbo.png)

### Representation of Graphs

1. **邻接表（adjacency lists）**

![526f7416a16614617109cebe2881ccb.png](https://s2.loli.net/2024/12/18/CZdegPKj2Jy3xTA.png)  
表示方法
- 如果图 $G$ 有 $n$ 个顶点 $V = \{v_1, v_2, \dots, v_n\}$，对于每个顶点 $v_i$​，我们使用一个列表存储与 $v_i$​ 相连的所有顶点。
- 对于**无向图**，若边 $\{u, v\}$ 存在，则在顶点 $u$ 的列表中包含 $u$ ，并在顶点 $v$ 的列表中包含 $u$ 。
- 对于**有向图**，若边 $(u,v)$ 存在，则在顶点 $u$ 的列表中包含 $v$

2. **邻接矩阵（adjacency matrices）** 


![c15bb86bc23585c1d4491e85d76c457.png](https://s2.loli.net/2024/12/18/KcYU96FiogXa8jL.png)

用邻接矩阵表示图时，当图中存在自环或者一对节点有多边相连时，此时邻接矩阵非 0-1 矩阵 

![4058c78918d6d34541960810927224c.png](https://s2.loli.net/2024/12/18/ZYVFOB8bokGy3KL.png)


3. **关联矩阵（incidence matrices）**

关联矩阵按图中的节点顺序标记节点与图中每一条边的关系，若边与该节点相连，则在节点对应的列中标记为 1

![8cb8df6fca76e4cf472ef0863ade281.png](https://s2.loli.net/2024/12/27/5liBjqVGXcHYn8u.png)

###  Isomorphism of Graphs 

**同构图**  
**Definition**  
两图同构当且仅当存在两顶点集间存在一个一一映射同时满足映射前后点的邻接关系，  
此时这样的映射被称为**Isomorphism**.  
==核心思想为利用图的不变量：节点数、边数、度的情况来判断两图是否同构==  
![6e06c0d41e82835ebb891589b10e414.png](https://s2.loli.net/2024/12/27/stV2unviUKhkmyL.png)

#### 判别

==核心思想为利用图的不变量：节点数、边数、度的情况来判断两图是否同构==
- Example1  
![8ba243509089a094343ac33252ac78c.png](https://s2.loli.net/2024/12/27/HWCe7i2fV8pclnM.png)
- Example2  
![35e5b35e9d61f5b584fd7b4d6902952.png](https://s2.loli.net/2024/12/27/OG6iSZftclPWq9A.png)
- Example3：对于同构图直接构造同构映射  
![cfc41d8164b949c60f0ab1d9e6b46c8.png](https://s2.loli.net/2024/12/27/Fhd9XvxwYNT4ajg.png)

### Path

**1. 无向图中的路**  
![deb82148c0e55eff8361a6000df3cc5.png](https://s2.loli.net/2024/12/27/vMszVpCfnyxHBk5.png)
- Circuit: 环路，路的起点与终点相同
- Simple path/circuit: 路中不存在重复边
- 路的长度：路中边的数量

**连通性 Connectivity**
- Connected Graph(连通图): 对于无向图，任意一对不同的节点之间均有路相连
- Disconnected Graph(非连通图): 对于无向图，存在不同的节点间没有路相连
- 性质：两节点间有路必有简单路（删去回路）-> 连通无向图间任意一对节点均有简单路

![2de8f94b67a8675193b810fa042ec5b.png](https://s2.loli.net/2024/12/27/gG8WLb36qmTEVHI.png)

**Connected Component: 连通分量**  
无向图中的连通分量，连通分量是一个子图，满足：
- 最大连通性：这个子图中的任意两个节点都通过路径连通，并且这个子图不能再加入其他顶点而保持连通
- 独立性：不同的连通分量之间没有共同的顶点或者边

当图中存在两个及以上连通分量时，该图不连通，此时图为其不交连通分量的并集

![d535ed2beddcc24a9f82f7943587148.png](https://s2.loli.net/2024/12/27/njkm5YzZvXPKfqe.png)

**2. 有向图中的路**  
![a39e73d00efe4e31ff9ae77cfd4b498.png](https://s2.loli.net/2024/12/27/1sRT6tcqyGU8YxA.png)

**3. Cut Vertices and Cut Edges**  
![b3aa228c12b4edd90309786ee3d8901.png](https://s2.loli.net/2024/12/27/jqxOKkA8Qph7u6S.png)  
![e2cc99de7635ddbd79be4fb31f150de.png](https://s2.loli.net/2024/12/27/WgIrKHLtfk2U1Z6.png)


- Cut Vertices: 在连通图中删去相应的节点以及与其相关的边,此时图不连通
- Cut Edges: 在连通图中删去该边，此时图不连通
- Edge Cut: 在图 G 中减去这些边的集合后，连通图变为非连通

**4. Paths and Isomorphism**  
利用路这一图形不变量来判断两图是否同构

![8e20f8e8d4cba7d6c68fd3e527398ac.png](https://s2.loli.net/2024/12/27/cSmduLtOMTN9qeZ.png)  
**5. Counting Paths between Vertices**  
在图 G 中，从点 $v_{i}$ 到 $v_{j}$ 路的条数即为 $A^{r}$ 中 $(i,j)$ 的项![1f09a0c1af8691282f9ff3584dcb826.png](https://s2.loli.net/2024/12/27/QHGOIUarbTAJ6v9.png)  
我们利用归纳法给出证明  
![dcfdae8692e991c4006f901dbdc6e77.png](https://s2.loli.net/2024/12/27/Yu5CHT8Rm6JAZEp.png)

**6. Euler Paths and Circuits**

![f5d6bd94e3905fc0c6aef3322007c88.png](https://s2.loli.net/2024/12/27/DYsEAQpbNxJoO3r.png)

- Euler Path: 经过图中的每一条边且没有重复边（顶点允许重复）
- Euler Circuit：经过图中的每条边且经过一次的回路

基本性质
- Euler Circuit: 图中的每一个节点度数均为偶数 ->因为对于每一个节点必有出边与路边相对应
- Euler Path: 图中有且仅有两个节点度数为奇数（起点与终点）

![d816bcdb271ebaa29e7bec770856a03.png](https://s2.loli.net/2024/12/27/y2a4hVeuXnN9YFJ.png)

当我们满足图中每个节点的度数均为偶数时，我们可以递归地构造一个 Euler Circuit

![93caf604000f111c4425f60ee9f0b65.png](https://s2.loli.net/2024/12/27/Js8bQA13rcyRhk5.png)

**7.  Hamilton Paths and Circuits**  
![ac0a6733d6841e4e151a6baba0dd9a3.png](https://s2.loli.net/2024/12/27/HzdxSKZc9X3BeGk.png)

- Hamilton Paths 哈密顿路：经过图中每一个节点恰好一次的简单路
- Hamilton Circuit 哈密顿圈：经过图中每一个节点恰好一次的简单回路

若哈密顿圈存在，其路径内必然不能包括小圈 ->可以作为否定性的条件（分析圈的关系）

没有简单地判定哈密顿路或者圈的条件，但是我们有以下定理：
- **Dirac's Theorem**: 若图 G 为简单图，且其中每个节点的度 $\geq \frac{n}{2}$ 则 G 存在哈密顿圈
- **Ore's Theorem**: 若图 G 为简单图，且对于图中任意一对非相邻的节点，均有 $deg(u)+deg(v)\geq n$，那么 G 存在哈密顿圈  
![5a4b88ee0a925e3e631c4d734b755d2.png](https://s2.loli.net/2024/12/27/qOhldi1w8Qg5F7P.png)

最短路径问题 ->考虑 Dijkstra 算法

### Planar Graphs

**Definition**  
平面图：当图可以被绘制在二维平面上且满足没有边交叉时，我们称该图为平面图  
![f049336908781576dd9e7c03af15e8c.png](https://s2.loli.net/2024/12/27/tgsPwNqzxQVdDrk.png)

- **Euler's Formula 欧拉公式**  
描述连通的简单平面图边数、顶点数与面数的关系  
![37c3e213d6ddf531a6aee62602d428a.png](https://s2.loli.net/2024/12/27/IfVwLOCxnrGTW28.png)

![aef25e703cc878d3dc20fd311f647d6.png](https://s2.loli.net/2024/12/27/pQl1KVn89mULjJe.png)

- **The Degree of Regions**  
区域的边数定义为区域边界上边的数目，当一条边在边界上出现两次时，它贡献两个度  
对于平面图，我们有

$$
r=e-v+2
$$

- **推论**
1. 对于简单的连通平面图，有 $e\leq 3v-6$
2. 对于简单的连通平面图，G 存在度数不大于 5 的节点
3. 对于简单的连通平面图，若其中不存在长度为 3 的环路，那么我们有 $e\leq 2v-4$

![3724b4ed6c50d41bd1a792c7fe0ac34.png](https://s2.loli.net/2024/12/27/ZBECM46AmVs7zey.png)  
==利用边的总数与平面区域的度的关系构造不等式 ->一个区域的边界至少需要三条边==

![d0f18951f4b297b29012855b7d4c9ce.png](https://s2.loli.net/2024/12/27/9VRhYTPGCXscDr3.png)

### Graph Coloring

染色问题

**简单图的着色问题（A coloring of a simple graph）**  
即为将颜色赋给图中的每一个节点，使得任意两个相邻的节点不会具有相同的颜色

**Chromatic Number 色数**  
给一张图着色所需最小的颜色数目，记为 $\chi(G)$

**四色定理**  
平面图的色数不超过 4


![268a1aab930854029a3d07f410a101f.png](https://s2.loli.net/2024/12/27/UM62qOHVdDZPYTt.png)

![b6b3dab52c7d5c80737603a331a276b.png](https://s2.loli.net/2024/12/27/LQvCsMJOtDPVfmg.png)
- n 阶完全图的色数一定为 n
- 完全二部图的色数均为 2
- 偶数个节点的圈色数为 2；奇数个节点的圈色数为 1

## Tree

### Basic

**Definition**  
A tree is a connected undirected graph with no simple circuits.树即为没有简单回路的连通无向图


**Theorem**  
An undirected graph is a tree iff there is a unique simple path between any two of its vertices.一个无向图是树当且仅当其任意两个节点之间都有一条唯一的简单路

### Rooted Trees

Rooted tree 即为我们在一个 Unrooted tree 中选定一个根节点，然后将所有边方向记为远离这个根节点

![818611963919175a2dab5f4c4740dd7.png](https://s2.loli.net/2024/12/27/KPNnZT2yr6zcLQl.png)  
![385dc2cecd662648a7e47bccf2c11c2.png](https://s2.loli.net/2024/12/27/wbnQPRfWxXpyStc.png)

- Parent: 对于节点 $v$ 存在的唯一有有向边 $u\to v$ 的节点 $v$
- Child: u 为 v 的 parent, v 为 u 的 child
- Siblings: 具有相同 parent 的节点
- Ancestors: 从根节点到本节点路上的所有点
- Descendants: 所有以该节点作为 ancestors 的节点
- Leaf: 没有 child 的节点
- Internal Vertices: 有 child 的节点

![4e1c56635270b8b82153ef94e12ff4c.png](https://s2.loli.net/2024/12/27/hwS7W3EiNOq8XBP.png)  
每个节点的 Children 数量小于等于 m -> m-Ary tree  
每个内点的 Children 数量均为 m -> full m-Ary tree

![f33cc50b2f49e5c21826e6a970aec27.png](https://s2.loli.net/2024/12/27/bxLor1NDkXpumgZ.png)



![940fee58d2d283a2a3d6f21354b8680.png](https://s2.loli.net/2024/12/27/LzlqeVTwUxYXHvk.png)

**平衡树**  
对于高度为 h 的 m-ary 树，所有 Leaf node 的 Level 均为 h 或 h-1

**Theorem: 高度为 h 的 m-ary 树中 leaf node 的个数**  
![324ca922a915a4945a9aba59839fe95.png](https://s2.loli.net/2024/12/27/7YEQOphNFe6d8Ut.png)  
![de1d9364c3a5e21e88cbfa4c8de8872.png](https://s2.loli.net/2024/12/27/QJ5GUefX1KFLdnp.png)
