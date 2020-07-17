#### [最小的k个数](https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/)

输入整数数组 `arr` ，找出其中最小的 `k` 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        
        arr.sort()
        res = []
        for n in arr[:k]:
            res.append(n)
        return res
      
# 时间复杂度是o(NlogN)
```

##### 使用堆 PriorityQueue

```java
class Solution {
    public int[] getLeastNumbers(int[] arr, int k) {
      	//默认小顶堆
        PriorityQueue<Integer> heap = new PriorityQueue<>();
        for (int i = 0; i < arr.length; i++){
            heap.add(arr[i]);
        }
        int[] res = new int[k];
        for (int j = 0; j < k; j++){
            res[j] = heap.poll(); 
        }
        return res;
    }
}
```

```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        import heapq
        heapq.heapify(arr)
        return heapq.nsmallest(k, arr)
```

