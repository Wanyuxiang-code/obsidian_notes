---
---

## Types of risks
- Specific risks: associated with a specific asset
- Systematic risks: common to all securities
## Diversification and Portofolio theory
1. Argument:
   The theroy assumes that the risk-return profile of a portfoliocan be optimized, where an  optimal portfolio displays the lowest possible level of risk for its level of return.
   - Varience calculation:
     $$\sigma^2 = (\sum_{i=1}^n{w_i\sigma_i})^2$$
     $$ \sum_{i=1}^n{w_i} = 1$$
2. Strategy:
   - Uncorrelated returns:
     Select securities whose performance is uncorrelated or negatively correlated
   - Portfolio with short sales:
     Allow short sales: sell short sells of the lower return asset and use the proceeds to nuy the higher return one(Applying leverage)
   - The Portfolio Frontier(visualization):
     Represents whether the current portfolio can be optimized to reach the frontier
   - **Competitive Analysis**:
     1. Motivation:
        - typical statistical method: only access to all the relevant information
        - online problemL continually produces new input and requires answers in response 
	 2. Effectiveness analysis:
	    Comparison object: offers a worst measure of the quality of the behavior of an algorithm which predicts the fufure
	 3. Competitive Ratio: Determine the linear cofficient
	    ALF(I)    $\leq$     c$*$OPT (I) + $\alpha$
     4. Examples:
        - Price searching:
          Sell when the price reach the case either the it goes to max or min are OK
          RPP(reservation price policy) :
          global fluctuation ratio: $\phi = \frac{M}{m}$
          competitive ratio: $c = \frac{\sqrt{Mm}}{m} = \sqrt{\phi}$
        - Randomized Algorithms:
          Make it difficult for an adversary to design a future that is bad for you
        - One-way trading
          Liquidate my position in a stock -> more flexibility, less market impact, less risks
	    - Threat-based strategy:
	      The threat-based strategy sells only when the price hits a new maximum. It sells just enough to ensure that we achieve a competitive ratio of c if the price drops to m for the rest of the game
	    - **Randomized Strategies**:
	    - Rebalancing Algorithms(adjust the weights of different stocks):
	    - Two-way trading:
	      - Two-way trading is a special case of online portfolio selection where you have only cash and one other security you can hold
	      - put all your assets into the security on any day it offers positive returns. Otherwise, put everything into cash.
        - **The (n,$\phi$) Adversary**:
          