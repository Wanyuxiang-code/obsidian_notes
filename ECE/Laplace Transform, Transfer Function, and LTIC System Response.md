---
title: Laplace Transform, Transfer Function, and LTIC System Response
date: 2025-05-15
date modified: 2025-05-15
categories: ECE210
tags:
  - ECE210
---

#ECE210 


## 拉普拉斯变换 (Laplace Transform)

### 拉普拉斯变换的引入与定义 (Introduction and Definition)


我们之前学习了傅里叶变换 (Fourier Transform)，它能将时域信号转换到频域进行分析。但是傅里叶变换要求信号满足狄利克雷条件 (Dirichlet conditions)，比如要求信号绝对可积。对于一些不满足这些条件的信号 (例如 $e^{at}u(t)$ 当 $a>0$ 时)，傅里叶变换可能不存在。

拉普拉斯变换可以看作是傅里叶变换的推广。它引入了一个复频率变量 $s = \sigma + j\omega$，其中 $\sigma$ 是实部，代表衰减或增长因子；$\omega$ 是虚部，代表角频率。

对于一个因果信号 (causal signal) $f(t)$ (即当 $t<0$ 时，$f(t)=0$)，其单边拉普拉斯变换 (Unilateral Laplace Transform) 定义为：
$$
\hat{F}(s) = \mathcal{L}\{f(t)\} = \int_{0^-}^{\infty} f(t)e^{-st}dt
$$
这里的 $0^-$ 表示积分下限从略小于0的时刻开始，这样做是为了能够处理在 $t=0$ 时刻可能存在的冲激函数 (impulse function) 或其导数。

*   **技术比喻**: 想象傅里叶变换是给信号拍了一张“频谱照片”，只能看到信号包含哪些频率成分。拉普拉斯变换则更进一步，它不仅能看到频率成分，还能通过复频率 $s$ 的实部 $\sigma$ 看到这些成分是随时间衰减 ($\sigma > 0$)、增长 ($\sigma < 0$) 还是稳定 ($\sigma = 0$) 的。这就像给信号做了一个更全面的“动态特性扫描”。

对于LTIC System，如果 $h(t)$ 为其的 **Impulse Response** , 那么系统的 **Transer Function** 即为其脉冲响应的Laplace Transform的结果

$$
H(s) = \int_{0}^{\infty}H(t)e^{-st}dt
$$
### 收敛域 (Region of Convergence, ROC)


拉普拉斯变换的积分不一定对所有的复数 $s$ 都收敛。使积分收敛的 $s$ 的取值范围称为收敛域 (Region of Convergence, ROC)。ROC 是 $s$ 平面 (s-plane) 上的一个区域。

*   **对于单边拉普拉斯变换 (因果信号)**：
    *   ROC 通常是一个位于 $s$ 平面某个垂直线的右半平面。这条垂直线由最右边的极点 (pole) 决定，即 ROC 是 $\text{Re}\{s\} > \sigma_{max}$，其中 $\sigma_{max}$ 是**所有极点实部中的最大值**。
    *   例如 (Slides p7 Example #1)，$f(t) = e^t u(t)$，其拉普拉斯变换为 $\hat{F}(s) = \frac{1}{s-1}$。积分 $\int_0^\infty e^t e^{-st} dt = \int_0^\infty e^{(1-s)t} dt$ 收敛的条件是 $\text{Re}\{1-s\} < 0$，即 $\text{Re}\{s\} > 1$。所以 ROC 是 $\sigma > 1$。这个函数的极点在 $s=1$。
    *   例如 (Slides p8 Example #2)，$h(t) = e^{-t} u(t)$，其拉普拉斯变换为 $\hat{H}(s) = \frac{1}{s+1}$。ROC 是 $\text{Re}\{s\} > -1$。极点在 $s=-1$。

*   **极点 (Poles)**: 是使 $\hat{F}(s)$ 的值为**无穷大（即不收敛）**的 $s$ 的值。**它们通常是 $\hat{F}(s)$ 分母多项式的根**。


> [!tip] 核心
> 关注函数 $f(t)$ 的 **Exact Exponential Order** 确定收敛域与极点

- **BIBO 稳定与 ROC:**
    一个 LTIC 系统是 BIBO (Bounded-Input Bounded-Output) 稳定的，当且仅当其传递函数 $\hat{H}(s)$ 的 ROC 包含 $j\omega$ 轴。
    对于因果系统，这等价于 $\hat{H}(s)$ 的所有极点 (poles) 都在 s 平面的左半平面 (Left-Half Plane, LHP)，即 $Re(p_i) < 0$ for all poles $p_i$。
    -  $j\omega$ 轴代表了所有纯正弦频率的输入。如果系统对这些频率的响应都是有界的 (即传递函数在 $j\omega$ 轴上不发散)，那么系统就是 BIBO 稳定的。极点在左半平面意味着系统的自然响应 (冲激响应 $h(t)$) 是随时间衰减的。
    - 对于**BIBO**的**LTIC**系统，其系统的Frequency Response一定存在
    - 对于非**BIBO**的**LTIC**系统，其系统的Frequecy Response可能不存在，但是拉普拉斯变换依然可能存在



### 与傅里叶变换的关系 (Relation to Fourier Transform)


**如果一个信号 $f(t)$ 的拉普拉斯变换 $\hat{F}(s)$ 的 ROC 包含 $j\omega$ 轴 (即 $\text{Re}\{s\} = \sigma = 0$ 包含在 ROC 内)，那么该信号的傅里叶变换 $F(\omega)$ 就存在(其实等价于傅里叶变换的绝对可积条件,拉普拉斯变换)**，并且可以通过令 $s=j\omega$ 从 $\hat{F}(s)$ 得到：
$$
F(\omega) = \hat{F}(s)|_{s=j\omega}
$$
例如，对于 $h(t) = e^{-t} u(t)$，$\hat{H}(s) = \frac{1}{s+1}$，ROC 是 $\text{Re}\{s\} > -1$。由于 ROC 包含了 $j\omega$ 轴，所以其傅里叶变换为 $H(\omega) = \frac{1}{j\omega+1}$。
而对于 $f(t) = e^t u(t)$，$\hat{F}(s) = \frac{1}{s-1}$，ROC 是 $\text{Re}\{s\} > 1$。由于 ROC 不包含 $j\omega$ 轴，所以其傅里叶变换不存在 (标准意义上的)。



### 拉普拉斯变换的性质 (Properties of Laplace Transform)

拉普拉斯变换有很多重要的性质，这些性质在解微分方程和分析系统时非常有用。
1.  **线性 (Linearity)**:
    $\mathcal{L}\{a f_1(t) + b f_2(t)\} = a \hat{F}_1(s) + b \hat{F}_2(s)$
    ROC 是 $\hat{F}_1(s)$ 和 $\hat{F}_2(s)$ 各自 ROC 的交集。
2.  **时移 (Time Shift)**: 
	 应用时移时先判断是否为**因果信号**
    对于因果信号 $f(t)u(t)$ 且 $t_0 \ge 0$，
    $\mathcal{L}\{f(t-t_0)u(t-t_0)\} = e^{-st_0} \hat{F}(s)$
    ROC 不变。
    *注意：* **因果信号和非因果信号**在时移性质应用上存在区别。对于非因果信号或不满足 $t_0 \ge 0$ 的情况，直接套用此公式可能会出错，此时建议回到定义式进行计算。例如 slides p16 的 Example $h(t) = e^{-(t+2)}u(t+2)$，这里 $t_0 = -2 < 0$，不能直接用时移性质，而应该用定义式。
3.  **s域平移 (Shift in s-domain / Frequency Shift)**:
    $\mathcal{L}\{e^{s_0 t} f(t)\} = \hat{F}(s-s_0)$
    ROC 会平移：如果原 ROC 是 $\text{Re}\{s\} > \sigma_0$，则新 ROC 是 $\text{Re}\{s-s_0\} > \sigma_0$，即 $\text{Re}\{s\} > \sigma_0 + \text{Re}\{s_0\}$。
4.  **时域微分 (Time Differentiation)**: 
	 对于因果信号， $f(0-)$ 均为0；对于非因果信号，需要考虑其具体值
    $\mathcal{L}\{\frac{df(t)}{dt}\} = s\hat{F}(s) - f(0^-)$
    $\mathcal{L}\{\frac{d^n f(t)}{dt^n}\} = s^n\hat{F}(s) - s^{n-1}f(0^-) - s^{n-2}f'(0^-) - \dots - f^{(n-1)}(0^-)$
    ROC 至少是 $\hat{F}(s)$ 的 ROC。如果 $\hat{F}(s)$ 在 $s=0$ 有极点，这个极点可能被微分运算消除。
    对于因果信号且初始条件为0 ($f(0^-)=0, f'(0^-)=0, \dots$)，则 $\mathcal{L}\{\frac{d^n f(t)}{dt^n}\} = s^n\hat{F}(s)$。
5.  **s域微分 (Differentiation in s-domain)**:
    $\mathcal{L}\{-t f(t)\} = \frac{d\hat{F}(s)}{ds}$
    ROC 不变。
6.  **时域积分 (Time Integration)**:
    $\mathcal{L}\{\int_{0^-}^t f(\tau)d\tau\} = \frac{1}{s}\hat{F}(s)$
    ROC 是 $\hat{F}(s)$ 的 ROC 与 $\text{Re}\{s\} > 0$ 的交集。
7.  **卷积 (Convolution)**:
    $\mathcal{L}\{f_1(t) * f_2(t)\} = \hat{F}_1(s) \hat{F}_2(s)$
    ROC 包含 $\hat{F}_1(s)$ 和 $\hat{F}_2(s)$ 各自 ROC 的交集。这个性质非常重要，它将时域的卷积运算转换成了 $s$ 域的乘积运算。
8.  **初值定理 (Initial Value Theorem)**:
    如果 $f(t)$ 在 $t=0^+$ 没有冲激或更高阶的奇异性，则
    $f(0^+) = \lim_{s \to \infty} s\hat{F}(s)$
9.  **终值定理 (Final Value Theorem)**:
    如果 $s\hat{F}(s)$ 的所有极点都在左半平面 (LHP)，即 $\lim_{t \to \infty} f(t)$ 存在，则
    $\lim_{t \to \infty} f(t) = \lim_{s \to 0} s\hat{F}(s)$

## 拉普拉斯逆变换 (Inverse Laplace Transform, ILT)

从 $s$ 域的表达式 $\hat{F}(s)$ 反求时域信号 $f(t)$ 的过程称为拉普拉斯逆变换，记为 $f(t) = \mathcal{L}^{-1}\{\hat{F}(s)\}$。对于单边拉普拉斯变换，如果 $\hat{F}(s)$ 存在，其逆变换是唯一的 (得到因果信号)。

我们主要处理有理函数 (rational functions) $\hat{F}(s) = \frac{N(s)}{D(s)}$，其中 $N(s)$ 和 $D(s)$ 是关于 $s$ 的多项式。

### 部分分式展开 (Partial Fraction Expansion, PFE)


PFE 是求有理函数逆变换的常用方法。基本思想是将复杂的 $\hat{F}(s)$ 分解成若干个简单项的和，然后利用已知的拉普拉斯变换对进行逆变换。

1.  **预处理：确保为真分式 (Proper Rational Function)**
    如果 $\hat{F}(s)$ 是假分式 (improper rational function)，即分子多项式 $N(s)$ 的阶数 $\ge$ 分母多项式 $D(s)$ 的阶数，需要先通过多项式长除法 (long division) 将其化为一个多项式和真分式之和：
    $\hat{F}(s) = Q(s) + \frac{R(s)}{D(s)}$
    其中 $Q(s)$ 是商式多项式，$R(s)$ 是余式多项式且其阶数小于 $D(s)$ 的阶数。多项式 $Q(s)$ 部分的逆变换会产生冲激函数及其各阶导数。余下的真分式 $\frac{R(s)}{D(s)}$ 再进行部分分式展开。


2.  **对真分式进行PFE**:
    *   **情况一：分母 $D(s)$ 只有互异实根 (Distinct Real Poles)** (Slides p23-25, Textbook p381-383)
        设 $D(s) = (s-p_1)(s-p_2)\dots(s-p_n)$，其中 $p_i$ 互不相同。
        $$
        \hat{F}(s) = \frac{A_1}{s-p_1} + \frac{A_2}{s-p_2} + \dots + \frac{A_n}{s-p_n}
        $$
        系数 $A_k$ 可以用“留数法”或“覆盖法” (cover-up method) 计算：
        $$
        A_k = [(s-p_k)\hat{F}(s)]_{s=p_k}
        $$
        每一项 $\frac{A_k}{s-p_k}$ 的逆变换是 $A_k e^{p_k t}u(t)$。


    *   **情况二：分母 $D(s)$ 有重根 (Repeated Real Poles)** 
        如果 $D(s)$ 包含因子 $(s-p_i)^r$，其中 $r$ 是重根的阶数。
        对应的部分分式展开项为：
        $$
        \frac{A_{i1}}{s-p_i} + \frac{A_{i2}}{(s-p_i)^2} + \dots + \frac{A_{ir}}{(s-p_i)^r}
        $$
        最高阶次项的系数 $A_{ir}$ 仍可用覆盖法计算：$A_{ir} = [(s-p_i)^r \hat{F}(s)]_{s=p_i}$。
        其他系数 $A_{i,r-m}$ ($1 \le m < r$) 的计算公式为：
        $$
        A_{i,r-m} = \frac{1}{m!} \frac{d^m}{ds^m} [(s-p_i)^r \hat{F}(s)]_{s=p_i}
        $$
        或者，也可以通过代入特定 $s$ 值或比较系数的方法求解。
        每一项 $\frac{A_{ik}}{(s-p_i)^k}$ 的逆变换是 $\frac{A_{ik}}{(k-1)!} t^{k-1} e^{p_i t}u(t)$。

    *   **情况三：分母 $D(s)$ 有共轭复根 (Distinct Complex Conjugate Poles)** 
        如果 $D(s)$ 包含因子 $(s - (\alpha+j\beta))(s - (\alpha-j\beta)) = (s-\alpha)^2 + \beta^2$。
        对应的部分分式展开项为：
        $$
        \frac{K_1}{s-(\alpha+j\beta)} + \frac{K_1^*}{s-(\alpha-j\beta)}
        $$
        其中 $K_1$ 和 $K_1^*$ 是共轭复数。$K_1$ 可以用覆盖法计算。
        这两项的逆变换合起来是：
        $2|K_1|e^{\alpha t} \cos(\beta t + \angle K_1) u(t)$
        或者，也可以将二次不可约因子保留在分母（然后待定其分子为关于s的一次函数，考虑待定系数法），展开成 $\frac{As+B}{(s-\alpha)^2 + \beta^2}$ 的形式，然后凑成标准变换对 $e^{-\alpha t}\cos(\beta t)u(t) \leftrightarrow \frac{s+\alpha}{(s+\alpha)^2+\beta^2}$ 和 $e^{-\alpha t}\sin(\beta t)u(t) \leftrightarrow \frac{\beta}{(s+\alpha)^2+\beta^2}$ 的线性组合。


### 处理非真有理函数 (Improper Rational Functions)

如果 $\hat{F}(s) = \frac{N(s)}{D(s)}$ 中，$N(s)$ 的阶数 $\ge D(s)$ 的阶数，则 $\hat{F}(s)$ 是非真有理函数。
需要先用多项式长除法：
$\hat{F}(s) = Q(s) + \frac{R(s)}{D(s)}$，其中 $Q(s)$ 是商多项式，$R(s)/D(s)$ 是真有理分式。
$Q(s)$ 的反变换会包含冲激函数及其导数。
例如：
- 如果 $Q(s) = C_0$ (常数)，则 $\mathcal{L}^{-1}\{C_0\} = C_0 \delta(t)$。
- 如果 $Q(s) = C_1 s$，则 $\mathcal{L}^{-1}\{C_1 s\} = C_1 \delta'(t)$ (假设因果)。


*   **Case 1: $\hat{F}(s) = s^k \hat{G}(s)$**
    *   **前提**: $\hat{G}(s)$ 是一个已知的变换，通常是真有理函数，其反变换为 $g(t)$。
    *   **条件**: $g(t)$ 是因果的，并且在 $t=0^-$ 处的初始值及其直到 $(k-1)$ 阶导数均为零。即 $g(0^-) = g'(0^-) = \dots = g^{(k-1)}(0^-) = 0$。
    *   **结论**: $f(t) = \frac{d^k g(t)}{dt^k}$。
    *   **解释**: 这是拉普拉斯变换的时域微分性质的直接应用：$\mathcal{L}\left\{\frac{d^k g(t)}{dt^k}\right\} = s^k \hat{G}(s) - s^{k-1}g(0^-) - \dots - g^{(k-1)}(0^-)$。当初始条件为零时，后面减去的项都消失了。
    *   **Example 13 (Slide 33)**: $\hat{F}(s) = \frac{s}{s+1}$
        -   这里 $k=1$, $\hat{G}(s) = \frac{1}{s+1}$。
        -   $g(t) = \mathcal{L}^{-1}\{\hat{G}(s)\} = e^{-t}u(t)$。
        -   $g(t)$ 是因果的，且 $g(0^-)=0$ (因为 $u(0^-)=0$)。
        -   所以 $f(t) = \frac{d}{dt}g(t) = \frac{d}{dt}(e^{-t}u(t))$。
        -   使用乘积求导法则: $f(t) = (\frac{d}{dt}e^{-t})u(t) + e^{-t}(\frac{d}{dt}u(t)) = -e^{-t}u(t) + e^{-t}\delta(t)$。
        -   利用冲激函数的筛选性质 (sifting property): $e^{-t}\delta(t) = e^{-0}\delta(t) = \delta(t)$。
        -   所以 $f(t) = -e^{-t}u(t) + \delta(t)$。
    *   **与长除法联系**:
        $\frac{s}{s+1} = \frac{s+1-1}{s+1} = \frac{s+1}{s+1} - \frac{1}{s+1} = 1 - \frac{1}{s+1}$。
        这里 $Q(s)=1$, $\frac{R(s)}{D(s)} = -\frac{1}{s+1}$。
        $\mathcal{L}^{-1}\{1\} = \delta(t)$。
        $\mathcal{L}^{-1}\{-\frac{1}{s+1}\} = -e^{-t}u(t)$。
        结果一致。可见 Case 1 是长除法的一种特殊情况，当除法结果是 $s^k$ 乘以一个简单的真有理分式时，可以看作是对真有理分式对应的时域信号求导。

*   **Case 2: $\hat{F}(s) = \frac{s^n + P_N(s)}{s^n + P_D(s)}$ (分子分母同阶，最高次系数为1)**
    *   **形式**: $\hat{F}(s) = \frac{s^n + \text{低阶项}}{s^n + \text{低阶项}}$ (这里 $P(s)$ 在 PPT 中指的是分母的低阶项，即 $D(s) = s^n + P(s)$，而分子是 $s^n$。PPT 的写法是 $\hat{F}(s) = \frac{s^n}{s^n + P(s)}$)
    *   **处理**: $\hat{F}(s) = \frac{s^n + P(s) - P(s)}{s^n + P(s)} = 1 - \frac{P(s)}{s^n + P(s)}$。
    *   令 $\hat{G}(s) = \frac{P(s)}{s^n + P(s)}$ (这是一个真有理函数)。
    *   则 $f(t) = \delta(t) - g(t)$。
    *   **Example 14 (Slide 35)**: $\hat{F}(s) = \frac{s}{s+1}$。
        -   $n=1$, $P(s)=1$ (与 PPT 记号对应)。
        -   $\hat{F}(s) = \frac{s}{s+1} = 1 - \frac{1}{s+1}$。
        -   $\hat{G}(s) = \frac{1}{s+1}$, $g(t) = e^{-t}u(t)$。
        -   $f(t) = \delta(t) - e^{-t}u(t)$。
    *   **解释**: 这本质上就是多项式长除法的第一步。商是1，余数是 $-P(s)$。

*   **Case 3: $\hat{F}(s) = \frac{s^n + Q_N(s)}{s^n + P_D(s)}$ (分子分母同阶，最高次系数为1，分子有额外低阶项)**
    *   **形式**: $\hat{F}(s) = \frac{s^n + Q(s)}{s^n + P(s)}$ (这里 $Q_N(s)$ 是分子 $N(s)$ 的低阶项 $Q(s)$, $P_D(s)$ 是分母 $D(s)$ 的低阶项 $P(s)$)。
    *   **处理**: $\hat{F}(s) = \frac{s^n + P(s) + Q(s) - P(s)}{s^n + P(s)} = 1 + \frac{Q(s) - P(s)}{s^n + P(s)}$。
    *   令 $\hat{G}(s) = \frac{Q(s) - P(s)}{s^n + P(s)}$ (这是一个真有理函数)。
    *   则 $f(t) = \delta(t) + g(t)$。
    *   **Example 15 (Slide 37)**: $\hat{F}(s) = \frac{s^2+1}{s^2+3s+2}$。
        -   $n=2$, $Q(s)=1$, $P(s)=3s+2$。
        -   $\hat{F}(s) = \frac{s^2+3s+2 - 3s - 2 + 1}{s^2+3s+2} = 1 + \frac{-3s-1}{s^2+3s+2} = 1 - \frac{3s+1}{s^2+3s+2}$。
        -   令 $\hat{G}_{orig}(s) = \frac{3s+1}{s^2+3s+2}$。
            $\hat{G}_{orig}(s) = \frac{3s+1}{(s+1)(s+2)} = \frac{A}{s+1} + \frac{B}{s+2}$。
            $A = \frac{3(-1)+1}{-1+2} = \frac{-2}{1} = -2$。
            $B = \frac{3(-2)+1}{-2+1} = \frac{-5}{-1} = 5$。
            $\hat{G}_{orig}(s) = \frac{-2}{s+1} + \frac{5}{s+2}$。
            $g_{orig}(t) = (-2e^{-t} + 5e^{-2t})u(t)$。
        -   所以 $f(t) = \delta(t) - g_{orig}(t) = \delta(t) - (-2e^{-t} + 5e^{-2t})u(t) = \delta(t) + (2e^{-t} - 5e^{-2t})u(t)$。
        -   PPT 中的 $\hat{G}(s)$ 是 $\frac{-(3s+1)}{s^2+3s+2}$, 所以 $f(t) = \delta(t) + g(t)$，其中 $g(t) = (2e^{-t} - 5e^{-2t})u(t)$。结果一致。
    *   **解释**: 这同样是多项式长除法的第一步。商是1，余数是 $Q(s)-P(s)$。

*   **Case 4: $\hat{F}(s) = e^{-as} \frac{N(s)}{D(s)}$ (其中 $\frac{N(s)}{D(s)}$ 可能是真或非真有理)**
    *   **前提**: $a > 0$。
    *   **处理**: 这利用了时移性质。
        1.  首先，令 $\hat{H}(s) = \frac{N(s)}{D(s)}$ (忽略 $e^{-as}$ 项)。
        2.  求出 $h(t) = \mathcal{L}^{-1}\{\hat{H}(s)\}$。如果 $\hat{H}(s)$ 本身是非真有理的，则在这一步就需要用前面的方法 (如长除法) 处理 $\hat{H}(s)$。
        3.  然后 $f(t) = h(t-a)u(t-a)$ (如果 $h(t)$ 是因果的，即 $h(t)=h(t)u(t)$)。更准确地说是 $f(t) = h_0(t-a)$ 其中 $h_0(t)$ 是 $\hat{H}(s)$ 对应的信号。通常我们处理因果信号，所以 $\hat{H}(s)$ 的反变换 $h(t)$ 本身就包含了 $u(t)$ 或者我们假设其为因果的。
    *   **Example 16 (Slide 39)**: $\hat{F}(s) = e^{-2s} \frac{1}{s+1}$。
        -   $a=2$。
        -   $\hat{G}(s) = \frac{1}{s+1}$ (PPT 中用 $\hat{G}(s)$ 表示 $\frac{N(s)}{D(s)}$)。
        -   $g(t) = \mathcal{L}^{-1}\{\hat{G}(s)\} = e^{-t}u(t)$。
        -   所以 $f(t) = g(t-2) = e^{-(t-2)}u(t-2)$。
    *   **如果 $\frac{N(s)}{D(s)}$ 非真?**
        例如 $\hat{F}(s) = e^{-as} \frac{s}{s+1}$。
        1.  令 $\hat{H}(s) = \frac{s}{s+1} = 1 - \frac{1}{s+1}$。
        2.  $h(t) = \mathcal{L}^{-1}\{\hat{H}(s)\} = \delta(t) - e^{-t}u(t)$。
        3.  $f(t) = h(t-a) = \delta(t-a) - e^{-(t-a)}u(t-a)$。


## s-domain Analysis of LTIC Systems (LTIC 系统的 s 域分析)

s 域分析是利用拉普拉斯变换 (Laplace Transform) 将**时域**(time-domain) 中的线性时不变 (Linear Time-Invariant, LTIC) 系统及其信号转换到**复频域** (s-domain)进行分析的方法。这样做通常可以简化分析过程，特别是对于涉及微分方程的系统。

### 基本概念 

1.  **系统输入输出关系**:
    -   在时域中，LTIC 系统的输出 $y(t)$ 是输入 $f(t)$ 与系统冲激响应 (impulse response) $h(t)$ 的卷积 (convolution):
        $$
        y(t) = f(t) * h(t)
        $$
    -   在 s 域中，卷积运算转换为乘法运算。设 $\hat{F}(s)$, $\hat{Y}(s)$, $\hat{H}(s)$ 分别是 $f(t)$, $y(t)$, $h(t)$ 的拉普拉斯变换，则零状态响应 (zero-state response) $\hat{Y}_{zs}(s)$ 为：
        $$
        \hat{Y}_{zs}(s) = \hat{F}(s) \hat{H}(s)
        $$
        其中 $\hat{H}(s)$ 被称为系统的传递函数 (Transfer Function)。

2.  **传递函数 (Transfer Function)**:
    -   传递函数 $\hat{H}(s)$ 定义为系统在**零初始条件**下，输出信号的拉普拉斯变换与输入信号的拉普拉斯变换之比：
        $$
        \hat{H}(s) = \frac{\hat{Y}_{zs}(s)}{\hat{F}(s)}
        $$
    -   对于集总参数 (lumped element) LTIC 系统，其传递函数通常是 s 的有理函数 (rational function)，即两个多项式之比：
        $$
        \hat{H}(s) = \frac{N(s)}{D(s)} = \frac{b_0s^m + b_1s^{m-1} + \dots + b_m}{s^n + a_1s^{n-1} + \dots + a_n}
        $$
        其中 $N(s)$ 是分子多项式， $D(s)$ 是分母多项式。


3.  **从传递函数到微分方程 (零状态)**:
    -   将 $\hat{Y}_{zs}(s) = \hat{F}(s) \hat{H}(s)$ 变形为：
        $$
        \hat{Y}_{zs}(s) D(s) = \hat{F}(s) N(s)
        $$
        展开后得到：
        $$
        \hat{Y}_{zs}(s) (s^n + a_1s^{n-1} + \dots + a_n) = \hat{F}(s) (b_0s^m + b_1s^{m-1} + \dots + b_m)
        $$
    -   利用拉普拉斯变换的微分性质 (假设信号为因果信号且初始条件为零，即 $\mathcal{L}\{\frac{d^k x(t)}{dt^k}\} = s^k \hat{X}(s)$)，可以将上式反变换回时域，得到描述系统零状态响应的微分方程：
        $$
        \frac{d^n y_{zs}(t)}{dt^n} + a_1 \frac{d^{n-1} y_{zs}(t)}{dt^{n-1}} + \dots + a_n y_{zs}(t) = b_0 \frac{d^m f(t)}{dt^m} + b_1 \frac{d^{m-1} f(t)}{dt^{m-1}} + \dots + b_m f(t)
        $$


### 完整解 (Full Solution) - 包含初始条件 
**以微分方程视角看**
- Zero-state output：对应微分方程的特解
- Zero-input output：对应微分方程的齐次解

系统的完整响应 $y(t)$ 包括零状态响应 $y_{zs}(t)$ 和零输入响应 (zero-input response) $y_{zi}(t)$：
$$
y(t) = y_{zs}(t) + y_{zi}(t)
$$
在 s 域中：
$$
\hat{Y}(s) = \hat{Y}_{zs}(s) + \hat{Y}_{zi}(s)
$$

1.  **考虑初始条件的拉普拉斯变换**:
    -   当考虑非零初始条件时，时域微分的拉普拉斯变换为：
        $$
        \mathcal{L}\left\{\frac{d^k x(t)}{dt^k}\right\} = s^k \hat{X}(s) - s^{k-1}x(0^-) - s^{k-2}x'(0^-) - \dots - x^{(k-1)}(0^-)
        $$
    -   将描述系统的微分方程 (包含 $y(t)$ 和 $f(t)$ 及其各阶导数) 进行拉普拉斯变换，并代入上述带有初始条件的微分性质。假设输入 $f(t)$ 是因果的 (causal)，则其在 $t<0$ 时的初始条件为零。
    -   整理后，可以将 $\hat{Y}(s)$ 表示为：
        $$
        \hat{Y}(s) (s^n + a_1s^{n-1} + \dots + a_n) - I_y(s) = \hat{F}(s) (b_0s^m + b_1s^{m-1} + \dots + b_m) - I_f(s)
        $$
        其中 $I_y(s)$ 是包含 $y(t)$ 及其导数在 $t=0^-$ 处初始条件的多项式， $I_f(s)$ 是包含 $f(t)$ 及其导数在 $t=0^-$ 处初始条件的多项式。
        如果输入 $f(t)$ 是在 $t \ge 0$ 时才施加的 (causal input)，则 $I_f(s) = 0$。

2.  **分离零状态响应和零输入响应**:
    -   求解 $\hat{Y}(s)$：
        $$
        \hat{Y}(s) = \frac{N(s)}{D(s)}\hat{F}(s) + \frac{I_y(s) - I_f(s) \text{ (assuming } I_f(s) \text{ moved from RHS)}}{D(s)}
        $$
        其中 $D(s) = s^n + a_1s^{n-1} + \dots + a_n$ 且 $N(s) = b_0s^m + \dots + b_m$。
    -   因此：
        -   零状态响应 (Zero-State Response):
            $$
            \hat{Y}_{zs}(s) = \frac{N(s)}{D(s)}\hat{F}(s) = \hat{H}(s)\hat{F}(s)
            $$
            这部分响应只由输入 $\hat{F}(s)$ 引起，假设所有初始条件为零。
        -   零输入响应 (Zero-Input Response):
            $$
            \hat{Y}_{zi}(s) = \frac{P(s)}{D(s)}
            $$
            其中 $P(s)$ 是一个仅由系统初始条件 $y(0^-), y'(0^-), \dots, y^{(n-1)}(0^-)$ 和输入信号在 $t=0^-$ 时的初始条件 (如果输入非因果) 决定的多项式。如果输入是因果的，则 $P(s)$ 仅由 $y(t)$ 的初始条件决定。这部分响应只由系统初始状态引起，假设输入为零。


### 特征多项式、特征极点和特征模式 

1.  **特征多项式 (Characteristic Polynomial)**:
    -   系统微分方程的特征多项式是传递函数分母 $D(s)$ (或者说，是齐次微分方程对应的代数多项式，或即系统输出对应的代数多项式):
        $$
        D(s) = s^n + a_1s^{n-1} + \dots + a_n
        $$
    -   这个多项式决定了系统的固有行为特性。

2.  **特征极点 (Characteristic Poles)**:
    -   特征多项式的根 $p_1, p_2, \dots, p_n$ (即满足 $D(s)=0$ 的 $s$ 值) 称为系统的特征极点。
    -   这些极点的位置直接影响系统的稳定性和响应特性。
    -   注意：这里的特征极点是指导致 $D(s)=0$ 的值。传递函数的极点是 $D(s)=0$ 的根，并且不能与 $N(s)=0$ 的根 (零点) 相消。

3.  **特征模式 (Characteristic Modes)**:
    -   零输入响应 $y_{zi}(t)$ 的形式由特征极点决定。
        -   如果 $p_i$ 是一个单实数极点，则对应的模式是 $A_i e^{p_i t}$。
        -   如果 $p_i, p_i^*$ 是一对共轭复极点 $\sigma_i \pm j\omega_i$，则对应的模式是 $e^{\sigma_i t}(B_i \cos(\omega_i t) + C_i \sin(\omega_i t))$。
        -   如果 $p_i$ 是一个 $k$ 重实数极点，则对应的模式是 $(A_1 + A_2 t + \dots + A_k t^{k-1})e^{p_i t}$。
    -   这些模式是系统“喜欢”振荡或衰减的方式，是系统的固有行为。


### 系统稳定性 

1.  **BIBO 稳定 (Bounded-Input Bounded-Output Stability)**:
    -   如果一个系统对于任何有界输入，其输出也是有界的，则称该系统是 BIBO 稳定的。
    -   对于 LTIC 系统，**BIBO 稳定的充要条件是其传递函数 $\hat{H}(s)$ 的所有极点都在 s 平面的左半平面 (Left-Half Plane, LHP)，即所有极点的实部都小于零 ($\text{Re}\{p_i\} < 0$)**。(这里指的是**经过零极点对消后的最简形式**传递函数的极点)。
    -   这意味着 $\hat{H}(s)$ 的收敛域 (Region of Convergence, ROC) 包含虚轴 $j\omega$-axis。
    -   这也意味着系统的冲激响应的**Exact Exponential Order**小于0

2.  **渐近稳定 (Asymptotical Stability)** :
    -   如果系统的零输入响应 $y_{zi}(t)$ 随着时间 $t \to \infty$ 趋近于零，即 $\lim_{t\to\infty} y_{zi}(t) = 0$，则称系统是渐近稳定的。
    -   这要求系统的所有特征极点 (characteristic poles，即 $D(s)=0$ 的所有根，**在进行任何可能的传递函数零极点对消之前**) 都在 s 平面的左半平面。

3.  **边缘稳定 (Marginally Stable)**:
    -   如果系统的零输入响应 $y_{zi}(t)$ 随着 $t \to \infty$ 保持**有界但不趋于零** (例如，产生持续的等幅振荡)，则称系统是边缘稳定的。
    -   这通常发生在系统**存在位于虚轴上的单重极点** (non-repeated poles on the $j\omega$-axis)，且其他极点都在左半平面时。
    -   如果虚轴上有重根极点，系统通常是不稳定的 (零输入响应会随时间无限增大，如 $t \sin(\omega t)$)。


**注意区分 BIBO 稳定和渐近稳定**:
-   一个系统可能存在位于右半平面或虚轴上的特征极点，但如果这些极点恰好被传递函数的零点所抵消，那么该系统可能仍然是 BIBO 稳定的 (因为这些“坏”模式不会被外部输入所激励)。
-   然而，这样的系统不是渐近稳定的，因为其零输入响应 (如果初始条件恰好能激励这些未被抵消的模式) 可能不会衰减到零。
-   通常，如果所有特征极点都在左半平面，系统既是 BIBO 稳定的也是渐近稳定的。

### LTIC 电路在 s 域的分析 

可以将电路元件直接转换到 s 域进行分析，这使得包含电感和电容的交流和暂态电路分析更加系统化。

1.  **电阻 (Resistor R)**:
    -   时域: $v(t) = R i(t)$
    -   s 域: $\hat{V}(s) = R \hat{I}(s)$
    -   阻抗 (Impedance): $Z_R(s) = R$

2.  **电感 (Inductor L)**:
    -   时域: $v(t) = L \frac{di(t)}{dt}$
    -   s 域 (考虑初始电流 $i(0^-)$): $\hat{V}(s) = sL \hat{I}(s) - L i(0^-)$
        -   这可以看作是一个阻抗 $sL$ 串联一个电压源 $L i(0^-)$ (方向与电流 $\hat{I}(s)$ 流过 $sL$ 产生的电压降相反，即 $L i(0^-)$ 的正端朝向电流流入端)。
    -   阻抗: $Z_L(s) = sL$

3.  **电容 (Capacitor C)**:
    -   时域: $i(t) = C \frac{dv(t)}{dt}$
    -   s 域 (考虑初始电压 $v(0^-)$): $\hat{I}(s) = sC \hat{V}(s) - C v(0^-)$
        -   变形为 $\hat{V}(s) = \frac{1}{sC} \hat{I}(s) + \frac{v(0^-)}{s}$
        -   这可以看作是一个阻抗 $\frac{1}{sC}$ 串联一个电压源 $\frac{v(0^-)}{s}$ (方向与 $v(0^-)$ 一致，即 $v(0^-)$ 的正极性对应 $\frac{v(0^-)}{s}$ 电压源的正端)。
    -   阻抗: $Z_C(s) = \frac{1}{sC}$

使用这些 s 域等效模型后，就可以像分析纯电阻电路一样，使用基尔霍夫定律 (Kirchhoff's Laws)、节点电压法、网孔电流法等标准电路分析技术来求解 s 域中的电压和电流。

### LTIC 系统组合 (LTIC System Combinations) 

多个 LTIC 系统可以组合成更复杂的系统。它们的总体传递函数可以通过各个子系统的传递函数来确定。

1.  **串联/级联 (Series or Cascade)**:
    -   系统 $H_1$ 的输出是系统 $H_2$ 的输入，以此类推。
        $f(t) \rightarrow \boxed{H_1(s)} \rightarrow \boxed{H_2(s)} \rightarrow \dots \rightarrow \boxed{H_k(s)} \rightarrow y(t)$
    -   总体传递函数是各个子系统传递函数的乘积：
        $$
        \hat{H}_{overall}(s) = \hat{H}_1(s) \hat{H}_2(s) \dots \hat{H}_k(s)
        $$


2.  **并联 (Parallel)**:
    -   同一个输入信号 $f(t)$ 同时作用于多个子系统 $H_1, H_2, \dots, H_k$，它们的输出相加得到最终输出 $y(t)$。
    -   总体传递函数是各个子系统传递函数的和：
        $$
        \hat{H}_{overall}(s) = \hat{H}_1(s) + \hat{H}_2(s) + \dots + \hat{H}_k(s)
        $$


3.  **反馈 (Feedback)**:
    -   一个基本的负反馈系统，包含一个前向通路 (forward path) $\hat{H}_1(s)$ 和一个反馈通路 (feedback path) $\hat{H}_2(s)$。输出信号的一部分通过 $\hat{H}_2(s)$ 反馈到输入端，与原始输入信号作差 (负反馈) 或作和 (正反馈) 后，再进入 $\hat{H}_1(s)$。
    -   对于负反馈系统：
        $$
        \hat{H}_{overall}(s) = \frac{\hat{H}_1(s)}{1 + \hat{H}_1(s)\hat{H}_2(s)}
        $$
    -   对于正反馈系统 (幻灯片中未明确画出，但若反馈信号是相加)：
        $$
        \hat{H}_{overall}(s) = \frac{\hat{H}_1(s)}{1 - \hat{H}_1(s)\hat{H}_2(s)}
        $$
    -   反馈是控制系统中非常重要的概念，可以用来改善系统性能，如提高稳定性、减小误差、改变系统响应速度等。


