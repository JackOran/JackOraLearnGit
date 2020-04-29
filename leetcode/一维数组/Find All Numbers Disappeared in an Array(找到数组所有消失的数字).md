### 找到数组所有消失的数字

***给定一个整数数组，其中1≤a[i]≤n (n =数组大小)，有些元素出现两次，有些元素出现一次。***

***找到[1,n]中不出现在这个数组中的所有元素。***

***你能在没有额外空间的情况下，在O(n)运行时完成它吗?您可以假定返回的列表不算作额外的空间。***

> ```
> Input:
> [4,3,2,7,8,2,3,1]
> 
> Output:
> [5,6]
> ```

```java
import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;
class Solution {
    public List<Integer> findDisappearedNumbers(int[] nums) {
        List<Integer> list = new ArrayList<Integer>();
        for(int i=0;i<nums.length;i++){
            list.add(i+1); //list= {1,2,3,4,5,6,7,8};
        }
        for(int j=0;j<nums.length;j++){
            list.set(nums[j]-1,0); //将nums中的元素在list中变为0
        }
        // System.out.print(list);
        for(int k=0;k<list.size();k++){
            if(list.get(k)==0){ //将0删除
                list.remove(k);
                k--;
            }
        }
        return list;
    }
}
```

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        for i in range(1,len(nums)+1):
            res.append(i)
        a = set(nums)
        b = set(res)
        return list(b-a)
```

