# 5、mysql数据和可视化软件的使用，模块操作msyql

## SQL语句数据行操作    

### 一、增

- 1、全列插入

  - insert into 表名 values(值1,值2,……);

  - 注意：主键是自增长，但是在全列插入式需要占位，插入成功后以实际值为准

  - insert into student values(0, 18, 'sunck');

  - insert into student values(0, 50, '刘德华');

  - insert into student values(0, 40, '刀郎');

- 2、缺省插入

  - inset into 表名(列1,列2,……) values(值1,值2,……);

- 3、同时插入多条数据

  - insert into 表名 values(值1,值2,……),(值1,值2,……),……;

  - insert into 表名(列1,列2,……) values(值1,值2,……),(值1,值2,……),……;

- 将一张表的数据导入另一张表中

  - t1(name, age)   t2(name, age)

  - t2中有2条数据，t1中没有数，可以将t2表中的数据直接导入到t1表中

  - insert into t1(name, age) select name,age from t2;

### 二、删

- 格式：

  - 根据条件删除某些数据：

    - delete from 表名 where 条件;

  - 清空表：

    - delete from 表名;

    - truncate table 表名;

- 示例：

  - delete from t1 where id = 1;

  - delete from t1 where id != 1;

  - delete from t1 where id > 1;

  - delete from t1 where id >= 1;

  - delete from t1 where id >= 1 and id <= 5;

  - delete from t1 where id < 4 or id > 5;

### 三、改

- 格式：

  - 根据条件具体修改某些数据：

    - update 表名 set 列1=值1,…… where 条件;

  - 全部列修改：

    - update 表名 set 列1=值1,……;

- 示例：

  - update t2 set age=18 where name='lilei';

### 四、逻辑删除

- 物理删除：将数数据从数据中删除。delete操作属于物理删除，物理删除的数据无法恢复，对于一些重要的数据，以后建议使用逻辑删除。

- 逻辑删除：本质是修改(update)操作，对于重要数据表，增加一个isDelete字段，一般默认为0(没有被删除的的意思)，该字段逻辑上表示该条数据是否被删除，真实情况是在数据库中本条数据还存在

### 五、查

- 1、查询全部

  - select * from 表名;

  - 说明：

    - a、from关键字后面写的表名，表示数据来源于这张表

    - b、select后面写表中的列名，如果是*，表示结果中显示表中所有的列

    - c、如果要查询多个列，列之间使用逗号分隔

- 2、条件查询

  - select * from 表名 where 条件;

  - a、比较运算符

    - =    >    <    >=    <=    !=     <>

    - select * from student where age > 30;

  - b、逻辑运算符

    - and    or    not

    - select * from student where age > 20 and age < 30;

    - select * from student where age < 20 or age > 30;

    - select * from student where not age < 20;

  - c、范围查询

    - in：表示在一个非连续的范围内

    - select * from student where id in(1,3,5);

    - between...and...：表示在一个连续的范围内

    - select * from student where id between 3 and 6;

  - d、空判断

    - is null：判空

    - select * from student where sid is null;

    - is not null：判非空

    - select * from student where sid is not null;

    - 注意：null 与 ''(空字符)是不同的

  - 优先级：    

    - 小括号，not，比较运算符，逻辑运算符

    - and比or优先运算，如果同时出现并希望先算or，需要结合小括号使用

- 3、模糊查询

  - 使用 like

  - %：表示任意多个字符

  - _：表示一个任意字符

  - select * from student where name like '高%';

  - select * from student where name like '高_';

  - select * from student where name like '高\%%';

- 4、分页查询

  - a、select * from 表名 limit [start,]count;

    - start：从start开始获取，如果没有默认从0开始

    - count：获取count条数据

  - select * from student limit 0, 5;

  - select * from student limit 5, 5;

  - select * from student limit 10, 5;

  - b、select * from 表名 limit count offset start;

  - select * from student limit 5 offset 0;

  - select * from student limit 5 offset 5;

  - select * from student limit 5 offset 10;

- 5、排序查询

  - 语法：select * from 表名 order by 列1 asc|desc[, 列2 asc|desc[,……]];

  - 说明：

    - 将行数据库按照列1进行排序，如果某些列1值相同时，则在按照列2进行排序，以此类推

    - 默认排序升序排序

    - asc表示升序排序

    - desc表示降序排序

  - select * from student order by sid asc, age asc, id desc;

- 6、聚合

  - 目的：为了快速得到统计数据

  - count(*)：表示计算总行数，括号中写*与列名，结果相同

  - max(列)：表示求此列的最大值

  - min(列)：表示求此列的最小值

  - sum(列)：表示此列的和

  - avg(列)：表示求此列的平均值

  - select count(*) from student where age = 34;

  - select max(age) from student where name like'高%';

  - select min(age) from student where name like'高%';

  - select sum(age) from student where name like'高%';

  - select avg(age) from student where name like'高%';

- 7、组合

  - 概述：

    - a、按照字段分组，表示此字段相同的数据会被放到一个组中

    - b、分组后，只能查询出相同的数据列，对于有差异的数据列无法出现在结果集中

    - c、可以对分组后的数据进行统计，做聚合运算

  - 语法：

    - select 列1,列2,……,聚合 from 表名 group by 列1,列2,……;

  - 示例：

    - select * from student;

    - select * from student group by grade_id;报错

    - select grade_id from student group by grade_id;

    - select grade_id,count(id) from student group by grade_id;

  - 分组后的数据筛选：

    - 需求：展示人数多于1的组信息

    - select grade_id,count(id) from student group by grade_id where count(id) > 1;

      - 报错
        e
    - 使用having

      - 说明：如果对于聚合函数结果进行二次筛选时必须使用having

      - 语法：select 列1,列2,……,聚合 from 表名 group by 列1,列2,…… having 列1,……聚合……;

      - 示例：select grade_id,count(id) from student group by grade_id having count(id) > 1;

    - having与where区别：

      - a、where是对from后面指定的表进行数据筛选，对于原始数据的筛选

      - b、having是对group by的结果进行筛选

- 8、关联查询（连接查询）

  - 需求：显示所有学生，不仅显示班级id，也要把班级名称显示出来

  - 实现：

    - select * from student,grade;#没有提供关系

    - select * from student,grade where student.grade_id = grade.id;

    - select grade_id,student.name,grade.name from student,grade where student.grade_id = grade.id;

  - 关联分类：

    - 1、表A left join 表B on

      - 表A与表B匹配的行会出现在结果集中，外加表A中独有的数据，未对应的数据使用null填充。(左边全部显示)

    - 2、表A right join 表B on

      - 表A与表B匹配的行会出现在结果集中，外加表B中独有的数据，未对应的数据使用null填充。(右边全部显示)

    - 3、表A inner join 表B on

      - 表A与表B匹配的行会出现在结果集中(将有null的行隐藏)

    - select * from student left join grade on student.grade_id = grade.id;

    - insert into student(name) values("sunck");

    - insert into grade(name) values('python05');

    - select * from student right join grade on student.grade_id = grade.id;

    - #交换表位置模拟了右关联

    - select * from grade left join student on student.grade_id = grade.id;

    - select * from student inner join grade on student.grade_id = grade.id;

  - 说明：

    - a、在查询或条件中推荐使用"表名.列名"的语法

    - b、如果多个表中的列名不重复，可以省略"表名."的部分

    - c、早起left与right存在性能上的差异，但是现在的mysql版本中已经没有差异了

  - 临时表： select 查询出来的结果作为表 可以进行链接查询等  比如 select * from student as A

## navicat的使用            

### 连接

### 创建数据库

### 删除数据库

### 建表

### 删表

### 建立关系

### 查询

### SQL注释 

- --空格

### 转成SQL到文件

- 命令实现转成SQL到文件

  - 数据表结构+数据

    - mysqldump -u用户名 -p密码 数据库名 > 转储文件名

  - 数据表结构

    - mysqldump -u用户名 -p密码 -d 数据库名 > 转储文件名

  - 示例

    - mysqldump -usunck -psunck1999 axf > axf.sql  
          mysqldump -usunck -psunck1999 -d axf > axf.sql

- 将转成文件导入数据库

  - 1、创建数据库

    - 2、导入

      - mysql -u用户名 -p密码 数据库名 < 转储文件名


## pymysql模块的使用        

### 1、链接数据库              

```
# -*- coding:utf-8 -*-  
    
  # 导入pymysql  
  import pymysql  
    
  # 连接数据库  
  # 参数1：mysql服务所在IP地址  
  # 参数2：用户名  
  # 参数3：用户密码  
  # 参数4：要连接的数据库  
  # 参数charset：显示汉字相关  
  db = pymysql.connect("www.sunck.wang", "sunck", "sunck1999", "axf", charset="utf8")  
    
  #创建cursor对象  
  cursor = db.cursor()  
    
  #待执行的SQL语句  
  sql = "select version();"  
    
  # 数据库的一些操作  
  # 执行SQL语句
  db.begin()
  cursor.execute(sql)  
  db.commit()
  # 获取返回信息  
  data = cursor.fetchone()  
  print(data)  
    
  # 断开数据库连接  
  cursor.close()  
  db.close()  
```


### 2、建表                     

```
#-*- coding:utf-8 -*-  
  import pymysql  
    
  db = pymysql.connect("www.sunck.wang", "sunck", "sunck1999", "axf", charset="utf8")  
  cursor = db.cursor()  
    
  # 建表之前首先判断表是否存在，存在则删除  
  sql1 = "drop table if exists student;"  
  sql2 = "create table student(id int not null auto_increment primary key,name char(20)) engine=innodb default charset=utf8;"  
    
    
  cursor.execute(sql1)  
  cursor.execute(sql2)  
    
    
    
  cursor.close()  
  db.close()  
```


### 3、增                      

```
# -*- coding:utf-8 -*-  
  import pymysql  
    
  db = pymysql.connect("www.sunck.wang", "sunck", "sunck1999", "axf", charset="utf8")  
  cursor = db.cursor()  
    
  #待执行的SQL语句  
  sql = "insert into student values(0, 'lilei');"  
    
  try:  
      cursor.execute(sql)  
      # 提交事物，真正写入数据库  
      db.commit()  
  except:  
      # 如果提交失败，回滚到上次提交的数据  
      db.rollback()  
    
  cursor.close()  
  db.close()  
```


### 4、改                       

```
# -*- coding:utf-8 -*-  
  import pymysql  
    
  db = pymysql.connect("www.sunck.wang", "sunck", "sunck1999", "axf", charset="utf8")  
  cursor = db.cursor()  
    
  sql = "update student set name='hanmeimeaaai'"  
    
  try:  
      cursor.execute(sql)  
      db.commit()  
      print("------------", cursor.rowcount)  
  except:  
      db.rollback()  
    
    
    
  cursor.close()  
  db.close()  
```


### 5、删

```
# -*- coding:utf-8 -*-  
  import pymysql  
    
  db = pymysql.connect("www.sunck.wang", "sunck", "sunck1999", "axf", charset="utf8")  
  cursor = db.cursor()  
    
  sql = "delete from student where id=1;"  
    
  try:  
      cursor.execute(sql)  
      db.commit()  
  except:  
      pass  
    
  cursor.close()  
  db.close()  
```


### 6、查

```
-*- coding:utf-8 -*-  
  import pymysql  
    
    
  '''  
  fetchone()  
  功能：获取下一个查询结果集，结果集是一个对象  
    
  fetchall()  
  功能：接收全部的返回结果  
    
  rowcount  
  是一个只读属性，返回执行execute()方法后影响的行数  
  '''  
    
    
    
    
  db = pymysql.connect("www.sunck.wang", "sunck", "sunck1999", "axf", charset="utf8")  
  # cursor = db.cursor()  
  # 以字典形式显示  
  cursor = db.cursor(cursor=pymysql.cursors.DictCursor)  
    
  sql = "select * from student where id>=3;"  
    
  try:  
      cursor.execute(sql)  
      # 获取所有数据列表  
      # reslist = cursor.fetchall()  
      # print(reslist)  
      # for row in reslist:  
      #     print(row)  
    
    
    
      # res = cursor.fetchone()  
      # print(res)  
    
    
      for i in range(cursor.rowcount):  
          res = cursor.fetchone()  
          print(res)  
    
  except:  
      print("查询有误")  
    
    
  cursor.close()  
  db.close()  
```

### 7、SQL注入

```python
# -*- coding:utf-8 -*-  
  import pymysql  
    
  account = input("账号：")  
  passwd = input("密码：")  
    
    
  db = pymysql.connect("www.sunck.wang", "sunck", "sunck1999", "axf", charset="utf8")  
  cursor = db.cursor(cursor=pymysql.cursors.DictCursor)  
    
  # sql = "select * from user where account='%s' and passwd='%s';"%(account, passwd)  
  # select * from user where account='111' -- ' and passwd='';  
  # select * from user where account='aaa' or 1=1 -- ' and passwd='';  
    
  #防止SQL注入  
  # sql = "select * from user where account=%s and passwd=%s;"  
  sql = "select * from user where account=%(account)s and passwd=%(passwd)s;"  
    
  print(sql)  
    
  try:  
      #execute为执行，格式化的数据在这里传值，以规避SQL注入  
      # cursor.execute(sql, [account, passwd])  
      cursor.execute(sql, {"account":account, "passwd":passwd})  
    
    
      res = cursor.fetchall()  
      if res:  
          print("登陆成功", res)  
      else:  
          print("登陆失败")  
  except:  
      print("查询有误")  
    
    
  cursor.close()  
  db.close()  
```


### 8、增加多条数据

```python
# -*- coding:utf-8 -*-  
  import pymysql  
    
  db = pymysql.connect("www.sunck.wang", "sunck", "sunck1999", "axf", charset="utf8")  
  cursor = db.cursor()  
    
  #待执行的SQL语句  
  sql = "insert into student(name) values(%s);"  
    
  try:  
      cursor.executemany(sql, [("aaa",),("bbb",),("ccc",)])  
      db.commit()  
  except:  
      db.rollback()  
    
  cursor.close()  
  db.close()  
```


### 9、新增数据的自增ID

```python
 # -*- coding:utf-8 -*-  
  import pymysql  
    
  db = pymysql.connect("www.sunck.wang", "sunck", "sunck1999", "axf", charset="utf8")  
  cursor = db.cursor()  
    
  sql = "insert into article(title) values(%s);"  
    
  try:  
      cursor.execute(sql, ["sunck"])  
    
      # 插入对应的媒体，得直到刚才插入的文章的id号  
      print("--------", cursor.lastrowid)  
    
      db.commit()  
  except:  
      db.rollback()  
    
  cursor.close()  
  db.close()  
```

