```
## 基本语法
```
1. 换行
   \\
   利用&可以对齐每行
## Mathtype
1. 句中公式 inline math mode
   \(x^2 + y^2 = z^2\)或
   $x^2 + y^2 = z^2$ (最常用，直接将所写部分用$框选)
2. display math mode(另一起行，居中展示)
   \[x^2 + y^2 = z^2\]或
3. 调用amsmath宏包时可有其他表达
   - \[\sqrt{x^2+1}\]
   - \(\sqrt{x^2+1}\)
   - \begin{math}
     \sqrt{x^2+1}
     \end{math}
4. 上下标
   上标: ^
   下标: __
5. 常见数学表达
   - 积分
     $\int_0^1 x^2 + y^2 \ dx $
   - 求和sigma
     \sum_{i=1}^{\infty} \frac{1}{n^s}
   - 连乘
     \prod_p \frac{1}{1 - p^{-s}} 
   - 分数表达
     \frac {分子} {分母}
     可以用\text{}来输入文本信息
     连分数用/cfrac
   - 二项式系数
     \binom{n}{k}
   - 矩阵表达
     ![[matrix.png]]
     利用$记号实现行中插入matrix
1. 括号的使用
![[latex_parentheses.png]]
   括号标注时注意\left  \right
