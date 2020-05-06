### Map的用法

1. Map中的集合，元素是**成对存在的**(理解为夫妻)。每个元素由键与值两部分组成，通过键可以找对所对应的值。
2. Map中的集合**不能包含重复的键，值可以重复**；每个键只能对应一个值。
3. Map中常用的集合为HashMap集合、LinkedHashMap集合。

#### Map的常见用法

- get方法：通过key来获取制定的value。
- put方法：将键值对添加到map中。
- remove方法：通过key将元素移除。
- replace方法：替换元素。
- keySet方法：得到map集合中所以的键。

```java
import java.util.HashMap;
import java.util.Map;

public class MapDemo {
    public static void main(String[] args) {
      Map<String,Integer> map = new HashMap<>();
       //添加元素
        map.put("A",10);
        map.put("B",20);
        map.put("C",3);
        map.put("D",24);
      //获取
      map.get("A");
      //移除
      map.remove("A");
      //遍历
      for(String key : map.keySet()){
        Integer val = map.get(key);
        System.out.println("key"+key+"value"+val);
      }
    }
}
```

