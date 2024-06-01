---
title: Portfolio Optimization
date created: 星期一, 五月 27日 2024, 11:46:54 中午
date modified: 星期六, 六月 1日 2024, 11:08:06 晚上
---

投资组合优化

## General Idea

1. Financial optimization:
   - Variables: Amounts invested in each asset 
   - Constraints: budget, investment per set, minimum return 
   - Objective:  Maxize proft, Minimize risk
2. Machine learning:
   - Variables: Model parameters
   - Constraints: Prior information, parameter limits
   - Objective: Minimize prediction error
3. Method:
   - least squares
   - linear optimization
   - convex optimization
4. Basic terms:
   - allocation weights:
     - 总资产:V
     - w: n维向量->记录给每个资产分配的权重
     - Property:  
       $V_(w_j)$ dollar value hold in asset j  
       w中分量线性和为1（齐次）  
       $w_j < 0$ means short positions(borrow)
   - Return over a period:
     - Asset return: $\hat{r_t}$ the farctional return vector of each asset
     - Portfolio return: $r_t$ = $\hat{r_t^T}w$ the return for the entire portfolio over period t
     - Total porofolio value after a period  
       $$ V_{t+1} = V_t + V_t\hat{r_t^T}w = V_t(1+r_t)$$

## Linear optimization

1. Average return:  
   $$ avg(r) = \frac{\sum_{t=1}^T{R_t}}{T} = \mu^Tw $$
   - Average return calculate the average return value over period T;
   - Additionally, $\mu$ is n-dimensional vector, representing the average return of each asset,it can be calculated by $$\mu = \frac{R^T}{T} \text{and $R^T$ is a n*T matrix, including all assets' return rate over the whole period} $$
2. 1-nrom Risk Approximation(1-范数风险近似):  
   Notice: It is no longer standard deviation(标准差)  
   $$||r-avg(r)1||_{\frac{1}{T}}$$

3. Risk-Return Objective:  
   Objective = $\mu^Tw - \frac{\sum_{t=1}^T(R_tw-\mu^Tw)^2}{T} + \text{(trade off parameter)}$  
   $\frac{\sum_{t=1}^T(R_tw-\mu^Tw)^2}{T}$ is the risk evaluation over time
    
   
   
   






























