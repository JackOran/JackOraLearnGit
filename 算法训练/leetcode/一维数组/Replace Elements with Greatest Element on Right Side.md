### Replace Elements with Greatest Element on Right Side（替换右边最大的元素）

***题目：给定一个数组“arr”，将该数组中的每个元素替换为其右边元素中最大的元素，并将最后一个元素替换为“-1”。***

> ```
> Input: arr = [17,18,5,4,6,1]
> Output: [18,6,6,6,1,-1]
> ```

```java
class Solution {
    public int[] replaceElements(int[] arr) {
        int m = 0;
        int maxNum =arr[0];
        while(m<arr.length){
            for(int i=m+1;i<arr.length;i++){
                if(arr[i] > maxNum){
                    maxNum = arr[i]; 
            }
        }
            arr[m] = maxNum;//遍历找出最大的值赋值
            maxNum = -1;
            m += 1;
    }
        if(arr.length==1){
            arr[0] = -1;
        }
        return arr;
  }
}
```

```python
class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = []  #新建一个列表，将最大的值加入
        m = 1
        for i in range(m,len(arr)):
            res.append(max(arr[m:]))
            m += 1
        res.append(-1)
        return res

        
```

