---
---

### World Quant平台学习
#### Alpha
1. 概念：
   Alpha即为一个用来预测当下金融市场的数学表达式，可以与之前所学的technical analysis相结合，构造相应的公式从市场交易中获利。
2. Websim相关术语:
   Universe: 当下alpha基于的数据集与回测集
   Pnl: daily_pnl = sum of (position * daily_return)
   Information Ratio: 强调当下模型的预测能力  $IR = \frac{mean(Daliy_{pnl})}{std(Daily_{pnl})}$ $Sharpe = \sqrt{252}*IR$ 
   Turnover: 换手率，体现交易的频次
   Drawdown: 刻画最大可能损失，体现了当前alpha的相对稳定程度与风险控制能力
#### Websim
1. 原理：
   利用fast expression的类编程语言迅速实现简单alpha的构造
2. 设置：
   可通过设置中的选项确定模拟与回测的具体要求，包括:
   Region and Universe, Delay, Decay, Neutralization, Max stock fraction, Unit check, Simulation timeframe
3. 迅速上手：
   1. Data:
      World quant brain向我们提供了平台可以选取的data,我们可以直接通过数据描述或者直接搜索名字确定我们需要的数据。
      <[WorldQuant BRAIN Data](https://platform.worldquantbrain.com/data?delay=1&instrumentType=EQUITY&region=USA&universe=TOP3000)>
   2. Operation:
     World quant brain想我们提供了一些简单的内置函数方便我们构造alpha
     <[Detailed Operator Descriptions](https://platform.worldquantbrain.com/learn/data-and-operators/detailed-operator-descriptions)>
 4. 测试结果数据分析

### 个人心得
#### 挖掘因子
1. 一个非常简单直接有效的方法是直接选取Example的模拟，然后在他给的hint基础上进行优化，这样我们可以得到一些因子的雏形，如果运气好甚至可以直接得到可以交的因子
2. 同时也可以善用互联网资源，world quant brain和知乎上都有一些因子挖掘的心得，我们可以借鉴他们逐步挖掘的想法，或者选取相似的技术指标对相关价值尺度进行复现
3. 还有一种行之有效的方法为借鉴我们之前所学的Techniacal analysis的一些因子，基于相对成熟的金融知识进行设计
4. 还可以通过alpha101中的相应公式进行适度挖掘组合
#### 优化（古法炼丹）
由于金融知识的相对不扎实，所以我调试的过程更像“炼丹”，但还是有一些经验的
1. 加权组合：
   在有了几个因子的雏形后，我们可以对相应的设计到同一领域的因子进行组合，还可以优化 他们的权重比例来调节一些参数
   比如当我在优化一个判断市场情绪的因子时，我发现直接采取一个情绪指标换手率太高，所以我再加上了一个rank(volume),一方面反映了交易量，另一方面也平衡了纯粹由情绪驱动的过高的换手率
2. 相似因子相互平衡挖掘：
   通过从Example中选取相似或者课对冲的因子进行优化，同时也可通过细致调试settings中的参数改善
总结：World quant Brain对于学过金融知识且熟悉fast expressions表达式的同学来说还是较为容易的，但对于金融知识相对匮乏的同学整个调试过程更偏向于黑盒，需要逐步积累经验

### 成果展示
我最近一共实现发掘了5个alpha因子，其中两个good,3个average,分别从不同的角度去考虑实现了对市场参数的一些指标的预测
Brain Medal
![](Attachment/26da868c93bde49d7203044acbd2365.png)
1.Market Emotion
>`0.3*snt_buzz + 2*rank(volume)
   
   ![](Attachment/0a993377e5837a280a2f875dedbc6b9.png)

2.Evaluate Liability
>`-ts_rank(fn_liab_fair_val_l1_a,160)`

![](Attachment/07c48406719a03e6233c24e301bfa97.png)
3.Evaluate the earnings by considering currency gain and retained earnings
>`rank(ts_delta(retained_earnings / sharesout, 65)) + rank(assets) + Sum(fn_oth_income_loss_fx_transaction_and_tax_translation_adj_a,255)`


![](Attachment/fc832ecb081ed6db7437d8c636248a8.png)
4.Liability
>`0.8*rank(liabilities / assets)+0.2*rank(cash_st / debt_st)`

![](Attachment/15070a3adfea8b2d0b1a30ca8024df8.png)

5.Short_selling
>`-rank(ts_sum((close-low)/(high-close),3)*rank(ts_delta(close,3)))`

![](Attachment/4764af06fc70e818f7164eecb0b8eac.png)

Current Rank:还在持续挖掘中，奖牌邮件还未收到，等待后续补充
![](Attachment/a84d6c02a153d64db559a596d9e93f2.png)