### Queue的用法

- 添加元素
  - add：在队尾添加，队列满，会报错。
  - offer：在队尾添加，队列满，报false。
- 删除元素
  - remove： 删除头部并返回，可删除指定元素。
  - poll： 删除头部并返回，但不可指定元素。
- 获取元素
  - element：返回头部元素。
  - peek：返回头部元素。

```java
package queue;

import java.util.LinkedList;
import java.util.Queue;

public class QueueDemo {
    public static void main(String[] args) {
        Queue<Integer> queue = new LinkedList<Integer>();
        //添加元素
        queue.add(1);
        queue.add(3);
        queue.offer(6);
        System.out.println(queue);
        System.out.println(queue.element());
        queue.offer(5);
        System.out.println(queue);
        //删除
      	queue.remove(3);
        queue.poll();
        System.out.println(queue);
        //获取元素
        queue.element();
        queue.peek();
    }
}

```

