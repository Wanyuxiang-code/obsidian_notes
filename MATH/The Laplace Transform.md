---
title: The Laplace Transform
date: 2025-05-15
date modified: 2025-05-15
categories: Math285
tags:
  - Math285
---

#Math285 


## 拉普拉斯变换 (The Laplace Transform)

### 积分变换与拉普拉斯变换的定义 (Integral Transforms and Definition of Laplace Transform)


- **积分变换 (Integral Transforms)**
    -   **一般定义**: 积分变换是一种数学运算，它将一个函数 $f(t)$ 通过一个积分核函数 $K(s,t)$ 映射到另一个函数 $F(s)$。形式如下：
        $$
        F(s) = \int_a^b K(s,t) f(t) dt
        $$
        这里的 $F(s)$ 是 $f(t)$ 的变换，$s$ 是变换域的变量 (通常是复数)。


-   **拉普拉斯变换的定义**: 拉普拉斯变换是一种特殊的积分变换，其中积分区间是 $(0, \infty)$，积分核是 $K(s,t) = e^{-st}$。
        对于函数 $f(t)$ (定义在 $t \ge 0$)，其拉普拉斯变换 $F(s)$ 或 $\mathcal{L}\{f(t)\}$ 定义为：
        $$
        F(s) = \mathcal{L}\{f(t)\} = \int_0^\infty e^{-st} f(t) dt
        $$
        这个积分针对所有使得积分收敛的复数 $s$ 进行定义。

### 拉普拉斯变换的适定域 (An Appropriate Domain for $\mathcal{L}$)

不是所有的函数都有拉普拉斯变换。为了确保积分收敛，函数 $f(t)$ 通常需要满足某些条件：

- **函数的条件**
    1.  **分段连续 (Piecewise Continuous)**:
        -   (i) 函数 $f(t)$ 的不连续点集 $\Delta$ 是离散的（即没有极限点）。
        -   (ii) $f(t)$ 在不包含不连续点的每个连通区间上是连续的。
        -   (iii) 在每个不连续点 $\alpha \in \Delta$，单侧极限 $f(\alpha^+)$ 和 $f(\alpha^-)$ 存在。
        **通俗理解**: 函数可以有**跳跃间断点**，但**不能有无穷震荡类型的间断点**，且在**任何有界区间内只能有有限个跳跃间断点**。

    2.  **指数阶 (Exponential Order)**:
        函数 $f(t)$ 当 $t \to \infty$ 时是（至多）指数阶的，如果存在实数 $a$ 和正常数 $K, M$，使得：
        $$
        |f(t)| \le K e^{at} \quad \text{当 } t \ge M
        $$
        指数阶意味着函数的增长速度不会超过某个指数函数 $e^{at}$。“指数阶”就像给函数的增长速度设了一个上限，它不能无限快地飞向无穷大。
        如果一个函数是分段连续且为指数阶的，那么它的拉普拉斯变换 $\mathcal{L}\{f(t)\}$ 是良定义的 (well-defined)，即积分是收敛的（对于某些 $s$ 值）。

- **关于条件的注解**
    -   分段连续允许有无限多个跳跃间断点，只要在任何有界子区间 $[0,R]$ 内是有限的 (例如 $f(t) = \lfloor t \rfloor$ 取整函数)。
    -   指数阶 $f(t) = O(e^{at})$ 的条件，其中 $a$ 可以是负数 (意味着函数衰减)。$a$ 越小，对函数增长的限制越强。
    -   **精确指数阶 (Exact Exponential Order)** $eo(f)$ 定义为使得 $f(t)=O(e^{at})$ 成立的最小的 $a$ 值 (下确界)。
        例如，多项式 $t^n$ 的精确指数阶是 $0$，因为对于任何 $a>0$，$t^n = O(e^{at})$，但 $t^n \neq O(e^{0t}) = O(1)$ (除非 $n=0$)。

- **指数阶的例子**
    1.  非零多项式和有理函数 (分母非零) 的精确指数阶都是 $0$。
    2.  指数多项式 $t \mapsto c_1 e^{a_1 t} + \dots + c_n e^{a_n t}$ ($a_1 < a_2 < \dots < a_n$) 的精确指数阶是 $a_n$ (增长最快的那一项的指数)。
    3.  $\sin(at), \cos(at)$ ($a \neq 0$) 的精确指数阶是 $0$ (因为它们是有界的，可以被 $K e^{0t}$ 控制)。
    4.  $t \mapsto e^{t^2}$ 不是指数阶的，因为它比任何 $e^{at}$ 增长都快。而 $t \mapsto e^{-t^2}$ 的精确指数阶是 $-\infty$ (因为它比任何 $e^{at}$ 衰减都快)。

### 拉普拉斯变换的解析性与微分性质 (Analyticity and Differentiation of $F(s)$)

- **$F(s)$ 的解析性定理**
    假设 $f(t)$ 是分段连续的，且精确指数阶为 $a \in \mathbb{R} \cup \{\pm\infty\}$。
    1.  如果 $a = +\infty$ (如 $e^{t^2}$)，则 $\mathcal{L}\{f(t)\}$ 可能对任何 $s$ 都不定义。
    2.  如果 $a \in \mathbb{R}$，则 $\mathcal{L}\{f(t)\}$ **至少在开半平面 $\text{Re}(s) > a$ 上有定义且解析 (analytic)**。
        **重要**: 解析意味着 $F(s)$ 在该区域内是复可微的，可以展开成幂级数。
    3.  如果 $a = -\infty$ (如 $e^{-t^2}$)，则 $\mathcal{L}\{f(t)\}$ 在整个复平面上都有定义且解析 (即 $F(s)$ 是一个**整函数 (entire function)**)。

    **$s$ 域微分性质**: 在情况 2 和 3 中，$F(s) = \mathcal{L}\{f(t)\}$ 可以在积分号下对 $s$ 微分：
    $$
    F'(s) = \frac{d}{ds} \int_0^\infty e^{-st} f(t) dt = \int_0^\infty \frac{\partial}{\partial s} (e^{-st} f(t)) dt = \int_0^\infty (-t) e^{-st} f(t) dt = -\mathcal{L}\{t f(t)\}
    $$
    推广得到：
    $$
    F^{(n)}(s) = (-1)^n \mathcal{L}\{t^n f(t)\}
    $$
 

- **定理证明概要**
    -   **证明思路 (Slide 9)**: 假设 $f(t)$ 是实值的。对于 $\text{Re}(s) \ge a+\delta$ ($\delta > 0$)，有 $|f(t)e^{-st}| = |f(t)|e^{-\text{Re}(s)t} \le K e^{at} e^{-(a+\delta)t} = K e^{-\delta t}$。由于 $\int_M^\infty K e^{-\delta t} dt$ 收敛，根据**魏尔斯特拉斯 M-判别法 (Weierstrass M-test)**，积分 $\int_0^\infty f(t)e^{-st} dt$ 在 $\text{Re}(s) \ge a+\delta$ 上一致收敛。一致收敛保证了 $F(s)$ 在 $\text{Re}(s) > a$ 上的连续性和可积性。通过证明积分号下微分的条件也满足，可以得到 $F(s)$ 的复可微性，从而得到解析性。
    -   **另一种证明思路 (Slide 10)**: 将 $F(s) = F(x+iy)$ 写成 $u(x,y) + iv(x,y)$ 的形式，然后验证 $u$ 和 $v$ 满足柯西-黎曼方程，从而证明 $F(s)$ 的复可微性（解析性）。

### 常见函数的拉普拉斯变换示例 (Examples of Laplace Transforms)

- **幻灯片 11**:
    1.  $\mathcal{L}\{1\} = \int_0^\infty e^{-st} \cdot 1 dt = \left[-\frac{1}{s}e^{-st}\right]_0^\infty = \frac{1}{s}$  (对于 $\text{Re}(s) > 0$)
    2.  $\mathcal{L}\{e^{at}\} = \int_0^\infty e^{-st} e^{at} dt = \int_0^\infty e^{-(s-a)t} dt = \frac{1}{s-a}$ (对于 $\text{Re}(s) > \text{Re}(a)$)
    3.  $\mathcal{L}\{\cos(bt)\} = \mathcal{L}\left\{\frac{e^{ibt} + e^{-ibt}}{2}\right\} = \frac{1}{2} \left( \frac{1}{s-ib} + \frac{1}{s+ib} \right) = \frac{1}{2} \frac{s+ib + s-ib}{(s-ib)(s+ib)} = \frac{s}{s^2+b^2}$ (对于 $\text{Re}(s) > 0$)
    4.  $\mathcal{L}\{\sin(bt)\} = \mathcal{L}\left\{\frac{e^{ibt} - e^{-ibt}}{2i}\right\} = \frac{1}{2i} \left( \frac{1}{s-ib} - \frac{1}{s+ib} \right) = \frac{1}{2i} \frac{s+ib - (s-ib)}{s^2+b^2} = \frac{b}{s^2+b^2}$ (对于 $\text{Re}(s) > 0$)

- **幻灯片 12**:
    5.  $\mathcal{L}\{t^n\}$ (n 为非负整数):
        $$
        \mathcal{L}\{t^n\} = \int_0^\infty t^n e^{-st} dt
        $$
        做替换 $\tau = st$, $d\tau = s dt$:
        $$
        = \int_0^\infty \left(\frac{\tau}{s}\right)^n e^{-\tau} \frac{d\tau}{s} = \frac{1}{s^{n+1}} \int_0^\infty \tau^n e^{-\tau} d\tau
        $$
        积分部分是 Gamma 函数 $\Gamma(n+1) = n!$。
        所以 $\mathcal{L}\{t^n\} = \frac{n!}{s^{n+1}}$ (对于 $\text{Re}(s) > 0$)。
        更一般地，对于 $r > -1$：
        $\mathcal{L}\{t^r\} = \frac{\Gamma(r+1)}{s^{r+1}}$ (对于 $\text{Re}(s) > 0$)
        例如 $\mathcal{L}\{t^{-1/2}\} = \mathcal{L}\{1/\sqrt{t}\} = \frac{\Gamma(1/2)}{s^{1/2}} = \frac{\sqrt{\pi}}{\sqrt{s}} = \sqrt{\frac{\pi}{s}}$。

- **幻灯片 13**:
    6.  $\mathcal{L}\{\lfloor t \rfloor\}$ (向下取整函数, "staircase" function):
        $\lfloor t \rfloor = n$ 当 $n \le t < n+1$。
        $$
        \mathcal{L}\{\lfloor t \rfloor\} = \sum_{n=0}^\infty \int_n^{n+1} n e^{-st} dt = \sum_{n=0}^\infty n \left[-\frac{1}{s}e^{-st}\right]_n^{n+1} \\
        = \sum_{n=0}^\infty \frac{n}{s} (e^{-sn} - e^{-s(n+1)}) = \frac{1}{s} \sum_{n=0}^\infty n e^{-sn} (1 - e^{-s})
        $$
        幻灯片中直接给出了结果（经过级数求和化简）：
        $$
        \mathcal{L}\{\lfloor t \rfloor\} = \frac{1}{s(e^s-1)} \quad (\text{for Re}(s)>0)
        $$


## 拉普拉斯变换的性质 (Properties of Laplace Transform)


- **收敛横坐标 (Abscissa of Convergence)**
    -   **绝对收敛横坐标 (Abscissa of Absolute Convergence) $\alpha$**: 使得 $\int_0^\infty |f(t)e^{-st}|dt$ 收敛的 $\text{Re}(s)$ 的下确界。积分在 $\text{Re}(s) > \alpha$ 时绝对收敛。
    -   **收敛横坐标 (Abscissa of Convergence) $\beta$**: 使得 $\int_0^\infty f(t)e^{-st}dt$ 收敛的 $\text{Re}(s)$ 的下确界。积分在 $\text{Re}(s) > \beta$ 时收敛。
    -   通常 $\beta \le \alpha$。如果 $f(t)$ 的精确指数阶为 $a_{exp}$，则 $\beta \le a_{exp} \le \alpha$。
    -   $F(s)$ 在 $\text{Re}(s) > \beta$ 的区域内解析。

- **线性性 (Linearity)**
    如果 $\mathcal{L}\{f_1(t)\}$ 在 $\text{Re}(s) > a_1$ 定义，$\mathcal{L}\{f_2(t)\}$ 在 $\text{Re}(s) > a_2$ 定义，则
    $$
    \mathcal{L}\{c_1 f_1(t) + c_2 f_2(t)\} = c_1 \mathcal{L}\{f_1(t)\} + c_2 \mathcal{L}\{f_2(t)\}
    $$
    定义域为 $\text{Re}(s) > \max\{a_1, a_2\}$。
    这个性质可以直接从积分的线性性得到。
    **应用**: 可以直接计算多项式的拉普拉斯变换，例如 $\mathcal{L}\{c_0 + c_1 t + \dots + c_d t^d\} = \frac{c_0}{s} + \frac{c_1}{s^2} + \dots + \frac{c_d d!}{s^{d+1}}$。

- **自变量的伸缩 (Dilations in the argument / Scaling)**
    如果 $F(s) = \mathcal{L}\{f(t)\}$，则对于 $r>0$：
    $$
    \mathcal{L}\{f(rt)\} = \frac{1}{r} F\left(\frac{s}{r}\right)
    $$
    **证明**: $\int_0^\infty f(rt)e^{-st}dt$。令 $\tau = rt$, $d\tau = r dt$。
    $= \int_0^\infty f(\tau) e^{-s(\tau/r)} \frac{d\tau}{r} = \frac{1}{r} \int_0^\infty f(\tau) e^{-(s/r)\tau} d\tau = \frac{1}{r} F\left(\frac{s}{r}\right)$。
    **例子**:
    $\mathcal{L}\{\cos(\omega t)\} = \frac{1}{\omega} \frac{s/\omega}{(s/\omega)^2+1} = \frac{s}{s^2+\omega^2}$ (已知 $\mathcal{L}\{\cos t\} = s/(s^2+1)$)。
    $\mathcal{L}\{\sin(\omega t)\} = \frac{1}{\omega} \frac{1}{(s/\omega)^2+1} = \frac{\omega}{s^2+\omega^2}$。
    求 $\mathcal{L}\{\cos^2 t\}$: 用倍角公式 $\cos^2 t = \frac{1+\cos(2t)}{2}$。
    $\mathcal{L}\{\cos^2 t\} = \frac{1}{2} (\mathcal{L}\{1\} + \mathcal{L}\{\cos(2t)\}) = \frac{1}{2} \left(\frac{1}{s} + \frac{s}{s^2+4}\right) = \frac{s^2+2}{s(s^2+4)}$。

- **自变量的平移 (Translations in the argument / Shifting Properties)**
    1.  **$t$ 域平移 ($s$ 域乘以指数)** ("Translations in the argument", 通常称为 **第二平移定理 (Second Shifting Theorem)** 或 $t$-shifting):
        定义单位阶跃函数 (unit step function) $u_c(t) = u(t-c)$:
        $$
        u_c(t) = \begin{cases} 0 & t < c \\ 1 & t \ge c \end{cases}
        $$
        如果 $F(s) = \mathcal{L}\{f(t)\}$，则对于 $c > 0$:
        $$
        \mathcal{L}\{u_c(t) f(t-c)\} = e^{-cs} F(s)
        $$
        **技术比喻**: $u_c(t)f(t-c)$ 的意思是将原函数 $f(t)$ 向右平移 $c$ 个单位，并且在 $t<c$ 的部分置零。这个操作在 $s$ 域对应于乘以一个指数衰减因子 $e^{-cs}$。
        **证明**: $\int_0^\infty u_c(t)f(t-c)e^{-st}dt = \int_c^\infty f(t-c)e^{-st}dt$。令 $\tau = t-c$, $d\tau = dt$。
        $= \int_0^\infty f(\tau)e^{-s(\tau+c)}d\tau = e^{-sc} \int_0^\infty f(\tau)e^{-s\tau}d\tau = e^{-sc}F(s)$。
        **例子**: $\mathcal{L}\{u_c(t)\} = e^{-cs}\mathcal{L}\{1\} = \frac{e^{-cs}}{s}$。

    2.  **$s$ 域平移 ($t$ 域乘以指数)** (通常称为 **第一平移定理 (First Shifting Theorem)** 或 $s$-shifting):
        如果 $F(s) = \mathcal{L}\{f(t)\}$，则对于任意复数 $c$:
        $$
        \mathcal{L}\{e^{ct} f(t)\} = F(s-c)
        $$
        **技术比喻**: 在 $t$ 域乘以一个指数函数 $e^{ct}$，在 $s$ 域对应于将 $F(s)$ 的自变量 $s$ 平移 $c$ 个单位。
        **例子**: $\mathcal{L}\{t^n e^{ct}\} = \frac{n!}{(s-c)^{n+1}}$ (已知 $\mathcal{L}\{t^n\} = n!/s^{n+1}$)。

- **拉普拉斯积分的逐项积分 (Term-wise Integration of Laplace Integrals)**
    如果一个函数 $f(t)$ 可以表示为收敛的幂级数 $f(t) = \sum_{n=0}^\infty \frac{a_n}{n!} t^n$ (即在 $t=0$ 解析)，并且其系数增长满足一定条件，那么它的拉普拉斯变换可以逐项进行：
    $$
    \mathcal{L}\{f(t)\} = \mathcal{L}\left\{\sum_{n=0}^\infty \frac{a_n}{n!} t^n\right\} = \sum_{n=0}^\infty \frac{a_n}{n!} \mathcal{L}\{t^n\} = \sum_{n=0}^\infty \frac{a_n}{n!} \frac{n!}{s^{n+1}} = \sum_{n=0}^\infty \frac{a_n}{s^{n+1}}
    $$
    **定理**: 若幂级数 $\sum a_n z^n$ 的收敛半径为 $R>0$，则对于 $f(t) = \sum_{n=0}^\infty \frac{a_n}{n!} t^n$ (对所有 $t \ge 0$ 有定义)，其拉普拉斯变换为 $\mathcal{L}\{f(t)\} = \sum_{n=0}^\infty \frac{a_n}{s^{n+1}}$，该级数对于 $\text{Re}(s) > 1/R$ 收敛。
    **例子 (Slide 26-27)**: 计算 $\mathcal{L}\left\{\frac{\sin t}{t}\right\}$。
    已知 $\sin t = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!} t^{2n+1}$。
    所以 $\frac{\sin t}{t} = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)!} t^{2n}$。(在 $t=0$ 处连续延拓 $f(0)=1$)
    这里 $a_{2n} = \frac{(-1)^n (2n)!}{(2n+1)!} = \frac{(-1)^n}{2n+1}$，奇数项系数为 $0$。
    $\mathcal{L}\left\{\frac{\sin t}{t}\right\} = \sum_{n=0}^\infty \frac{a_{2n}}{s^{2n+1}} = \sum_{n=0}^\infty \frac{(-1)^n}{(2n+1)s^{2n+1}} = \frac{1}{s} - \frac{1}{3s^3} + \frac{1}{5s^5} - \dots$
    这是 $\arctan(1/s)$ 的泰勒展开 (令 $x=1/s$)。所以 $\mathcal{L}\left\{\frac{\sin t}{t}\right\} = \arctan\left(\frac{1}{s}\right)$ (或 $\text{arccot}(s)$)。

- **拉普拉斯变换与微分 (Laplace Transform and Differentiation)**
    1.  **$s$ 域微分 (Differentiation in the Codomain)**:
        $$
        F'(s) = -\mathcal{L}\{t f(t)\} \quad \text{or} \quad \mathcal{L}\{t f(t)\} = -F'(s)
        $$
        **例子**: 推导 $\mathcal{L}\{t^k e^{ct}\}$。已知 $\mathcal{L}\{e^{ct}\} = \frac{1}{s-c}$。
        $\mathcal{L}\{t e^{ct}\} = -\frac{d}{ds}\left(\frac{1}{s-c}\right) = \frac{1}{(s-c)^2}$。
        $\mathcal{L}\{t^2 e^{ct}\} = -\frac{d}{ds}\left(\frac{1}{(s-c)^2}\right) = \frac{2}{(s-c)^3}$。
        依此类推 $\mathcal{L}\{t^k e^{ct}\} = \frac{k!}{(s-c)^{k+1}}$。

    2.  **$t$ 域微分 (Differentiation in the Domain)**: 这是将拉普拉斯变换应用于求解微分方程的核心。
        **定理**: 假设 $f(t)$ 连续且 $f'(t)$ 分段连续，且 $\mathcal{L}\{f(t)\} = F(s)$ 在 $\text{Re}(s) > a$ 定义。则：
        $$
        \mathcal{L}\{f'(t)\} = sF(s) - f(0) \quad (\text{for Re}(s) > a)
        $$
        如果 $f(0)$ 不连续，用 $f(0^+)$ 代替。
        **证明思路**: 分部积分 $\int_0^\infty f'(t)e^{-st}dt = [f(t)e^{-st}]_0^\infty - \int_0^\infty f(t)(-s e^{-st})dt = (0 - f(0)) + s \int_0^\infty f(t)e^{-st}dt = sF(s) - f(0)$。
        这里需要 $f(t)e^{-st} \to 0$ 当 $t \to \infty$，这由 $f(t)$ 的指数阶和 $\text{Re}(s)>a$ 保证。

        **推论 (Corollary)**: 对于高阶导数 (假设 $f, f', \dots, f^{(n-1)}$ 连续，$f^{(n)}$ 分段连续)：
        $$
        \mathcal{L}\{f^{(n)}(t)\} = s^n F(s) - s^{n-1}f(0) - s^{n-2}f'(0) - \dots - f^{(n-1)}(0)
        $$
        $t$ 域的微分运算在 $s$ 域对应于乘以 $s$ 并减去初始条件相关的项。这正是它能将微分方程转化为代数方程的魔力所在。

- **拉普拉斯变换与积分 (Laplace Transform and Integration)**
    1.  **$t$ 域积分 (Integration in the Domain)**:
        如果 $F(s) = \mathcal{L}\{f(t)\}$，则
        $$
        \mathcal{L}\left\{\int_0^t f(\tau) d\tau\right\} = \frac{F(s)}{s} \quad (\text{for Re}(s) > \max\{a,0\})
        $$
        **证明思路**: 令 $g(t) = \int_0^t f(\tau)d\tau$。则 $g'(t)=f(t)$ 且 $g(0)=0$。
        $\mathcal{L}\{g'(t)\} = s\mathcal{L}\{g(t)\} - g(0) \Rightarrow \mathcal{L}\{f(t)\} = s\mathcal{L}\{g(t)\} \Rightarrow F(s) = s \mathcal{L}\{g(t)\}$。
        所以 $\mathcal{L}\{g(t)\} = F(s)/s$。

	 2. **$s$ 域积分 (Integration in the Codomain)**
    如果 $\mathcal{L}\{f(t)\} = F(s)$ 且 $\lim_{t\to 0^+} \frac{f(t)}{t}$ 存在 (或更一般地，$\int_0^1 \frac{f(t)}{t}dt$ 存在)，则：
    $$
    \mathcal{L}\left\{\frac{f(t)}{t}\right\} = \int_s^\infty F(\sigma) d\sigma \quad (\text{for Re}(s) > a)
    $$
    **例子**: 已知 $\mathcal{L}\{\sin t\} = \frac{1}{s^2+1}$。
    $\mathcal{L}\left\{\frac{\sin t}{t}\right\} = \int_s^\infty \frac{1}{\sigma^2+1} d\sigma = [\arctan \sigma]_s^\infty = \frac{\pi}{2} - \arctan s = \text{arccot } s$ (与之前逐项积分结果一致)。
    再用 $t$ 域积分性质：$\mathcal{L}\left\{\int_0^t \frac{\sin \tau}{\tau} d\tau\right\} = \frac{\text{arccot } s}{s}$。
    $\int_0^t \frac{\sin \tau}{\tau} d\tau$ 被称为**正弦积分 (Sine Integral)** $\text{Si}(t)$。

- **拉普拉斯变换与卷积 (Laplace Transform and Convolution)**
    **卷积定义**: 两个函数 $f(t)$ 和 $g(t)$ (定义在 $t \ge 0$) 的卷积 $(f*g)(t)$ 定义为：
    $$
    (f*g)(t) = \int_0^t f(\tau) g(t-\tau) d\tau
    $$
    **卷积定理 (Convolution Theorem)**:
    如果 $\mathcal{L}\{f(t)\} = F(s)$ 且 $\mathcal{L}\{g(t)\} = G(s)$，则：
    $$
    \mathcal{L}\{(f*g)(t)\} = F(s)G(s)
    $$
    即，$t$ 域的卷积对应于 $s$ 域的普通乘积。
    **证明思路 (Slide 38, 40-41)**: 从 $F(s)G(s)$ 的定义出发，将其写成二重积分，然后通过变量替换（令 $u = t_1+\tau, v=t_1$ 或类似的）和交换积分次序 (需要 Fubini 定理保证) 得到 $\mathcal{L}\{(f*g)(t)\}$ 的形式。
    **应用 (Slide 42)**: 求 $\mathcal{L}^{-1}\left\{\frac{s}{(s^2+1)^2}\right\}$。
    $\frac{s}{(s^2+1)^2} = \frac{s}{s^2+1} \cdot \frac{1}{s^2+1}$。
    已知 $\mathcal{L}\{\cos t\} = \frac{s}{s^2+1}$ 且 $\mathcal{L}\{\sin t\} = \frac{1}{s^2+1}$。
    所以 $\mathcal{L}^{-1}\left\{\frac{s}{(s^2+1)^2}\right\} = (\cos t) * (\sin t) = \int_0^t \cos \tau \sin(t-\tau) d\tau$。
    通过三角恒等式计算积分得到 $\frac{1}{2} t \sin t$。
    所以 $\mathcal{L}\left\{\frac{1}{2} t \sin t\right\} = \frac{s}{(s^2+1)^2}$。

### 拉普拉斯逆变换 (Inversion of the Laplace Transform)

- **唯一性 (Uniqueness)**:
    如果两个分段连续函数 $f_1(t)$ 和 $f_2(t)$ 具有相同的拉普拉斯变换 $F(s)$，那么它们在所有连续点上是相等的。也就是说，拉普拉斯逆变换 $\mathcal{L}^{-1}\{F(s)\}$ **(在连续点上) 是唯一的**。
    更准确地说，如果 $F_1(s)=F_2(s)$ 在某个右半平面成立，并且满足一定条件，则 $f_1(t^-)=f_2(t^-)$ 且 $f_1(t^+)=f_2(t^+)$。如果 $f_1, f_2$ 连续，则 $f_1=f_2$。
- **逆变换公式（不考）**:
    存在一个明确的逆变换公式，称为**Bromwich 积分**或 Mellin 逆变换公式，它涉及到复平面上的路径积分：
    $$
    f(t) = \frac{1}{2\pi i} \lim_{T\to\infty} \int_{\gamma-iT}^{\gamma+iT} e^{st} F(s) ds
    $$
    其中 $\gamma$ 是一个实数，使得积分路径在 $F(s)$ 的所有奇点右侧。这个公式在实际计算中通常与留数定理结合使用，超出了本课程的基础范围。
    在实践中，我们通常通过查表和利用拉普拉斯变换的性质来求逆变换。

## 用拉普拉斯变换求解初值问题 (IVP)
### Basic Idea
这是拉普拉斯变换在微分方程中的核心应用。

**核心变换方程**
$$
\mathcal{L}\{f^{(n)}(t)\} = s^n F(s) - s^{n-1}f(0) - s^{n-2}f'(0) - \dots - f^{(n-1)}(0)
$$

- **基本思想**:
    对于一个常系数线性微分方程的初值问题，例如二阶：
    $ay'' + by' + cy = f(t)$,  $y(0)=y_0$, $y'(0)=y_1$
    求解步骤：
    1.  **变换方程**: 对整个微分方程两边取拉普拉斯变换。利用微分性质 $\mathcal{L}\{y'(t)\} = sY(s) - y(0)$ 和 $\mathcal{L}\{y''(t)\} = s^2Y(s) - sy(0) - y'(0)$ (其中 $Y(s) = \mathcal{L}\{y(t)\}$), 以及右端项 $f(t)$ 的变换 $F_s(s)=\mathcal{L}\{f(t)\}$。这将把微分方程转换成一个关于 $Y(s)$ 的**代数方程**。
    2.  **求解 $Y(s)$**: 从代数方程中解出 $Y(s)$。
    3.  **逆变换**: 对 $Y(s)$ 进行拉普拉斯逆变换得到原函数 $y(t) = \mathcal{L}^{-1}\{Y(s)\}$。这通常需要部分分式分解 (partial fraction decomposition) 和查表。

- **例子**: $y' + 2y = -1$, $y(0)=1$
    1.  $\mathcal{L}\{y'\} + 2\mathcal{L}\{y\} = \mathcal{L}\{-1\}$
        $(sY(s) - y(0)) + 2Y(s) = -1/s$
        $sY(s) - 1 + 2Y(s) = -1/s$
    2.  $(s+2)Y(s) = 1 - 1/s = (s-1)/s$
        $Y(s) = \frac{s-1}{s(s+2)}$
    3.  部分分式: $\frac{s-1}{s(s+2)} = \frac{A}{s} + \frac{B}{s+2}$。解得 $A = -1/2, B = 3/2$。
        $Y(s) = -\frac{1}{2s} + \frac{3}{2(s+2)}$
        $y(t) = \mathcal{L}^{-1}\left\{-\frac{1}{2s}\right\} + \mathcal{L}^{-1}\left\{\frac{3}{2(s+2)}\right\} = -\frac{1}{2} \cdot 1 + \frac{3}{2} e^{-2t} = -\frac{1}{2} + \frac{3}{2}e^{-2t}$

- **例子**: $y'' + y = \sin(\omega t)$, $y(0)=1, y'(0)=1$
    1.  $\mathcal{L}\{y''\} + \mathcal{L}\{y\} = \mathcal{L}\{\sin(\omega t)\}$
        $(s^2Y(s) - sy(0) - y'(0)) + Y(s) = \frac{\omega}{s^2+\omega^2}$
        $s^2Y(s) - s - 1 + Y(s) = \frac{\omega}{s^2+\omega^2}$
    2.  $(s^2+1)Y(s) = s+1 + \frac{\omega}{s^2+\omega^2}$
        $Y(s) = \frac{s+1}{s^2+1} + \frac{\omega}{(s^2+1)(s^2+\omega^2)}$
    3.  **Case $\omega \neq \pm 1$**:
        $\frac{\omega}{(s^2+1)(s^2+\omega^2)} = \frac{A s+B}{s^2+1} + \frac{C s+D}{s^2+\omega^2}$。
        幻灯片直接给出分解结果（或通过特定技巧）：
        $\frac{\omega}{(s^2+1)(s^2+\omega^2)} = \frac{\omega}{\omega^2-1} \left(\frac{1}{s^2+1} - \frac{1}{s^2+\omega^2}\right)$。
        $Y(s) = \frac{s}{s^2+1} + \frac{1}{s^2+1} + \frac{\omega}{\omega^2-1}\frac{1}{s^2+1} - \frac{\omega}{\omega^2-1}\frac{1}{s^2+\omega^2}$
        $Y(s) = \frac{s}{s^2+1} + \left(1+\frac{\omega}{\omega^2-1}\right)\frac{1}{s^2+1} - \frac{1}{\omega^2-1}\frac{\omega}{s^2+\omega^2}$
        $Y(s) = \frac{s}{s^2+1} + \frac{\omega^2+\omega-1}{\omega^2-1}\frac{1}{s^2+1} - \frac{1}{\omega^2-1}\frac{\omega}{s^2+\omega^2}$
        $y(t) = \cos t + \frac{\omega^2+\omega-1}{\omega^2-1} \sin t - \frac{1}{\omega^2-1} \sin(\omega t)$ 

    4.  **Case $\omega = \pm 1$**: (共振情况)
        如果 $\omega=1$, $Y(s) = \frac{s+1}{s^2+1} + \frac{1}{(s^2+1)^2}$。
        $\mathcal{L}^{-1}\left\{\frac{s+1}{s^2+1}\right\} = \cos t + \sin t$。
        需要求 $\mathcal{L}^{-1}\left\{\frac{1}{(s^2+1)^2}\right\}$。

### Continuous Forcing & Discontinuous Forcing 


我们考虑一个典型的**二阶常系数线性微分方程**：
$$
ay'' + by' + cy = f(t)
$$
其中 $a, b, c$ 是常数，$a \neq 0$，而 $f(t)$ 就是所谓的**强迫项 (forcing function)** 或输入函数。

#### 1. 连续强迫项 (Continuous Forcing) 

##### 定义与含义
当强迫项 $f(t)$ 在所考虑的时间区间（通常是 $t \ge 0$）上是一个**连续函数**时，我们称之为连续强迫。这意味着 $f(t)$ 的图像没有断裂或跳跃。

**例子**:
-   $f(t) = -1$ (常数函数，Slide 47)
-   $f(t) = \sin(\omega t)$ (正弦函数，Slide 48)
-   $f(t) = e^{kt}$ (指数函数)
-   $f(t) = t^2$ (多项式函数)
-   Slide 62 中的分段函数，虽然是分段定义的，但它在连接点 $t=1$ 处是连续的 ($t=1$ 时 $f(1)=1$；$2-t$ 在 $t=1$ 时 $f(1)=1$)，所以它仍然是一个连续强迫项。

##### 对解的影响和处理方法

1.  **解的存在唯一性 (Slide 51)**:
    如果 $f(t)$ 是连续的，那么根据常微分方程的**存在唯一性定理 (Existence and Uniqueness Theorem)** (对于线性方程有更强的结论)，对于给定的初始条件 $y(0)=y_0, y'(0)=y_1$，微分方程在 $t \ge 0$ 上**存在唯一的解 $y(t)$**。这个解 $y(t)$ 本身以及它的导数 $y'(t)$ 和二阶导数 $y''(t)$ 都会是**连续的**。

2.  **求解方法**:
    -   **待定系数法 (Method of Undetermined Coefficients)**: 如果 $f(t)$ 是特定形式的函数（如多项式、指数函数、正弦/余弦函数及其乘积和线性组合），此方法适用。
    -   **参数变易法 (Variation of Parameters)**: 这是一个更通用的方法，适用于任何连续的 $f(t)$。
    -   **拉普拉斯变换法 (Laplace Transform Method)**: 这种方法对于连续强迫项同样有效。

3.  **解的性质 (Slide 52Theorem)**:
    如果 $f(t)$ 是连续且指数阶的，那么任何解 $y(t)$ 也是连续且指数阶的。这意味着解 $y(t)$ 的拉普拉斯变换 $Y(s)$ 存在于某个右半平面。


#### 2. 不连续强迫项 (Discontinuous Forcing) (Slides 53-61, 64-70)

##### 定义与含义
当强迫项 $f(t)$ 在所考虑的时间区间上**不是处处连续**时，我们称之为不连续强迫。最常见的不连续类型是**跳跃间断点 (jump discontinuities)**。这意味着 $f(t)$ 的图像在某些点会发生突然的跳跃。

**例子**:
-   **阶梯函数/矩形脉冲 (Slide 53, 57-59)**:
    $f(t) = \begin{cases} 1 & 0 < t < 1 \\ 0 & t > 1 \end{cases}$
    这个函数在 $t=1$ 处有一个跳跃间断点。
-   **一系列矩形脉冲 (Slide 60-61)**:
    $f(t) = 1$ for $t \in [0,1] \cup [2,3] \cup [4,5]$, and $0$ otherwise.
    这个函数在 $t=1, 2, 3, 4, 5$ 都有跳跃间断点。
-   **脉冲函数 (Impulsive Forcing - 狄拉克 $\delta$ 函数, Slides 64-70)**:
    狄拉克 $\delta$ 函数是一种理想化的不连续强迫，它在单个点上施加一个“无穷大”的力，但在极短的时间内完成，使得总冲量为有限值 (通常为1)。这是一种极端的不连续。

##### 对解的影响和处理方法

![22a51e6adf17297be74a1a87db580da.png](https://s2.loli.net/2025/05/15/WgBAqPotsQ7GD4u.png)



1.  **解的定义调整 (Slide 53 Definition)**:
    当 $f(t)$ 不连续时，$y''(t)$ 通常在 $f(t)$ 的不连续点处**不存在** (因为 $y''(t) = (f(t) - by' - cy)/a$，如果 $f(t)$ 跳跃，$y', y$ 连续，则 $y''$ 也会跳跃，从而导致 $y''$ 不存在)。
    因此，我们需要调整对“解”的定义：
    -   一个函数 $y(t)$ 称为 IVP 的解，如果：
        1.  $y(t)$ 是 **$C^1$ 函数**，即 $y(t)$ 和 $y'(t)$ 都是连续的。**这是非常重要的一点！即使强迫项不连续，解本身和它的一阶导数通常仍然保持连续性。** 这源于物理系统的惯性，例如一个物体的位置和速度不会因为受到的力突然改变而瞬间跳变。
        2.  $y''(t)$ 存在于 $f(t)$ **连续的那些点**，并且在这些点上满足微分方程 $ay'' + by' + cy = f(t)$。
        3.  $y(t)$ 满足初始条件 $y(0)=y_0, y'(0)=y_1$。

2.  **解的存在唯一性 (Slide 55 Theorem)**:
    -   如果 $f(t)$ 是**分段连续**的，则 IVP 仍然具有**唯一的解** (在上述调整的定义下)。
    -   这个唯一的解可以通过以下方式构造：在 $f(t)$ 的每个连续区间内分别求解 ODE，并利用 $y(t)$ 和 $y'(t)$ 的连续性在间断点处“粘合”这些解段。

3.  **求解方法**:
    -   **拉普拉斯变换法 (Laplace Transform Method)**: 这是处理不连续强迫项**非常强大和方便**的方法。利用单位阶跃函数与拉普拉斯变换的平移性质与线性，我们可以轻松解决非连续的情况
        -   关键在于能够将分段定义的 $f(t)$ 用**单位阶跃函数 $u_c(t)$** 表示出来。
            例如，$f(t) = \begin{cases} g_1(t) & 0 \le t < c \\ g_2(t) & t \ge c \end{cases}$ 可以写成 $f(t) = g_1(t) + u_c(t)(g_2(t) - g_1(t))$ (如果 $g_1(t)$ 在 $t \ge c$ 也有定义且我们想在 $t \ge c$ 时完全替换为 $g_2(t)$)，或者更常见的是用 $f(t) = g_1(t)[u_0(t)-u_c(t)] + g_2(t)u_c(t)$ 这样的形式。
            对于矩形脉冲 $f(t) = 1$ for $a \le t < b$ and $0$ 否则，可以表示为 $f(t) = u_a(t) - u_b(t)$。
        -   一旦 $f(t)$ 用单位阶跃函数表示，就可以利用拉普拉斯变换的**第二平移定理** ($\mathcal{L}\{u_c(t)g(t-c)\} = e^{-cs}G(s)$) 来求 $\mathcal{L}\{f(t)\}$。
        -   后续步骤与连续强迫项类似：解出 $Y(s)$，然后进行逆变换。逆变换时也可能需要用到第二平移定理。

4.  **解的性质**:
    -   $y(t)$ 和 $y'(t)$ 是连续的。
    -   $y''(t)$ 在 $f(t)$ 的不连续点处通常也是不连续的（发生跳跃）。这意味着解的“平滑度”降低了，但不会像 $f(t)$ 那样完全断开。
    -   **例子 (Slide 59 图像)**:
        -   强迫项 $f(t)$ (虚线) 在 $t=1$ 处从 $1$ 跳到 $0$。
        -   解 $y(t)$ (红色曲线) 在 $t=1$ 处是连续的，并且其斜率 $y'(t)$ (蓝色曲线) 在 $t=1$ 处也是连续的。
        -   但是，如果观察 $y'(t)$ 的斜率 (即 $y''(t)$)，你会发现在 $t=1$ 处，$y'(t)$ 的变化趋势有一个急剧的转折，这意味着 $y''(t)$ 在那里不连续。
        -   在 $0 < t < 1$ 区间，ODE 是 $y''+y=1$。在 $t>1$ 区间，ODE 是 $y''+y=0$。解在这两个区间内分别满足对应的方程。


**例题**
- 注意如何将时域与频域的平移相互对应
- 注意如何将分段函数利用 $u(t)$ 进行转化
![a163bc0adc7a7655c38752d54e22f8e.png](https://s2.loli.net/2025/05/15/6jP5A4RMZgGdbiW.png)
![401843fc9fa14f7cbd7314d73e2b768.png](https://s2.loli.net/2025/05/15/MxmSYlyZVdhH9Ur.png)

##### 针对脉冲强迫 (Impulsive Forcing - Dirac $\delta$ Function)
**脉冲强迫的核心性质**
$$
\begin{align}
& \mathcal{L}(\delta(t)) = 1 \\
& \int_{-\infty}^{\infty}  \delta(t) dt =1 \\
& \int_{-\infty}^{\infty}  f(t) \delta(t-t_{0}) dt = \frac{f(t_{0}-)+f(t_{0}+)}{2}   \\
& \mathcal{L}( \delta(t-t_{0})) = e^{-st_{0}} \\
& u'(t) = \delta(t)
\end{align}
$$


这是不连续强迫的一种极端情况。

-   **影响**: 当强迫项是 $\delta(t-t_0)$ 时，它在 $t=t_0$ 时刻给系统一个瞬时冲量。
    -   解 $y(t)$ 在 $t=t_0$ 处仍然是**连续的**。
    -   但是，解的一阶导数 $y'(t)$ 在 $t=t_0$ 处会发生一个**跳跃**。跳跃的幅度与 $\delta$ 函数的系数和 $y''$ 项的系数有关。
        例如，对于 $ay''+by'+cy = k\delta(t-t_0)$，如果 $y(t_0^-)$ 和 $y'(t_0^-)$ 是 $t_0$ 之前的状态，则 $y(t_0^+) = y(t_0^-)$，但 $y'(t_0^+) - y'(t_0^-) = k/a$。
    -   $y''(t)$ 则会包含一个 $\delta$ 函数项。

-   **求解**: 拉普拉斯变换是处理 $\delta$ 函数强迫项的标准且有效的方法，因为 $\mathcal{L}\{\delta(t-t_0)\} = e^{-st_0}$ 形式简单。



- **卷积的应用 (Slide 71: The use of the convolution)**
    对于 $a Y'' + b Y' + c Y = F_s(s)$ (假设初始条件为0，得到特解 $Y_p(s)$)，
    $Y_p(s) = \frac{1}{as^2+bs+c} F_s(s) = H(s)F_s(s)$。
    $H(s) = \frac{1}{as^2+bs+c}$ 称为系统的**传递函数 (transfer function)**。
    $h(t) = \mathcal{L}^{-1}\{H(s)\}$ 称为系统的**脉冲响应 (impulse response)**，即当输入为 $\delta(t)$ (单位脉冲) 时的输出。
    根据卷积定理，$y_p(t) = (h*f)(t) = \int_0^t h(t-\tau)f(\tau)d\tau$。
    **即，系统的零状态响应是脉冲响应与输入信号的卷积。**
