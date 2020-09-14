### Third Maximum Number（第三大数字）

***题目：给定一个非空整数数组，返回该数组中的第三个最大数字。如果不存在，则返回最大数目。时间复杂度必须在O(n)中。***

> ```
> Input: [3, 2, 1]
> 
> Output: 1
> 
> 说明:第三个最大值是1。
> Input: [1, 2]
> 
> Output: 2
> 
> 说明:第三个最大值不存在，因此返回最大值(2)。
> ```

```java
import java.util.Arrays;
class Solution {
    public int thirdMax(int[] nums) {
        Arrays.sort(nums);
        int index = 0;
        for(int i=1;i<nums.length;i++){
            if(nums[index] != nums[i]){
                index++;
                nums[index] = nums[i];
            }
        }
        int[] arr = new int[index+1];
        int m = 0;
        while(m<index+1){
            for(int j=0;j<index+1;j++){
                arr[m] = nums[j];
                m++;
            }
        }
        int maxNum = arr[0];
        for(int k=0;k<arr.length;k++){
            if(arr[k] > maxNum){
                maxNum = arr[k];
            }
        }
        // Arrays.sort(arr);
        // System.out.println(Arrays.toString(arr));
        // System.out.print(index+1);
        if(arr.length<3){
            return maxNum;
        }else{
            Arrays.sort(arr);
            return arr[arr.length-3];
        }
    }
}
```

```python
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        if(len(nums)<3):
            return max(nums)
        return nums[-3]
```

