---
title: Technical Analysis
date created: 星期一, 五月 27日 2024, 11:46:54 中午
date modified: 星期六, 六月 1日 2024, 2:08:43 下午
---

## General picture
技术分析：
Based on the past market data including prices and volumes to analyze or predict the direction of prices.

## Technical indicators(技术指标)
### Trend indicator
   - Simple  Moving Average(SMA):
     1. principle:
        calculate the average history data and can adjust the duration of history to determine the trend duration
     2. trading strategy:
        Bullish(看涨): when a more sensitive SMA crosses less sensitive SMA from below -> the current market favor
        Bearlish(看跌): when a more sensitive SMA crosses less sensitive SMA from above
   - Exponential Moving Average(EMA):
     1. principle:
        Based on the data of SMA, calculate the different weights of different history periods. 
     2. Characteristic:
        It can help smooth out price data over a certain period of time and minimize the impact of random price spikes.
        It is more sensitive to more current prices by stressing their weights.
   - Moving Average Convergence /Divergence(MACD):
     1. sum: momentum oscillator primarily used to trade trends
     2. construction:
        MACD line: 12-period EMA - 26-period EMA
        Signal line: 9-period EMA of the MACD line
     3. working principles:
        Notice: it assumes that the price should retain the previous history values
        It can help the analysts to gain insights into the market trend
        When MACD crossing above the zero line -> bullish
        When MACD crossing below the zero line -> bearish 
   - Average Directional Movement Index(ADX)*
     1. sum: measure the overall **strength** of a trend, itself can't tell the direction of the trend
     2. constructions:
        - Directional Movement(DM): compare the current period price range with the previous period price range.
          H_c + L_c > H_p + L_p -> PDI exist
        - TR = max{current high - current low; current high - previous low; current low -previous low}
     3. Interpretations:
        - Values range form 0 to 100, and ADX > 25: strong trend, ADX < 20: weak trend or trading average environment
        - ADX rising -> The trend is getting stronger
     
### Momentum Indicators
- Overbought and Oversold in Oscillators
  1. definition of oscillator
     Indicators which are bounded
  2. Overbought: the oscillator reaches a zero close to upper bound
  3. Oversold: the oscillator reaches a zero close to lower bound
  4. Strategy:
     If the oscillator reaches either bound -> the market is vulnerable to reversal(which may indicate the trend change)
     However, if the trend of the market is changing, the prediction of oscillator will fail -> It is dependent on the underlying trend
     即通过历史高位与低位来判断当下某些资产的价格趋势
- Stochastic Oscillator(随机指标):*
  1. Geberal ideas: When the market favors, the close price tends to approach the upper bound of a period price; When the market disfavors, the close price tends to approach the lower bound of a period price
  2. It compares a particular closing price of an asset to a range of its prices over a certain period
  3. Interpretations:
     A sell signal is given when the oscillator is above the 80 level and then crosses back below 80. Conversely, a buy signal is given when the oscillator is below 20 and then crosses back above 20
- Relative Strength Index:
  1. Sum: measures the speed and change of price movements
  2. Interpretations:
     The RSI oscillates from zero and 100. Traditionally, the RSI is considered overbought when above 70 and oversold when below 30.
### Volume Indicators
- General Rules:
  1. Increasing volume reinforces the trend directions
  2. Declining volume diminishes the trend directions
  3. A price peak or trough(谷) on ultrahigh volume is often an important reversal point in a trend
  4. Volume indicators should be considered warnings but not signals of change in trend directions
- On Balance Volume(OBV):
  1. Descriptions:
     measures buying and selling pressure as cumulative indicator
  2. Calculation:
     Volumes(up days) - Volumes(down days)
  3. Interpretations:
     The volumes are often seen as indicators of market expectations. So when OBV is rising -> bullish trend and when OBV is decreasing -> price down
     Divergence: If the price is up but the OBV is decreasing - > may indicate a reversal 
- Money Flow Index:
  1. Components
     Typical Price(TP): average of high, low and close price
     Raw Money Flow(RMF):TP /* Volume
     Money Flow Ratio(MFR): calculate by sum the positive RMF and negative RMF
  2. Interpretations:
   Overbought/Oversold: An MFI of over 80 suggests that the security is overbought and could be primed for a price decline. Conversely, an MFI under 20 suggests the security may be oversold and potentially ready to bounce back.
- Accumulation/Distribution:
  1. definition:
     accumulation: People are actively buying a security over a period
     distribution: Sellers are controlling the market and the stock price is likely to be under pressure or decreasing
  2. calculations:
     $$Multiplier = \frac{2*Close-Low-High}{High-Low}$$$$Money Flow Volume = Multiplier * Volume$$$$Line = Previous A/D \  Line + MoneyFlowVolume$$
  3. Interpretations: 
     When both price and Accumulation/Distribution are making higher peaks and higher troughs, the uptrend is likely to continue.
     When both price and Accumulation/Distribution are making lower peaks and lower troughs, the downtrend is likely to continue

### Volatility Indicators
- Bollinger Bands:
    1. Descriptions:
       A type of price envelope plotted at a standard deviation level above an dbelow a simple moving Average
	2. It can indicate the volatility that help predicts likelihood of a sharp price move in either direction
- Average True Range

### Support and resistance indicators



























  

