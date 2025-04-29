---
title: Modulation and AM Radio
date: 2025-04-23
date modified: 2025-04-23
categories: ECE210
tags:
  - ECE210
---

#ECE210 


## 调制 (Modulation)

调制是一种将**信息信号 (信息承载信号，通常是低频信号，如音频)** 加载到**载波信号 (carrier signal，通常是高频正弦波)** 上的过程。

-   **输入信号 (Input Signal / Baseband Signal):** 这就是我们要传输的信息，例如语音、音乐等。它通常处在较低的频率范围 (基带)，例如音频信号的带宽大约在 15 kHz 左右 (Slide 6)。我们用 $f(t)$ 表示这个信号，其傅里叶变换为 $F(\omega)$。
-   **载波信号 (Carrier Signal):** 一个高频的正弦波，例如 $cos(\omega_c t)$，其中 $\omega_c$ 是载波角频率 (carrier angular frequency)，$f_c = \omega_c / (2\pi)$ 是载波频率 (carrier frequency)。这个频率远高于输入信号的最高频率 (Slide 4: $\omega_c \gg \Omega$，其中 $\Omega$ 是 $f(t)$ 的带宽)。
-   **已调信号 (Modulated Signal):** 经过调制过程产生的信号，它承载了输入信号的信息，并且频谱被搬移到了载波频率附近。



## 傅里叶变换的频移特性 (Frequency Shift Property)

这是理解调制原理的关键数学基础。

-   **基本性质:** 如果 $f(t)$ 的傅里叶变换是 $F(\omega)$，那么：
    -   $f(t) e^{j\omega_c t} \leftrightarrow F(\omega - \omega_c)$
    -   $f(t) e^{-j\omega_c t} \leftrightarrow F(\omega + \omega_c)$
    这表示，在时域乘以一个复指数 $e^{j\omega_c t}$，等效于在频域将其频谱 $F(\omega)$ 向右平移 $\omega_c$。乘以 $e^{-j\omega_c t}$ 则是向左平移 $\omega_c$。

-   **调制特性 (Modulation Property):**
    我们通常使用实数载波 $\cos(\omega_c t)$。利用欧拉公式 $\cos(\omega_c t) = \frac{e^{j\omega_c t} + e^{-j\omega_c t}}{2}$，我们可以推导出调制信号 $x(t) = f(t) \cos(\omega_c t)$ 的频谱：
    $$
    x(t) = f(t) \cos(\omega_c t) = f(t) \left( \frac{e^{j\omega_c t} + e^{-j\omega_c t}}{2} \right) = \frac{1}{2} f(t) e^{j\omega_c t} + \frac{1}{2} f(t) e^{-j\omega_c t}
    $$
    对其进行傅里叶变换，利用线性性质和频移特性：
    $$
    X(\omega) = \mathcal{F}\{x(t)\} = \frac{1}{2} F(\omega - \omega_c) + \frac{1}{2} F(\omega + \omega_c)
    $$
    **结论:** 将基带信号 $f(t)$ 乘以载波 $\cos(\omega_c t)$，其效果是**将原始信号的频谱 $F(\omega)$ 左右平移到载波频率 $\pm \omega_c$ 的位置，并且幅度减半**。原始信号的频谱通常集中在 $\omega=0$ 附近 (基带)，调制后则搬移到了 $\pm \omega_c$ 附近 (射频 Radio Frequency, RF)。

## 为什么需要调制 (Why Modulate)? 

主要有两个原因：

1.  **天线长度 (Antenna Length):**
    -   高效发射或接收电磁波的天线长度 $L$ 通常需要与信号波长 $\lambda$ 相当，例如 $L \approx \lambda/4$。
    -   波长 $\lambda = c / f_c$，其中 $c$ 是光速，$f_c$ 是信号频率。
    -   对于低频的基带信号 (如音频 $f_c \approx 15$ kHz)，所需的波长 $\lambda = (3 \times 10^8 \text{ m/s}) / (15 \times 10^3 \text{ Hz}) = 20$ km。天线需要几公里长，这显然不切实际。
    -   通过调制将信号搬移到高频载波 (如 AM 广播 $f_c \approx 1$ MHz)，波长 $\lambda = 300$ m，天线长度 (如 75m) 就变得可以接受了。Slide 6 给出了 AM 电台 WILL (580 kHz) 的例子，所需天线长度 $> 130$m。FM 和卫星通信频率更高，天线更短。
    -   可以认为天线类似于一个**高通滤波器 (High-pass filter)**，它对高频信号的辐射/接收效率更高。

2.  **信道共享/可用带宽 (Available Bandwidth / Channel Sharing):**
    -   如果所有人都直接在基带 (低频) 传输信号，它们的频谱会重叠在一起，互相干扰 (interfere with one another)。
    -   调制允许我们将不同的信号分配到不同的载波频率 $f_c$ 上，就像给每个广播电台分配一个特定的频道一样。这样，在接收端就可以通过滤波器选择想要收听的频道，而不会受到其他电台的干扰。这称为**频分复用 (Frequency Division Multiplexing, FDM)**。
    -   监管机构 (如美国的 FCC, 国际上的 ITU) 会分配特定的频段 (frequency bands) 和频道间隔 (channel spacing)。例如，美国的 AM 广播频段是 540 kHz 到 1700 kHz，频道间隔是 10 kHz (Slide 6, 18)。中国的 AM 频段是 531 kHz 到 1602 kHz，频道间隔是 9 kHz (Slide 6)。

## 幅度调制 (Amplitude Modulation, AM)

AM 是最基本、最早使用的调制方式之一。其核心思想是：**让载波的幅度随着基带信号 $f(t)$ 的变化而变化** ($f(t)$ modulates the Amp. of Carrier signal)。

主要有两种形式：

1.  **双边带抑制载波调幅 (Double Sideband Suppressed Carrier, DSB-SC):**
    -   信号形式: $x_{DSB}(t) = f(t) \cos(\omega_c t)$ (Slide 4, 5, 7)
    -   频谱: $X_{DSB}(\omega) = \frac{1}{2} [F(\omega - \omega_c) + F(\omega + \omega_c)]$
    -   特点: 实现简单 (只需乘法器/混频器 mixer)，但解调相对复杂 (需要相干解调)。频谱中没有单独的载波分量。

2.  **标准调幅 (Standard AM):**
    -   信号形式: $x_{AM}(t) = [A + f(t)] \cos(\omega_c t)$，其中 $A$ 是一个足够大的直流偏置 (DC offset)，使得 $A + f(t) > 0$ 恒成立。
    -   频谱: $X_{AM}(\omega) = \frac{A}{2} [\delta(\omega - \omega_c) + \delta(\omega + \omega_c)] + \frac{1}{2} [F(\omega - \omega_c) + F(\omega + \omega_c)]$
    -   特点: 包含了一个离散的载波分量 (频谱中的两个冲激)。优点是可以使用非常简单的**包络检波 (envelope detection)** 进行解调，使得接收机成本低廉。这是商业 AM 广播采用的方式。缺点是发射功率效率较低，因为大部分功率消耗在传输载波 $A \cos(\omega_c t)$ 上，而不是信息 $f(t)$ 上。

## 解调 (Demodulation) - 恢复原始信号

解调是调制的逆过程，目的是从接收到的已调信号中恢复出原始的基带信号 $f(t)$。主要有两种方法：

### 5.1 相干解调 (Coherent Demodulation / Synchronous Detection) 
适用于 DSB-SC 和 Standard AM。

1.  **原理:** 在接收端，将接收到的信号 $x(t)$ 再次乘以一个与发射端**完全相同频率和相位**的本地载波 $\cos(\omega_c t)$。
    $$
    z(t) = x(t) \cos(\omega_c t) = f(t) \cos(\omega_c t) \cos(\omega_c t) = f(t) \cos^2(\omega_c t)
    $$
2.  **数学推导:** 利用三角恒等式 $\cos^2(\theta) = \frac{1 + \cos(2\theta)}{2}$：
    $$
    z(t) = f(t) \left( \frac{1 + \cos(2\omega_c t)}{2} \right) = \underbrace{\frac{1}{2} f(t)}_{\text{低频项 (基带)}} + \underbrace{\frac{1}{2} f(t) \cos(2\omega_c t)}_{\text{高频项 (围绕 } 2\omega_c \text{ )}}
    $$
3.  **低通滤波 (Low-Pass Filtering, LPF):** 将 $z(t)$ 通过一个低通滤波器 (LPF)，滤除高频项 ($2\omega_c$ 附近的分量)，保留低频项。滤波器的截止频率 $\Omega_{LPF}$ 需要满足 $BW_{f(t)} < \Omega_{LPF} < 2\omega_c$ ($BW_{f(t)}$ 是 $f(t)$ 的带宽)。
4.  **输出:** LPF 的输出即为 $\frac{1}{2} f(t)$，再乘以 2 即可恢复 $f(t)$ 。

**相干解调的挑战:**

-   **相位同步:** 接收端的本地载波 $\cos(\omega_c t)$ 必须与发射端的载波具有完全相同的频率和相位。
-   **信道延迟 (Time Delay):** 如果信道引入延迟 $t_d$，接收信号为 $r(t) = f(t-t_d) \cos(\omega_c(t-t_d))$。如果本地载波是 $\cos(\omega_c t)$，则相乘后 $z'(t) = r(t) \cos(\omega_c t)$。
    使用积化和差公式 $\cos A \cos B = \frac{1}{2}[\cos(A-B) + \cos(A+B)]$：
    $$
    z'(t) = f(t-t_d) \frac{1}{2} [\cos(-\omega_c t_d) + \cos(2\omega_c t - \omega_c t_d)]
    $$
    经过 LPF 后得到: $\frac{1}{2} f(t-t_d) \cos(\omega_c t_d)$。
-   **问题:** 恢复出的信号幅度被乘以了一个因子 $\cos(\omega_c t_d)$。由于 $\omega_c$ 很高，即使 $t_d$ 很小，$\omega_c t_d$ 也可能很大，导致 $\cos(\omega_c t_d)$ 值波动剧烈，甚至可能为 0，使信号丢失！(Slide 9: "small $t_d \rightarrow$ large phase shift $\omega_c t_d$ cause Amp of $f(t-t_d)$ fluctuate")。
-   **解决方案:** 需要复杂的**锁相环 (Phase-Locked Loop, PLL)** 电路来确保接收端本地载波与接收信号中的载波同步。这增加了接收机的复杂度和成本。

### 包络检波 (Envelope Detection)

这是 Standard AM 的常用解调方法，非常简单。

1.  **原理:** 对于 Standard AM 信号 $x_{AM}(t) = [A + f(t)] \cos(\omega_c t)$，如果 $A + f(t) > 0$ 恒成立，那么信号的**包络 (envelope)** 就是 $A + f(t)$。包络检波器直接提取这个包络。
2.  **实现:**
    -   **整流 (Rectification):** 将 AM 信号通过一个非线性器件，通常是**二极管 (diode)**。理想二极管只允许电流单向通过，相当于对信号进行了**半波整流 (half-wave rectification)**。也可以使用**全波整流 (full-wave rectifier)**，相当于取绝对值 (Slide 13, 15 框图中的 $|\cdot|$ )。设整流后信号为 $z(t)$。对于 $x_{AM}(t)$ 且 $A+f(t)>0$，$|x_{AM}(t)| = (A + f(t)) |\cos(\omega_c t)|$。
    -   **低通滤波 (LPF):** 将整流后的信号 $z(t)$ 通过 LPF。
3.  **数学解释:**
    -   $|\cos(\omega_c t)|$ 是一个周期信号，其基频为 $2\omega_c$。它可以展开为傅里叶级数：
        $|\cos(\omega_c t)| = \frac{C_0}{2} + \sum_{n=1}^{\infty} C_n \cos(n 2\omega_c t + \theta_n)$ (其中 $C_0/2 = 2/\pi$ 是直流平均值)
    -   因此，整流后的信号为：
        $z(t) = (A + f(t)) \left( \frac{C_0}{2} + \sum_{n=1}^{\infty} C_n \cos(n 2\omega_c t + \theta_n) \right)$
        $z(t) = \underbrace{\frac{C_0}{2} (A + f(t))}_{\text{低频包络项}} + \underbrace{\sum_{n=1}^{\infty} C_n (A + f(t)) \cos(n 2\omega_c t + \theta_n)}_{\text{高频项 (围绕 } 2\omega_c, 4\omega_c, ... \text{ )}}$
    -   LPF 滤除高频项，保留低频包络项 $\frac{C_0}{2} (A + f(t))$。
    -   再通过隔直电容去除直流分量 $\frac{C_0}{2} A$，并调整增益，即可恢复 $f(t)$。
4.  **关键条件:**
    -   包络检波能正确恢复 $f(t)$ 的前提是包络本身 $[A + f(t)]$ 就代表了 $f(t)$。这要求 $A + f(t) > 0$ **始终成立**。
    -   如果使用 DSB-SC 信号 $x(t) = f(t) \cos(\omega_c t)$，其中 $f(t)$ 可以取负值，那么 $|x(t)| = |f(t)| |\cos(\omega_c t)|$。经过 LPF 后得到的是 $\frac{C_0}{2} |f(t)|$，而不是 $f(t)$ (信号发生失真，负半周被翻转)。
    -   这就是为什么商业 AM 广播要采用 Standard AM (加入大的直流偏置 A)。
5.  **非线性:** 整流器是一个**非线性 (Non linear)** 器件。
6.  **对信道延迟的鲁棒性 (Slide 17):**
    -   如果接收信号为 $r(t) = [A + f(t-t_d)] \cos(\omega_c(t-t_d))$，包络检波器会提取其包络 $A + f(t-t_d)$。
    -   相比相干解调，它对载波的相位 $\omega_c t_d$ 不敏感，只是恢复出的信号有时间延迟 $t_d$。这使得接收机设计大大简化。

## 超外差接收机 (Superheterodyne AM Receiver) (Slide 18-25)


**核心问题:**

-   接收天线会收到很多不同频率的电台信号 (宽带频谱 R(f))。
-   我们需要选择其中一个电台 (例如 580 kHz)，并滤除其他电台信号。这需要一个**可调谐的窄带带通滤波器 (Tunable Narrow Band-Pass Filter)**。
-   在 RF 频率 (几百 kHz 到几 MHz) 直接制作高性能 (高 Q 值、陡峭边沿) 且**可调谐**的窄带 BPF 是非常**困难且昂贵**的 (difficult and expensive)，尤其是在模拟电路中。滤波器的相对带宽 $B/f_c$ 很小，对元件精度、稳定性要求极高。
---


**超外差原理 (Superheterodyne Principle):**

-   **核心思想:** 不直接在原始的 RF 频率 $f_c$ 上进行窄带滤波和主放大，而是先将**所有**接收到的电台信号通过**混频 (Mixing)**，将**所选中的电台**的频率**变换 (heterodyne/shift)** 到一个**固定的、较低的中间频率 (Intermediate Frequency, IF)** $f_{IF}$。
-   **主要优点:**
    -   大部分的**滤波**和**放大**都在这个**固定的 IF** $f_{IF}$ 上进行。
    -   由于 $f_{IF}$ 是固定的 (例如美国 AM 为 455 kHz)，可以设计和制造出**非常高性能、稳定、窄带的 IF 滤波器** (IF-filter)。
    -   由于 $f_{IF}$ 比 $f_c$ 低，设计和制造高增益的**IF 放大器 (IFA)** 也相对容易。

---


**超外差接收机结构与工作流程:**

1.  **天线 (Antenna):** 接收空中所有电台的 RF 信号 $r(t)$。
2.  **预选器 (Pre-selector) / RF 滤波器:** 一个**可调谐的、相对较宽的**带通滤波器 $H_{BPF}(\omega)$。它的中心频率与想要接收的电台频率 $f_c$ 同步调谐。
    -   **作用 1:** 初步选择所需电台 $f_c$ 附近的信号，抑制远离 $f_c$ 的强干扰信号。
    -   **作用 2 (关键):** 抑制**镜像频率 (Image Frequency)** 的干扰 (后面详述)。
3.  **射频放大器 (RF Amplifier, RFA):** 对通过预选器的信号进行初步放大 (可选，Slide 25 有)。
4.  **混频器 (Mixer):** 将 RFA 输出的信号与**本地振荡器 (Local Oscillator, LO)** 产生的信号 $\cos(\omega_{LO} t)$ 相乘。LO 的频率 $\omega_{LO}$ 是**可调的**。
    -   混频器的输出包含**和频** ($\omega_c + \omega_{LO}$) 与**差频** ($|\omega_c - \omega_{LO}|$) 分量。
5.  **本地振荡器 (Local Oscillator, LO):** 产生一个频率可调的正弦信号 $\cos(\omega_{LO} t)$。**调谐旋钮 (Tuning knob)** 同时控制**预选器**的中心频率和**LO**的频率 $f_{LO}$，使得**目标电台 $f_c$** 经混频后，其**差频**始终等于**固定的中频 $f_{IF}$**。
    -   通常采用**高边注入 (high-side injection)**: $f_{LO} = f_c + f_{IF}$ (Slide 20, 24)。
    -   例如，接收 $f_c = 580$ kHz, $f_{IF} = 455$ kHz，则 $f_{LO} = 580 + 455 = 1035$ kHz。
    -   接收 $f_c = 1490$ kHz, $f_{IF} = 455$ kHz，则 $f_{LO} = 1490 + 455 = 1945$ kHz。
6.  **中频滤波器 (IF-filter):** 一个**固定中心频率** ($f_{IF}$)、**窄带宽** (例如 AM 约 10 kHz)、**高性能**的带通滤波器 $H_{IF}(\omega)$。
    -   **作用:** 它只允许频率为 $f_{IF}$ 的信号通过，滤除混频产生的和频分量、其他电台变换后的频率分量等所有干扰。这是接收机**选择性 (selectivity)** 的主要来源。
7.  **中频放大器 (IF Amplifier, IFA):** 对通过 IF 滤波器的**纯净 IF 信号**进行**主要放大 (gain)**。由于工作在固定频率 $f_{IF}$，放大器可以设计得非常稳定且增益很高。
8.  **解调器 (Detector):** 通常是**包络检波器 (Envelope Detector, Env. Det.)**，从放大的 IF 信号中恢复出原始的基带音频信号 $f(t)$。
9.  **音频放大器 (Audio Amplifier, AA):** 对解调出的音频信号 $f(t)$ 进行放大，驱动扬声器 (Speaker) 或耳机。**音量控制 (Volume control)** 通常在此级或之前实现。

---

**镜像频率问题 (Image Frequency Problem):**


混频器的输出包含多个频率分量，主要是**和频** ($f_{RF} + f_{LO}$) 和**差频** ($|f_{RF} - f_{LO}|$)。我们调整 $f_{LO}$，使得我们**想要接收**的电台频率 $f_c$ 产生的**差频**正好等于中频 $f_{IF}$。

即，我们希望：
$$
|f_c - f_{LO}| = f_{IF}
$$
在标准的 AM 接收机中，通常采用**高边注入 (high-side injection)**，即本地振荡器的频率高于接收频率：
$$
f_{LO} = f_c + f_{IF}
$$
这样，差频就是：
$$
f_{LO} - f_c = (f_c + f_{IF}) - f_c = f_{IF}
$$
这个 $f_{IF}$ 信号会被后续的**中频滤波器 (IF Filter)** 选中并通过。


问题在于，混频器是一个“盲目”的数学运算器件 (乘法器)。它并不知道哪个输入频率是我们想要的 $f_c$。它会对**所有**进入混频器的 RF 频率 $f_{RF}$ 都执行 $f_{LO} \pm f_{RF}$ 的运算。

现在考虑，是否存在**另一个**不同于 $f_c$ 的输入频率，我们称之为**镜像频率 ($f_{IM}$)**，它在与**同一个** $f_{LO}$ 混频后，产生的**差频也恰好是 $f_{IF}$**？

是的，存在！我们需要找到 $f_{IM}$ 使得：
$$
|f_{IM} - f_{LO}| = f_{IF}
$$
使用我们选择的 $f_{LO} = f_c + f_{IF}$，代入上式：
$$
|f_{IM} - (f_c + f_{IF})| = f_{IF}
$$
这有两种可能：

1.  $f_{IM} - (f_c + f_{IF}) = f_{IF}$
    $\implies f_{IM} = f_c + f_{IF} + f_{IF}$
    $\implies \boxed{f_{IM} = f_c + 2f_{IF}}$

2.  $f_{IM} - (f_c + f_{IF}) = -f_{IF}$
    $\implies f_{IM} = f_c + f_{IF} - f_{IF}$
    $\implies f_{IM} = f_c$ (这正是我们想要接收的频率)

**结论:**
除了我们想要接收的频率 $f_c$ 之外，还有一个频率 $f_{IM} = f_c + 2f_{IF}$，当它进入混频器时，也会被转换成中频 $f_{IF}$！
$$
|f_{IM} - f_{LO}| = |(f_c + 2f_{IF}) - (f_c + f_{IF})| = |f_{IF}| = f_{IF}
$$
这个 $f_{IM}$ 就叫做**镜像频率 (Image Frequency)**。

---

**如何解决镜像频率问题？**

解决这个问题的关键在于：**必须在信号进入混频器之前，就将镜像频率 $f_{IM}$ 的信号尽可能地滤除掉**。

这就是**预选器 (Pre-selector)** 或**射频滤波器 (RF Filter)** 的作用。它位于天线之后、混频器之前 (Slide 25 中的 $H_{BPF}(\omega)$)。

-   **功能:** 预选器是一个**可调谐**的带通滤波器，其中心频率与你想要接收的电台频率 $f_c$ **同步调谐**。
-   **要求:**
    -   它需要有足够的**带宽**来通过整个想要的信号频道 (例如 AM 约 10 kHz)。
    -   但同时，它必须对**镜像频率 $f_{IM} = f_c + 2f_{IF}$** 提供足够的**衰减 (Attenuation)**。
-   **带宽权衡:**
    -   预选器的带宽通常比 IF 滤波器宽得多。它不需要像 IF 滤波器那样精确地只选择一个频道。
    -   它的主要任务是**抑制**强干扰信号，尤其是**镜像频率**的信号。
    -   预选器的性能（即抑制镜像频率的能力）直接影响接收机的**镜像抑制比 (Image Rejection Ratio)**，这是一个衡量接收机质量的重要指标。

**例子 (Slide 21, 22):**

-   接收 $f_c = 580$ kHz (WILL 电台)。$f_{IF} = 455$ kHz。
-   镜像频率 $f_{IM} = 580 + 2 \times 455 = 1490$ kHz。
-   当你将收音机调谐到 580 kHz 时，预选器也必须调谐到以 580 kHz 为中心。它需要通过 580 kHz 附近的信号，但要**尽力阻止** 1490 kHz 的信号进入混频器。
-   预选器的带宽需要足够宽以覆盖 580 kHz 频道，但又需要足够窄（或者说滚降足够陡峭），以便在 1490 kHz 处有足够的衰减。

**中频 $f_{IF}$ 的选择与镜像抑制的关系:**

-   镜像频率与目标频率的间隔是 $f_{IM} - f_c = 2f_{IF}$。
-   如果选择的**中频 $f_{IF}$ 越高**，那么镜像频率 $f_{IM}$ 就离目标频率 $f_c$ **越远**。
-   频率间隔越大，对于预选器来说，就**越容易**将 $f_{IM}$ 滤除掉，即可以获得更好的镜像抑制效果。
-   但是，选择过高的 $f_{IF}$ 又会使得设计高性能、稳定的 IF 滤波器和放大器变得更困难。
-   因此，中频 $f_{IF}$ 的选择是一个**权衡 (trade-off)**。455 kHz 是历史悠久且广泛用于 AM 广播接收机的标准中频值。


---
**LO 频率选择 (Slide 24):**

-   选择 $f_{LO} = f_c + f_{IF}$ (高边注入) 还是 $f_{LO} = f_c - f_{IF}$ (低边注入)？
-   对于 AM 波段 (540-1700 kHz) 和 $f_{IF}=455$ kHz：
    -   高边注入: $f_{LO} \in [995, 2155]$ kHz。频率范围比 $f_{LO,max}/f_{LO,min} \approx 2.16$。
    -   低边注入: $f_{LO} \in [85, 1245]$ kHz。频率范围比 $f_{LO,max}/f_{LO,min} \approx 14.6$。
-   **结论:** 制造一个频率调谐范围比约为 2 的振荡器比范围比约为 15 的振荡器要容易得多且性能更稳定。因此，**AM 接收机通常采用高边注入 $f_{LO} = f_c + f_{IF}$**。

