#### [全排列 II](https://leetcode-cn.com/problems/permutations-ii/)

> 给定一个可包含重复数字的序列，返回所有不重复的全排列。
>
> 示例:
>
> 输入: [1,1,2]
> 输出:
> [
>   [1,1,2],
>   [1,2,1],
>   [2,1,1]
> ]

**如果涉及考虑重复元素，或者大小比较的情况，对列表排序是一个不错的选择**

```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        def backtrack(nums, track):
            if nums == []:
                res.append(track[:])
                return
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue
                backtrack(nums[:i] + nums[i+1:], track + [nums[i]])
        backtrack(nums, [])
        return res
```



```python
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        nums.sort()
        visited = set()
        def backtrack(nums, track):
            if len(nums) == len(track):
                res.append(track[:])
                return
            for i in range(len(nums)):
                if i in visited or (i > 0 and i - 1 not in visited and nums[i] == nums[i-1]):
                    continue
                visited.add(i)
                backtrack(nums, track+[nums[i]])
                visited.remove(i)
        backtrack(nums, [])
        return res
```

