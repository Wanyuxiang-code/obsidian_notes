---
title: Applications to Physics
date: 2024-10-12
date modified: 2024-11-09
categories: unlabeled
tags: [Math241]
---
#Math241 

## Coordinate Systems

### Setup

通过 Linear Mapping 换系：一个正交矩阵用来替换正交基，一个平移向量确定原点  
![769655e7b541359fba91f848f438e2e.png](https://s2.loli.net/2024/10/12/Kn52UwLqeWlykhI.png)  
**正交矩阵的基本性质**
- 模长不变

$$
|Ux| = |x|
$$

意味该变换能够保持距离不变

$$
d(x,y) = |x-y| = |Ux'-Uy'|= |x'-y'|
$$

- $U、U^{T}$

$$
UU^{T} = I_{n}
$$

- $\det(U)=\pm1$


![f0982f8b912b4d9d5a4f02865bc62c5.png](https://s2.loli.net/2024/10/12/8VazGFCImXq52oO.png)

## Motion in Space: Velocity and Acceleration

### Velocity, Speed and Acceleration

**注意速度、速率与加速度取决于对曲线参数的选取，而曲率、曲线长度、转矩则独立于曲线参数的选取**
- Velocity: 直接考虑对点的运动轨迹求导，即可得出运动的顺势速度（包括方向与大小）  
![7e94260223cb37124542c1e910fec1f.png](https://s2.loli.net/2024/10/09/p9rt738ixEfPjAJ.png)
- Speed: 即为速度向量的模长

$$
|v(t)|=|r'(t)|=\frac{ds}{dt}
$$

- Acceleration

$$
a(t)=v'(t)=r''(t)
$$

- 联系：牛顿运动定律： $F(t)=ma(t)$  
![e223cdd16b41098b2ed10c486fb04e4.png](https://s2.loli.net/2024/10/09/PMFlAcwyRh96ndu.png)
- Projectile Motion 抛体运动 (**考虑物理方法即可**)

#### Example

### Tangential and Normal Components of Acceleration

$$
\begin{align}
& T(t) = \frac{r'(t)}{|r(t)|} = \frac{\mathrm{v}}{v}  \\
& a = \mathrm{v}' = (vT)' = v'T + vT' \\
& \kappa = \frac{|T'|}{|r'|} = \frac{|T'|}{v}, T'=|T'|N=\kappa vN \\
& a = v'T + \kappa v^{2}N  \\
& a = a_{T}T+ a_{N}N, a_{T}=v', a_{N}=\kappa v^{2}
\end{align}
$$

其中: 可以分别利用点乘计算相应的系数（对于 T，N 的便捷计算则可以参考先后求一二阶导后考虑正交化）

$$
\begin{align}
& a_{T}=v'=\frac{\mathrm{v}\cdot a}{v}=  \frac{r'(t)\cdot r''(t)}{|r'(t)|}  \\
& a_{N} = \kappa v^{2}= \frac{|r'(t)\times r''(t)|}{|r'(t)|}
\end{align}
$$

### Polar form of Conics(圆锥曲线的极坐标形式)

**二次型**  
![0839f17a025c0464452e15e148823fa.png](https://s2.loli.net/2024/10/14/4cjSMmVA9aITvQ7.png)  
![8779e33b90ed621cbf11659554d8a91.png](https://s2.loli.net/2024/10/14/8i3G5NsQUqfMcaw.png)

**极坐标形式**：非退化的二次曲线到焦点与到准线的距离之比为定值  
![d7d48dd9377efb3ce5af7f92126df97.png](https://s2.loli.net/2024/10/14/Pjwf5Q6qUC4Livz.png)
- 离心率 $e =\frac{\sqrt{ a^{2}\mp b^{2} }}{a}$
- 焦准距
- 半通径 $e=\frac{l}{p}$  
![219e591ab915306a2d433d3351d76b9.png](https://s2.loli.net/2024/10/14/kR1zV4e9NGuD6MT.png)

### Kepler's Laws of Planetary Motion 开普勒行星运动定律

![6c2e69687998e91ee72e69f2526d301.png](https://s2.loli.net/2024/10/14/E5LRcia9npXzjyv.png)  
**证明**
- 首先证明行星的运动轨迹为平面  
r 与 a 的叉乘为 0 -> 角加速度为 0  ->角动量为定值  
这样我们即可得到该运动轨迹所对应确定平面的角动量  
![b2c1abcd104aad4fef3e972ea34a6af.png](https://s2.loli.net/2024/10/15/Mb7T4HWNJXus3rz.png)  
![94be178adef7a6bb5054cd6451dae72.png](https://s2.loli.net/2024/10/15/9advEzU2m5NFYMt.png)

![59dc1518bccec9f2108ce5e02051f30.png](https://s2.loli.net/2024/10/15/IlUBvOsnFVmfb1W.png)

![e080791fc97d36c85238f28920c00f6.png](https://s2.loli.net/2024/10/15/PpWsabDOlvcAQNw.png)

**注意 e 与 l 的取值**

$$
e = \frac{c}{GM} , l = \frac{h^{2}}{GM}
$$

![abaa00787c053c052b4a0e39406fcd9.png](https://s2.loli.net/2024/10/15/u9lmZwn7XHNL6Gv.png)  
![17fe287f446c1bc1cf4cff0778ba3a4.png](https://s2.loli.net/2024/10/15/5QjwMs2uzf6eWIp.png)
