---
title: Phasors and Sinusoidal Steady State
date: 2025-03-21
date modified: 2025-03-31
categories: ECE210
tags: [ECE210]
---

#ECE210

## Phasors, Co-Sinusoids, and Impedance

### Phasors and co-sinusoids

![7048a65aefdfba0a01cf9df1d1be48d.png](https://s2.loli.net/2025/03/23/5PhtsbnepzEwGWy.png)  
**相关参数**
- Amplitude 振幅: |F|
- Phase 相位: $\omega t+\theta$
- Phase shift： $\theta= \angle F$
- Radian frequency 角频率: $\omega$

$$
F = Ae^{j\theta}
$$

sin 信号的相位与 cos 信号的相位转换

$$
|F|\sin(\omega t+\phi) = |F|\cos \left( \omega t+\phi- \frac{\pi}{2} \right)
$$

即

$$
|F|e^{j(\phi-\pi/2)} = -j |F|e^{j\phi}
$$

直接将 sin 对应的相位减去 $\frac{\pi}{2}$ 即可得到对应的 cos 相位

所有输入的角频率相同的正余弦信号都可以简化为如下通式:

$$
\mathrm{Re}\{Fe^{j\omega t}\}
$$

### Superposition and derivatives of co-sinusoids

- **线性和**  
直接做正常的复数加法即可，实部加实部，虚部加虚部

![d1bd81c82ee72c4bba7edeceb20781a.png](https://s2.loli.net/2025/03/23/6GUE9Tt5JDnPwoW.png)

- **Derivative Principle**  
![3332925e2b797da87dc4a592a543307.png](https://s2.loli.net/2025/03/23/wOrnEb8ZvqxWFM6.png)  
Example：直接根据结果猜测可能的角频率并转化未相位的计算

$$
\frac{df}{dt} +4f(t) = 2\cos(4t)
$$

![1afcde5ac2522a8167f13b144b23c2b.png](https://s2.loli.net/2025/03/23/xP19ZLMD7JCRfQq.png)

### V-I Phase Relation

![f81d23be302fd844f236c9b9d24d77b.png](https://s2.loli.net/2025/03/23/qg2UIHCNBEtjxMi.png)

### Impedance and phasor method

![445528d3c421633a5ca8dc27148925c.png](https://s2.loli.net/2025/03/23/KIJqzuFbCoNrWec.png)

**一般步骤**
- 将电路中的电容电感元件换为对应的阻抗元件，其中角频率由电源决定
- 根据 KCL,KVL 列方程
- 将解得的相位结果转化为 sin cos

## Sinusoidal Steady-State Analysis

### Impedance combinations and voltage and current division

**Imepedance Combinations->原来的串并联规律依然适用,对复数也适用**

![fd9cfeef4f4a89f5a01bcac7c4f43ee.png](https://s2.loli.net/2025/03/23/VbdmevM8f6gto92.png)

**分压与分流 ->也遵循原来的规律**  
![911afe749fd10560f7640262f1ad241.png](https://s2.loli.net/2025/03/23/tU5KbHCsE7iD2O1.png)

### Source Transformation and Superposition Method

对于电压电流的稳态，我们依然有:

$$
V_{s} = Z_{s}I_{s} \equiv I_{s} = \frac{V_{s}}{Z_{s}}
$$

我们可以用下图展示例子中的转化等效过程:  
![41b91604016cc51b5863ca6b8fd570f.png](https://s2.loli.net/2025/03/23/DArVsj7x8SKnQMX.png)

**注意计算电路中的总电压总电流时 ->对于 independent sources 我们可以直接单独关注其对整体电路的影响**


![6183c90bcac9523a8ba34570f3b53ac.png](https://s2.loli.net/2025/03/23/1U5NZJS2np4KzcY.png)

### Tip

注意区分 Steady State Response, Transient State Respone, Zero-input Response, Zero-state Response  
[[Circuits for Signal Processing#Response Summary]]  
一些可以考虑的小技巧  
**1. 基本关系**

总响应 = Zero-State Response + Zero-Input Response  (线性系统)  
总响应 = Transient Response + Steady-State Response  (线性系统)

**2. 计算**  
steady-state: 即为微分方程的特解，可以通过 phase 求解  
zero-state: 考虑初始电压或电流为 0 代入初值，然后通过给 steady state 加上一个待定系数的衰减指数函数求解  
zero-input：直接根据电路结构计算时间常数即可  
transient-state: 计算出总相应后直接减去 steady-state

## Average and Available Power

对于处于 sinusoidal steady-state 状态下的电路，其中每个元件所吸收的能量为:

$$
p(t) = v(t)i(t)
$$

但此为瞬时能量，净吸收的能量我们用瞬时能量在时间周期内的均值来计算。

$$
P = \frac{1}{T} \int_{t=0}^{T}v(t)i(t)dt 
$$

### Average Power - Phasor

![3bc125187cb6254eb08c2f878805062.png](https://s2.loli.net/2025/03/31/6xyJpn5h4EjsNIT.png)

$$
P = \frac{1}{2}\mathrm{Re}\{VI^{*}\}
$$

**对于纯电阻电路**

$$
P = \frac{1}{2}\mathrm{Re}\{RII^{*}\} = \frac{R|I|^{2}}{2} = \frac{|V|^{2}}{2R}
$$

 或者

$$
P = RI_{rms}^{2} = \frac{V^{2}_{rms}}{R}
$$

**对于电阻与电感 ->平均功率为 0**  
![62ccd8a6dfa8f4ff7902ebaff99dd22.png](https://s2.loli.net/2025/03/31/9bamAg4TYj56P7D.png)

### Available Power and Maximum Power Transfer

我们关注一个线性、sinusoidal steady state 网络能给外界负载传递多少能量  
![465331cf448cf31a8cee1077fc7cd6d.png](https://s2.loli.net/2025/03/31/Dz2gtRNF8Gjc7rX.png)

经过化简，我们可以得出，当外界负载满足：

$$
\begin{align}
& X_{L} = -X_{T} \\
& R_{L} = R_{T}
\end{align}
$$

电路传递给负载的功率有最大值 (即 $Z_{L} =Z_{T}^{*}$)  
此时

$$
P_{a} = \frac{|V_{T}|^{2}}{8R_{T}}
$$

## Resonance

**1. Non-dissipative elements->不需要外界电源也能通过共振维持稳态**  
![33cb1c7308ed84306d9eabc33672d55.png](https://s2.loli.net/2025/03/31/orxgvD4dPYeQcEB.png)

$$
\left( j\omega L + \frac{1}{j\omega C} \right)I = 0
$$

由此得出

$$
\begin{align}
& \omega = \frac{1}{\sqrt{ LC }} =\omega_{0} \\
& i(t) = \mathrm{Re}\{Ie^{j\omega_{0}t}\} = |I|\cos(\omega_{0}t+\theta) \\
& v(t) = \mathrm{Re}\left\{ \frac{I}{j\omega_{0}C}e^{j\omega_{0}t} \right\} = \frac{|I|}{\omega_{0}C}\sin(\omega_{0}+\theta)
\end{align}
$$

**2. Dissipative Elements->需要外界电源**

对于 RLC 电路，当处于共振状态下 ( $\omega_{0} =\frac{1}{\sqrt{ LC }}$ ), 电阻与电感的等效电阻为 0，此时可以等效为短路，对于外界电压响应的电流最大或者对于外界电流相应的电压最大

![4e2ede5fdf2109013e37bf60aa5a0db.png](https://s2.loli.net/2025/03/31/et8flOU92SFgqEm.png)
