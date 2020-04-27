### map函数

```python
map(function,iterable,....)
```

map函数第一个参数接收一个**函数名**，后面的参数是一个**迭代序列**，返回的是一个集合。

注：***map函数不改变原list，而是返回一个新的list。***

##### 实例：

```python
def square(x):
  return x**2
map(square,[1,2,3,4,5])

#结果
[1,4,9,16,25]
```

也可以通过***lambda匿名函数***的方法来使用map()函数

```python
map(lambda x,y:x+y,[1,2,3,4],[5,6,7,8])

#结果
[6,8,10,12]
```

通过lambda函数使返回值是一个***元组***：

```python
map(lambda x,y:(x**y,x+y),[1,2,3],[2,3,1])

#结果
[(1,3),(8,5),(3,4)]
```

##### map还可以实现***类型转换***

```python
#将元组转换为list
map(int,(1,2,3))
#结果
[1,2,3]
```

```python
#将字符串转换为list
map(int,'1234')
#结果
[1,2,3,4]
```

```python
#提取字典中的key,并将结果放在一个list中：
map(int,{1:2,2:3,3:4})
#结果
[1,2,3]
```

### filter函数

```python
filter(function,iterable,...)
```

***和map用法类似，但是可以过滤元素的迭代函数。***

```python
def is_even(num):
  return num%2==0

a = filter(is_even,[1,2,3,4,5,6])
print(list(a))
#结果
[2,4,6]
```

```python
#可以通过匿名函数
b = filter(lambda x:x%2==0,[1,2,3,4,5,6])
list(b)
#结果
[2,,4,6]
```

### reduce函数

```python
reduce(function,sequence)
```

作用是用function对序列进行累积操作。

```python
from functools import reduce
reduce(lambda x,y:x*y,[1,2,3,4])
#结果
1*2*3*4=24
24
```

