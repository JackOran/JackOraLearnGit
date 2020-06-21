### [第 N 个泰波那契数](https://leetcode-cn.com/problems/n-th-tribonacci-number/description/)

> 泰波那契序列 Tn 定义如下： 
>
> T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
>
> 给你整数 `n`，请返回第 n 个泰波那契数 Tn 的值。

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        first = 0
        second = 1
        thired = 1
        for i in range(3,n+1):
            s = first + second + thired
            first = second
            second = thired
            thired = s
        return thired
```

