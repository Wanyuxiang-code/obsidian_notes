---
title: Computing the Matrix Exponential
date: 2025-05-16
date modified: 2025-05-16
categories: Math285
tags:
  - Math285
---
#Math285 



## 引言与基本概念 (Introduction and Basic Concepts)

### 1.  系统定义 (System Definition) (Slide 4)

-   **核心方程 (Core Equation)**:
    我们主要研究的是一阶线性常微分方程组 (First-Order Linear ODE Systems)。其一般形式为：
    $$
    \mathbf{y}' = A\mathbf{y} + \mathbf{b}(t)
    $$
    其中:
    -   $\mathbf{y}(t) = \begin{pmatrix} y_1(t) \\ \vdots \\ y_n(t) \end{pmatrix}$ 是一个包含 $n$ 个未知函数的向量。
    -   $\mathbf{y}'(t) = \frac{d\mathbf{y}}{dt}$ 是这些函数的导数向量。
    -   $A$ 是一个 $n \times n$ 的常系数矩阵 (coefficient matrix)。
    -   $\mathbf{b}(t)$ 是一个 $n \times 1$ 的向量函数，称为非齐次项 (inhomogeneous term) 或源项 (source term)。

-   **自治系统 (Autonomous System)**: 如果矩阵 $A$ 和向量 $\mathbf{b}$ 都不显式地依赖于时间 $t$ (即 $A$ 和 $\mathbf{b}$ 都是常数)，则系统称为自治系统。
-   **齐次系统 (Homogeneous System)**: 如果 $\mathbf{b}(t) \equiv \mathbf{0}$，则系统为齐次系统: $\mathbf{y}' = A\mathbf{y}$。
-   **非齐次系统 (Inhomogeneous/Non-homogeneous System)**: 如果 $\mathbf{b}(t) \not\equiv \mathbf{0}$，则系统为非齐次系统。

### 2.  学习动机与实例 (Motivation and Examples) (Slides 5-8)

-   **物理系统建模 (Modeling Physical Systems)**:
    -   **弹簧-质量系统 (Spring-Mass Systems)**:
        这类系统通常由二阶微分方程描述。例如，Slide 5 中的一个双质量块、三弹簧系统：
        $$
        \begin{align}
        & m x_1''(t) = -(k_1 + k_2)x_1 + k_2 x_2 + F_1(t) \\
        & m x_2''(t) = k_2 x_1 - (k_2 + k_3)x_2 + F_2(t)
        \end{align}
     $$
        通过引入新的变量来**降阶 (order reduction)**。令 $y_1 = x_1, y_2 = x_2, y_3 = x_1', y_4 = x_2'$。
        则原二阶 $2 \times 2$ 系统可以转换为一个一阶 $4 \times 4$ 系统 $\mathbf{y}' = A\mathbf{y} + \mathbf{f}(t)$：
        $$
        \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix}' = \begin{pmatrix} 0 & 0 & 1 & 0 \\ 0 & 0 & 0 & 1 \\ -(k_1+k_2)/m & k_2/m & 0 & 0 \\ k_2/m & -(k_2+k_3)/m & 0 & 0 \end{pmatrix} \begin{pmatrix} x_1 \\ x_2 \\ x_3 \\ x_4 \end{pmatrix} + \begin{pmatrix} 0 \\ 0 \\ F_1(t)/m \\ F_2(t)/m \end{pmatrix}
        $$
        这展示了将高阶标量 ODE 或高阶 ODE 系统转化为一阶 ODE 系统的重要性。

    -   **LRC 电路 (LRC Electric Circuits)** (Slide 7, 8 (Figure 7.1.2)):
        例如，一个并联 LRC 电路中，电流 $I(t)$ 和电压 $V(t)$ 的关系可以用一个一阶齐次线性系统描述：
        $$
        \begin{align}
        & I'(t) = \frac{1}{L}V \\
        & V'(t) = -\frac{1}{C}I - \frac{1}{RC}V
        \end{align}
     $$
        可以写成矩阵形式：
        $$
        \begin{pmatrix} I \\ V \end{pmatrix}' = \begin{pmatrix} 0 & 1/L \\ -1/C & -1/(RC) \end{pmatrix} \begin{pmatrix} I \\ V \end{pmatrix}
        $$

## 基础理论回顾 (Review of Fundamental Theory) 

### 初值问题 (Initial Value Problem - IVP) 

-   对于系统 $\mathbf{y}' = A\mathbf{y} + \mathbf{b}(t)$ 和初始条件 $\mathbf{y}(t_0) = \mathbf{y}_0$：
    -   **存在唯一解 (Existence and Uniqueness)**: 如果 $\mathbf{b}(t)$ 的所有分量函数在包含 $t_0$ 的区间上**连续**，则 IVP 在该区间上有唯一的最大解。
    -   如果 $\mathbf{b}(t) = \mathbf{b}$ (常数向量，自治系统)，则解在整个实数轴 $\mathbb{R}$ 上定义。

### 齐次系统的解结构 (Solution Structure of Homogeneous Systems)

-   对于齐次系统 $\mathbf{y}' = A\mathbf{y}$：
    -   **解空间 (Solution Space)**: 所有的解构成一个 $n$ 维向量空间。这个空间是所有从 $\mathbb{R}$ 到 $\mathbb{C}^n$ 的映射构成的函数空间 $(\mathbb{C}^n)^\mathbb{R}$ 的一个子空间 $S$。
    -   这意味着如果 $\mathbf{y}_1(t), \dots, \mathbf{y}_n(t)$ 是 $n$ 个线性无关的解，那么任何解都可以表示为它们的线性组合： $\mathbf{y}(t) = c_1\mathbf{y}_1(t) + \dots + c_n\mathbf{y}_n(t)$。

### 基本矩阵与非齐次系统解 (Fundamental Matrix and Solution of Inhomogeneous Systems)

-   **基本矩阵 (Fundamental Matrix) $\Phi(t)$**:
    -   定义: 一个 $n \times n$ 矩阵函数 $\Phi(t)$，其列向量是 $\mathbf{y}' = A\mathbf{y}$ 的 $n$ 个线性无关的解。
    -   性质: $\Phi'(t) = A\Phi(t)$，并且 $\det(\Phi(t)) \neq 0$。
-   **非齐次系统 $\mathbf{y}' = A\mathbf{y} + \mathbf{b}(t)$ 的通解 (General Solution)**:
    -   使用基本矩阵的公式 (也称为参数变易法 - Variation of Parameters):
        $$
        \mathbf{y}(t) = \Phi(t) \left( \mathbf{c}_0 + \int_{t_0}^t \Phi(s)^{-1}\mathbf{b}(s) ds \right)
        $$
        其中 $\mathbf{c}_0 = \Phi(t_0)^{-1}\mathbf{y}(t_0)$。
    -   或者，如果已知一个特解 (particular solution) $\mathbf{y}_p(t)$：
        $$
        \mathbf{y}(t) = \Phi(t)\mathbf{c}_0 + \mathbf{y}_p(t)
        $$
        这里 $\Phi(t)\mathbf{c}_0$ 是对应齐次系统的通解。

### 矩阵指数 (Matrix Exponential) - 时间无关情形的特性

-   **定义 (Definition)**: 对于常数矩阵 $A$，矩阵指数 $e^{At}$ (或 $\exp(At)$) 定义为泰勒级数：
    $$
    e^{At} = \sum_{k=0}^{\infty} \frac{(At)^k}{k!} = I_n + At + \frac{(At)^2}{2!} + \frac{(At)^3}{3!} + \dots
    $$
-   **关键性质 (Key Properties)**:
    -   $\frac{d}{dt} e^{At} = A e^{At}$。
    -   $e^{A \cdot 0} = I_n$ (单位矩阵)。
    -   因此，$e^{At}$ 是齐次系统 $\mathbf{y}' = A\mathbf{y}$ 的一个基本矩阵，且是在 $t=0$ 时取值为单位矩阵的那个特殊基本矩阵，称为**标准基本矩阵 (standard fundamental matrix)**。
    -   对于 IVP $\mathbf{y}' = A\mathbf{y}$，$\mathbf{y}(0) = \mathbf{y}_0$，其解为 $\mathbf{y}(t) = e^{At}\mathbf{y}_0$。
-   **不同基本矩阵的关系 (Relation between Fundamental Matrices)**:
    -   任意两个基本矩阵 $\Phi_1(t)$ 和 $\Phi_2(t)$ 通过一个常数可逆矩阵 $C$ 相关联：$\Phi_1(t) = \Phi_2(t)C$。
    -   任何基本矩阵 $\Phi(t)$ 都可以表示为 $\Phi(t) = e^{At}\Phi(0)$。
    -   因此，如果知道任何一个基本矩阵 $\Phi(t)$，就可以计算 $e^{At} = \Phi(t)\Phi(0)^{-1}$。
-   **核心问题 (Central Problem)**: 如何有效地计算 $e^{At}$？

## 计算矩阵指数 $e^{At}$ (Computing the Matrix Exponential $e^{At}$) (Slides 11-29, 58-64, 65-72)

### A. 基于对角化 (Based on Diagonalization)

当矩阵 $A$ 有 $n$ 个线性独立的特征向量时（特征方程有 $n$ 个不同根），矩阵 $A$ 可以对角化

#### A1. $A$ 是对角矩阵 (A is a Diagonal Matrix) 

-   如果 $A = \text{diag}(\lambda_1, \lambda_2, \dots, \lambda_n)$，即
    $$
    A = \begin{pmatrix} \lambda_1 & 0 & \cdots & 0 \\ 0 & \lambda_2 & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & \lambda_n \end{pmatrix}
    $$
-   系统 $\mathbf{y}' = A\mathbf{y}$ 解耦 (decoupled) 成 $n$ 个独立的标量方程：$y_i' = \lambda_i y_i$。
-   每个标量方程的解是 $y_i(t) = c_i e^{\lambda_i t}$。
-   因此，通解为 $\mathbf{y}(t) = \begin{pmatrix} c_1 e^{\lambda_1 t} \\ \vdots \\ c_n e^{\lambda_n t} \end{pmatrix} = \text{diag}(e^{\lambda_1 t}, \dots, e^{\lambda_n t}) \mathbf{c}$。
-   基本矩阵可以是 $\Phi(t) = \text{diag}(e^{\lambda_1 t}, \dots, e^{\lambda_n t})$。
-   由于 $\Phi(0) = \text{diag}(e^0, \dots, e^0) = I_n$，所以
    $$
    e^{At} = \text{diag}(e^{\lambda_1 t}, \dots, e^{\lambda_n t}) = \begin{pmatrix} e^{\lambda_1 t} & 0 & \cdots & 0 \\ 0 & e^{\lambda_2 t} & \cdots & 0 \\ \vdots & \vdots & \ddots & \vdots \\ 0 & 0 & \cdots & e^{\lambda_n t} \end{pmatrix}
    $$


#### A2. $A$ 可对角化 (A is Diagonalizable) 

-   **条件 (Condition)**: 矩阵 $A$ 有 $n$ 个线性无关的特征向量 (eigenvectors)。
-   **对角化过程 (Diagonalization Process)**:
    存在一个可逆矩阵 $S$，其列是 $A$ 的特征向量 $\mathbf{v}_1, \dots, \mathbf{v}_n$，以及一个对角矩阵 $D = \text{diag}(\lambda_1, \dots, \lambda_n)$，其中 $\lambda_i$ 是对应 $\mathbf{v}_i$ 的特征值 (eigenvalues)，使得 $A = SDS^{-1}$ (或者 $S^{-1}AS = D$)。
-   **坐标变换 (Coordinate Transformation)**:
    令 $\mathbf{y}(t) = S\mathbf{z}(t)$。代入 $\mathbf{y}' = A\mathbf{y}$：
    $S\mathbf{z}' = A(S\mathbf{z}) \implies \mathbf{z}' = S^{-1}AS\mathbf{z} \implies \mathbf{z}' = D\mathbf{z}$。
    这是一个对角化系统，我们已经知道如何求解：$z_i(t) = c_i e^{\lambda_i t}$。
-   **原始系统的解 (Solution in Original Coordinates)**:
    $\mathbf{y}(t) = S\mathbf{z}(t) = S \begin{pmatrix} e^{\lambda_1 t} c_1 \\ \vdots \\ e^{\lambda_n t} c_n \end{pmatrix} = S \text{diag}(e^{\lambda_1 t}, \dots, e^{\lambda_n t}) \mathbf{c}$。
    可以写成 $\mathbf{y}(t) = c_1 e^{\lambda_1 t}\mathbf{v}_1 + \dots + c_n e^{\lambda_n t}\mathbf{v}_n$。
-   **计算 $e^{At}$** (Slide 15-16, 58):
    我们知道 $e^{At} = \sum_{k=0}^\infty \frac{t^k A^k}{k!}$。
    因为 $A = SDS^{-1}$, 所以 $A^k = (SDS^{-1})^k = SD S^{-1} S D S^{-1} \dots S D S^{-1} = S D^k S^{-1}$。
    所以，
    $$
    e^{At} = \sum_{k=0}^\infty \frac{t^k (S D^k S^{-1})}{k!} = S \left( \sum_{k=0}^\infty \frac{t^k D^k}{k!} \right) S^{-1} = S e^{Dt} S^{-1}
    $$
    由于 $e^{Dt} = \text{diag}(e^{\lambda_1 t}, \dots, e^{\lambda_n t})$，所以
    $$
    e^{At} = S \begin{pmatrix} e^{\lambda_1 t} & & \\ & \ddots & \\ & & e^{\lambda_n t} \end{pmatrix} S^{-1}
    $$
-   **基本矩阵视角 (Fundamental Matrix Perspective)**:
    一个基本矩阵是 $\Phi(t) = (e^{\lambda_1 t}\mathbf{v}_1 | \dots | e^{\lambda_n t}\mathbf{v}_n) = S \text{diag}(e^{\lambda_1 t}, \dots, e^{\lambda_n t})$。
    $\Phi(0) = S \text{diag}(1, \dots, 1) = S$。
    则 $e^{At} = \Phi(t)\Phi(0)^{-1} = S \text{diag}(e^{\lambda_1 t}, \dots, e^{\lambda_n t}) S^{-1}$。
-   **例子 (Example)** : $y''+y=0 \implies \mathbf{y}' = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} \mathbf{y}$。
    $A = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$。特征值 $\lambda_1 = i, \lambda_2 = -i$。
    对应特征向量 $\mathbf{v}_1 = \begin{pmatrix} 1 \\ i \end{pmatrix}, \mathbf{v}_2 = \begin{pmatrix} 1 \\ -i \end{pmatrix}$ (或者 Slide 18 中的形式，只是顺序和常数倍数不同)。
    $S = \begin{pmatrix} 1 & 1 \\ i & -i \end{pmatrix}$ (Slide 18 使用了不同的 $S$ 的形式，但结果等价)。
    计算后得到 $e^{At} = \begin{pmatrix} \cos t & \sin t \\ -\sin t & \cos t \end{pmatrix}$。
    Slide 19 提到了一些备注，如实矩阵 $A$ 的复共轭特征值和特征向量的关系。
-   **例子 (Example)** : $A = \begin{pmatrix} 2 & -2 & -16 \\ 0 & 1 & 6 \\ 0 & 0 & -2 \end{pmatrix}$。
    由于是上三角矩阵，特征值在对角线上：$\lambda_1=2, \lambda_2=1, \lambda_3=-2$。
    特征值互异，所以 $A$ 可对角化。
    计算出特征向量，构成 $S$，然后就可以计算 $e^{At}$ (虽然这里没有显式给出 $e^{At}$，而是给出了基本解组)。
    基本解组为 $\mathbf{y}_1(t) = e^{2t}\begin{pmatrix} 1 \\ 0 \\ 0 \end{pmatrix}, \mathbf{y}_2(t) = e^{t}\begin{pmatrix} 2 \\ 1 \\ 0 \end{pmatrix}, \mathbf{y}_3(t) = e^{-2t}\begin{pmatrix} -3 \\ 2 \\ -1 \end{pmatrix}$。
-   **例子 (Optional Example)** : 一个 $3 \times 3$ 循环矩阵的例子，其特征值和特征向量已知 (来自 Math257)。
    $A = \begin{pmatrix} 1 & 0 & 1 \\ 1 & 1 & 0 \\ 0 & 1 & 1 \end{pmatrix}$。特征值 $2, \omega, \omega^2$ (其中 $\omega = e^{2\pi i/3}$)。
    Slides 24-26 展示了如何用这些特征值和特征向量（构成 $S$）来计算 $e^{At}$。
    Slides 27-29 提供了一些关于求解这个特定例子特征值/向量的额外技巧，以及如何从复数解中提取实数基本解组。

### B. 基于广义特征向量和若尔当标准型 (Generalized Eigenvectors and Jordan Canonical Form) - 当 $A$ 不可对角化时 

当矩阵 $A$ 的某些特征值的代数重数 (algebraic multiplicity) 大于其几何重数 (geometric multiplicity) 时，$A$ 没有 $n$ 个线性无关的特征向量，因此不可对角化。


**核心思想**:
1.  找到一个可逆矩阵 $S$，其列由 $A$ 的广义特征向量构成，使得 $A$ 可以被转换为其若尔当标准型 $J$：$A = SJS^{-1}$ (或者 $S^{-1}AS = J$)。
2.  利用这个分解，计算 $e^{At} = S e^{Jt} S^{-1}$。
3.  计算 $e^{Jt}$ 相对容易，因为 $J$ 是一个分块对角矩阵，每个块是一个若尔当块。

**步骤详解**:
**1. 找到 $A$ 的特征值 (Eigenvalues) 及其代数重数 (Algebraic Multiplicities)**

-   求解特征方程 $\det(A - \lambda I) = 0$ 得到所有特征值 $\lambda_1, \lambda_2, \dots, \lambda_r$。
-   确定每个特征值 $\lambda_k$ 的代数重数 $m_k$ (即它作为特征方程根的次数)。

**2. 为每个特征值 $\lambda_k$ 找到广义特征向量并构成若尔当链 (Jordan Chains)**

这是最关键且可能最复杂的一步。对于每个特征值 $\lambda_k$ (代数重数为 $m_k$)：

1.  **计算普通特征向量**:
    求解 $(A - \lambda_k I)\mathbf{v} = \mathbf{0}$ 找到所有线性无关的特征向量。其解空间的维数是 $\lambda_k$ 的**几何重数 (geometric multiplicity)** $g_k$。
    -   $g_k$ 告诉我们对应于 $\lambda_k$ 有多少个若尔当块。
    -   如果对所有 $k$ 都有 $g_k = m_k$，则矩阵 $A$ 可对角化，就不需要 JCF 了。我们现在处理的是 $g_k < m_k$ 的情况。

2.  **寻找广义特征向量**:
    广义特征向量 $\mathbf{v}$ 满足 $(A - \lambda_k I)^p \mathbf{v} = \mathbf{0}$ 对于某个正整数 $p \le m_k$，但 $(A - \lambda_k I)^{p-1} \mathbf{v} \neq \mathbf{0}$。
    -   所有与 $\lambda_k$ 相关的广义特征向量（加上零向量）构成**广义特征空间 (generalized eigenspace)** $G_{\lambda_k} = \ker((A - \lambda_k I)^{m_k})$。其维数为 $m_k$。

3.  **构造若尔当链**:
    一个与特征值 $\lambda_k$ 相关的长度为 $p$ 的若尔当链是一组向量 $\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_p\}$，满足：
    -   $(A - \lambda_k I)\mathbf{v}_1 = \mathbf{0}$ ($\mathbf{v}_1$ 是一个普通的特征向量)
    -   $(A - \lambda_k I)\mathbf{v}_2 = \mathbf{v}_1$
    -   $(A - \lambda_k I)\mathbf{v}_3 = \mathbf{v}_2$
    -   ...
    -   $(A - \lambda_k I)\mathbf{v}_p = \mathbf{v}_{p-1}$
    这里，$\mathbf{v}_p$ 称为链的**生成元 (generator)** 或顶层广义特征向量。$\mathbf{v}_1, \dots, \mathbf{v}_p$ 都是广义特征向量，且它们是线性无关的。
    每个若尔当链对应一个若尔当块。链的长度 $p$ 就是对应若尔当块的大小。

    **如何找到这些链 (一种常见策略，"自上而下")**:
    a.  确定最长链的长度 $p_{\max}$：它是最小的整数使得 $\ker((A-\lambda_k I)^{p_{\max}}) = G_{\lambda_k}$ (通常 $p_{\max}$ 是使得 $\dim \ker((A-\lambda_k I)^{p_{\max}})$ 首次达到 $m_k$ 的那个幂次，或者更准确地说，是使得 $\dim \ker((A-\lambda_k I)^j)$ 不再增加的最小 $j$)。
    b.  选择一个向量 $\mathbf{v}_{p_{\max}}$ 使得 $\mathbf{v}_{p_{\max}} \in \ker((A-\lambda_k I)^{p_{\max}})$ 但 $\mathbf{v}_{p_{\max}} \notin \ker((A-\lambda_k I)^{p_{\max}-1})$。
    c.  然后依次计算链中的其他向量：
        $\mathbf{v}_{p_{\max}-1} = (A - \lambda_k I)\mathbf{v}_{p_{\max}}$
        $\mathbf{v}_{p_{\max}-2} = (A - \lambda_k I)\mathbf{v}_{p_{\max}-1}$
        ...
        $\mathbf{v}_1 = (A - \lambda_k I)\mathbf{v}_2$
    d.  如果这个链中的 $p_{\max}$ 个向量还没有张成整个 $G_{\lambda_k}$ (即 $p_{\max} < m_k$ 或者几何重数 $g_k > 1$)，你需要在已找到链的张成空间的补空间中，针对次长链或其他同样长度的链重复此过程。
        -   例如，如果有 $g_k$ 个若尔当块，你就需要找到 $g_k$ 个这样的链的生成元，它们共同生成的链向量集合将构成 $G_{\lambda_k}$ 的一组基。
        -   确定若尔当块的结构（多少个块，每个块多大）可以通过分析核空间的维数序列 $d_j = \dim \ker((A-\lambda_k I)^j)$ 来得到。大小为 $j$ 的块的数量是 $2d_j - d_{j-1} - d_{j+1}$。

**3. 构造矩阵 $S$ 和若尔当标准型 $J$**

1.  **构造 $S$**:
    矩阵 $S$ 的列由所有若尔当链中的广义特征向量组成。
    -   将每个链中的向量 $\{\mathbf{v}_1, \mathbf{v}_2, \dots, \mathbf{v}_p\}$ 按此顺序（$\mathbf{v}_1$ 是特征向量，$\mathbf{v}_p$ 是生成元）作为 $S$ 的连续列。
    -   对所有特征值的所有链都这样做，将它们拼接起来形成 $S$。
    -   $S$ 必须是可逆的。

2.  **构造 $J$**:
    $J$ 是一个分块对角矩阵：
    $$
    J = \begin{pmatrix} J_1 & & \\ & J_2 & & \\ & & \ddots & \\ & & & J_s \end{pmatrix}
    $$
    其中每个 $J_i$ 是一个若尔当块，对应于 $S$ 中的一个若尔当链。
    如果一个链是 $\{\mathbf{v}_1, \dots, \mathbf{v}_p\}$ (对应特征值 $\lambda_k$)，则对应的若尔当块是一个 $p \times p$ 矩阵：
    $$
    J_i = \begin{pmatrix}
    \lambda_k & 1 & 0 & \cdots & 0 \\
    0 & \lambda_k & 1 & \cdots & 0 \\
    \vdots & \ddots & \ddots & \ddots & \vdots \\
    0 & \cdots & 0 & \lambda_k & 1 \\
    0 & \cdots & \cdots & 0 & \lambda_k
    \end{pmatrix}
    $$
    （主对角线上是特征值 $\lambda_k$，紧邻主对角线上方的是 1，其他位置是 0）。
    $J$ 中若尔当块的顺序和大小必须与 $S$ 中广义特征向量链的排列方式一致，以满足 $AS = SJ$。

**4. 计算 $S^{-1}$**

-   这是标准的可逆矩阵求逆过程。

**5. 计算 $e^{Jt}$**

由于 $J$ 是分块对角矩阵，所以 $e^{Jt}$ 也是一个分块对角矩阵：
$$
e^{Jt} = \begin{pmatrix} e^{J_1 t} & & \\ & e^{J_2 t} & & \\ & & \ddots & \\ & & & e^{J_s t} \end{pmatrix}
$$
现在我们需要计算每个若尔当块的指数 $e^{J_i t}$。
令 $J_i = \lambda_k I_p + N_p$，其中 $I_p$ 是 $p \times p$ 单位矩阵，$N_p$ 是一个 $p \times p$ 的幂零矩阵 (nilpotent matrix)，其主对角线上方元素为 1，其余为 0 (例如，$N_3 = \begin{pmatrix} 0&1&0 \\ 0&0&1 \\ 0&0&0 \end{pmatrix}$)。$N_p^p = \mathbf{0}$。
由于 $\lambda_k I_p$ 和 $N_p$ 可交换，所以：
$$
e^{J_i t} = e^{(\lambda_k I_p + N_p)t} = e^{\lambda_k I_p t} e^{N_p t} = e^{\lambda_k t} I_p \cdot e^{N_p t} = e^{\lambda_k t} e^{N_p t}
$$
而幂零矩阵的指数可以用其泰勒级数的有限项计算：
$$
e^{N_p t} = I_p + (N_p t) + \frac{(N_p t)^2}{2!} + \dots + \frac{(N_p t)^{p-1}}{(p-1)!}
$$
(因为 $N_p^j = \mathbf{0}$ 对于 $j \ge p$)

**例如**:
-   如果 $J_i = \begin{pmatrix} \lambda_k & 1 \\ 0 & \lambda_k \end{pmatrix}$ (大小 $p=2$)，则 $N_2 = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$。
    $e^{N_2 t} = I_2 + N_2 t = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix} + \begin{pmatrix} 0 & t \\ 0 & 0 \end{pmatrix} = \begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix}$。
    所以 $e^{J_i t} = e^{\lambda_k t} \begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} e^{\lambda_k t} & t e^{\lambda_k t} \\ 0 & e^{\lambda_k t} \end{pmatrix}$。

-   如果 $J_i = \begin{pmatrix} \lambda_k & 1 & 0 \\ 0 & \lambda_k & 1 \\ 0 & 0 & \lambda_k \end{pmatrix}$ (大小 $p=3$)，则 $N_3 = \begin{pmatrix} 0 & 1 & 0 \\ 0 & 0 & 1 \\ 0 & 0 & 0 \end{pmatrix}$。
    $N_3 t = \begin{pmatrix} 0 & t & 0 \\ 0 & 0 & t \\ 0 & 0 & 0 \end{pmatrix}$, $(N_3 t)^2 = \begin{pmatrix} 0 & 0 & t^2 \\ 0 & 0 & 0 \\ 0 & 0 & 0 \end{pmatrix}$, $(N_3 t)^3 = \mathbf{0}$。
    $e^{N_3 t} = I_3 + N_3 t + \frac{(N_3 t)^2}{2!} = \begin{pmatrix} 1 & t & t^2/2 \\ 0 & 1 & t \\ 0 & 0 & 1 \end{pmatrix}$。
    所以 $e^{J_i t} = e^{\lambda_k t} \begin{pmatrix} 1 & t & t^2/2 \\ 0 & 1 & t \\ 0 & 0 & 1 \end{pmatrix}$。

以此类推，可以得到任意大小若尔当块的指数。

**6. 计算 $e^{At} = S e^{Jt} S^{-1}$**

-   将前面得到的 $S$, $e^{Jt}$, 和 $S^{-1}$ 相乘，即可得到最终的 $e^{At}$。

#### B1. 理论基础 (Theoretical Foundation)

-   **动机来自高阶标量 ODE (Motivation from higher-order scalar ODEs)** :
    一个 $n$ 阶常系数齐次线性标量 ODE $a(D)y=0$ (其中 $a(X)$ 是特征多项式) 的解包含形如 $t^k e^{\lambda t}$ 的项，其中 $\lambda$ 是特征根，$k$ 小于该根的重数。
    通过降阶，这个标量 ODE 可以转换为一个一阶 $n \times n$ 系统 $\mathbf{y}' = C\mathbf{y}$，其中 $C$ 是 $a(X)$ 的**伴随矩阵 (companion matrix)**。这个系统的解向量的分量就是 $t^k e^{\lambda t}$ 及其导数。
-   **尝试解 (Ansatz)** : 
    对于代数重数为 $m$ 的特征值 $\lambda$，我们尝试寻找形如
    $$
    \mathbf{y}(t) = e^{\lambda t}\mathbf{v}_0 + t e^{\lambda t}\mathbf{v}_1 + \dots + t^{m-1}e^{\lambda t}\mathbf{v}_{m-1}
    $$
    的解，其中 $\mathbf{v}_j \in \mathbb{C}^n$ 是待定向量。
-   **推导向量链 (Deriving Vector Chains)**:
    将上述 Ansatz 代入 $\mathbf{y}' = A\mathbf{y}$ 并比较 $t^k e^{\lambda t}$ 的系数，可以得到一个向量链：
    -   $(A - \lambda I_n)\mathbf{v}_{m-1} = \mathbf{0}$  ($\mathbf{v}_{m-1}$ 是一个普通的特征向量)
    -   $(A - \lambda I_n)\mathbf{v}_{m-2} = \mathbf{v}_{m-1}$
    -   ...
    -   $(A - \lambda I_n)\mathbf{v}_0 = \mathbf{v}_1$
    这个链可以等价地写成：
    -   $(A - \lambda I_n)\mathbf{v}_{m-1} = \mathbf{0}$
    -   $(A - \lambda I_n)^2\mathbf{v}_{m-2} = \mathbf{0}$ (但 $(A - \lambda I_n)\mathbf{v}_{m-2} \neq \mathbf{0}$)
    -   ...
    -   $(A - \lambda I_n)^m\mathbf{v}_0 = \mathbf{0}$ (但 $(A - \lambda I_n)^{m-1}\mathbf{v}_0 \neq \mathbf{0}$)
    向量 $\mathbf{v}_0, \dots, \mathbf{v}_{m-1}$ 称为**广义特征向量链 (chain of generalized eigenvectors)**，$\mathbf{v}_0$ 是链的生成元。
-   **广义特征向量与广义特征空间 (Generalized Eigenvectors and Eigenspaces)** :
    -   **广义特征向量 (Generalized Eigenvector)**: 对特征值 $\lambda_i$ (代数重数为 $m_i$)，若 $\mathbf{v} \in \mathbb{C}^n \setminus \{\mathbf{0}\}$ 满足 $(A - \lambda_i I_n)^{m_i}\mathbf{v} = \mathbf{0}$，则 $\mathbf{v}$ 是 $A$ 关于 $\lambda_i$ 的广义特征向量。
    -   **广义特征空间 (Generalized Eigenspace) $G_{\lambda_i}$**: 由所有对应于 $\lambda_i$ 的广义特征向量以及零向量构成的子空间。即 $G_{\lambda_i} = \ker((A - \lambda_i I_n)^{m_i})$。
    -   **性质 (Properties)**:
        -   $\dim(G_{\lambda_i}) = m_i$ (**广义特征空间的维数等于特征值的代数重数**，即广义特征向量对应的方程对应的解空间即由相应特征值对应的广义特征向量组成)。
        -   $\mathbb{C}^n = G_{\lambda_1} \oplus G_{\lambda_2} \oplus \dots \oplus G_{\lambda_r}$ (整个空间可以分解为所有广义特征空间的直和)。
-   **重要注记 (Notes on Generalized Eigenspaces)** :
    -   普通特征空间 $E_{\lambda_i} = \ker(A-\lambda_i I_n)$ 是 $G_{\lambda_i}$ 的子空间。
    -   $A$ 可对角化当且仅当对所有 $i$ 都有 $G_{\lambda_i} = E_{\lambda_i}$。
    -   如果 $\lambda_i$ 是单根 ($m_i=1$)，则 $G_{\lambda_i} = E_{\lambda_i}$。
    -   有子空间链 $E_{\lambda_i} \subseteq \ker((A-\lambda_i I_n)^2) \subseteq \dots \subseteq \ker((A-\lambda_i I_n)^{m_i}) = G_{\lambda_i}$。
-   **核心定理 (Main Theorem for Solutions)** (Slide 35):
    1.  设 $B = \{\mathbf{v}_1, \dots, \mathbf{v}_n\}$ 是由 $A$ 的广义特征向量构成的 $\mathbb{C}^n$ 的一组基。
        如果 $\mathbf{v}_j \in B$ 是与特征值 $\lambda_i$ (代数重数为 $m_i$) 相关联的广义特征向量，则定义函数
        $$
        \mathbf{y}_j(t) = \sum_{k=0}^{m_i-1} \frac{t^k}{k!} e^{\lambda_i t} (A - \lambda_i I_n)^k \mathbf{v}_j = e^{\lambda_i t} \left( \mathbf{v}_j + t(A-\lambda_i I_n)\mathbf{v}_j + \frac{t^2}{2!}(A-\lambda_i I_n)^2\mathbf{v}_j + \dots \right)
        $$
        (注意这里的求和上限是 $m_i-1$，因为如果 $k \ge m_i$，则 $(A-\lambda_i I_n)^k \mathbf{v}_j = \mathbf{0}$ 如果 $\mathbf{v}_j \in G_{\lambda_i}$)。
        这些函数 $\mathbf{y}_1(t), \dots, \mathbf{y}_n(t)$ 构成 $\mathbf{y}'=A\mathbf{y}$ 的一个基本解组 (fundamental system of solutions)。
    2.  矩阵指数可以表示为：
        $$
        e^{At} = (\mathbf{y}_1(t) | \dots | \mathbf{y}_n(t)) (\mathbf{v}_1 | \dots | \mathbf{v}_n)^{-1}
        $$
        其中 $(\mathbf{v}_1 | \dots | \mathbf{v}_n)$ 是由基向量 $\mathbf{v}_j$ 构成的矩阵 $S$。
-   **证明概要 (Proof Outline)** (Slide 36):
    -   已证明 $\mathbf{y}_j(t)$ 是解。
    -   关键在于证明线性无关性。由于 $\mathbf{y}_j(0) = \mathbf{v}_j$ (从 $\mathbf{y}_j(t)$ 的定义式中令 $t=0$ 可得)，且 $\mathbf{v}_j$ 构成一组基，因此 $\mathbf{y}_j(t)$ 也线性无关。
    -   第 (2) 部分是 $e^{At} = \Phi(t)\Phi(0)^{-1}$ 的一个实例。

#### B2. 应用与计算 (Application and Computation) (Slides 37-57, 59)

-   **例子: $A = \begin{pmatrix} 1 & -1 \\ 1 & 3 \end{pmatrix}$** (Slides 37-38)
    -   特征多项式 $\chi_A(X) = X^2 - 4X + 4 = (X-2)^2$。
    -   单一特征值 $\lambda=2$，代数重数 $m=2$。
    -   $G_{\lambda=2} = \mathbb{C}^2$。我们选择标准基 $B = \{\mathbf{e}_1, \mathbf{e}_2\}$ 作为广义特征向量基。
        -   对 $\mathbf{v}_1 = \mathbf{e}_1 = \begin{pmatrix} 1 \\ 0 \end{pmatrix}$:
            $(A-2I)\mathbf{e}_1 = \begin{pmatrix} -1 & -1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} 1 \\ 0 \end{pmatrix} = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$。
            $(A-2I)^2\mathbf{e}_1 = \begin{pmatrix} -1 & -1 \\ 1 & 1 \end{pmatrix} \begin{pmatrix} -1 \\ 1 \end{pmatrix} = \begin{pmatrix} 0 \\ 0 \end{pmatrix}$。
            $\mathbf{y}_1(t) = e^{2t}(\mathbf{e}_1 + t(A-2I)\mathbf{e}_1) = e^{2t}\begin{pmatrix} 1 \\ 0 \end{pmatrix} + te^{2t}\begin{pmatrix} -1 \\ 1 \end{pmatrix} = e^{2t}\begin{pmatrix} 1-t \\ t \end{pmatrix}$。
        -   对 $\mathbf{v}_2 = \mathbf{e}_2 = \begin{pmatrix} 0 \\ 1 \end{pmatrix}$:
            $(A-2I)\mathbf{e}_2 = \begin{pmatrix} -1 \\ 1 \end{pmatrix}$。
            $\mathbf{y}_2(t) = e^{2t}(\mathbf{e}_2 + t(A-2I)\mathbf{e}_2) = e^{2t}\begin{pmatrix} 0 \\ 1 \end{pmatrix} + te^{2t}\begin{pmatrix} -1 \\ 1 \end{pmatrix} = e^{2t}\begin{pmatrix} -t \\ 1+t \end{pmatrix}$。
    -   基本矩阵 $\Phi(t) = (\mathbf{y}_1(t) | \mathbf{y}_2(t)) = e^{2t}\begin{pmatrix} 1-t & -t \\ t & 1+t \end{pmatrix}$。
    -   由于 $\Phi(0) = I_2$ (因为我们用了标准基作为 $\mathbf{v}_j$)，所以 $e^{At} = \Phi(t)$。

-   **若尔当标准型 (Jordan Canonical Form - JCF)** (Slides 39-40 (notes), 59 (point 3)):
    -   任何矩阵 $A$ 都可以通过相似变换 $S^{-1}AS = J$ 转化为其若尔当标准型 $J$。
    -   $J$ 是一个分块对角矩阵，每个对角块 $J_i$ 是一个若尔当块 (Jordan block)，形如：
        $$
        J_i = \begin{pmatrix} \lambda_i & 1 & & \\ & \lambda_i & \ddots & \\ & & \ddots & 1 \\ & & & \lambda_i \end{pmatrix}
        $$
    -   $e^{At} = S e^{Jt} S^{-1}$。
    -   $e^{Jt} = \text{diag}(e^{J_1 t}, \dots, e^{J_r t})$。
    -   计算 $e^{J_i t}$: $J_i = \lambda_i I + N_i$，其中 $N_i$ 是一个主对角线上方元素为1的幂零矩阵 (nilpotent matrix)。
        由于 $\lambda_i I$ 和 $N_i$ 可交换，所以 $e^{J_i t} = e^{(\lambda_i I + N_i)t} = e^{\lambda_i t I} e^{N_i t} = e^{\lambda_i t} e^{N_i t}$。
        $e^{N_i t} = I + N_i t + \frac{(N_i t)^2}{2!} + \dots + \frac{(N_i t)^{k-1}}{(k-1)!}$ (如果 $N_i$ 是 $k \times k$ 且 $N_i^k=0$)。
        例如，如果 $J_i = \begin{pmatrix} \lambda_i & 1 \\ 0 & \lambda_i \end{pmatrix}$, $N_i = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, $N_i^2=0$。
        $e^{J_i t} = e^{\lambda_i t} (I + N_i t) = e^{\lambda_i t} \begin{pmatrix} 1 & t \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} e^{\lambda_i t} & t e^{\lambda_i t} \\ 0 & e^{\lambda_i t} \end{pmatrix}$。
    -   Slide 40-41 进一步解释了如何使用这种分块形式，以及 $e^{A_i t}$ 的级数会因 $(A_i - \lambda_i I)^{m_i}=0$ 而截断。
-   **寻找广义特征向量基的策略 (Strategy for finding basis of generalized eigenvectors)** (Slides 42-45, "Notes on the theorem"):
    -   $\mathbf{w}_k = (A - \lambda_i I_n)^k \mathbf{v}_j$ 本身也是广义特征向量。
    -   $\mathbf{y}_j(t)$ 的定义中的求和项会终止。
    -   **链 (Chains)**: $\mathbf{w}_0, \mathbf{w}_1, \dots, \mathbf{w}_k$ (其中 $\mathbf{w}_k \neq \mathbf{0}, \mathbf{w}_{k+1}=\mathbf{0}$) 线性无关。$\mathbf{w}_k$ 是普通特征向量。
    -   一个广义特征空间 $G_{\lambda_i}$ 的基可以由若干这样的链构成。
    -   **"深度优先" 策略 (Depth-first strategy)** (Slide 44):
        1.  找到使 $\ker((A-\lambda_i I)^k) = G_{\lambda_i}$ 的最小 $k$。
        2.  选择一个 $\mathbf{w} \in G_{\lambda_i}$ 使得 $(A-\lambda_i I)^{k-1}\mathbf{w} \neq \mathbf{0}$。
        3.  这生成一个长度为 $k$ 的链 $\mathbf{w}_0=\mathbf{w}, \mathbf{w}_1=(A-\lambda_i I)\mathbf{w}, \dots, \mathbf{w}_{k-1}=(A-\lambda_i I)^{k-1}\mathbf{w}$。
        4.  如果这些向量的张成空间还不是 $G_{\lambda_i}$，则在补空间中重复此过程。
        5.  一个长度为 $k$ 的链会产生 $k$ 个形式上越来越简单的基本解 (Slide 45)。
-   **例子: $A = \begin{pmatrix} -26 & 49 & 74 \\ -8 & 16 & 25 \\ -4 & 7 & 10 \end{pmatrix}$** (Slides 46-48)
    -   $\chi_A(X) = (X-2)(X+1)^2$。特征值 $\lambda_1=2$ (重数1)，$\lambda_2=-1$ (重数2)。
    -   $\lambda_1=2$: 特征向量 $\mathbf{v}_1 = (7,4,0)^T$。解 $\mathbf{y}_1(t) = e^{2t}\mathbf{v}_1$。
    -   $\lambda_2=-1$: $A+I = \begin{pmatrix} -25 & 49 & 74 \\ -8 & 17 & 25 \\ -4 & 7 & 11 \end{pmatrix}$。 $\ker(A+I)$ 的维数 (几何重数) 是1，由 $\mathbf{v}_2 = (-1,1,-1)^T$ 张成。
        由于代数重数是2，几何重数是1，$A$ 不可对角化。
        我们需要一个广义特征向量 $\mathbf{v}_3$ 使得 $(A+I)\mathbf{v}_3 = \mathbf{v}_2$ (且 $(A+I)^2\mathbf{v}_3 = \mathbf{0}$)。
        解 $\begin{pmatrix} -25 & 49 & 74 \\ -8 & 17 & 25 \\ -4 & 7 & 11 \end{pmatrix} \mathbf{v}_3 = \begin{pmatrix} -1 \\ 1 \\ -1 \end{pmatrix}$，得到 $\mathbf{v}_3 = (2,1,0)^T$ (Slide 48)。
    -   基本解组：
        $\mathbf{y}_1(t) = e^{2t}\mathbf{v}_1$
        $\mathbf{y}_2(t) = e^{-t}\mathbf{v}_2$ (来自特征向量 $\mathbf{v}_2$)
        $\mathbf{y}_3(t) = e^{-t}(\mathbf{v}_3 + t(A+I)\mathbf{v}_3) = e^{-t}(\mathbf{v}_3 + t\mathbf{v}_2)$ (来自广义特征向量 $\mathbf{v}_3$)
-   **复杂例子 (A more complex example)** (Slides 49-56): 一个 $6 \times 6$ 矩阵。
    -   特征多项式 $\chi_A(X) = (X-4)^2(X+2)^4$。
    -   $\lambda_1=4$ (代数重数2)。计算 $\ker(A-4I)$ 得到2个线性无关的特征向量 $\mathbf{v}_1, \mathbf{v}_2$ (Slide 51)。这意味着对应于 $\lambda_1=4$ 的若尔当块都是 $1 \times 1$ 的，即它是可对角化的部分。
    -   $\lambda_2=-2$ (代数重数4)。计算 $\ker(A+2I)$ 得到2个线性无关的特征向量 (Slide 52，记为 $\mathbf{v}_3, \mathbf{v}_4$)。几何重数为2。
        这意味着对应于 $\lambda_2=-2$ 的若尔当结构由2个若尔当块组成，总大小为4。可能是两个 $2 \times 2$ 块，或者一个 $3 \times 1$ 和一个 $1 \times 1$ 块。
    -   计算 $(A+2I)^2$ 和 $(A+2I)^3$ (Slide 53)。发现 $\text{rank}((A+2I)^3)=2$，所以 $\dim(\ker((A+2I)^3))=4$。这说明最长的链长度为3。
        因此，若尔当块是 $J_1(-2)$ (大小3) 和 $J_2(-2)$ (大小1)。
    -   选择 $\mathbf{w}_1 = \mathbf{e}_2$ 使得 $(A+2I)^2\mathbf{w}_1 \neq \mathbf{0}$ (Slide 54)。
        生成链: $\mathbf{w}_1=\mathbf{e}_2$, $\mathbf{w}_2=(A+2I)\mathbf{w}_1$, $\mathbf{w}_3=(A+2I)^2\mathbf{w}_1$。$\mathbf{w}_3$ 是一个特征向量。
        另一个特征向量 $\mathbf{w}_4$ (即 $\mathbf{v}_4$ from Slide 52) 线性独立于 $\mathbf{w}_3$。
    -   基本解 (Slide 55):
        $\mathbf{y}_1(t)=e^{4t}\mathbf{v}_1, \mathbf{y}_2(t)=e^{4t}\mathbf{v}_2$
        $\mathbf{y}_3(t)=e^{-2t}(\mathbf{w}_1 + t\mathbf{w}_2 + \frac{t^2}{2}\mathbf{w}_3)$ (来自长度为3的链)
        $\mathbf{y}_4(t)=e^{-2t}(\mathbf{w}_2 + t\mathbf{w}_3)$ (来自长度为3的链)
        $\mathbf{y}_5(t)=e^{-2t}\mathbf{w}_3$ (来自长度为3的链)
        $\mathbf{y}_6(t)=e^{-2t}\mathbf{w}_4$ (来自长度为1的链，即普通特征向量)
    -   Slide 56 展示了用 SageMath 计算得到的 $e^{At}$ 的最终形式。
-   **对角化矩阵的特解 (Alternative method for particular solution for diagonalizable A)** (Slide 57):
    如果 $A$ 可对角化，$\mathbf{y}' = A\mathbf{y} + \mathbf{q}(t)$。可以将 $\mathbf{q}(t)$ 在 $A$ 的特征向量基底下展开 $\mathbf{q}(t) = \sum q_i(t)\mathbf{v}_i$ (这里符号与slide稍有不同，slide中 $q(t)$ 分解为 $q_1(t)+q_2(t)$，其中 $q_i(t)$ 本身是向量)。
    然后对每个分量 $z_i' = \lambda_i z_i + q_i(t)$ 单独求解。
    这在某些情况下可能比直接用参数变易法简单。

### C. 基于Cayley-Hamilton定理或最小多项式 (Based on Cayley-Hamilton Theorem or Minimal Polynomial) 

#### 总结

**核心目标**：将 $e^{At}$ 表示为 $e^{At} = c_0(t)I + c_1(t)A + \dots + c_{d-1}(t)A^{d-1}$，并求解系数函数 $c_k(t)$。

**步骤 1: 确定零化多项式 $a(X)$及其次数 $d$**

-   计算矩阵 $A$ 的特征多项式 $\chi_A(X) = \det(A-XI)$。
-   令选定的多项式为 $a(X)$，其次数为 $d$。

**步骤 2: 写出 $e^{At}$ 的多项式形式**

-   根据 $a(X)$ 的次数 $d$，写出：
    $$
    e^{At} = c_0(t)I + c_1(t)A + c_2(t)A^2 + \dots + c_{d-1}(t)A^{d-1}
    $$
    其中 $c_0(t), c_1(t), \dots, c_{d-1}(t)$ 是待求的时间函数。



**步骤 3: 确定系数函数 $c_k(t)$ 满足的标量 ODE**

-   所有系数函数 $c_k(t)$ 都满足同一个 $d$ 阶标量常系数线性齐次微分方程：
    $$
    a(D)y = 0
    $$
    其中 $D = \frac{d}{dt}$ 是微分算子，$a(D)$ 是将 $a(X)$ 中的 $X$ 替换为 $D$ 得到的微分算子。
    例如，如果 $a(X) = X^2 + pX + q$，则 $a(D)y = y'' + py' + qy = 0$。


**步骤 4: 求解每个系数函数 $c_k(t)$**

-   对于每个 $k = 0, 1, \dots, d-1$，函数 $c_k(t)$ 是以下初值问题 (IVP) 的唯一解：
    -   **微分方程**: $a(D)y = 0$
    -   **初始条件**:
        $$
        y^{(j)}(0) = \delta_{jk} \quad \text{for } j = 0, 1, \dots, d-1
        $$
        其中 $\delta_{jk}$ 是 Kronecker delta ($j=k$ 时为 1，否则为 0)。
        这意味着对于 $c_k(t)$：
        $c_k(0) = 0, \dots, c_k^{(k-1)}(0) = 0, \quad c_k^{(k)}(0) = 1, \quad c_k^{(k+1)}(0) = 0, \dots, c_k^{(d-1)}(0) = 0$

    **实际求解方法**:
    1.  找到 $a(D)y=0$ 的 $d$ 个线性无关的基本解 $y_1(t), y_2(t), \dots, y_d(t)$。
    2.  对每个 $c_k(t)$，可以写成 $c_k(t) = \sum_{m=1}^d \alpha_{km} y_m(t)$。
    3.  利用上述初始条件确定常数 $\alpha_{km}$。
        (或者使用 Slide 71 中基于 Wronskian 矩阵逆的方法一次性求出所有 $c_k(t)$ 对应的组合系数)。

**步骤 5: 代入并组合得到 $e^{At}$**

-   将求解得到的 $c_0(t), c_1(t), \dots, c_{d-1}(t)$ 以及计算出的 $A$ 的幂次代回到步骤 2 的表达式中：
    $$
    e^{At} = c_0(t)I + c_1(t)A + c_2(t)A^2 + \dots + c_{d-1}(t)A^{d-1}
    $$
-   进行矩阵的数乘和加法运算得到最终的 $e^{At}$ 矩阵。


#### 理论

这种方法提供了一种不直接计算特征向量或若尔当型就能得到 $e^{At}$ 的途径。

-   **核心定理 (Main Theorem)** :
    假设存在一个多项式 $a(X) = a_0 + a_1 X + \dots + a_d X^d$ 使得 $a(A) = \mathbf{0}$。(根据 Cayley-Hamilton 定理，$A$ 的特征多项式 $\chi_A(X)$ 满足 $\chi_A(A)=\mathbf{0}$。最小多项式 $\mu_A(X)$ 是满足此条件的次数最低的首一多项式，且 $\mu_A(X)$ 整除 $\chi_A(X)$。这里 $d$ 是 $a(X)$ 的次数。)
    1.  $e^{At}$ 的每个元素 $e_{ij}(t)$ 都满足标量常微分方程 $a(D)y=0$ (其中 $D = d/dt$)。
    2.  $e^{At}$ 可以表示为 $A$ 的一个次数严格小于 $d$ 的多项式，其系数是 $t$ 的函数：
        $$
        e^{At} = c_0(t)I_n + c_1(t)A + \dots + c_{d-1}(t)A^{d-1}
        $$
        其中函数 $c_k(t)$ 是标量 ODE $a(D)y=0$ 的解，并且满足特定的初始条件：
        对于每个 $k \in \{0, 1, \dots, d-1\}$，$c_k(t)$ 满足
        $c_k^{(j)}(0) = \delta_{kj}$ (Kronecker delta)，即在 $j=k$ 时导数为1，其他导数为0。
        更形象地说，如果把这些 $c_k(t)$ 函数及其直到 $d-1$ 阶的导数在 $t=0$ 的值排成一个矩阵 $W(t) = [c_j^{(i)}(t)]$ (Wronskian 矩阵的思想)，那么 $W(0) = I_d$ (d阶单位矩阵)。
        Slide 65 将初始条件表述为：$(y(0), y'(0), \dots, y^{(d-1)}(0)) = \mathbf{e}_{k+1}$ (第 $k+1$ 个标准单位向量) 时，解是 $c_k(t)$。
-   **推论 (Corollary)** :
    $c_k(t)$ 的具体形式由 $a(X)$ (通常取最小多项式 $\mu_A(X)$) 的根 $\lambda_i$ 及其重数 $m_i$ 决定。
    如果 $\mu_A(X) = \prod_{i=1}^r (X-\lambda_i)^{m_i}$，则每个 $c_k(t)$ 都是 $\sum_{j=1}^r P_j(t)e^{\lambda_j t}$ 的形式，其中 $P_j(t)$ 是次数小于 $m_j$ 的多项式。
-   **证明概要 (Proof Outline)** (Slide 67):
    -   (1) 因为 $a(A)=\mathbf{0}$，且 $\frac{d}{dt}e^{At}=Ae^{At}$，所以 $a(D)e^{At} = a(A)e^{At} = \mathbf{0} \cdot e^{At} = \mathbf{0}$ (矩阵)。这意味着 $e^{At}$ 的每个元素都满足 $a(D)y=0$。
    -   (2) 定义 $\Phi(t) = c_0(t)I + \dots + c_{d-1}(t)A^{d-1}$。由于 $c_j(t)$ 的初始条件，可以验证 $\Phi^{(i)}(0) = A^i$ 对于 $0 \le i \le d-1$。
        同时，$e^{At}$ 也满足 $\frac{d^i}{dt^i}e^{At}|_{t=0} = A^i$。
        由于 $\Phi(t)$ 和 $e^{At}$ 都满足 $a(D)Y=\mathbf{0}$ 以及相同的 $d$ 个初始条件 (在 $t=0$ 时的值及其直到 $d-1$ 阶导数)，根据解的唯一性，它们必须相等。
-   **例子: $A = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$** (Slide 68)
    -   $\chi_A(X) = X^2+1$。所以 $a(X)=X^2+1$, $d=2$。
    -   $e^{At} = c_0(t)I + c_1(t)A$。
    -   $c_0(t)$ 满足 $y''+y=0, y(0)=1, y'(0)=0 \implies c_0(t)=\cos t$。
    -   $c_1(t)$ 满足 $y''+y=0, y(0)=0, y'(0)=1 \implies c_1(t)=\sin t$。
    -   $e^{At} = (\cos t)I + (\sin t)A = \begin{pmatrix} \cos t & \sin t \\ -\sin t & \cos t \end{pmatrix}$。
-   **例子: 投影矩阵 (Projection Matrix) $P^2=P$** (Slide 69)
    -   如果 $P \neq 0, I$，则最小多项式 $\mu_P(X)=X^2-X = X(X-1)$。所以 $a(X)=X^2-X, d=2$。
    -   $e^{Pt} = c_0(t)I + c_1(t)P$。
    -   $c_0(t)$ 满足 $y''-y'=0, y(0)=1, y'(0)=0 \implies y'(t)=0 \implies y(t)=1 \implies c_0(t)=1$。
    -   $c_1(t)$ 满足 $y''-y'=0, y(0)=0, y'(0)=1 \implies y'(t)=e^t \implies y(t)=e^t-1 \implies c_1(t)=e^t-1$。
    -   $e^{Pt} = I + (e^t-1)P$。
-   **例子: 之前的 $3 \times 3$ 不可对角化矩阵 $A$** (Slides 70-72)
    -   $\chi_A(X) = (X-2)(X+1)^2 = X^3 - 3X - 2$。所以 $a(X)=X^3-3X-2, d=3$。
    -   $e^{At} = c_0(t)I + c_1(t)A + c_2(t)A^2$。
    -   $c_0, c_1, c_2$ 都是 ODE $y''' - 3y' - 2y = 0$ 的解，该 ODE 的基本解组是 $e^{2t}, e^{-t}, te^{-t}$。
    -   初始条件:
        $c_0(0)=1, c_0'(0)=0, c_0''(0)=0$
        $c_1(0)=0, c_1'(0)=1, c_1''(0)=0$
        $c_2(0)=0, c_2'(0)=0, c_2''(0)=1$

## 第四部分：时变系数系统 (Time-Dependent Coefficient Systems) (Slide 73)

-   当系统为 $\mathbf{y}' = A(t)\mathbf{y}$ 时，即系数矩阵 $A$ 依赖于时间 $t$。
-   **指数矩阵 $e^{B(t)}$ (Exponential Matrix)**: $e^{B(t)} = \sum_{k=0}^\infty \frac{1}{k!} (B(t))^k$ 定义良好。
-   **关键问题**: $\frac{d}{dt} e^{B(t)}$ 一般不等于 $B'(t)e^{B(t)}$。
    这是因为 $(B(t)^k)' \neq k B(t)^{k-1}B'(t)$ 一般不成立，除非 $B(t)$ 和 $B'(t)$ 可交换。
    例如，$(B(t)^2)' = B'(t)B(t) + B(t)B'(t)$。
-   因此，$\mathbf{y}(t) = e^{\int A(s)ds} \mathbf{c}$ **通常不是** $\mathbf{y}' = A(t)\mathbf{y}$ 的解。
-   **特殊情况 (Special Case)**:
    如果 $A(t)$ 与其积分 $B(t) = \int_{t_0}^t A(s)ds + B_0$ (实际上是 $A(t)$ 与 $B(t)$ 中任意两个时刻的值可交换，一个更强的条件是 $A(t_1)$ 与 $A(t_2)$ 对任意 $t_1,t_2$ 可交换) 处处可交换，则 $\mathbf{y}(t) = e^{B(t)}\mathbf{c}$ 是解。
    (更准确地说，如果 $A(t)$ 与 $\int A(s)ds$ 可交换，则 $e^{\int A(s)ds}$ 是解。)
