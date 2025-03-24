---
title: Circuit Basics
date: 2025-02-21
date modified: 2025-03-10
categories: ECE210
tags: [ECE210]
---

#ECE210

## Ideal Circuit Elements 

### Sources

**1. Independent Sources*

**独立电压源**  
独立电压源能够维持两极的固定电势差，与通过的电流大小无关

**独立电流源**  
独立电流源能够维持通过该元件的电流恒定，不受两端电压的影响

**2. Dependent sources**  
![79eaaea396f10fb43d10f2abafc6a15.png](https://s2.loli.net/2025/02/21/1VerYiKBPgopdOI.png)  
非独立电流源或电压源受电路中其他处的电压或电流影响

### Capacitors & Inductors

![819b38850786e1b38403ddc80eb2fff.png](https://s2.loli.net/2025/02/21/RDGCI9jrmicNxSf.png)  
**AC 电路中，电容储存的能量**：

$$
\begin{align}
& p = vi = vC \frac{dv}{dt} = \frac{d}{dt} \left( \frac{1}{2}Cv^{2} \right) \\
& w = \frac{1}{2}Cv^{2}
\end{align}
$$

**AC 电路中，电感储存的能量**

$$
w = \frac{1}{2}Li^{2}
$$

## Linear Circuit

### Linearity

![a867cde9d809c3c17c8ccba975956b7.png](https://s2.loli.net/2025/02/24/dWbML6lFTGeN9mu.png)  
**线性电路（Linear Circuit）** 是指电路中的电压和电流之间的关系是线性的，也就是说电路的响应遵循叠加原理。在线性电路中，电流和电压的变化成正比，并且电路的元素（如电阻、电感、电容等）满足线性方程。

**常见线性电路**
- 纯电阻电路为线性电路
- 包含电容、电感的电路也可以为线性电路
- 若电路中存在非线性 $i-v$ 关系的元件（例如二极管）则系统为非线性电路

### Superposition 

![1180dee412b8bc1f5fd51c162db30b5.png](https://s2.loli.net/2025/02/24/f7QZMm4eOzF2x8t.png)

**线性电路中的叠加原理（Superposition Principle）** 的核心思想是：对于线性电路，多个电源（电压源或电流源）共同作用时，电路的总响应（如电流、电压）等于每个电源**独立作用**时产生的响应的代数和。

1. **对于每个电源，考虑其单独对电路的影响**：
    
    - **暂时去除所有其他电源**：在分析每个电源时，将电路中的其他电源“去掉”。
        - 对于**电压源，将其短路（即将电压源替换为一根导线，电压为 0）**。
        - 对于**电流源，将其开路（即将电流源替换为断路，电流为 0）**。
    - 然后，分析剩余电路中电源的作用，计算出由该电源单独引起的电流或电压。
2. **重复这一过程，分别计算每个电源的贡献**：
    
    - 对于每一个电源，重复上述过程，单独计算它所引起的电流或电压。
3. **将所有电源的响应代数求和**：
    
    - 由于线性电路遵循叠加原理，最终的电流或电压等响应等于各个电源独立作用时产生的响应之和。

### Thevenin & Norton Equivalents

#### Thevenin Equivalents

**Thevenin 等效电路的结构**

Thevenin 等效电路由 **一个独立电压源** 和 **一个串联电阻** 组成：

- **$V_{th}$（Thevenin 等效电压）**：它等于原电路在负载端口**开路**时的电压（即开路电压）。
- **$R_{th}$​（Thevenin 等效电阻）**：它等于从端口看进去，所有独立电源被关掉（**电压源短路、电流源开路**）后的等效电阻

#### Norton Equivalents

**Norton 等效电路的结构**

Norton 等效电路由 **一个独立电流源** 和 **一个并联电阻** 组成：

- **$I_{N}$​（Norton 等效电流）**：它等于端口短路时的电流（即短路电流）。
- **$R_{N}$（Norton 等效电阻）**：它等于从端口看进去的等效电阻，计算方法与 Thevenin 相同

#### 相互转换

- **Thevenin → Norton**：

$$
I_{N} = \frac{V_{th}}{R_{th}}, R_{N}=R_{th}
$$

- **Norton → Thevenin**： 

$$
V_{th} = I_{N}\times R_{N}, R_{th} = R_{N}
$$

#### Test signal method for dependent sources

**测试信号法的基本原理**  
**核心思想：**

- **引入一个测试信号**（测试电压 $V_{test}$​ 或测试电流 $I_{test}$，以激励电路，迫使受控源工作。
- **计算响应**：去除所有独立电源（电压源短路，电流源断路，**受控源保留**）计算流过端口的电流或电压，以确定等效电阻。

## Available Power & Maximum Power Transfer

**Available Power**

$$
P = \frac{V_{Th}^{2}}{R_{Th}} 
$$

![2c0ac8b08e8225d80a8301e26cfd2cc.png](https://s2.loli.net/2025/02/24/uPVQHOsKbwTJx4e.png)

负载功率最大条件：

$$
R_{L} = R_{th}
$$