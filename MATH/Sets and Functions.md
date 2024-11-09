---
title: Sets and Functions
date: 2024-09-27
date modified: 2024-11-09
categories: Math213
tags:
  - Math213
---
#Math213 

## Sets

### Basic

- **Concept**: A set is an unordered collection of objects. The objects are called elements or members.(强调无序性)
- **Representation**:  
![5f83ecf312bbe59ceb88a9516063239.png](https://s2.loli.net/2024/09/27/pqmDMblFLjGP1dv.png)
- **Subset**:  
![343b4685595384c6820e2df5d6a525e.png](https://s2.loli.net/2024/09/27/5n3HlMWk27u8OoN.png)
- **Size-Carinality 集合的势**  
![2e5215c192361d9ad54ff5f9d50b6f1.png](https://s2.loli.net/2024/09/27/noOcPD3K1bIFSXZ.png)
- **Power Set**: 集合所有子集的集合

### Tuple and Cartesian Product

- Tuple:**Tuple 强调元素的有序性**  
![f6977c25a800ddeabe4fc532ea30dce.png](https://s2.loli.net/2024/09/27/R6j3D7fWJ2TN1C4.png)

- Cartesian Product: **各集合元素的有序组合**  
![a01fc501d518028c7099bc510866d82.png](https://s2.loli.net/2024/09/27/mKxZz7AFbGuRNlk.png)
- Relation: **A subset of of the Cartesian product $A \times B$ is called a relation from the set A to the set B
- **

### Operation

- Union:  
![9316fed1ca6f06c4d93d079e6368deb.png](https://s2.loli.net/2024/09/27/P1CI7dgLwiy2UJn.png)
- Intersection  
![777a1e4fedc984c37cbddcd3905dfd7.png](https://s2.loli.net/2024/09/27/GVMhsS8FJePipoy.png)
- Difference  
![677aa5312aac0e76cfa348e0fd197a3.png](https://s2.loli.net/2024/09/27/1BqlnZsYzycpXrP.png)
- Complement  
![5e7bc02206765601205e3f5289f16da.png](https://s2.loli.net/2024/09/27/LSVEa1kiOzhDBv6.png)

### Identities

![77fbecd60c5911d0c34e5c7f711ceab.png](https://s2.loli.net/2024/09/27/PAmbp45Vytawg6X.png)  
![9ed865c5859bce3020dcac748d5920e.png](https://s2.loli.net/2024/09/27/VFnDAf3PSqUuKJL.png)  
![fcc24455dca4f899efe4cdb25ceb66b.png](https://s2.loli.net/2024/09/27/eQcotEaIzACJ15b.png)

## Function

### Basic

- **Concept**  
![a72dd7eb3c5963abc01c8bc8a91011c.png](https://s2.loli.net/2024/09/27/uZl7sqnwY59EbXe.png)  
domain: 定义域  
codomain: 上域  
range：值域  
$f(a)=b$: a 为 preimage, b 为 image
- **Type**
1. injective: 单射函数，不同的像对应不同的原像  
**one-to-one**  
![ec253a79a29017fa8145b47957b9b95.png](https://s2.loli.net/2024/09/27/N5U8j4FotGJW2eX.png)
2. Surjective: 满射函数，对任意的像都有原像与之对应  
即陪域中每个元素都被覆盖  
**onto**  
![a40c9e25f3ced05f54667f940291ff3.png](https://s2.loli.net/2024/09/27/6bjrBXKZqfGPVuC.png)
3. Bijective: 双射函数，既为单射又为满射  
**one-to-one correspondence**  
![5618eff0519eaaa9e656e1d26106ac2.png](https://s2.loli.net/2024/09/27/HN3jvUSqLWybXGR.png)  
**证明 Bijective Function: 证明单射和满射即可**

![c44a9da43b9349ded1c5ce5c9523068.png](https://s2.loli.net/2024/09/29/i4F3Xxa69GY1D5V.png)

4. Inverse Function  
![45e6e3184f15c0a73ea9134cf41975a.png](https://s2.loli.net/2024/09/29/tPMZHeRbjTLi2Xo.png)

### Composition of Functions

**Concept**  
![738f3aa9300d49fd8d4e3bee25693be.png](https://s2.loli.net/2024/09/29/KusyGnd43ZhVFBo.png)

**对于双射，映射及其逆映射的复合即为 Identity Function**  
![ff195719aaf95196e211096d1491bb1.png](https://s2.loli.net/2024/09/29/yN3xd7SlEeQmIzr.png)

### Special Function

- Floor and Ceiling Function
- Factorial Function

### Sequence

**Definition**  
![b05311c96a40f2e7ece143e8a16bf39.png](https://s2.loli.net/2024/09/29/RQ9ikBemGaFCz1s.png)  
还可利用递归形式定义  
![efae723fb4fdaa39b71075ffa72dea2.png](https://s2.loli.net/2024/09/29/Th2odCGf8VuOaLy.png)  
确定初始项，然后即可根据后项与前项之间的关系定义

**Common Types**
- Geometric Progression: 等比
- Arithmetic Progression: 等差

## Cardinality

### Countable

The elements of the set can be **enumerated** and listed  
![376caa6de6f2aa9006e9a1e678a2120.png](https://s2.loli.net/2024/09/29/stbpRZQqHvEUghy.png)  
考察集合的势与正整数集势的关系  
![255eac2b42d769445cc1162e039075c.png](https://s2.loli.net/2024/09/29/D8GLj6p1RVOsTMq.png)


**Core: check one-to-one correspondence 或者寻找一种合理的排列方式**

**Notice**: 正有理数集可数，考虑控制分子分母的和，然后逐项列举  
![1d7a6864b584b7bbc24926ed1308649.png](https://s2.loli.net/2024/10/11/NnYjMd2HLVZDJ3v.png)  
![17191638b8c4149e7f04443601c764d.png](https://s2.loli.net/2024/10/11/qnd7sB2VUNQrzoE.png)

**注意有理数集，代数集可数**

### Uncountable Set

$\mathbb{R}$ ,   $(0,1)$ 不可数，康托尔对角线  
![23bcf85deb072e9b08cb5c97164b908.png](https://s2.loli.net/2024/10/11/5SmIal9tqkgcyzw.png)

**证明集合的势相等**：考虑构造两者相互的 one-to-one correspondence  
![c33820f9a8b3d37b9a49ee7f258ee8a.png](https://s2.loli.net/2024/10/11/Fnw5P8TvlHBZ7AV.png)

### Computable

![13bf3939680722c446c2efd47571aa0.png](https://s2.loli.net/2024/10/11/cZ1zJgn2bKP4oep.png)

P: 表示 Power set,即集合所有子集构成的集合