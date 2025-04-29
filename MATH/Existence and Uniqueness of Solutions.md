---
title: Existence and Uniqueness of Solutions
date: 2025-04-03
date modified: 2025-04-05
categories: Math285
tags: [Math285]
---

#Math285 

> [!tip] 概要
> 本节我们主要阐述n维一阶ODE解的存在性与唯一性定理
> - 将定理推广到覆盖 $n$ 维一阶 ODE 系统，其向量形式为 $y' = f(t, \mathbf{y})$，其中 $y \in \mathbb{R}^n$。这一点至关重要，因为它允许我们通过将高阶标量 ODE 转化为一阶系统，从而将结果应用于高阶 ODE。
> - 放宽对函数 $f(t, y)$ 的条件。我们将使用一个称为关于 $y$ 的 **利普希茨条件 (Lipschitz condition)** 的较弱条件，而不是要求 $f$ 对 $y$ 的分量具有连续偏导数。这个更宽泛的条件使得定理能够覆盖更多在应用中 (尤其是在工程数学中) 很重要的 ODE 类型。


## Lipschitz Conditions

### Definition

*   **1. 定义**
    *   我们考虑一个函数 $f: D \to \mathbb{R}^n$，其定义域 $D$ 是 $\mathbb{R} \times \mathbb{R}^n$ 的一个子集。你可以将 $t$ 想象成时间，$y$ 想象成状态向量。
    *   我们说 $f(t, y)$ 在 $D$ 上关于 $y$ 满足 **Lipschitz 条件**，是指存在一个常数 $L > 0$ (称为 **利普希茨常数 (Lipschitz constant)**)，使得对于 $D$ 中的任意两个点 $(t, y_1)$ 和 $(t, y_2)$ (注意它们的 $t$ 值相同)：
        $$
        |f(t, y_1) - f(t, y_2)| \le L |y_1 - y_2|
        $$
        这里的 $|\cdot|$ 表示 $\mathbb{R}^n$ 中的欧几里得范数 (Euclidean norm)。这个条件本质上限制了当你改变 $y$ 时，函数 $f$ 的变化速度，并且这种限制对所有 $t$ 是一致的。
        *   *技术比喻 (Technical Analogy):* 想象函数值 $f(t, y)$ 代表在时间 $t$ 和位置 $y$ 处某个地貌的海拔高度。Lipschitz 条件意味着该地貌在 $y$ 方向的坡度是有界的；它不可能是无限陡峭的。Lipschitz 常数 $L$ 就是这个陡峭程度的界限。**对于满足条件的函数，只要我们能够控制自变量的变化，就能够控制因变量的增长**
    *   我们说 $f$ 关于 $y$ 满足 **局部利普希茨条件 (locally Lipschitz condition)**，是指对于 *每一个* 点 $(t_0, y_0) \in D$，都存在一个它周围的邻域 $D'$ (包含在 $D$ 内)，在这个邻域上 Lipschitz 条件对某个常数 $L$ 成立。这个 $L$ 对于不同的邻域可能是不同的。这个局部版本是我们将在定理中主要使用的。

### Proposition

*   **2. 命题**
    *   这个命题提供了一个检验局部 Lipschitz 条件的常用方法：
      如果函数 $f: D \to \mathbb{R}^n$ 在**开集 $D$** 上关于变量 $y = (y_1, \dots, y_n)$ 具有**连续的偏导数**，那么 $f$ 在 $D$ 上关于 $y$ 满足局部 Lipschitz 条件。
    *   **证明思路 (Proof Idea):**
        1.  对于 $D$ 中的任意点 $(a, b)$，因为 $D$ 是开集，我们可以找到一个围绕 $(a, b)$ 的闭凸邻域 $V$ (例如一个小的矩形区域 $V = \{(t, y) \mid |t-a| \le r, |y-b| \le r\}$)，它完全包含在 $D$ 中。
        2.  对固定 $t$，将 **中值定理 (Mean Value Theorem)** (向量值函数的积分形式) 应用于函数 $g(y) = f(t, y)$。这给出：
            $$
            f(t, y_1) - f(t, y_2) = \left( \int_0^1 J_{f,y}(t, y_1 + s(y_2 - y_1)) ds \right) (y_1 - y_2)
            $$
            其中 $J_{f,y}$ 是 $f$ 关于 $y$ 的 **雅可比矩阵 (Jacobian matrix)**，包含偏导数 $\partial f_i / \partial y_j$。我们将积分得到的矩阵记为 $A(t, y_1, y_2)$。
        3.  由于**偏导数在紧集 $V$ 上是连续的，因此它们在 $V$ 上是有界的**。设 $M$ 是 $V$ 中所有 $|\partial f_i / \partial y_j|$ 的一个上界。
        4.  然后我们可以界定矩阵 $A$ 的范数。幻灯片 7 使用了 Frobenius 范数 $||A||_F$，并表明 $||A||_F \le \sqrt{n^2 M^2} = nM$。利用性质 $|Av| \le ||A||_F |v|$，我们得到：
            $$
            |f(t, y_1) - f(t, y_2)| \le ||A||_F |y_1 - y_2| \le nM |y_1 - y_2|
            $$
        5.  因此，$f$ 在邻域 $V$ 上是 Lipschitz 的，Lipschitz 常数为 $L = nM$。因为这对任何点 $(a, b)$ 都适用，所以 $f$ 是局部 Lipschitz 的。

### Example
*   **3.例子: 艾里方程 (Airy's Equation)**
    *   二阶 ODE $y'' = ty$ 通过令 $y_0 = y, y_1 = y'$ 转化为一阶系统。该系统为 $y' = (y_0', y_1')^T = (y_1, ty_0)^T$。因此，$\mathbf{f}(t, y) = (y_1, ty_0)^T$，其中 $y = (y_0, y_1)^T$。
    *   函数 $\mathbf{f}$ 的偏导数为：$\partial f_1/\partial y_0 = 0, \partial f_1/\partial y_1 = 1, \partial f_2/\partial y_0 = t, \partial f_2/\partial y_1 = 0$。这些在任何地方都是连续的。因此，根据命题，$\mathbf{f}$ 在 $\mathbb{R} \times \mathbb{R}^2$ 上关于 $y$ 是局部 Lipschitz 的。
    *  直接推导：
        $$
        |\mathbf{f}(t, y) - \mathbf{f}(t, z)| = \sqrt{(y_1 - z_1)^2 + (t y_0 - t z_0)^2} = \sqrt{(y_1 - z_1)^2 + t^2 (y_0 - z_0)^2}
        $$
        如果我们将 $t$ 限制在一个区间 $|t| \le R$ (并假设 $R \ge 1$)，那么：
        $$
        |\mathbf{f}(t, y) - \mathbf{f}(t, z)| \le \sqrt{R^2(y_1 - z_1)^2 + R^2 (y_0 - z_0)^2} = R |y - z|
        $$
        所以，$\mathbf{f}$ 在任何带状区域 $[-R, R] \times \mathbb{R}^2$ 上都是 Lipschitz 的，其 Lipschitz 常数为 $L=R$ (对于 $R \ge 1$)。这证实了它处处是局部 Lipschitz 的。幻灯片 9 指出，对于一个点 $(t, y)$，我们可以取邻域 $V = [t-1, t+1] \times \mathbb{R}^2$ 并使用 $L = |t|+1$。

### Remarks
*   **4. 备注**
    *   我们可以联系单变量函数 $f: [a, b] \to \mathbb{R}$ 与 Lipschitz 连续性。它提到紧区间上的 $C^1$ 函数是 Lipschitz 的，并且 Lipschitz 连续性意味着 **一致连续性 (uniform continuity)** (但反之不成立，例如 $[0, \infty)$ 上的 $\sqrt{x}$)。
    *   **线性映射 (linear maps)** $f(x) = Ax$ 是 Lipschitz 的，其 $L = ||A||$ (算子范数)。它还指出 $f(x) = \sqrt{x}$ 在 $x=0$ 附近不是 Lipschitz 的。
    *   这个概念推广到任意 **度量空间 (metric spaces)** $(M, d)$ 和 $(M', d')$ 之间的映射：$d'(T(x), T(y)) \le L d(x, y)$。它将此与 **巴拿赫不动点定理 (Banach's Fixed Point Theorem)** 中使用的 **压缩映射 (contraction mappings)** 联系起来，此时 $L < 1$。


### Connections to Integral Equations
**5. 与积分方程的联系**

*  一个由 ODE $y' = f(t, y)$ 和初始条件 $y(t_0) = y_0$ 组成的 **初值问题 (Initial Value Problem, IVP)** 等价于一个 **积分方程 (integral equation)**。
*   一个在包含 $t_0$ 的区间 $I$ 上定义的连续函数 $\phi(t)$ 是该 IVP 的解，*当且仅当* 它满足：
    $$
    \phi(t) = y_0 + \int_{t_0}^t f(\tau, \phi(\tau)) d\tau \quad \text{对于所有 } t \in I
    $$
*   这个等价性是由微积分基本定理建立的。如果 $\phi(t)$ 满足积分方程，对其求导得到 $\phi'(t) = f(t, \phi(t))$，并且令 $t=t_0$ 得到 $\phi(t_0)=y_0$。反之，将 $\phi'(t) = f(t, \phi(t))$ 从 $t_0$ 积分到 $t$ 就得到积分方程。
*   这种重新表述是关键，因为证明积分方程的存在性和唯一性通常更容易处理，特别是使用像不动点定理这样的分析工具。


## The Uniqueness Theorem

### Theorem Statement

> [!tip] **定理陈述 :** **唯一性定理 (Uniqueness Theorem)**
> 假设 $f(t, y)$ 在**开区域**$D \subseteq \mathbb{R} \times \mathbb{R}^n$ 上**连续**，并且关于 $y$ 满足**局部 Lipschitz 条件**。如果 $\phi: I \to \mathbb{R}^n$ 和 $\psi: I \to \mathbb{R}^n$ 是同一区间 $I$ 上同一个 IVP $y' = f(t, y), y(t_0) = y_0$ 的两个解，那么它们必须是相同的，即对于所有 $t \in I$，有 $\phi(t) = \psi(t)$。


*   **证明** 证明依赖于一个引理，该引理隐含地使用了 Gronwall 不等式。
    1.  **引理 (Lemma):** 如果两个解 $\phi$ 和 $\psi$ 在 $I$ 中的某点 $a$ 相等 (即 $\phi(a) = \psi(a)$)，那么它们必定在 $a$ 周围的一个小区间内相等，具体来说是对于某个 $\epsilon > 0$，在 $I \cap [a-\epsilon, a+\epsilon]$ 上相等。
    2.  **引理证明 (Proof of Lemma)**
        *   从积分形式开始：$\phi(t) - \psi(t) = \int_a^t [f(\tau, \phi(\tau)) - f(\tau, \psi(\tau))] d\tau$。
        *   取范数，并在 $(a, \phi(a))$ 的一个邻域 $V$ 内使用局部 Lipschitz 条件 (常数为 $L$)：
            $$
            |\phi(t) - \psi(t)| \le \left| \int_a^t |f(\tau, \phi(\tau)) - f(\tau, \psi(\tau))| d\tau \right| \le \left| \int_a^t L |\phi(\tau) - \psi(\tau)| d\tau \right|
            $$
            (积分外的绝对值处理了 $t<a$ 与 $t>a$ 的情况)。
        *   令 $M(t) = \max_{\tau \in [a, t] \text{ 或 } [t, a]} |\phi(\tau) - \psi(\tau)|$。那么上述不等式意味着 $|\phi(t) - \psi(t)| \le L |t-a| M(t)$。
        *   由于这对 $a$ 和 $t$ 之间的所有 $t'$ 都成立，所以 $M(t)$ 也必须满足 $M(t) \le L |t-a| M(t)$。
        *   选择足够小的 $\epsilon$ (例如 $\epsilon = \min\{\delta, 1/(2L)\}$，其中 $\delta$ 定义了局部 Lipschitz 条件成立的区间)，使得对于 $t \in I \cap [a-\epsilon, a+\epsilon]$，我们有 $L|t-a| \le L\epsilon \le 1/2$。
        *   那么 $M(t) \le (1/2) M(t)$，这只有当 $M(t) = 0$ 时才成立。
        *   因此，对于所有 $t \in I \cap [a-\epsilon, a+\epsilon]$，有 $\phi(t) = \psi(t)$。
    3.  **定理证明 (Proof of Theorem)** 使用反证法。假设 $\phi$ 和 $\psi$ 是不同的解。令 $A = \{t \in I \mid \phi(t) = \psi(t)\}$ (非空，因为 $t_0 \in A$) 且 $N = I \setminus A$ (假设非空)。
        *   考虑存在 $t_1 \in N$ 且 $t_1 > t_0$ 的情况。令 $t_2 = \inf \{ t \in N \mid t \ge t_0 \}$。由于 $A$ 相对于 $I$ 是闭集 (由连续性可知) 并且包含 $[t_0, t_0+\epsilon]$ (由引理可知)，$t_2$ 必定存在，$t_2 > t_0$，且 $t_2 \in A$。
        *   但如果 $t_2 \in A$，引理意味着 $\phi$ 和 $\psi$ 必须在 $[t_2, t_2 + \epsilon'] \cap I$ 上对于某个 $\epsilon' > 0$ 相等。这与 $t_2$ 是它们在 $t_0$ 之后开始不同的点的下确界相矛盾。
        *   如果 $N$ 包含小于 $t_0$ 的点，类似的论证也适用。
        *   因此，$N$ 必须是空集，即对于所有 $t \in I$，$\phi(t) = \psi(t)$。

### Examples and Remark
*   **例子和备注**
    *   **例 1:** $y' = \sqrt{|y|}$， $y(t_0)=0$。我们知道 $y_1(t)=0$ 是一个解。同时 $y_2(t) = \frac{1}{4}(t-t_0)|t-t_0|$ 是另一个解。唯一性失败了！为什么？函数 $f(y) = \sqrt{|y|}$ 在 $y=0$ 处不是 Lipschitz 的。它的导数在 $y=0$ 附近趋于无穷。定理在 $y=0$ 处的假设不满足。然而，对于 $y_0 \ne 0$ 的情况，$f$ 是局部 Lipschitz 的，因此只要解不碰到 $y=0$，唯一性就成立。
    *   **例 2:** $y' = y \ln|y|$ (对于 $y \ne 0$，$f(0)=0$)。$y(t)=0$ 是一个解。其他解是 $y(t) = \pm e^{c e^t}$。这些解永远不会达到 $y=0$。所以，尽管 $f(y) = y \ln|y|$ 在 $y=0$ 处不是局部 Lipschitz 的 (导数 $1+\ln|y| \to -\infty$)，但 $y(t_0)=0$ 的 IVP 确实有唯一解 ($y(t)=0$)。这表明 **Lipschitz 条件对于唯一性是充分的，但不是必要的**。
    *   **备注** 定理的条件 (f 连续性，关于 y 的局部 Lipschitz 性) 很常用，因为它们能导出相对简单的证明并覆盖许多应用场景。这些条件可以放宽 (例如，Peano 定理只需要连续性即可保证存在性；Osgood 条件则放宽了 Lipschitz 条件来保证唯一性)，但证明会变得更加困难。
    *   **练习:** 唯一性定理是否适用于 $y'=|y|$? 是的。$f(y)=|y|$ 是连续的。它是否 Lipschitz？$|f(y_1) - f(y_2)| = ||y_1| - |y_2|| \le |y_1 - y_2|$ (根据反三角不等式)。所以 $L=1$。它是全局 Lipschitz 的。定理适用，解是唯一的。


## Existence Theorem
**存在性定理 (皮卡-林德洛夫) (The Existence Theorem (Picard-Lindelöf))**

### Theorem Statement

> [!tip] 定理陈述
> **存在性定理 (Existence Theorem)** (通常称为 Picard-Lindelöf 定理)：
> 假设 $f(t, y)$ 在开区域 $D \subseteq \mathbb{R} \times \mathbb{R}^n$ 上**连续**，并且关于 $y$ 满足**局部 Lipschitz 条件**。那么对于任意初始点 $(t_0, y_0) \in D$，存在一个区间 $I = [t_0-\epsilon, t_0+\epsilon]$ (对于某个 $\epsilon > 0$) 以及至少一个 IVP $y' = f(t, y), y(t_0) = y_0$ 的解 $\phi: I \to \mathbb{R}^n$。


*   **证明策略 (Proof Strategy)** 证明使用了 **巴拿赫不动点定理 (Banach's Fixed Point Theorem)** 应用于我们之前定义的积分算子 $T$：$(T\phi)(t) = y_0 + \int_{t_0}^t f(\tau, \phi(\tau)) d\tau$。解就是算子 $T$ 的一个不动点 $\phi = T\phi$。
    1.  **构建空间 (Set up the Space)**
        *   找到一个以 $(t_0, y_0)$ 为中心且包含在 $D$ 中的闭矩形 (或高维中的闭圆柱体) $V = [t_0-r, t_0+r] \times \bar{B}(y_0, r)$。
        *   在这个紧集 $V$ 上，连续函数 $f$ 是有界的，设 $|f(t, y)| \le M$。同时，由于 $f$ 是局部 Lipschitz 的，它在 $V$ 上以某个常数 $L$ 满足 Lipschitz 条件。
        *   选择一个时间区间宽度 $\epsilon = \min\{r, r/M, 1/(2L)\}$。这个关键的选择确保了 $T$ 具有良好的性质。
        *   定义函数空间 $\mathcal{M}$ 为所有连续函数 $\phi: [t_0-\epsilon, t_0+\epsilon] \to \mathbb{R}^n$ 的集合，这些函数的图像保持在 $V$ 的 $y$ 部分内：对于所有 $t \in [t_0-\epsilon, t_0+\epsilon]$，$|\phi(t) - y_0| \le r$。
        *   为 $\mathcal{M}$ 配备最大范数 (或上确界范数) $||\phi - \psi||_\infty = \max_{t \in [t_0-\epsilon, t_0+\epsilon]} |\phi(t) - \psi(t)|$。这使得 $\mathcal{M}$ 成为一个 **完备度量空间 (complete metric space)** (它是区间上连续函数构成的 Banach 空间的闭子集)。
    2.  **证明 T 将 $\mathcal{M}$ 映射到 $\mathcal{M}$ (Show $T$ maps $\mathcal{M}$ into $\mathcal{M}$)** 对于任何 $\phi \in \mathcal{M}$，我们需要证明 $(T\phi)$ 也在 $\mathcal{M}$ 中。即需证明 $|(T\phi)(t) - y_0| \le r$。
        $$
        |(T\phi)(t) - y_0| = \left| \int_{t_0}^t f(\tau, \phi(\tau)) d\tau \right| \le \left| \int_{t_0}^t |f(\tau, \phi(\tau))| d\tau \right|
        $$
        因为 $\phi \in \mathcal{M}$，$(\tau, \phi(\tau))$ 在 $V$ 中，所以 $|f(\tau, \phi(\tau))| \le M$。
        $$
        |(T\phi)(t) - y_0| \le M |t - t_0| \le M \epsilon
        $$
        因为我们选择了 $\epsilon \le r/M$，所以 $M\epsilon \le r$。因此，$T\phi \in \mathcal{M}$。
    3.  **证明 T 是一个压缩映射 (Show $T$ is a Contraction Mapping):** 我们需要证明对于某个常数 $C < 1$，有 $||T\phi_1 - T\phi_2||_\infty \le C ||\phi_1 - \phi_2||_\infty$。
        $$
        |(T\phi_1)(t) - (T\phi_2)(t)| = \left| \int_{t_0}^t [f(\tau, \phi_1(\tau)) - f(\tau, \phi_2(\tau))] d\tau \right|
        $$
        $$
        \le \left| \int_{t_0}^t |f(\tau, \phi_1(\tau)) - f(\tau, \phi_2(\tau))| d\tau \right| \le \left| \int_{t_0}^t L |\phi_1(\tau) - \phi_2(\tau)| d\tau \right|
        $$
        $$
        \le L \left| \int_{t_0}^t ||\phi_1 - \phi_2||_\infty d\tau \right| = L |t - t_0| ||\phi_1 - \phi_2||_\infty \le L \epsilon ||\phi_1 - \phi_2||_\infty
        $$
        对 $t$ 取最大值得到 $||T\phi_1 - T\phi_2||_\infty \le (L\epsilon) ||\phi_1 - \phi_2||_\infty$。
        由于我们选择了 $\epsilon \le 1/(2L)$，常数 $C = L\epsilon \le 1/2 < 1$。因此 $T$ 是一个压缩映射。
    4.  **应用巴拿赫不动点定理 (Apply Banach Fixed Point Theorem)** 由于 $T$ 是完备度量空间 $\mathcal{M}$ 上的压缩映射，它在 $\mathcal{M}$ 中有唯一的**不动点 (fixed point)** $\phi^*$。这个不动点 $\phi^*$ 满足 $\phi^* = T\phi^*$，这意味着它解积分方程，并因此在区间 $[t_0-\epsilon, t_0+\epsilon]$ 上解 IVP。


### Notes and Iteration
*   **注释和迭代 (Notes and Iteration)**
    *   **皮卡-林德洛夫迭代 (Picard-Lindelöf Iteration):** Banach 定理还告诉我们如何找到不动点：通过迭代。从一个初始猜测 $\phi_0 \in \mathcal{M}$ 开始 (通常是常数函数 $\phi_0(t) = y_0$)，然后计算逐次逼近：
        $$
        \phi_{k+1}(t) = (T\phi_k)(t) = y_0 + \int_{t_0}^t f(\tau, \phi_k(\tau)) d\tau
        $$
        序列 $\phi_k(t)$ 在 $[t_0-\epsilon, t_0+\epsilon]$ 上 **一致收敛 (uniformly converges)** 到唯一的解 $\phi^*(t)$。


### Iteration Examples



**1. 皮卡-林德洛夫迭代法回顾 (Picard-Lindelöf Iteration Recap)**



皮卡-林德洛夫迭代法构造了一个函数序列，其定义如下：

1. 初始函数 (Initial function): $\phi_{0}(t) \equiv y_{0}$
2. 迭代步骤 (Iterative step): 
$$ \phi_{k+1}(t) = y_0 + \int_{t_0}^t f(\tau, \phi_k(\tau)) d\tau \quad \text{for } k = 0, 1, 2, \dots $$

定理证明的核心思想是利用 巴拿赫不动点定理 (Banach's Fixed Point Theorem。我们定义了一个算子 (operator) T:

$$
T\phi(t) = y_{0} + \int_{t_{0}}^{t}f(\tau,\phi(\tau))d \tau
$$


在合适的函数空间 (配备了均匀收敛度量 d∞​) 中，如果 f 满足局部 Lipschitz 条件 (Lipschitz condition) 且 t 的区间足够小，那么 T 是一个 压缩映射 (contraction mapping) 。这意味着 T 有唯一的不动点 ϕ∗，满足 Tϕ∗=ϕ∗，这个不动点就是我们要求的 IVP 的解 。同时，从任意初始函数 (比如 ϕ0​≡y0​) 开始应用算子 T 进行迭代得到的序列 ϕk+1​=Tϕk​，会收敛到这个不动点 ϕ∗ 


**2. 讲义中的例子 (Example from the Slides)** 
讲义中给出的例子是求解以下 IVP：

$$
y' = 2ty  \ \cap y(0) = 0
$$

我们来执行皮卡-林德洛夫迭代：

1. k = 0:
    $$
\phi_{0}(t) \equiv y_{0}
$$
    
2. k = 1:
    
  $$
    
    \begin{aligned}
    
    \phi_1(t) &= y_0 + \int_{0}^t f(\tau, \phi_0(\tau)) d\tau \\
    
    &= y_0 + \int_{0}^t 2\tau y_0 d\tau \\
    
    &= y_0 + 2y_0 \left[ \frac{\tau^2}{2} \right]_0^t \\
    
    &= y_0 + y_0 t^2 \\
    
    &= y_0 (1 + t^2)
    
    \end{aligned}$$
    

3. k = 2:
    
    $$
    
    \begin{aligned}
    
    \phi_2(t) &= y_0 + \int_{0}^t f(\tau, \phi_1(\tau)) d\tau \\
    
    &= y_0 + \int_{0}^t 2\tau [y_0 (1 + \tau^2)] d\tau \\
    
    &= y_0 + 2y_0 \int_{0}^t (\tau + \tau^3) d\tau \\
    
    &= y_0 + 2y_0 \left[ \frac{\tau^2}{2} + \frac{\tau^4}{4} \right]_0^t \\
    
    &= y_0 + y_0 t^2 + y_0 \frac{t^4}{2} \\
    
    &= y_0 \left( 1 + t^2 + \frac{t^4}{2} \right) = y_0 \left( 1 + \frac{(t^2)^1}{1!} + \frac{(t^2)^2}{2!} \right)
    
    \end{aligned}
    
    $$

4. 推广到 k (General term):
    
    通过数学归纳法，我们可以得到 ϕk​(t) 的一般形式：
    
    $$
    
    \phi_k(t) = y_0 \sum_{i=0}^k \frac{(t^2)^i}{i!} = y_0 \left( 1 + \frac{t^2}{1!} + \frac{t^4}{2!} + \dots + \frac{t^{2k}}{k!} \right)
    
    $$

5. 取极限 (Taking the limit):
    
    当 k→∞ 时，我们得到：
    
    $$
    
    \phi(t) = \lim_{k \to \infty} \phi_k(t) = y_0 \sum_{i=0}^\infty \frac{(t^2)^i}{i!}
    
    $$
    

    所以，极限函数是：
    
    $$
    
    \phi(t) = y_0 e^{t^2}
    
    $$

## Corollaries
### Maximal Solutions

**核心概念:**
一个初值问题 (IVP) 的解可能只在某个有限的区间上定义。最大解指的是这个解在其“自然”的最大可能定义区间上的延伸。

**1. 定义**
一个 ODE $y' = f(t, y)$ 的解 $\phi: I \to \mathbb{R}^n$ (其中 $I$ 是一个区间) 被称为**最大解 (maximal / non-extendable solution)**，如果不存在另一个解 $\psi: J \to \mathbb{R}^n$，使得 $J$ 是一个严格包含 $I$ ($J \supsetneq I$) 的区间，并且在 $I$ 上 $\psi(t) = \phi(t)$。
换句话说，最大解是不能再被延伸到更大定义域上的解。

**2. 推论**
在存在唯一性定理的假设下 (即 $f: D \to \mathbb{R}^n$ 在开集 $D \subseteq \mathbb{R} \times \mathbb{R}^n$ 上连续，且关于 $y$ 局部 Lipschitz)，对于任意初始条件 $(t_0, y_0) \in D$：

1.  **存在唯一最大解 (Existence and Uniqueness of Maximal Solution):** 存在一个*唯一*的最大解 $\phi_0: I_0 \to \mathbb{R}^n$，满足 IVP $y' = f(t, y)$ 且 $y(t_0) = y_0$。
    *   这里的 $I_0$ 就是这个最大解的定义区间，称为**最大存在区间 (maximal interval of existence)**。

2.  **最大存在区间的性质 (Properties of the Maximal Interval):**
    *   $I_0$ 是一个**开区间 (open interval)**。
    *   对于 $I_0$ 的任何一个端点 $e$ (如果存在，即 $I_0$ 不是整个 $\mathbb{R}$)，当 $t \to e$ 时，解曲线 $\{(t, \phi_0(t)); t \in I_0\}$ 必然会任意接近区域 $D$ 的边界 $\partial D$。

**3. 解释**

*   **唯一性保证了“最大”:** 正是因为在满足条件的区域内，通过每一点的解都是唯一的，我们才能将所有包含 $(t_0, y_0)$ 的局部解“无缝拼接”起来，形成一个唯一的、不能再延长的最大解。
*   **开区间 $I_0$**: 如果 $I_0$ 包含某个端点 $a$，比如 $I_0 = [a, b)$，那么 $(a, \phi_0(a))$ 就在 $D$ 内部。根据存在性定理，我们可以在 $a$ 点附近找到一个解，这个解可以向 $a$ 的左侧延伸一点点，这就与 $I_0$ 是最大区间矛盾了。所以 $I_0$ 必须是开区间。
*   **趋近边界 (Approaching the Boundary)** 这点非常关键。它说明了解不能在区域 $D$ 的“内部”突然停止。如果解 $\phi_0(t)$ 的定义区间 $I_0 = (a, b)$ 是有限的，那么当 $t$ 趋近于 $a$ 或 $b$ 时，必然发生以下至少一种情况：
    *   解的值趋于无穷大，即 $|\phi_0(t)| \to \infty$。
    *   点 $(t, \phi_0(t))$ 趋近于 $D$ 的边界上的某个点 $(e, y^*)$，其中 $(e, y^*) \notin D$ (这里 $e=a$ 或 $e=b$)。
    *   **技术比喻:** 想象你在一个地图 $D$ 上沿着一条由 $f(t,y)$ 决定的路径行走。只要你还在地图内部，并且你的速度 ($y'$) 是有界的（这通常由 $f$ 的连续性保证），你就总能再往前走一步。你被迫停下来只有两种可能：要么你走到了地图的边界 ($\partial D$)，要么你走向了无限远 ($|y| \to \infty$)。你的行走时间区间 $I_0$ 必然是开放的，因为你永远不会“恰好停在”地图内部的某一点。

**4. 证明思路**
1.  **构造 $I_0$ 与 $\phi_0$:** 将所有包含 $t_0$ 的、满足 IVP 的解的定义区间的并集定义为 $I_0$。利用唯一性定理证明在 $I_0$ 的重叠部分，不同的解取值相同，因此可以定义一个统一的函数 $\phi_0$ 在 $I_0$ 上。 $\phi_0$ 显然是最大解。
2.  **证明 $I_0$ 是开区间:** 使用反证法。假设 $I_0$ 包含某个端点 $a$，则 $(a, \phi_0(a)) \in D$。根据存在性定理，存在一个以 $a$ 为中心的区间上的解，这与 $I_0$ 的最大性矛盾。
3.  **证明趋近边界:** 使用反证法。假设当 $t \to a$ (左端点) 时，解曲线 $\{(t, \phi_0(t)); a < t \le t_0\}$ 包含在一个 $D$ 的紧子集 (compact subset) $C$ 内。由于 $f$ 在紧集 $C$ 上连续有界，可以证明 $\lim_{t \to a^+} \phi_0(t)$ 存在（记为 $y_a$）。并且 $(a, y_a)$ 必须在 $D$ 内 (否则就趋近边界了)。我们可以将 $\phi_0$ 连续延拓到 $a$ 点，定义 $\phi_0(a) = y_a$。但这又回到了 $I_0$ 包含端点 $a$ 的情况，与 $I_0$ 是开区间矛盾。

#### 相关例题


1.  **最大存在区间的性质 (Properties of the Maximal Interval):**
    *   这是解决这类问题的关键！如果区间的端点 $a$ 或 $b$ 是**有限的** (即 $a > -\infty$ 或 $b < +\infty$)，那么当 $t$ 趋近于这个有限端点时，解曲线 $(t, \phi_0(t))$ 必须**趋近于区域 $D$ 的边界 $\partial D$ 或者趋向于无穷大 ($|\phi_0(t)| \to \infty$)**。
    *   **技术比喻 (Technical Analogy):** 想象你在地图 $D$ 上按照微分方程 $y'=f(t,y)$ 指示的路线行走。只要你还在地图内部，并且你的速度（由 $f$ 的连续性保证通常有界），你总能再往前走。你被迫停下来的唯一可能，要么是你走到了地图的**边界 (boundary)**，要么是你走向了**无限远 (infinity)**。你的行走时间区间 $(a, b)$ 不可能在你还在地图内部舒适区域的时候就突然结束。

2.  **特殊情况：自治系统 $y' = f(y)$ 且 $D = \mathbb{R} \times \mathbb{R}^n$ (或 $\mathbb{R} \times \mathbb{R}$):**
    *   对于 Self Review Note 中的例题，方程都是自治的 $y' = f(y)$，且 $f(y)$ 都是多项式或简单的函数，其定义域 $D$ 通常是整个 $\mathbb{R} \times \mathbb{R}$。
    *   在这种情况下，区域 $D$ **没有有限的边界**。因此，最大存在区间 $(a, b)$ 的端点 $a$ 或 $b$ 是**有限**的**唯一原因**是解 $y(t)$ 在有限时间内**趋于无穷大 (blows up to infinity)**，即 $|y(t)| \to \infty$。

**解题策略：判断最大存在区间的形式**

对于自治方程 $y' = f(y)$，其中 $f(y)$ 在整个 $\mathbb{R}$ 上都满足 EUT 条件（例如 $f(y)$ 是多项式），我们需要判断最大存在区间 $I_0 = (a, b)$ 的形式，即判断 $a$ 和 $b$ 是否为有限值。

1.  **检查 EUT 条件:**
    *   确认 $f(y)$ 是连续的且关于 $y$ 局部 Lipschitz。对于多项式 $f(y)$，这是自动满足的。因此，存在唯一的最大解，其存在区间为开区间 $(a, b)$。

2.  **分析解的走向:**
    *   计算初始点的导数值 $y'(t_0) = f(y(t_0)) = f(y_0)$。
    *   如果 $f(y_0) > 0$，解 $y(t)$ 在 $t>t_0$ 时会增加。
    *   如果 $f(y_0) < 0$，解 $y(t)$ 在 $t>t_0$ 时会减少。
    *   如果 $f(y_0) = 0$，则 $y_0$ 是平衡点，解是 $y(t) \equiv y_0$，最大存在区间是 $(-\infty, +\infty)$。

3.  **判断有限时间爆破 (Finite Time Blow-up):**
    *   **核心思想:** 解是否能在有限时间内趋于 $+\infty$ 或 $-\infty$？这取决于 $f(y)$ 在 $y \to \pm \infty$ 时的增长速度。
    *   **启发式积分检验 (Heuristic Integral Test):**
        *   **考察右端点 $b$ (对应 $t \to b^-$):** 如果解 $y(t)$ 趋向 $+\infty$，我们需要看积分 $\int_{y_0}^{\infty} \frac{dy}{f(y)}$ (或对于某个大数 $C$，考察 $\int_{C}^{\infty} \frac{dy}{f(y)}$) 是否**收敛 (converges)**。
            *   如果积分**收敛**，意味着 $y$ 只需要“有限的时间”就能达到无穷大，因此右端点 $b$ 是**有限的** ($b < +\infty$)。
            *   如果积分**发散 (diverges)**，意味着 $y$ 需要“无限的时间”才能达到无穷大，因此右端点 $b$ 是**无限的** ($b = +\infty$)。
        *   **考察左端点 $a$ (对应 $t \to a^+$):** 如果解 $y(t)$ 趋向 $-\infty$，我们需要看积分 $\int_{-\infty}^{y_0} \frac{dy}{-f(y)}$ (或对于某个大负数 $-C$，考察 $\int_{-\infty}^{-C} \frac{dy}{-f(y)}$) 是否**收敛**。
            *   如果积分**收敛**，意味着 $y$ 只需要“有限的时间”就能达到负无穷大，因此左端点 $a$ 是**有限的** ($a > -\infty$)。
            *   如果积分**发散**，意味着 $y$ 需要“无限的时间”才能达到负无穷大，因此左端点 $a$ 是**无限的** ($a = -\infty$)。
    *   **积分收敛/发散的判断:**
        *   比较 $f(y)$ 与 $y^p$ 的增长阶数。积分 $\int^{\infty} \frac{dy}{y^p}$ 在 $p>1$ 时收敛，在 $p \le 1$ 时发散。
        *   如果当 $y \to \infty$ 时，$f(y)$ 的增长速度**快于** $y$ (例如 $y^2, y^5, e^y$)，则 $\int^{\infty} \frac{dy}{f(y)}$ 倾向于**收敛** $\implies b$ 有限。
        *   如果当 $y \to \infty$ 时，$f(y)$ 的增长速度**等于或慢于** $y$ (例如 $y, \sqrt{y}, \ln y$)，则 $\int^{\infty} \frac{dy}{f(y)}$ 倾向于**发散** $\implies b = +\infty$。
        *   对 $y \to -\infty$ 的情况作类似分析 (注意分母是 $-f(y)$)。

4.  **结合初始条件和平衡点:**
    *   解曲线不能穿过平衡点。如果解趋向于某个平衡点 $y_{eq}$，则需要看积分 $\int^{y_{eq}} \frac{dy}{f(y)}$ 是否收敛。如果发散（通常是这样，例如 $f(y)$ 在 $y_{eq}$ 附近表现像 $c(y-y_{eq})$），则需要无限时间到达平衡点。

5.  **确定区间形式:** 根据对 $a$ 和 $b$ 有限性的判断，选择对应的区间形式：$(a, b)$, $(a, +\infty)$, $(-\infty, b)$, 或 $(-\infty, +\infty)$。

**例题分析**

**Question 12 (第一题): $y' = y^5 + y$, $y(0)=1$. Interval form?**

1.  **EUT 条件:** $f(y) = y^5 + y$ 是多项式，连续且 $\partial f / \partial y = 5y^4 + 1$ 连续。EUT 满足。最大解区间 $I_0 = (a, b)$ 是开区间。
2.  **解的走向:** $y'(0) = f(1) = 1^5 + 1 = 2 > 0$。解 $y(t)$ 从 $y=1$ 开始随 $t$ 增加而增加。
3.  **判断右端点 $b$:** 当 $y \to +\infty$ 时，$f(y) \approx y^5$。增长速度快于 $y$ ($p=5 > 1$)。
    *   检验积分 $\int^{\infty} \frac{dy}{y^5 + y}$。因为被积函数在 $y \to \infty$ 时行为像 $1/y^5$，根据 p-积分判别法，此积分**收敛**。
    *   结论：解将在有限时间内爆破到 $+\infty$。因此 $b$ 是**有限的** ($b < +\infty$)。
4.  **判断左端点 $a$:** 当 $t$ 减小时 ($t<0$)，解 $y(t)$ 从 $y=1$ 开始减少。它会趋向何处？ $f(y) = y(y^4+1)$，唯一的平衡点是 $y=0$。由于解不能穿过平衡点，且 $y(0)=1 > 0$，解 $y(t)$ 在 $t \to -\infty$ 时必然趋向于 $y=0$。
    *   检验到达 $y=0$ 是否需要无限时间。考察积分 $\int_{1}^{\epsilon} \frac{dy}{y^5 + y}$ (其中 $\epsilon \to 0^+$)。当 $y \to 0^+$ 时，$f(y) \approx y$。积分 $\int^{\epsilon} \frac{dy}{y}$ 发散 (像 $\ln y$)。
    *   结论：解需要无限时间才能到达 $y=0$。因此 $a = -\infty$。
5.  **区间形式:** 结合 $a=-\infty$ 和 $b$ 有限，最大存在区间形式为 $(-\infty, b)$。


**Question 13 (第二题): $y' = y^2 + y$, $y(0) = y_0 > 0$. Interval form?**

1.  **EUT 条件:** $f(y) = y^2 + y$ 是多项式，EUT 满足。$I_0 = (a, b)$ 是开区间。
2.  **解的走向:** $y'(0) = f(y_0) = y_0(y_0+1)$。因为 $y_0 > 0$，所以 $y'(0) > 0$。解 $y(t)$ 从 $y=y_0$ 开始随 $t$ 增加而增加。
3.  **判断右端点 $b$:** 当 $y \to +\infty$ 时，$f(y) \approx y^2$。增长速度快于 $y$ ($p=2 > 1$)。
    *   检验积分 $\int^{\infty} \frac{dy}{y^2 + y}$。行为像 $\int^{\infty} \frac{dy}{y^2}$，**收敛**。
    *   结论：解将在有限时间内爆破到 $+\infty$。$b$ 是**有限的** ($b < +\infty$)。
4.  **判断左端点 $a$:** 当 $t$ 减小时，解 $y(t)$ 从 $y=y_0 > 0$ 开始减少。平衡点是 $y=0$ 和 $y=-1$。解不能穿过 $y=0$。因此，当 $t \to -\infty$ 时，解 $y(t)$ 趋向于 $y=0$。
    *   检验到达 $y=0$ 是否需要无限时间。考察积分 $\int_{y_0}^{\epsilon} \frac{dy}{y^2 + y}$ ($\epsilon \to 0^+$)。当 $y \to 0^+$ 时，$f(y) \approx y$。积分 $\int^{\epsilon} \frac{dy}{y}$ **发散**。
    *   结论：需要无限时间才能到达 $y=0$。$a = -\infty$。
5.  **区间形式:** 结合 $a=-\infty$ 和 $b$ 有限，最大存在区间形式为 $(-\infty, b)$。


**Question 12 (第三题): $y' = y^3 + 1$, $y(0)=0$. Interval form?**

1.  **EUT 条件:** $f(y) = y^3 + 1$ 是多项式，EUT 满足。$I_0 = (a, b)$ 是开区间。
2.  **解的走向:** $y'(0) = f(0) = 0^3 + 1 = 1 > 0$。解 $y(t)$ 从 $y=0$ 开始随 $t$ 增加而增加。
3.  **判断右端点 $b$:** 当 $y \to +\infty$ 时，$f(y) \approx y^3$。增长速度快于 $y$ ($p=3 > 1$)。
    *   检验积分 $\int^{\infty} \frac{dy}{y^3 + 1}$。行为像 $\int^{\infty} \frac{dy}{y^3}$，**收敛**。
    *   结论：解将在有限时间内爆破到 $+\infty$。$b$ 是**有限的** ($b < +\infty$)。
4.  **判断左端点 $a$:** 
    让我们考虑 $t<0$ 的情况。 $y'(0)=1>0$。这意味着在 $t=0$ 的一个小邻域内， $y(t)$ 是关于 $t$ 递增的。因此对于 $t$ 略小于 0， $y(t)$ 应该略小于 0。
    当 $y \in (-1, 0)$ 时，$y^3$ 在 $(-1, 0)$ 之间，$y^3+1 > 0$。所以 $y'(t)>0$。这意味着如果解进入了 $(-1, 0)$ 区间，它会倾向于增加（朝 $y=0$ 移动）。
    当 $y < -1$ 时，$y^3 < -1$，$y^3+1 < 0$。所以 $y'(t)<0$。
    平衡点是 $y=-1$ (因为 $y^3+1=0$)。
    解从 $y(0)=0$ 出发。当 $t$ 减小时，它会趋向平衡点 $y=-1$ 吗？是的，因为在 $(-1, 0)$ 区间 $y'>0$，在 $(-\infty, -1)$ 区间 $y'<0$，所以 $y=-1$ 是一个**稳定平衡点 (stable equilibrium)**。解 $y(t)$ 在 $t \to -\infty$ 时会趋向 $y=-1$。
    *   检验到达 $y=-1$ 是否需要无限时间。考察积分 $\int_{0}^{-\epsilon} \frac{dy}{y^3 + 1}$ (其中 $\epsilon \to -1^+$)。当 $y \to -1^+$ 时，$y^3+1 = (y+1)(y^2-y+1) \approx 3(y+1)$。积分 $\int^{-1} \frac{dy}{3(y+1)}$ **发散** (像 $\ln|y+1|$)。
    *   结论：需要无限时间才能到达 $y=-1$。$a = -\infty$。
5.  **区间形式:** 结合 $a=-\infty$ 和 $b$ 有限，最大存在区间形式为 $(-\infty, b)$。



### 高阶常微分方程 (Higher-Order ODEs)

高阶微分方程是指导数阶数大于等于 2 的微分方程，一般表示为：

$$y^{(n)} = f(t, y, y', ..., y^{(n-1)})$$

其中 $f: D \to \mathbb{R}$，$D \subseteq \mathbb{R} \times \mathbb{R}^n$ 是开集。

#### 高阶 ODE 与一阶系统的关系

为了将存在唯一性定理应用于高阶 ODE，我们需要将其转化为一阶 ODE 系统：

1. 首先进行阶降，设置 $y_0 = y$, $y_1 = y'$, ..., $y_{n-1} = y^{(n-1)}$
2. 将原方程转化为向量形式 $\mathbf{y'} = \mathbf{f}(t, \mathbf{y})$

对于向量函数 $\mathbf{f}$，如果原函数 $f$ 满足关于 $y$ 的局部利普希茨条件 (Lipschitz condition)，那么向量函数 $\mathbf{f}$ 也满足关于 $\mathbf{y}$ 的局部利普希茨条件。

#### 高阶微分方程的存在唯一性定理

**定理**（高阶微分方程的存在唯一性）：
假设 $f: D \to \mathbb{R}$，$D \subseteq \mathbb{R} \times \mathbb{R}^n$ 是**连续**函数，并且在 $D$ 上关于 $\mathbf{y}$ 满足**局部利普希茨条件**。令 $(a, b) = (a, b_0, ..., b_{n-1}) \in D$。

**唯一性**
1. 如果 $\phi, \psi: I \to \mathbb{R}$ 是以下初值问题的解：
   $$y^{(n)} = f(t, y, y', ..., y^{(n-1)}) \wedge y^{(i)}(a) = b_i \text{ for } 0 \leq i \leq n-1$$
   则 $\phi(t) = \psi(t)$ 对所有 $t \in I$ 成立。

**存在性**
2. 存在 $\epsilon > 0$ 和函数 $\phi: [a-\epsilon, a+\epsilon] \to \mathbb{R}$ 是上述初值问题的解。

需要注意的是，**如果 $f$ 的偏导数 $\frac{\partial f}{\partial y_0}, \ldots, \frac{\partial f}{\partial y_{n-1}}$ 是连续的，那么上述定理的条件就满足了**。

#### 示例

Airy 方程是二阶 ODE：$y'' = ty$, $(t, y) \in \mathbb{R}^2$

通过阶降：$y_0 = y$, $y_1 = y'$, $\mathbf{y} = (y_0, y_1) = (y, y')$，得到等价的二维系统：

$$\mathbf{y}' = \begin{pmatrix} y_0' \\ y_1' \end{pmatrix} = \begin{pmatrix} y' \\ y'' \end{pmatrix} = \begin{pmatrix} y_1 \\ t y_0 \end{pmatrix} = \mathbf{f}(t, \mathbf{y})$$

其中 $\mathbf{f}(t, \mathbf{y}) = \mathbf{f}(t, y_0, y_1) = (y_1, ty_0)$，$(t, y_0, y_1) \in \mathbb{R}^3$。

由于 $\mathbf{f}$ 是连续可微的（甚至是 $C^\infty$ 类的），根据性质，$\mathbf{f}$ 满足关于 $\mathbf{y}$ 的局部利普希茨条件。

### 积分曲线 (Integral Curves)

#### 分类定义
1.  **对于显式或隐式定义的 ODE (Explicit or Implicit ODEs):**
    *   考虑形如 $y' = f(t, y)$ 或更一般的隐式形式 $f(t, y, y') = 0$ 的一阶标量 ODE。
    *   其**积分曲线 (Integral Curve)** 被定义为一个**极大解 (Maximal Solution)** $\phi: I \to \mathbb{R}$ 的**图像 (graph)**。
    *   这个图像是在 $t$-$y$ 平面上的点集：
        $$
        \{(t, \phi(t)); t \in I\}
        $$
    *   这里的“极大解”意味着这个解 $\phi$ 定义在尽可能大的区间 $I$ 上，不能再被拓展到包含 $I$ 的更大区间上。
    *   **技术比喻:** 想象一下方程 $y' = f(t, y)$ 描述了一个在平面上运动的点的速度 $(1, y')$ 如何依赖于当前位置 $(t, y)$。一个极大解 $\phi(t)$ 就描述了这个点的一条具体运动轨迹。这条轨迹画出来的**完整路径**，就是积分曲线。

2.  **对于 "微分形式" 的 ODE (Differential Form ODEs):**
    *   考虑形如 $M(x, y) dx + N(x, y) dy = 0$ 的方程。这种形式在物理和工程中也很常见。
    *   其**积分曲线 (Integral Curve)** 被定义为一个**极大解 (Maximal Solution)** $\gamma: I \to \mathbb{R}^2$ 的**值域 (range)** $\gamma(I)$。
    *   这里，$\gamma(t) = (x(t), y(t))$ 是一个**光滑的 (smooth)** 参数曲线，并且对于所有 $t \in I$ 满足:
        $$
        M(x(t), y(t))x'(t) + N(x(t), y(t))y'(t) = 0
        $$
    *   这里的“极大性”是指，不存在另一个解，其值域严格包含 $\gamma(I)$。也就是说，这条曲线本身是“最长的”满足条件的路径。
    *   **技术比喻:** 这种形式不再直接要求 $y$ 是 $x$ 的函数 (或者 $t$ 的函数)。它更像是在描述平面上每一点 $(x, y)$ 的一个允许的运动方向 (垂直于向量 $(M, N)$ 的方向)。积分曲线就是沿着这些允许方向光滑地移动所形成的**完整路径**，比如一个圆圈。

**两种定义的联系与区别**

Slide 40 给出了一个很好的例子来说明这两者之间的关系：$x dx + y dy = 0$。

*   按照 **定义 2**，我们寻找参数曲线 $(x(t), y(t))$ 使得 $x(t)x'(t) + y(t)y'(t) = 0$。这等价于 $\frac{d}{dt} (x(t)^2 + y(t)^2) = 0$。
*   这意味着 $x(t)^2 + y(t)^2 = C$ (常数)。所以，这个微分形式方程的积分曲线是**圆心在原点的圆 (circles)** $x^2 + y^2 = R^2$ (其中 $R = \sqrt{C} > 0$，排除了 $R=0$ 的情况因为要求解是光滑曲线，并且极大性排除了圆弧段)。

*   现在，我们将它改写成 **定义 1** 中的显式形式 $y' = dy/dx = -x/y$。
*   这个显式 ODE 在 $y=0$ (即 x-轴) 上是**未定义的**。
*   它的解是 $y(x) = \pm \sqrt{R^2 - x^2}$，定义域为 $x \in (-R, R)$。
*   这些解的图像 (按照 **定义 1** 的积分曲线) 是**上半圆 (upper semi-circles)** 和**下半圆 (lower semi-circles)**。

*   **关键点:** 一个由 $M dx + N dy = 0$ 定义的积分曲线 (例如一个完整的圆) 可能对应于其显式形式 $y' = -M/N$ 的**多个**积分曲线 (例如上半圆和下半圆)。这种“分裂”通常发生在 $N(x, y) = 0$ 的点上，这些点对应于显式 ODE $y' = -M/N$ 的垂直切线或奇点。

#### 积分曲线的唯一性

这个推论给出了积分曲线唯一性的条件：

*   **条件:**
    1.  $M(x, y)$ 和 $N(x, y)$ 在**开集** $D \subseteq \mathbb{R}^2$ 上是 $C^1$ 函数 (即具有**连续的一阶偏导数**)。
    2.  方程 $M(x, y) dx + N(x, y) dy = 0$ 在 $D$ 中**没有奇点 (singular points)**。**奇点是指同时满足 $M(x, y) = 0$ 和 $N(x, y) = 0$ 的点**。
*   **结论:** 如果满足这些条件，那么对于 $D$ 中的**每一个点**，**恰好**有一条积分曲线穿过该点。

*   **理解:**
    *   非奇点 $(x_0, y_0)$ 意味着向量 $(M(x_0, y_0), N(x_0, y_0))$ 非零。
    *   积分曲线在该点的切线方向必须与 $(M, N)$ 垂直，因此切线方向是唯一确定的。
    *   由于切线不能同时水平 ($N \neq 0$) 和垂直 ($M \neq 0$)，我们总可以在该点附近将曲线表示为 $y=y(x)$ (如果 $N \neq 0$) 或 $x=x(y)$ (如果 $M \neq 0$)。
    *   对应的显式 ODE $dy/dx = -M/N$ 或 $dx/dy = -N/M$ 在局部满足我们之前学过的**存在唯一性定理**的条件 (因为 $M, N$ 是 $C^1$ 保证了局部 Lipschitz 条件)，从而保证了局部解的存在唯一性。
    *   结合解的极大性，可以证明全局唯一性。

**重要备注和反例**

*   **Remark:** 如果两条积分曲线相交，那么交点**必定是**奇点。因为在非奇点处，根据推论，只有一条积分曲线通过。
*   **Afternote (Counterexample):** 考虑 $2y dx - x dy = 0$。
    *   这里 $M(x, y) = 2y$, $N(x, y) = -x$ 都是 $C^1$ (实际上是 $C^\infty$)。
    *   唯一的奇点是 $(0, 0)$，因为 $M=0 \implies y=0$, $N=0 \implies x=0$。
    *   在**非奇点区域** $\mathbb{R}^2 \setminus \{(0,0)\}$ 中，推论的条件满足。但是，通过 $(0, y_0)$ (其中 $y_0 \neq 0$) 的解只有 y-轴 ($x=0$) 本身。而通过 $(x_0, y_0)$ (其中 $x_0 \neq 0$) 的解却有**无穷多条**! 例如，我们可以沿着抛物线 $y = (y_0/x_0^2) x^2$ 到达原点，然后从原点沿着任意一条抛物线 $y=Cx^2$ (或者 $x=0$ 的另一半) 离开。
    *   **为什么推论在这里似乎失效了？** 推论保证在**非奇点区域 D'** 内，过每一点的积分曲线是唯一的。但是这个例子表明，不同的积分曲线可以**在奇点 (0,0) 处汇合或分叉**，导致即使在非奇点区域，从全局来看唯一性也可能被破坏。Slide 44 的图形象地展示了这一点，所有 $y = C x^2$ 的曲线都在原点相交。
    *   这与我们之前看到的 $y' = \sqrt{|y|}$ (Slide 18) 不同，那个例子是 $f(t, y) = \sqrt{|y|}$ 在 $y=0$ 处不满足 Lipschitz 条件导致非唯一性。而 $2y dx - x dy = 0$ 的例子中 $M, N$ 都是 $C^1$，问题出在奇点的行为。

总结来说，积分曲线为我们提供了一种几何上理解微分方程解的方式。对于 $y'=f(t,y)$，它是解的图像。对于 $Mdx+Ndy=0$，它是满足约束的光滑参数曲线的值域。在没有奇点的良好条件下 ($M, N$ 是 $C^1$)，通过每一点的积分曲线是唯一的。但在奇点处或附近，行为可能变得复杂，唯一性可能丧失。

## Example 判断解的存在唯一


要判断解的唯一性，我们主要依赖**皮卡-林德洛夫定理 (Picard-Lindelöf Theorem)**，它同时保证了解的存在性和唯一性。

定理内容 (简化版，针对一阶方程 $y' = f(t, y)$)：
假设函数 $f(t, y)$ 在包含点 $(t_0, y_0)$ 的某个**开区域 (open region)** $D \subseteq \mathbb{R}^2$ 内满足以下两个条件：
1.  $f(t, y)$ 在 $D$ 内是**连续的 (continuous)**。
2.  $f(t, y)$ 在 $D$ 内关于变量 $y$ 满足**局部利普希茨条件 (locally Lipschitz condition)**。

那么，对于初始值问题 (Initial Value Problem, IVP):
$$
y' = f(t, y), \quad y(t_0) = y_0
$$
在包含 $t_0$ 的某个区间 $I$ 上，**存在 (exists)** 且**唯一 (unique)** 一个解 $\phi(t)$。

**关键点：利普希茨条件 (Lipschitz Condition)**

*   **定义:** 函数 $f(t, y)$ 在区域 $D$ 内关于 $y$ 满足 Lipschitz 条件，是指存在一个常数 $L > 0$ (利普希茨常数)，使得对于区域 $D$ 内任意两个点 $(t, y_1)$ 和 $(t, y_2)$ (注意 $t$ 值相同)，都有：
    $$
    |f(t, y_1) - f(t, y_2)| \le L |y_1 - y_2|
    $$

*   **实用判据:** 检验 Lipschitz 条件的一个非常实用的方法是检查**偏导数 $\frac{\partial f}{\partial y}$ 的连续性**。
    > **命题 (Proposition):** 如果偏导数 $\frac{\partial f}{\partial y}$ 在包含 $(t_0, y_0)$ 的开区域 $D$ 内**存在且连续 (exists and is continuous)**，那么 $f(t, y)$ 在该区域内关于 $y$ 满足局部 Lipschitz 条件。

*   **不唯一性的根源:** 当 $f(t, y)$ 在初始点 $(t_0, y_0)$ 附近**不满足** Lipschitz 条件时，唯一性就可能被破坏。这通常发生在 $\frac{\partial f}{\partial y}$ 在 $(t_0, y_0)$ 附近**无界 (unbounded)** 的情况。

### 解题策略



1.  **快速排除线性选项 (Eliminate Linear Options):**
    *   首先扫描所有选项，找出**线性 ODE (Linear ODE)**。线性 ODE 通常形如 $y' + p(t)y = q(t)$ 或 $y' = a(t)y + b(t)$。
    *   线性 ODE 在其系数 $p(t), q(t)$ (或 $a(t), b(t)$) 连续的区间内，其解对于给定的初始条件通常是**唯一**的 (除非系数在 $t_0$ 处有奇点)。因此，如果题目要求找出解**不唯一**或**可能不唯一**的选项，线性 ODE 通常可以**优先排除**。
    *   笔记中的例子 (Page 25): $y'' = \sqrt{t}y$, $y' = ty$, $t^2y'' = y$ 都被视为 (关于 $y$ 及其导数) 线性的，倾向于有唯一解。

2.  **重点关注非线性选项中的“危险信号” (Focus on "Danger Signals" in Non-linear Options):**
    *   在剩下的非线性选项中，寻找那些已知**容易破坏 Lipschitz 条件**的函数形式，尤其是在初始值 $y_0$ 附近。这些是导致解不唯一的“高危”特征：
        *   **绝对值函数 (Absolute Value):** 涉及 $|y|$ 或 $|y'|$。例如 $y' = |y|$ 或 $y' = t|y|$。函数在 $y=0$ 点不可微，不满足 Lipschitz 条件。
        *   **分数次幂或根式 (Fractional Powers/Roots):** 涉及 $\sqrt{y}$, $y^{1/3}$, $y^{2/3}$ 等。例如 $y' = y^{2/3}$ 或 $y'' = t\sqrt{y}$。这类函数在 $y=0$ 处的导数 ($\frac{\partial f}{\partial y}$) 会趋于无穷，不满足 Lipschitz 条件。
        *   **导数的非线性函数 (Non-linear Function of Derivative):** 涉及 $(y')^k$ (k>1) 或其他关于 $y'$ 的复杂函数。例如 $(y')^3 = y$ (等价于 $y' = y^{1/3}$)。
        *   **分母含 $y$ (Variable y in Denominator):** 涉及 $1/y$, $1/\sqrt{y}$ 等。例如 $y' = 1/y$。函数在 $y=0$ 处未定义或导数无界。
        *   **对数函数 (Logarithm):** 涉及 $y \ln|y|$。函数在 $y=0$ 处导数无界。

3.  **对比与选择 (Compare and Select):**
    *   如果存在多个包含“危险信号”的非线性选项，优先选择那些**最符合**你在课堂或笔记中遇到的**经典非唯一性例子**的选项。例如 $y' = \sqrt{|y|}$, $y' = y^{2/3}$, $y' = y^{1/3}$ 是非常典型的例子。
    *   比较“危险”的程度。通常，分数次幂/根式和绝对值是考试中最常见的陷阱。

4.  **回顾教案例题 (Recall Lecture Examples):**
    *   回忆老师在课上或者笔记中强调过的导致非唯一性的典型方程，看哪个选项与其最相似。




### 总结

求解关于 ODE 解唯一性的问题，关键在于理解**利普希茨条件 (Lipschitz condition)** 及其与**偏导数 $\partial f / \partial y$ 连续性**的关系。

*   **主要流程：**
    1.  识别 ODE 是线性的还是非线性的。线性 ODE 通常解唯一 (需注意系数奇点)。
    2.  对于非线性 ODE $y' = f(t, y)$，检查函数 $f(t, y)$ 关于 $y$ 的偏导数 $\partial f / \partial y$。
    3.  判断 $\partial f / \partial y$ 是否在**初始点 $(t_0, y_0)$ 附近连续**。如果连续，则局部 Lipschitz 条件满足，解在该点附近是唯一的。
    4.  如果 $\partial f / \partial y$ 在 $(t_0, y_0)$ 附近**无界** (例如因为 $y=y_0$ 导致分母为零，或出现 $y^{-k}$ 形式且 $y_0=0$)，则 Lipschitz 条件不满足，**解可能不唯一**。
    5.  特别留意包含 $\sqrt{y}$, $|y|$, $y^{p/q}$ ($q>p\ge 1$) 等形式的项，它们在 $y=0$ 附近是典型的非 Lipschitz “危险信号”。

*   **选择题技巧：** 优先排除线性选项，然后在非线性选项中寻找上述“危险信号”。与课堂/笔记中的经典非唯一性例子进行比对。