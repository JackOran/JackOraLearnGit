#### [子集 II](https://leetcode-cn.com/problems/subsets-ii/)

> 给定一个可能包含重复元素的整数数组 nums，返回该数组所有可能的子集（幂集）。
>
> 说明：解集不能包含重复的子集。
>
> 示例:
>
> 输入: [1,2,2]
> 输出:
> [
>   [2],
>   [1],
>   [1,2,2],
>   [2,2],
>   [1,2],
>   []
> ]
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/subsets-ii
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



```python
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        nums.sort()
        res = []
        def backtrack(index, track):
            res.append(track)
            for i in range(index, len(nums)):
                if i > index and nums[i] == nums[i-1]:
                    continue
                backtrack(i + 1, track + [nums[i]])
        backtrack(0, [])
        return res
```

