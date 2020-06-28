### Valid Mountain Array（有效山阵）

***题目：给定一个整数数组“A”，当且仅当它是一个有效的山地数组时，返回“true”***

> ```markdown
> Input: [0,3,2,1]
> Output: true
> 
> Input: [2,1]
> Output: false
> ```

```java
class Solution {
    public boolean validMountainArray(int[] A) {
        int N = A.length;
        int m = 0;
        int n = 0;
        if(A.length<3){
            return false;
        }
        for(int i=0;i<A.length-1;i++){
            if(A[i]<A[i+1]){
                m++;     //m个递增
            }
            else{
                break;
            }
        }
        for(int j=m;j<A.length-1;j++){
            if(A[j]>A[j+1]){
                n++;    //n个递减的
            }
            else{
                break;
            }
        }
        if(m+n == A.length-1 && m!=0 && n!=0){
            return true;
        }
        else{
            return false;
        }
    }
}
```

```python
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        if(len(A)<3):
            return False
        maxNum = max(A)
        if A[-1] == maxNum:
            return False
        if A == sorted(A) or A == sorted(A,reverse=True):
            return False
        index = A.index(maxNum)
        nums1 = []
        nums2 = []
        
        for i in A[:index]:
            nums1.append(i)
        for j in A[index+1:]:
            nums2.append(j)
        a = sorted(nums1)
        b = sorted(nums2,reverse=True)
        if nums1 == a and nums2 == b:
            for i in range(1,len(nums1)):
                if nums1[i-1] >= nums1[i]:
                    return False
            for j in range(1,len(nums2)):
                if nums2[j-1] <= nums2[j]:
                    return False
            return True
        
```

