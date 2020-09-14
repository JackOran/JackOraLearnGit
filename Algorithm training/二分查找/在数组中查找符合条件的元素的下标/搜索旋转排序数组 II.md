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
当数组为 `[1,2,1,1,1]`,`nums[mid] == nums[left] == nums[right]`，需要 `left++, right --`  缩小区间来查找;

当 `nums[left]<= nums[mid]`，说明是在左半边的递增区域

a. `nums[left] <=target < nums[mid]`，说明 `target` 在 `left` 和 `mid` 之间。我们令`right = mid - 1`;

b. 不在之间，我们令 `left = mid + 1`;

当 `nums[mid] < nums[right]`，说明是在右半边的递增区域

a. `nums[mid] < target <= nums[right]`，说明 `target` 在 `mid` 和 `right` 之间，我们令`left = mid + 1`

b. 不在之间，我们令 `right = mid - 1`;

```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            if nums[left] == nums[mid] == nums[right]:
                left += 1
                right -= 1
            elif nums[mid] >= nums[left]:
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
#时间复杂度为o(logN)
```

