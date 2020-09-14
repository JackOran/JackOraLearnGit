#### [两个数组的交集 II](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/)

给定两个数组，编写一个函数来计算它们的交集。

示例 1:

输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
示例 2:

输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]

##### 先排序，然后遍历进行判断

```java
class Solution {
    public int[] intersect(int[] nums1, int[] nums2) {
        Arrays.sort(nums1);
        Arrays.sort(nums2);
        int i=0, j=0, k=0;
        while (i < nums1.length && j < nums2.length){
            if (nums1[i] < nums2[j]){
                i++;
            }else if (nums1[i] > nums2[j]){
                j++;
            }else {
                nums1[k++] = nums1[i++];
                j++;
            }
        }
        return Arrays.copyOf(nums1, k);
    }
}
```

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        res = []
        len1 = len(nums1)
        len2 = len(nums2)
        nums1.sort()
        nums2.sort()
        m, n = 0, 0
        while m < len1 and n < len2:
            if nums1[m] < nums2[n]:
                m += 1
            elif nums1[m] > nums2[n]:
                n +=1
            else:
                res.append(nums1[m])
                m += 1
                n += 1
        return res
```

