---
title: Pairs trading
date created: 星期一, 五月 27日 2024, 11:46:54 中午
date modified: 星期一, 六月 3日 2024, 10:57:52 晚上
categories: Quantitative_Finance
---

## Basic ideas:

1. Statistical strategy -> try to build correlations between different stocks
2. Example  
   When a well established price correlation between A and B broke down, i.e. stock A traded up while B traded down, they would sell A and buy B, betting that the spread would eventually converge.
3. Advantages: Market Neutrality
   - Market neutral: trading strategies which are independent of market movements are said to be market neutral
   - Pair trading is mean-reverting strategy, assuming that prices will revert to historical trends and it is largely self-funding.
4. Risks:
   - Transaction cost
   - Involution
   - The increased divergence -> rational response to news about one of the companies

## Strategy Specification

1. Correlation built:  
   Pairs were formed based on price correlations over a 12-month period, starting every month
2. Trading:  
   Each pair was then traded (possibly multiple times) over the next six months.  
   The pair was “bought” when its ratio spread was outside two standard deviations of its 12-month spread. If normally distributed, this should happen about 5% of the time.
3. Pair Formation:  
   A matching partner for each security was found by minimizing the squared deviations between the two normalized daily price series, where dividends were reinvested.
4. Return Computation:  
   Pairs that open and converge will have positive cash flows; Pairs that open but do not converge will have positive or negative cash flows on the last day of the trading interval when all positions are closed out