#### [搜索旋转排序数组 II](https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii/)

> 假设按照升序排序的数组在预先未知的某个点上进行了旋转。
>
> ( 例如，数组 [0,0,1,2,2,5,6] 可能变为 [2,5,6,0,0,1,2] )。
>
> 编写一个函数来判断给定的目标值是否存在于数组中。若存在返回 true，否则返回 false。
>
> 示例 1:
>
> 输入: nums = [2,5,6,0,0,1,2], target = 0
> 输出: true
> 示例 2:
>
> 输入: nums = [2,5,6,0,0,1,2], target = 3
> 输出: false
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array-ii
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

**第一类**
1011110111 和 1110111101 这种。此种情况下 **nums[left] == nums[mid]**，分不清到底是前面有序还是后面有序，此时 **left++** 即可。相当于去掉一个重复的干扰项。

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return True
            if nums[left] <= nums[mid]:
                # 特殊情况
                if nums[left] == nums[mid]:
                    left += 1
                    continue
                if nums[left] <= target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
        return False
               
```

