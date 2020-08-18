#### [ N皇后](https://leetcode-cn.com/problems/n-queens/)

> n 皇后问题研究的是如何将 n 个皇后放置在 n×n 的棋盘上，并且使皇后彼此之间不能相互攻击。
>
> ![img](https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/10/12/8-queens.png)
>
> 上图为 8 皇后问题的一种解法。
>
> 给定一个整数 n，返回所有不同的 n 皇后问题的解决方案。
>
> 每一种解法包含一个明确的 n 皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        board=[['.']*n for _ in range(n)] # 初始化二维棋盘
        # print(board)
        res=[]
        
        def isValid(board,row,col):
            n=len(board)
            # 检查列是否有皇后互相冲突
            for i in range(n):
                if board[i][col]=='Q':
                    return False
            # 检查右上方是否有皇后互相冲突
            r_row,r_col=row,col
            while r_row>0 and r_col<n-1:
                r_row-=1
                r_col+=1
                if board[r_row][r_col]=='Q':
                    return False
            # 检查左上方是否有皇后互相冲突
            l_row,l_col=row,col
            while l_row>0 and l_col>0:
                l_row-=1
                l_col-=1
                if board[l_row][l_col]=='Q':
                    return False
            return True
        
        def backtrack(board,row):
        #     if 满足条件:
        #         res.append(路径)
        #         return
            if row==len(board):
                tmp_list=[] #二维变一维添加到res中
                for e_row in board:
                    tmp=''.join(e_row)
                    tmp_list.append(tmp)
                res.append(tmp_list)
                return
            
        #     for 选择 in 选择列表:
        #         做选择
        #         backtrack(路径,选择列表)
        #         撤销选择
            for col in range(len(board[0])):
                if not isValid(board,row,col):
                    # print(isValid(board,row,col))
                    continue
                board[row][col]='Q'
                # print(board)
                backtrack(board,row+1)
                board[row][col]='.'
        backtrack(board, 0)
        return res
```

```python
def solveNQueens(self, n):
    def DFS(queens, xy_dif, xy_sum):
        p = len(queens)
        if p==n:
            result.append(queens)
            return None
        for q in range(n):
            if q not in queens and p-q not in xy_dif and p+q not in xy_sum: 
                DFS(queens+[q], xy_dif+[p-q], xy_sum+[p+q])
    result = []
    DFS([],[],[])
    return [ ["."*i + "Q" + "."*(n-i-1) for i in sol] for sol in result]
```

```python
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        res = []
        
        def dfs(i, queens, pie, na):
         		# 行到达n
            if  i == n:
                res.append(queens)
                return
            # 遍历列
            for j in range(n):
                if j not in queens and i-j not in pie and i+j not in na:
                    dfs(i + 1, queens+[j], pie + [i-j], na + [i+j])
        dfs(0, [], [], [])
        return [['.' * i + 'Q' + '.' * (n - i - 1) for i in sol] for sol in res]
```

