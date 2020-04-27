### Duplicate Zeros(重复0)

***题目：Given a fixed length array `arr` of integers, duplicate each occurrence of zero, shifting the remaining elements to the right.***

> ```markdown
> Input: [1,0,2,3,0,4,5,0]
> Output: null
> Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
> ```

```java
class Solution {
    public void duplicateZeros(int[] arr) {
        int N = arr.length;
        for(int i=0;i<N;i++){
            if(arr[i]==0){
                for(int j=N-1;j>i;j--){
                    arr[j] = arr[j-1];
                }
                i++;
                //System.out.print(i + " ");
            }
        }
        // for(int i=0;i<N;i++){
        //     System.out.print(arr[i] + " ");
        // }
    }
}
```

```python
class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        i = 0
        n = len(arr)
        if 0<=n<=10000:
            while(i<n):
                if arr[i] == 0:
                    arr.insert(i,0)
                    # print(arr)
                    arr.pop(-1)
                    # print(arr)
                    i += 1
                i += 1
        
            
                
```

