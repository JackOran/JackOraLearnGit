#### [杨辉三角 II](https://leetcode-cn.com/problems/pascals-triangle-ii/)

> ![img](https://upload.wikimedia.org/wikipedia/commons/0/0d/PascalTriangleAnimated2.gif)
>
> **示例:**
>
> ```
> 输入: 3
> 输出: [1,3,3,1]
> ```



```python
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        
        dp = [[0] * n for n in range(1, rowIndex + 2)]
        for i in range(rowIndex+1):
            dp[i][0] = dp[i][-1] = 1
        for i in range(len(dp)):
            for j in range(i+1):
                if dp[i][j] == 0:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
        return dp[-1]
```

