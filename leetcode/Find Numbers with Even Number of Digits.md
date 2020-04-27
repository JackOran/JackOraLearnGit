### Find Numbers with Even Number of Digits（找到包含偶数位的数字）

Given an array `nums` of integers, return how many of them contain an **even number** of digits.

> ```markdown
> Input: nums = [12,345,2,6,7896]
> Output: 2
> Explanation: 
> 12 contains 2 digits (even number of digits). 
> 345 contains 3 digits (odd number of digits). 
> 2 contains 1 digit (odd number of digits). 
> 6 contains 1 digit (odd number of digits). 
> 7896 contains 4 digits (even number of digits). 
> Therefore only 12 and 7896 contain an even number of digits.
> ```

```java
class Solution {
    public int findNumbers(int[] nums) {
        int N = nums.length;
        int count = 0;
        for(int i=0;i<N;i++){
            if(String.valueOf(nums[i]).length() % 2 == 0){
                count++;
            }  
        }
        return count;
    }
}
```

```python
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for i in range(len(nums)):
            if len(str(nums[i]))%2==0:
                count += 1
        return count
```

