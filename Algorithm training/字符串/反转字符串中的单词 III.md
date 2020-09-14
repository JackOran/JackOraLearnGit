#### [反转字符串中的单词 III](https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/)

> 给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。
>
> 示例 1:
>
> 输入: "Let's take LeetCode contest"
> 输出: "s'teL ekat edoCteeL tsetnoc" 
>



```python
class Solution:
    def reverseWords(self, s: str) -> str:
        if not s:
            return ""
        s = s.strip().split()
        res = []
        # print(s)
        for words in s:
            res.append(words[::-1])
        return ' '.join(res)
```

```python
2、利用两次切片，不需遍历
先反转单词列表 再反转字符串

以字符串 “I love drag queen” 为例：

s.split(" ") 将字符串分割成单词列表:


['I', 'love', 'drag', 'queen']
s.split(" ")[::-1] 将单词列表反转:


['queen', 'drag', 'love', 'I']
" ".join(s.split(" ")[::-1]) 将单词列表转换为字符串，以空格分隔:


"queen drag love I"
" ".join(s.split(" ")[::-1])[::-1] 将字符串反转：

”I evol gard neeuq“
```




```python
class Solution:
    def reverseWords(self, s: str) -> str:
        
        if not s:
            return ""
        return ' '.join(s.split()[::-1])[::-1]
```

