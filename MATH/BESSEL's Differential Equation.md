---
title: BESSEL's Differential Equation
date: 2025-05-15
date modified: 2025-05-15
categories: Math285
tags:
  - Math285
---

#Math285 


## 贝塞尔微分方程概述 (Overview of Bessel's Differential Equation)

### 贝塞尔方程的定义
这里给出了贝塞尔微分方程的标准形式：
$$
x^2 y'' + xy' + (x^2 - \nu^2)y = 0, \quad x > 0
$$
其中：
- $y''$ 是 $y$ 对 $x$ 的二阶导数， $y'$ 是一阶导数。
- $\nu$ 是一个非负实数参数，称为贝塞尔方程的**阶 (order)**。
- 当 $\nu \in \mathbb{Z}$ (整数) 时，方程的解被称为$\nu$ 阶柱函数 (cylinder functions of order $\nu$)**。

为了使用**弗罗贝尼乌斯方法 (Frobenius Method)** 求解，我们将方程改写为标准形式 $y'' + P(x)y' + Q(x)y = 0$：
$$
y'' + \frac{1}{x} y' + \left(1 - \frac{\nu^2}{x^2}\right) y = 0
$$
这里 $P(x) = \frac{1}{x}$，$Q(x) = 1 - \frac{\nu^2}{x^2}$。
可以看出 $x_0 = 0$ 是一个**正则奇点 (regular singular point)**，因为 $xP(x) = 1$ 和 $x^2 Q(x) = x^2 - \nu^2$ 在 $x_0=0$ 点解析。
根据弗罗贝尼乌斯理论：
- $p_0 = \lim_{x\to0} xP(x) = 1$
- $q_0 = \lim_{x\to0} x^2Q(x) = -\nu^2$

对应的**指标方程 (indicial equation)** 为：
$$
r(r-1) + p_0 r + q_0 = 0
$$
代入 $p_0=1, q_0=-\nu^2$：
$$
\begin{align}
& r(r-1) + 1 \cdot r - \nu^2 = 0 \\
& r^2 - r + r - \nu^2 = 0 \\
& r^2 - \nu^2 = 0
\end{align}
$$
所以指标方程的根 (exponents at the singularity) 是 $r_1 = \nu$ 和 $r_2 = -\nu$。

幻灯片提到了根据 $\nu$ 的值，我们会落入弗罗贝尼乌斯定理的不同情况：
- **Case 1**: $r_1 - r_2 = 2\nu$ 不是整数。 (对应 $\nu \notin \{0, \frac{1}{2}, 1, \frac{3}{2}, 2, \dots\}$)
- **Case 3**: $r_1 = r_2$。 (对应 $\nu = 0$，此时 $r_1=r_2=0$)
- **Case 4**: $r_1 - r_2 = N$ 是一个正整数。 (对应 $\nu \in \{\frac{1}{2}, 1, \frac{3}{2}, 2, \dots\}$，此时 $N=2\nu$)

### 求解过程 - 第一类贝塞尔函数 (Slides 5-6: Solving Process - Bessel Function of the First Kind)

我们尝试一个弗罗贝尼乌斯级数解 (series solution) 的形式，对应较大的根 $r_1 = \nu$:
$$
y(x) = x^\nu \sum_{n=0}^\infty a_n x^n = \sum_{n=0}^\infty a_n x^{n+\nu} \quad (a_0 \neq 0)
$$
将这个级数代入贝塞尔方程 $x^2 y'' + xy' + (x^2 - \nu^2)y = 0$。
关键步骤：
1.  **计算导数**:
    $y' = \sum_{n=0}^\infty (n+\nu) a_n x^{n+\nu-1}$
    $y'' = \sum_{n=0}^\infty (n+\nu)(n+\nu-1) a_n x^{n+\nu-2}$
2.  **代入方程**:
    $x^2 y'' = \sum (n+\nu)(n+\nu-1) a_n x^{n+\nu}$
    $x y' = \sum (n+\nu) a_n x^{n+\nu}$
    $x^2 y = \sum a_n x^{n+\nu+2} = \sum a_{n-2} x^{n+\nu}$ (调整了下标以便合并)
    $-\nu^2 y = \sum -\nu^2 a_n x^{n+\nu}$
3.  **合并级数**:
    $L[y] = \sum_{n=0}^\infty [(n+\nu)(n+\nu-1) + (n+\nu) - \nu^2] a_n x^{n+\nu} + \sum_{n=2}^\infty a_{n-2} x^{n+\nu} = 0$
    方括号中的项可以化简：
    $(n+\nu)^2 - (n+\nu) + (n+\nu) - \nu^2 = (n+\nu)^2 - \nu^2 = n^2 + 2n\nu + \nu^2 - \nu^2 = n(n+2\nu)$
    所以：
    $L[y] = \sum_{n=0}^\infty n(n+2\nu) a_n x^{n+\nu} + \sum_{n=2}^\infty a_{n-2} x^{n+\nu} = 0$
4.  **写出各项系数**:
    - $n=0$: $0(0+2\nu)a_0 x^\nu = 0$。因为 $a_0 \neq 0$，这一项总是成立，这与指标方程 $r^2-\nu^2=0$ 当 $r=\nu$ 时一致。
    - $n=1$: $1(1+2\nu)a_1 x^{1+\nu} = 0$。因为 $1+2\nu \ge 1$ (由于 $\nu \ge 0$)，所以必须有 $a_1 = 0$。
    - $n \ge 2$: $n(n+2\nu)a_n + a_{n-2} = 0$。这给出了**递推关系 (recurrence relation)**:
      $$
      a_n = -\frac{a_{n-2}}{n(n+2\nu)}, \quad \text{for } n \ge 2
      $$

由于 $a_1 = 0$，所有奇数项系数 $a_3, a_5, \dots$ 均为 0。我们只需要考虑偶数项系数 $a_{2m}$。
令 $n=2m$ ($m \ge 1$):
$$
a_{2m} = -\frac{a_{2m-2}}{2m(2m+2\nu)} = -\frac{a_{2m-2}}{4m(m+\nu)}
$$
由此可以得到 $a_{2m}$ 的通项 (Slide 5 末尾)：
$$
a_{2m} = \frac{(-1)^m a_0}{2^{2m} m! (\nu+1)(\nu+2)\dots(\nu+m)}
$$
这里，$(\nu+1)(\nu+2)\dots(\nu+m)$ 的表达有点像阶乘。

**归一化 (Normalization) 和 $J_\nu(x)$ **

- **第一种归一化**: 若选择 $a_0=1$，我们得到一个解 $y_1(x)$：
  $$
  y_1(x) = x^\nu \sum_{m=0}^\infty \frac{(-1)^m}{m! 2^{2m}(\nu+1)(\nu+2)\cdots(\nu+m)} x^{2m}
  $$
- **标准归一化 (引入 Gamma 函数)**: 为了得到更简洁和通用的形式，特别是对于非整数 $\nu$，我们使用**Gamma 函数 (Gamma function)** $\Gamma(z)$。
  回顾一下 Gamma 函数的性质：$\Gamma(z+1) = z\Gamma(z)$，且对于正整数 $k$，$\Gamma(k+1) = k!$。
  我们可以将 $(\nu+1)(\nu+2)\cdots(\nu+m)$ 表示为 $\frac{\Gamma(\nu+m+1)}{\Gamma(\nu+1)}$。
  标准的 $a_0$ 选择是 $a_0 = \frac{1}{2^\nu \Gamma(\nu+1)}$。
  这样做是为了让 $J_\nu(x)$ 有一个特定的形式。当 $\nu$ 是非负整数时，$\Gamma(\nu+1) = \nu!$，所以 $a_0 = \frac{1}{2^\nu \nu!}$。
  代入 $a_{2m}$ 的表达式：
  $$
  a_{2m} = \frac{(-1)^m}{2^{2m} m! (\nu+1)\dots(\nu+m)} \cdot \frac{1}{2^\nu \Gamma(\nu+1)} \\
  = \frac{(-1)^m}{m! 2^{2m+\nu} \Gamma(\nu+m+1)}
  $$
  因此，**第一类 $\nu$ 阶贝塞尔函数 (Bessel function of the first kind of order $\nu$)** $J_\nu(x)$ 定义为：

$$
  J_\nu(x) = \sum_{m=0}^\infty \frac{(-1)^m}{m! \Gamma(\nu+m+1)} \left(\frac{x}{2}\right)^{2m+\nu}
$$
  这个级数对于所有 $x \in (0, \infty)$ 收敛。如果 $\nu \ge 0$，它在 $x=0$ 处也是有定义的。

### 不同 $\nu$ 值的讨论 (Discussion for Different Values of $\nu$)

#### Case $\nu \notin \mathbb{Z}$ (Slides 9-10: $\nu$ is not an integer)
- 指标方程的根是 $r_1 = \nu$ 和 $r_2 = -\nu$。
- 它们之差 $r_1 - r_2 = 2\nu$。如果 $2\nu$ 不是一个整数，那么根据弗罗贝尼乌斯定理，我们可以得到两个线性无关的解：
  $y_1(x) = J_\nu(x)$ (由 $r_1 = \nu$ 得到)
  $y_2(x) = J_{-\nu}(x)$ (由 $r_2 = -\nu$ 得到，通过将定义中的 $\nu$ 替换为 $-\nu$)
  $$
  J_{-\nu}(x) = \sum_{m=0}^\infty \frac{(-1)^m}{m! \Gamma(-\nu+m+1)} \left(\frac{x}{2}\right)^{2m-\nu}
  $$
  当 $\nu$ 不是整数时，$J_\nu(x)$ 和 $J_{-\nu}(x)$ 是线性无关的，它们构成了贝塞尔方程的**基本解系 (fundamental system of solutions)**。

- **幻灯片 10 的 Remark**: 即使 $2\nu$ 是一个非零整数 (例如 $\nu = 1/2, 3/2, \dots$)，但 $\nu$ 本身不是整数，我们仍然发现 $J_\nu(x)$ 和 $J_{-\nu}(x)$ 是线性无关的。**这属于弗罗贝尼乌斯定理的 Case 4，但公式简化得像 Case 1，没有出现对数项**。
  - 解释 (Explanation): 幻灯片指出，在这种情况下 ($N=2\nu$ 是奇数)，第二解的对数项系数 $a = \lim_{r\to r_2} (r-r_2) a_N(r)$ 为零，并且系数 $a_n(r)$ 在 $r_2 = -\nu$ 处是解析的。因此，第二解的形式与 Case 1 相同。

#### Case $\nu = 0$ (Slides 11-15: Order Zero)
- 指标方程的根是 $r_1 = r_2 = 0$。这属于弗罗贝尼乌斯定理的 Case 3。
- 第一个解是 $J_0(x)$:
  $$
  J_0(x) = \sum_{m=0}^\infty \frac{(-1)^m}{(m!)^2} \left(\frac{x}{2}\right)^{2m} = 1 - \frac{x^2}{4} + \frac{x^4}{64} - \dots
  $$
  $J_0(x)$ 在 $x=0$ 处是解析的，并且满足 $J_0(0)=1, J_0'(0)=0$ (如 Slide 11 Note 所示)。
- 第二个解 $y_2(x)$ 将包含一个对数项，形式为 (Slide 12):
  $$
  y_2(x) = J_0(x) \ln x + \sum_{n=1}^\infty b_n x^n
  $$
  其中 $b_n = a_n'(0)$ (这里 $a_n(r)$ 是弗罗贝尼乌斯方法中更一般的系数形式)。
  幻灯片 12-13 详细推导了 $a_{2m}'(0)$：
  - $a_{2m+1}(r)=0$ (奇数项为零)。
  - $a_{2m}(r) = \frac{(-1)^m}{(r+2)^2(r+4)^2\dots(r+2m)^2}$ (这里是 $a_0(r)=1$ 的情况)。
  - 使用**对数导数 (logarithmic derivative)** $\text{ld}(f) = f'/f$。
    $\text{ld}(a_{2m}(r)) = \text{ld}((-1)^m) - 2\sum_{k=1}^m \text{ld}(r+2k) = 0 - 2\sum_{k=1}^m \frac{1}{r+2k}$
  - 所以 $a_{2m}'(r) = a_{2m}(r) \left( -2\sum_{k=1}^m \frac{1}{r+2k} \right)$。
  - 当 $r=0$ 时，$a_{2m}'(0) = a_{2m}(0) \left( -2\sum_{k=1}^m \frac{1}{2k} \right) = a_{2m}(0) \left( -\sum_{k=1}^m \frac{1}{k} \right) = -\frac{(-1)^m}{(2^m m!)^2} H_m$。
    其中 $a_{2m}(0) = \frac{(-1)^m}{(2^m m!)^2}$，$H_m = 1 + \frac{1}{2} + \dots + \frac{1}{m}$ 是**调和数 (harmonic number)**。
  - 所以 $b_{2m} = a_{2m}'(0) = \frac{(-1)^{m+1} H_m}{2^{2m}(m!)^2}$。
  - 于是第二个解的一个形式是 (Slide 13):
    $$
    y_2(x) = J_0(x) \ln x + \sum_{m=1}^\infty \frac{(-1)^{m+1}H_m}{(m!)^2} \left(\frac{x}{2}\right)^{2m}
    $$
- **第二类0阶贝塞尔函数 (Bessel function of the second kind of order 0)**，也称为**诺依曼函数 (Neumann function)** 或**韦伯函数 (Weber function)**，通常记为 $Y_0(x)$。它是 $J_0(x)$ 和上面 $y_2(x)$ 的特定线性组合 (Slide 13-14)：
  $$
  Y_0(x) = \frac{2}{\pi} \left( y_2(x) + (\gamma - \ln 2)J_0(x) \right)
  $$
  其中 $\gamma = \lim_{n\to\infty} (H_n - \ln n) \approx 0.577$ 是**欧拉-马歇罗尼常数 (Euler-Mascheroni constant)**。
  $Y_0(x)$ 在 $x=0$ 处不是解析的 (甚至没有定义)，当 $x \to 0^+$ 时，$Y_0(x) \sim \frac{2}{\pi} \ln x$ (Slide 14)。
  $J_0(x)$ 和 $Y_0(x)$ 构成了 $\nu=0$ 时贝塞尔方程的基本解系。

#### Case $\nu \in \mathbb{Z}^+$ (Slide 16: $\nu$ is a positive integer)
- 指标方程的根是 $r_1 = \nu$ 和 $r_2 = -\nu$。它们之差 $r_1 - r_2 = 2\nu$ 是一个正整数。这属于弗罗贝尼乌斯定理的 Case 4。
- 第一个解是 $J_\nu(x)$，它在 $x=0$ 处是解析的。
  $$
  J_\nu(x) = \sum_{m=0}^\infty \frac{(-1)^m}{m! (\nu+m)!} \left(\frac{x}{2}\right)^{2m+\nu}
  $$
- 对于第二个解：在这种情况下，$J_{-\nu}(x)$ 与 $J_\nu(x)$ 是线性相关的。具体来说：
  $$
  J_{-\nu}(x) = (-1)^\nu J_\nu(x), \quad \text{for } \nu \in \mathbb{Z}^+
  $$
  **技术比喻**: 想象你有两把钥匙 $J_\nu$ 和 $J_{-\nu}$。当 $\nu$ 不是整数时，这两把钥匙能打开两把不同的锁。但当 $\nu$ 是正整数时，$J_{-\nu}$ 实际上只是 $J_\nu$ 的一个副本（可能倒过来，即 $(-1)^\nu$ 倍），它们只能打开同一把锁。所以你需要一把全新的、不同类型的钥匙 $Y_\nu(x)$ 来打开第二把锁。
- 因此，我们需要一个不同形式的第二解，即**第二类 $\nu$ 阶贝塞尔函数 (Bessel function of the second kind of order $\nu$)** $Y_\nu(x)$。它的构造类似于 $Y_0(x)$，通常也包含对数项，并且形式更复杂。
  一般定义为：
  $$
  Y_\nu(x) = \lim_{p \to \nu} \frac{J_p(x) \cos(p\pi) - J_{-p}(x)}{\sin(p\pi)}
  $$
  当 $\nu$ 是整数时，这个极限存在并且给出了一个与 $J_\nu(x)$ 线性无关的解。
  $J_\nu(x)$ 和 $Y_\nu(x)$ 构成了 $\nu \in \mathbb{Z}^+$ 时贝塞尔方程的基本解系。

#### Special Case $\nu = 1/2$ (Slides 18-19: Order 1/2)
- 这是一个特殊情况，虽然 $2\nu = 1$ 是整数，但 $\nu=1/2$ 不是整数。如前所述 ($J_\nu, J_{-\nu}$ 线性无关)。
- $J_{1/2}(x)$ 和 $J_{-1/2}(x)$ 可以用初等函数表示：(此时 $a_{0},a_{1}$ 均可以自由定义，所以可以产生两个线性无关的解)
  - 从 Slide 18，通过选择系数 $(a_0, a_1)$，可以推导出：
    - 若 $(a_0, a_1)=(1,0)$ （对应 $r = -1/2$ 的情况，这是 Slide 18 的出发点），可以得到 $y(x) \propto \frac{\cos x}{\sqrt{x}}$。
    - 若 $(a_0, a_1)=(0,1)$ （对应 $r = -1/2$ 的情况），可以得到 $y(x) \propto \frac{\sin x}{\sqrt{x}}$。
  - Slide 19 从 $J_\nu(x)$ 的一般公式出发，使用 $\Gamma(1/2) = \sqrt{\pi}$ 和 $\Gamma(z+1)=z\Gamma(z)$：
    $$
    J_{1/2}(x) = \sqrt{\frac{2}{\pi x}} \sin x
    $$
    $$
    J_{-1/2}(x) = \sqrt{\frac{2}{\pi x}} \cos x
    $$
  这两个函数线性无关，构成了 $\nu=1/2$ 时贝塞尔方程的基本解系。
  这表明，虽然贝塞尔函数通常是超越函数，但在某些特定半整数阶时，它们可以简化为初等函数。

### 贝塞尔函数的图像 (Slides 7, 15, 17)
- **Slide 7**: 展示了不同阶（包括负阶、半整数阶）的 $J_\nu(x)$ 的图像。它们通常表现为在原点附近有特定行为（取决于 $\nu$），并在 $x \to \infty$ 时呈现衰减振荡。
![64bebc5dcdc66124bc1616099d92c98.png](https://s2.loli.net/2025/05/15/yjktS9mqsRpznNH.png)


- **Slide 15**: 展示了 $J_0(t)$ 和 $Y_0(t)$ 的图像。$J_0(0)=1$，$Y_0(t)$ 在 $t \to 0^+$ 时趋于 $-\infty$。两者都呈衰减振荡。

![3b691ce942be84f72149f87d6fdada8.png](https://s2.loli.net/2025/05/15/7VPFzEfCyiDkRq1.png)



- **Slide 17**: 展示了不同整数阶 $J_\nu(x)$ ($\nu \ge 0$) 的图像。

![ab226601d436302d1aa19860da0369b.png](https://s2.loli.net/2025/05/15/OPRFSkNBECqbxmt.png)


## 贝塞尔函数的应用 (Application of Bessel Functions)

这里介绍了一个重要应用：求解**二维波动方程 (2-dimensional wave equation)**。
- **定理 (Theorem, Slide 20)**:
  考虑二维波动方程：
  $$
  \left( \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2} - \frac{1}{c^2} \frac{\partial^2}{\partial t^2} \right) u(x,y,t) = 0
  $$
  如果一个解 $u(x,y,t)$ 可以写成 $u(x,y,t) = f(\lambda r) e^{i(\nu\phi \pm \lambda c t)}$ 的形式，其中 $(r, \phi)$ 是极坐标 ($x=r\cos\phi, y=r\sin\phi$)，$\nu \in \mathbb{Z}$，$\lambda, c > 0$，那么函数 $f(s)$ (这里用 $s$ 代替 $r$ 作为自变量) 必须满足参数为 $\nu$ 的贝塞尔方程：
  $$
  s^2 f''(s) + s f'(s) + (s^2 - \nu^2) f(s) = 0
  $$

- **证明思路 (Proof, Slide 22)**:
  1. 将拉普拉斯算子 $\Delta = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}$ 转换为极坐标形式:
     $$
     \Delta = \frac{\partial^2}{\partial r^2} + \frac{1}{r} \frac{\partial}{\partial r} + \frac{1}{r^2} \frac{\partial^2}{\partial \phi^2}
     $$
  2. 将 $u(x,y,t) = f(\lambda r) e^{i(\nu\phi \pm \lambda c t)}$  代入波动方程。
     $\frac{\partial^2 u}{\partial \phi^2} = f(\lambda r) (-\nu^2) e^{i(\nu\phi \pm \lambda c t)}$
     $\frac{\partial^2 u}{\partial t^2} = f(\lambda r) (-(\lambda c)^2) e^{i(\nu\phi \pm \lambda c t)}$
  3. 经过计算（如 Slide 22 所示），可以得到一个关于 $f(\lambda r)$ 的常微分方程。
     令 $s = \lambda r$。则 $\frac{d}{dr} = \lambda \frac{d}{ds}$，$\frac{d^2}{dr^2} = \lambda^2 \frac{d^2}{ds^2}$。
     代入后整理，最终会得到：
     $$
     s^2 f''(s) + s f'(s) + (s^2 - \nu^2)f(s) = 0
     $$
     其中 $f(s)$ 是 $f$ 关于其自变量 $s=\lambda r$ 的函数。

- **注释 (Notes, Slide 21)**:
  - 这种形式的解来源于**分离变量法 (separation of variables)**。
  - 这可以用来确定圆形膜（如鼓面）的**简正模式 (normal modes)**。
    边界条件：在膜的边缘 $r=R$ (即 $x^2+y^2=R^2$) 处，$u(x,y,t)=0$。
    这意味着 $f(\lambda R)=0$，即 $J_\nu(\lambda R)=0$ (通常排除 $Y_\nu$ 因为它在 $r=0$ 奇异，而鼓面中心应该是良好定义的)。
    因此，$\lambda R$ 必须是 $J_\nu(x)$ 的零点，记为 $z_{\nu n}$ (第 $n$ 个正零点)。
    所以 $\lambda = z_{\nu n}/R$。
  - $\nu=0$ 对应于旋转不变的解。

## 总结 (Summary)

1.  **贝塞尔微分方程**: $x^2 y'' + xy' + (x^2 - \nu^2)y = 0$ 是一个重要的二阶线性 ODE，$\nu$ 是其阶。
2.  **正则奇点**: $x_0=0$ 是一个正则奇点，指标方程为 $r^2 - \nu^2 = 0$，根为 $r_{1,2} = \pm \nu$。
3.  **第一类贝塞尔函数 $J_\nu(x)$**:
    $$
    J_\nu(x) = \sum_{m=0}^\infty \frac{(-1)^m}{m! \Gamma(\nu+m+1)} \left(\frac{x}{2}\right)^{2m+\nu}
    $$
    这是对所有 $\nu$ 都存在的一个解。

4.  **第二类贝塞尔函数 $Y_\nu(x)$ (诺依曼函数)**:
    -   如果 $\nu$ **不是整数**，则 $J_{-\nu}(x)$ 是与 $J_\nu(x)$ 线性无关的第二个解。通常 $Y_\nu(x)$ 会定义为 $J_\nu(x)$ 和 $J_{-\nu}(x)$ 的特定线性组合。
    -   如果 $\nu$ **是整数** (包括 $\nu=0$)，$J_{-\nu}(x) = (-1)^\nu J_\nu(x)$，它们线性相关。第二个解 $Y_\nu(x)$ 形式更复杂，通常包含 $\ln x$ 项，并且在 $x=0$ 处是奇异的。
        -   $Y_0(x) = \frac{2}{\pi} \left( (J_0(x) \ln x + \sum_{m=1}^\infty \frac{(-1)^{m+1}H_m}{(m!)^2} (\frac{x}{2})^{2m}) + (\gamma - \ln 2)J_0(x) \right)$
5.  **基本解系**:
    -   若 $\nu \notin \mathbb{Z}$ (非整数): $\{J_\nu(x), J_{-\nu}(x)\}$
    -   若 $\nu \in \mathbb{Z}$ (整数): $\{J_\nu(x), Y_\nu(x)\}$
6.  **特殊情况 $\nu = n + 1/2$** (n 为整数): $J_{n+1/2}(x)$ 和 $J_{-(n+1/2)}(x)$ 可以用初等函数 (如 $\sin x, \cos x$ 和 $x$ 的幂次) 表示。
    例如: $J_{1/2}(x) = \sqrt{\frac{2}{\pi x}} \sin x$, $J_{-1/2}(x) = \sqrt{\frac{2}{\pi x}} \cos x$。


