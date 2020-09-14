#### [单词接龙 II](https://leetcode-cn.com/problems/word-ladder-ii/)

> 给定两个单词（beginWord 和 endWord）和一个字典 wordList，找出所有从 beginWord 到 endWord 的最短转换序列。转换需遵循如下规则：
>
> 每次转换只能改变一个字母。
> 转换后得到的单词必须是字典中的单词。
> 说明:
>
> 如果不存在这样的转换序列，返回一个空列表。
> 所有单词具有相同的长度。
> 所有单词只由小写字母组成。
> 字典中不存在重复的单词。
> 你可以假设 beginWord 和 endWord 是非空的，且二者不相同。
> 示例 1:
>
> 输入:
> beginWord = "hit",
> endWord = "cog",
> wordList = ["hot","dot","dog","lot","log","cog"]
>
> 输出:
> [
>   ["hit","hot","dot","dog","cog"],
>   ["hit","hot","lot","log","cog"]
> ]
> 示例 2:
>
> 输入:
> beginWord = "hit"
> endWord = "cog"
> wordList = ["hot","dot","dog","lot","log"]
>
> 输出: []
>
> 解释: endWord "cog" 不在字典中，所以不存在符合要求的转换序列。

```python
class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        # 使用通配符构造邻接表（每个单词的任意子串作为两个节点之间的边）
        hash=collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                hash[word[:i]+"*"+word[i+1:]].append(word)

        # 生成需要访问的路径队列
        queue = [[beginWord, [beginWord]]]
        # 生成已访问节点
        visited = set()
        visited.add(beginWord)
        # 保存结果
        res = []

        while queue:
            # new_visited = set()
            # 依次输出队列中所有路径
            for _ in range(len(queue)):
                word, path = queue.pop(0)
                # 如果当前节点是endWord，保存路径
                if word == endWord:
                    res.append(path)

                # 访问该节点所有边
                for i in range(len(word)):
                    masked_word = word[:i]+"*"+word[i+1:]
                    # 访问该节点通过这条边能够访问的所有节点
                    for j in hash[masked_word]:
                        # 因为是求最短路径，所以如果节点已经访问过则不再访问
                        if j not in visited:
                            
                            queue.append([j, path + [j]])
                            visited.add(j)
            # 更新已经访问过的节点
          	visited |= new_visited

        return res
```

