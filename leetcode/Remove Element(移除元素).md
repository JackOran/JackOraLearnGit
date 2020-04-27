### Remove Element(移除元素)

***题目：Given an array nums and a value val, remove all instances of that value [in-place](https://en.wikipedia.org/wiki/In-place_algorithm) and return the new length.***

> ```markdown
> Given nums = [3,2,2,3], val = 3,
> 
> Your function should return length = 2, with the first two elements of nums being 2.
> 
> It doesn't matter what you leave beyond the returned length.
> ```

```java
class Solution {
    public int removeElement(int[] nums, int val) {
        int index=0;  
        for(int i=0;i<nums.length;i++){
            if(nums[i]==val){  //如果等于val跳过
                continue;
            }else{
              nums[index] = nums[i]; //存储非val元素
                index++;
            }
        }
        return index;
    }
}
```

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        index = 0
        for i in range(len(nums)):
            if(nums[i]==val):
                continue
            else:
                nums[index] = nums[i]
                index += 1
        return index
```

