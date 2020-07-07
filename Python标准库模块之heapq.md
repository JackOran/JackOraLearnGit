## Python标准模块之heapq

### 创建堆

方式创建堆的两种方式：

- 一种是使用`空列表`，然后使用heapq.heappush()函数把值加入堆中。
- 另一种是使用`heap.heapify(list)`转换`列表`为堆结构。

```python
# 第一种创建堆方式（小顶堆,空列表）
import heapq
nums = [2, 3, 5, 1, 54, 23, 132]
heap = []
for num in nums:
    heapq.heappush(heap, num)
print(heap[0])
print(heap)
print(type(heap))

#  第二种创建方式 （将列表转换为堆结构）
nums = [2, 3, 5, 1, 54, 23, 132]
heapq.heapify(nums)
print(nums)
```

### 访问堆内容

```python
import heapq
nums = [2, 43, 45, 23, 12]
heapq.heapify(nums)
# print (list((heapq.heappop(nums) for _ in range(len(nums)))))
result = [heapq.heappop(nums) for _ in range(len(nums))]
print(result)
```

### merge合并

```python
# heapq.merge() 返回的是可迭代对象,用于合并多个排序后的序列成一个排序后的序列，返回排序后的值的迭代器。
import heapq
num1 = [32, 3, 5, 34, 54, 23, 132]
num2 = [23, 2, 12, 656, 324, 23, 54]
num1 = sorted(num1)
num2 = sorted(num2)

res = heapq.merge(num1, num2)
print(list(res))
```

### 删除最小的并添加一个元素

```python
# 如果需要删除堆中最小元素并加入一个元素，可以使用heapq.heaprepalce() 函数
import heapq
nums = [1, 2, 4, 5, 3]
heapq.heapify(nums)

heapq.heapreplace(nums, 23)
print([heapq.heappop(nums) for _ in range(len(nums))])
```

### 获取最大最小元素

```python
# 如果需要获取堆中最大或最小的范围值，则可以使用`heapq.nlargest()` 或`heapq.nsmallest()`函数
import heapq

nums = [1, 3, 4, 5, 2]
print(heapq.nsmallest(3, nums))
print(heapq.nlargest(3, nums))
```

