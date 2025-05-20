---
title: Uniform Convergence
date: 2025-03-26
date modified: 2025-04-05
categories: Math285
tags:
  - Math285
---

#Math285 

## 概述与引言

一致收敛 (Uniform Convergence) 是研究微分方程解的存在性定理、傅里叶级数理论以及其他实分析重要主题的基础概念。  
一致收敛的概念源于这样一个问题：函数序列或级数的极限函数是否继承了序列或级数各项的性质，如连续性或可微性。对于普通的点态收敛 (pointwise convergence)，答案往往是否定的。

## Point-wise V.S. Uniform Convergence

### 点态收敛与一致收敛

设 $I \subseteq \mathbb{R}$ 是一个区间，$(f_n)_{n=0}^{\infty}$ 是定义在 $I$ 上的函数序列 $f_n: I \to \mathbb{R}$。

1. **点态收敛 (Pointwise Convergence)**：如果对于每一个 $x \in I$，数列 $(f_n(x))$ 收敛，则称序列 $(f_n)$ 在 $I$ 上点态收敛。此时，$f(x) = \lim_{n \to \infty} f_n(x)$ 定义了一个函数 $f: I \to \mathbb{R}$，称为 " 极限函数 " 或 " 点态极限 "。

2. **一致收敛 (Uniform Convergence)**：如果序列 $(f_n)$ 点态收敛且极限函数 $f: I \to \mathbb{R}$ 满足：对于每个 $\varepsilon > 0$，存在一个 " 一致的 " 响应 $N \in \mathbb{N}$ 使得对于所有 $n > N$ 和所有 $x \in I$ 都有 $|f(x) - f_n(x)| < \varepsilon$。

**关键区别**：
- 点态收敛允许响应 $N = N_{\varepsilon,x}$ 依赖于 $x$（和 $\varepsilon$）
- 一致收敛要求响应 $N = N_{\varepsilon}$ 仅依赖于 $\varepsilon$ 而与 $x$ 无关

几何上，序列 $(f_n)$ 一致收敛到 $f$ 当且仅当对于每个 $\varepsilon > 0$，除了有限多个 $f_n$ 的图像外，所有 $f_n$ 的图像都包含在 $f$ 图像的 $2\varepsilon$ 垂直宽度的带状区域内。

**一致收敛是比点态收敛更强的性质 ->我们能够控制极限函数与数列中任何一个函数在定义域上任意点的差值**

**对于一致连续的函数序列，其极限函数能够继承序列函数的性质 ->连续、微分、积分**

函数序列一致收敛等价于,在x的定义域内:
$$
\lim_{ n \to \infty }sup |f(x)-f_{n}(x)| = 0
$$

## 三个反例

以下是三个重要反例，它们说明点态收敛不足以保证极限函数继承序列函数的性质：

### 反例 1（连续性不保持）

考虑函数序列 $f_n(x) = x^n$, $x \in [0,1]$。这些函数都是连续的，且点态收敛到：

$$
f(x) = \lim_{n \to \infty} f_n(x) = \lim_{n \to \infty} x^n = \begin{cases}
0 & \text{如果} 0 \leq x < 1, \\
1 & \text{如果} x = 1,
\end{cases}
$$

但极限函数 $f$ 在 $x = 1$ 处有不连续性。

### 反例 2（微分不可交换）

考虑函数序列 $g_n(x) = \frac{\sin(nx)}{\sqrt{n}}$, $x \in [0,2\pi]$。  
我们有 $g_n(x) \to g(x) \equiv 0$ 点态（甚至一致！），$g$ 可微，且 $g'(x) \equiv 0$。

但导数序列为：

$$
g'_n(x) = \sqrt{n}\cos(nx), x \in [0,2\pi]
$$

$\lim_{n \to \infty} g'_n(x)$ 对任意 $x$ 都不存在。

### 反例 3（积分不可交换）

考虑函数序列 $h_n: [0,1] \to \mathbb{R}$ 定义为：

$$
h_n(x) = \begin{cases}
2n^2x & \text{如果} 0 \leq x \leq 1/2n, \\
2n - 2n^2x & \text{如果} 1/2n \leq x \leq 1/n, \\
0 & \text{如果} 1/n \leq x \leq 1.
\end{cases}
$$

$h_n$ 图像和 $x$ 轴确定了顶点在 $(0,0)$, $(1/2n, n)$, $(1/n, 0)$ 的三角形，在 $[1/n, 1]$ 上 $h_n$ 为零。

$h_n(x) \to h(x) \equiv 0$ 点态收敛，但 $h_n$ 下的面积为 $1/2$，所以：

$$
\lim_{n \to \infty} \int_0^1 h_n(x) dx = \frac{1}{2} \neq 0 = \int_0^1 \lim_{n \to \infty} h_n(x) dx
$$

## 三个重要定理（连续、微分、积分）

一致收敛的引入正是为了避免上述反例。以下三个定理回答了前面提出的问题，前提是要求函数序列或其导数序列一致收敛。

### 定理 1（连续性定理）

如果所有函数 $f_n$ 在 $x_0 \in I$ 处连续且序列 $(f_n)$ 在 $I$ 上一致收敛，则 $f(x) = \lim_{n \to \infty} f_n(x)$, $x \in I$, 在 $x_0$ 也连续。特别地，**连续函数的一致收敛序列的极限函数也是连续函数**。

### 定理 2（微分定理）

如果所有函数 $f_n$ 都是 $C^1$ 函数，$(f_n)$ 在 $I$ 上点态收敛，且**导数序列 $(f'_n)$ 在 $I$ 上一致收敛**，则 $f(x) = \lim_{n \to \infty} f_n(x)$, $x \in I$, 也是 $C^1$ 函数且满足 $f'(x) = \lim_{n \to \infty} f'_n(x)$。

### 定理 3（积分定理）

如果 $I$ 是**有界区间**，所有函数 $f_n$ 在 $I$ 上都是（勒贝格）可积的，且 $(f_n)$ 在 $I$ 上一致收敛，则极限函数 $f(x) = \lim_{n \to \infty} f_n(x)$ 也是可积的，且有：

$$
\int_I f(x) dx = \lim_{n \to \infty} \int_I f_n(x) dx
$$

**注意**：区间 $I$ 必须是有界的，否则结论可能不成立。

## Weierstrass 一致收敛判别法

### Weierstrass 判别法

假设 $f_n: D \to \mathbb{R}$ ($n = 0, 1, 2, \ldots$) 是定义在公共定义域 $D$ 上的函数，且存在 " 一致 " 界 $M_n \in \mathbb{R}$ 使得对所有 $n \in \mathbb{N}$ 和 $x \in D$ 有 $|f_n(x)| \leq M_n$。如果级数 $\sum_{n=0}^{\infty} M_n$ 在 $\mathbb{R}$ 中收敛（即 $\sum_{n=0}^{\infty} M_n < \infty$），则**函数级数** $\sum_{n=0}^{\infty} f_n$ 一致收敛。

**应用于三角级数**：  
函数级数 $\sum_{n=1}^{\infty} \frac{\cos(nx)}{n^2}$ 和 $\sum_{n=1}^{\infty} \frac{\sin(nx)}{n^2}$ 在 $\mathbb{R}$ 上一致收敛（因此表示 $\mathbb{R}$ 上的连续函数）。

## 复幂级数

### 复幂级数的基本概念

复幂级数是形如 $\sum_{n=0}^{\infty} a_n(z-a)^n$ 的级数，其中 $z$ 和 $a$ 是复数，$a_n$ 是复系数。这些级数是复变函数理论的核心，类似于实变函数中的幂级数，但在复分析中有更加丰富的性质。

#### 收敛区域与收敛半径

**核心概念：收敛半径 (Radius of Convergence)**

对于任意给定的复幂级数，存在一个唯一的非负实数 $R$ (可以为 $0$ 或 $\infty$)，称为收敛半径，使得：

1.  级数在 **开圆盘 (open disk)** $|z - z_0| < R$ 内 **绝对收敛 (absolutely convergent)** (因此也收敛)。这个区域被称为 **收敛圆盘 (Disk of Convergence)**。
2.  级数在区域 $|z - z_0| > R$ 内 **发散 (divergent)**。
3.  在边界圆周 $|z - z_0| = R$ 上的点的收敛性需要单独判断，级数可能收敛，也可能发散。

**如何计算收敛半径 R？**


**方法一：柯西-阿达玛公式 (Cauchy-Hadamard Theorem) / 根值判别法 (Root Test)**

这是最通用的公式。计算 $L$：
$$
L = \limsup_{n \to \infty} \sqrt[n]{|a_n|}
$$
这里的 $\limsup$ 是上极限 (limit superior)。如果 $\lim_{n \to \infty} \sqrt[n]{|a_n|}$ 存在，那么 $L$ 就等于这个极限。

然后，收敛半径 $R$ 由下式给出：
$$
R = \begin{cases}
\frac{1}{L} & \text{if } 0 < L < \infty \\
\infty & \text{if } L = 0 \\
0 & \text{if } L = \infty
\end{cases}
$$
(我们约定 $1/0 = \infty$ 和 $1/\infty = 0$)。



**方法二：达朗贝尔判别法 (d'Alembert's Test) / 比值判别法 (Ratio Test)**

如果下面的极限存在 (或为 $\infty$)：
$$
L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|
$$
那么收敛半径 $R$ 同样由下式给出：
$$
R = \begin{cases}
\frac{1}{L} & \text{if } 0 < L < \infty \\
\infty & \text{if } L = 0 \\
0 & \text{if } L = \infty
\end{cases}
$$

*   **重要提示:** 比值判别法 **并非总是适用**，因为极限 $\lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|$ 可能不存在。然而，在许多常见情况下 (例如 $a_n$ 包含阶乘或简单的幂次)，这个极限确实存在，并且比根值判别法更容易计算。
*   **适用场景:** 当 $a_n$ 包含阶乘 (factorials) 或 $n$ 的幂次时，这个方法通常计算更简便。

**总结步骤：**

1.  **写出级数的一般项 $a_n (z-z_0)^n$，识别出系数 $a_n$ 和中心 $z_0$。**
2.  **选择判别法：**
    *   如果 $a_n$ 涉及 $n$ 次方，优先考虑 **根值判别法 (Cauchy-Hadamard)**。计算 $L = \limsup_{n \to \infty} \sqrt[n]{|a_n|}$。
    *   如果 $a_n$ 涉及阶乘或 $n$ 的简单幂次，优先考虑 **比值判别法 (Ratio Test)**。计算 $L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right|$ (如果极限存在)。
3.  **根据 $L$ 的值确定收敛半径 $R$：**
    *   若 $L=0$，则 $R = \infty$。
    *   若 $L=\infty$，则 $R = 0$。
    *   若 $0 < L < \infty$，则 $R = 1/L$。
4.  **得出结论：** 级数在开圆盘 $|z - z_0| < R$ 内绝对收敛，在 $|z - z_0| > R$ 内发散。

**例子：**

*   **例 1:** $\sum_{n=0}^{\infty} \frac{z^n}{n!}$
    $a_n = 1/n!$, $z_0 = 0$。使用比值判别法：
    $$
    L = \lim_{n \to \infty} \left| \frac{a_{n+1}}{a_n} \right| = \lim_{n \to \infty} \left| \frac{1/(n+1)!}{1/n!} \right| = \lim_{n \to \infty} \frac{n!}{(n+1)!} = \lim_{n \to \infty} \frac{1}{n+1} = 0
    $$
    因为 $L=0$，所以 $R = \infty$。级数对所有复数 $z$ 都收敛。

*   **例 2:** $\sum_{n=1}^{\infty} n^n (z-i)^n$
    $a_n = n^n$, $z_0 = i$。使用根值判别法：
    $$
    L = \limsup_{n \to \infty} \sqrt[n]{|a_n|} = \lim_{n \to \infty} \sqrt[n]{n^n} = \lim_{n \to \infty} n = \infty
    $$
    因为 $L=\infty$，所以 $R = 0$。级数仅在 $z = z_0 = i$ 时收敛。

*   **例 3:** $\sum_{n=0}^{\infty} (\frac{1+i}{2})^n z^n$
    $a_n = (\frac{1+i}{2})^n$, $z_0 = 0$。使用根值判别法：
    $$
    |a_n| = \left| \left(\frac{1+i}{2}\right)^n \right| = \left| \frac{1+i}{2} \right|^n = \left( \frac{|1+i|}{2} \right)^n = \left( \frac{\sqrt{1^2+1^2}}{2} \right)^n = \left( \frac{\sqrt{2}}{2} \right)^n
    $$
    $$
    L = \lim_{n \to \infty} \sqrt[n]{|a_n|} = \lim_{n \to \infty} \sqrt[n]{\left( \frac{\sqrt{2}}{2} \right)^n} = \frac{\sqrt{2}}{2}
    $$
    因为 $L = \frac{\sqrt{2}}{2}$，所以 $R = \frac{1}{L} = \frac{2}{\sqrt{2}} = \sqrt{2}$。级数在 $|z| < \sqrt{2}$ 内收敛。




### 一致收敛性

复幂级数的关键性质是它在**严格小于收敛半径的任何闭圆盘上一致收敛**。

**定理**：如果复幂级数 $\sum_{n=0}^{\infty} a_n(z-a)^n$ 的收敛半径为 $R > 0$，那么对于任何 $R' < R$，该级数在闭圆盘 $\overline{B}_{R'}(a) = \{z \in \mathbb{C} : |z-a| \leq R'\}$ 上一致收敛。

#### 证明思路

为了证明一致收敛性，我们选择 $z_1 = a + (R'+R)/2$，使得 $R' < |z_1-a| < R$（当 $R = \infty$ 时，可以选择 $z_1 = a + 2R'$）。

对于 $z \in \overline{B}_{R'}(a)$（实际上只需 $|z-a| \leq R'$），我们有：

$$
|a_n(z-a)^n| = |a_n(z_1-a)^n| \left|\frac{z-a}{z_1-a}\right|^n \leq |a_n(z_1-a)^n|\theta^n
$$

其中 $\theta = \frac{2R'}{R'+R} < 1$。

由于 $|z_1-a| < R$，级数 $\sum_{n=0}^{\infty} a_n(z_1-a)^n$ 收敛，因此存在常数 $M$ 使得 $|a_n(z_1-a)^n| \leq M$。这意味着：

$$
|a_n(z-a)^n| \leq M\theta^n \text{ 对 } z \in \overline{B}_{R'}(a)
$$

由于 $\sum_{n=0}^{\infty} M\theta^n = \frac{M}{1-\theta}$ 收敛，根据 Weierstrass 判别法，$\sum_{n=0}^{\infty} a_n(z-a)^n$ 在 $\overline{B}_{R'}(a)$ 上一致收敛。

###  逐项微分性质

**定理**：设 $\sum_{n=0}^{\infty} a_n(z-a)^n$ 是收敛半径为 $R > 0$ 的复幂级数，则：

1. 该级数表示了开圆盘 $B_R(a)$ 上的可微（全纯）函数 $f(z) = \sum_{n=0}^{\infty} a_n(z-a)^n$
2. 函数 $f$ 可以逐项求导，导数由以下级数表示：

$$
f'(z) = \sum_{n=1}^{\infty} na_n(z-a)^{n-1} = \sum_{n=0}^{\infty} (n+1)a_{n+1}(z-a)^n
$$

3. 导数级数的收敛半径也是 $R$

#### 直接证明

考虑差商：

$$
\frac{f(z)-f(z_0)}{z-z_0} = \sum_{n=0}^{\infty} a_n \frac{z^n-z_0^n}{z-z_0} = \sum_{n=1}^{\infty} a_n(z^{n-1}+z^{n-2}z_0+\cdots+z_0^{n-1})
$$

当 $z \to z_0$ 时，上式趋近于：

$$
\sum_{n=1}^{\infty} na_nz_0^{n-1}
$$

这个极限交换是有效的，因为在 $z_0$ 的邻域内有一致收敛性。通过 Weierstrass 判别法可以证明，表达式：

$$
\left|a_n(z^{n-1}+z^{n-2}z_0+\cdots+z_0^{n-1})\right| \leq n|a_n|(\max\{|z|,|z_0|\})^{n-1}
$$

在 $z_0$ 的适当邻域内一致有界。

### 重要例子与应用

#### 例子 1：三角函数的幂级数展开

在复分析中，三角函数通常通过其幂级数定义：

$$
\cos z = \sum_{k=0}^{\infty} \frac{(-1)^k}{(2k)!}z^{2k}, \quad \sin z = \sum_{k=0}^{\infty} \frac{(-1)^k}{(2k+1)!}z^{2k+1}
$$

这些级数的收敛半径 $R = \infty$，可以在整个复平面上逐项求导，得到熟知的关系：$\sin' = \cos$, $\cos' = -\sin$。

在复平面中，三角函数与双曲函数有优雅的关系：

$$
\cos z = \cosh(iz), \quad \sin z = -i\sinh(iz)
$$

这表明复余弦函数在虚轴上的行为类似于实双曲余弦函数。

#### 2：正弦积分函数

正弦积分函数定义为：

$$
\text{Si}(x) = \int_0^x \frac{\sin t}{t} dt = \int_0^x \sum_{n=0}^{\infty} \frac{(-1)^n t^{2n}}{(2n+1)!} dt
$$

由于定义 $\sin x$ 的幂级数和 $\sin(x)/x$ 的收敛半径都是 $\infty$，函数级数在任何区间 $[0,x]$ 上一致收敛，因此可以逐项积分：

$$
\text{Si}(x) = \sum_{n=0}^{\infty} \int_0^x \frac{(-1)^n t^{2n}}{(2n+1)!} dt = \sum_{n=0}^{\infty} \frac{(-1)^n x^{2n+1}}{(2n+1)!(2n+1)} = x - \frac{x^3}{18} + \frac{x^5}{600} - \frac{x^7}{35280} \pm \cdots
$$

#### 例子 3：幂级数在组合计数中的应用

幂级数可以作为生成函数用于求解组合问题，如求 $s_n = 1^2 + 2^2 + \cdots + n^2$ 的闭式公式。

步骤：
1. 从几何级数开始：$\sum_{n=0}^{\infty} x^n = \frac{1}{1-x}$ （适用于 $|x| < 1$）
2. 求导得到：$\sum_{n=1}^{\infty} nx^{n-1} = \frac{1}{(1-x)^2}$
3. 乘以 $x$：$\sum_{n=1}^{\infty} nx^n = \frac{x}{(1-x)^2}$
4. 应用运算符 $x\frac{d}{dx}$ 两次得到：$\sum_{n=1}^{\infty} n^2x^n = \frac{x+x^2}{(1-x)^3}$
5. 乘以 $\frac{1}{1-x}$ 得到：$\sum_{n=1}^{\infty} s_n x^n = \frac{x+x^2}{(1-x)^4}$
6. 展开并比较系数，得到：$s_n = \frac{(2n+1)(n+1)n}{6}$

### 复可微性与全纯函数

复幂级数自然导致全纯函数的概念，即复可微的函数。一个函数 $f: D \to \mathbb{C}$ 在点 $z_0 \in D$ 处复可微，当且仅当极限：

$$
f'(z_0) = \lim_{h \to 0} \frac{f(z_0+h) - f(z_0)}{h}
$$

存在（其中 $h$ 是复数且趋向于零）。

由**幂级数定义的函数不仅在其收敛圆盘内是复可微的，而且拥有任意阶导数（全纯函数）**。这是实变幂级数所没有的强大性质。

**定理**：由收敛幂级数定义的函数 $f(z) = \sum_{n=0}^{\infty} a_n(z-a)^n$ 满足：
1. 在收敛圆盘内任一点 $z_0$ 处的 Taylor 展开就是函数本身
2. 导数系数满足 $f^{(k)}(a) = k!a_k$
3. 在 $a$ 附近任意小邻域内的行为完全决定了整个函数

### 复对数函数与三角级数求值

复对数函数 $\ln z = \ln|z| + i\arg z$ 提供了求解特定三角级数的强大工具。

例如，考虑级数 $\sum_{n=1}^{\infty} \frac{z^n}{n}$，它在单位圆盘内表示函数 $f(z) = -\ln(1-z)$。通过在单位圆周上（除 $z=1$ 外）计算该函数的值，我们可以得到：

$$
\sum_{n=1}^{\infty} \frac{\cos(nx)}{n} = -\ln\left(2\sin\frac{x}{2}\right), \quad (0 < x < 2\pi)
$$

$$
\sum_{n=1}^{\infty} \frac{\sin(nx)}{n} = \frac{\pi-x}{2}, \quad (0 < x < 2\pi)
$$

这些结果对于特定值可以得到著名的级数求和：
- $\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n} = \ln 2$
- $\sum_{n=0}^{\infty} \frac{(-1)^n}{2n+1} = \frac{\pi}{4}$

类似地，考虑 $\sum_{n=1}^{\infty} \frac{\cos(nx)}{n^2}$，可以证明它等于 $\frac{(x-\pi)^2}{4} - \frac{\pi^2}{12}$，从而得到：
- $\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}$（Basel 问题）
- $\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^2} = \frac{\pi^2}{12}$

## 复变微分与实变微分的对比

复函数 $f: D \to \mathbb{C}$, $D \subseteq \mathbb{C}$ 对应于一对实二元函数 $u, v: D \to \mathbb{R}$，通过 $f(z) = u(x,y) + iv(x,y)$。

**定理**：$f$ 在 $z = (x,y)$ 处复可微当且仅当 $f$ 在 $(x,y)$ 处实可微（即，$u,v$ 在 $(x,y)$ 可微）且满足：

$$
u_x(x,y) = v_y(x,y), u_y(x,y) = -v_x(x,y)
$$

特别地，$f$ 在整个区域上复可微当且仅当 $f$ 实可微且 $u,v$ 满足柯西 - 黎曼方程 (Cauchy-Riemann PDEs)：

$$
u_x = v_y \text{ 且 } u_y = -v_x
$$

## 复对数函数

复对数的主支 (principal branch of the complex logarithm) 定义为：  
该定义可以通过解方程

$$
w = e^{z} = e^{x+iy} = e^{x}\cos(y) + ie^{x}\sin(y)
$$

$$
\ln z = \ln|z| + i\arg z = \ln\sqrt{x^2 + y^2} + i\arctan(y/x), x = \text{Re}z > 0
$$

**定理**：$f(z) = \ln z$ 在其定义域上复可微且 $f'(z) = 1/z$。

对于 $|z-1| < 1$，我们有：

$$
\ln z = \sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n}(z-1)^n = (z-1) - \frac{(z-1)^2}{2} + \frac{(z-1)^3}{3} - \frac{(z-1)^4}{4} \pm \cdots
$$

## Trigononmetric Evaluation

### 第一个核心例子： $\sum_{n=1}^{\infty} \frac{z^n}{n}$ (Slides 51-58)

这个例子是推导三角级数求值的起点。

1.  **级数定义与收敛域**:
    * 考虑幂级数 $f(z) = \sum_{n=1}^{\infty} \frac{z^n}{n}$。
    * 通过比值判别法或者直接积分 $\sum_{n=0}^{\infty} w^n = \frac{1}{1-w}$ 可知，该级数的收敛半径 $R=1$。
    * 在收敛圆盘 $B_1(0) = \{ z \in \mathbb{C}; |z| < 1 \}$ 内部，我们知道 $f'(z) = \sum_{n=1}^{\infty} z^{n-1} = \frac{1}{1-z}$ (Slide 51)。
    * 结合 $f(0)=0$，积分可得 $f(z) = -\ln(1-z)$ (Slide 51)。这里的 $\ln$ 是复对数的主分支。

2.  **边界收敛性 (Convergence on the Boundary)**:
    * 我们关心的是当 $|z|=1$ 时级数的行为，即 $z=e^{ix}$ ($x \in [0, 2\pi)$) (Slide 52)。
    * 此时级数变为 $f(e^{ix}) = \sum_{n=1}^{\infty} \frac{e^{inx}}{n} = \sum_{n=1}^{\infty} \frac{\cos(nx)}{n} + i \sum_{n=1}^{\infty} \frac{\sin(nx)}{n}$。
    * 我们已知：
        * 当 $x=0$ ($z=1$) 时，实部为 $\sum \frac{1}{n}$ (调和级数 Harmonic Series)，发散。
        * 当 $x=\pi$ ($z=-1$) 时，级数为 $\sum \frac{(-1)^n}{n} = -\ln(2)$ (交错调和级数 Alternating Harmonic Series)，收敛 (Slide 52)。
    * 对于 $z \neq 1$ 且 $|z|=1$ 的情况，级数收敛。证明这一点需要更精细的工具，如 **Abel 求和法 (Abel Summation)** 或称为 **分部求和法 (Partial Summation)** (Slide 54)。
        * 基本思想：类似于分部积分，将求和式的项进行重组。设 $s_n(z) = \sum_{k=1}^n z^k = \frac{z(1-z^n)}{1-z}$。对 $z \neq 1$，当 $|z|=1$ 时，$|s_n(z)| = \left|\frac{z(1-z^n)}{1-z}\right| \le \frac{|z|(1+|z^n|)}{|1-z|} = \frac{2}{|1-z|}$，即 $s_n(z)$ 关于 $n$ 是一致有界的 (uniformly bounded) (只要 $z$ 远离 1，例如在区域 $D_r = \{z \in \mathbb{C}; |z| \le 1, |z-1| \ge r\}$ 上，界为 $M=2/r$) (Slide 55, 56)。
        * 级数 $\sum \frac{z^n}{n}$ 可以写成 $\sum a_n b_n$ 的形式，其中 $a_n = 1/n$ 单调递减趋于 0， $b_n = z^n$ 的部分和 $s_n(z)$ 一致有界。根据 **Dirichlet 一致收敛判别法 (Dirichlet's Test for Uniform Convergence)** (Slide 71，虽然这部分在 Slides 后面，但 Dirichlet 判别法是理解边界收敛性的标准工具，这里我们先借用其思想)，可以证明级数在 $D_r$ 上一致收敛。

3.  **利用连续性求值**:
    * 由于级数在 $B_1(0) \setminus \{1\}$ 的闭子集上（如 $D_r$）一致收敛，根据一致收敛的连续性定理 (Slide 15)，函数 $f(z) = \sum \frac{z^n}{n}$ 在 $B_1(0) \setminus \{1\}$ 上连续 (Slide 57)。
    * 因此，对于 $z_0 = e^{i\phi} \neq 1$，我们可以通过取极限来计算 $f(z_0)$：

        $$
        f(e^{i\phi}) = \lim_{r \uparrow 1} f(re^{i\phi}) = \lim_{r \uparrow 1} (-\ln(1-re^{i\phi}))

$$
    
*   利用 $-\ln(1-z) = -\ln|1-z| - i \arg(1-z)$ (Slide 51) 以及连续性，可以得到 (Slide 57, 58)：
        $$
        f(e^{i\phi}) = -\ln|1-e^{i\phi}| - i \arg(1-e^{i\phi})
        
$$

    *   通过三角恒等变换 $|1-e^{i\phi}|^2 = (1-\cos\phi)^2 + \sin^2\phi = 2 - 2\cos\phi = 4\sin^2(\phi/2)$，以及 $\arg(1-e^{i\phi}) = \arg(1-\cos\phi - i\sin\phi)$ (注意 $1-\cos\phi \ge 0$)，可以算出 $\arg = \arctan(\frac{-\sin\phi}{1-\cos\phi}) = \arctan(-\cot(\phi/2)) = \arctan(\tan(\phi/2 - \pi/2)) = (\phi-\pi)/2$ (对于 $0 < \phi < 2\pi$)。
    *   所以：
        $$
        f(e^{i\phi}) = -\ln(2\sin(\phi/2)) - i \frac{\phi-\pi}{2} = -\ln(2\sin(\phi/2)) + i \frac{\pi-\phi}{2}
        

$$
        注意这里 $\sin(\phi/2) > 0$ 因为 $0 < \phi < 2\pi$。

4.  **重要三角级数结果**:
    *   比较实部和虚部，我们得到两个重要的三角级数求值结果 (Slide 58)，对于 $0 < x < 2\pi$：
        $$
        \sum_{n=1}^{\infty} \frac{\cos(nx)}{n} = -\ln\left(2\sin\frac{x}{2}\right)
        
$$

        $$
        \sum_{n=1}^{\infty} \frac{\sin(nx)}{n} = \frac{\pi - x}{2}
        

$$


### 第二个核心例子： $\sum_{n=1}^{\infty} \frac{\cos(nx)}{n^2}$ (Slides 59-61)

这个例子展示了如何利用前面得到的级数和以及**逐项微分/积分定理**。

1.  **级数定义与一致收敛**:
    *   考虑函数 $g(x) = \sum_{n=1}^{\infty} \frac{\cos(nx)}{n^2}$。
    *   由于 $|\frac{\cos(nx)}{n^2}| \le \frac{1}{n^2}$ 且 $\sum_{n=1}^{\infty} \frac{1}{n^2}$ 收敛 ($\pi^2/6$)，根据 Weierstrass M 判别法，级数 $g(x)$ 在 $\mathbb{R}$ 上一致收敛 (Slide 59)。
    *   因此 $g(x)$ 是一个连续的 $2\pi$-周期函数。

2.  **逐项微分**:
    *   形式上对 $g(x)$ 求导得到级数 $\sum_{n=1}^{\infty} \frac{-\sin(nx) \cdot n}{n^2} = -\sum_{n=1}^{\infty} \frac{\sin(nx)}{n}$ (Slide 59)。
    *   我们知道这个导数级数 $-\sum \frac{\sin(nx)}{n} = - \frac{\pi-x}{2} = \frac{x-\pi}{2}$ 在 $(0, 2\pi)$ 内收敛。而且，我们在讨论第一个例子时，通过 Abel/Dirichlet 判别法得知 $\sum \frac{z^n}{n}$ 在 $D_r$ 上一致收敛，这意味着它的虚部 $\sum \frac{\sin(nx)}{n}$ 在例如 $[\delta, 2\pi-\delta]$ ($\delta>0$) 这样的闭区间上是一致收敛的。
    *   根据函数级数的逐项微分定理 (Slide 16)，如果 $g(x)$ 逐点收敛 (这里是一致收敛) 且其导数级数在区间上一致收敛，那么 $g(x)$ 在该区间上可微，并且其导数等于导数级数的和。
    *   因此，对于 $x \in (0, 2\pi)$，我们有 $g'(x) = \frac{x-\pi}{2}$ (Slide 60)。

3.  **积分求 $g(x)$**:
    *   对 $g'(x)$ 积分，得到 $g(x) = \int \frac{x-\pi}{2} dx = \frac{(x-\pi)^2}{4} + C$ (Slide 60)。
    *   确定常数 $C$：我们需要利用 $g(x)$ 的级数形式。我们可以计算 $g(x)$ 在 $[0, 2\pi]$ 上的积分。
        *   方法一 (利用级数)：根据一致收敛性，可以逐项积分 (Slide 19, 60)：
            $$
            \int_0^{2\pi} g(x) dx = \int_0^{2\pi} \sum_{n=1}^{\infty} \frac{\cos(nx)}{n^2} dx = \sum_{n=1}^{\infty} \int_0^{2\pi} \frac{\cos(nx)}{n^2} dx
            
$$

            $$
            = \sum_{n=1}^{\infty} \left[ \frac{\sin(nx)}{n^3} \right]_0^{2\pi} = \sum_{n=1}^{\infty} (0 - 0) = 0
            

$$
        *   方法二 (利用积分表达式)：
            $$
            \int_0^{2\pi} \left( \frac{(x-\pi)^2}{4} + C \right) dx = \left[ \frac{(x-\pi)^3}{12} + Cx \right]_0^{2\pi}
            
$$

            $$
            = \left( \frac{\pi^3}{12} + 2\pi C \right) - \left( \frac{(-\pi)^3}{12} + 0 \right) = \frac{\pi^3}{12} + 2\pi C + \frac{\pi^3}{12} = \frac{\pi^3}{6} + 2\pi C
            

$$
    *   令两个结果相等：$\frac{\pi^3}{6} + 2\pi C = 0$，解得 $C = -\frac{\pi^2}{12}$ (Slide 61)。

4.  **最终结果与特殊值**:
    *   因此，我们得到求值公式 (Slide 61)，对于 $0 \le x \le 2\pi$：
        $$
        g(x) = \sum_{n=1}^{\infty} \frac{\cos(nx)}{n^2} = \frac{(x-\pi)^2}{4} - \frac{\pi^2}{12}
        
$$

    *   代入特殊值可以得到著名的 Basel 问题结果：
        *   令 $x=0$：$g(0) = \sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{(-\pi)^2}{4} - \frac{\pi^2}{12} = \frac{\pi^2}{4} - \frac{\pi^2}{12} = \frac{3\pi^2 - \pi^2}{12} = \frac{2\pi^2}{12} = \frac{\pi^2}{6}$ (Slide 61)。
        *   令 $x=\pi$：$g(\pi) = \sum_{n=1}^{\infty} \frac{\cos(n\pi)}{n^2} = \sum_{n=1}^{\infty} \frac{(-1)^n}{n^2} = \frac{(\pi-\pi)^2}{4} - \frac{\pi^2}{12} = -\frac{\pi^2}{12}$。
            *   注意这给出 $\sum_{n=1}^{\infty} \frac{(-1)^{n-1}}{n^2} = \frac{\pi^2}{12}$ (Slide 61)。

### 第三个例子

这个例子的主要目的是帮助大家**区分函数序列 (sequence of functions) 的一致收敛性和函数级数 (series of functions) 的一致收敛性**，这是一个常见的混淆点。同时，它也演示了如何将序列的收敛问题转化为级数的收敛问题来分析。

**问题设定 (Slide 64):**

我们考虑定义在 $\mathbb{R}$ 上的函数序列 $(f_n)_{n \ge 0}$，其中：

$$
f_n(x) = \frac{x}{1 + nx^2}, \quad n = 0, 1, 2, \dots
$$

我们需要回答三个问题：

1.  序列 $(f_n)$ 是否一致收敛 (converge uniformly)？
2.  级数 $\sum_{n=0}^{\infty} f_n(x)$ 是否一致收敛？
3.  通过将序列 $(f_n)$ 的收敛问题转化为一个级数的收敛问题，并应用 Weierstrass M 判别法 (Weierstrass M-test) 来研究序列 $(f_n)$ 的一致收敛性。

**解答过程：**

**1. 序列 $(f_n)$ 的一致收敛性 (Slide 65)**

*   **逐点收敛 (Point-wise Convergence):**
    * 当 $x=0$ 时，$f_n(0) = \frac{0}{1+0} = 0$ 对所有 $n$ 成立，所以 $f_n(0) \to 0$。
    * 当 $x \neq 0$ 时，分母 $1+nx^2 \to \infty$ 当 $n \to \infty$。因为分子 $x$ 是固定的，所以 $f_n(x) = \frac{x}{1+nx^2} \to 0$ 当 $n \to \infty$。
    * 结论：函数序列 $(f_n)$ 逐点收敛于极限函数 $f(x) \equiv 0$。

*   **一致收敛 (Uniform Convergence):**
    * 要判断是否一致收敛于 $f(x)=0$，我们需要考察 $\sup_{x \in \mathbb{R}} |f_n(x) - f(x)| = \sup_{x \in \mathbb{R}} |f_n(x)|$ 是否随着 $n \to \infty$ 趋于 0。
    * 我们需要找到 $|f_n(x)|$ 的最大值。注意到 $f_n(x)$ 是奇函数，我们只需考虑 $x \ge 0$ 的情况并求 $f_n(x)$ 的最大值。当 $x \to \infty$ 时 $f_n(x) \to 0$。$f_n(x)$ 是连续可微的，最大值必然在导数为 0 的点取到。
    * 求导：

        $$
        f_n'(x) = \frac{d}{dx} \left( \frac{x}{1+nx^2} \right) = \frac{1 \cdot (1+nx^2) - x \cdot (2nx)}{(1+nx^2)^2} = \frac{1 - nx^2}{(1+nx^2)^2}

$$
    
*   令 $f_n'(x) = 0$，得到 $1-nx^2 = 0$，即 $x^2 = 1/n$。在 $x \ge 0$ 时，解得 $x_n = 1/\sqrt{n}$。
    *   计算最大值：
        $$
        M_n = f_n(x_n) = f_n(1/\sqrt{n}) = \frac{1/\sqrt{n}}{1 + n(1/\sqrt{n})^2} = \frac{1/\sqrt{n}}{1 + n(1/n)} = \frac{1/\sqrt{n}}{2} = \frac{1}{2\sqrt{n}}
        
$$

    *   由于对称性，$\inf_{x \in \mathbb{R}} f_n(x) = -M_n = -1/(2\sqrt{n})$。所以 $\sup_{x \in \mathbb{R}} |f_n(x)| = M_n = \frac{1}{2\sqrt{n}}$。
    *   检查极限：
        $$
        \lim_{n\to\infty} \sup_{x \in \mathbb{R}} |f_n(x)| = \lim_{n\to\infty} \frac{1}{2\sqrt{n}} = 0
        

$$
    *   结论：因为差值的上确界趋于 0，所以**序列 $(f_n)$ 在 $\mathbb{R}$ 上一致收敛于 0**。
    *   *备选方法 (Slide 66 提及)*：利用不等式 $1+nx^2 \ge 2\sqrt{nx^2} = 2\sqrt{n}|x|$ (由 $a^2+b^2 \ge 2ab$ 或 AM-GM 不等式得到)，可得 $|f_n(x)| = \frac{|x|}{1+nx^2} \le \frac{|x|}{2\sqrt{n}|x|} = \frac{1}{2\sqrt{n}}$ (对 $x \neq 0$ 成立，对 $x=0$ 也成立)。由于 $\frac{1}{2\sqrt{n}} \to 0$，这也证明了 $(f_n)$ 一致收敛于 0。

**2. 级数 $\sum_{n=0}^{\infty} f_n(x)$ 的一致收敛性 (Slide 66)**

*   我们需要判断级数 $\sum_{n=0}^{\infty} \frac{x}{1+nx^2}$ 的一致收敛性。
*   首先考虑**逐点收敛性**。
    *   当 $x=0$ 时，每一项都是 0，级数收敛于 0。
    *   当 $x \neq 0$ 时，级数的项为 $f_n(x) = \frac{x}{1+nx^2}$。对于固定的 $x \neq 0$，当 $n$ 很大时，$1+nx^2 \approx nx^2$，所以 $f_n(x) \approx \frac{x}{nx^2} = \frac{1}{x} \cdot \frac{1}{n}$。
    *   根据**级数收敛的必要条件**，若级数收敛，则通项必须趋于 0 ($f_n(x) \to 0$)。这一点满足。
    *   但是，这还不够。我们将其与**调和级数 (harmonic series)** $\sum_{n=1}^{\infty} \frac{1}{n}$ (发散) 进行比较。
    *   使用**极限比较判别法 (Limit Comparison Test)**：
        $$
        \lim_{n\to\infty} \frac{f_n(x)}{1/n} = \lim_{n\to\infty} \frac{x/(1+nx^2)}{1/n} = \lim_{n\to\infty} \frac{nx}{1+nx^2} = \lim_{n\to\infty} \frac{x}{(1/n)+x^2} = \frac{x}{x^2} = \frac{1}{x}
        
$$

        因为极限值 $1/x$ 是一个非零常数，并且 $\sum 1/n$ 发散，所以级数 $\sum_{n=1}^{\infty} f_n(x)$ 对于所有 $x \neq 0$ 都**发散**。 (Slide 66 用了更直接的大小比较：当 $n > 1/x^2$ 时，$f_n(x) = \frac{1/x}{1/x^2 + n} > \frac{1/x}{n+n} = \frac{1}{2x} \cdot \frac{1}{n}$，通过比较判别法得出结论。)
* 结论：因为级数 $\sum f_n(x)$ 仅在 $x=0$ 处逐点收敛，在 $x \neq 0$ 时发散，所以它**不可能一致收敛**于任何包含非零点的区间上。

**对比 (1) 和 (2)：** 这个例子清晰地显示了序列 $(f_n)$ 本身一致收敛 (趋于 0)，但由这些项构成的级数 $\sum f_n$ 却几乎处处发散。这强调了序列收敛和级数收敛是不同的概念。

> [!tip] 基本思路  
> 通过上述例子我们可以发现
> - 求证函数序列一致收敛与函数级数一致收敛我们都需先  
>   **1.  验证点态收敛，即当 n 充分大时，对应的项是否收敛到一个常值**  
>   **2. 验证极限函数与函数序列中的函数的差距能否控制**
> - 对于函数序列：我们关注单个函数的收敛性
> - 对于函数级数：我们关注级数（即函数序列求和）的收敛性

**3. 通过级数研究序列 $(f_n)$ 的一致收敛性 (Slides 67-70)**

*   **方法 (Slide 67)：**
    * 将序列 $(f_n)$ 的收敛问题转化为一个级数的收敛问题。定义一个新的函数序列 $(g_n)$：

        $$
        g_0(x) = f_0(x)

$$
    
    $$
        g_n(x) = f_n(x) - f_{n-1}(x) \quad \text{for } n \ge 1
        
$$

    *   这样构造之后，序列 $(f_n)$ 正是级数 $\sum_{k=0}^{\infty} g_k(x)$ 的**部分和序列 (sequence of partial sums)**，即 $f_n(x) = \sum_{k=0}^{n} g_k(x)$。
    *   因此，序列 $(f_n)$ 一致收敛 **当且仅当** 级数 $\sum_{k=0}^{\infty} g_k(x)$ 一致收敛。
    *   我们的目标是证明 $\sum g_n$ 一致收敛，然后由此推断 $(f_n)$ 一致收敛。我们将尝试使用 Weierstrass M 判别法。

*   **计算 $g_n(x)$ (Slide 68)：**
    *   $g_0(x) = f_0(x) = \frac{x}{1+0 \cdot x^2} = x$。
    * 对于 $n \ge 1$：

        $$
        g_n(x) = f_n(x) - f_{n-1}(x) = \frac{x}{1+nx^2} - \frac{x}{1+(n-1)x^2}

$$
    
    通分：
        $$
        g_n(x) = x \left[ \frac{(1+(n-1)x^2) - (1+nx^2)}{(1+nx^2)(1+(n-1)x^2)} \right] = x \left[ \frac{-x^2}{(1+nx^2)(1+(n-1)x^2)} \right]
        
$$

        $$
        g_n(x) = \frac{-x^3}{(1+nx^2)(1+(n-1)x^2)}
        

$$

*   **应用 Weierstrass M 判别法 (Slides 68-70)：**
    *   我们需要找到一个正项级数 $\sum M_n$ 使得 $|g_n(x)| \le M_n$ 对所有 $x \in \mathbb{R}$ 成立，并且 $\sum M_n$ 收敛。
    *   **困难点 (Problem 1, Slide 68)：** $g_0(x) = x$ 是无界的！Weierstrass M 判别法要求级数的每一项都被一个常数 $M_n$ 界定。因此，我们不能直接将 M 判别法应用于 $\sum_{n=0}^{\infty} g_n(x)$。
    *   **解决方案 (Slide 68, 70)：** M 判别法可以应用于级数的尾部。如果 $\sum_{n=N}^{\infty} g_n(x)$ 一致收敛，那么原级数 $\sum_{n=0}^{\infty} g_n(x)$ (以及其部分和序列 $f_n(x)$) 也是一致收敛的（只要前面的有限项 $g_0, \dots, g_{N-1}$ 都是有良好定义的函数）。所以，我们尝试对 $\sum_{n=1}^{\infty} g_n(x)$ 或 $\sum_{n=2}^{\infty} g_n(x)$ 应用 M 判别法。
    *   **寻找 $M_n$ (Problem 2, Slide 69-70)：** 我们需要为 $|g_n(x)| = \frac{|x^3|}{(1+nx^2)(1+(n-1)x^2)}$ (对于 $n \ge 1$) 寻找一个与 $x$ 无关的上界 $M_n$。
        *   直接求 $g_n(x)$ 的极值比较复杂。Slide 69 和 70 采用了分段估计的策略：
        *   **当 $x$ 较小 (Slide 69)**，例如 $|x| \le 1/\sqrt{n}$ 时：
            这时 $nx^2 \le 1$。我们可以利用分母的下界 $1+nx^2 \ge 1$ 和 $1+(n-1)x^2 \ge 1$。分子 $|x^3| \le (1/\sqrt{n})^3 = 1/n^{3/2}$。所以：
            $$
            |g_n(x)| \le \frac{|x^3|}{1 \cdot 1} \le \frac{1}{n^{3/2}}
            
$$

        *   **当 $x$ 较大 (Slide 70)**，例如 $|x| > 1/\sqrt{n}$ 时 ($n \ge 2$)：
            这时 $nx^2 > 1$ 和 $(n-1)x^2 > (n-1)/n \approx 1$。我们可以利用分母的增长： $1+nx^2 > nx^2$ 且 $1+(n-1)x^2 > (n-1)x^2$。所以：
            $$
            |g_n(x)| = \frac{|x^3|}{(1+nx^2)(1+(n-1)x^2)} < \frac{|x^3|}{(nx^2)((n-1)x^2)} = \frac{|x^3|}{n(n-1)x^4} = \frac{1}{n(n-1)|x|}
            

$$
            由于 $|x| > 1/\sqrt{n}$，所以 $1/|x| < \sqrt{n}$。代入上式：
            $$
            |g_n(x)| < \frac{\sqrt{n}}{n(n-1)} = \frac{1}{\sqrt{n}(n-1)}
            
$$

        *   **统一界 (Slide 70)：** 我们现在有两个上界，一个用于小 $x$，一个用于大 $x$。对于 $n \ge 2$，哪个界更大？$\frac{1}{n^{3/2}}$ 和 $\frac{1}{(n-1)\sqrt{n}}$。因为 $n-1 < n$，所以 $\sqrt{n}(n-1) < n\sqrt{n} = n^{3/2}$，因此 $\frac{1}{(n-1)\sqrt{n}} > \frac{1}{n^{3/2}}$。这意味着 $\frac{1}{(n-1)\sqrt{n}}$ 可以作为适用于所有 $x$ 的统一上界 $M_n$ (对于 $n \ge 2$)。
            $$
            |g_n(x)| \le M_n = \frac{1}{(n-1)\sqrt{n}} \quad \text{for } n \ge 2, \forall x \in \mathbb{R}
            

$$
    *   **检验 $\sum M_n$ 的收敛性 (Slide 70)：** 我们需要判断级数 $\sum_{n=2}^{\infty} M_n = \sum_{n=2}^{\infty} \frac{1}{(n-1)\sqrt{n}}$ 是否收敛。
        *   当 $n$ 很大时，$n-1 \approx n$，所以 $M_n \approx \frac{1}{n\sqrt{n}} = \frac{1}{n^{3/2}}$。
        *   这是一个 p-级数 (p-series) $\sum 1/n^p$ 的形式，其中 $p=3/2 > 1$，所以 $\sum 1/n^{3/2}$ 收敛。
        *   根据**极限比较判别法**，由于 $\lim_{n\to\infty} \frac{M_n}{1/n^{3/2}} = \lim_{n\to\infty} \frac{n^{3/2}}{(n-1)\sqrt{n}} = \lim_{n\to\infty} \frac{n}{n-1} = 1$，并且 $\sum 1/n^{3/2}$ 收敛，所以 $\sum_{n=2}^{\infty} M_n$ 也收敛。

*   **结论 (Slide 70)：**
    *   根据 Weierstrass M 判别法，级数 $\sum_{n=2}^{\infty} g_n(x)$ 在 $\mathbb{R}$ 上一致收敛。
    *   由于 $f_n(x) = g_0(x) + g_1(x) + \sum_{k=2}^{n} g_k(x)$，并且 $\sum_{k=2}^{\infty} g_k(x)$ 一致收敛，这意味着 $f_n(x)$ 在 $\mathbb{R}$ 上**一致收敛** (收敛到 $g_0(x)+g_1(x)+\sum_{k=2}^\infty g_k(x)$)。
    *   这通过另一种方法（尽管更复杂）验证了第 (1) 问的结论。

**总结:**

这个例子非常巧妙地展示了：

1.  一个函数序列 $(f_n)$ 可以一致收敛。
2.  但由该序列构成的函数级数 $\sum f_n$ 可能发散。
3.  序列的收敛性可以通过构造 $g_n = f_n - f_{n-1}$ 转化为级数 $\sum g_n$ 的收敛性问题。
4.  Weierstrass M 判别法是证明级数一致收敛的有力工具，但有时需要对级数的开始几项做特殊处理 (如 $g_0$ 无界的情况)。



### 总结

> [!tip] 一般思路
> **1. 确定所求级数的一致收敛性**
> 利用 **Weierstrass 判别法** 确定级数的绝对收敛上界，证明其绝对值上界的级数收敛，进而证明该级数收敛
> **2. 充分利用一致收敛的性质**
> 利用一致收敛的 **连续性、逐项微分、逐项积分** 的性质，将所求级数与已有结果充分结合
> 求解常数时可以考虑
> - 特殊值
> - 对等式两边分别积分微分
> 
> **3. 关注经典结果** 


## 多元情况


**1. 背景与动机**

*   我们在课程前面主要讨论的是单变量函数序列/级数的一致收敛，即 $f_k: I \to \mathbb{R}$ (其中 $I \subseteq \mathbb{R}$)。这是因为在标准的微积分教学顺序中，一致收敛的概念通常在学习多变量微积分之前引入。
*   然而，我们建立的关于一致收敛的核心定理——**连续性定理 (Continuity Theorem)**、**微分定理 (Differentiation Theorem)** 和**积分定理 (Integration Theorem)**——都有对应的多变量版本，这些版本在数学和物理的许多领域都非常重要。
*   这部分 Slides 主要关注**微分定理的多变量推广**。

**2. 多变量微分定理 (Theorem (differentiation, multivariable case), Slide 80)**

这个定理描述了在什么条件下，一个收敛的 $C^1$ 函数序列的极限函数也是 $C^1$，并且可以交换极限与偏导数的顺序。

*   **设定:**
    *   我们有一个定义在 $D \subseteq \mathbb{R}^n$ (n 维欧氏空间中的一个子集) 上的函数序列 $(f_k)_{k \in \mathbb{N}}$，每个函数 $f_k: D \to \mathbb{R}$。
    *   **向量表示:** 我们用 $\mathbf{x} = (x_1, x_2, \dots, x_n)$ 表示 $D$ 中的点。

*   **假设条件:**
    1.  **光滑性:** 每个函数 $f_k$ 都是 $C^1$ 函数。这意味着 $f_k$ 的所有一阶偏导数 $\frac{\partial f_k}{\partial x_i}$ ($i=1, \dots, n$) 都存在且在 $D$ 上连续。
    2.  **逐点收敛:** 函数序列 $(f_k)$ 在 $D$ 上**逐点收敛 (point-wise converges)** 于某个极限函数 $f(\mathbf{x}) = \lim_{k\to\infty} f_k(\mathbf{x})$。
    3.  **导数一致收敛:** 对于**每一个**偏导数指标 $i$ ($1 \le i \le n$)，对应的**偏导数序列** $\left( \frac{\partial f_k}{\partial x_i} \right)_{k \in \mathbb{N}}$ 在 $D$ 上**一致收敛 (converges uniformly)**。 (注意：这里要求 *所有 n 个* 偏导数序列都一致收敛)。

*   **结论:**
    1.  **极限函数的光滑性:** 极限函数 $f$ 也是一个 $C^1$ 函数。
    2.  **极限与偏导交换:** $f$ 的偏导数等于 $f_k$ 偏导数的极限，即：
        $$
        \frac{\partial f}{\partial x_i}(\mathbf{x}) = \lim_{k\to\infty} \frac{\partial f_k}{\partial x_i}(\mathbf{x}) \quad \text{for } 1 \le i \le n \text{ and } \mathbf{x} \in D.
        
$$

**3. 证明思路 (Proof Outline, Slide 81)**

证明这个定理的关键在于巧妙地将多变量问题“降维”到我们已经熟悉的单变量情形。

*   **回顾 $C^1$:** 要证明 $f$ 是 $C^1$，我们需要证明两件事：(a) $f$ 的所有一阶偏导数 $\frac{\partial f}{\partial x_i}$ 都存在；(b) 这些偏导数本身都是关于 $\mathbf{x}$ 的连续函数。
*   **(a) 偏导数存在性与极限交换:**
    * 我们以 $\frac{\partial f}{\partial x_1}$ 为例。固定 $x_2, \dots, x_n$ 不变，将 $f_k$ 视为仅关于 $x_1$ 的单变量函数 $h_k(x_1) = f_k(x_1, x_2, \dots, x_n)$。
    *   $h_k(x_1)$ 的导数就是偏导数 $\frac{\partial f_k}{\partial x_1}$ (作为 $x_1$ 的函数)。
    * 根据假设 (2)，序列 $h_k(x_1)$ 逐点收敛于 $h(x_1) = f(x_1, x_2, \dots, x_n)$。
    * 根据假设 (3)，导数序列 $h_k'(x_1) = \frac{\partial f_k}{\partial x_1}$ (作为 $x_1$ 的函数) 是一致收敛的。
    * 现在，对于 $h_k(x_1)$ 和 $h(x_1)$，我们满足了**单变量微分定理 (Slide 16)** 的所有条件！
    * 应用单变量微分定理，我们得出结论：极限函数 $h(x_1)$ 可导，并且 $h'(x_1) = \lim_{k\to\infty} h_k'(x_1)$。
    * 这表明 $\frac{\partial f}{\partial x_1}$ 存在，并且 $\frac{\partial f}{\partial x_1} = \lim_{k\to\infty} \frac{\partial f_k}{\partial x_1}$。
    * 对 $i=2, \dots, n$ 重复此过程，证明所有偏导数都存在且满足极限交换公式。
*   **(b) 偏导数的连续性:**
    * 我们已经知道 $\frac{\partial f}{\partial x_i} = \lim_{k\to\infty} \frac{\partial f_k}{\partial x_i}$，并且这个收敛是**一致的** (假设 3)。
    * 根据假设 (1)，每个 $\frac{\partial f_k}{\partial x_i}$ 都是**连续的** (作为 $\mathbb{R}^n \to \mathbb{R}$ 的函数)。
    * 此时，我们应用**多变量版本的连续性定理** (即单变量连续性定理 Slide 15 的直接推广)：一个连续函数序列的**一致极限**也是连续函数。
    * 因此，作为连续函数序列 $(\frac{\partial f_k}{\partial x_i})$ 的一致极限，$\frac{\partial f}{\partial x_i}$ 必定是连续函数。
    * 由于所有偏导数 $\frac{\partial f}{\partial x_i}$ 都连续，所以 $f$ 是 $C^1$ 函数。

**4. 定理的局部性 (Note on Locality, Slide 82)**

* 微分是一个**局部性质**，即一个函数在某点是否可微只取决于该点附近的行为。
* 这意味着多变量微分定理的假设条件可以适当减弱：我们不需要偏导数序列 $(\frac{\partial f_k}{\partial x_i})$ 在整个 $D$ 上一致收敛，只需要它们在**每一点 $\mathbf{x} \in D$ 的某个邻域 $D_\mathbf{x}$ 上一致收敛**即可。这个 " 局部一致收敛 " 的条件仍然足以保证结论成立。
* 类似的局部化思想也适用于连续性定理和积分定理（特别是在紧致积分域上，利用 Heine-Borel 定理）。

**5. 应用实例：求解拉普拉斯方程 (Application: Laplace's Equation, Slides 83-84)**

这是一个非常经典的应用，展示了如何利用上述定理来验证一个由级数定义的函数是某个偏微分方程的解。

*   **问题:** 证明函数 $f(x, y) = \sum_{k=0}^{\infty} c_k e^{-ky} \cos(kx)$ 在上半平面 $\mathbb{R} \times \mathbb{R}^+$ (即 $y>0$) 内满足拉普拉斯方程 $\Delta f = \frac{\partial^2 f}{\partial x^2} + \frac{\partial^2 f}{\partial y^2} = 0$。这里假设系数 $c_k$ 最多是多项式增长 ($c_k = O(k^d)$)。
*   **思路:**
    1.  **形式计算 (Assume term-wise differentiation):** 假设我们可以逐项求导两次，计算出 $\frac{\partial^2 f}{\partial x^2}$ 和 $\frac{\partial^2 f}{\partial y^2}$ 的级数表达式 (Slide 83)。
        *   $\frac{\partial^2 f}{\partial x^2} = \sum_{k=0}^{\infty} c_k e^{-ky} (-k^2 \cos(kx))$
        *   $\frac{\partial^2 f}{\partial y^2} = \sum_{k=0}^{\infty} c_k (k^2 e^{-ky}) \cos(kx)$
    2.  **验证方程:** 将两者相加，发现每一项都变成 $c_k e^{-ky} \cos(kx) (-k^2 + k^2) = 0$，所以形式上 $\Delta f = 0$。
    3.  **关键步骤：证明逐项微分的合法性 (Justification, Slide 84):** 我们需要应用多变量微分定理两次，来确保上面的形式计算是有效的。
        * 我们需要证明定义 $f$ 的级数，以及定义其一阶、二阶偏导数的级数，都在上半平面的**局部**一致收敛。
        *   **目标区域:** 只需证明在任何形如 $H_\delta = \{(x, y) \in \mathbb{R}^2 \mid y \ge \delta\}$ (其中 $\delta > 0$ 是任意小的正常数) 的水平带状区域上一致收敛即可。因为上半平面中的任何点 $(x_0, y_0)$ 必包含在某个 $H_\delta$ 中 (取 $\delta < y_0$)。
        *   **使用 Weierstrass M 判别法:** 以 $\frac{\partial^2 f}{\partial x^2}$ 的级数 $\sum (-k^2 c_k e^{-ky} \cos(kx))$ 为例：
            * 在 $H_\delta$ 上， $|-k^2 c_k e^{-ky} \cos(kx)| \le k^2 |c_k| e^{-ky} |\cos(kx)|$。
            * 利用已知条件：$|c_k| \le C k^d$ (对大 k)，$e^{-ky} \le e^{-k\delta}$ (因为 $y \ge \delta$)，$|\cos(kx)| \le 1$。
            * 得到上界：$|-k^2 c_k e^{-ky} \cos(kx)| \le k^2 (C k^d) e^{-k\delta} \cdot 1 = C k^{d+2} e^{-k\delta}$。
            * 令 $M_k = C k^{d+2} e^{-k\delta}$。这是一个与 $(x, y)$ 无关的界。
        *   **检验 $\sum M_k$ 收敛性:** 级数 $\sum_{k=0}^{\infty} C k^{d+2} e^{-k\delta}$ 是否收敛？是的，因为 $e^{-k\delta}$ 的指数衰减速度远快于任何多项式 $k^{d+2}$ 的增长速度 (只要 $\delta > 0$)。可以用比值判别法或根值判别法证明。
        *   **M 判别法结论:** $\sum \frac{\partial^2 f}{\partial x^2}$ 在 $H_\delta$ 上一致收敛。
        *   **推广:** 类似地可以证明 $f$ 本身以及其它一阶、二阶偏导数的级数在 $H_\delta$ 上都一致收敛。
        *   **应用微分定理:** 由于定义二阶偏导数的级数是一致收敛的，我们可以应用多变量微分定理 (两次)：
            * 首先，由于 $\sum \frac{\partial f}{\partial x}$ 和 $\sum \frac{\partial f}{\partial y}$ 一致收敛，且 $\sum f$ 逐点收敛，所以 $f$ 是 $C^1$ 函数，且 $\frac{\partial f}{\partial x} = \sum \frac{\partial f_k}{\partial x}$，$\frac{\partial f}{\partial y} = \sum \frac{\partial f_k}{\partial y}$。
            * 然后，再对 $\frac{\partial f}{\partial x}$ 和 $\frac{\partial f}{\partial y}$ 应用定理。例如，由于 $\sum \frac{\partial^2 f}{\partial x^2}$ 和 $\sum \frac{\partial^2 f}{\partial y \partial x}$ (需要额外验证这个混合偏导级数也一致收敛，通常是可以的) 一致收敛，且 $\sum \frac{\partial f}{\partial x}$ 逐点收敛，所以 $\frac{\partial f}{\partial x}$ 是 $C^1$ 函数，即 $f$ 是 $C^2$ 函数。并且 $\frac{\partial^2 f}{\partial x^2} = \sum \frac{\partial^2 f_k}{\partial x^2}$。
        * 最终，我们证明了形式计算中的逐项微分是合法的。

## 均匀收敛的进一步判别法

### Cauchy 一致收敛判别法

1. 函数序列 $(f_n)$ 一致收敛当且仅当对于每个 $\varepsilon > 0$，存在 $N \in \mathbb{N}$ 使得对于所有 $m,n > N$ 和所有 $x \in D$ 都有 $|f_m(x) - f_n(x)| < \varepsilon$。

2. 函数级数 $\sum_{n=1}^{\infty} f_n$ 一致收敛当且仅当对于每个 $\varepsilon > 0$，存在 $N \in \mathbb{N}$ 使得对于所有 $n \geq m > N$ 和所有 $x \in D$ 都有 $\left|\sum_{k=m}^{n} f_k(x)\right| < \varepsilon$。

### Dirichlet 一致收敛判别法

设 $(f_n)$ 是 $D$ 上单调递减的实值函数序列，且 $(g_n)$ 是 $D$ 上的复值函数序列。如果满足以下条件之一，函数级数 $\sum_{n=1}^{\infty} f_n g_n$ 在 $D$ 上一致收敛：

1. $(f_n)$ 一致收敛到 $D$ 上的 $0$，且级数 $\sum_{n=1}^{\infty} g_n$ 的部分和 $G_n = g_1 + \cdots + g_n$ 在 $D$ 上一致有界。

### Abel 一致收敛判别法

如果 $(f_n)$ 在 $D$ 上一致有界，且级数 $\sum_{n=1}^{\infty} g_n$ 在 $D$ 上一致收敛，则函数级数 $\sum_{n=1}^{\infty} f_n g_n$ 在 $D$ 上一致收敛。

## 含参数广义积分的一致收敛

### 定义

假设 $f$ 是定义域为 $D \times [0,\infty)$ 的实值函数，且对于每个 $R \in [0,\infty)$ 和 $x \in D$，$\int_0^R f(x,t) dt$ 有定义。

1. 如果对于每个 $x \in D$，$\lim_{R \to \infty} \int_0^R f(x,t) dt$ 存在，则称 $\int_0^{\infty} f(x,t) dt$ 在 $D$ 上点态收敛。

2. 如果 $\int_0^{\infty} f(x,t) dt$ 点态收敛且对于每个 $\varepsilon > 0$，存在 " 一致的 " 响应 $R_0 \in [0,\infty)$ 使得对于所有 $R > R_0$ 和所有 $x \in D$ 都有：

   $$


\left|F(x) - \int_0^R f(x,t) dt\right| = \left|\int_R^{\infty} f(x,t) dt\right| < \varepsilon

$$
   则称 $\int_0^{\infty} f(x,t) dt$ 在 $D$ 上一致收敛。

### 连续性定理（广义积分）
假设 $I \subseteq \mathbb{R}$ 是一个区间，$f: I \times [a,\infty) \to \mathbb{R}$ 是连续的二元函数，且 $\int_a^{\infty} f(x,t) dt$ 在 $I$ 上一致收敛。则 $F: I \to \mathbb{R}$, $x \mapsto \int_a^{\infty} f(x,t) dt$ 是连续的。

### 微分定理（广义积分）
假设 $I \subseteq \mathbb{R}$ 是一个区间，$f: I \times [a,\infty) \to \mathbb{R}$ 是连续的二元函数，偏导数 $f_x = \partial f/\partial x: I \times [a,\infty) \to \mathbb{R}$ 存在且也是连续的二元函数，$\int_a^{\infty} f(x,t) dt$ 在 $I$ 上点态收敛，且 $\int_a^{\infty} f_x(x,t) dt$ 在 $I$ 上一致收敛。则 $F: I \to \mathbb{R}$, $x \mapsto \int_a^{\infty} f(x,t) dt$ 可微且
$$

F'(x) = \int_a^{\infty} f_x(x,t) dt

$$

即我们可以在积分号下求导。

### Weierstrass 判别法（广义积分）
假设存在函数 $\Phi: [0,\infty) \to \mathbb{R}$ 使得对于所有 $(x,t) \in D \times [0,\infty)$ 都有 $|f(x,t)| \leq \Phi(t)$，且 $\int_0^{\infty} \Phi(t) dt$ 在 $\mathbb{R}$ 中收敛。

则 $\int_0^{\infty} f(x,t) dt$ 在 $D$ 上一致（且绝对）收敛。

### Dirichlet 与 Abel 判别法（广义积分）
假设对于每个 $x \in D$，函数 $t \mapsto f(x,t)$ 连续可微且单调递减，且 $t \mapsto g(x,t)$ 连续。则在以下条件之一下，$\int_0^{\infty} f(x,t)g(x,t) dt$ 在 $D$ 上一致收敛：

1. 对于 $t \to \infty$，$f(x,t)$ 一致收敛到零，且存在"一致界" $M > 0$ 使得对于所有 $R \in [0,\infty)$ 和 $x \in D$ 都有 $\left|\int_0^R g(x,t) dt\right| \leq M$。

2. 存在 $M > 0$ 使得对于所有 $t \in [0,\infty)$ 和 $x \in D$ 都有 $|f(x,t)| \leq M$，且 $\int_0^{\infty} g(x,t) dt$ 在 $D$ 上一致收敛。

