### 单例模式

```python
"""单例：是一种软件设计模式，该模式的主要目的是确保一个类只有一个实例存在

实现单例的方式：
    1、使用模块
    2、使用__new__
    3、使用装饰器
    4、使用元类
    
"""
```

### 使用模块实现单例

```python
# -*- coding:utf-8 -*-

class Card(object):
    def __init__(self, cardId, passwd, money):
        self.cardId = cardId
        self.passwd = passwd
        self.money  = money


c = Card("888888", "666666", 10000)
```

### 使用__new__实现单例

```python
# __new__()方法：是一个类方法，返回一个对象的实例，在使用类实例化对象时自动调用，目的是在堆区开辟一片内存空间，会在__init__之前调用
# 使用：创建单例类

class Person(object):

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, "isinstance"):
            cls.instance = super(Person, cls).__new__(cls)
        return cls.instance


per1 = Person()
per1.name = "lilei"
per2 = Person()
print(per1.name)
print(per1 is per2)
```

### 使用装饰器实现单例

```python
def card(cls):
    instance = {}
    def getinstance(*args, **kwargs):
        if cls not in instance:
            instance[cls] =cls(*args, **kwargs)
        return instance[cls]
    return getinstance

@card
class Card(object):
    pass

c1 = Card()
c2 = Card()

print(c1 is c2)
```

### 重写

```python
#重写：将继承的方法重写写一遍，在原有的功能基础上添加一些新的功能
class Person(object):
    #重写：将继承的方法重写写一遍，在原有的功能基础上添加一些新的功能
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
    def say(self):
        return "my name is %s, I am %d years old"%(self.name, self.age)
    #需求：打印该类型的对象时，想打印出对象的各个属性值
    #解决：重写__str__方法
    #__str__()方法：在调用print打印对象时自动调用

    #是显示给用户的
    def __str__(self):
        return "name:%s\nage:%d\nheight:%.2f\nweight:%.2f"%(self.name, self.age, self.height, self.weight)
    #是给机器用的，在python解释器里直接敲对象后回车自动调用
    def __repr__(self):
        return "name:%s\nage:%d\nheight:%.2f\nweight:%.2f"%(self.name, self.age, self.height, self.weight)

per = Person("lilei", 20, 170, 80)
print(per)


```

### 读文件

```python
"""
过程：
    1、找到文件
    2、打开文件
    3、读取文件内容
    4、关闭文件
    
    原型：
    def open(file, mode='r', buffering=None, encoding=None, errors=None, newline=None, closefd=True)
'''

'''打开方式
r     以只读方式打开文件，文件的引用将会放在文件开头
rb    以二进制格式打开只读文件，文件的引用将会放在文件开头
r+    以读写方式打开文件，文件的引用将会放在文件开头
w     以只写方式打开文件，如果该文件已经存在，则将其内容覆盖，如果不存在则会创建文件
wb    以二进制格式打开只写文件，如果该文件已经存在，则将其内容覆盖，如果不存在则会创建文件
w+    以读写方式打开文件，如果该文件已经存在，则将其内容覆盖，如果不存在则会创建文件
a     打开一个文件用于追加，如果该文件已经存在，文件的引用将会放在文件的末尾，也就是说新的内容添加到已有内容之后。果不存在则会创建文件进行写入
a+    打开一个文件用于读写，如果该文件已经存在，文件的引用将会放在文件的末尾，也就是说新的内容添加到已有内容之后。果不存在则会创建文件进行写入
'''
#关闭文件：文件使用完后必须关闭，因为文件对象会占用操作系统的资源，并且操作系统同一时间能打开的文件的数量是有限的
fp.close()
```

### 写文件

```python
#简单方式
# with open("sunck.txt", "w") as fp1:
#     fp1.write("asd")
```

### os模块

```python
# 获取当前目录   .
print(os.curdir)
# 得到当前工作目录的绝对路径
print(os.getcwd())
# 返回指定目录下的所有文件和目录   listdir([path]),没有path返回当前工作目录下的
print(os.listdir(r"C:\Users\xlg\Desktop\gp01"))
#创建指定目录
# os.mkdir(r"C:\Users\xlg\Desktop\gp01\day14")
#删除目录
# os.rmdir(r"C:\Users\xlg\Desktop\gp01\day14")
#拼接路径
print(os.path.join(r"C:\Users\xlg\Desktop\gp01\day13\abc", "kaige.txt"))
#判断是否是目录（得存在），是返回True, 否则返回False,
print(os.path.isdir(r"C:\Users\xlg\Desktop\gp01\day13\code"))
#判断普通文件是否存在，存在返回True， 否则返回False
print(os.path.isfile(r"C:\Users\xlg\Desktop\gp01\day13\code\kaige.txt"))
#判断文件和目录是否存在
print(os.path.exists(r"C:\Users\xlg\Desktop\gp01\day13\abc"))
```

