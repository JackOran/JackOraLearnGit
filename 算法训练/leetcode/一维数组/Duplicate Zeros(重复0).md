### Duplicate Zeros(重复0)

***题目：给定一个固定长度的整数数组“arr”，重复出现的每个0，将其余的元素向右移动。***

> ```markdown
> Input: [1,0,2,3,0,4,5,0]
> Output: null
> 说明:调用函数后，将输入数组修改为:[1,0,0,2,3,0,0,4]
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

