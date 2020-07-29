### [x 的平方根](https://leetcode-cn.com/problems/sqrtx/)

> 实现 int sqrt(int x) 函数。
>
> 计算并返回 x 的平方根，其中 x 是非负整数。
>
> 由于返回类型是整数，结果只保留整数的部分，小数部分将被舍去。
>
> 示例 1:
>
> 输入: 4
> 输出: 2
> 示例 2:
>
> 输入: 8
> 输出: 2
> 说明: 8 的平方根是 2.82842..., 
>      由于返回类型是整数，小数部分将被舍去。

#### 二分查找

- 抛物线
- y = x ^ 2在y轴的右侧单调递增
- 具有上下界

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 0 and x == 1:
            return x
        low, high = 0, x
        while low <= high:
            mid = (low + high)//2
            if mid * mid == x:
                return int(mid)
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1
        return int(high)
```

```java
class Solution {
    public int mySqrt(int x) {
        
        if (x == 0 || x == 1){
            return x;
        }
        long low = 0, high = x;
        while (low <= high){
            long mid = low + (high - low) / 2;
            System.out.println(mid);
            if (mid * mid == x){
                return (int) mid;
            }else if(mid * mid < x){
                low = mid + 1;
            }else{
                high = mid - 1;
            }
        }
        return (int) high;
    }
}
```

#### 牛顿迭代法

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        
        temp = x
        while temp * temp > x:
            temp = (temp + x/temp)/2
        return temp
```

```python
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        temp = x//2
        while temp * temp > x:
            temp = (temp + x/temp) // 2
        return int(temp)
```

