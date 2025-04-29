---
title: Thermodynamics out of equilibrium
date: 2025-04-28
date modified: 2025-04-28
categories: PHYS213
tags:
  - PHYS213
---

#PHYS213 



## Lecture 7: Thermodynamic Processes Reversible Processes


系统状态的变化路径称为热力学过程。我们特别关注以下四种理想化的过程，它们构成了许多热力学循环的基础：

1.  **等容过程 (Isochoric Process):**
    -   定义：体积 $V$ 保持不变 ($dV=0$)。
    -   P-V 图：一条垂直的线段。
    -   **热力学第一定律 (First Law of Thermodynamics, FLT):** $\Delta U = Q - W_{by}$。
    -   做功 (Work done by the system): $W_{by} = \int p dV = 0$。因为体积不变，系统不对外做功。
    -   热量 (Heat): $Q = \Delta U$。所有传入的热量都用于增加系统的内能。
    -   对于理想气体 (Ideal Gas): $\Delta U = C_V \Delta T = \alpha Nk \Delta T$。因此 $Q = C_V \Delta T$。 (这里 $\alpha$ 取决于气体类型，例如单原子气体 $\alpha=3/2$)。利用理想气体状态方程 $pV=NkT$，在体积不变时，$p/T = \text{constant}$，所以 $\Delta p / \Delta T = \text{constant}$，可以得到 $\Delta U = \alpha V \Delta p$ (如 Slide 8 所示)。

2.  **等压过程 (Isobaric Process):**
    -   定义：压强 $p$ 保持不变 ($dp=0$)。
    -   P-V 图：一条水平的线段。
    -   做功: $W_{by} = \int p dV = p \int dV = p (V_f - V_i) = p \Delta V$。
    -   内能变化 (Internal Energy Change): $\Delta U = C_V \Delta T$ (对于理想气体，内能仅是温度的函数)。
    -   热量: $Q = \Delta U + W_{by} = C_V \Delta T + p \Delta V$。
    -   对于理想气体: $p \Delta V = Nk \Delta T$。所以 $Q = C_V \Delta T + Nk \Delta T = (C_V + Nk) \Delta T$。我们定义 **定压热容 (Heat capacity at constant pressure)** $C_p = C_V + Nk$。因此 $Q = C_p \Delta T$。
    -   **技术比喻:** 等压加热时，系统像一个需要推开活塞才能膨胀的气球。一部分热量用来提高内部温度（增加内能 $\Delta U$），另一部分则用来对外做功 $W_{by}$ 把活塞推开。因此，等压过程比等容过程需要更多的热量来达到相同的温度升高，即 $C_p > C_V$ (Slide 5)。

3.  **等温过程 (Isothermal Process):**
    -   定义：温度 $T$ 保持不变 ($dT=0$)。
    -   P-V 图：一条双曲线 ($p \propto 1/V$ 对于理想气体)。
    -   对于理想气体: 内能 $U$ 只依赖于 $T$，所以 $\Delta U = 0$。
    -   热力学第一定律: $\Delta U = 0 = Q - W_{by}$，因此 $Q = W_{by}$。系统吸收的热量全部用来对外做功。
    -   做功 (理想气体):
        $$
        W_{by} = \int_{V_i}^{V_f} p dV = \int_{V_i}^{V_f} \frac{NkT}{V} dV = NkT \int_{V_i}^{V_f} \frac{dV}{V} = NkT \ln\left(\frac{V_f}{V_i}\right)
        $$
    -   这个过程通常需要系统与一个大的 **热库 (thermal reservoir)** 接触以保持温度恒定。

4.  **绝热过程 (Adiabatic Process):**
    -   定义：系统与外界没有热量交换 ($Q=0$)。这通常发生在快速进行的过程中（来不及热交换）或者系统被良好绝热时。
    -   P-V 图：比等温线更陡峭的曲线。
    -   热力学第一定律: $\Delta U = Q - W_{by} = -W_{by}$。系统对外做功会导致内能减少（温度下降），对系统做功会导致内能增加（温度升高）。
    -   对于理想气体 (准静态过程 Quasi-static process):
        我们可以推导出过程方程 (Slide 6)。从 $\Delta U = -W_{by}$ 开始：
        $\alpha Nk dT = -p dV = -\frac{NkT}{V} dV$
        分离变量：$\alpha \frac{dT}{T} = -\frac{dV}{V}$
        积分：$\alpha \int \frac{dT}{T} = -\int \frac{dV}{V}$
        $\alpha \ln T = -\ln V + \text{constant}$
        $\ln(T^\alpha) + \ln V = \text{constant} \Rightarrow \ln(T^\alpha V) = \text{constant}$
        所以:
        $$
        T^\alpha V = \text{constant}
        $$
        利用 $pV=NkT$ 消去 $T$ ($T \propto pV$)，得到：
        $(pV)^\alpha V = \text{constant} \Rightarrow p^\alpha V^{\alpha+1} = \text{constant}$
        两边取 $1/\alpha$ 次方: $p V^{(\alpha+1)/\alpha} = \text{constant}$。
        我们定义 **绝热指数 (adiabatic index)** $\gamma = C_p/C_V = (C_V+Nk)/C_V = (\alpha Nk + Nk)/(\alpha Nk) = (\alpha+1)/\alpha$。
        因此，理想气体准静态绝热过程满足：
        $$
        pV^\gamma = \text{constant}
        $$
        因为 $\gamma = (\alpha+1)/\alpha > 1$，所以绝热线 $p \propto V^{-\gamma}$ 比等温线 $p \propto V^{-1}$ 更陡峭 (Slide 7)。

### 可逆性与不可逆性 (Reversibility and Irreversibility)

(Slide 10-14, 26)

-   **可逆过程 (Reversible Process):** 一个过程是可逆的，如果它可以通过无穷小的改变，使得系统和环境都精确地回到初始状态，并且不留下任何其他变化。
    -   关键特征：过程进行得无限缓慢 (准静态，quasi-static)，使得系统在每一步都无限接近于平衡态。
    -   没有耗散效应 (dissipative effects)，如摩擦 (friction)、粘滞性 (viscosity)、非弹性形变、电流产生的热等。
    -   没有非平衡的热传递，例如跨越有限温度差的热传递。
    -   **熵判据 (Entropy Criterion):** 一个过程是可逆的，当且仅当系统与环境的总熵变 (total entropy change) 为零：$\Delta S_{tot} = \Delta S_{sys} + \Delta S_{surr} = 0$ (Slide 10)。
    -   **准静态的绝热过程** ($Q=0$) 是可逆的，因为 $dS = dQ_{rev}/T = 0$，系统熵不变，环境也无变化，$\Delta S_{tot}=0$ (Slide 12)。
    -   **准静态的等温过程** (与温度恒为 $T$ 的热库接触) 是可逆的。如果系统从热库吸收热量 $Q$，则 $\Delta S_{sys} = Q/T$，热库失去热量 $Q$，$\Delta S_{res} = -Q/T$。因此 $\Delta S_{tot} = Q/T - Q/T = 0$ (Slide 12)。
    -   Slide 3 和 13 中将等容和等压过程标记为不可逆，这通常是指实际操作中，例如将系统突然与一个不同温度的热库接触进行等容加热，或在有摩擦的活塞下进行等压膨胀。这些实际过程涉及有限温差传热或摩擦，导致 $\Delta S_{tot} > 0$。然而，理想化的等容和等压过程 *可以* 作为可逆循环的一部分，只要热量交换是通过一系列无穷小的温差或可逆方式进行的。

-   **不可逆过程 (Irreversible Process):** 自然界中发生的所有宏观过程都是不可逆的。它们不能自行反向进行。
    -   特征：过程进行速度有限，系统偏离平衡态；存在耗散效应；存在有限温差传热。
    -   总熵总是增加：$\Delta S_{tot} > 0$。
    -   **例子 (Slide 11, 14, 26):**
        -   一个物体由于摩擦而减速停止，其宏观动能转化为内能（热）。反过来，物体的内能自发地转化为宏观动能，让物体重新运动起来，是永远不会发生的 (Slide 11)。
        -   **自由膨胀 (Free Expansion):** 气体向真空膨胀 (Slide 14)。这是一个快速、非准静态的过程。虽然对于理想气体 $W=0, Q=0, \Delta U=0$，但过程是高度不可逆的，气体不会自发地收缩回原来的体积。熵是增加的。
        -   跨越有限温差的热传递 (热量从热物体传到冷物体)。
        -   摩擦生热。

### 热机与效率 (Heat Engines and Efficiency)

(Slide 15, 22)

-   **热机 (Heat Engine):** 一种将热能转化为有用功的装置。它通常在一个 **循环 (cycle)** 中工作，意味着工作物质 (working substance, e.g., gas) 经过一系列过程后回到其初始状态 ($\Delta U_{cycle}=0$)。
-   **工作原理 (Slide 15):**
    1.  从高温热库 ($T_h$) 吸收热量 $Q_h$。
    2.  对外做功 $W_{by}$。
    3.  向低温热库 ($T_c$) 排放废热 $Q_c$。
    4.  循环往复。
    **注意:** 热库是指足够大，以至于吸收或放出热量时其自身温度保持不变的系统。
-   **能量守恒 (Energy Conservation):** 对于一个完整的循环 $\Delta U_{cycle}=0$，根据热力学第一定律 $Q_{net} = W_{by}$。净吸收的热量 $Q_{net} = Q_h - Q_c$ (我们定义 $Q_h, Q_c, W_{by}$ 均为正值，代表其大小)。所以：
    $$
    W_{by} = Q_h - Q_c
    $$
-   **效率 (Efficiency) $\epsilon$ (Slide 22):** 定义为 "得到的有用功" 与 "付出的代价 (吸收的热量)" 之比。
    $$
    \epsilon = \frac{W_{by}}{Q_h} = \frac{Q_h - Q_c}{Q_h} = 1 - \frac{Q_c}{Q_h}
    $$
    效率表示有多少从高温热库吸收的热量被转化为了功。因为必须有废热 $Q_c$ 排出 (后面会看到这是第二定律的要求)，所以效率 $\epsilon$ 总是小于 1 (或 100%)。

### 斯特林循环 (Stirling Cycle) - 热机实例

(Slide 16-21)
![7cbd854c0b2dc203d2e45102162ec31.png](https://s2.loli.net/2025/04/28/UbjnMPGxRsFlOS6.png)


斯特林循环是一个由两个等温过程和两个等容过程组成的理想循环。
-   过程 1 ($4 \to 1$): 等容加热 ($V_a$ 不变, $T$ 从 $T_c$ 升到 $T_h$)。吸收热量 $Q_1 = C_V(T_h-T_c)$。
-   过程 2 ($1 \to 2$): 等温膨胀 ($T_h$ 不变, $V$ 从 $V_a$ 增到 $V_b$)。吸收热量 $Q_2 = W_2 = NkT_h \ln(V_b/V_a)$。
-   过程 3 ($2 \to 3$): 等容冷却 ($V_b$ 不变, $T$ 从 $T_h$ 降到 $T_c$)。放出热量 $|Q_3| = C_V(T_h-T_c)$。
-   过程 4 ($3 \to 4$): 等温压缩 ($T_c$ 不变, $V$ 从 $V_b$ 减到 $V_a$)。放出热量 $|Q_4| = |W_4| = NkT_c \ln(V_b/V_a)$。

-   **净功 (Net Work):** $W_{by} = W_2 + W_4 = NkT_h \ln(V_b/V_a) - NkT_c \ln(V_b/V_a) = Nk(T_h - T_c) \ln(V_b/V_a)$ (Slide 19)。这等于 P-V 图上封闭曲线所围的面积。
-   **总吸热 $Q_h$:** 来自高温过程的热量。在 Slide 20 中定义为 $Q_h = Q_1 + Q_2 = \alpha Nk(T_h-T_c) + NkT_h \ln(V_b/V_a)$。 (在实际的带回热器 (regenerator) 的斯特林发动机中，$Q_1$ 的热量可以由 $Q_3$ 放出的热量提供，此时 $Q_h$ 仅为 $Q_2$。但按此幻灯片的计算方式，我们用 $Q_1+Q_2$)。
-   **效率 (Efficiency):** $\epsilon = W_{by}/Q_h = \frac{Nk(T_h - T_c) \ln(V_b/V_a)}{\alpha Nk(T_h-T_c) + NkT_h \ln(V_b/V_a)}$。
-   **数值算例 (Slide 21):** 对于 $V_b=2V_a$, 单原子气体 $\alpha=3/2$, $T_h=373K$, $T_c=273K$，计算得到 $\epsilon \approx 16.9\%$。

### 热力学第二定律与卡诺效率 (The Second Law and Carnot Efficiency)

(Slide 23-27, 31)

-   **热力学第二定律 (The Second Law of Thermodynamics):** 有多种等价表述。这里用到的是克劳修斯表述的推论和熵表述：
    -   **开尔文-普朗克表述推论:** 不可能制造出一种循环工作的热机，只从一个热源吸热，将之完全转化为功，而不在低温热库留下任何其它变化 (即 $Q_c$ 不可能为零)。
    -   **熵表述:** 在任何涉及孤立系统的过程中，系统的总熵永不减少 ($\Delta S_{tot} \ge 0$)。对于可逆过程 $\Delta S_{tot}=0$，对于不可逆过程 $\Delta S_{tot}>0$。

-   **效率上限 (Maximum Efficiency):** (Slide 23-24)
    考虑任意一个在 $T_h$ 和 $T_c$ 之间工作的热机。在一个循环中，引擎本身熵变 $\Delta S_{engine}=0$。热库的熵变是 $\Delta S_{hot} = -Q_h/T_h$ (失去热量) 和 $\Delta S_{cold} = +Q_c/T_c$ (得到热量)。
    根据第二定律，总熵变 $\Delta S_{tot} = \Delta S_{engine} + \Delta S_{hot} + \Delta S_{cold} = 0 - Q_h/T_h + Q_c/T_c \ge 0$。
    整理得到：$\frac{Q_c}{T_c} \ge \frac{Q_h}{T_h}$，即 $\frac{Q_c}{Q_h} \ge \frac{T_c}{T_h}$。
    将此代入效率公式 $\epsilon = 1 - Q_c/Q_h$，得到：
    $$
    \epsilon \le 1 - \frac{T_c}{T_h}
    $$
    这个结果表明，任何在给定温度 $T_h$ 和 $T_c$ 之间工作的热机，其效率不可能超过 $1 - T_c/T_h$。这个上限被称为 **卡诺效率 (Carnot Efficiency)**：
    $$
    \epsilon_{Carnot} = 1 - \frac{T_c}{T_h}
    $$
    -   这是一个 **普适定律 (universal law)**，不依赖于工作物质或热机的具体设计。
    -   只有 **可逆热机 (reversible engine)** 才能达到卡诺效率 (此时 $\Delta S_{tot}=0$，不等号取等号)。
    -   提高效率的方法：提高 $T_h$ 或降低 $T_c$ (Slide 25)。

-   **卡诺循环 (Carnot Cycle):** (Slide 27)
    为了达到卡诺效率，热机必须只由可逆过程组成。卡诺设计了一个理想的可逆循环，由以下四个过程组成：
    1.  等温膨胀 (Isothermal expansion) at $T_h$。
    2.  绝热膨胀 (Adiabatic expansion) (温度从 $T_h$ 降到 $T_c$)。
    3.  等温压缩 (Isothermal compression) at $T_c$。
    4.  绝热压缩 (Adiabatic compression) (温度从 $T_c$ 回到 $T_h$)。
    由于所有过程都是可逆的，卡诺循环的效率等于 $\epsilon_{Carnot}$。

-   **效率损失与熵产生 (Efficiency Loss and Entropy Production):** (Slide 26, 31)
    对于任何不可逆的热机 ($\Delta S_{tot} > 0$)，其效率必然低于卡诺效率。效率损失的大小与总熵产生 $\Delta S_{tot}$ 直接相关：
    $$
    \epsilon = \epsilon_{Carnot} - \frac{T_c \Delta S_{tot}}{Q_h}
    $$
    要提高效率，就要尽量减少系统中的不可逆性（减少熵产生）。

### 制冷机与热泵 (Refrigerators and Heat Pumps)

(Slide 28-30)

热机是利用温差做功，反过来，我们可以利用功来传递热量，这就是制冷机和热泵。它们的工作原理本质上是热机循环的逆转。

-   **性能系数 (Coefficient of Performance, COP):** 用于衡量制冷机和热泵的性能，定义为 "得到的结果" / "付出的代价 (输入的功)"。

-   **制冷机 (Refrigerator):**
    -   目标：从低温处 ($T_c$) 移走热量 $Q_c$ (使其保持低温)。
    -   代价：需要输入功 $W_{in}$ (注意 $W_{in}$ 在图中标记为 $W_{on}$)。
    -   能量守恒：$Q_h = Q_c + W_{in}$ (向高温环境 $T_h$ 排出总热量 $Q_h$)。
    -   性能系数：$\text{COP}_{Ref} = K = \frac{Q_c}{W_{in}}$。
    -   卡诺制冷机制冷系数 (上限):
        $$
        K_{Carnot} = \frac{T_c}{T_h - T_c}
        $$

-   **热泵 (Heat Pump):**
    -   目标：向高温处 ($T_h$) 输送热量 $Q_h$ (例如给房间供暖)。
    -   代价：需要输入功 $W_{in}$。
    -   能量守恒：$Q_h = Q_c + W_{in}$ (从低温环境 $T_c$ 吸收热量 $Q_c$)。
    -   性能系数：$\text{COP}_{HP} = K' = \frac{Q_h}{W_{in}}$。
    -   卡诺热泵制热系数 (上限):
        $$
        K'_{Carnot} = \frac{T_h}{T_h - T_c}
        $$
    -   关系：$\text{COP}_{HP} = \text{COP}_{Ref} + 1$。

-   **重要特点:** 当温差 $T_h - T_c$ 很小时，制冷机和热泵的 COP 可以远大于 1。这意味着它们传递的热量可以远大于驱动它们所需的功。例如，Slide 30 的例子中，只需 8.5W 的功率就能将 70W 的热量从冰箱内部抽出。

## Lecture 8: Reversible Processes


### 热力学基本概念回顾

-   **系统 (System) 与环境 (Environment):** 在热力学中，我们通常关注一个特定的**系统** (例如，气缸中的气体) 以及它周围的**环境** (Surroundings)。
-   **热机示意图 (Heat Engine Diagram):** Slide 2 展示了一个典型的热机模型。
    -   它从高温热源 (Hot Reservoir) $T_H$ 吸收热量 $Q_H$。
    -   一部分能量转化为功 (Work) $W_{out}$ 输出。
    -   剩余的热量 $Q_C$ 排放到低温热源 (Cold Reservoir) $T_C$。
-   **四种基本热力学过程 (Four Thermodynamic Processes, Slide 3):**
    -   **等容过程 (Isochoric Process):** 体积 $V$ 保持不变。在 P-V 图上是一条垂直线。
    -   **等压过程 (Isobaric Process):** 压强 $p$ 保持不变。在 P-V 图上是一条水平线。过程中做的功是 $W = p \Delta V$，在 P-V 图上是曲线下的面积 (灰色区域)。
    -   **等温过程 (Isothermal Process):** 温度 $T$ 保持不变。对于理想气体，P-V 图上是一条双曲线 ($p \propto 1/V$)。
    -   **绝热过程 (Adiabatic Process):** 系统与外界没有热量交换 ($Q=0$)。对于理想气体，P-V 图上也是一条曲线 ($p \propto 1/V^\gamma$)，通常比等温线更陡峭 (steeper)。

![e13f1eb815995276c7110a9ccf68fa2.png](https://s2.loli.net/2025/04/29/6sRflQpdxAkrGUj.png)



### 可逆过程与熵 (Reversible Processes and Entropy)

-   **可逆过程的定义:** 一个过程是可逆的，意味着系统和环境**总能**恢复到初始状态，并且在外界不留下任何变化。
-   **可逆过程的熵条件 (Entropy Condition for Reversibility):** 一个过程是可逆的，其**充要条件**是系统与环境的总熵变 (Total Entropy Change) 为零。
    $$
    \Delta S_{TOT} = \Delta S_{system} + \Delta S_{environment} = 0
    $$
    -   这意味着在可逆过程中，**没有净熵产生 (No net entropy is produced!)** (Slide 5)。

-   **可逆过程的类型 (Types of Reversible Processes, Slide 5):** 在热力学中，只有两种基本类型的过程可以是可逆的：
    1.  **准静态绝热过程 (Quasi-static adiabatic processes, $Q=0$)**
    2.  **准静态等温过程 (Quasi-static isothermal processes, T constant)**
    -   **准静态 (Quasi-static):** 指过程进行得**极其缓慢**，系统在任何时刻都无限接近于平衡态 (Equilibrium)。这是实现可逆性的必要条件，但不是充分条件 (还需要无摩擦等)。

> [!tip] 准静态 vs. 可逆过程 (Quasi-static vs. Reversible Processes)
> -   **关系:**
> 	-   **所有可逆过程都必须是准静态的 (All reversible processes are quasi-static)** 。因为如果过程不是缓慢进行的，系统内部就会出现不平衡 (如压强差、温度差)，导致熵产生，从而不可逆。
> 	-   **但并非所有准静态过程都是可逆的 (Not all quasi-static processes are reversible)**。例如，一个缓慢进行的有摩擦的过程，虽然是准静态的，但摩擦会产生熵，因此是不可逆的。
> 	-   **技术比喻:** 缓慢地 (准静态地) 移动一个物体，如果在有摩擦的表面上移动，能量会因摩擦转化为热量 (熵增加)，这个过程无法完美倒过来让热量变回机械能并将物体推回原处，所以是不可逆的。只有在理想的无摩擦表面上缓慢移动，才可能是可逆的。



### 非平衡过程 (Non-equilibrium Processes, Slide 6)
![43307080d4d858956771af55a543b9f.png](https://s2.loli.net/2025/04/29/t7h83dsARgoI6Ew.png)

-   **自由膨胀 (Free Expansion):** Slide 6 的例子是一个典型的**非平衡过程**。气体突然冲入真空区域。
    -   这是一个**快速**过程，不是准静态的。
    -   系统在膨胀过程中并不处于平衡态，因此我们不能用 $pV=NkT$ 这样的状态方程来描述中间过程 (只能描述初始和最终的平衡态)。
    -   由于是向真空膨胀，气体不对外做功 ($W=0$)。如果容器绝热 ($Q=0$)，根据热力学第一定律 $\Delta U = Q - W = 0$，理想气体的内能不变，因此温度也不变。
    -   尽管能量守恒且温度可能不变，但这是一个**高度不可逆**的过程，总熵是显著增加的 ($\Delta S_{TOT} > 0$)。

### 绝热与等温过程详解 (Detailed Look at Adiabatic and Isothermal Processes)

-   **绝热过程 (Adiabatic Process):**
    -   $Q=0$ (系统与外界无热量交换)。
    -   对于**可逆 (准静态) 绝热过程**，熵变 $\Delta S = \int dQ/T = 0$。系统熵不变。
    -   对于理想气体，该过程遵循 $p V^\gamma = \text{const}$，其中 $\gamma = C_p/C_v$ 是绝热指数 (adiabatic index)，也等于 $(\alpha+1)/\alpha$，这里 $\alpha = N_{DOF}/2$ (自由度的一半)。
-   **等温过程 (Isothermal Process):**
    -   $T = \text{const}$ (系统与一个恒温热库接触)。
    -   对于**可逆 (准静态) 等温过程**，系统与热库之间有热量交换 $Q$。
    -   系统熵变 $\Delta S_{sys} = Q/T$ 
    -   热库 (环境) 熵变 $\Delta S_{res} = -Q/T$ (与系统熵变大小相等，符号相反)。
    -   总熵变 $\Delta S_{tot} = \Delta S_{sys} + \Delta S_{res} = 0$。
    -   对于理想气体，该过程遵循 $p V = \text{const}$ (即 $p = \text{const} / V$)。

### 热机效率与制冷机制冷系数 (Efficiency and COP)

-   **通用评价指标 (General Form):** 性能 = 你得到的 (What you get) / 你付出的 (What you paid for)。
-   **热机效率 (Engine Efficiency, $\epsilon$):**
    -   **得到:** 做出的功 $W$。
    -   **付出:** 从高温热源吸收的热量 $Q_H$ (例如，燃料燃烧产生的热量)。
    -   $\epsilon = \frac{W}{Q_H}$。根据能量守恒 $W = Q_H - Q_C$，所以 $\epsilon = \frac{Q_H - Q_C}{Q_H} = 1 - \frac{Q_C}{Q_H}$。
-   **制冷机性能系数 (Refrigerator COP):**
    -   **得到:** 从低温物体 (冰箱内部) 移走的热量 $Q_C$。
    -   **付出:** 消耗的功 $W$ (例如，压缩机消耗的电能)。
    -   $COP_{ref} = \frac{Q_C}{W}$。

-   **热泵性能系数 (Heat Pump COP):**
    -   **得到:** 向高温物体 (室内) 输送的热量 $Q_H$。
    -   **付出:** 消耗的功 $W$ (例如，电能)。
    -   $COP_{HP} = \frac{Q_H}{W}$。
    -   注意 $Q_H = W + Q_C$，所以 $COP_{HP} = \frac{W+Q_C}{W} = 1 + COP_{ref}$。热泵的 COP 通常大于 1。

### 卡诺循环与卡诺效率 (Carnot Cycle and Efficiency, Slide 10, 14, 18)

-   **卡诺循环 (Carnot Cycle):** 由两个可逆等温过程和两个可逆绝热过程组成的理想热力学循环。


-   **卡诺定理 (Carnot's Theorem):** 在相同的高温热源 $T_H$ 和低温热源 $T_C$ 之间工作的所有热机中，**可逆热机 (如卡诺热机) 的效率最高。所有可逆热机在该条件下效率都相同**。

-   **卡诺效率 (Carnot Efficiency, $\epsilon_{Carnot}$):**
    $$
    \epsilon_{Carnot} = 1 - \frac{T_C}{T_H}
    $$
    -   这是理论上的最大效率。**注意：温度 $T_H$ 和 $T_C$ 必须使用绝对温标 (开尔文 Kelvin, K)。**
    -   对于**可逆循环 (卡诺循环)**，有 
    $$\frac{Q_C}{Q_H} = \frac{T_C}{T_H}$$
-   **不可逆性对效率的影响 (Inefficiency due to Irreversibility):**
    -   对于**任何**在 $T_H$ 和 $T_C$ 之间工作的热机，总熵变 $\Delta S_{total} = \frac{Q_C}{T_C} - \frac{Q_H}{T_H} \ge 0$ (等号仅对可逆过程成立)。
    -   实际效率 $\epsilon$ 与卡诺效率的关系为：
        $$
        \epsilon = 1 - \frac{Q_C}{Q_H} = 1 - \frac{T_C}{T_H} \left( \frac{Q_C/T_C}{Q_H/T_H} \right)
        $$
        推导:
        从 $\Delta S_{total} = \frac{Q_C}{T_C} - \frac{Q_H}{T_H}$ 可得 $\frac{Q_C}{T_C} = \frac{Q_H}{T_H} + \Delta S_{total}$。
        所以 $\frac{Q_C}{Q_H} = \frac{T_C}{T_H} + \frac{T_C \Delta S_{total}}{Q_H}$。
        代入效率公式 $\epsilon = 1 - \frac{Q_C}{Q_H}$：
        $$
        \epsilon = 1 - \left( \frac{T_C}{T_H} + \frac{T_C \Delta S_{total}}{Q_H} \right) = \left( 1 - \frac{T_C}{T_H} \right) - \frac{T_C \Delta S_{total}}{Q_H}
        $$
        即：
        $$
        \epsilon = \epsilon_{Carnot} - \frac{T_C \Delta S_{total}}{Q_H}
        $$
    -   由于 $\Delta S_{total} \ge 0$, $T_C > 0$, $Q_H > 0$，所以实际效率 $\epsilon \le \epsilon_{Carnot}$。任何不可逆因素 ($\Delta S_{total} > 0$) 都会降低热机效率。
    -   卡诺热机是理想化的，现实中无法完全实现，因为它要求过程无限缓慢且没有摩擦等损耗。


### 可选内容: 理想气体绝热过程公式推导 (Optional: Adiabatic formula)

-   Slide 20 提供了一个推导理想气体准静态绝热过程 $PV^\gamma = \text{const}$ 的过程。
-   它结合了以下三个基本定律：
    1.  **理想气体状态方程 (Ideal gas law):** $pV = NkT$ 及其微分形式 $pdV + Vdp = NkdT$。
    2.  **热力学第一定律 (1st law of Thermo):** 对于绝热过程 $dQ=0$，所以 $dU = -pdV$。
    3.  **能量均分定理 (Equipartition theorem):** 理想气体内能 $U = \frac{N_{DOF}}{2} NkT$，其微分形式 $dU = \frac{N_{DOF}}{2} NkdT$ (其中 $N_{DOF}$ 是每个分子的自由度)。
-   通过联立和积分这些方程，最终可以得到 $PV^\gamma = \text{const}$，其中 $\gamma = (N_{DOF}/2 + 1) / (N_{DOF}/2) = C_p/C_v$。
