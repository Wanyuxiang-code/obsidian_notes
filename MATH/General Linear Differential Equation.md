---
title: General Linear Differential Equation
date: 2025-04-17
date modified: 2025-04-17
categories: Math285
tags:
  - Math285
---

#Math285 


## 概述 (Overview)


这部分课程的核心是处理**线性常微分方程 (Linear Ordinary Differential Equations, Linear ODE's)** 及其系统，特别是当系数可能是**时变 (time-dependent)** 的情况。

-   **主要挑战**: 对于系数依赖于时间 $t$ 的齐次线性 ODE (homogeneous linear ODE)，通常**没有**通用的方法来直接计算其**基本解组 (fundamental system of solutions)**。
-   **解决方法**:
    -   对于**非齐次 ODE (inhomogeneous ODE)**，如果我们已知对应齐次方程的基本解组，可以使用**参数变易法 (variation of parameters)** 来求特解 (particular solution)，进而得到通解 (general solution)。
    -   我们将首先详细讨论**一阶线性 ODE 系统 (1st-order linear ODE systems)**，包括解的存在性和唯一性定理 (Existence and Uniqueness Theorem) 的加强版以及解的线性代数结构 (Linear Algebra aspects)。
    -   接着，引入**矩阵指数函数 (matrix exponential function)** $A \to e^A$，这是一个强大的工具，用于**完全解决**系数**不依赖**于时间的齐次线性系统 $y' = Ay$。我们可以通过矩阵函数 $t \mapsto e^{At}$ 得到解。
    -   然后，利用**降阶法 (order reduction)** 将高阶标量线性 ODE (higher-order scalar linear ODE) 转化为一阶系统，从而应用前面的理论。
-   **二阶 ODE 重点**:
    -   我们将更深入地探讨时变线性二阶 ODE。
    -   讨论 3 个经典的例子 (Legendre, Hermite, Laguerre)，它们有特殊的**多项式解 (polynomial solution)**。
    -   介绍一种通用方法：已知一个非零解时，如何通过**降阶法**找到第二个线性无关解，从而构成基本解组。
    -   最后讨论**欧拉方程 (Euler equations)**，这类方程在后续通过级数解法 (series solutions) 求解线性二阶 ODE 时很重要 


## 一般线性微分方程 (General Linear Differential Equations)

### 一阶线性系统 (First-Order Linear Systems)

#### 定义 


一个 (可能时变的) 一阶线性 ODE 系统具有以下形式：
$$
\mathbf{y'}= A(t)\mathbf{y} + b(t) \quad (\text{LS})
$$
其中：
-   $t$ 属于某个区间 $I \subseteq \mathbb{R}$ ($I$ 不是空集或单点集)。
-   $A: I \to \mathbb{C}^{n \times n}$, $t \mapsto A(t) = (a_{ij}(t))$ 是 $n \times n$ 的矩阵函数。
-   $b: I \to \mathbb{C}^n$, $t \mapsto b(t) = (b_i(t))$ 是 $n$ 维向量函数。
-   $A(t)$ 和 $b(t)$ 的所有分量函数在 $I$ 上都是**连续的 (continuous)**。
-   $y: J \to \mathbb{C}^n$ ($J \subseteq I$ 是子区间) 是一个可微的**解 (solution)**，如果对于所有 $t \in J$，满足 $y'(t) = A(t)y(t) + b(t)$。

**Term**:
-   如果 $b(t) \equiv 0$，系统称为**齐次的 (homogeneous)**。
-   否则，称为**非齐次的 (inhomogeneous)**。

#### 解的存在唯一性 (Existence and Uniqueness of Solutions)


-   对于函数 $f(t, y) = A(t)y + b(t)$，如果我们把 $t$ 限制在 $I$ 的任意**紧子区间 (compact subinterval)**（闭合且有界）上，那么$A(t)$ 的**范数 $||A(t)||$ 有界**，设界为 $L$。此时，对于任意 $y_1, y_2 \in \mathbb{C}^n$，有：
    $$
    |f(t, y_1) - f(t, y_2)| = |A(t)(y_1 - y_2)| \le ||A(t)|| |y_1 - y_2| \le L |y_1 - y_2|
    $$
    这表明 $f(t, y)$ 关于 $y$ 满足**局部 Lipschitz 条件 (local Lipschitz condition)**。因此，标准的**存在唯一性定理 (Existence and Uniqueness Theorem, EUT)** 适用于这类系统，保证了任何初值问题 (Initial Value Problem, IVP) $y' = A(t)y + b(t), y(t_0) = y_0$ ($t_0 \in I, y_0 \in \mathbb{C}^n$) 至少在 $t_0$ 的一个小邻域内存在唯一的解。

-    **定理 (更强的结论)**: 对于**线性**系统，IVP 的解不仅局部存在唯一，而且在**整个区间 $I$ 上都存在且唯一**。这与非线性情况形成对比 (例如 $y'=y^2$, 其解 $y=1/(C-x)$ 可能在有限时间内 "爆炸" blow up)。
-   **证明思路 (Proof Sketch - Picard-Lindelöf Iteration)**:
    1.  构造 **Picard 迭代序列 (Picard-Lindelöf iterates)**:
        $y_0(t) = y_0$ (常数向量)
        $$
        y_k(t) = y_0 + \int_{t_0}^t (A(s)y_{k-1}(s) + b(s)) ds, \quad k = 1, 2, 3, \dots
        $$

    2.  在紧子区间 $J = [a, b]$ 上 ($t_0 \in J$)，利用 $||A(t)|| \le L$，通过数学归纳法 (mathematical induction) 证明相邻迭代项之差的范数满足：
        $$
        |y_{k+1}(t) - y_k(t)| \le K \frac{(L|t-t_0|)^k}{k!}
        $$
        其中 $K$ 是 $|y_1(t)-y_0|$ 在 $J$ 上的一个界。
    3.  这表明函数项级数 $\sum_{k=0}^\infty (y_{k+1}(t) - y_k(t))$ 的各项范数可以被收敛的数值级数 $\sum K \frac{(L(b-a))^k}{k!} = K e^{L(b-a)}$ 控制 (绝对且一致地)。
    4.  根据 **Weierstrass M-判别法 (Weierstrass M-test)**，函数序列 $(y_k(t))$ 在 $J$ 上**一致收敛 (converges uniformly)** 到一个极限函数 $y_\infty(t)$。
    5.  由于一致收敛，极限函数 $y_\infty(t)$ 在 $J$ 上是**连续的 (continuous)**，并且满足积分方程：
        $$
        y_\infty(t) = y_0 + \int_{t_0}^t (A(s)y_\infty(s) + b(s)) ds
        $$
    6.  根据**微积分基本定理 (Fundamental Theorem of Calculus)**，对上式求导，得到 $y_\infty'(t) = A(t)y_\infty(t) + b(t)$，且 $y_\infty(t_0)=y_0$。因此 $y_\infty(t)$ 是 IVP 在 $J$ 上的解。
    7.  由于任何区间 $I$ 都可以被递增的紧子区间序列 $J_m = [a_m, b_m]$ (例如 $J_1 \subseteq J_2 \subseteq \dots$ 且 $\cup J_m = I$) 所穷尽 (exhausted)，因此解 $y_\infty(t)$ 可以在整个 $I$ 上定义。唯一性则来自标准的 EUT 证明 (Gronwall 不等式)。
-   **(Slide 11) 非线性情况的区别**: 对于 $y'=y^2, y(0)=1$，Picard 迭代得到的多项式序列 $\phi_k(t)$ 在 $t \ge 1$ 时发散，这与解 $y=1/(1-t)$ 在 $t=1$ 处 blow up 的行为一致。线性系统的系数 $A(t)$ 提供了足够的控制，防止了这种 blow-up。

#### 解的线性代数结构 (The Link with Linear Algebra)


-   **(Slide 12) 定理**: 考虑**齐次系统 (homogeneous system)** $y' = A(t)y$。
    -   它的所有解构成一个向量空间 (vector space)，记为 $V$。这是因为解的线性组合仍然是解 (叠加原理 Principle of Superposition)。
    -   这个解空间 $V$ 的维数 (dimension) 是 $n$ (在 $\mathbb{C}$ 上，如果 $A(t)$ 和 $y$ 是复数的；在 $\mathbb{R}$ 上，如果 $A(t)$ 和 $y$ 是实数的)。
    -   对于 $k$ 个解 $y_1, \dots, y_k: I \to \mathbb{C}^n$，以下**三条等价**：
        1.  函数 $y_1, \dots, y_k$ 在函数空间 $(C^n)^I$ 中是**线性无关的 (linearly independent)**。
        2.  **存在某个** $t_0 \in I$，使得向量 $y_1(t_0), \dots, y_k(t_0)$ 在 $\mathbb{C}^n$ 中是线性无关的。
        3.  **对于所有** $t_{0} \in I$，向量 $y_1(t_0), \dots, y_k(t_0)$ 在 $\mathbb{C}^n$ 中都是线性无关的。
-   **(Slide 13) 证明思路**:
    -   证明 $V$ 是向量空间：已在定理中说明 (解的和、标量倍数仍是解)。
    -   证明等价性：(3) $\implies$ (2) $\implies$ (1) 是明显的。(1) $\implies$ (3) 是关键：假设函数 $y_1, \dots, y_k$ 线性无关，但在某个 $t_0$ 时向量 $y_1(t_0), \dots, y_k(t_0)$ 线性相关，即存在不全为零的 $c_i$ 使得 $\sum c_i y_i(t_0) = 0$。考虑函数 $y(t) = \sum c_i y_i(t)$，它也是 $y'=A(t)y$ 的解，并且 $y(t_0)=0$。同时，$y_{zero}(t) \equiv 0$ 也是一个解且 $y_{zero}(t_0)=0$。根据 EUT 的唯一性，必须有 $y(t) \equiv 0$ 在整个 $I$ 上成立，即 $\sum c_i y_i(t) = 0$。但这与 $y_1, \dots, y_k$ 作为函数线性无关的假设矛盾。因此 (1) $\implies$ (3) 成立。
    -   证明维数是 $n$：固定 $t_0 \in I$，考虑**求值映射 (evaluation map)** $E_{t_0}: V \to \mathbb{C}^n$，定义为 $E_{t_0}(y) = y(t_0)$。
        -   $E_{t_0}$ 是线性的 (因为 $y_1(t_0)+y_2(t_0)=(y_1+y_2)(t_0)$ 等)。
        -   $E_{t_0}$ 是**单射 (injective)** (根据 (1) $\implies$ (2)，如果 $y(t_0)=0$，则 $y \equiv 0$，核空间只有零向量)。
        -   $E_{t_0}$ 是**满射 (surjective)** (根据 EUT，对于任意 $y_0 \in \mathbb{C}^n$，都存在解 $y \in V$ 使得 $y(t_0)=y_0$)。
        -   因此，$E_{t_0}$ 是一个**向量空间同构 (vector space isomorphism)**，这意味着 $\dim V = \dim \mathbb{C}^n = n$。
-   **(Slide 14) 重要概念**:
    -   **基本解组 (Fundamental System of Solutions)**: 解空间 $V$ 的一组基 (basis) $\{y_1, \dots, y_n\}$。
    -   **基础矩阵 (Fundamental Matrix)** $\Phi(t)$: 一个 $n \times n$ 矩阵，其列 (columns) 由一个基本解组构成，即 $\Phi(t) = [y_1(t) | \dots | y_n(t)]$。
    -   **测试**: 函数组 $\{y_1, \dots, y_n\}$ 构成基本解组 $\iff$ 对应的矩阵 $\Phi(t_0)$ 在**某个** (等价于，**所有**) $t_0 \in I$ 是**可逆的 (invertible)**，即 $\text{rank}(\Phi(t_0)) = n$ (或者 $\det(\Phi(t_0)) \neq 0$)。
    -   基础矩阵满足矩阵形式的 ODE:
        $$
        \Phi'(t) = A(t)\Phi(t)
        $$
        因为 $A\Phi = A[y_1|\dots|y_n] = [Ay_1|\dots|Ay_n] = [y'_1|\dots|y'_n] = \Phi'$。
    -   齐次系统的**通解 (general solution)** 可以写为：
        $$
        y(t) = \Phi(t) \mathbf{c}
        $$
        其中 $\mathbf{c} = (c_1, \dots, c_n)^T \in \mathbb{C}^n$ 是任意常数向量。

#### 非齐次情况 (The Inhomogeneous Case)

(Slides 15-16)

-   **(Slide 15) 定理 (参数变易法 Variation of Parameters)**:
    1.  任何**非齐次线性**系统 $y' = A(t)y + b(t)$ 都是**可解的 (solvable)**。
    2.  一个**特解 (particular solution)** $y_p(t)$ 可以通过以下公式给出 (其中 $t_0 \in I$ 是任意选定的起点)：
        $$
        y_p(t) = \Phi(t) c(t) \quad \text{其中} \quad c(t) = \int_{t_0}^t \Phi(s)^{-1} b(s) ds
        $$
        这里 $\Phi(t)$ 是对应齐次系统的**任意**一个基础矩阵。
        *技术比喻*: 参数变易法就像是认为齐次通解 $y_h(t) = \Phi(t)c$ 中的常数向量 $c$ 其实是随时间变化的 $c(t)$。我们寻找 $c(t)$ 的变化规律 (即 $c'(t)$)，使得 $y_p(t) = \Phi(t)c(t)$ 能够正好满足非齐次方程。这种变化 $c(t)$ 就“吸收”了非齐次项 $b(t)$ 的影响。
    3.  非齐次系统的**通解 (general solution)** 是：
$$
        y(t) = y_p(t) + y_h(t) = \Phi(t) c(t) + \Phi(t) c_0 = \Phi(t) \left( \int_{t_0}^t \Phi(s)^{-1} b(s) ds + c_0 \right)
$$
        其中 $y_h(t) = \Phi(t)c_0$ 是对应齐次系统的通解，$c_0 \in \mathbb{C}^n$ 是任意常数向量。
    4.  常数向量 $c_0$ 由初始条件 $y(t_0)=y_0$ 决定：$y_0 = \Phi(t_0)c(t_0) + \Phi(t_0)c_0 = \Phi(t_0)(0 + c_0) \implies c_0 = \Phi(t_0)^{-1} y_0$。
-   **(Slide 16) 证明思路**:
    -   证明 (1): 假设解的形式为 $y_p(t) = \Phi(t)c(t)$。对其求导：
        $y_p' = \Phi' c + \Phi c' = (A\Phi)c + \Phi c' = A(\Phi c) + \Phi c' = A y_p + \Phi c'$。
        要使 $y_p' = Ay_p + b$，我们必须要求 $\Phi c' = b$，即 $c' = \Phi(t)^{-1}b(t)$。
        由于 $A(t)$ 和 $b(t)$ 连续，$\Phi(t)$ 的元素也连续可微。根据线性代数知识，$\Phi(t)^{-1}$ 的元素可以通过 $\Phi(t)$ 的元素进行加减乘除运算 (涉及伴随矩阵 Adjoint matrix 和行列式 determinant) 得到，因此 $\Phi(t)^{-1}$ 也是连续的。
        这意味着 $\Phi(t)^{-1}b(t)$ 是连续的，根据微积分基本定理，其积分 $c(t) = \int_{t_0}^t \Phi(s)^{-1}b(s) ds$ 存在且可微，且 $c'(t) = \Phi(t)^{-1}b(t)$。这证明了 $y_p(t)$ 是一个特解。
    -   证明 (2): 如果 $y_1, y_2$ 都是非齐次系统的解，那么它们的差 $(y_1-y_2)' = (Ay_1+b) - (Ay_2+b) = A(y_1-y_2)$，说明 $y_1-y_2$ 是齐次系统的解，即 $y_1-y_2 = y_h$。因此任何解都可以表示为一个特解 $y_p$ 加上一个齐次解 $y_h$。

#### 示例 (Example)

(Slides 17-19)

考虑系统：
$y_1' = y_1 + t y_2 + 1$
$y_2' = t y_1 + y_2$
即 $y' = A(t)y + b(t)$ 其中 $A(t) = \begin{pmatrix} 1 & t \\ t & 1 \end{pmatrix}$, $b(t) = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$。

1.  **解齐次系统 $y' = A(t)y$**:
    -   (Slide 17) 使用技巧：令 $s = y_1 + y_2$, $d = y_1 - y_2$。
    -   求导发现 $s' = y_1' + y_2' = (y_1+ty_2) + (ty_1+y_2) = (1+t)(y_1+y_2) = (1+t)s$。
    -   $d' = y_1' - y_2' = (y_1+ty_2) - (ty_1+y_2) = (1-t)(y_1-y_2) = (1-t)d$。
    -   这两个是解耦的 (decoupled) 一阶线性 ODE，容易解得 $s(t) = c_1 e^{\int (1+t) dt} = c_1 e^{t+t^2/2}$ 和 $d(t) = c_2 e^{\int (1-t) dt} = c_2 e^{t-t^2/2}$。
    -   (Slide 18) 反解 $y_1 = (s+d)/2$, $y_2 = (s-d)/2$ 得到齐次解：
        $y_1(t) = \frac{1}{2} (c_1 e^{t+t^2/2} + c_2 e^{t-t^2/2})$
        $y_2(t) = \frac{1}{2} (c_1 e^{t+t^2/2} - c_2 e^{t-t^2/2})$
    -   可以写成矩阵形式 $y(t) = \Phi(t) c'$，其中一个基础矩阵是 (忽略常数因子 1/2):
        $$
        \Phi(t) = \begin{pmatrix} e^{t+t^2/2} & e^{t-t^2/2} \\ e^{t+t^2/2} & -e^{t-t^2/2} \end{pmatrix}
        $$
        对应的基本解组是 $y_1(t) = e^{t+t^2/2}\begin{pmatrix} 1 \\ 1 \end{pmatrix}$ 和 $y_2(t) = e^{t-t^2/2}\begin{pmatrix} 1 \\ -1 \end{pmatrix}$。
2.  **解非齐次系统**:
    -   (Slide 19) 使用参数变易法，需要计算 $\Phi(t)^{-1}b(t)$。
    -   先计算 $\det(\Phi(t)) = -e^{t+t^2/2}e^{t-t^2/2} - e^{t+t^2/2}e^{t-t^2/2} = -2e^{2t}$。
    -   $\Phi(t)^{-1} = \frac{1}{-2e^{2t}} \begin{pmatrix} -e^{t-t^2/2} & -e^{t-t^2/2} \\ -e^{t+t^2/2} & e^{t+t^2/2} \end{pmatrix} = \frac{1}{2} \begin{pmatrix} e^{-t-t^2/2} & e^{-t-t^2/2} \\ e^{-t+t^2/2} & -e^{-t+t^2/2} \end{pmatrix}$。
    -   $\Phi(t)^{-1}b(t) = \Phi(t)^{-1}\begin{pmatrix} 1 \\ 0 \end{pmatrix} = \frac{1}{2} \begin{pmatrix} e^{-t-t^2/2} \\ e^{-t+t^2/2} \end{pmatrix}$。
    -   计算 $c(t) = \int_0^t \Phi(s)^{-1}b(s) ds = \frac{1}{2} \begin{pmatrix} \int_0^t e^{-s-s^2/2} ds \\ \int_0^t e^{-s+s^2/2} ds \end{pmatrix}$ (注意这里 $t_0=0$ 被选定)。
    -   特解 $y_p(t) = \Phi(t)c(t) = \frac{1}{2} \begin{pmatrix} e^{t+t^2/2} & e^{t-t^2/2} \\ e^{t+t^2/2} & -e^{t-t^2/2} \end{pmatrix} \begin{pmatrix} \int_0^t e^{-s-s^2/2} ds \\ \int_0^t e^{-s+s^2/2} ds \end{pmatrix}$。
        (展开后形式见 Slide 19)。
    -   通解为 $y(t) = y_p(t) + \Phi(t)c_0$。
    -   Slide 19 还提到，可以直接解耦非齐次方程 $s'=(1+t)s+1, d'=(1-t)d+1$，然后用 $y_p=(s_p+d_p)/2, (s_p-d_p)/2$ 得到同样结果 (可能积分形式不同，但导数相同)。

### 矩阵指数函数 (The Matrix Exponential Function)

(Slides 20-28)

这个工具主要用于解决**常系数**齐次线性系统 $y'=Ay$，其中 $A$ 是一个常数矩阵。

#### 定义与收敛性 (Definition & Convergence)

(Slide 20)
==对于任意的矩阵指数函数所关联的级数总是收敛==
-   **定义**: 对于 $n \times n$ 矩阵 $A$ (可以是实的或复的)，**矩阵指数 (matrix exponential)** 定义为幂级数：
    $$
    \exp(A) := e^A := \sum_{k=0}^\infty \frac{1}{k!} A^k = I + A + \frac{1}{2!}A^2 + \frac{1}{3!}A^3 + \dots
    $$
    其中 $A^0 = I$ (单位矩阵)。
-   **收敛性**: 这个级数总是收敛的。
    -   证明思路：$\mathbb{C}^{n \times n}$ 中的收敛等价于**逐元素收敛 (entry-wise convergence)**。
    -   设 $a = \max_{i,j} |A_{ij}|$。可以证明 $A^k$ 的每个元素的绝对值被 $n^{k-1} a^k$ (对于 $k\ge 1$) 或某个类似的界控制。
    -   因此，级数 $\sum \frac{1}{k!} A^k$ 的每个 $(i,j)$ 位置上的标量级数 $\sum_{k=0}^\infty \frac{(A^k)_{ij}}{k!}$ 的各项绝对值小于等于 $\delta_{ij} + \sum_{k=1}^\infty \frac{n^{k-1}a^k}{k!}$ (或者用范数 $||A^k|| \le ||A||^k$ 也可以)。这个级数收敛 (例如，通过比值判别法或与 $e^{na}$ 或 $e^{||A||}$ 的级数比较)。
    -   由于每个位置上的级数都绝对收敛，因此矩阵级数 $e^A$ 收敛。

#### 基本性质 (Properties)

(Slides 21-23)

-   **(Slide 21) 关键性质**: 如果两个矩阵 $A$ 和 $B$ **可交换 (commute)**，即 $AB = BA$，那么
    $$
    e^{A+B} = e^A e^B
    $$
    -   证明思路：由于级数绝对收敛，可以像处理标量指数函数那样重新排列 $e^A e^B = (\sum \frac{A^k}{k!})(\sum \frac{B^l}{l!})$ 的乘积项。利用 $AB=BA$，可以使用**二项式定理 (Binomial Theorem)** $(A+B)^m = \sum_{k=0}^m \binom{m}{k} A^k B^{m-k}$，最终证明 $e^A e^B = \sum_{m=0}^\infty \frac{(A+B)^m}{m!} = e^{A+B}$。
    -   **重要**: 如果 $AB \neq BA$，这个性质**不成立**！ (Slide 22 给出了反例)
-   **(Slide 22) 推论**:
    -   由于 $A$ 和 $-A$ 可交换，所以 $e^A e^{-A} = e^{A-A} = e^0 = I$。
    -   这意味着 $e^A$ **总是可逆的 (invertible)**，其逆矩阵是 $(e^A)^{-1} = e^{-A}$。
-   **(Slide 23) 练习**:
    -   对角矩阵 $D = \text{diag}(d_1, \dots, d_n)$ 的指数是 $e^D = \text{diag}(e^{d_1}, \dots, e^{d_n})$。
    -   $e^A$ 是对称的 (symmetric) $\iff A$ 是对称的。 ($(e^A)^T = \sum \frac{(A^T)^k}{k!} = e^{A^T}$ )
    -   $e^A$ 是正交的 (orthogonal) $\iff A$ 是**反对称的 (skew-symmetric)** ($A^T = -A$)。 (因为 $e^A$ 正交 $\iff (e^A)^T (e^A) = I \iff e^{A^T} e^A = I \iff e^{-A} e^A = I$，这总是成立。但还需要 $e^{A^T} = (e^A)^T = (e^A)^{-1} = e^{-A}$，这需要 $A^T = -A$)。
    -   $e^A = e^B$ **不**一定意味着 $A=B$ (例如 $A=0, B=2\pi i I$ in $\mathbb{C}^{n \times n}$)。
    -   在实数域 $\mathbb{R}^{n \times n}$ 中， $A \mapsto e^A$ 的像集 (range) 是所有行列式为正的可逆矩阵的一部分，但**不是**所有可逆矩阵 (例如，行列式为负的矩阵无法表示为 $e^A$)。在复数域 $\mathbb{C}^{n \times n}$ 中，它是所有**可逆矩阵**的集合 (矩阵对数 Logarithm 的存在性)。

#### 矩阵指数与 ODE (Matrix Exponential and ODEs)

(Slides 24-28)

-   **(Slide 24) 微分性质**: 考虑矩阵函数 $t \mapsto e^{At}$ (这里 $A$ 是常数矩阵, $t$ 是标量)。
    -   对定义级数 $\sum \frac{t^k A^k}{k!}$ **逐项求导 (termwise differentiation)** (可以证明是合法的，因为收敛性很好)：
        $$
        \frac{d}{dt} e^{At} = \sum_{k=1}^\infty \frac{k t^{k-1} A^k}{k!} = \sum_{k=1}^\infty \frac{t^{k-1} A^k}{(k-1)!} = A \sum_{k=1}^\infty \frac{t^{k-1} A^{k-1}}{(k-1)!} = A \sum_{j=0}^\infty \frac{(tA)^j}{j!} = A e^{At}
        $$
        (也可以写成 $e^{At}A$)。
-   **(Slide 24) 定理**: 对于常系数齐次线性系统 $y' = Ay$：
    -   矩阵 $\Phi(t) = e^{At}$ 是一个**基础矩阵 (fundamental matrix)**。
        (因为 $\Phi'(t) = A e^{At} = A\Phi(t)$，且 $\Phi(0) = e^{A \cdot 0} = e^0 = I$， $I$ 是可逆的)。
    -   该系统的**通解 (general solution)** 是 $y(t) = e^{At} \mathbf{c}$。
    -   对应初值问题 $y(0)=y_0$ 的**唯一解**是 $y(t) = e^{At} y_0$。
        (因为 $y(0) = e^{A \cdot 0} y_0 = I y_0 = y_0$)。
-   **(Slide 25) 示例**: $y''+y=0 \implies y_1'=y_2, y_2'=-y_1$。系统矩阵 $A = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$。
    -   $A^2 = -I, A^3 = -A, A^4 = I, \dots$ (周期为 4)。
    -   $e^{At} = I + tA + \frac{t^2}{2!}A^2 + \frac{t^3}{3!}A^3 + \dots$
        $= I(1 - \frac{t^2}{2!} + \frac{t^4}{4!} - \dots) + A(t - \frac{t^3}{3!} + \frac{t^5}{5!} - \dots)$
        $= I \cos t + A \sin t = \begin{pmatrix} \cos t & 0 \\ 0 & \cos t \end{pmatrix} + \begin{pmatrix} 0 & \sin t \\ -\sin t & 0 \end{pmatrix} = \begin{pmatrix} \cos t & \sin t \\ -\sin t & \cos t \end{pmatrix}$ (旋转矩阵)。
    -   对于 $y(0)=6, y'(0)=2$，即 $y_0 = \begin{pmatrix} 6 \\ 2 \end{pmatrix}$，解为
        $y(t) = e^{At}y_0 = \begin{pmatrix} \cos t & \sin t \\ -\sin t & \cos t \end{pmatrix} \begin{pmatrix} 6 \\ 2 \end{pmatrix} = \begin{pmatrix} 6\cos t + 2\sin t \\ -6\sin t + 2\cos t \end{pmatrix}$。
        第一分量 $y_1(t) = y(t) = 6\cos t + 2\sin t$，与已知解吻合。
-   **(Slides 26-27) 示例 (非齐次)**: $y''+y=t \implies y' = Ay + b(t)$ with $A$ 同上, $b(t) = \begin{pmatrix} 0 \\ t \end{pmatrix}$。
    -   使用参数变易法，特解 $y_p(t) = e^{At} c(t)$，其中 $c(t) = \int_0^t e^{-As} b(s) ds$。
    -   $e^{-As} = \begin{pmatrix} \cos(-s) & \sin(-s) \\ -\sin(-s) & \cos(-s) \end{pmatrix} = \begin{pmatrix} \cos s & -\sin s \\ \sin s & \cos s \end{pmatrix}$。
    -   $e^{-As}b(s) = \begin{pmatrix} \cos s & -\sin s \\ \sin s & \cos s \end{pmatrix} \begin{pmatrix} 0 \\ s \end{pmatrix} = \begin{pmatrix} -s\sin s \\ s\cos s \end{pmatrix}$。
    -   $c(t) = \int_0^t \begin{pmatrix} -s\sin s \\ s\cos s \end{pmatrix} ds = \begin{pmatrix} t\cos t - \sin t \\ t\sin t + \cos t - 1 \end{pmatrix}$ (通过分部积分计算)。
    -   $y_p(t) = e^{At}c(t) = \begin{pmatrix} \cos t & \sin t \\ -\sin t & \cos t \end{pmatrix} \begin{pmatrix} t\cos t - \sin t \\ t\sin t + \cos t - 1 \end{pmatrix} = \begin{pmatrix} t - \sin t \\ 1 - \cos t \end{pmatrix}$ (化简后)。
    -   (Slide 27) 通解 $y(t) = y_p(t) + e^{At}c_0$。
        $y(t) = \begin{pmatrix} t - \sin t \\ 1 - \cos t \end{pmatrix} + \begin{pmatrix} c_1\cos t + c_2\sin t \\ -c_1\sin t + c_2\cos t \end{pmatrix}$ (令 $c_0 = (c_1, c_2)^T$)。
        注意到 $y_p(t) = (t, 1)^T$ 也可以作为特解 (因为 $y''+y=0+t=t$)，对应的 $y(t) = t + c_1\cos t + c_2\sin t$。这与上面 $y_p$ 推导出的通解形式一致 (只是 $c_1, c_2$ 的定义不同)。
        Slide 27 还指出了 $e^{At}$ 方法总能给出实数基本解组 (如果 $A$ 是实矩阵)，而对角化 $A$ (如果可能) 可能会得到复数形式的基本解组 (如 $e^{it}(1, i)^T, e^{-it}(1, -i)^T$)。
-   **(Slide 28) 概念检查 (Concept Check)**: 总结了关于矩阵 IVP 的 EUT、基础矩阵的性质、 $e^{\int A ds}$ 的局限性 (只在 $A(t)$ 与 $\int A(s)ds$ 可交换时才可能是解，比如 $A$ 是常数) 以及 EUT 对非齐次矩阵系统也适用。

### 高阶线性 ODE (Higher-Order Linear ODE's)

(Slides 29-37)

#### 降阶法 (Order Reduction)

(Slide 29)

-   任何一个 $n$ 阶线性标量 ODE
    $$
    y^{(n)} + a_{n-1}(t)y^{(n-1)} + \dots + a_1(t)y' + a_0(t)y = b(t)
    $$
    可以通过令 $y_1 = y, y_2 = y', \dots, y_n = y^{(n-1)}$ 转化为一个 $n \times n$ 的一阶线性系统 $Y' = A(t)Y + B(t)$，其中 $Y = (y_1, \dots, y_n)^T$。
-   状态转移关系为：
    $y_1' = y_2$
    $y_2' = y_3$
    ...
    $y_{n-1}' = y_n$
    $y_n' = y^{(n)} = -a_0(t)y_1 - a_1(t)y_2 - \dots - a_{n-1}(t)y_n + b(t)$
-   写成矩阵形式 $Y' = A(t)Y + B(t)$，其中 $B(t) = (0, \dots, 0, b(t))^T$ 且 $A(t)$ 是**友矩阵 (Companion Matrix)** 的转置：
    $$
    A(t) = \begin{pmatrix}
    0 & 1 & 0 & \dots & 0 \\
    0 & 0 & 1 & \dots & 0 \\
    \vdots & \vdots & \vdots & \ddots & \vdots \\
    0 & 0 & 0 & \dots & 1 \\
    -a_0(t) & -a_1(t) & -a_2(t) & \dots & -a_{n-1}(t)
    \end{pmatrix}
    $$

#### 推论 (Corollary)

(Slides 30-31)

将一阶系统的结论应用到通过降阶法得到的高阶 ODE 系统上：

1.  **齐次解空间**: 齐次 $n$ 阶 ODE $L[y]=0$ 的所有解构成函数空间 $C^n(I)$ 的一个 $n$ 维子空间 $S$。
2.  **基本解组与 Wronskian**: 函数组 $\{y_1(t), \dots, y_n(t)\}$ 是解空间 $S$ 的一组基 (即基本解组) $\iff$ 它们的 **Wronskian 行列式 (Wronskian determinant)** 在某个 (等价于，所有) $t \in I$ 非零。
    这里的 **Wronskian 矩阵 (Wronski matrix)** 定义为：
    $$
    W(t) = \begin{pmatrix}
    y_1(t) & y_2(t) & \dots & y_n(t) \\
    y_1'(t) & y_2'(t) & \dots & y_n'(t) \\
    \vdots & \vdots & \ddots & \vdots \\
    y_1^{(n-1)}(t) & y_2^{(n-1)}(t) & \dots & y_n^{(n-1)}(t)
    \end{pmatrix}
    $$
    **Wronskian** 指的是 $W(t) = \det(W(t))$。
    *注意*: 这个 $W(t)$ 矩阵正好是对应一阶系统的基础矩阵 $\Phi(t)$ (如果 $y_1, \dots, y_n$ 是基本解组)。
3.  **非齐次解**: 非齐次 $n$ 阶 ODE $L[y]=b(t)$ 总有解。解在整个 $I$ 上存在。其通解的形式为 $y(t) = y_p(t) + y_h(t)$，其中 $y_p$ 是一个特解，$y_h$ 是齐次通解 (来自 $S$)。解集构成 $S$ 的一个**陪集 (coset)** $\{y_p + y_h \mid y_h \in S\}$。
4.  **初值问题 (IVP)**: 对于任意 $t_0 \in I$ 和任意初始值 $c_0, c_1, \dots, c_{n-1} \in \mathbb{C}$，IVP
    $$
    L[y]=b(t), \quad y(t_0)=c_0, y'(t_0)=c_1, \dots, y^{(n-1)}(t_0)=c_{n-1}
    $$
    存在**唯一的解**，且该解在整个区间 $I$ 上有定义。

#### 示例 (Example - Higher Order Variation of Parameters)

(Slides 32-37)

考虑 ODE: $y''' - y'' - 2y' = \frac{1}{1-t}$, for $t \in (-\infty, 1)$.

1.  **(Slide 32) 齐次解**: 齐次方程 $y''' - y'' - 2y' = 0$。特征方程 $r^3 - r^2 - 2r = r(r^2-r-2) = r(r-2)(r+1) = 0$。根为 $r=0, 2, -1$。
    基本解组为 $\{y_1(t)=1, y_2(t)=e^{-t}, y_3(t)=e^{2t}\}$。
    Wronskian 矩阵为:
  $$
    W(t) = \begin{pmatrix} 1 & e^{-t} & e^{2t} \\ 0 & -e^{-t} & 2e^{2t} \\ 0 & e^{-t} & 4e^{2t} \end{pmatrix}
$$
    这个 $W(t)$ 是对应一阶系统的基础矩阵 (第一行是 $y$, 第二行是 $y'$, 第三行是 $y''$)。(注意这里 $y_1=y, y_2=y', y_3=y''$ 来降阶)。
2.  **(Slides 33-34) 参数变易法 (直接对高阶 ODE)**:
    我们寻找特解 $y_p(t) = c_1(t)y_1(t) + c_2(t)y_2(t) + c_3(t)y_3(t)$。系数 $c_i'(t)$ 满足线性方程组 $W(t) \begin{pmatrix} c_1' \\ c_2' \\ c_3' \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \\ b(t)/a_n(t) \end{pmatrix}$。这里 $a_n=1$ (因为 $y'''$ 系数为 1)，$b(t)=1/(1-t)$。
    所以 $W(t) c' = (0, 0, 1/(1-t))^T$。我们需要解出 $c' = W(t)^{-1} (0, 0, 1/(1-t))^T$。
    Slide 33 通过高斯消元法求 $W(t)^{-1}$ (结果复杂，见 slide)。
    然后得到 $c'(t) = W(t)^{-1}b_{vec}(t)$ (这里 $b_{vec}$ 是系统形式的 $B(t)$，即 $(0,0,b(t))^T$)。
    积分得到 $c(t)$ (结果是含有积分的表达式)。
    $y_p(t) = c_1(t)y_1(t) + c_2(t)y_2(t) + c_3(t)y_3(t)$ 得到特解。
    通解 $y(t) = y_p(t) + \gamma_1 y_1(t) + \gamma_2 y_2(t) + \gamma_3 y_3(t)$。
3.  **(Slides 35-37) 矩阵指数方法 (概念性)**:
    -   系统为 $Y'=AY+B(t)$， $A = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 2 & 1 \end{pmatrix}$ (对应 $y'''=y''+2y'$), $B(t)=(0,0,1/(1-t))^T$。
    -   常系数系统，解可以写为 $Y(t) = e^{At}(c(t) + Y_0)$，其中 $c(t) = \int_0^t e^{-As} B(s) ds$ (假设 $t_0=0$)。
    -   关键点：$e^{At}$ 可以通过基础矩阵 $W(t)$ 计算：
        $$ e^{At} = W(t) W(0)^{-1} $$
        证明：令 $\Phi_1(t) = e^{At}$ 和 $\Phi_2(t) = W(t)W(0)^{-1}$。两者都满足 $\Phi'=A\Phi$ 且 $\Phi(0)=I$。根据解的唯一性， $\Phi_1(t) = \Phi_2(t)$。
    -   Slide 36 计算了 $W(0)^{-1}$ 并给出了 $e^{At} = W(t)W(0)^{-1}$ 的具体表达式。
    -   然后给出 $c(t) = \int_0^t e^{-As}B(s) ds = \int_0^t W(0)W(s)^{-1}B(s) ds$。
    -   最终解 $Y(t) = e^{At}Y(0) + e^{At} \int_0^t e^{-As}B(s) ds$。
    -   Slide 37 将 $Y(t)$ 的第一个分量 $y(t)$ 写出，形式是 $y(0), y'(0), y''(0)$ (即 $Y(0)$ 的分量) 乘以 $e^{At}$ 对应行的元素，再加上积分项。

### Wronskian 行列式 (The Wronskian)

(Slides 40-43)

#### 定义 (Definition)

(Slide 40)

1.  对于一阶线性系统 $y'=A(t)y$ 的 $n$ 个解 $\mathbf{y_1(t)}, \dots, \mathbf{y_n(t)}$，它们的 **Wronskian** (或 Wronski 行列式) 是 $W(t) = \det [y_1(t) | \dots | y_n(t)]$。
2.  对于 $n$ 阶标量齐次线性 ODE 的 $n$ 个解 $y_1(t), \dots, y_n(t)$，它们的 **Wronskian** 是 $W(t) = \det W(t)$，其中 $W(t)$ 是 Wronskian 矩阵：
    $$
    W(t) = \begin{pmatrix}
    y_1 & \dots & y_n \\
    y_1' & \dots & y_n' \\
    \vdots & \ddots & \vdots \\
    y_1^{(n-1)} & \dots & y_n^{(n-1)}
    \end{pmatrix}
    $$

*注*: Wronskian 矩阵 $W(t)$ (在定义 2 中) 和基础矩阵 $\Phi(t)$ (在定义 1 中，当解构成基时) 是密切相关的，尤其是在通过降阶法转换后。Wronski 行列式提供了检验解是否线性无关的关键工具。

#### 阿贝尔定理 (Abel's Theorem)

(Slides 41-43)

-   **(Slide 41) 定理**: Wronskian **$W(t)$ 满足一个一阶线性齐次 ODE**
    $$
    W'(t) = a(t) W(t)
    $$
    其中：
    -   在情况 1 (一阶系统 $y'=A(t)y$) 中，$a(t) = \text{trace}(A(t)) = \sum_{i=1}^n a_{ii}(t)$ (矩阵 $A(t)$ 的迹)。
    -   在情况 2 ($n$ 阶标量 ODE $y^{(n)} + a_{n-1}(t)y^{(n-1)} + \dots = 0$) 中，$a(t) = -a_{n-1}(t)$ ($y^{(n-1)}$ 项的系数的负值)。
-   **(Slide 41) 推论**: $W(t)$ 的解为：
    $$
    W(t) = W(t_0) \exp\left(\int_{t_0}^t a(s) ds\right)
    $$
    或者说 $W(t) = c \exp(\int a(s) ds)$ 对某个常数 $c$。
    这意味着：如果 Wronskian 在一点 $t_0$ 为零，则它在整个区间 $I$ 上恒为零；如果在一点非零，则在整个区间 $I$ 上都非零。
    这再次印证了前面关于线性无关的等价性 (只需检查一点即可)。
-   **(Slide 42) 证明思路 (n=2)**:
    对于 $W(t) = \det \begin{pmatrix} \phi_{11} & \phi_{12} \\ \phi_{21} & \phi_{22} \end{pmatrix} = \phi_{11}\phi_{22} - \phi_{21}\phi_{12}$。
    $W'(t) = (\phi_{11}'\phi_{22} + \phi_{11}\phi_{22}') - (\phi_{21}'\phi_{12} + \phi_{21}\phi_{12}')$。
    使用 $\Phi'=A\Phi$ (即 $\phi_{ij}' = \sum_k a_{ik}\phi_{kj}$) 代入并化简，可以得到 $W'(t) = (a_{11}+a_{22})W(t) = \text{trace}(A)W(t)$。
-   **(Slide 43) 示例**:
    回顾 $y'' - \frac{1}{2t}y' + \frac{1}{2t^2}y = 0$。
    对应的系统矩阵 $A(t) = \begin{pmatrix} 0 & 1 \\ -1/(2t^2) & 1/(2t) \end{pmatrix}$。
    $\text{trace}(A(t)) = 0 + 1/(2t) = 1/(2t)$。
    根据 Abel 定理，$W'(t) = \frac{1}{2t} W(t)$。
    解这个 ODE 得到 $W(t) = c \exp(\int \frac{1}{2t} dt) = c \exp(\frac{1}{2}\ln|t|) = c |t|^{1/2}$。
    因为我们考虑 $t>0$，所以 $W(t)=c\sqrt{t}$。
    之前我们直接计算得到 $W(t) = -\frac{1}{2}\sqrt{t}$，这与 Abel 定理的结果一致 (常数 $c=-1/2$ 由具体选择的解 $y_1=t, y_2=\sqrt{t}$ 在某点的值确定)。



## 二阶线性常微分方程 (Second-Order Linear ODE's)

(Slides 47-64)

这部分关注一些特殊的二阶线性 ODE。

### 2.1 三个著名的例子 (Three Famous Examples)

(Slides 47-50)

介绍三个以数学家命名的二阶时变线性 ODE，它们在物理和工程中有重要应用。它们都是形如 $p(t)y'' + q(t)y' + r(t)y = 0$ 的方程族，参数为 $n \in \{0, 1, 2, \dots\}$。

1.  **(Slide 47) 勒让德方程 (Legendre's Differential Equation)**:
    $$
    (1 - t^2)y'' - 2ty' + n(n+1)y = 0, \quad \text{for } t \in (-1, 1) \quad (Le_n)
    $$
2.  **(Slide 47) 埃尔米特方程 (Hermite's Differential Equation)**:
    $$
    y'' - 2ty' + 2ny = 0, \quad \text{for } t \in \mathbb{R} \quad (He_n)
    $$
3.  **(Slide 47) 拉盖尔方程 (Laguerre's Differential Equation)**:
    $$
    ty'' + (1 - t)y' + ny = 0, \quad \text{for } t > 0 \quad (La_n)
    $$

-   **(Slide 48) 定理**: 这些方程都有**多项式解 (polynomial solutions)**。
    -   $(Le_n)$ 的解是 $n$ 次**勒让德多项式 (Legendre Polynomial)** $P_n(t)$ (定义见 Rodrigues' formula):
        $$
        P_n(t) = \frac{1}{2^n n!} \frac{d^n}{dt^n} \left( (t^2 - 1)^n \right)
        $$
    -   $(He_n)$ 的解是 $n$ 次**埃尔米特多项式 (Hermite Polynomial)** $H_n(t)$:
        $$
        H_n(t) = (-1)^n e^{t^2} \frac{d^n}{dt^n} (e^{-t^2})
        $$
    -   $(La_n)$ 的解是 $n$ 次**拉盖尔多项式 (Laguerre Polynomial)** $L_n(t)$:
        $$
        L_n(t) = e^t \frac{d^n}{dt^n} (t^n e^{-t}) \quad \text{(Generalized Laguerre uses } t^\alpha e^{-t})
        $$
-   **(Slide 49) 注记**:
    -   在实数域上，多项式和多项式函数是一一对应的。
    -   定义中的归一化因子 (normalization factors) 并不影响它们是 ODE 解的事实 (因为 ODE 是线性的齐次的)。
-   **(Slide 50) 证明思路 (Legendre)**:
    证明 $P_n(t)$ 满足 $(Le_n)$ (这里用未归一化的版本 $\tilde{P}_n = \frac{d^n}{dt^n}(t^2-1)^n$) 的一种方法是计算 $D^{n+1}[(t^2-1)D((t^2-1)^n)]$ 两次，利用莱布尼兹公式 (Leibniz's formula) $D^k(fg) = \sum \binom{k}{i} (D^i f)(D^{k-i} g)$。两次计算结果应该相等，从而推导出 $\tilde{P}_n$ 满足的 ODE。

### 降阶法 (Order Reduction)

(Slides 51-54)

这是一种通用技术：如果我们知道二阶齐次线性 ODE $y'' + a(t)y' + b(t)y = 0$ 的一个非零解 $\phi(t)$，如何找到第二个线性无关的解 $\psi(t)$？

-   **(Slide 51) 方法**:
    1.  假设第二个解的形式为 $\psi(t) = \phi(t) u(t)$。
    2.  将 $\psi(t)$ 代入原 ODE。
    3.  利用 $\phi(t)$ 是解这一事实，可以消去含有 $u$ (但没有 $u$ 的导数) 的项。
    4.  得到一个关于 $u'$ 的**一阶线性 ODE** (实际上是关于 $u''$ 和 $u'$ 的二阶 ODE，但可以看作 $v=u'$ 的一阶 ODE)：
        $$
        \phi u'' + (2\phi' + a\phi)u' = 0
        $$
        或者写成标准形式（假设 $\phi \neq 0$）：
        $$
        u'' + \left( 2\frac{\phi'(t)}{\phi(t)} + a(t) \right) u' = 0 \quad (R)
        $$
    5.  解这个关于 $u'$ 的一阶 ODE：
        设 $v=u'$，则 $v' + (2\phi'/\phi + a)v = 0$。这是一个可分离变量或线性一阶 ODE。解为：
        $$
        v(t) = u'(t) = C \exp\left( -\int \left( 2\frac{\phi'(s)}{\phi(s)} + a(s) \right) ds \right) = C \frac{1}{(\phi(t))^2} \exp\left( -\int a(s) ds \right)
        $$
    6.  积分 $u'(t)$ 得到 $u(t)$ (取 $C=1$ 且忽略积分常数即可得到一个非平凡的 $u(t)$)。
    7.  $\psi(t) = \phi(t)u(t)$ 就是第二个线性无关解。
-   **(Slide 52) 推导**: 直接代入 $\psi=\phi u$, $\psi'=\phi'u+\phi u'$, $\psi''=\phi''u+2\phi'u'+\phi u''$ 到 $y''+ay'+by=0$ 中，整理得到 $(\phi''+a\phi'+b\phi)u + (\phi u'' + (2\phi'+a\phi)u') = 0$。由于第一项为零 (因 $\phi$ 是解)，只剩下 $\phi u'' + (2\phi'+a\phi)u' = 0$。
-   **(Slides 53-54) 示例 (Legendre n=1)**:
    方程 $(1-t^2)y'' - 2ty' + 2y = 0$。标准形式 $y'' - \frac{2t}{1-t^2}y' + \frac{2}{1-t^2}y = 0$。
    已知解 $\phi(t) = P_1(t) = t$。这里 $a(t) = -2t/(1-t^2)$。
    寻找 $\psi(t) = t u(t)$。 $u'(t)$ 满足：
    $u'' + (2\frac{1}{t} - \frac{2t}{1-t^2})u' = 0$。
    解 $u'$: $\ln|u'| = -\int (2/t - 2t/(1-t^2)) dt = -2\ln|t| - \ln|1-t^2| + C'$
    $u'(t) = C \frac{1}{t^2(1-t^2)}$。
    取 $C=1$，积分 $u'(t)$ (用部分分式 partial fractions $\frac{1}{t^2(1-t^2)} = \frac{1}{t^2} + \frac{1}{1-t^2} = \frac{1}{t^2} + \frac{1/2}{1+t} + \frac{1/2}{1-t}$):
    $u(t) = \int (\frac{1}{t^2} + \frac{1/2}{1+t} + \frac{1/2}{1-t}) dt = -\frac{1}{t} + \frac{1}{2}\ln|1+t| - \frac{1}{2}\ln|1-t| = -\frac{1}{t} + \frac{1}{2} \ln\left|\frac{1+t}{1-t}\right|$。
    第二个解 $\psi(t) = \phi(t)u(t) = t(-\frac{1}{t} + \frac{1}{2}\ln|\frac{1+t}{1-t}|) = -1 + \frac{t}{2}\ln|\frac{1+t}{1-t}|$。
    由于 $-1$ 是常数，也是齐次解 (对应 $n=0$ 的 $P_0(t)=1$ 乘以常数)，可以去掉。所以第二个线性无关解可以取为 $y_2(t) = \frac{t}{2}\ln|\frac{1+t}{1-t}|$。
    (Slide 54 给出的形式是 $\psi(t) = \frac{t}{2}\ln(\frac{1+t}{1-t}) - 1$，在区间 $(-1,1)$ 上)。
    基本解组是 $\{ t, \frac{t}{2}\ln(\frac{1+t}{1-t}) - 1 \}$ 或等价地 $\{ t, \frac{t}{2}\ln(\frac{1+t}{1-t}) \}$。

### 欧拉方程 (Euler Equations)

(Slides 55-64)

这是一类重要的具有非恒定系数的二阶 ODE。

#### 定义 (Definition)

(Slide 55)

-   **欧拉方程 (Euler Equation)** (或 Cauchy-Euler 方程) 的形式为：
    $$
    t^2 y'' + \alpha t y' + \beta y = 0 \quad (E)
    $$
    其中 $\alpha, \beta$ 是**常数** (这里假设是实数)。
-   性质：
    -   齐次，线性，二阶。
    -   系数 $t^2, \alpha t, \beta$ 不是常数 (除非 $\alpha=\beta=0$)。
    -   在 $t=0$ 处有一个**奇点 (singular point)**，因为如果写成标准形式 $y'' + (\alpha/t)y' + (\beta/t^2)y = 0$，系数在 $t=0$ 未定义 (除非 $\alpha=\beta=0$)。
    -   因此，解通常在区间 $(-\infty, 0)$ 和 $(0, \infty)$ 上分别考虑。

#### 解法 (Solution Method)

(Slides 59-64)

-   **基本思想**: 在区间 $t>0$ 上，尝试解的形式 $y(t) = t^r$。
    -   $y' = r t^{r-1}$, $y'' = r(r-1)t^{r-2}$。
    -   代入方程 (E)：
        $t^2 [r(r-1)t^{r-2}] + \alpha t [r t^{r-1}] + \beta [t^r] = 0$
        $r(r-1)t^r + \alpha r t^r + \beta t^r = 0$
        $(r^2 - r + \alpha r + \beta) t^r = 0$
    -   因为 $t^r \neq 0$ (对于 $t>0$)，所以必须满足：
        $$
        r^2 + (\alpha - 1)r + \beta = 0
        $$
        这个代数方程称为**特征方程 (characteristic equation)** 或**指标方程 (indicial equation)**。

-   **解的三种情况** (取决于特征方程的根 $r_1, r_2$):

    1.  **(Slide 59) Case 1: 不同实根 (Distinct Real Roots)** $r_1 \neq r_2$ (当 $(\alpha-1)^2 - 4\beta > 0$)。
        -   在 $t>0$ 上，两个线性无关解是 $y_1(t) = t^{r_1}$ 和 $y_2(t) = t^{r_2}$。
        -   通解为 $y(t) = c_1 t^{r_1} + c_2 t^{r_2}$。
        -   在 $t<0$ 上，令 $t = -s$ ($s>0$)，方程变为 $s^2 y'' + \alpha s y' + \beta y = 0$，解为 $y(s) = c_1 s^{r_1} + c_2 s^{r_2}$。所以 $y(t) = c_1 (-t)^{r_1} + c_2 (-t)^{r_2} = c_1 |t|^{r_1} + c_2 |t|^{r_2}$。
        -   通解可以统一写为 $y(t) = c_1 |t|^{r_1} + c_2 |t|^{r_2}$ 对 $t \neq 0$。

    2.  **(Slide 63) Case 2: 重复实根 (Repeated Real Roots)** $r_1 = r_2 = r = (1-\alpha)/2$ (当 $(\alpha-1)^2 - 4\beta = 0$)。
        -   在 $t>0$ 上，一个解是 $y_1(t) = t^r$。
        -   需要用**降阶法**找第二个解。令 $y_2 = u(t) y_1(t) = u(t) t^r$。代入标准形式 $y'' + (\alpha/t)y' + (\beta/t^2)y = 0$， $a(t)=\alpha/t$。
        -   $u'' + (2\frac{y_1'}{y_1} + a)u' = u'' + (2\frac{r t^{r-1}}{t^r} + \frac{\alpha}{t})u' = u'' + (\frac{2r+\alpha}{t})u' = 0$。
        -   由于 $r=(1-\alpha)/2 \implies 2r = 1-\alpha \implies 2r+\alpha = 1$。
        -   方程变为 $u'' + (1/t)u' = 0$。令 $v=u'$, $v' + (1/t)v = 0$。解得 $v = u' = C/t$。
        -   积分得 $u(t) = C \ln t + D$。取 $C=1, D=0$，得到 $u(t)=\ln t$。
        -   第二个线性无关解是 $y_2(t) = (\ln t) t^r$。
        -   在 $t>0$ 上，通解为 $y(t) = c_1 t^r + c_2 (\ln t) t^r$。
        -   在 $t<0$ 上，解为 $y(t) = c_1 |t|^r + c_2 (\ln |t|) |t|^r$。

    3.  **(Slide 64) Case 3: 共轭复根 (Complex Conjugate Roots)** $r_{1,2} = \lambda \pm i\mu$ ($\mu \neq 0$) (当 $(\alpha-1)^2 - 4\beta < 0$)。
        -   在 $t>0$ 上，形式解为 $t^{\lambda \pm i\mu}$。
        -   使用欧拉公式 $t^{i\mu} = e^{\ln(t^{i\mu})} = e^{i\mu \ln t} = \cos(\mu \ln t) + i \sin(\mu \ln t)$。
        -   $t^{\lambda \pm i\mu} = t^\lambda t^{\pm i\mu} = t^\lambda (\cos(\mu \ln t) \pm i \sin(\mu \ln t))$。
        -   两个线性无关的**实数解**可以通过取复数解的实部和虚部得到：
            $y_1(t) = t^\lambda \cos(\mu \ln t)$
            $y_2(t) = t^\lambda \sin(\mu \ln t)$
        -   在 $t>0$ 上，通解为 $y(t) = t^\lambda (c_1 \cos(\mu \ln t) + c_2 \sin(\mu \ln t))$。
        -   在 $t<0$ 上，用 $|t|$ 替换 $t$，$\ln|t|$ 替换 $\ln t$：
            $y(t) = |t|^\lambda (c_1 \cos(\mu \ln |t|) + c_2 \sin(\mu \ln |t|))$。

#### 解在 $t=0$ 附近的行为 (Behavior near t=0)

(Slides 56-58, 60-62, 63-64)

-   **反射原理 (Reflection Principle)** (Slide 56): $t>0$ 的解 $\phi(t)$ 可以通过 $\psi(t)=\phi(-t)$ 得到 $t<0$ 的解。
-   **跨越 $t=0$ 的光滑性 (Smoothness across t=0)** (Slides 57-58):
    -   一个解 $\phi(t)$ (定义在 $t>0$) 能否延拓成一个在 $t=0$ 处二次连续可微 ($C^2$) 的函数，取决于其在 $t \to 0^+$ 时的行为。
    -   如果 $\lim_{t\to 0^+} \phi''(t)$ 存在，则 $\lim_{t\to 0^+} \phi'(t)$ 和 $\lim_{t\to 0^+} \phi(t)$ 也存在。
    -   要使得延拓后的函数 (包含 $t=0$ 和 $t<0$ 部分) 在 $t=0$ 处 $C^2$ 光滑，必须要求 $\phi'(0) = \lim_{t\to 0^+} \phi'(t) = 0$ (因为 $\psi'(0)=-\phi'(0)$，要左右导数匹配)。
    -   对于 $y(t)=|t|^r$ (Case 1 & 2)，$y'(t)=r|t|^{r-1}\text{sgn}(t)$, $y''(t)=r(r-1)|t|^{r-2}$。
        -   $\lim_{t\to 0} y'(t) = 0$ 要求 $r-1 > 0$, 即 $r>1$。
        -   $\lim_{t\to 0} y''(t)$ 存在要求 $r-2 \ge 0$, 即 $r \ge 2$ (如果 $r=2$, $y''$ 是常数)。
        -   因此 $|t|^r$ 在 $t=0$ 处是 $C^2$ 的 $\iff r=0$ (此时 $y=1$) 或 $r \ge 2$。
    -   对于 $y(t)=|t|^r \ln|t|$ (Case 2)，行为更差，通常在 $t=0$ 不光滑。
    -   对于 $y(t)=|t|^\lambda \cos/\sin(\mu \ln|t|)$ (Case 3)，当 $t\to 0$, $\ln|t|\to -\infty$，函数会无限振荡 (除非 $\lambda$ 足够大能压制)。 $\lim_{t\to 0} y'(t)=0$ 要求 $\lambda > 1$。 $\lim_{t\to 0} y''(t)$ 存在要求 $\lambda \ge 2$。
-   **解空间 $S_0$ (定义在 $\mathbb{R}$ 上)** (Slides 60-62 for Case 1):
    -   $S_0$ 由那些可以在 $t=0$ 处光滑连接 (至少 $C^2$) 的解构成。
    -   维数 $\dim(S_0)$ 取决于 $r_1, r_2$ (或 $\lambda$) 相对于 0, 1, 2 的值。
    -   例如：
        -   如果 $r_1, r_2 < 0$，只有 $y=0$ 是 $S_0$ 的解，$\dim=0$。
        -   如果 $r_1=0, r_2 < 0$，只有 $y=c$ (常数) 是 $S_0$ 解，$\dim=1$。
        -   如果 $r_1=1, r_2=0$ (即 $t^2y''+ty'=0$)，解 $y=c_1+c_2t$ 在 $t=0$ 是 $C^\infty$，$\dim=2$。
        -   如果 $r_1 > 2, 0 < r_2 < 1$，只有 $y=c_1 |t|^{r_1}$ (满足 $y(0)=y'(0)=y''(0)=0$) 和 $y=0$ 可以延拓。$\dim=2$ (基是 slide 61 给出的 $y_1, y_2$ 函数，它们在 $t=0$ 处不是传统基的意义，而是指所有解都可以由它们在 $t>0$ 和 $t<0$ 的部分组合而成)。
        -   如果 $r_1 > 2, r_2 = 2$，则 $y=c_1 |t|^{r_1} + c_2 t^2$ 是解。 $\dim=3$ (基 $y_1, y_2$ (来自 $r_1$), $y_3=t^2$)。
        -   如果 $r_1 > 2, r_2 > 2$，则 $\dim=4$ (基 $y_1, y_2$ (来自 $r_1$), $y_3, y_4$ (来自 $r_2$))。
    -   Case 2 和 Case 3 的分析类似，基于 $t^r, |t|^r \ln|t|, |t|^\lambda \cos/\sin(\mu \ln|t|)$ 在 $t=0$ 的光滑性。
