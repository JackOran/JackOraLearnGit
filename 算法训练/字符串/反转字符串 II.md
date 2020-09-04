#### [反转字符串 II](https://leetcode-cn.com/problems/reverse-string-ii/)

> 
> 给定一个字符串 `s` 和一个整数 `k`，你需要对从字符串开头算起的每隔 `2k` 个字符的前 `k` 个字符进行反转。
>
> - 如果剩余字符少于 `k` 个，则将剩余字符全部反转。
> - 如果剩余字符小于 `2k` 但大于或等于 `k` 个，则反转前 `k` 个字符，其余字符保持原样。
>
>  
>
> **示例:**
>
> ```
> 输入: s = "abcdefg", k = 2
> 输出: "bacdfeg"
> ```

#### 

```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s = list(s)
        print(s)
        # 每2k个元素反转前k个元素
        for i in range(0, len(s), 2*k):
            s[i:i+k] = reversed(s[i:i+k])
        return ''.join(s)
```



```python
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        # 奇数个反转 偶数不反转
        res, flag = '', True
        for i in range(0, len(s), k):
            res += s[i:i+k][::-1] if flag else s[i:i+k]
            flag = not flag
        return res
```

