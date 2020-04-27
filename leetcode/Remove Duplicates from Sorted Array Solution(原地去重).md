### Remove Duplicates from Sorted Array（去重）

***题目：Given a sorted array nums, remove the duplicates [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) such that each element appear only once and return the new length.***

> ```markdown
> Given nums = [1,1,2],
> 
> Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
> 
> It doesn't matter what you leave beyond the returned length.
> ```

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        int index = 0;      //拿数组第一个值与后面的元素进行比较
        for(int i=1;i<nums.length;i++){
            if(nums[index] != nums[i]){
                index++;
                nums[index] = nums[i];
            }
        }
        return index+1;
    }
}
```

```python
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        for i in range(1,len(nums)):
            if nums[index] != nums[i]:
                index += 1
                nums[index] = nums[i]
        return index+1
        
```

