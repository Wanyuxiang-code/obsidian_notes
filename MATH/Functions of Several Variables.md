---
title: Functions of Several Variables
date: 2024-10-15
date modified: 2024-11-09
categories: Math241
tags:
  - Math241
---
#Math241 

## Limit and Continuity

### Basic Terminology

**多元函数**  
![6c1b83c92be0feaf8a1bd4b4d8614c7.png](https://s2.loli.net/2024/10/16/rndhN4jUc2sg5IW.png)

**Limit and Continuity**
- Definition  
![79abea0e4a1d18e66fd9aa1e0a231c5.png](https://s2.loli.net/2024/10/16/97canGBwSvqYixH.png)  
即为都利用欧几里得距离去衡量向量之间的的接近程度，以满足极限或连续性定义中无穷小的条件

![d82bc6c6d280edf428265499ef921de.png](https://s2.loli.net/2024/10/16/wqE9W2TSKMVzOeB.png)  
![685f464a72a1dd72b3e889cd74295d6.png](https://s2.loli.net/2024/10/16/isE97yFQ4VHzPT5.png)

注意：
- 只有 Accumulation Point 才有极限的定义 (即只考虑 Accumulation Point 的极限)
- **对于映射结果也为高维向量的函数，其极限存在的条件也即为各个维度上极限存在（注意逼近的路径任意，可以从空间中各个方向逼近，但极限存在意味着均需得到相同的结果）**

**Graphs**: 对多元函数进行可视化  
![c32da6d349c6ae63ab8770408720ab2.png](https://s2.loli.net/2024/10/16/cUjDMOkJXlo3dus.png)  
**Level Sets**  
即固定其函数取值的结果，考察对应定义域中点集的分布（最终可以画出形象的等高线）  
![90e65aaf3acb05964bcbb044218966e.png](https://s2.loli.net/2024/10/16/ptJC5mAMojH1azQ.png)

### Examples

![138fd8a67cc3443180d87fffbbd1dbc.png](https://s2.loli.net/2024/10/16/Dcom4ejPzvNY5TU.png)

![6cd2d0c18c9fb8a5b84d52d80e3dedd.png](https://s2.loli.net/2024/10/16/DOQaJg2NqfrA9ws.png)

![862b517527dc2aa9346d32a48b3428f.png](https://s2.loli.net/2024/10/16/gexqS7vNZLmwuTK.png)

#### Complex Function

![0eaef6b72f3d1b4a787e80b80b008a0.png](https://s2.loli.net/2024/10/16/FHISXqJrgB23L5G.png)
- 共轭
- 模长
- 倒数 (multiplicative inverse)
- **指数形式**

![3d4eabad970ff1f95a21dc738ddc73b.png](https://s2.loli.net/2024/10/16/1EbOyCg6i8h4IFV.png)
- **单位根**  
![0d665e6fc94404a5f3aa30894656798.png](https://s2.loli.net/2024/10/16/ZNxnCWO2vfVRLyM.png)

**代数基本定理**：研究多项式方程根的关系，注意实系数方程虚根成对  
![4df926c4d5242d7240349c6ab40483e.png](https://s2.loli.net/2024/10/22/j1KSxs2ucbPYvhX.png)



**Midterm2 注意以下映射的关系**  
![bffc1832374c85cf1c0cc5be9909253.png](https://s2.loli.net/2024/10/16/prK1IxSZE754zGM.png)  
![5a791a2d2395921f2db2cc08f784036.png](https://s2.loli.net/2024/10/22/ecQ4Aa5b1vBoUJT.png)

### Further Rule

**核心即为对连续函数的组合与复合的结果依然为连续函数**  
![5227765f5dce11344eba81e061d6be3.png](https://s2.loli.net/2024/10/16/kFP1zeJLBgqj9ip.png)  
证明：  
![3c98dd29ecd9354ac2205154fe2ed5c.png](https://s2.loli.net/2024/10/22/gBPklAeKjpTfDzv.png)

**Useful Remarks**
 - 对于定义域为闭集，陪域为 $\mathbb{R}$ 的情况可以确定最大值与最小值的存在
 - 如果定义域是连通的，即可在对应区间内连续取值  
![a4c5bc2dda9714f66211c0d00768630.png](https://s2.loli.net/2024/10/22/NdgQ9cDe8rXIMiP.png)

## Limit Computations

TIP:
- 考察哪些点的极限有意义：  
**只有对于 Accumulation point 考察该点的极限才有意义**
- 考察哪些点的极限存在：  
**注意如果极限存在，那么一定有对于每个维度从任意方向逼近都能得到相同的结果**

常用手段
- 利用基本不等式进行基础的放缩
- 利用极限语言定义去构造
- 直接构造反例
- 通过在脑中形象

### Example

![d6da4234b3627c965a25ae559b4f0cf.png](https://s2.loli.net/2024/10/22/agBYr4NetkDJKTx.png)  
![8dc2d3b16f025cd60df00eb0a8d8b90.png](https://s2.loli.net/2024/10/22/L1yMdjGeHIEtknf.png)
