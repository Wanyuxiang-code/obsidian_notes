---
title: Phase Space
date: 2025-04-06
date modified: 2025-04-06
categories: Math285
tags:
  - Math285
---

#Math285 

## Autonomous systems and Orbits

### 定义与基本性质
- **1. 自治系统 (Autonomous System)**: 
    
    一个 n 维一阶 ODE 系统被称为 自治的 (autonomous)，如果方程右侧的函数 f 不显式地依赖于自变量 t：
    
    $$
    
    \mathbf{y}' = \mathbf{f}(\mathbf{y})
    
    $$
    
    其中 $\mathbf{y}=(y_{1},\dots ,y_{n})\in \mathbb{R}^{n}$，而 $f:D\to \mathbb{R}^{n}$ 定义在 $\mathbb{R}^{n}$ 的某个区域 D 上。
    
- **2. 时间平移不变性 (Time-Shift Invariance)**: 
    
    自治系统的一个关键特性是：**如果 y(t) 是系统的一个解，那么对于任意常数 c，函数 z(t)=y(t+c) (也就是将原解在时间轴上平移 c) 也是该系统的一个解**。这是因为 z′(t)=y′(t+c)=f(y(t+c))=f(z(t))。
    
- **3. 轨道 (Orbits / Trajectories)**: 
    
    一个解 y(t) 在 相空间 (phase space) $\mathbb{R}^{n}$ 中描绘出的**曲线的 值域 (range) 被称为该解的 轨道 (orbit) 或 轨迹 (trajectory)**。它表示系统状态 y 随时间演化的几何路径，是一个不包含时间参数 t 的点集。

### 唯一性与轨道划分
- **1. 唯一性与轨道划分 (Uniqueness and Partitioning by Orbits)**: 
    
    根据 存在唯一性定理 (Existence and Uniqueness Theorem)，对于满足条件的自治系统 y′=f(y)：
    
    1. 通过相空间中的任何一点 $y_{0}\in D$ ，存在唯一的 **最大解 (maximal solution)** y(t) 满足 $y(t_{0}) = y_{0}$ 。
    2. 两条不同的最大解所对应的轨道，要么完全相同 (这种情况下，两个解函数**彼此之间仅相差一个时间平移**)，要么完全不相交。**轨道永远不会交叉或合并** (除非它们是同一条轨道)。
    3. 因此，所有解的轨道构成了相空间 D 的一个 **划分 (partition)**。每个点都恰好属于一条轨道。
- **2. 平衡点 (Equilibrium Points / Critical Points)**: 
    
    相空间中使得 $f(y_{0})=0$ 的点 $y_{0}$ 被称为 平衡点 (equilibrium point) 或 临界点 (critical point)。
    
    如果 $y_{0}$ 是一个平衡点，那么常数函数  $y(t)\equiv y_{0}$ ​ 就是系统的一个解。这种解对应的轨道仅仅是单个点 $y_{0}$ ​。平衡点代表系统处于静止不变的状态。
    

### Phase Line Analysis
**1. 一维相线分析 (Phase Line Analysis, n=1)** 

当系统是一维时，即 $y'=f(y)$ ，相空间就是一条直线，称为 **相线 (phase line)** (通常就是 y 轴)。

- **作图步骤:**
    
    1. 找出所有平衡点，即方程 f(y)=0 的所有实数根。在相线上标记这些点。
    2. 在相邻平衡点之间的每个区间内，f(y) 的符号是恒定的。
        - 如果 f(y)>0，则 y′(t)>0，解 y(t) 随时间 t 增加而增加。在相线上该区间画一个指向右边的箭头 →。
        - 如果 f(y)<0，则 y′(t)<0，解 y(t) 随时间 t 增加而减少。在相线上该区间画一个指向左边的箭头 ←。 
- **平衡点的稳定性 (Stability of Equilibrium Points)**: 
    
    相线图可以帮助我们判断平衡点 y0​ 的稳定性：
    
    - **渐近稳定 (Asymptotically Stable):** 如果 y0​ 两侧的箭头都指向 y0​ (←y0​→ 是错误的，应该是 →y0​←)。这意味着，如果初始值 y(t0​) 足够接近 y0​，那么解 y(t) 在 t→∞ 时会趋近于 y0​。 graphically: f(y) 在 y0​ 附近从正变为负 (如果 f 可微，通常意味着 f′(y0​)<0)。
    - **不稳定 (Unstable):** 如果 y0​ 两侧的箭头都背离 y0​ (←y0​→)。这意味着，即使初始值非常接近 y0​ (但不等于 y0​)，解 y(t) 最终也会远离 y0​。 graphically: f(y) 在 y0​ 附近从负变为正 (如果 f 可微，通常意味着 f′(y0​)>0)。
    - **半稳定 (Semistable):** 如果 y0​ 一侧的箭头指向 y0​，而另一侧的箭头背离 y0​ (→y0​→ 或 ←y0​←)。 graphically: f(y) 在 y0​ 处变号失败 (如果 f 可微，通常意味着 f′(y0​)=0，并且 y0​ 是一个拐点但非局部极值点)。
    - **稳定 (Stable)** 定义是指：对任意 ϵ>0，存在 δ>0，使得若 ∣y(t0​)−y0​∣<δ，则对所有 t≥t0​ 都有 ∣y(t)−y0​∣<ϵ。渐近稳定是比稳定更强的条件。)
- 例子: Logistic 方程 (Logistic Equation): 
    
    y′=r(1−y/K)y (其中 r,K>0)。
    
    平衡点是 y=0 和 y=K。
    
    f(y) 在 (0,K) 区间为正，在 (K,∞) 和 (−∞,0) 区间为负 (假设 y 代表种群数量，通常只考虑 y≥0)。
    
    相线图显示：y=0 是不稳定的 (←0→)，y=K 是渐近稳定的 (→K←)。
    

**2. 二维相平面分析 (Phase Plane Analysis, n=2)** 

当系统是二维时，即 y′=f(y) 其中 y=(y1​,y2​)，相空间是 **相平面 (phase plane)**。

- 轨道是相平面上的曲线。
    
- 我们可以通过将高阶自治 ODE 转化为一阶系统来应用相平面分析。例如，二阶 ODE y′′=f(y,y′)可以转化为系统：
    
    令 y1​=y, y2​=y′。则 Y=(y1​,y2​) 满足：
    
    $$
    
    \begin{pmatrix} y_1' \ y_2' \end{pmatrix} = \begin{pmatrix} y_2 \ f(y_1, y_2) \end{pmatrix}
    
    $$
    
- 例子: 无阻尼谐振子 (Undamped Harmonic Oscillator):
    
    y′′+y=0。
    
    转化为系统：令 y1​=y, y2​=y′。
    
    $$
    
    \begin{pmatrix} y_1' \ y_2' \end{pmatrix} = \begin{pmatrix} y_2 \ -y_1 \end{pmatrix} = \mathbf{F}(y_1, y_2)
    
    $$
    
    唯一的平衡点是 F(y1​,y2​)=(0,0) 的解，即 (y1​,y2​)=(0,0)。
    
    系统的通解是 y1​(t)=y(t)=Acost+Bsint, y2​(t)=y′(t)=−Asint+Bcost。
    
    计算轨道的方程：
    
    $$
    
    y_1(t)^2 + y_2(t)^2 = (A \cos t + B \sin t)^2 + (-A \sin t + B \cos t)^2 = A^2 + B^2
    
    $$
    
    这说明，对于任意初始条件 (y(0),y′(0))=(A,B)，解对应的状态向量 (y(t),y′(t)) 始终位于以原点为中心、半径为 A2+B2​ 的圆上 。
    
    相平面图由以下轨道组成：
    
    - 原点 (0,0) (平衡点)。
    - 以原点为中心的一系列同心圆。每个圆对应不同的初始能量 A2+B2。 这些轨道构成了整个相平面的划分。箭头方向可以通过计算 F(y1​,y2​) 在某些点（例如坐标轴上的点）的方向来确定，它们指示了在圆上是顺时针还是逆时针运动（在这个例子中，例如在 (1,0) 点，F(1,0)=(0,−1)，表示向下运动，所以是顺时针）。

## Exponential Expansion

设 $A$ 是一个 $2 \times 2$ 的矩阵。
$$
A = \begin{pmatrix} a & b \\ c & d \end{pmatrix}
$$
计算 $e^{At}$ 的核心在于求解 $A$ 的特征值。

**第一步：求解特征值 (Eigenvalues)**

特征值 $\lambda$ 由特征方程 $\det(A - \lambda I) = 0$ 给出：
$$
\det \begin{pmatrix} a - \lambda & b \\ c & d - \lambda \end{pmatrix} = (a - \lambda)(d - \lambda) - bc = 0
$$
展开得到一个关于 $\lambda$ 的二次方程：
$$
\lambda^2 - (a+d)\lambda + (ad-bc) = 0
$$
注意到 $a+d = tr(A)$ (矩阵 $A$ 的迹 Trace) 且 $ad-bc = det(A)$ (矩阵 $A$ 的行列式 Determinant)。所以特征方程是：
$$
\lambda^2 - tr(A) \lambda + det(A) = 0
$$
解这个二次方程，得到两个特征值，记为 $\lambda_1$ 和 $\lambda_2$。

**第二步：根据特征值的不同情况计算 $e^{At}$**

这里有三种主要情况：

**情况 1：两个不同的实数特征值 ($\lambda_1 \neq \lambda_2$, $\lambda_1, \lambda_2 \in \mathbb{R}$)**

当有两个不同的特征值时，矩阵 $A$ 一定是可对角化的。我们可以利用一个基于 **Cayley-Hamilton 定理** (Cayley-Hamilton Theorem) 的思想：任何 $n \times n$ 矩阵 $A$ 都满足其自身的特征方程。对于 $2 \times 2$ 矩阵，这意味着 $(A - \lambda_1 I)(A - \lambda_2 I) = 0$。更进一步地，对于任何解析函数 $f(x)$ (比如 $f(x)=e^{xt}$)，可以将 $f(A)$ 表示为 $A$ 的次数低于 $n$ (这里是低于 2) 的多项式。

即，存在标量系数 $c_0(t)$ 和 $c_1(t)$，使得：
$$
e^{At} = c_0(t) I + c_1(t) A
$$
为了确定这两个系数，我们利用这个关系式对于特征值也必须成立 (可以想象将这个等式作用于特征向量上)：
$$
e^{\lambda t} = c_0(t) + c_1(t) \lambda
$$
将两个不同的特征值 $\lambda_1$ 和 $\lambda_2$ 代入，得到一个线性方程组：
1.  $e^{\lambda_1 t} = c_0(t) + c_1(t) \lambda_1$
2.  $e^{\lambda_2 t} = c_0(t) + c_1(t) \lambda_2$

求解这个关于 $c_0(t)$ 和 $c_1(t)$ 的方程组：
从 (1) - (2)： $e^{\lambda_1 t} - e^{\lambda_2 t} = c_1(t) (\lambda_1 - \lambda_2)$
所以 (因为 $\lambda_1 \neq \lambda_2$)：
$$
c_1(t) = \frac{e^{\lambda_1 t} - e^{\lambda_2 t}}{\lambda_1 - \lambda_2}
$$
将 $c_1(t)$ 代回 (1)： $c_0(t) = e^{\lambda_1 t} - \lambda_1 c_1(t) = e^{\lambda_1 t} - \lambda_1 \frac{e^{\lambda_1 t} - e^{\lambda_2 t}}{\lambda_1 - \lambda_2}$
化简可得：
$$
c_0(t) = \frac{\lambda_1 e^{\lambda_2 t} - \lambda_2 e^{\lambda_1 t}}{\lambda_1 - \lambda_2}
$$
最后，将 $c_0(t)$ 和 $c_1(t)$ 代回 $e^{At} = c_0(t) I + c_1(t) A$：
$$
e^{At} = \frac{\lambda_1 e^{\lambda_2 t} - \lambda_2 e^{\lambda_1 t}}{\lambda_1 - \lambda_2} I + \frac{e^{\lambda_1 t} - e^{\lambda_2 t}}{\lambda_1 - \lambda_2} A
$$
这个公式直接用特征值 $\lambda_1, \lambda_2$ 和矩阵 $A$ 本身来计算 $e^{At}$，避免了显式计算特征向量和矩阵求逆。

*(同样适用于两个不同的复共轭特征值 $\lambda_{1,2} = \alpha \pm i\beta$ 的情况，只是计算会涉及复数指数 $e^{(\alpha \pm i\beta)t} = e^{\alpha t}(\cos(\beta t) \pm i \sin(\beta t))$，但最终结果 $e^{At}$ 仍是实数矩阵)*

**情况 2：一个重根实数特征值 ($\lambda_1 = \lambda_2 = \lambda$)，且 $A$ 是可对角化的**

这种情况非常特殊。如果一个 $2 \times 2$ 矩阵有重根特征值 $\lambda$ 并且是可对角化的，那么它必须已经是**标量矩阵 (Scalar Matrix)** 的形式：
$$
A = \begin{pmatrix} \lambda & 0 \\ 0 & \lambda \end{pmatrix} = \lambda I
$$
在这种极其简单的情况下：
$$
e^{At} = e^{(\lambda I)t} = e^{\lambda t I} = \sum_{k=0}^{\infty} \frac{(\lambda t I)^k}{k!} = \sum_{k=0}^{\infty} \frac{(\lambda t)^k I^k}{k!} = \left( \sum_{k=0}^{\infty} \frac{(\lambda t)^k}{k!} \right) I = e^{\lambda t} I
$$
所以：
$$
e^{At} = \begin{pmatrix} e^{\lambda t} & 0 \\ 0 & e^{\lambda t} \end{pmatrix}
$$

**情况 3：一个重根实数特征值 ($\lambda_1 = \lambda_2 = \lambda$)，但 $A$ 不是可对角化的**

这是当 $A \neq \lambda I$ 但仍然有 $\lambda_1 = \lambda_2 = \lambda$ 时发生的情况。这意味着 $A$ 的若尔当标准型 (Jordan Normal Form) 是 $J = \begin{pmatrix} \lambda & 1 \\ 0 & \lambda \end{pmatrix}$。
我们仍然可以使用 $e^{At} = c_0(t) I + c_1(t) A$ 的形式，但是之前的求解方法因为 $\lambda_1 - \lambda_2 = 0$ 而失效。我们需要一个新的条件。

当存在重根时，不仅 $e^{\lambda t} = c_0(t) + c_1(t) \lambda$ 成立，它的导数（对 $\lambda$ 求导）也应该成立（这与最小多项式有关）：
$$
\frac{d}{d\lambda} (e^{\lambda t}) = \frac{d}{d\lambda} (c_0(t) + c_1(t) \lambda)
$$
计算得到：
$$
t e^{\lambda t} = c_1(t)
$$
现在我们有了两个方程：
1.  $e^{\lambda t} = c_0(t) + c_1(t) \lambda$
2.  $t e^{\lambda t} = c_1(t)$

求解这个简单的系统：
$c_1(t) = t e^{\lambda t}$
$c_0(t) = e^{\lambda t} - \lambda c_1(t) = e^{\lambda t} - \lambda (t e^{\lambda t}) = (1 - \lambda t) e^{\lambda t}$

代回 $e^{At} = c_0(t) I + c_1(t) A$：
$$
e^{At} = (1 - \lambda t) e^{\lambda t} I + t e^{\lambda t} A
$$
这个公式也可以从 $A = P J P^{-1}$ 推导出来。我们知道 $e^{Jt} = e^{\lambda t} \begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix}$。
并且，根据 Cayley-Hamilton 定理，对于这种情况， $(A - \lambda I)^2 = 0$。
我们可以写 $A = \lambda I + (A - \lambda I)$。由于 $\lambda I$ 和 $(A - \lambda I)$ 可交换，
$e^{At} = e^{(\lambda I + (A - \lambda I))t} = e^{\lambda I t} e^{(A - \lambda I)t} = e^{\lambda t} I \cdot e^{(A - \lambda I)t}$
计算 $e^{(A - \lambda I)t}$ 的级数：
$e^{(A - \lambda I)t} = I + (A - \lambda I)t + \frac{((A - \lambda I)t)^2}{2!} + \dots$
由于 $(A - \lambda I)^2 = 0$，所有更高次的项也都是零。
$e^{(A - \lambda I)t} = I + (A - \lambda I)t$
所以，
$e^{At} = e^{\lambda t} (I + (A - \lambda I)t) = e^{\lambda t} I + t e^{\lambda t} (A - \lambda I)$
$e^{At} = e^{\lambda t} I + t e^{\lambda t} A - \lambda t e^{\lambda t} I = (1 - \lambda t)e^{\lambda t} I + t e^{\lambda t} A$
这与我们之前用系数法得到的结果一致。

**总结计算步骤：**

1.  **计算特征值:** 求解 $\lambda^2 - tr(A) \lambda + det(A) = 0$ 得到 $\lambda_1, \lambda_2$。
2.  **判断情况:**
    *   如果 $\lambda_1 \neq \lambda_2$ (不同实数或复共轭)，使用公式：
        $$
        e^{At} = \frac{\lambda_1 e^{\lambda_2 t} - \lambda_2 e^{\lambda_1 t}}{\lambda_1 - \lambda_2} I + \frac{e^{\lambda_1 t} - e^{\lambda_2 t}}{\lambda_1 - \lambda_2} A
        $$
    *   如果 $\lambda_1 = \lambda_2 = \lambda$ 并且 $A = \lambda I$，使用公式：
        $$
        e^{At} = e^{\lambda t} I
        $$
    *   如果 $\lambda_1 = \lambda_2 = \lambda$ 并且 $A \neq \lambda I$，使用公式：
        $$
        e^{At} = (1 - \lambda t)e^{\lambda t} I + t e^{\lambda t} A
        $$
3.  **代入计算:** 将 $\lambda_1, \lambda_2$ (或 $\lambda$) 以及矩阵 $A$ 和单位矩阵 $I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}$ 代入相应的公式，计算最终的 $e^{At}$ 矩阵。

这种方法特别适用于二维情况，因为它避免了复杂的矩阵求逆或寻找广义特征向量的过程，而是直接利用特征值 $\lambda$ 和原始矩阵 $A$ 来构造结果。