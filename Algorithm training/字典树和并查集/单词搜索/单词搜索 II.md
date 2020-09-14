#### [单词搜索 II](https://leetcode-cn.com/problems/word-search-ii/)

> 
> 给定一个二维网格 **board** 和一个字典中的单词列表 **words**，找出所有同时在二维网格和字典中出现的单词。
>
> 单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母在一个单词中不允许被重复使用。
>
> **示例:**
>
> ```
> 输入: 
> words = ["oath","pea","eat","rain"] and board =
> [
>   ['o','a','a','n'],
>   ['e','t','a','e'],
>   ['i','h','k','r'],
>   ['i','f','l','v']
> ]
> 
> 输出: ["eat","oath"]
> ```



```python
class Solution:     
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:

        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
        self.res = set()
        self.root = {}
        self.end_of_word = "#"

        # 创建Trie
        for word in words:
            node = self.root
            for char in word:
                node = node.setdefault(char, {})
            node[self.end_of_word] = self.end_of_word
            
        m, n = len(board), len(board[0])
        def dfs(board, i, j, cur_word, cur_dict):
            cur_word += board[i][j]
            cur_dict = cur_dict[board[i][j]]
            if self.end_of_word in cur_dict:
                self.res.add(cur_word)
            tmp, board[i][j] = board[i][j], "@"
            for k in range(4):
                x, y = i + dx[k], j + dy[k]
                if 0 <= x < m and 0 <= y < n and board[x][y] != "@" and board[x][y] in cur_dict:
                    dfs(board, x, y, cur_word, cur_dict)
            board[i][j] = tmp
            
        for i in range(m):
            for j in range(n):
                if board[i][j] in self.root:
                    dfs(board, i, j, "", self.root)
        return list(self.res)
```

