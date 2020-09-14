### Merge Sorted Array（数组合并排序）

***给定两个已排序的整数数组nums1和nums2，将nums2合并为一个已排序的数组nums1。***

> ```markdown
> Input:
> nums1 = [1,2,3,0,0,0], m = 3
> nums2 = [2,5,6],       n = 3
> 
> Output: [1,2,2,3,5,6]
> ```

```java
import java.util.Arrays;
class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
       for(int i=0;i<n;i++){
           nums1[m+i] = nums2[i];
       }
        Arrays.sort(nums1);
    }
}
```

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        if m <= n:
            if(len(nums1))<3:
                for i in nums1[:]:
                    if i == 0:
                        nums1.remove(i)
                for i in range(n):
                    nums1.append(nums2[i])
                b = nums1.sort()
                return b
            else:
                N = len(nums1) - m
                if N == len(nums1):
                    for i in nums1[:]:
                        if i == 0:
                            nums1.remove(i)
                    for i in range(n):
                        nums1.append(nums2[i])
                    b = nums1.sort()
                    return b
                else:
                    for i in nums1[m:]:
                        if i == 0:
                            nums1.remove(i)
                    # print(nums1)
                    for j in range(n):
                        nums1.append(nums2[j])
                    a = nums1.sort()
                    return a
        else:
            for i in nums1[m:]:
                if i == 0:
                    nums1.remove(i)
                    # print(nums1)
            for j in range(n):
                nums1.append(nums2[j])
            a = nums1.sort()
            return a

```

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        for i in range(n):
            nums1[m+i] = nums2[i]
        nums1.sort()

        
```

