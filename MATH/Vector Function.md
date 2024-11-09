---
title: Vector Function
date: 2024-09-19
date modified: 2024-11-09
categories: Math241
tags:
  - Math241
---
#Math241 

## Vector-valued function

### Basic

#### Definition

vector-valued function, or vector function, is simply a function whose  
**domain is a set of real numbers and whose range is a set of vectors**  
即将 $\mathbb{R}\to \mathbb{R}^{n}$  
![810962263527548f219130fb4a8907f.png](https://s2.loli.net/2024/09/24/IMSPYQ8p1vngRDa.png)

#### Parametric Curve & Non-Parametric Curve

**Parametric Cruve**  
![a21991924ed973b180494d747e5fdfc.png](https://s2.loli.net/2024/09/24/hOulmC6p98YtdzE.png)  
将非参数的曲线转化为参数化的曲线  
Example:  
![31cabc0dabf1bd697468563a56c928e.png](https://s2.loli.net/2024/09/24/PWSpVjk2oylnLJw.png)

**注意：一个非参数的曲线可以有多种参数化的表示**  
**Closed Parametric Curve**:  
![09db6bc7feac1418c4141f7b37e79da.png](https://s2.loli.net/2024/09/24/B8sZFQIRTc1j6En.png)

## Limits and Continuity

### Basic Term

**Notation**  
![43f23adb861fcb226012ab53f810c19.png](https://s2.loli.net/2024/09/24/muI2RibO19wntXd.png)  
![0b1a8dd80bf70db6e0689c388c14198.png](https://s2.loli.net/2024/09/26/JlFc8y3e7OjC6PB.png)



![b5f07ec4816f6ca2d23698b866ef989.png](https://s2.loli.net/2024/09/26/7cLCIJaWOFrjG2Q.png)
- **interior point**：内点，即考虑以 a 为中心的小球包含在一个三维子域中,D 记为其邻域
- **boundary point**: 边界点，即以 a 的为中心的球一定包括三维域内与域外的点
- **limit point**: 三维域内存在序列极限趋于 a(注意 D 内的点一定是极限点，同时包含其边界)
- **accumulation point**: 即 a 点周围稠密（任意取一个小球都能包含 D 中其他一个点）


![4fbf9dc58855fc6af3ec3c889c19d31.png](https://s2.loli.net/2024/09/26/1DLulQXsSRIfwox.png)

![9b01d3164b080f6551b79ef86d11745.png](https://s2.loli.net/2024/09/26/UdGfBEJ1aSqo7vX.png)

![e537797cdbb8504869418261a4a5594.png](https://s2.loli.net/2024/10/15/gawI3AN8ZTzCOsm.png)

### Concept

- **无穷点序列的极限 Limit of a Sequence**  
即序列中的所有点收敛到空间中一个点（利用球的半径去刻画极限），或者即对向量的任何一个分量都在该点出有极限

一旦确定收敛，极限便唯一确定  
![4bedb2f93f05109f248db26eb32c378.png](https://s2.loli.net/2024/09/26/GgKHxoMtv12JlA5.png)

- **曲线的极限与连续性 Limits and Continuity for Curves**  
![593aa2310b72095080bfb312ab93ebc.png](https://s2.loli.net/2024/09/26/kOosStJhWjLRZnf.png)

极限：外层向量函数的极限等于各内层维数上函数分别趋近

$$
\lim_{ t \to a } r(t)= <\lim_{ t \to a } f(t),\lim_{ t \to a } g(t),\lim_{ t \to a }h(t)>
$$

连续性: 即对任意一个内层函数都在 a 处收敛

$$
\lim_{ t \to a } r(t) = r(a)
$$

- **考虑在现实中的泛化定义**（考虑非标准化的基与原点的平移）  
![7dc5c84372126b28f72f510e2c10a57.png](https://s2.loli.net/2024/09/26/vX3c4pb7RszOkhw.png)

*证明直接考虑用矩阵表示线性变换，然后即可将原空间中的基转化为标准基，然后直接将对应的极限加和即可*

## Differentiation and Integration

### Differentiation

#### Concept

- 定义  
**与之前极限的定义类似，只要每个分量上对应的函数可导即可；对于换底 + 平移后的空间同样适用**  
![a0c499745a46594a69f676d5d7c2d7a.png](https://s2.loli.net/2024/09/26/iOvuK3TFe8ZY5GA.png)
- 切线  
**即切点加对应导数确定方向构成的直线**  
![daac52538b3be430cb9aaea59eb2ebf.png](https://s2.loli.net/2024/09/26/hFVNTptc8DP712W.png)

#### Differentiation Rules

![51f489d4397de5e2faba5a8e37e9636.png](https://s2.loli.net/2024/09/26/Er2qT4mBlyfZbSi.png)  
![7a3df36d74f181a10adb35dc610890d.png](https://s2.loli.net/2024/09/26/4MvaC1VwNGsd8lq.png)

Proof:  
![f927fc99f0f32cebc6ab6378e39103e.png](https://s2.loli.net/2024/09/26/qEDRmxu1l3tehJI.png)

当曲线的模长为定值时, $r'(t)$ 总与 $r(t)$ 正交

![22d2aa01fc33a7aaaf59e4595789d57.png](https://s2.loli.net/2024/09/26/JwNkBaqAG7prfF8.png)

**注意对曲线模的求导**：

$$
|r(t)|'|r(t)|=r(t)\cdot r'(t)
$$

且我们有 $\frac{d}{dt} \frac{r(t)}{|r(t)|}$ 与 $r(t)$ 垂直

### Integration

![3067c0bb88d6e3db66493e7a1f12bfb.png](https://s2.loli.net/2024/09/26/dwsKrziS1u7LDOn.png)

## Arc Length

### Definition

**关注 Slides 上关于 Arc Length 基于任意划分区间计算得到的最小上界/对划分区间取极限所得到的两种定义**

计算曲线长度的公式  
![16b94d7b6d60a656977701f40121faa.png](https://s2.loli.net/2024/10/08/vPmEc32lbpxH8L4.png)  
只要曲线为 $C^{1}-curve$（在闭集上连续可导） ,即可直接从导数的模长积分得到最终的曲线长度

**Piece-wise $C^{1}-Curves$**: 即将每一段可以直接用的 $C^{1}-Curve$ 直接积起来即可 

![84756b959406691303c3cb6ab08060d.png](https://s2.loli.net/2024/10/08/k9F3TZfuULptC4q.png)

**注意，对于这样的曲线需要满足在整个区间上连续，并且在断点处两边的单侧极限相等**  
![1e834ad2f1c090cac49555c90e9f314.png](https://s2.loli.net/2024/10/08/Ec6xkYO3eugsfBA.png)



![7447e2716859614b14c11af92a44fd5.png](https://s2.loli.net/2024/09/26/WiGMa9JDeOPQB5L.png)  
**Arc Length Function**  
![eecb39c8bfcaaadfeaec03e0186b1e3.png](https://s2.loli.net/2024/09/26/L65lERPDxq9Ceid.png)

**注意：以曲线长度对曲线进行参数化**：
- 可以先考虑积分表示曲线长度函数，然后根据结果合理换元
- 见 Worksheet4

### Uniform Continuity 一致连续

**Definition**  
![a352f610cc4e2a21e3ce4000cec66f7.png](https://s2.loli.net/2024/10/08/MRH5Lt8rjqEcmaI.png)  
**核心即为确定对于曲线上任意的点，我们可以找一个不取决于具体点的最小 $\Delta$ ,即可控制任意逼近**

![a4e555c58ee761a413baa5351037674.png](https://s2.loli.net/2024/10/08/PFf6ELeYM9aQN83.png)  
连续 + 紧集 ->一致连续

### Parametrization with Respect to Arc Length

![9c759cc6618aa5f80783ac140f38176.png](https://s2.loli.net/2024/10/10/1vcn5lrPM6xKwb3.png)

**核心即为对 Arc Length 积分后通过换元，使得基本的元表示单位曲线的长度**  
->基于此，我们容易得到其导数为单位向量（结合反函数的性质以及曲线长度函数的定义即可）

![5a1c59aa97ff7d3103c5f89afcde403.png](https://s2.loli.net/2024/10/10/vZlSwROorU8ygGA.png)

## Curvature 曲率

**Smooth Curve 定义：在定义域上 $r'(t)$ 存在且不为零

对于一个由 $r(t)$ 定义的光滑的曲线，单位切线向量即为：

$$
T(t) = \frac{r'(t)}{|r'(t)|}
$$

**利用切线单位向量与单位曲线长度的比值的模长来衡量曲线方向变化的速率 ->即为曲率**

![ffdc4c52c8ddf1fc63e39dec897ef31.png](https://s2.loli.net/2024/09/26/phPeK9DX2RSIq3a.png)  
![971618d75138679955ec2128f741ec2.png](https://s2.loli.net/2024/09/26/tViLDdPBqM8SFNK.png)  
![57e02a920b0bd9f068f6a3a4d448914.png](https://s2.loli.net/2024/09/26/6XoROmqcwMyjJ5n.png)

对于特殊的由 $y=f(x)$ 表示的曲线，我们有  
![247c18c3c88d54d5ec354a8f9b6e1bc.png](https://s2.loli.net/2024/10/09/rbkjM64eATOQv1y.png)

### Normal and Binormal Vectors

#### Vectors

- **定义 $T(t)$ 的单位法向量**  
**由 $T(t)$ 的模长恒为定值，我们容易得到 $T'(t)$ 与其正交**
1. **再由两者叉乘得到第三个法向量 $B(t)$**
2. **注意为避免计算的复杂性, $N(t)$ 与 $T(t)$ 可直接利用对 $r(t)$ 求一二阶导得到其对应的方向**  
![b1ecff5bf79b56089902125a93fa07e.png](https://s2.loli.net/2024/09/26/znftkjIHmPaex14.png)

还可以利用正交化的方法分别计算 T(t) 与 N(t),**即考虑正交化 $f'(t)$ 与 $f''(t)$**

![d36f3ba7ebea8fa3e3e1e40917fd424.png](https://s2.loli.net/2024/10/10/ZMSocUikD3I6quL.png)

**利用取二阶导并减去其在一阶导上的投影得到，避免复杂计算与求导**

#### Planes

- **Taylor's Formula for Curves**

![da2a7fd9e5d72b2f9c2c7dd3219f2c1.png](https://s2.loli.net/2024/10/10/wsqavtPZMUWxCDK.png)
- **Big-O and Little-o Notation**  
大 O 表示两者关系为常数，小 o 表示可以在此量级上任意小  
![d79722479475c7b4fd1a680ff151d87.png](https://s2.loli.net/2024/10/10/EhzlxLFIweuGgQY.png)




- **Normal Plane**  
由 Normal Vector 与 Binormal Vector 决定的平面,法向量即为单位切线向量
- **Osculating Plane** 摆动平面  
由 T 与 N 确定的平面，法向量为 Binormal Vector

![ed4d2b37fb21a5724cabd0d5ee1b86b.png](https://s2.loli.net/2024/10/10/NkU78hovEFHOr9R.png)

![e3f886e8e520d920228e3975b9fd172.png](https://s2.loli.net/2024/10/09/gINGJrYDdqAwyVE.png)
- **Center of Curvature and Osculating Circles**  
经过曲线上一点，半径为 $\frac{1}{\kappa}$,距点 P 方向即为 N
- **Evolute**: the movement of the center of the osculating circle

$$
e(t) = f(t) + \frac{1}{\kappa(t)}N(t)
$$

![64d06897bc5c2df3316521070871168.png](https://s2.loli.net/2024/10/09/rBju6cl45bqziQT.png)  
![4ead33b13b4d7a8a4e6719bc71114bc.png](https://s2.loli.net/2024/10/12/lhIAbYX7BSrE1no.png)  
**当空间曲线本身位于一个平面内时，其摆动平面即为其所位于的平面**

![3c95a1b6fcf35c6aaef3384723a9f05.png](https://s2.loli.net/2024/10/12/mvOLtV7qcI34RfK.png)

**注意：可以用曲率最值判断何为空间中曲线的顶点**  
Example:  
Find the vertex of parabola $(1+t,1+t^{2},t+t^{2})$ in $\mathbb{R}^{3}$



**总结**  
![ed41bcd24aff0ce32561a3b458b6b4a.png](https://s2.loli.net/2024/10/09/Pu5stycFGCql2Ab.png)

### Torsion

![f58b3ab4aa01d69fcce832cb061baf5.png](https://s2.loli.net/2024/10/09/Cew7PhTtpi9ZaNd.png)  
![8ee932199b39bc915dcdccb2aff0d0e.png](https://s2.loli.net/2024/10/09/nwotCjgcGTkUP48.png)  
![e6043a8f7ecf03d9f1538bbf9ef7772.png](https://s2.loli.net/2024/10/09/xwlMnB6a23hHC5W.png)

**当以曲线的弧长参数化时，我们有**  
![c287d37858708d81d7fdd8fea77099b.png](https://s2.loli.net/2024/10/09/bhwOrcSoVY5zKTB.png)



