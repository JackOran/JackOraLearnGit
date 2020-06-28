### Remove Duplicates from Sorted Array（去重）

***题目：给定一个排序的数组号，删除重复的[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)，这样每个元素只出现一次，并返回新的长度。***

> ```markdown
> Given nums = [1,1,2],
> 
> 您的函数应该返回length = 2, nums的前两个元素分别为1和2。
> 
> 不管你留下什么超过返回的长度。
> ```

```java
class Solution {
    public int removeDuplicates(int[] nums) {
        int index = 0;      //拿数组第一个值与后面的元素进行比较
        for(int i=1; i<nums.length; i++){
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

