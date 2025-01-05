---
title: Number Theory
date: 2024-10-16
date modified: 2024-12-02
categories: Math213
tags: [Math213]
---

#Math213 

## Basic

### Division 整除

![bfa319fb03e65b9ec7ddef185c65366.png](https://s2.loli.net/2024/10/16/dBu8f5FnrUITiet.png)
- **带余除法**  
divisor: 除数， dividend: 被除数， quotient 商，remainder 余数  
![194d6cb7ed2c2c54d62b00b0165b439.png](https://s2.loli.net/2024/10/16/A4hgZlYRsMJvyIQ.png)  


![d556cce7d0e770032e02af452b2653c.png](https://s2.loli.net/2024/10/16/hL3lQM5sHf1BZTq.png)

注意带余除法的计算复杂度通过位运算简化可实现 $O(q\log a)$ 量级

- **同余** congruent  
![1ba8b0c976fe12f075eb7c041e7a03a.png](https://s2.loli.net/2024/10/16/9dvMlOFuSqwDCU7.png)  
![b2f624215e524eea85d0add3dfd0c38.png](https://s2.loli.net/2024/10/16/spVjtLFnkTD9WcZ.png)  
![e335986f079be96146718d2c2895dfc.png](https://s2.loli.net/2024/10/16/wmhj25QLPrTeKAB.png)
- **mod m 的剩余系**

 ![56c3e382e9022b3d4cd7f3b042ab160.png](https://s2.loli.net/2024/10/16/aTJO23Qp1gw9xto.png)  
![e08e00d041ee07e063abe4be914886f.png](https://s2.loli.net/2024/10/16/mYVPu5IABoOr23c.png)

### 整数进制表示

![b3d64ab476dec6654958ce1d0eb7bb4.png](https://s2.loli.net/2024/10/16/xDA3Lm8z4v65tnP.png)  
![fbb18f9f094ae94e98c04579f617ba2.png](https://s2.loli.net/2024/10/16/HzXmBENq8OcZKnd.png)

### Algorithm for Integer Operations

**Multiplication**  
![a65386426cb9a72b84087cca20398f9.png](https://s2.loli.net/2024/10/16/lMORCZfNXbh27rA.png)  
**Binary  Modular Exponentiation**  
![bc92642a48cd17fc3effb2bf7bcd460.png](https://s2.loli.net/2024/10/16/NKRMJO86HWtI4sq.png)

### 质数

![0988e37c7eb7579d09f7209377932b7.png](https://s2.loli.net/2024/10/16/Rnq8tEKOirsdgBz.png)  
Prime: 质数  
Composite：合数

### 最大公约数 (GCD) 与最小公倍数 (LCM)

![259d66ea5f8053efed57d00863996cc.png](https://s2.loli.net/2024/10/16/bAsx42X9Dnyfjv6.png)  
![a29bce1552bda518904e68a4393a9d0.png](https://s2.loli.net/2024/10/16/NOqBC6UsyHrZAJT.png)  
![8c5e3af43c5b1932801a687166b9566.png](https://s2.loli.net/2024/10/16/PAH6QCoRJlxfvS8.png)

**辗转相除求 GCD**: 直接写出辗转相除的过程，然后将中间量一步步向前代换，得到 gcd 作为两数线性表示的最小值  
![d9847900521925892bbf591893a2fd3.png](https://s2.loli.net/2024/10/16/zdFMLNUPExOSlRe.png)

**裴蜀定理：GCD 为两者的线性表示**  
![d36d6d73d5a3b86637d8cda2ba40b4a.png](https://s2.loli.net/2024/10/16/FWGKlR6hYSiwszr.png)

![ef5243adb0383ef0daee370510818c1.png](https://s2.loli.net/2024/10/16/kGhoAtEMgeLNiCU.png)  
**注意：可以利用裴蜀定理得出 gcd 的线性表示确定不定方程的解集**


![8b0cefa0c08509fb2ef4a140b004c6f.png](https://s2.loli.net/2024/10/16/PmED5loxgNWbf73.png)

### 线性同余

![514612f7f0b8e537ac13a83791a6292.png](https://s2.loli.net/2024/10/16/VOCESTN7t3Ayghr.png)

**逆**：
- **当 a,m 互素时，存在 a 模 m 的逆**  
![c1ec69a4d9de211062db75d6eb68b86.png](https://s2.loli.net/2024/10/16/ejPh6IBHb9MrFEo.png)

- **求解逆：考虑利用 gcd 的线性表示辗转相除**  
![f2644877ed38fef689706bc68b41e1a.png](https://s2.loli.net/2024/10/16/nQiOao84wyGAfJP.png)


![2d2ec565b512573ae295d3062c0bbba.png](https://s2.loli.net/2024/10/16/whtXRJaPDEUKqTj.png)


**中国剩余定理**  
![356fa8af191d14a32bb06186ea4e2be.png](https://s2.loli.net/2024/10/16/RlAHdXWB2wSJyxi.png)

**注意 CRT 解的构造过程**：  
记

$$
M_{i} = \frac{m}{m_{i}}
$$

对于每一个 $M_{i}$, 我们考虑其模 $m_{i}$ 的逆

$$
M_{i}y_{i} \equiv 1 \pmod{m_{i}}
$$

最终若有 $m_{i}$ 两两互素，我们有模 m 意义下的唯一解：

$$
x \equiv \sum_{i=i}^{n}a_{i}M_{i}y_{i}
$$

## Crytography

### Pseudorandom Number Generators

**利用线性同余递推数列生成随机数**  
![ebe7f01acd412d1f0c1f79bd2d5b48b.png](https://s2.loli.net/2024/10/26/zhJyQvlTacuDfxM.png)

### Hash Functions

**Definition**  
![e3b18a5170d5a1509e4069138bfbfd1.png](https://s2.loli.net/2024/10/26/JwOKiblYZFqT18R.png)  
将任意长度的数据映射到固定长度的数据

**Common Solution**  
直接利用同余函数进行映射  
![f55042dd29687a469b17ea602c547c9.png](https://s2.loli.net/2024/10/26/aveTqZ2pHgwFYtr.png)  
避免同余后的结果映射到相同位置 ->Assign Free Location following the occupied memory location assigned by the hashing function(即将对应的映射结果向后递推)  
![d82d218ada9f23090d26696483ed2fe.png](https://s2.loli.net/2024/10/26/m6VeizGIKfjO3dL.png)

### Cryptography

#### Shift Ciphers

**将明文加上偏移量后关注其在完全剩余系中的结果**  
![cf0675df79beedcdbdad69fb946ddf2.png](https://s2.loli.net/2024/10/26/ugalMsb71hViIR9.png)  
![a6eb365b3272be739e8c9898fd433cd.png](https://s2.loli.net/2024/10/26/W5nMDIXByVFfCb6.png)

**复杂化 ->考虑引入一个与模互素的数，构造新的完全剩余系**  
![9a2a5d1e2a0beaaee1fa84feb661078.png](https://s2.loli.net/2024/10/26/oKymnWaEb9Bzdk5.png)

#### Private/Public Key Cryptosystem

**Public Key Cryptosystem**  
![92d3706017f339c5028a26f5379c286.png](https://s2.loli.net/2024/10/26/yLmr2Tu6xEegSpi.png)

**RSA Cryptosystem**
- **原理**  
![dd4504731ea57d5272351b2a5572da8.png](https://s2.loli.net/2024/10/27/Mv8Q217uFs9EnIK.png)  
![a1da575a670448681d4cd2c52931fea.png](https://s2.loli.net/2024/10/27/87bKeirvRwqjlfE.png)

公钥：(n,e)  
私钥：(d)  
注意核心的大素数一定需要保密

- **例子**：  
![ac0ef3ef7380adc65b5cc388a695d6e.png](https://s2.loli.net/2024/10/27/A56T2ZXP1OB8ona.png)  
![9307e0f225d4c4e90a8b1d457886bec.png](https://s2.loli.net/2024/10/27/Y6EakDGXhubNASz.png)

- 应用  
![e24a15f958cb1b704384f99c7238a70.png](https://s2.loli.net/2024/10/27/p8luY4jvmZwi5Sr.png)



![b899bd7ac6ace36a18572b370b32131.png](https://s2.loli.net/2024/10/27/EL7oNv1bQsgDcaS.png)

![9545e644e671f519c9bb6f6490e47c4.png](https://s2.loli.net/2024/10/27/JMyqG9YBiAVQSge.png)

- **关注原根的概念**：素数的原根即为其最小生成整个 modp 完系的生成元

### Blockchain