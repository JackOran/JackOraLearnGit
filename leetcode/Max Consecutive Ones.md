### Max Consecutive Ones（最大连续1个数）

***题目：Given a binary array, find the maximum number of consecutive 1s in this array.***

> ```markdown
> Input: [1,1,0,1,1,1]
> Output: 3
> Explanation: The first two digits or the last three digits are consecutive 1s.
>     The maximum number of consecutive 1s is 3.
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
                if ma > count:
                    ma = ma
                else:
                    ma = count
            else:
                count = 0
        return ma
```

