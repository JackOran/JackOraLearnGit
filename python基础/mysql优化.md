# 6、mysql优化
## 1、索引                 

### 一、作用

- 1、约束

- 2、加速查找

### 二、分类

- 1、主键索引

	- 特点：最多有一个、不能为空、不能重复、加速查找

- 2、普通索引

- 3、唯一索引

	- 特点：可以有多个、不能重复、加速查找

- 4、联合索引

	- 分类：联合主键索引、联合唯一索引、联合普通索引

- 5、全文索引

### 三、为什么使用索引？

- 快

- select * from student where name='tom40000';慢

- select * from student where id='10000';快

- 小学时候使用字典

- 无索引：从前到后依次遍历查找

### 四、原理：

- 额外的文件保存特殊的数据结构

- 注意：查询快，插入、更新、删除操作会变慢

### 五、索引算法种类

- 1、btree索引

	- 名称：二叉树

	- mysql使用的格式，效率高

- 2、hash索引

	- 单值查询速度快，但是在文件中所以不是按照顺序排序的，所以范围查询时效率不会太高

### 六、创建索引

- 1、主键索引

	- 不建议额外添加，在建表时已经创建

- 2、全文索引

	- 作用：用于在一篇文章中，检索文本信息的

	- 说明：mysql从3.23.23版本开始支持全文索引，全文索引的类型为fulltext，可以创建在varchar或者text类型的字段身上。

	- 注意：一般不用mysql的，一般会基于其他框架实现

- 3、普通索引

	- 格式：create index 索引名称 on 表名(列名);

	- create index index_name on student(name);

	- 删除：drop index 索引名称 on 表名;

	- 索引合并

		- 把多个单列索引合并使用

		- 假设：

			- create index index_email on student(email);

			- create index index_name on student(name);

		- 搜索：

			- where name='';

			- where email='';

			- where name='' and email='';

- 4、唯一索引

	- 格式：create unique index 索引名称 on 表名(列名);

	- 删除：drop unique index 索引名称 on 表名;

- 5、联合索引

	- a、联合唯一索引

		- 格式：create unique index 索引名称 on 表名(列名1,列名2,……);

		- 删除：drop unique index 索引名称 on 表名;

	- b、联合普通索引

		- 格式：create index 索引名称 on 表名(列名1,列名2,……);

		- 删除：drop index 索引名称 on 表名;

	- 最左侧前缀匹配特性：

		- 假设：create index index_name_email_age on student(name, email, age);

		- 能使用到索引的情况：

			- 1、select * from student where name='tome40000';

			- 2、where name='tome40000' and email='11@qq.com';

			- 3、where name='tome40000' and age=5;

			- 4、where name='tome40000' and email='11@qq.com' and aeg=5;

		- 不走索引的情况：

			- 1、where email='11@qq.com';

			- 2、where age=5;

			- 3、where email='11@qq.com' and age=5;

- 6、索引合并VS联合索引

	- 联合索引效率高于索引合并

- 7、覆盖索引

	- 假设：create index index_name on student(name);

	- 使用：

		- select * from student where name='tom42000';

		- #直接在索引文件中获取信息，无需在去表中获取，这种行为就叫覆盖索引

		- select name from student where name='tom42000';

### 七、索引的注意事项

- 1、频繁查找的列创建索引

- 2、避免使用select *

- 3、尽量使用count(1)或者count(列)替代count(*)，因为在有些数据中count(*)效率低，但是在现版本的mysql中不存在这个问题

- 4、创建表是尽量使用char替换varchar

- 5、表的字段顺序固定长度字段优先

- 6、联合索引替代多个单列索引合并(经常使用多个条件查询时)

- 7、尽量使用短索引

	- 1352345234@qq.com

	- 1352343333@qq.com

	- 1352555555@qq.com

	- 1352666666@qq.com

	- 1352777777@qq.com

	- 给字段类型为text类型添加索引必须使用端索引

	- 假设xxx字段为text类型

	- create index index_xxx on table(xxx);报错

	- create index index_xxx on table(xxx(5));xxx字段前五个字符为索引

- 8、使用连接(join)替代子查询

- 9、类型需要一致

- 10、索引散列值重复少不适合建立索引

	- 性别不适合建立索引

### 八、命中索引

- 给字段创建索引，并不是所有的情况都能使用到索引，索引要想生效需要命中索引。

- 无法命中索引的请情况

	- 1、like 'xxx%'

		- 假设：create index index_name on student(name);

		- select * from student where name like 'tom89%';

	- 2、使用函数

		- select * from student where reverse(name)='tom12345';

	- 3、or

		- or有时会导致无法命中索引

		- 假设：索引为id、name

		- 特别的：当or条件中有未建立索引的列才失效

		- 走索引：

			- select * from student where id=444444;

			- select * from student where sid=888888 or name='tom999998';

		- 不走索引：

			- select * from student where sid=888888 or email='9753308846@qq.com';

		- 走索引：

			- select * from student where sid=888888 or email='9753308846@qq.com' and name='tom880788';

	- 4、类型不一致

		- 如果列是字符串类型，传入条件必须使用''引起来

		- 假设：索引为id、name

		- select * from student where name=999;

		- 注意：主键列不适用

	- 5、!=

		- 普通索引不走索引

			- select * from student where name!='tom99999';

		- 注意：主键列不适用

	- 6、>

		- 普通索引不走索引

		- 注意：如果是主键或者索引类型是整数类型，还是会走索引

	- 7、order by

		- 当根据索引排序时，选择的映射如果不是索引，则不走索引

			- 不走：select email from student order by name desc;

			- 走：select name from student order by name desc;

		- 注意：如果对主键排序，还是会走索引的

			- select * from student order by id desc;

	- 8、联合索引没有使用最左侧前缀

## 2、计划执行              

### 作用：让mysql预估执行操作的时间(一般正确)

### 使用：explain SQL语句

### 字段：

- 1、select_type

	- 查询类型

		- simple   简单查询

		- primary  最外层查询

		- subquery 映射子查询

		- derived  子查询

		- union    联合查询

		- union result  使用联合的结果

- 2、table

	- 正在访问的表名

- 3、type

	- 查询时的访问方式

	- all

	- index

	- range

	- index_range

	- ref_or_null

	- ref

	- eq_ref

	- const

	- system

- 4、 possible_keys

	- 可能使用的索引

- 5、key

	- 真实使用的索引

- 6、key_len

	- mysql中使用索引字段的长度

- 7、rows

	- mysql估计为了找到所需要的行而读取的数据行数

- 8、Extra

	- 包含mysql解决查询的详细信息

	- Using index

	- Using where

	- Using temporary

	- Using filesort

	- Range checked for each recode

## 3、分页优化            

### select * from student limit 2000000,10;

- 解决方案：

	- 1、不让访问

	- 2、索引表中扫描

		- select * from student where id in(select id from student limit 200000,10);

	- 3、记住当前页数据的最大id和最小id

		- max_id  min_id

		- a、只有上一页和下一页

			- 下一页：

				- select * from student where id > max_id limit 10;

			- 上一页：

				- select * from student where id < min_id order by id desc limit 10;

		- b、上一页  100  [101]  102  103  104  105  下一页

			- 目前在101，点击104

				- select * from student where id in(select id from (select id from student where id > max_id limit 30) as T order by T.id desc limit 10);

			- 目前在104，点击101

				- select * from student where id in(select id from (select id from student where id < max_id limit 30) as T order by T.id asc limit 10);

## 4、视图         

### 概念：给SQL起别名，方便以后使用，类似临时表

### select * from student where id > 40000;

### select * from (select * from student where id > 40000) where age > 4;

### select * from (select * from student where id > 40000) where age > 20;

### select * from (select * from student where id > 40000) where age > 50;

### 创建视图

- 格式：create view 视图名称 as SQL;

- create view v1 as select * from student where id > 40000;

### 使用：

- select * from v1;

### 注意：视图虚拟存在

### 删除：drop view 视图名称;

### 修改：alter view 视图名称 as SQL;

### 注意：视图不常用，可读性不高

## 5、触发器

### 作用：当对某张表做增删改操作时，可以使用触发器自定义关联行为

### 注意：查询不会触发触发器

### 举例：在用户注册时，会在用户表中增加一条数据，同时也要在日志表中增加一条数据

### 解决例子中的问题

- 1、程序级别解决，两条SQL语句顺序执行

- 2、触发器解决，只需要再用户表中插入，而无需手动往日志表中添加数据

### 实验
```sql
- create table grade(  
      id int not null auto_increment primary key,  
      name char(20)  
  ) engine=innodb default charset=utf8;  
  create table teacher(  
      id int not null auto_increment primary key,  
      name char(20)  
  ) engine=innodb default charset=utf8;  
    
    
    
  #如此创建会出现问题，结束字符问题  
  create trigger aaa after insert on grade for each row  
  begin  
      insert into teacher(name) values("tom");  
  end  
    
    
    
  delimiter：修改结束字符  
  delimiter //  
  create trigger aaa after insert on grade for each row  
  begin  
      insert into teacher(name) values("tom");  
  end //  
  delimiter ;  
    
    
    
  需求：插入一个班级后，插入的老师的名字与班级名相同  
  insert into grade(name) values("python03");  
    
  delimiter //  
  create trigger aaa after insert on grade for each row  
  begin  
      insert into teacher(name) values(new.name);  
  end //  
  delimiter ;  
    
  注意：new表示新数据  
    
    
  需求：删除一个班级后，在插入一个老师，老师的名字为删除的班级的名字  
  delete from grade where id=1;  
    
  delimiter //  
  create trigger bbb after delete on grade for each row  
  begin  
      insert into teacher(name) values(old.name);  
  end //  
  delimiter ;  
    
  注意：old表示老数据
```
### 创建触发器

- 1、插入前

	- create trigger 触发器名 before insert on 表名 for each row  
	            begin  
	                ……  
	            end

- 2、插入后

	- create trigger 触发器名 after insert on 表名 for each row  
	            begin  
	                ……  
	            end

- 3、删除前

	- create trigger 触发器名 before delete on 表名 for each row  
	            begin  
	                ……  
	            end

- 4、删除后

	- create trigger 触发器名 after delete on 表名 for each row  
	            begin  
	                ……  
	            end

- 5、更新前

	- create trigger 触发器名 before update on 表名 for each row  
	            begin  
	                ……  
	            end

- 6、更新后

	- create trigger 触发器名 after update on 表名 for each row  
	            begin  
	                ……  
	            end

## 6、函数  

### 内置函数

### 自定义函数
```sql
- delimiter //  
  create function func3(  
      a int,  
      b int)  
  returns int  
  begin  
      declare num int default 0;  
      set num = a + b;  
      return(num);  
  end //  
  delimiter ;
```
## 7、NULL字段

### 建议：以后在建表时额外增加几个无用(备用)的字段

```sql
create table student(  
      id int not null auto_increment primary key,  
      name char(20),  
      grade_id int,  
      constraint fk_student_grade foreign key(grade_id) references grade(id)  
  ) engine=innodb default charset=utf8;  
  alter 增加一个money 字段  
    
    
    
  create table student(  
      id int not null auto_increment primary key,  
      name char(20),  
      grade_id int,  
      constraint fk_student_grade foreign key(grade_id) references grade(id),  
      a int null,   
      b int null,  
      c int null,  
      d int null  
  ) engine=innodb default charset=utf8;   
  修改备用字段的名或类型，保证以前的数据该字段都有值
```
