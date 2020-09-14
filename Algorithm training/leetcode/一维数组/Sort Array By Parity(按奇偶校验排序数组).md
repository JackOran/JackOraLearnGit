### 按奇偶校验排序数组

***题目:给定一个`A`非负整数数组，返回一个数组，该数组包含的所有偶数元素`A`，后跟的所有奇数元素`A`***

> ```
> 输入：[3,1,2,4] 
> 输出：[2,4,3,1]
> 输出[4,2,3,1]，[2,4,1,3]和[4,2,1,3]也将被接受。
> ```

```java
class Solution {
    public int[] sortArrayByParity(int[] A) {
        int N = A.length;
        int[] a = new int[N];
        int m = 0;
        for(int i=0;i<N;i++){
            if(A[i]%2==0){
                a[m] = A[i];
                m++;
            }
        }
        while(m<N){
            for(int j=0;j<N;j++){
                if(A[j]%2 != 0){
                    a[m] = A[j];
                    m++;
                }
            }
        }
        return a;
    }
}
```

```python
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        res = []
        for i in range(len(A)):
            if A[i]%2 == 0:
                res.append(A[i])
        for j in range(len(A)):
            if A[j]%2 != 0:
                res.append(A[j])
        return res
        
```

