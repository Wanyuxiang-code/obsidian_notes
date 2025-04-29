---
title: Fourier Transform and LTI System Response to Energy Signals
date: 2025-04-14
date modified: 2025-04-14
categories: ECE210
tags:
  - ECE210
---

#ECE210 



## 傅里叶变换对 $f(t) \leftrightarrow F(\omega)$ 及其性质 (Fourier Transform Pairs and Their Properties)

### 傅里叶变换 (Fourier Transform) 与反变换 (Inverse Fourier Transform)

- **傅里叶变换 (FT):** 将一个时域信号 $f(t)$ 转换到频域表示 $F(\omega)$。它告诉我们信号由哪些频率的正弦/余弦波组成，以及各个频率分量的幅度和相位。
  公式定义为:
  $$
  F(\omega) = \int_{-\infty}^{\infty} f(t)e^{-j\omega t} dt
  $$
  其中 $\omega$ 是角频率 (rad/s)， $F(\omega)$ 通常是一个复数函数，包含了幅度和相位信息。

- **傅里叶反变换 (IFT):** 将频域表示 $F(\omega)$ 转换回时域信号 $f(t)$。
  公式定义为:
  $$
  f(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega)e^{j\omega t} d\omega
  $$

- **变换对表示:** 我们常用 $f(t) \leftrightarrow F(\omega)$ 来表示 $f(t)$ 和 $F(\omega)$ 构成一个傅里叶变换对。

### 存在条件 (Existence Conditions)

- 傅里叶变换存在的**充分条件**是信号 $f(t)$ **绝对可积 (Absolutely Integrable, A.I.)**，即：
  $$
  \int_{-\infty}^{\infty} |f(t)| dt < \infty
  $$
  这保证了定义 $F(\omega)$ 的积分收敛。
- **技术比喻:** 这就像问一个信号的总“震动量”是不是有限的。如果无限时间内的总震动量是有限的，我们就能很好地分析它的频率构成。满足 $|f(t)|$ 绝对可积的信号称为能量信号
- 需要注意的是，即使某些信号不满足绝对可积条件 (例如 $sinc(t)$ 函数，或者理想的 $cos(\omega_0 t)$)，它们在特定条件下 (如满足狄利克雷条件 Dirichlet conditions) 可能仍然存在傅里叶变换，或者可以通过广义函数 (如狄拉克 δ 函数) 来表示其变换 [^3]。

### 重要性质 (Properties)

傅里叶变换具有许多重要的性质，这些性质极大地简化了信号与系统分析：

- **线性 (Linearity):** $a f(t) + b g(t) \leftrightarrow a F(\omega) + b G(\omega)$ 。
  - **说明:** 系统的响应等于各个输入信号独立产生的响应之和。这就像混音，总音效是各个乐器声音的叠加。
- **幅度缩放 (Amplitude Scaling):** $K f(t) \leftrightarrow K F(\omega)$ 。
  - **说明:** 信号在时域整体放大 K 倍，其频谱也在频域整体放大 K 倍。
- **时间缩放 (Time Scaling):** 对于实数 $a$: $f(at) \leftrightarrow \frac{1}{|a|} F(\frac{\omega}{a})$
  - **说明:**
    - 当 $|a| > 1$ 时，信号在时域被压缩 (变窄)，其频谱在频域被扩展 (变宽)。
    - 当 $0 < |a| < 1$ 时，信号在时域被扩展 (变宽)，其频谱在频域被压缩 (变窄)。
    - 当 $a < 0$ 时，信号在时域还会反转。
  - **技术比喻:** 这就像播放磁带。快速播放 ($a>1$) 时，声音持续时间变短，但音调 (频率) 变高 (频谱展宽)；慢速播放 ($a<1$) 则相反。时域宽度和频域宽度之间存在 **反比关系** 。
- **时间平移 (Time Shifting):** $f(t-t_0) \leftrightarrow e^{-j\omega t_0} F(\omega)$。
  - **说明:** 信号在时域平移 $t_0$，其傅里叶变换的幅度 $|F(\omega)|$ 不变，但会引入一个线性相移 $- \omega t_0$。
  - **技术比喻:** 这就像声音信号的延迟播放。声音内容 (频率成分) 没变，只是到达的时间晚了，这体现在频域的相位变化上。
- **对称性/对偶性 (Symmetry/Duality):** 若 $f(t) \leftrightarrow F(\omega)$，则 $F(t) \leftrightarrow 2\pi f(-\omega)$ 。
  - **说明:** 时域函数和频域函数的形式可以互换 (经过适当缩放和反转)。这个性质很有用，可以从已知的变换对推导出新的变换对 (例如 Slide 19 的例子)。
- **厄米特性 (Hermitian Property):** 如果 $f(t)$ 是实数信号，则 $F(-\omega) = F^*(\omega)$ (其中 $*$ 表示复共轭)。
  - **说明:** 这意味着对于实信号，$|F(\omega)|$ 是偶函数 (关于 $\omega=0$ 对称)，而相位 $\angle F(\omega)$ 是奇函数。
- **实偶/奇信号性质 (Real Even/Odd Signals):** 
    - 如果 $f(t)$ 是实偶函数 (Real and Even)，则 $F(\omega)$ 也是实偶函数。
    - 如果 $f(t)$ 是实奇函数 (Real and Odd)，则 $F(\omega)$ 是纯虚奇函数。

![ac758baf82721426f7255cce92c089a.png](https://s2.loli.net/2025/04/23/S3j5Wxa4usEFeR8.png)

### 常见变换对举例
![0392db7810ea1755e8536427fb5956b.png](https://s2.loli.net/2025/04/23/UdsSI4Th3GX8LvH.png)

、

*注意： $\mathrm{rect}(x)$ 是矩形函数， $\Delta(x)$ 是三角形函数， $\mathrm{sinc}(x) = \sin(x)/x$ 是 Sinc 函数。*
## 信号的频域描述 (Frequency-Domain Description of Signals)

这一部分关注如何从频域角度描述信号的能量特性。

### 信号能量 (Signal Energy) 与帕塞瓦尔定理 (Parseval's Theorem)

- **能量信号 (Energy Signal):** 指总能量有限，平均功率为零的信号。我们主要讨论这类信号的傅里叶变换。
- **信号能量 (W):** 一个信号 $f(t)$ 的总能量定义为:
  $$
  W = \int_{-\infty}^{\infty} |f(t)|^2 dt
  $$
- **帕塞瓦尔定理 (Parseval's Theorem):** 该定理建立了信号的时域能量与频域能量之间的关系 :
  $$
  W = \int_{-\infty}^{\infty} |f(t)|^2 dt = \frac{1}{2\pi} \int_{-\infty}^{\infty} |F(\omega)|^2 d\omega
  $$
- **能量谱密度 (Energy Spectral Density, ESD):** $|F(\omega)|^2$ 被称为信号的能量谱密度。它描述了信号能量在不同频率上的分布情况。单位频率间隔内的能量由 $\frac{1}{2\pi}|F(\omega)|^2$ 给出。
- **技术比喻:** 帕塞瓦尔定理就像能量守恒。无论你是在时间维度上测量信号的总能量 (所有时刻能量的总和)，还是在频率维度上测量 (所有频率分量能量的总和)，得到的总能量是相同的。能量谱密度 $|F(\omega)|^2$ 则告诉你，在不同的频率 "频道" 上，信号携带了多少能量。

### 分贝与Bandwidth

#### 分贝
**1. 定义与目的**

分贝 (dB) 本身不是一个单位，而是一个**无量纲的对数标度 (logarithmic scale)**，用于表示两个物理量之间的**比率 (ratio)**。它最常用于表示功率 (power)、强度 (intensity) 或幅度 (amplitude) 的相对大小。

使用对数标度的主要原因有：

1.  **压缩大范围数值:** 信号的功率或幅度可能变化非常大（跨越多个数量级），使用对数可以将其压缩到一个更易于处理和表示的范围。
2.  **简化计算:** 级联系统 (cascaded systems) 的总增益 (gain) 或衰减 (attenuation) 计算，在对数域中可以将乘法/除法转换为加法/减法。
3.  **匹配人类感知:** 人类对声音响度或光线亮度的感知本身就接近于对数关系。

**2. 计算公式**

dB 的计算取决于所比较的物理量是功率量还是场量（如电压、电流、声压）。

1.  **功率比 (Power Ratio):**
    当比较两个功率 $P_1$ 和 $P_0$ 时，其 dB 值为：
    $$
    dB = 10 \log_{10} \left( \frac{P_1}{P_0} \right)
    $$
    这里的 $P_0$ 是**参考功率 (reference power)**。

2.  **幅度/电压比 (Amplitude/Voltage Ratio):**
    当比较两个幅度量（如电压 $V_1$ 和 $V_0$，或电流 $I_1$ 和 $I_0$）时，假设阻抗 (impedance) 不变，功率与幅度的平方成正比 ($P \propto V^2$)。因此，dB 值为：
    $$
    dB = 10 \log_{10} \left( \frac{P_1}{P_0} \right) = 10 \log_{10} \left( \frac{V_1^2 / R}{V_0^2 / R} \right) = 10 \log_{10} \left( \left( \frac{V_1}{V_0} \right)^2 \right) = 20 \log_{10} \left( \frac{V_1}{V_0} \right)
    $$
    这里的 $V_0$ 是**参考电压 (reference voltage)**。

**3. 参考值 (Reference Value)**

使用 dB 时必须有一个参考值 ($P_0$ 或 $V_0$)。这个参考值可以是：

-   **标准参考值:** 如 dBm (参考 1 毫瓦, 1mW)，dBW (参考 1 瓦, 1W)，dBV (参考 1 伏特, 1V)，dBu (参考 0.775 伏特)。
-   **相对参考值:** 比如信号的最大值、系统的输入值、噪声基底等。在滤波器或系统频率响应中，通常将最大响应（例如通带中心）作为 0 dB 参考点。

**4. 常见 dB 值解读**

-   **0 dB:** 表示信号值等于参考值 ($P_1 = P_0$ 或 $V_1 = V_0$)。
-   **+3 dB:** 表示功率大约变为原来的 **2 倍** ($10 \log_{10}(2) \approx 3.01$)。幅度大约变为原来的 $\sqrt{2} \approx 1.414$ 倍 ($20 \log_{10}(\sqrt{2}) \approx 3.01$)。
-   **-3 dB:** 表示功率大约变为原来的 **1/2 倍** ($10 \log_{10}(1/2) \approx -3.01$)。幅度大约变为原来的 $1/\sqrt{2} \approx 0.707$ 倍 ($20 \log_{10}(1/\sqrt{2}) \approx -3.01$)。**这个值在带宽定义中特别重要。**
-   **+10 dB:** 表示功率变为原来的 **10 倍**。
-   **-10 dB:** 表示功率变为原来的 **1/10 倍**。
-   **+20 dB:** 表示功率变为原来的 **100 倍**，幅度变为原来的 **10 倍**。
-   **-20 dB:** 表示功率变为原来的 **1/100 倍**，幅度变为原来的 **1/10 倍**。

**5. 在傅里叶变换和频谱中的应用**

在课程幻灯片中，dB 被用来定义带宽。具体来说，-3dB 点是指信号的**能量谱密度 (Energy Spectral Density, ESD)** $|F(\omega)|^2$ 下降到其最大值（通常是 $|F(0)|^2$）**一半**的位置。
$$
10 \log_{10} \left( \frac{|F(\omega_{3dB})|^2}{|F(0)|^2} \right) = -3 \text{ dB}
$$
这等价于：
$$
\frac{|F(\omega_{3dB})|^2}{|F(0)|^2} = 10^{-3/10} \approx \frac{1}{2}
$$
因为 $|F(\omega)|^2$ 代表能量（类似于功率），所以使用 $10 \log_{10}$ 的形式。

#### 带宽 (Bandwidth, BW)

**1. 定义与目的**

带宽是衡量信号在**频域**中占据的**频率范围**或系统能够有效处理的**频率范围**的指标。它量化了信号频谱的“宽度”或系统频率响应的“宽度”。带宽是通信、信号处理和系统设计中的一个核心概念。

带宽的大小影响：

-   信息传输速率 (Data Rate)
-   信号对噪声和干扰的敏感度
-   系统设计的复杂性和成本

**2. 带宽的种类/定义**

带宽没有唯一的、普遍适用的定义。具体使用哪种定义取决于应用场景和分析目的。以下是一些常见的带宽定义：

1.  **绝对带宽 (Absolute Bandwidth):**
    信号频谱**严格不为零**的整个频率范围。对于许多理论信号（如理想矩形脉冲的 sinc 频谱），绝对带宽是无限的，因此在实际中不常用。

2.  **3dB 带宽 (3dB Bandwidth) 或 半功率带宽 (Half-Power Bandwidth):**
    这是**最常用**的带宽定义，尤其是在滤波器和放大器设计中。它指的是信号的功率谱或能量谱密度下降到其峰值**一半 (-3dB)** 的频率范围。
    -   **对于低通信号 (Low-Pass Signal):** 带宽通常指从 0 Hz (DC) 到功率谱密度下降为峰值一半的正频率 $\omega_{3dB}$ (或 $f_{3dB}$)。即 $BW = \omega_{3dB}$ (或 $f_{3dB}$) [Slide p5, Slide p23]。此时 $|F(\omega_{3dB})|^2 = \frac{1}{2} |F(peak)|^2$，通常 $|F(peak)|^2 = |F(0)|^2$。等效地，幅度谱 $|F(\omega)|$ 下降到峰值的 $1/\sqrt{2}$ (约 0.707)。
    -   **对于带通信号 (Band-Pass Signal):** 带宽指功率谱密度下降到峰值一半的**上边频 (upper cutoff frequency) $\omega_H$** 与**下边频 (lower cutoff frequency) $\omega_L$** 之差。即 $BW = \omega_H - \omega_L$ [Slide p6, Slide p28]。此时 $|F(\omega_H)|^2 = |F(\omega_L)|^2 = \frac{1}{2} |F(peak)|^2$，其中峰值通常出现在中心频率 $\omega_c$ 附近。


3.  **r% 能量带宽 (r% Energy Bandwidth):**
    指包含信号总能量 **r%**（例如 90%, 99%）的频率范围。计算方式是积分能量谱密度 $|F(\omega)|^2$，找到包含所需能量比例的最小频率范围。
    -   对于低通信号，通常是从 $\omega=0$ 算起的对称区间 $[-\Omega_r, \Omega_r]$ (或只考虑正频率 $[0, \Omega_r]$，此时带宽为 $\Omega_r$)。
    -   对于带通信号，通常是关于中心频率 $\omega_c$ 对称的区间 $[\omega_c - \Omega_r/2, \omega_c + \Omega_r/2]$。
    计算公式如所示（针对低通，只考虑正频率）：
    $$
    \frac{1}{2\pi} \int_{0}^{\Omega_r} |F(\omega)|^2 d\omega = \frac{r}{100} \times \frac{W}{2}
    $$
    其中 $W$ 是信号总能量 (参考帕塞瓦尔定理)，这里除以 2 是因为只考虑正频率部分 (假设能量谱偶对称)。



### 能量带宽 (Energy Bandwidth)

能量带宽衡量的是信号能量在频域中集中的程度，即信号的主要频率成分占据了多大的频率范围。

- **概念:** 对于低通信号 (能量主要集中在 $\omega=0$ 附近) 或带通信号 (能量集中在某个 $\pm \omega_c$ 附近)，我们可以定义其带宽。
- **技术比喻:** 带宽就像一条信息高速公路的宽度。带宽越宽，意味着信号包含的频率范围越广，可能传输的信息速率也越高。
- **常见定义:**
    - **3dB 带宽 (3dB Bandwidth):** 对于低通信号，指能量谱密度 $|F(\omega)|^2$ 从最大值下降到其一半 (即下降 3dB) 时的正频率 $\omega_{3dB}$ 。对于带通信号，指能量谱密度包络下降到峰值一半时的频率范围宽度。
    - **r% 能量带宽 (r% Energy Bandwidth):** 指包含信号总能量 r% (例如 99%) 的最小频率范围 $[-\omega_r, \omega_r]$ (对于低通) 或 $[\omega_{c,low}, \omega_{c,high}]$ 及 $[-\omega_{c,high}, -\omega_{c,low}]$ (对于带通)。计算时需要积分能量谱密度，直到达到总能量的 r%。
        - 例如，99% 能量带宽 $\omega_{99\%}$ 满足 (低通情况):
          $$
          \frac{1}{2\pi} \int_{-\omega_{99\%}}^{\omega_{99\%}} |F(\omega)|^2 d\omega = 0.99 \times W = 0.99 \times \frac{1}{2\pi} \int_{-\infty}^{\infty} |F(\omega)|^2 d\omega
          $$
 

## LTI 电路与系统对能量信号的响应 (LTI Circuit and System Response to Energy Signals)

这一部分应用傅里叶变换来分析 LTI 系统对能量信号输入 $f(t)$ 的输出 $y(t)$。

### 核心关系: 频域乘积

- 对于一个 LTI 系统，如果其频率响应 (Frequency Response) 为 $H(\omega)$ (这是系统冲激响应 $h(t)$ 的傅里叶变换)，输入信号为 $f(t)$ (其傅里叶变换为 $F(\omega)$)，则输出信号 $y(t)$ 的傅里叶变换 $Y(\omega)$ 为:
  $$
  Y(\omega) = H(\omega) F(\omega)
  $$
- **说明:** 这个公式是 LTI 系统频域分析的核心。它表明，在频域中，LTI 系统的作用是**将输入信号的每个频率分量 $F(\omega)$ 乘以系统的频率响应 $H(\omega)$**。时域的卷积运算 (Convolution) 在频域变成了简单的乘法运算，这大大简化了分析。
- **技术比喻:** $H(\omega)$ 就像一个音频均衡器 (Equalizer)。它对输入声音 $F(\omega)$ 的不同频率成分进行不同的调整 (增强或减弱，并可能引入延迟/相移)。$Y(\omega)$ 就是经过均衡器调整后的声音频谱。

### 计算输出信号 $y(t)$ 的步骤

要找到 LTI 系统对能量信号输入的时域响应 $y(t)$，通常遵循以下步骤:

1.  **计算输入的傅里叶变换:** 找到输入信号 $f(t)$ 的傅里叶变换 $F(\omega)$。
2.  **频域相乘:** 将 $F(\omega)$ 乘以系统的频率响应 $H(\omega)$，得到输出的傅里叶变换 $Y(\omega) = H(\omega) F(\omega)$。
3.  **计算输出的傅里叶反变换:** 对 $Y(\omega)$ 进行傅里叶反变换，得到时域输出信号 $y(t)$:
    $$
    y(t) = \frac{1}{2\pi} \int_{-\infty}^{\infty} Y(\omega) e^{j\omega t} d\omega = \frac{1}{2\pi} \int_{-\infty}^{\infty} H(\omega) F(\omega) e^{j\omega t} d\omega
    $$


