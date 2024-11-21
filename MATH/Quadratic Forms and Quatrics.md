#Math241 
## Quadratic Forms
### Concept
- **二次型与正定矩阵**

![9a81f218cfd35fb4b441a36f0c82bcb.png](https://s2.loli.net/2024/11/21/57BHt3o8Qh2JmNv.png)

- **Coordinate Change**

![211b82adc2ca86ec5fa4366091494ea.png](https://s2.loli.net/2024/11/21/wV7UKQuljNrnbvp.png)

- **等价二次型->能够通过引入一个可逆的线性变换矩阵在两个二次型对应的矩阵之间进行转化**

![7dcdc020723e93ef1ce47332236c7e8.png](https://s2.loli.net/2024/11/21/ZqsDEURCAef692X.png)
$$
B = S^{T}AS
$$

### Theorem
![491b664c74be26ca5d129aa7d24e6bb.png](https://s2.loli.net/2024/11/21/TioxltHPcbkpOgL.png)

**核心为任意一个二次型可以经过可逆矩阵的转化得到正则态->消除交叉项**

**Observation**
- SYLVESTER's Inertia Theorem意味着任何一个表示二次型的矩阵都可以被变换为如下的对角阵
$$
\begin{pmatrix}
I_{r} & & \\
 &-I_{s}   \\
& & 0_{t}
\end{pmatrix}
$$
- 可以通过其正则形式轻松确定二次型对应的矩阵是否正定


## Quadrics and their Classification
### Definition
![e0e31b736d21508e9cb0a679a0c870b.png](https://s2.loli.net/2024/11/21/mkrJ3XFHU7f6ELe.png)
Quadric（二次曲面）即为n维二次实系数多项式对应的Level Surface


**Example**
- $\mathbb{R}^{n}$ 中任意的仿射空间为Quadric
- $\mathbb{R}^{3}$ 中两个独立的平面也可以构成二次曲面
-  $\mathbb{R}^{3}$ 中的二次曲面可以由 $\mathbb{R}^{2}$ 中的圆锥曲线变化得到
![1cb8623aa4f5f29a9a50acc73c18056.png](https://s2.loli.net/2024/11/21/z2GYOq6lWfIdKSw.png)

**General Quadric**
![de9421ba4d7bbb912f170505d5a72c0.png](https://s2.loli.net/2024/11/21/Is4pvrVD83hHPqx.png)
