### Move Zeroes(移动零)

***给定一个数组`nums`，编写一个函数，将所有`0`' 移到它的末尾，同时保持非零元素的相对顺序。***

> ```
> 输入： [0,1,0,3,12]
> 输出： [1,3,12,0,0]
> 
> 注意事项：
> 
> 您必须就地执行此操作，而不需要复制阵列。
> 减少操作总数。
> ```

```java
class Solution {
    public void moveZeroes(int[] nums) {
        int k = 0;
        for(int i=0;i<nums.length;i++){
            if(nums[i] !=0){
                nums[k] = nums[i]; //将不为0的赋值给k
                k++;
            }
        }
        while(k<nums.length){
            nums[k] = 0;
            k++;
        }
    }
}
```

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count = 0
        for i in nums[:]:
            if i==0:
                nums.remove(i)
                count+=1
        for j in range(count):
            nums.append(0)
        return nums
```

