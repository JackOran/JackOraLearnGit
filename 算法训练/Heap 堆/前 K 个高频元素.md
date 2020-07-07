#### [前 K 个高频元素](https://leetcode-cn.com/problems/top-k-frequent-elements/)

> 给定一个非空的整数数组，返回其中出现频率前 k 高的元素。
>
>  
>
> 示例 1:
>
> 输入: nums = [1,1,1,2,2,3], k = 2
> 输出: [1,2]
> 示例 2:
>
> 输入: nums = [1], k = 1
> 输出: [1]

```python
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        res = collections.Counter(nums)
        return [i[0] for i in res.most_common(k)]
```

##### 使用堆

```java
class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        //通过hash表来计算nums个数
        Map<Integer, Integer> hashmap = new HashMap<>();
        for (int num : nums){
            hashmap.put(num, hashmap.getOrDefault(num,0) + 1);
        }
        // 构造一个大顶堆
        PriorityQueue<Integer> max_pq = new PriorityQueue<>(new Comparator<Integer>() {
            @Override
            public int compare(Integer a, Integer b) {
                return hashmap.get(b) - hashmap.get(a);
            }
        });
        for (Integer key : hashmap.keySet()){
            max_pq.add(key);
        }
        //取出大顶堆的元素
        int[] res = new int[k];
        for (int i = 0; i < k; i++){
            res[i] = max_pq.poll();
        }
        return res;
    }
}
```

