#### [Fizz Buzz](https://leetcode-cn.com/problems/fizz-buzz/)

> 写一个程序，输出从 1 到 n 数字的字符串表示。
>
> 1. 如果 n 是3的倍数，输出“Fizz”；
>
> 2. 如果 n 是5的倍数，输出“Buzz”；
>
> 3.如果 n 同时是3和5的倍数，输出 “FizzBuzz”。
>
> n = 15,
>
> 返回:
> [
>     "1",
>     "2",
>     "Fizz",
>     "4",
>     "Buzz",
>     "Fizz",
>     "7",
>     "8",
>     "Fizz",
>     "Buzz",
>     "11",
>     "Fizz",
>     "13",
>     "14",
>     "FizzBuzz"
> ]

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        res = []
        for i in range(1,n+1):
            if i % 3 == 0 and i % 5 != 0:
                res.append("Fizz")
            elif i % 5 == 0 and i % 3 != 0:
                res.append("Buzz")
            elif i % 3 == 0 and i % 5 == 0:
                res.append("FizzBuzz")
            else:
                res.append(str(i))
        return res
```

##### 通过二进制来做

- 00 不可整除
- 01 可被3整除
- 10 可被5整除
- 11 可同时被3和5整除

```java
class Solution {
    public List<String> fizzBuzz(int n) {
        List<String> list = new ArrayList<>(n);

        for (int i=1; i<=n; i++){
            int res  = 0;
            res += i % 3 == 0 ? 0b1 : 0;
            res += i % 5 == 0 ? 0b10 : 0;

            if (res == 0b1){
                list.add("Fizz");
            }else if (res == 0b10){
                list.add("Buzz");
            }else if (res == 0b11){
                list.add("FizzBuzz");
            }else{
                list.add(String.valueOf(i));
            }
        }
        return list;
    }
}
```

