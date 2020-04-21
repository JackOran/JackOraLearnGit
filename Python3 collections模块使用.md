#Python3 collections模块使用

###1.Counter(类似于字典)

- 可以支持方便的，快速的计数

```python
#Python3 Collections模块
from collections import Counter
cn = Counter()
word_list = ["a","b","a","c","d","b"]
for word in word_list:
    cn[word] += 1
print(cn)

#Counter对象类似于字典，如果某个项缺失，会返回0，而不是报出KeyError
cn["a"]
#删除
del cn["a"]

#update 加
a1 = Counter({"a":4,"b":2,"c":4})
a2 = Counter({"a":3,"b":1,"c":2})
a1.update(a2)
a1

#subtract 减
b1 = Counter(a=4,b=2,c=3)
b2 = Counter(a=1,b=1,c=2)
b1.subtract(b2)
b1
```

### 2.deque(类似于列表)

- deque是栈和队列的一种广义实现，deque是"double-end queue"的简称；deque支持线程安全、有效内存地以近似O(1)的性能在deque的两端插入和删除元素。

- **append(x)，** 将x添加到deque的右侧；

  **appendleft(x)，** 将x添加到deque的左侧；

  **clear()，** 将deque中的元素全部删除，最后长度为0；

  **count(x)，** 返回deque中元素等于x的个数；

  **extend(iterable)，** 将可迭代变量iterable中的元素添加至deque的右侧；

  **extendleft(iterable)，** 将变量iterable中的元素添加至deque的左侧，往左侧添加序列的顺序与可迭代变量iterable中的元素相反；

  **pop()，** 移除和返回deque中最右侧的元素，如果没有元素，将会报出IndexError；

  **popleft()，** 移除和返回deque中最左侧的元素，如果没有元素，将会报出IndexError；

  **remove(value)，** 移除第一次出现的value，如果没有找到，报出ValueError；

  **reverse()，** 反转deque中的元素，并返回None；

  **rotate(n)，** 从右侧反转n步，如果n为负数，则从左侧反转，d.rotate(1)等于d.appendleft(d.pop())；

  **maxlen，** 只读的属性，deque的最大长度，如果无解，就返回None；

  ```python
  #deque 双端队列
  from collections import deque
  d = deque('abc')
  for ele in d:
      print(ele.upper())
      
  #添加单个迭代对象
  d.append('i')
  d.appendleft('A')
  
  #返回移除最右侧元素
  d.pop()
  #返回移除最左侧元素
  d.popleft()
  
  #翻转并用列表表示
  list(reversed(d))
  
  #添加多个迭代对象
  d.extend("ijk")
  d.extendleft('eee')
  #删除
  d.remove("a")
  #翻转
  d.reverse()
  ```

  