# Java 栈 stack方法总结

java中stack的方法：

1. push 添加
2. pop 弹出
3. size  大小
4. peek 得到栈顶元素但不弹出
5. is_empty 判断空
6. search（）查找在栈中是否存在

```java
package stack;

import java.util.Stack;

public class Fun_stack {
    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<Integer>();
        stack.push(0);
        System.out.println(stack.search(2));
        System.out.println(stack.size());
        System.out.println(stack.isEmpty());
        stack.push(1);
        System.out.println(stack.peek());
        System.out.println(stack.size());
    }
}

```

