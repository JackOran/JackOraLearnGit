### Squares of a Sorted Array（排序数组的平方）

***Given an array of integers `A` sorted in non-decreasing order, return an array of the squares of each number, also in sorted non-decreasing order.***

> ```markdown
> Input: [-4,-1,0,3,10]
> Output: [0,1,9,16,100]
> ```

```java
import java.util.Arrays;
class Solution {
    public int[] sortedSquares(int[] A) {
        int N = A.length;
        for(int i=0; i<N; i++){
            A[i] = A[i] * A[i];
        }
        Arrays.sort(A);
        return A;
    }
}
```

```python
class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        a = map(lambda x:x**2,A)
        return sorted(a)
        
```



