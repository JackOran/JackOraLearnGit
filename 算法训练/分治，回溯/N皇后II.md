#### [N皇后 II](https://leetcode-cn.com/problems/n-queens-ii/)

> ![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/8-queens.png)
>
> 给定一个整数 n，返回 n 皇后不同的解决方案的数量。
>
> 示例:
>
> 输入: 4
> 输出: 2
> 解释: 4 皇后问题存在如下两个不同的解法。
> [
>  [".Q..",  // 解法 1
>   "...Q",
>   "Q...",
>   "..Q."],
>
>  ["..Q.",  // 解法 2
>   "Q...",
>   "...Q",
>   ".Q.."]
> ]
>



```python
class Solution:
    def totalNQueens(self, n: int) -> int:
        def dfs(i, queens, pie, na):
          	# 行i到达n个皇后，直接返回
            if i == n:
                return 1
            total = 0
            # 遍历列
            for j in range(n):
                if j not in queens and i+j not in pie and i-j not in na:
                    total += dfs(i + 1, queens + [j], pie + [i+j], na + [i -j])
            return total
        return dfs(0, [], [], [])
      
```

