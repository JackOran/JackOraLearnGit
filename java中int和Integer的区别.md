# java中int和Integer的区别

#### ***1.int是基本数据类型，Integer是引用类型，实际是一个对象，存储的是引用对象的地址。***

#### 2.

```java
Integer i = new Integer(100);
Integer j = new Integer(100);
System.out.print(i == j); //false
```

#### *因为new生成的是两个对象，内存地址不同。*

####3.

```java
public class Hello {
    public static void main(String[] args) {
        //System.out.println("Hello java");
        Integer i1 = new Integer(100);
        Integer i2 = new Integer(100);
        int i3 = 100;
        System.out.println(i1==i2); // false
        System.out.println(i1==i3); //true
    }

}
```

####  *对于Integer（是否是new生成的）与int只要值相同就是true。包装类Integer和基本数据类型int进行比较的时候，Integer会自动拆包装为int，实际上就是两个int类型值的比较，相等则为true。*

####4.

```java
public class Hello {
    public static void main(String[] args) {
//        System.out.println("Hello java");
        Integer i1 = new Integer(100);
        Integer i2 = 100;
        System.out.println(i1==i2);//false
    }

}
```

####   *对于new生成的Integer和非new生成的Integer，不管值是否相等，结果都是false。因为非new是java常量池中的对象，而new创建的是指向堆中的对象，内存地址不同，所以为false。*









