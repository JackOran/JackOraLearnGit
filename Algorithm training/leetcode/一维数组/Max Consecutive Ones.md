### Max Consecutive Ones（最大连续1个数）

***题目：给定一个二进制数组，找出该数组中连续的1的最大数目。***

> ```markdown
> Input: [1,1,0,1,1,1]
> Output: 3
> 说明:前两位或后三位是连续的1。
>    连续的1的最大数目是3。
> ```

```java
class Solution {
    public int findMaxConsecutiveOnes(int[] nums) {
        int max = 0;
        int count = 0;
        int N = nums.length;
        for(int i=0; i<N; i++){
            if(nums[i]!=0){
                count++;
                max = max>count?max:count;
            }else{
                count = 0;
            }
        }
        return max;
    }
}
```

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ma = 0
        count = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                count += 1
                ma = max(ma,count)
            else:
                count = 0
        return ma
```

