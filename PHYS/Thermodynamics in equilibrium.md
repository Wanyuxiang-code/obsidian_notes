---
title: Thermodynamics in equilibrium
date: 2025-04-15
date modified: 2025-04-15
categories: PHYS213
tags:
  - PHYS213
---

#PHYS213


## Lecture 1: Equilibrium, Entropy, and Energy (平衡、熵与能量)

这是我们正式进入热物理学习的第一讲，核心概念是 **熵 (Entropy)**。

### 为什么需要新概念？(Why Need a New Concept?)

-   我们知道能量是守恒的 (Energy is conserved) - 这就是 **热力学第一定律 (The First Law of Thermodynamics)**。
-   但是，第一定律无法告诉我们能量流动的方向。例如，热量总是自发地从热物体流向冷物体，而不是反过来，即使反过来能量也是守恒的。
-   我们需要一个新的物理量来解释过程的方向性。这个量就是 **熵 (Entropy)**。
-   **热力学第二定律 (The Second Law of Thermodynamics)** 指出：在一个孤立系统中，**总熵永远是增加的 (Total entropy always increases)**。
-   本课程的主要目标就是理解熵及其应用，例如解释为什么热量必须从热传递到冷。

### 宏观态与微观态 (Macrostate vs. Microstate)

-   **宏观态 (Macrostate):** 描述系统整体性质的一组我们关心的变量，例如体积 (volume, V)、压强 (pressure, p)、温度 (temperature, T)、内能 (internal energy, U)、粒子数 (number of particles, N) 等。我们通常可以**直接测量宏观量**。
-   **微观态 (Microstate):** 描述系统中所有微观粒子 (原子、分子) 的具体状态，例如每个粒子的精确位置 (position) 和速度 (velocity)。微观态的数量极其庞大。

-   **技术比喻 (Analogy):** 想象一下摇两个骰子。
    -   *宏观态* 就是你关心的 **总点数** (例如 7 点)。
    -   *微观态* 就是两个骰子 **具体的点数组合** (例如 {1, 6}, {2, 5}, {3, 4}, {4, 3}, {5, 2}, {6, 1})。
    -   对于“总点数为 7”这个宏观态，有 6 种不同的微观态与之对应。

### 熵的定义 (Definition of Entropy)

-   熵 $S$ 是与某个宏观态对应的 **微观态数量 $\Omega$** 的量度。其数学定义是 **玻尔兹曼公式 (Boltzmann's formula)**:
    $$
    S = k \ln \Omega
    $$
    -   $k$ 是 **玻尔兹曼常数 (Boltzmann constant)** ($k \approx 1.38 \times 10^{-23}$ J/K)。
    -   $\Omega$ (Omega) 是对应于该**宏观态的微观态的数量 (number of microstates)**。$\Omega$ 通常是一个巨大的数字。
    -   取对数 ($\ln$) 是为了让熵具有 **可加性 (additivity)**。如果系统由两个独立的子系统 1 和 2 组成，总微观态数 $\Omega_{tot} = \Omega_1 \times \Omega_2$，那么总熵 $S_{tot} = k \ln(\Omega_1 \Omega_2) = k \ln \Omega_1 + k \ln \Omega_2 = S_1 + S_2$。这使得处理复杂系统更加方便。

### 熵与概率 (Entropy and Probability)

-   **基本假设:** 在一个孤立系统达到 **热平衡 (thermal equilibrium)** 时，所有可能的微观态都是 **等概率 (equally likely)** 出现的。

-   **推论:** 观察到某个宏观态 $A$ 的概率 $P(A)$ 正比于其对应的微观态数目 $\Omega(A)$。
    $$
    P(A) = \frac{\Omega(A)}{\Omega_{total}}
    $$
    其中 $\Omega_{total}$ 是系统所有可能的微观态的总数。
-   **核心结论:** **最容易出现的 (最可能的) 宏观态是熵最大的那个宏观态 (The most probable macrostate is the one with the highest entropy)**。因为熵越大，意味着 $\Omega$ 越大，对应的微观态越多，系统随机演化时“撞上”这个宏观态的可能性就越大。

### 熵与平衡 (Entropy and Equilibrium)

-   系统总是趋向于熵增加的方向演化。当系统达到 **平衡 (Equilibrium)** 时，它会处于熵最大的那个宏观态。
-   **寻找平衡态的策略 (Strategy to find equilibrium):**
    1.  计算系统的熵 $S$ 作为宏观态变量 (例如体积 $V_1$) 的函数。
    2.  找到使熵 $S$ 最大化的那个变量值，该值就对应平衡态。

-   **例子：体积交换平衡 (Equilibrium of Volume Exchange)** (Slides 20-22)
    -   考虑一个盒子被一个可移动的隔板分成两部分 $V_1$ 和 $V_2$ ($V = V_1 + V_2$)，分别装有 $N_1$ 和 $N_2$ 个粒子 ($N = N_1 + N_2$)。隔板可以移动，改变 $V_1$ (从而也改变了 $V_2$)。
    -   目标: 找到平衡时 $V_1$ 的值。
    -   假设单位体积内容纳的微观态数量由 $n_T$ 描述 (Slide 20 的 $n_T = 1/V_0$ 可能指一个基本的体积单元，或者更广义地理解为每个粒子在单位体积内的状态数密度)。一个粒子在体积 $V_1$ 中的微观态数 $\propto V_1$。对于 $N_1$ 个独立粒子，微观态数 $\Omega_1 \propto V_1^{N_1}$。更精确地，幻灯片给出 $\Omega_1 = (n_T V_1)^{N_1}$ 和 $\Omega_2 = (n_T V_2)^{N_2}$。（这里的 $n_T$ 可能包含动量空间的贡献，但在体积交换问题中我们主要关心体积依赖性）。
    -   总微观态数 $\Omega_{tot} = \Omega_1 \Omega_2 = (n_T V_1)^{N_1} (n_T V_2)^{N_2} = (n_T)^N V_1^{N_1} (V-V_1)^{N_2}$。
    -   为了方便计算，最大化 $\ln \Omega_{tot}$ (这等价于最大化 $S_{tot}$):
        $$
        \ln \Omega_{tot} = N \ln n_T + N_1 \ln V_1 + N_2 \ln(V-V_1)
        $$
    -   求导数并令其为零来找极值：
        $$
        \frac{d (\ln \Omega_{tot})}{d V_1} = \frac{N_1}{V_1} + N_2 \frac{1}{V-V_1}(-1) = \frac{N_1}{V_1} - \frac{N_2}{V_2} = 0
        $$
    -   平衡条件是:
        $$
        \frac{N_1}{V_1} = \frac{N_2}{V_2}
        $$
        这意味着两边的 **粒子数密度 (particle density)** 相等。
    -   从熵的角度看，平衡条件是 $\frac{d S_{tot}}{d V_1} = 0$，这等价于 $\frac{d S_1}{d V_1} + \frac{d S_2}{d V_1} = 0$。因为 $V_2 = V - V_1$，所以 $dV_2 = -dV_1$。因此 $\frac{d S_2}{d V_1} = \frac{d S_2}{d V_2} \frac{dV_2}{d V_1} = -\frac{d S_2}{d V_2}$。平衡条件变为：
        $$
        \left(\frac{\partial S_1}{\partial V_1}\right)_{U_1, N_1} = \left(\frac{\partial S_2}{\partial V_2}\right)_{U_2, N_2}
        $$
        (这里使用偏导数更严谨，因为熵还可能依赖于能量 U 和粒子数 N，在体积交换过程中它们可能保持不变)。这说明平衡时，熵随体积的变化率在两边是相等的。
    -   对于理想气体，我们知道 $p = \frac{NkT}{V}$。如果两边温度 $T$ 相同，那么 $N/V$ 相等意味着压强 $p$ 相等。这与我们的直觉相符：隔板在两边压强相等时达到平衡。

### Lecture 1 总结

-   熵 $S = k \ln \Omega$ 是理解热现象方向性的关键。
-   系统自发趋向于熵最大的宏观态，也就是最可能出现的宏观态。
-   平衡态可以通过最大化系统的总熵来找到。
-   当两个系统可以交换体积时，平衡条件是 $\frac{N_1}{V_1} = \frac{N_2}{V_2}$ (密度相等)，或者更普遍地 $\frac{\partial S_1}{\partial V_1} = \frac{\partial S_2}{\partial V_2}$。

## Lecture 2: Work, Heat, and Temperature (功、热量与温度)

这一讲我们引入了热力学第一定律的具体形式，并给出了温度的热力学定义。

### 热力学第一定律 (First Law of Thermodynamics)

-   这是能量守恒定律在热力学系统中的表述。
-   公式：
    $$
    \Delta U = Q + W_{on}
    $$
    或者
    $$
    \Delta U = Q - W_{by}
    $$
    -   $U$ 是系统的 **内能 (Internal Energy)**：系统内部所有微观粒子动能和势能的总和 (包括平动、转动、振动等)。内能是一个 **状态函数 (state function)**，只取决于**系统的当前宏观状态 (N, V, T 等)，与如何达到该状态的历史路径无关**。
    -   $Q$ 是 **热量 (Heat)**：由于温差而传递的能量。$Q > 0$ 表示系统吸收热量，$Q < 0$ 表示系统放出热量。
    -   $W$ 是 **功 (Work)**：系统与外界通过宏观位移 (例如体积改变) 交换的能量。
        -   $W_{on}$ 是 **外界对系统做的功 (work done on the system)**。当系统被压缩时 ($V$ 减小)，$W_{on} > 0$。
        -   $W_{by}$ 是 **系统对外界做的功 (work done by the system)**。当系统膨胀时 ($V$ 增大)，$W_{by} > 0$。
        -   注意两者关系：$W_{by} = -W_{on}$。选择哪个公式取决于习惯，但要保持一致。
    -   $Q$ 和 $W$ 都不是状态函数，而是 **过程量 (process quantities)**，它们的值依赖于系统从初始态到最终态所经历的具体路径。


### 功的计算 (Calculating Work)

-   对于气体在准静态过程中 (过程进行得足够慢，系统随时近似处于平衡态) 体积从 $V_i$ 变化到 $V_f$，系统对外做的功为：
    $$
    W_{by} = \int_{V_i}^{V_f} p dV
    $$
    在 p-V 图上，这等于曲线下的面积。
-   如果体积不变 ($dV = 0$)，则 $W = 0$。
-   如果压强恒定 ($p = \text{const}$)，则 $W_{by} = p (V_f - V_i)$。

### 热量 (Heat)

-   热量 $Q$ 是因温差导致的能量传递。
-   需要区分热量 $Q$ 和 内能 $U$。$Q$ 是能量的 *流动*， $U$ 是系统 *拥有* 的能量。

### 温度的热力学定义 (Thermodynamic Definition of Temperature)

-   回顾 Lecture 1：当两个只能交换能量的系统达到热平衡时，它们的 $\frac{\partial S}{\partial U}$ 相等。
-   这启发我们将温度 $T$ 定义为与 $\frac{\partial S}{\partial U}$ 相关的量。定义 **绝对温度 (Absolute Temperature)** $T$ (单位：开尔文 K) 如下：
    $$
    \frac{1}{T} \equiv \left( \frac{\partial S}{\partial U} \right)_{V, N}
    $$
    (偏导数是在体积 $V$ 和粒子数 $N$ 保持不变的条件下进行的)。
-   **意义：**
    1.  这个定义保证了在热平衡时，**相互接触的系统具有相同的温度** ($T_1 = T_2$)。
    2.  它解释了热量流动的方向：能量倾向于从 $T$ 高 (即 $\partial S/\partial U$ 小) 的地方流向 $T$ 低 (即 $\partial S/\partial U$ 大) 的地方，以使得总熵最大化。
    3.  **从 $S(U)$ 曲线的形状来看 (通常是向上凸的，即二阶导数小于 0)**，可以推断出 $T$ 通常是正的，并且 $(\partial T / \partial U)_V > 0$ (即增加能量会升高温度)。Slide 12 展示了 $dS/dU < 0$ (对应 $T < 0$) 或 $dS/dU$ 随 $U$ 增加而增加 (对应 $T$ 随 $U$ 增加而减少) 的情况是不符合物理现实的 (至少对于常见系统)。

### 热容 (Heat Capacity)

-   **热容 (Heat Capacity)** $C$ 定义为使系统温度升高 1K 所需吸收的热量。更精确地，是吸收热量与温度变化率之比：
    $$
    C = \frac{dQ}{dT}
    $$
    单位是 J/K。
-   热容的值取决于加热过程是如何进行的，特别是体积或压强是否保持不变：
    -   **定容热容 (Heat Capacity at Constant Volume)** $C_V$: 在体积不变 ($W=0$) 的条件下测量。此时 $dQ = dU$ (根据第一定律)。
        $$
        C_V = \left( \frac{\partial U}{\partial T} \right)_V
        $$
    -   **定压热容 (Heat Capacity at Constant Pressure)** $C_P$: 在压强不变的条件下测量。此时系统可能会膨胀做功 $W_{by} = p dV$。$dQ = dU + p dV$。
        $$
        C_P = \left( \frac{\partial Q}{\partial T} \right)_p
        $$
        对于大多数物质，加热时会膨胀 ($dV > 0$)，需要额外的能量来做功，所以通常 $C_P > C_V$。
-   还有 **比热容 (specific heat capacity)** $c$ (单位质量的热容，J/(kg·K)) 和 **摩尔热容 (molar heat capacity)** $C_{mol}$ (单位摩尔的热容，J/(mol·K))。

### 潜热 (Latent Heat)

-   在 **相变 (phase transition)** 过程中 (例如冰融化成水，水蒸发成汽)，系统吸收或放出热量，但温度保持不变。这部分热量称为 **潜热 (Latent Heat)** $L$。
-   例如，熔化热 (heat of fusion)、汽化热 (heat of vaporization)。
-   **在相变过程中，由于 $dT=0$ 但 $dQ \neq 0$，热容 $C = dQ/dT$ 是无限大的。**

### 熵、温度与热容的关系 (Relation between S, T, C_V)

-   我们可以通过 $C_V$ 和 $T$ 来计算熵的变化。考虑一个定容过程：
    -   我们有 $dS = \left( \frac{\partial S}{\partial T} \right)_V dT$。
    -   利用链式法则：$\left( \frac{\partial S}{\partial T} \right)_V = \left( \frac{\partial S}{\partial U} \right)_V \left( \frac{\partial U}{\partial T} \right)_V$。
    -   根据定义，$\left( \frac{\partial S}{\partial U} \right)_V = \frac{1}{T}$ 且 $\left( \frac{\partial U}{\partial T} \right)_V = C_V$。
    -   所以，$\left( \frac{\partial S}{\partial T} \right)_V = \frac{C_V}{T}$。
-   积分可得定容过程中从温度 $T_0$ 到 $T_f$ 的熵变：
    $$
    \Delta S = S(T_f) - S(T_0) = \int_{T_0}^{T_f} \frac{C_V(T)}{T} dT
    $$
-   类似地，也可以推导出定压过程的熵变公式 (涉及 $C_P$)。

### Lecture 2 总结

-   热力学第一定律 $\Delta U = Q + W_{on}$ 是能量守恒。$U$ 是状态函数，$Q, W$ 是过程量。
-   温度由熵相对于能量的变化率定义: $1/T = (\partial S / \partial U)_V$。平衡时 $T$ 处处相等。
-   热容 $C = dQ/dT$ 描述物体温度随吸热的变化。$C_V = (\partial U / \partial T)_V$。
-   熵变可以通过热容计算: $\Delta S = \int (C_V/T) dT$ (定容)。
-   所有这些概念 (U, S, T, Q, W, C) 紧密联系在一起。

## Lecture 3: Ideal Gas, Equipartition, Heat Capacity (理想气体、能量均分与热容)

### 理想气体 (Ideal Gas)

-   **微观模型 (Microscopic Model):**
    -   由大量分子组成，分子自身体积可忽略 (点粒子)。
    -   分子间除碰撞外无相互作用力 (没有势能)。
    -   分子做随机运动，与器壁的碰撞是弹性的。
-   **宏观性质:** 满足 **理想气体状态方程 (Ideal Gas Law):**
    $$
    pV = NkT
    $$
    或者
    $$
    pV = nRT
    $$
    -   $N$ 是分子数，$n$ 是摩尔数。
    -   $k$ 是玻尔兹曼常数，$R = N_A k$ 是 **通用气体常数 (universal gas constant)** ($R \approx 8.314$ J/(mol·K))，$N_A$ 是 **阿伏伽德罗常数 (Avogadro constant)** ($N_A \approx 6.022 \times 10^{23}$ mol⁻¹)。

### 压强的微观解释 (Kinetic Theory of Pressure)

-   气体压强源于大量分子不断碰撞器壁产生的持续冲量。
-   推导结果 (Slide 8):
    $$
    p = \frac{2}{3} \frac{N}{V} \langle KE_{trans} \rangle
    $$
    -   $\langle KE_{trans} \rangle = \frac{1}{2} m \langle v^2 \rangle$ 是单个分子的 **平均平动动能 (average translational kinetic energy)**。
    -   这个公式将宏观量 $p$ 与微观量 $\langle KE_{trans} \rangle$ 联系起来。

### 能量均分定理 (Equipartition Theorem)

-   **定理内容:** 在温度为 $T$ 的热平衡状态下，能量中每一个 **二次型自由度 (quadratic degree of freedom)** 对系统平均能量的贡献是 $\frac{1}{2}kT$。
    -   **二次型自由度** 指的是能量表达式中包含某个**坐标或动量平方项的形式**，例如：
        -   平动动能: $\frac{1}{2}mv_x^2$, $\frac{1}{2}mv_y^2$, $\frac{1}{2}mv_z^2$ (共 3 个)
        -   转动动能: $\frac{1}{2}I_x\omega_x^2$, $\frac{1}{2}I_y\omega_y^2$ (对于线性分子，绕轴转动忽略不计，通常有 2 个；对于非线性分子有 3 个)
        -   谐振子势能: $\frac{1}{2}kx^2$ (1 个)
        -   谐振子动能: $\frac{1}{2}mv_x^2$ (1 个)
    -   **重要:** 像重力势能 $mgh$ 这种不是坐标或动量的二次方项，就不符合均分定理。
    -   均分定理的严格证明需要用到更深入的统计力学知识 (后续课程会涉及)。

-   **应用:**
    -   **单原子理想气体:** 只有 3 个平动自由度。每个原子平均能量 $U_{atom} = 3 \times (\frac{1}{2}kT) = \frac{3}{2}kT$。总内能 $U = N \times U_{atom} = \frac{3}{2}NkT$。
    -   **双原子理想气体 (刚性转子):** 3 个平动 + 2 个转动自由度 (绕键轴转动忽略)。每个分子平均能量 $U_{molecule} = (3+2) \times (\frac{1}{2}kT) = \frac{5}{2}kT$。总内能 $U = \frac{5}{2}NkT$。 (注：在低温下转动会被“冻结”，高温下振动会被“激活”，导致自由度数变化)。
    -   **非线性多原子理想气体 (刚性转子):** 3 个平动 + 3 个转动自由度。$U_{molecule} = (3+3) \times (\frac{1}{2}kT) = 3kT$。总内能 $U = 3NkT$。
    -   **固体 (原子在晶格中振动):** 每个原子有 3 个方向的振动，每个方向包含 1 个动能自由度 ($\frac{1}{2}mv^2$) 和 1 个势能自由度 ($\frac{1}{2}kx^2$)。总共 $3 \times (1+1) = 6$ 个自由度。每个原子平均能量 $U_{atom} = 6 \times (\frac{1}{2}kT) = 3kT$。总内能 $U = 3NkT$ (Dulong-Petit 定律)。

-   **理想气体内能 (Internal Energy of Ideal Gas):** 对于有 $\alpha$ 个二次型自由度的分子组成的理想气体 (这里 $\alpha$ 是 Slide 17 中的 `a` 乘以 2，即 $N_{DOF}$)，其内能为:
    $$
    U = N \times \alpha \times (\frac{1}{2}kT) = \frac{\alpha}{2} NkT = \frac{N_{DOF}}{2} NkT
    $$
    (注意: Slide 13, 17 中的 $\alpha$ 指的是 $\frac{N_{DOF}}{2}$，这与自由度 $N_{DOF}$ 不同，使用时需注意区分。)
    -   由于理想气体分子间无势能，其内能仅取决于温度 $T$ (和自由度)。

### 理想气体的热容 (Heat Capacity of Ideal Gas)

-   **定容热容 $C_V$:**
    $$
    C_V = \left( \frac{\partial U}{\partial T} \right)_V = \frac{\partial}{\partial T} \left( \frac{N_{DOF}}{2} NkT \right) = \frac{N_{DOF}}{2} Nk = \frac{N_{DOF}}{2} nR
    $$
    -   单原子气体 ($N_{DOF}=3$): $C_V = \frac{3}{2}Nk$。
    -   双原子气体 ($N_{DOF}=5$, 室温): $C_V = \frac{5}{2}Nk$。
    -   固体 ($N_{DOF}=6$): $C_V = 3Nk$。
    -   对于理想气体，在自由度数目不变的温度范围内，$C_V$ 是一个常数。

-   **定压热容 $C_P$:**
    -   对于任何满足 $U$ 只依赖于 $T$ 的系统 (例如理想气体)，可以证明一个普适关系 (用到第一定律和 $pV=NkT$):
        $$
        C_P = C_V + Nk = C_V + nR
        $$
    -   所以，$C_P = \left( \frac{N_{DOF}}{2} + 1 \right) Nk = \left( \frac{N_{DOF}}{2} + 1 \right) nR$。

-   **热容比 (Heat Capacity Ratio) $\gamma$ (伽马):**
    $$
    \gamma = \frac{C_P}{C_V} = \frac{(\frac{N_{DOF}}{2} + 1) Nk}{\frac{N_{DOF}}{2} Nk} = \frac{\frac{N_{DOF}}{2} + 1}{\frac{N_{DOF}}{2}} = 1 + \frac{2}{N_{DOF}}
    $$
    -   单原子气体 ($\gamma = 1 + 2/3 = 5/3 \approx 1.67$)
    -   双原子气体 ($\gamma = 1 + 2/5 = 7/5 = 1.4$)
    -   $\gamma$ 在绝热过程中非常重要。

### 等温过程的功 (Work in Isothermal Process)

-   如果理想气体在恒定温度 $T$ 下从 $V_i$ 膨胀到 $V_f$，做的功为：
    $$
    W_{by} = \int_{V_i}^{V_f} p dV = \int_{V_i}^{V_f} \frac{NkT}{V} dV = NkT \int_{V_i}^{V_f} \frac{dV}{V} = NkT \ln\left(\frac{V_f}{V_i}\right)
    $$

### 熵、温度、压强的热力学定义总结

-   Lecture 3 Slide 24 总结了如何从熵 $S$ 出发，通过求导得到温度 $T$ 和压强 $p$ 的热力学定义：
    $$
    \left(\frac{\partial S}{\partial U}\right)_{V,N} = \frac{1}{T}
    $$
    $$
    \left(\frac{\partial S}{\partial V}\right)_{U,N} = \frac{p}{T}
    $$
-   这表明熵 $S(U, V, N)$ 是一个包含了系统所有热力学信息的 **基本函数 (fundamental function)**。

### Lecture 3 总结

-   理想气体模型是热力学的重要基础。$pV=NkT$。
-   压强来自微观粒子的碰撞。$p = \frac{2N}{3V} \langle KE_{trans} \rangle$。
-   能量均分定理指出每个二次型自由度贡献 $\frac{1}{2}kT$ 的平均能量。
-   理想气体的内能 $U = \frac{N_{DOF}}{2}NkT$，只依赖于温度。
-   理想气体的热容 $C_V = \frac{N_{DOF}}{2}Nk$ 和 $C_P = C_V + Nk$ 在一定温度范围内是常数。
-   熵是连接宏观与微观、以及各个热力学量的核心。

## Lecture 4: Equipartition and Molar Heat Capacity

### 能量均分定理 (Equipartition Theorem) 与热容 (Heat Capacity)

#### 核心概念：能量均分定理

能量均分定理是连接微观粒子运动和宏观系统内能 (Internal Energy) $U$ 以及温度 $T$ 的桥梁。它的核心思想是：

-   对于一个处于热平衡状态 ($T$) 的系统，能量会**平均分配**给系统所有**活跃的**二次型自由度 (quadratic degrees of freedom)。
-   每个活跃的二次型自由度平均分配到的能量是 $\frac{1}{2}kT$。
    -   这里的 $k$ 是玻尔兹曼常数 (Boltzmann constant)。
    -   "二次型自由度" 指的是能量项可以表示为某个坐标或动量的平方形式，例如动能 $\frac{1}{2}mv_x^2$ 或谐振子势能 $\frac{1}{2}kx^2$。

#### 自由度 (Degrees of Freedom, DOF)

自由度是指确定一个粒子 (原子或分子) 在空间中的状态所需要的独立参数的数量。

-   **平动自由度 (Translational DOF):** 描述粒子在空间中直线运动的能力。在三维空间中，有 $x, y, z$ 三个方向的平动自由度。这就像控制一架无人机在空中前后、左右、上下移动。
-   **转动自由度 (Rotational DOF):** 描述分子绕轴旋转的能力。
    -   单原子分子 (Monoatomic) 如 He, Ne: 体积很小，转动惯量几乎为零，一般不考虑转动自由度。
    -   线性分子 (Linear molecules) 如双原子分子 (Diatomic) $H_2, O_2$ 或 $CO_2$: 有 2 个转动自由度，对应于绕通过质心且垂直于分子轴的两个相互垂直的轴的转动。绕分子自身轴线的转动，其转动惯量极小，对应的能量量子化间隔很大，通常在室温下不被激发。
    -   非线性分子 (Non-linear molecules) 如 $H_2O, CH_4$: 有 3 个转动自由度，对应于绕通过质心的三个相互垂直的轴的转动。
-   **振动自由度 (Vibrational DOF):** 描述分子内部原子间相对位置改变 (化学键的伸缩和弯曲) 的能力。每个振动模式包含两项二次型能量：动能和势能。因此，每个活跃的振动模式贡献 $2 \times \frac{1}{2}kT = kT$ 的能量。


**注意： 计算 $v_{rms}$ 应只考虑平动动能的贡献**

$$
v_{rms} = \sqrt{ \frac{3RT}{M} }
$$

#### 理想气体的内能 $U$ 和定容热容 $C_V$ 

根据能量均分定理，我们可以计算理想气体的内能 $U$ (忽略分子间相互作用势能)。对于 $N$ 个分子的理想气体：

1.  **单原子气体 (Monoatomic Gas):**
    -   只有 3 个平动自由度 ($x, y, z$ 方向动量)。
    -   每个自由度贡献 $\frac{1}{2}kT$ 能量。
    -   总内能 $U = N \times 3 \times \frac{1}{2}kT = \frac{3}{2}NkT$。
    -   定容热容 (Heat Capacity at Constant Volume) $C_V$ 定义为 $C_V = (\frac{\partial U}{\partial T})_V$。
    -   $C_V = \frac{d}{dT}(\frac{3}{2}NkT) = \frac{3}{2}Nk$。

2.  **双原子气体 (Diatomic Gas) (室温附近):**
    -   有 3 个平动自由度和 2 个转动自由度 (通常在室温下，振动自由度未被激发)。共 5 个自由度。
    -   总内能 $U = N \times (3+2) \times \frac{1}{2}kT = \frac{5}{2}NkT$。
    -   定容热容 $C_V = \frac{d}{dT}(\frac{5}{2}NkT) = \frac{5}{2}Nk$。

3.  **双原子气体 (高温):**
    -   3 个平动 + 2 个转动 + 1 个振动模式 (包含动能和势能，共 2 个二次项)。共 $3+2+2=7$ 个等效自由度。
    -   总内能 $U = N \times (3+2+2) \times \frac{1}{2}kT = \frac{7}{2}NkT$。
    -   定容热容 $C_V = \frac{7}{2}Nk$。

4.  **非线性多原子气体 (Non-linear Polyatomic Gas) (室温附近):**
    -   3 个平动 + 3 个转动自由度 (振动通常未激发)。共 6 个自由度。
    -   总内能 $U = N \times (3+3) \times \frac{1}{2}kT = 3NkT$。
    -   定容热容 $C_V = 3Nk$。




#### 自由度的 "冻结" (Frozen Out) 现象

-   **量子效应:** 为什么不是所有自由度在任何温度下都活跃？这是量子力学的结果。能量不是连续的，而是量子化的 (quantized)。要激发一个自由度 (如转动或振动)，分子需要获得足够的能量 $\Delta E$ 来跃迁到下一个能级。
-   **温度依赖:** 分子的平均热运动能量与温度 $T$ 相关 (约为 $kT$)。
    -   当 $kT \ll \Delta E$ 时，分子很难获得足够的能量来激发该自由度，该自由度就像被 "冻结" (frozen out) 了，对热容没有贡献。
    -   当 $kT \approx \Delta E$ 或 $kT \gg \Delta E$ 时，该自由度被激发，开始对热容有贡献。
-   **技术比喻:** 想象一下爬楼梯。平动能级间隔非常小，就像一个几乎平缓的斜坡，总能轻松移动 (总能被激发)。转动能级间隔稍大，像正常的楼梯，需要一定的 "抬腿" 能量 (温度) 才能上一级。振动能级间隔更大，像很高的台阶，需要更大的能量 (更高的温度) 才能上去。
-   **氢气 ($H_2$) 例子 (Slide 4 图示):**
    -   **低温 (< 100 K):** 只有平动自由度活跃 ($C_V \approx \frac{3}{2}Nk$)。
    -   **中温 (约 100 K - 1000 K):** 平动和转动自由度都活跃 ($C_V \approx \frac{5}{2}Nk$)。这是我们通常说的室温情况。
    -   **高温 (> 1000 K):** 平动、转动和振动自由度都活跃 ($C_V \approx \frac{7}{2}Nk$)。

#### 固体的热容 (Heat Capacity of a Solid)

-   **模型:** 将固体中的原子看作是通过弹簧相互连接的小球 (晶格振动)。
-   **自由度:** 每个原子可以在 $x, y, z$ 三个方向上振动。
    -   每个方向的振动都包含动能 ($\frac{1}{2}mv_x^2$) 和势能 ($\frac{1}{2}kx^2$)，都是二次项。
    -   因此，每个原子有 $3 \times 2 = 6$ 个二次型自由度。
-   **内能:** 根据能量均分定理，每个原子平均能量为 $6 \times \frac{1}{2}kT = 3kT$。对于包含 $N$ 个原子的固体，总内能 $U = 3NkT$。 (假设温度不太低，均分定理适用)。
-   **热容:** 固体的热容 $C = (\frac{\partial U}{\partial T}) \approx 3Nk$。
    -   对于固体和大多数液体，体积变化很小，所以定压热容 $C_P$ 和定容热容 $C_V$ 非常接近 ($C_P \approx C_V$)，通常直接用 $C$ 表示。
-   **摩尔热容 (Molar Heat Capacity) (Slide 6):**
    -   将 $N = nN_A$ (n 是摩尔数, $N_A$ 是阿伏加德罗常数) 和 $k = R/N_A$ (R 是理想气体常数) 代入。
    -   $C = 3 (nN_A) (R/N_A)  = 3nR$。
    -   摩尔热容 $C_{mol} = C/n = 3R$。
    -   $R \approx 8.314 J/(mol \cdot K)$，所以 $C_{mol} \approx 3 \times 8.314 \approx 24.9 J/(mol \cdot K)$。
    -   这就是**杜隆-珀蒂定律 (Dulong-Petit Law)**：许多固体在室温附近的摩尔热容约为 $3R$。Slide 6 的表格数据验证了这一点。

#### 能量均分定理总结 (Slide 7 & 8)

-   能量均分定理提供了一个基于活跃自由度数量计算物质内能 $U$ 和定容热容 $C_V$ 的框架：
    $$
    U = \frac{N_{DOF}}{2} NkT + \text{const}
    $$
    $$
    C_V = \left(\frac{\partial U}{\partial T}\right)_{V,N} = \frac{N_{DOF}}{2} Nk
    $$
    -   $N_{DOF}$ 是每个粒子活跃的二次型自由度数目。
-   $N_{DOF}$ 取决于温度，因为量子效应会 "冻结" 能量间隔较大的自由度。
-   知道 $U(T)$ 可以让我们计算熵变 $\Delta S$ 和热容 $C_V$，从而了解系统加热或冷却的难易程度。

### 热传导 (Heat Conduction)

热传导是热量从高温区域向低温区域传递的三种基本方式之一 (另外两种是对流和辐射)，主要发生在固体和静止流体中。

#### 基本机制

-   微观上看，热能是粒子 (原子、分子、电子) 无规则运动的动能。
-   在温度不均匀的物体中，高温区的粒子平均动能较大，低温区的粒子平均动能较小。
-   通过碰撞或相互作用，能量会从高动能粒子传递给低动能粒子。这就像拥挤人群中，活跃的人会撞到不活跃的人，把能量传过去。
-   虽然能量向各个方向随机扩散，但从高温区传出的能量多于从低温区传回的能量，导致净能量从高温流向低温。
-   热量传递的速率，即**热流 (Heat Current)** $H$ (单位时间传递的热量，单位：瓦特 W)，取决于**温度梯度 (Temperature Gradient)** $\frac{dT}{dx}$ (温度随距离的变化率)。
    $$
    H \propto \frac{dT}{dx}
    $$

#### 傅里叶热传导定律 (Fourier's Law of Heat Conduction) (Slide 10)

-   **热流密度 (Heat Current Density) $J$:** 单位时间内垂直通过单位面积的热量。单位：W/m²。
    $$
    J = -\kappa \frac{dT}{dx}
    $$
    -   $\kappa$ 是**热导率 (Thermal Conductivity)**，是材料本身的性质，表示材料导热能力强弱。单位：W/(m·K)。 $\kappa$ 越大，导热性能越好。
    -   负号表示热量流动的方向与温度升高的方向相反 (即总是从高温流向低温)。
-   **总热流 (Total Heat Current) $H$:** 通过整个截面积 $A$ 的总热流。
    $$
    H = J A = -\kappa A \frac{dT}{dx}
    $$
    单位：W。

#### 典型问题：平板热传导与热阻 (Slide 11)

考虑一个厚度为 $d$，截面积为 $A$，两侧表面温度分别为 $T_1$ 和 $T_2$ ($T_1 > T_2$) 的均匀材料平板。假设达到稳态 (steady state)，温度梯度是均匀的：

-   温度梯度 $\frac{dT}{dx} = \frac{T_2 - T_1}{d} = -\frac{T_1 - T_2}{d} = -\frac{\Delta T}{d}$，其中 $\Delta T = T_1 - T_2$ 是温度差。
-   热流密度 $J = -\kappa (-\frac{\Delta T}{d}) = \kappa \frac{\Delta T}{d}$。
-   总热流 $H = J A = \frac{\kappa A}{d} \Delta T$。

-   **热阻 (Thermal Resistance) $R_{thermal}$:**
    -   为了类比电路中的欧姆定律 ($I = \Delta V / R$)，我们定义热阻 $R_{thermal}$。
    -   热流 $H$ 相当于电流 $I$。
    -   温度差 $\Delta T$ 相当于电压降 $\Delta V$。
    -   则 $H = \frac{\Delta T}{R_{thermal}}$。
    -   比较 $H = \frac{\kappa A}{d} \Delta T$，得到：
        $$
        R_{thermal} = \frac{d}{\kappa A}
        $$
    -   热阻越大，在相同温度差下，热流越小。这就像电阻越大，在相同电压下，电流越小。

#### 应用实例：窗户热损失 (Slide 12)

Slide 12 计算了一个具体例子：通过玻璃窗的热损失。

-   给定参数：室内 $22^\circ C$, 室外 $0^\circ C \implies \Delta T = 22 K$。面积 $A = 0.3 m^2$。厚度 $d = 0.5 cm = 0.005 m$。玻璃热导率 $\kappa \approx 1 W/(m \cdot K)$。
-   计算热流：
    $$
    H = \frac{\kappa A}{d} \Delta T = \frac{(1 \, W/(m \cdot K)) (0.3 \, m^2)}{0.005 \, m} (22 \, K) = 60 \times 22 \, W = 1320 \, W
    $$
-   这个结果 (1320 W) 相当大，说明窗户是建筑物热量损失的重要途径，特别是在温差较大的情况下。

#### 气体的热导率 (Slide 13)

-   气体的热传导是通过分子碰撞传递能量。其热导率 $\kappa$ 与分子的平均速度 $\langle v \rangle$、平均自由程 (mean free path) $\lambda$ (两次碰撞之间平均走过的距离)、密度 $\rho$ 以及定容比热 $c_v$ 相关：
    $$
    k = \frac{1}{3} \langle v \rangle \lambda \rho c_v
    $$

-   更进一步的推导表明，气体的热导率 $\kappa$ 大致正比于 $\sqrt{T/m}$，其中 $T$ 是绝对温度，$m$ 是分子质量。
    $$
    \kappa \propto \sqrt{\frac{T}{m}}
    $$
-   Slide 13 的表格给出了一些气体在特定温度下的热导率值。可以看到 H2 和 He 的热导率相对较高，因为它们的分子质量小，平均速度快。

#### 固体的热导率

-   固体的热传导主要通过两种机制：
    1.  **晶格振动 (Lattice Vibrations) / 声子 (Phonons):** 原子振动会像波一样在晶格中传播，传递能量。这在所有固体中都存在。
    2.  **自由电子 (Free Electrons):** 在金属中，自由电子可以快速移动并携带能量。这是金属导热性能远好于绝缘体的主要原因。



## Lecture 5: Boltzmann Factor
### 从孤立系统到热接触系统 (From Isolated System to System in Thermal Contact)

-   **之前 (Up until now):** 我们主要关注孤立系统 (Isolated System)。
    -   特点：总能量 $U$ 固定。
    -   基本假设：等概率原理 (Principle of equal a priori probability)，即所有能量相同的微观态 (microstates) 出现的可能性都相等。
-   **现在 (From now on):** 我们考虑一个小系统 (small system) 与一个非常大的热力学蓄水池 (Thermal Reservoir) 进行热接触。
    -   特点：系统的温度 $T$ 由热力学蓄水池决定并保持恒定。
    -   重要变化：
        -   小系统的能量不再固定，它可以与蓄水池交换能量。因此，小系统可以处于不同能量 $E_n$ 的微观态 $n$。
        -   不同能量的微观态出现的概率不再相等，而是依赖于其能量 $E_n$。直观上，系统将能量 $E_n$ 交给蓄水池越多 (即系统自身能量 $E_n$ 越低)，这种情况发生的可能性越大，因为这会使得拥有巨大自由度的蓄水池的熵 (entropy) 增加得更多。


### 热力学蓄水池 (Thermal Reservoir)

-   定义：一个非常大的系统，其热容 (Heat Capacity $C_V$) 极大。
-   关键特性：当小系统从中吸收或向其释放能量时，蓄水池的温度 $T_R$ 几乎不变。
    -   数学上，这意味着我们可以忽略能量交换对 $T_R$ 造成的影响，即 $\frac{\partial T_R}{\partial U_R} \approx 0$ 和更高阶的导数。这在后面的推导中至关重要 (用于泰勒展开的截断)。

### 玻尔兹曼因子 (Boltzmann Factor)

核心目标是计算小系统处于能量为 $E_n$ 的特定微观态 $n$ 的概率 $P_n$。

-   **基本原理:** 概率 $P_n$ 正比于整个复合系统 (小系统 + 蓄水池) 处于相应状态的总微观态数量 $\Omega_{total}$。当小系统处于确定状态 $n$ (能量 $E_n$) 时，其微观态数 $\Omega_{sys}=1$。此时，蓄水池的能量为 $U_R = U_{total} - E_n$。因此，复合系统的总微观态数就等于蓄水池在能量为 $U_R$ 时的微观态数 $\Omega_R(U_R)$。
$$
    P_n \propto \Omega_{total} = \Omega_{sys}(E_n) \times \Omega_R(U_{total} - E_n)
$$
    由于 $\Omega_{sys}(E_n)=1$ (我们指定了系统处于 *特定* 微观态 $n$)，所以：
    $$
    P_n \propto \Omega_R(U_{total} - E_n)
    $$

-   **推导过程:**
    1.  利用玻尔兹曼熵公式 $S = k_B \ln \Omega$，其中 $k_B$ 是玻尔兹曼常数 (Boltzmann constant)。则 $\Omega_R = e^{S_R / k_B}$。
        $$
        P_n \propto e^{S_R(U_{total} - E_n) / k_B}
        $$
    2.  对蓄水池的熵 $S_R(U_R)$ 在 $U_R = U_{total}$ (即 $E_n=0$) 附近进行泰勒展开，只保留到一阶导数 (因为蓄水池很大，$E_n \ll U_{total}$，且温度 $T_R$ 稳定)。
        $$
        S_R(U_{total} - E_n) \approx S_R(U_{total}) - \left. \frac{\partial S_R}{\partial U_R} \right|_{U_{total}} E_n
        $$

    3.  根据热力学温度的定义:
        $$
        \frac{1}{T_R} = \left. \frac{\partial S_R}{\partial U_R} \right|_{U_{total}}
        $$
    4.  代入泰勒展开式：
        $$
        S_R(U_{total} - E_n) \approx S_R(U_{total}) - \frac{E_n}{T_R}
        $$
    5.  代回到概率表达式 $P_n$:
        $$
        P_n \propto e^{\left( S_R(U_{total}) - E_n/T_R \right) / k_B} = e^{S_R(U_{total}) / k_B} \cdot e^{-E_n / (k_B T_R)}
        $$
    6.  由于 $e^{S_R(U_{total}) / k_B}$ 是一个不依赖于小系统状态 $n$ 的常数 (只与蓄水池总能量有关)，我们可以将其吸收到比例系数中。令 $T_R = T$ (系统与蓄水池平衡时的温度)，得到：
        $$
        P_n \propto e^{-E_n / (k_B T)}
        $$
        这个因子 $e^{-E_n / (k_B T)}$ 就是著名的 **玻尔兹曼因子 (Boltzmann Factor)**。它表明，系统处于能量为 $E_n$ 的状态的概率随能量 $E_n$ 的增加呈指数衰减。

### 归一化与配分函数 (Normalization and Partition Function)

-   **归一化 (Normalization):** 所有可能状态的概率之和必须等于 1。
    $$
    \sum_n P_n = 1
    $$
    我们之前得到 $P_n = C \cdot e^{-E_n / (k_B T)}$，其中 C 是归一化常数。
    $$
    \sum_n C \cdot e^{-E_n / (k_B T)} = C \sum_n e^{-E_n / (k_B T)} = 1
    $$
    因此，
    $$
    C = \frac{1}{\sum_n e^{-E_n / (k_B T)}}
    $$

-   **配分函数 (Partition Function, Z):** 分母部分的求和被称为配分函数 $Z$。
    $$
    Z = \sum_n e^{-E_n / (k_B T)}
    $$
    这个求和是对系统所有可能的 **微观态 (microstates)** $n$ 进行的。
    -   $Z$ 是一个无量纲的量，它依赖于温度 $T$ 和系统的能谱 $\{E_n\}$。
    -   $Z$ 的大小粗略地反映了在温度 $T$ 下，系统有多少个状态是显著可及的 (significantly populated)。


-   **最终概率公式:**
    $$
    P_n = \frac{e^{-E_n / (k_B T)}}{Z} = \frac{e^{-E_n / (k_B T)}}{\sum_j e^{-E_j / (k_B T)}}
    $$
    这就是 **玻尔兹曼分布 (Boltzmann distribution)**。



-   **温度依赖性:**
    -   **低温极限 ($T \to 0$):** $k_B T \to 0$。对于任何 $E_n > E_0$ (基态能量)，$-E_n / (k_B T) \to -\infty$，所以 $e^{-E_n / (k_B T)} \to 0$。只有能量最低的基态 (ground state) 的玻尔兹曼因子不为零。如果基态是唯一的 (non-degenerate)，能量为 $E_0$，则 $Z \approx e^{-E_0 / (k_B T)}$。如果我们方便地设定 $E_0 = 0$，则 $Z \to 1$。如果基态有 $g_0$ 个简并态 (degenerate states)，即有 $g_0$ 个不同的微观态都具有最低能量 $E_0$，则 $Z \approx g_0 e^{-E_0 / (k_B T)}$。若设 $E_0 = 0$，则 $Z \to g_0$。这意味着在绝对零度附近，系统几乎完全被限制在能量最低的状态(或状态群)中，有效的可及状态数量就是基态的简并度。
    -   **高温极限 ($T \to \infty$):** $k_B T \to \infty$。对于任何有限的 $E_n$，$-E_n / (k_B T) \to 0$，所以 $e^{-E_n / (k_B T)} \to 1$。此时，$Z$ 趋向于系统中 **所有** 微观态的总数 $N_{total}$ (如果总数是有限的话)。这意味着在非常高的温度下，能量不再是限制因素，所有状态都变得同等可能被访问。
    -   通常情况下，$Z$ 随温度 $T$ 的升高而单调增加，因为更高的温度使得更多的高能级状态变得“可及”。



### 实例
#### 三能级分子 (Example: 3-State Molecule)

-   系统：一个分子有三个能级 $E_0, E_1, E_2$。能量间距为 $\epsilon = 10^{-20}$ J。我们可以方便地设 $E_0 = 0$, $E_1 = \epsilon$, $E_2 = 2\epsilon$。
-   环境：温度 $T = 1000$ K。
-   计算：
    1.  计算玻尔兹曼因子中的指数项 $E_n / (k_B T)$。注意单位。 $k_B \approx 1.38 \times 10^{-23}$ J/K。
        $$
        \frac{\epsilon}{k_B T} = \frac{10^{-20} \text{ J}}{(1.38 \times 10^{-23} \text{ J/K}) (1000 \text{ K})} \approx 0.725
        $$
    2.  计算配分函数 $Z$:
        $$
        Z = \sum_{n=0}^{2} e^{-E_n / (k_B T)} = e^{-E_0 / (k_B T)} + e^{-E_1 / (k_B T)} + e^{-E_2 / (k_B T)}
        $$
        $$
        Z = e^0 + e^{-\epsilon/(k_B T)} + e^{-2\epsilon/(k_B T)} = 1 + e^{-0.725} + e^{-2 \times 0.725}
        $$
        $$
        Z \approx 1 + 0.484 + 0.235 = 1.719
        $$
    3.  计算概率 $P_1$ (处于中间能级 $E_1 = \epsilon$ 的概率)：
        $$
        P_1 = \frac{e^{-E_1 / (k_B T)}}{Z} = \frac{e^{-\epsilon / (k_B T)}}{Z} \approx \frac{0.484}{1.719} \approx 0.282
        $$
    4.  计算概率 $P_2$ (处于最高能级 $E_2 = 2\epsilon$ 的概率)：
        $$
        P_2 = \frac{e^{-E_2 / (k_B T)}}{Z} = \frac{e^{-2\epsilon / (k_B T)}}{Z} \approx \frac{0.235}{1.719} \approx 0.137
        $$
    5.  (补充) $P_0 = \frac{e^{-E_0 / (k_B T)}}{Z} = \frac{1}{Z} \approx \frac{1}{1.719} \approx 0.582$。验证：$P_0 + P_1 + P_2 \approx 0.582 + 0.282 + 0.137 = 1.001$ (由于近似导致微小误差)。

#### 温度依赖性分析

![125504837ba93c6012c1ac3eb1dd5e5.png](https://s2.loli.net/2025/04/22/TSV7OilZFxXgjor.png)

-   **当 $T \to 0$:**
    -   $\frac{E_n}{k_B T} \to +\infty$ (对于 $E_n > 0$)。
    -   $e^{-E_n / (k_B T)} \to 0$ (对于 $E_n > 0$)。
    -   $e^{-E_0 / (k_B T)} = e^0 = 1$。
    -   $Z \to 1 + 0 + 0 = 1$。
    -   $P_0 = 1/Z \to 1$。$P_1 \to 0$, $P_2 \to 0$。
    -   **结论:** 在绝对零度，系统必然处于能量最低的基态。
-   **当 $T \to \infty$:**
    -   $\frac{E_n}{k_B T} \to 0$。
    -   $e^{-E_n / (k_B T)} \to e^0 = 1$。
    -   $Z \to 1 + 1 + 1 = 3$。
    -   $P_0 \to 1/3$, $P_1 \to 1/3$, $P_2 \to 1/3$。
    -   **结论:** 在极高温度下，所有能级被占据的概率趋于相等 (假设没有简并度)。能量差异相对于 $k_B T$ 变得微不足道。
-   **当 T 减小 (decrease T):**
    -   $1/T$ 增大。指数项 $-E_n / (k_B T)$ 对于 $E_n > 0$ 变得更负。
    -   $e^{-E_n / (k_B T)}$ 对于能量越高的状态 ($E_2 > E_1 > E_0=0$) 下降得越快。
    -   因此，$P_2$ 的相对比例会减小。$P_2$ 随 $T$ 减小而 **减小 (decreases)**。


#### 简并情况计算配分函数 Z

我们定义 $Z$ 是对 **所有微观态 (microstates)** 求和。然而，在实际计算中，经常会遇到多个不同的微观态具有 **相同能量** 的情况，这被称为 **简并 (degeneracy)**。

-   假设系统的能量只能取一系列离散的值 $E_0, E_1, E_2, ...$ (这些称为能级, energy levels)。
-   对于某个特定的能级 $E_j$，可能有 $g(E_j)$ 个不同的微观态都具有这个能量。$g(E_j)$ 就叫做能级 $E_j$ 的 **简并度 (degeneracy)**。
-   在这种情况下，我们可以将求和按照能级来组织：
    $$
    Z = \sum_{\text{所有微观态 } n} e^{-E_n / (k_B T)} = \sum_{\text{所有能级 } j} \sum_{\substack{\text{态 } n \\ \text{属于能级 } j}} e^{-E_j / (k_B T)}
    $$
    由于内层求和中的每一项都是 $e^{-E_j / (k_B T)}$，并且有 $g(E_j)$ 项，所以：
    $$
    Z = \sum_{\text{能级 } j} g(E_j) e^{-E_j / (k_B T)}
    $$
    这个形式通常在实践中更常用，特别是当我们知道系统的能谱 (energy spectrum) $E_j$ 和相应的简并度 $g(E_j)$ 时。

    *例子：* 回到三能级分子，能量为 $E_0=0, E_1=\epsilon, E_2=2\epsilon$。如果每个能级都是非简并的，即 $g(E_0)=1, g(E_1)=1, g(E_2)=1$，那么
    $Z = 1 \cdot e^{-0/(k_B T)} + 1 \cdot e^{-\epsilon/(k_B T)} + 1 \cdot e^{-2\epsilon/(k_B T)}$。
    如果假设 $E_1$ 能级是双重简并的 (two-fold degenerate)，即 $g(E_1)=2$，而其他能级非简并，那么
    $Z = 1 \cdot e^{-0/(k_B T)} + 2 \cdot e^{-\epsilon/(k_B T)} + 1 \cdot e^{-2\epsilon/(k_B T)}$。

### 能量交换与微观态计数 (Energy Exchange and Microstate Counting)

这部分内容通过简化的模型 (量子谐振子，Quantum Harmonic Oscillator, SHO) 来帮助我们直观理解为什么与蓄水池接触时，低能态更可能出现，并为玻尔兹曼因子的推导提供另一种角度的支撑。

-   **模型:** N 个 SHO 共享 $q$ 个能量子 $\epsilon$ (总能量 $U = q\epsilon$)。每个振子能量 $E_i = n_i \epsilon$，$n_i$ 是整数。总能量约束 $\sum n_i = q$。
-   **微观态 (Microstate):** 一种具体的能量分配方式 $\{n_1, n_2, ..., n_N\}$。
-   **总微观态数 $\Omega$ (或 $W$):**
    -   **Checkpoint 2 (N=2, q=4):** 两个振子分 4 份能量。可能的分配 $(n_1, n_2)$ 有: (0, 4), (1, 3), (2, 2), (3, 1), (4, 0)。共 5 种。 $\Omega = 5$。
    -   **Exercise (N=3, q=2):** 三个振子分 2 份能量。可能的分配 $(n_1, n_2, n_3)$ 有: (2,0,0), (0,2,0), (0,0,2), (1,1,0), (1,0,1), (0,1,1)。共 6 种。 $\Omega = 6$。
    -   **通用公式 (q-formula):** $N$ 个振子共享 $q$ 个能量子的总微观态数为：
        $$
        \Omega(N, q) = \binom{q + N - 1}{q} = \frac{(q+N-1)!}{q!(N-1)!}
        $$
        验证：N=2, q=4, $\Omega = \binom{4+2-1}{4} = \binom{5}{4} = 5$。
        验证：N=3, q=2, $\Omega = \binom{2+3-1}{2} = \binom{4}{2} = \frac{4!}{2!2!} = 6$。

-   **单个振子的能量概率 (N=3, q=2 例子):**
    -   考虑振子 #1 的能量。
    -   $E_1=0$ (即 $n_1=0$): 对应的状态有 (0,2,0), (0,0,2), (0,1,1)。共 3 种。 $P(E_1=0) = 3/6 = 1/2$。
    -   $E_1=\epsilon$ (即 $n_1=1$): 对应的状态有 (1,1,0), (1,0,1)。共 2 种。 $P(E_1=\epsilon) = 2/6 = 1/3$。
    -   $E_1=2\epsilon$ (即 $n_1=2$): 对应的状态有 (2,0,0)。共 1 种。 $P(E_1=2\epsilon) = 1/6$。
    -   **观察:** 振子 #1 的能量越高，其出现的概率越低。
    -   **原因:** 当振子 #1 拿走更多能量时，留给其他振子 (可以看作是“蓄水池”) 的能量就越少，导致其他振子可分配能量的方式 (微观态数) 减少。因为等概率原理适用于整个 **孤立** 系统，所以振子 #1 处于某个能量 $E_1$ 的概率正比于 **剩下 N-1 个振子** 在能量为 $U-E_1$ 时的微观态数。

-   **平均能量 (Average Energy):**
    $$
    \langle E_1 \rangle = \sum_{n=0}^{2} P(E_1=n\epsilon) \cdot (n\epsilon) = (1/2)(0) + (1/3)(\epsilon) + (1/6)(2\epsilon) = 0 + \frac{1}{3}\epsilon + \frac{1}{3}\epsilon = \frac{2}{3}\epsilon
    $$
    由于总能量 $U=2\epsilon$ 分给 3 个振子，平均每个振子 $\langle E \rangle = U/N = (2\epsilon)/3$。结果一致。

#### 从微观态计数角度理解热接触 (Connecting Microstates to Thermal Contact)

-   **模型:** 1 个小系统 (振子 #1) + 3 个振子组成的蓄水池 (振子 #2, #3, #4)。总能量 $U=4\epsilon$ ($q=4$, 总 $N=4$ 个振子)。
-   **目标:** 计算小系统 (振子 #1) 处于能量 $E_n = n\epsilon$ 的概率 $P_n$。
-   **关键点:** $P_n$ 正比于当振子 #1 能量为 $E_n$ 时，**蓄水池 (剩下 3 个振子)** 所拥有的微观态数 $\Omega_R(U_R)$。这里 $U_R = U - E_n = (4-n)\epsilon$。蓄水池有 $N_R=3$ 个振子。
-   **计算:** 使用 $\Omega_R(N_R, q_R) = \Omega(3, 4-n)$ 公式 $\binom{q_R+N_R-1}{q_R} = \binom{(4-n)+3-1}{4-n} = \binom{6-n}{4-n}$。
    -   $n=0$: $E_0=0$, $U_R=4\epsilon$ ($q_R=4$). $\Omega_R = \binom{6-0}{4-0} = \binom{6}{4} = \frac{6!}{4!2!} = 15$。
    -   $n=1$: $E_1=\epsilon$, $U_R=3\epsilon$ ($q_R=3$). $\Omega_R = \binom{6-1}{4-1} = \binom{5}{3} = \frac{5!}{3!2!} = 10$。
    -   $n=2$: $E_2=2\epsilon$, $U_R=2\epsilon$ ($q_R=2$). $\Omega_R = \binom{6-2}{4-2} = \binom{4}{2} = \frac{4!}{2!2!} = 6$。
    -   $n=3$: $E_3=3\epsilon$, $U_R=\epsilon$ ($q_R=1$). $\Omega_R = \binom{6-3}{4-3} = \binom{3}{1} = 3$。
    -   $n=4$: $E_4=4\epsilon$, $U_R=0$ ($q_R=0$). $\Omega_R = \binom{6-4}{4-4} = \binom{2}{0} = 1$。
-   **总状态数:** $\Omega_{total} = \sum_n \Omega_R(U-E_n) = 15+10+6+3+1 = 35$。这等于用总公式 $\Omega(N=4, q=4) = \binom{4+4-1}{4} = \binom{7}{4} = \frac{7!}{4!3!} = 35$ 计算的结果。
-   **概率 $P_n = \Omega_R(U-E_n) / \Omega_{total}$:**
    -   $P_0 = 15/35 \approx 0.43$
    -   $P_1 = 10/35 \approx 0.29$
    -   $P_2 = 6/35 \approx 0.17$
    -   $P_3 = 3/35 \approx 0.09$
    -   $P_4 = 1/35 \approx 0.03$
-   **再次确认:** 概率 $P_n$ 随着能量 $E_n$ 的增加而减小。这与玻尔兹曼因子的指数衰减行为定性一致。当蓄水池非常大 ($N_R \to \infty$) 时，这种关系会趋向于精确的指数形式 $e^{-E_n / (k_B T)}$。

### 总结 (Summary)

-   当一个系统与恒定温度 $T$ 的热力学蓄水池接触达到平衡时，系统处于特定微观态 $n$ (能量 $E_n$) 的概率由玻尔兹曼分布给出：
    $$
    P_n = \frac{e^{-E_n / (k_B T)}}{Z}
    $$
-   其中 $e^{-E_n / (k_B T)}$ 是玻尔兹曼因子，它量化了能量对概率的影响 (能量越高，概率越低)。
-   $Z = \sum_j e^{-E_j / (k_B T)}$ 是配分函数，它是对所有状态的玻尔兹曼因子求和，起到归一化的作用，并且本身包含了系统在温度 $T$ 下的热力学信息 (我们将在后续课程中看到 Z 如何联系到自由能、熵、平均能量等宏观量)。

## Lecture 6: Boltzmann Examples

### 回顾：玻尔兹曼分布与简并态 (Recap: Boltzmann Distribution & Degenerate States)

当一个小系统与一个恒定温度 $T$ 的大热库 (heat reservoir) 接触达到热平衡时，这个小系统处于某个具有能量 $E_n$ 的特定微观状态 (microstate) 的概率 $P_n$ 由 **玻尔兹曼因子 (Boltzmann factor)** 给出：

$$
P_n = \frac{e^{-E_n/kT}}{Z}
$$

这里的 $k$ 是玻尔兹曼常数 (Boltzmann's constant)。为了保证所有状态的概率之和为 1 ($\sum P_n = 1$)，我们引入了归一化常数 $Z$，称为 **配分函数 (partition function)**：

$$
Z = \sum_n e^{-E_n/kT}
$$

其中求和遍历系统所有可能的微观状态 $n$。配分函数 $Z$ 本身也包含了系统的热力学信息，它大致告诉我们在温度 $T$ 下，系统有多少个状态是显著可及的 (how many states are populated)。例如，当 $T \to 0$ 时，只有基态 (ground state) 被占据，如果基态不简并，$Z \to 1$。

**技术比喻:** 配分函数 $Z$ 就像一个衡量系统在特定温度下“活跃程度”的指标。温度越高，系统越有可能探索能量更高的状态， $Z$ 通常就越大，表示有更多的状态参与进来。

**简并态 (Degenerate States):** 
通常，系统可能有多个不同的微观状态对应同一个能量值 $E$。这种情况称为简并 (degenerate)。如果能量 $E$ 有 $g(E)$ 个不同的状态，那么系统具有能量 $E$ 的概率 $P(E)$ 就需要把所有这些简并状态的概率加起来：

$$
P(E) = \sum_{\text{states } n \text{ with energy } E} P_n = \sum_{\text{states } n \text{ with energy } E} \frac{e^{-E/kT}}{Z} = g(E) \frac{e^{-E/kT}}{Z}
$$

这里的 $g(E)$ 就是能量 $E$ 的 **简并度 (degeneracy factor)**。计算配分函数 $Z$ 时也需要考虑简并度：

$$
Z = \sum_{\text{energy levels } E} g(E) e^{-E/kT}
$$

**例子 (Slide 8):** 一个原子系统有能量为 0 的基态 (degeneracy $g(0)=1$) 和能量为 $\epsilon$ 的第一激发态 (first excited state) (degeneracy $g(\epsilon)=2$)。
- 配分函数 $Z = g(0)e^{-0/kT} + g(\epsilon)e^{-\epsilon/kT} = 1 + 2e^{-\epsilon/kT}$。
- 基态概率 $P(E=0) = 1 \cdot e^{-0/kT} / Z = 1/Z$。
- 激发态概率 $P(E=\epsilon) = 2 \cdot e^{-\epsilon/kT} / Z = 2e^{-\epsilon/kT}/Z$。
- 如果要找到基态和激发态占据概率相等的温度 $T$，即 $P(E=0) = P(E=\epsilon)$，则 $1/Z = 2e^{-\epsilon/kT}/Z$，得到 $1 = 2e^{-\epsilon/kT}$，解出 $e^{\epsilon/kT} = 2$，即 $\epsilon/kT = \ln(2)$。所以 $T = \epsilon / (k \ln 2)$。

### 解决玻尔兹曼问题的通用策略 (Strategy for Boltzmann Problems)


处理这类问题通常遵循以下步骤：

1.  **列出系统的微观状态 (microstates) 及其对应的能量 $E_i$。** 需要注意是否有简并态。
2.  **计算配分函数 $Z = \sum_i g_i e^{-E_i/kT}$。**
3.  **计算系统处于某个特定状态 $A$ (能量为 $E_A$) 的概率 $P(A) = g_A e^{-E_A/kT} / Z$。**
4.  **计算系统的平均能量 (average energy) 或内能 (internal energy) $U(T)$。**
    $$
    U(T) = \langle E \rangle = \sum_i E_i P(\text{state } i, T) = \sum_{\text{levels } E} E \cdot P(E) = \frac{1}{Z} \sum_{\text{levels } E} g(E) E e^{-E/kT}
    $$
    (这里 $P(\text{state } i, T)$ 是单个微观状态 $i$ 的概率， $P(E)$ 是具有能量 $E$ 的概率)。
5.  **计算系统的定容热容 (heat capacity at constant volume) $C_V(T)$。**
    $$
    C_V(T) = \left( \frac{\partial U}{\partial T} \right)_V
    $$
6.  **(可选) 计算系统的熵 (entropy) $S(T)$。** 
    $$
    S(T) = \int_0^T \frac{C_V(T')}{T'} dT'
    $$

这个流程展示了从微观状态和能量出发，如何通过统计方法（玻尔兹曼分布）计算宏观热力学量（如 $U$, $C_V$, $S$）。


### 应用实例 (Boltzmann Examples)


#### 1. 顺磁自旋 (Paramagnetic Spins) - 二能级系统 (2-Level System)


考虑一个简单的模型：$N$ 个独立的磁偶极矩 (magnetic dipoles) $\mu$，置于外部磁场 $B$ 中。每个偶极矩只能指向平行或反平行于磁场的方向（这是量子化的结果）。
-   状态 1: 自旋向上 (spin up)，能量 $E_H = +\mu B$ (假设 $\mu$ 定义为与磁场方向相反时能量更高)。
-   状态 2: 自旋向下 (spin down)，能量 $E_L = -\mu B$。

这是一个典型的 **二能级系统 (two-level system)**。单个自旋的配分函数为：
$$
Z = e^{-E_H/kT} + e^{-E_L/kT} = e^{-\mu B/kT} + e^{+\mu B/kT}
$$


两种状态的概率分别为：
$$
P_H = \frac{e^{-\mu B/kT}}{Z} \quad \text{and} \quad P_L = \frac{e^{+\mu B/kT}}{Z}
$$
利用这些概率，我们可以计算系统的平均能量、磁化强度以及热容等。例如，平均能量 $U(T) = N \langle E \rangle = N (E_H P_H + E_L P_L)$。

#### 2. 量子谐振子 (Quantum Harmonic Oscillators) 与固体热容



这是理解固体热容的关键模型。

-   **单个量子谐振子 (Single Quantum Harmonic Oscillator, SHO):**
    能量是量子化的，能级是等间距的：$E_n = n\epsilon$ (这里 $\epsilon = hf$, $h$ 是普朗克常数， $f$ 是振子频率，我们暂时忽略了零点能 $1/2 hf$，因为它是一个常数，对热容没有贡献)。假设每个能级都是非简并的 ($g(n)=1$)。
    配分函数 $Z$ 是一个等比数列求和 (geometric series)：
    $$
    Z = \sum_{n=0}^{\infty} e^{-E_n/kT} = \sum_{n=0}^{\infty} e^{-n\epsilon/kT} = \sum_{n=0}^{\infty} (e^{-\epsilon/kT})^n
    $$
    令 $x = e^{-\epsilon/kT}$，则 $Z = \sum_{n=0}^\infty x^n = \frac{1}{1-x}$ （要求 $x<1$，这在 $T>0$ 时总成立）。
    $$
    Z = \frac{1}{1 - e^{-\epsilon/kT}}
    $$
    状态 $n$ 的概率为：
    $$
    P_n = \frac{e^{-n\epsilon/kT}}{Z} = (1 - e^{-\epsilon/kT}) e^{-n\epsilon/kT}
    $$
    **能级占据情况:**
    -   低温下 ($kT \ll \epsilon$): $e^{-\epsilon/kT}$ 非常小，$P_0 \approx 1$，系统几乎完全处于基态。高能级几乎不被占据。
    -   高温下 ($kT \gg \epsilon$): $e^{-\epsilon/kT} \approx 1 - \epsilon/kT$，$P_n$ 随 $n$ 缓慢减小，许多能级都被占据。
    **技术比喻:** 低温时，系统像个“懒惰”的人，只愿意待在最舒服的基态；高温时，系统获得足够能量，变得“活跃”，愿意尝试更高的能量状态。

    **平均能量 $\langle E \rangle$ (Slide 15):** 通过求和 $\sum E_n P_n$ 可以得到 (具体推导见补充材料或教材)：
    $$
    \langle E \rangle = \frac{\epsilon}{e^{\epsilon/kT} - 1}
    $$
    **极限情况分析:**
    -   高温极限 ($kT \gg \epsilon$): $e^{\epsilon/kT} \approx 1 + \epsilon/kT$。
        $$
        \langle E \rangle \approx \frac{\epsilon}{(1 + \epsilon/kT) - 1} = \frac{\epsilon}{\epsilon/kT} = kT
        $$
        这符合 **能量均分定理 (Equipartition Theorem)**。对于一维谐振子，有两个平方项的能量（动能 $\frac{1}{2}mv^2$ 和势能 $\frac{1}{2}kx^2$），每个自由度贡献 $kT/2$ 的平均能量，总共 $kT$。
        **注意:** 能量均分定理成立的条件是 $kT$ 远大于能级间距 $\epsilon$。
    -   低温极限 ($kT \ll \epsilon$): $e^{\epsilon/kT} \gg 1$。
        $$
        \langle E \rangle \approx \epsilon e^{-\epsilon/kT} \ll kT
        $$
        能量远小于 $kT$，振动模式被 **"冻结" (frozen out)**，因为它很难被激发到第一个激发态。

    **热容 $C_V$ (Slide 16):** 对于 $N$ 个独立的谐振子，总能量 $U = N \langle E \rangle$。热容 $C = dU/dT$：
    $$
    C = N \frac{d\langle E \rangle}{dT} = Nk \left( \frac{\epsilon}{kT} \right)^2 \frac{e^{\epsilon/kT}}{(e^{\epsilon/kT} - 1)^2}
    $$
    **极限情况分析:**
    -   高温极限 ($kT \gg \epsilon$): $C \approx Nk$。每个振子贡献 $k$ 的热容 (对应两个自由度的 $kT/2 + kT/2 = kT$ 的能量)。
    -   低温极限 ($kT \ll \epsilon$): $C \approx Nk (\epsilon/kT)^2 e^{-\epsilon/kT} \to 0$。当温度趋于零时，热容也趋于零。
    这解释了 Slide 5 中双原子分子振动模式在低温下对热容没有贡献（被冻结），只有在 $T \sim 1000K$ (对应 $kT \sim \epsilon_{vib}$) 时才开始贡献热容。旋转模式类似，但 $\epsilon_{rot}$ 较小，在 $T \sim 100K$ 左右就被激发。平动模式能级间距极小，在任何实际温度下都满足 $kT \gg \epsilon_{trans}$，总是符合均分定理。

-   **爱因斯坦固体模型 (Einstein Solid):**
    将固体看作由 $N$ 个原子组成，每个原子可以在其格点位置附近独立地进行三维振动。这相当于 $3N$ 个独立的一维量子谐振子（每个原子在 x, y, z 方向各有一个）。假设所有振子的频率 $f$ (能量量子 $\epsilon = hf$) 都相同。
    总能量 $U = 3N \langle E \rangle = 3N \frac{\epsilon}{e^{\epsilon/kT} - 1}$。
    总定容热容 $C_V = 3N k \left( \frac{\epsilon}{kT} \right)^2 \frac{e^{\epsilon/kT}}{(e^{\epsilon/kT} - 1)^2}$。
    **极限情况:**
    -   高温极限 ($kT \gg \epsilon$): $C_V \to 3Nk$。这就是经典的 **杜隆-珀蒂定律 (Dulong-Petit Law)**。
    -   低温极限 ($kT \ll \epsilon$): $C_V \to 0$。这成功解释了实验观测到的固体热容在低温下趋于零的现象，这是经典理论无法解释的。
    Slide 18 的图展示了 $C_V$ 随温度变化的典型行为：从低温的 0 增长到高温的 $3Nk$ 平台。

#### 3. 大气定律 (The Law of Atmospheres)


考虑处于热平衡 ($T$ 恒定) 的理想气体分子在重力场中的分布。
-   一个分子在海平面 (高度 $h=0$) 的能量为 $E(0)$ (主要是动能)。
-   同一个分子如果在高度 $h$ 处具有相同的运动状态（即相同动能），其总能量为 $E(h) = E(0) + mgh$，其中 $m$ 是分子质量， $g$ 是重力加速度。
-   根据玻尔兹曼分布，分子出现在高度 $h$ 的概率 $P(h)$ 与出现在高度 0 的概率 $P(0)$ 之比为：
    $$
    \frac{P(h)}{P(0)} = \frac{e^{-E(h)/kT}}{e^{-E(0)/kT}} = \frac{e^{-(E(0)+mgh)/kT}}{e^{-E(0)/kT}} = e^{-mgh/kT}
    $$
-   对于理想气体，压强 $p$ 正比于分子数密度 $N/V$，而密度正比于找到分子的概率。因此，压强随高度的变化关系为：
    $$
    \frac{p(h)}{p(0)} = e^{-mgh/kT}
    $$
    这就是 **大气定律 (law of atmospheres)**。它表明大气压随高度指数下降。


-   **特征高度 (Characteristic Height) $h_c$:**
    定义 $h_c = kT/mg$。则大气定律可以写成 $p(h) = p(0) e^{-h/h_c}$。$h_c$ 是大气压强降低到其地面值 $1/e$ (约 37%) 时的高度。它代表了气体分子在重力作用下能够显著分布的典型高度尺度。
    从 Slide 22 的实际数据看，对于地球大气 (主要是 N2, O2)，在 $T=227K$ 时，$h_c \approx 7$ km。

-   **讨论:**
    -   $h_c = kT/mg$ 表明，质量 $m$ 越小的气体，其特征高度 $h_c$ 越大，即可以分布到更高的高度。
    -   这就是为什么轻气体如氢 (H2) 和氦 (He) 在大气层中可以延伸到非常高的高度，而较重的 O2, N2 主要集中在低层。
    -   氦气由于质量小 ($m$ 小，$h_c$ 大)，可以到达大气层非常高的区域，在那里受到太阳紫外辐射电离，并可能被太阳风等过程带走，导致地球上的氦气不断流失，造成氦气短缺 (Helium shortage)。
    -   水分子 ($m$ 相对较小) 会自发地从一杯水中蒸发 (单个分子获得足够能量逃逸)，但整杯水 (质量 $M$ 极大，$h_c$ 极小) 不会自发地作为一个整体跳出杯子，因为这需要克服巨大的重力势能，对应的玻尔兹曼因子 $e^{-Mgh/kT}$ 几乎为零。

### 总结


我们已经建立了几个核心概念之间的联系：
-   微观状态数 $\Omega(U)$ $\rightarrow$ 熵 $S(U) = k \ln \Omega(U)$ (统计力学基础)。
-   从 $S(U)$ 可以反解出 $U(T)$ (通过 $1/T = (\partial S / \partial U)_V$)。
-   从 $U(T)$ 可以计算热容 $C_V(T) = (\partial U / \partial T)_V$。
-   从 $C_V(T)$ 可以计算熵变 $\Delta S = \int (C_V/T) dT$ 和内能变化 $\Delta U = \int C_V dT$。

另外两条重要的计算路径：
-   **能量均分定理:** 在高温经典极限下 ($kT \gg$ 能量间距)，直接给出 $U(T)$ (每个二次型自由度贡献 $kT/2$)。
-   **玻尔兹曼分布:** 对于与热库接触的系统，可以计算 $Z$, $P_n$, 进而得到 $U(T)$，适用于所有温度。

实验上，测量 $C(T)$ 通常是最容易的。

