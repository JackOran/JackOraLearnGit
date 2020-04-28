### Remove Element(移除元素)

***题目：给定一个数组号和一个val值，删除该值的所有实例[in-place](https://en.wikipedia.org/wiki/In-place_algorithm)并返回新的长度。***

> ```markdown
> Given nums = [3,2,2,3], val = 3,
> 
> 您的函数应该返回length = 2, nums的前两个元素为2。
> 
> 不管你留下什么超过返回的长度。
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

