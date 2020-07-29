#### [Pow(x, n)](https://leetcode-cn.com/problems/powx-n/)

> 实现 pow(x, n) ，即计算 x 的 n 次幂函数。
>
> 示例 1:
>
> 输入: 2.00000, 10
> 输出: 1024.00000
> 示例 2:
>
> 输入: 2.10000, 3
> 输出: 9.26100
> 示例 3:
>
> 输入: 2.00000, -2
> 输出: 0.25000
> 解释: 2-2 = 1/22 = 1/4 = 0.25

##### 分治算法

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:

        if n < 0:
            return 1/self.myPow(x, -n)
        if n == 0:
            return 1
        if n == 1:
            return x
        subproblem = self.myPow(x, n//2)
        if n % 2 == 0:
            result = subproblem * subproblem
        else:
            result = subproblem * subproblem * x
        return result
```

##### 暴力解法

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        return x ** n
```

