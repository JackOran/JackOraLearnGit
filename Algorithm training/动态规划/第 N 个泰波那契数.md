#### [第 N 个泰波那契数](https://leetcode-cn.com/problems/n-th-tribonacci-number/)

> 泰波那契序列 Tn 定义如下： 
>
> T0 = 0, T1 = 1, T2 = 1, 且在 n >= 0 的条件下 Tn+3 = Tn + Tn+1 + Tn+2
>
> 给你整数 n，请返回第 n 个泰波那契数 Tn 的值。

![第N个斐波拉契数](/Users/apple/Desktop/第N个斐波拉契数.png)

```java
class Solution {
    public int tribonacci(int n) {
        if(n < 2){
            return n;
        }
        if(n==2){
            return 1;
        }
        int first = 0;
        int second = 1;
        int thired = 1;
        for(int i=3; i<n+1; i++){
            int newElement = first + second + thired;
            first = second;
            second = thired;
            thired = newElement;
        }
        return thired;
    }
}
```

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        
        dp = {}
        dp[0] = 0
        dp[1] = 1
        dp[2] = 1
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
        return dp[n]
```

#### 带有记忆化搜索的dp

```python
class Solution:
    def tribonacci(self, n: int) -> int:
        
        if n <= 1:
            return n
        memo = {0:0, 1:1, 2:1}
        for i in range(3, n+1):
            if i in memo:
                return memo[i]
            else:
                memo[i] = memo[i-1] + memo[i-2] + memo[i-3]
        return memo[n]
```

