# Dijkstra双栈算术表达式求值算法

```java
package test;

import edu.princeton.cs.introcs.StdIn;
import edu.princeton.cs.introcs.StdOut;

import java.util.Stack;

//Dijkstra双栈表达式求值算法
public class Evaluate {
    public static void main(String[] args) {
        //运算符和操作数
        Stack<String> ops = new Stack<String>();
        Stack<Double> vals = new Stack<Double>();
      
        //判断运算符
        while (!StdIn.isEmpty()) {
            String s = StdIn.readString();
            if (s.equals("(")){

            }
            else if (s.equals("+")){
                ops.push(s);
            }
            else if (s.equals("-")) {
                ops.push(s);
            }
            else if (s.equals("*")) {
                ops.push(s);
            }
            else if (s.equals("/")) {
                ops.push(s);
            }
            else if (s.equals("sqrt")) {
                ops.push(s);
            }
            else if (s.equals(")")) {
                //运算符和操作数弹出，经过计算后结果入栈
                String op = ops.pop();
                Double v = vals.pop();
                if (op.equals("+")) {
                    v = vals.pop() + v;
                }
                else if (op.equals("-")) {
                    v = vals.pop() - v;
                }
                else if (op.equals("*")) {
                    v = vals.pop() * v;
                }
                else if (op.equals("/")) {
                    v = vals.pop() / v;
                }
                else if (op.equals("sqrt")) {
                    v = Math.sqrt(v);
                }
            }
            else {
                vals.push(Double.parseDouble(s.trim()));
            }
        }
        StdOut.println(vals.pop());
    }
}

```

![image-20200420145616709](/Users/apple/Library/Application Support/typora-user-images/image-20200420145616709.png)

#### 报错说是pop出错

