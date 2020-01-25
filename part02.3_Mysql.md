## **4、基本SQL命令**

**库管理**

```mysql
    1、查看已有库；
      show databases;

    2、创建库并指定字符集；
      create database 库名 charset utf8;

    3、查看当前所在库；
      select database();

    4、切换库；
      use 库名;

    5、查看库中已有表；
      show tables;

    6、删除库；
      drop database 库名;
```

**表管理**

```mysql
    1、创建表并指定字符集；
      create table 表名(字段名 字段类型 xxx)charset=utf8
    2、查看创建表的语句 (字符集、存储引擎)；
      show create table 表名()
    3、查看表结构;
      desc 表名;
    4、删除表;
      drop table 表名1,表名2,表名3
```

**表记录管理**

```mysql
    1、增 ： insert into 表名(字段名) values(),();
    2、删 ： delete from 表名 where 条件;
    -删之前谨慎,用select检查一下
    -优先考虑伪删除
    3、改 ： update 表名 set 字段名=值,字段名=值 where 条件;
    4、查 ： select 字段名/* from 表名 where
```

**表字段管理（alter table 表名）**

```mysql
    1、增 ： alter table 表名 add 字段名 字段类型 first|after 字段名;
    2、删 ： alter table 表名 drop 字段名;
    -删除有风险
    3、改 ： alter table 表名 modify
     字段名 新类型;
    4、表重命名：alter table 表名 rename 新表名;
```




关系型数据库处理海量并发请求时效率偏低



MySQL数据库
==========================

| Tedu Python 教学部 |
| --- |
| Author：吕泽|
| Days：2天|

-----------
[toc]

## 数据库概述

### 数据存储阶段 

【1】 人工管理阶段

缺点 ：  数据无法共享,不能单独保持,数据存储量有限

【2】 文件管理阶段 （.txt  .doc  .xls）
    
优点 ： 数据可以长期保存,可以存储大量的数据,使用简单

缺点 ：  数据一致性差,数据查找修改不方便,数据冗余度可能比较大

【3】数据库管理阶段

优点 ： 数据组织结构化降低了冗余度,提高了增删改查的效率,容易扩展,方便程序调用，做自动化处理

缺点 ：需要使用sql 或者 其他特定的语句，相对比较复杂

### 数据库应用

>融机构、游戏网站、购物网站、论坛网站 ... ... 

![](mark_down_img/数据库系统.png)

### 基础概念

>数据 ： 能够输入到计算机中并被识别处理的信息集合

>数据结构 ：研究一个数据集合中数据之间关系的

>数据库 ： 按照数据结构，存储管理数据的仓库。数据库是在数据库管理系统管理和控制下，在一定介质上的数据集合。

>数据库管理系统 ：管理数据库的软件，用于建立和维护数据库

>数据库系统 ： 由数据库和数据库管理系统，开发工具等组成的集合 


### 数据库分类和常见数据库

* 关系型数据库和非关系型数据库
      
>关系型： 采用关系模型（二维表）来组织数据结构的数据库 
>关系型的数据库使用比较广泛

> 非关系型： 不采用关系模型组织数据结构的数据库
> 不是用二维表组织数据结构

* 开源数据库和非开源数据库

> 开源：MySQL、SQLite、MongoDB


> 非开源：Oracle、DB2、SQL_Server

* 常见的关系型数据库
  
> MySQL(Oracle)、Oracle、SQL_Server、DB2(IBM) SQLite(嵌入式)  
> 基于B/S模式,MYSQL应用比较广泛


### 认识关系型数据库和MySQL

1. 数据库结构 （图库结构）

>数据元素 --> 记录 -->数据表 --> 数据库

![](mark_down_img/库结构.png)

2. 数据库概念解析

>数据表 ： 存放数据的表格 

>字段： 每个列，用来表示该列数据的含义

>记录： 每个行，表示一组完整的数据

![](mark_down_img/表结构.png)

3. MySQL特点

* 是开源数据库，使用C和C++编写 
* 能够工作在众多不同的平台上
* 提供了用于C、C++、Python、Java、Perl、PHP、Ruby众多语言的API
* 存储结构优良，运行速度快
* 功能全面丰富

4. MySQL安装

>Ubuntu安装MySQL服务
>>安装服务端: sudo apt-get install mysql-server
>>安装客户端: sudo apt-get install mysql-client
>>> 配置文件：/etc/mysql
>>> 命令集： /usr/bin
>>> 数据库存储目录 ：/var/lib/mysql

>Windows安装MySQL
>>下载MySQL安装包(windows)  https://dev.mysql.com/downloads/mysql/
  mysql-installer***5.7.***.msi
>>安装教程去安装

5. 启动和连接MySQL服务

>服务端启动
>>查看MySQL状态: sudo /etc/init.d/mysql status
>>启动服务：sudo /etc/init.d/mysql start | stop | restart

>客户端连接
>>命令格式 
>>>mysql -h主机地址 -u用户名 -p密码
>>>mysql -hlocalhost -uroot -p123456
>>>本地连接可省略 -h 选项: mysql -uroot -p123456

>关闭连接
>> ctrl-D
>> exit


## SQL语句

> 什么是SQL
>
> >结构化查询语言(Structured Query Language)，一种特殊目的的编程语言，是一种数据库查询和程序设计语言，用于存取数据以及查询、更新和管理关系数据库系统。

> SQL语句使用特点
>* SQL语言基本上独立于数据库本身
>* 各种不同的数据库对SQL语言的支持与标准存在着细微的不同
>* 每条命令必须以 ; 结尾
>* SQL命令关键字不区分字母大小写
  参数是区分大小写的

## MySQL 数据库操作

### 数据库操作

1.查看已有库

>show databases;

2.创建库(指定字符集)
>create database 库名 [character set utf8];

```sql
e.g. 创建stu数据库，编码为utf8
create database stu character set utf8;
create database stu charset=utf8;
```

3.查看创建库的语句(字符集)
>show create database 库名;

```sql
e.g. 查看stu创建方法
show create database stu;
```

4.查看当前所在库

>select database();

5.切换库

>use 库名;

> 修改库的默认编码格式    
alter database dict_test default charset  utf8;
```sql
e.g. 使用stu数据库
use stu;
```

6.删除库
>drop database 库名;

```sql
e.g. 删除test数据库
drop database test;
```

7.库名的命名规则
>* 数字、字母、下划线,但不能使用纯数字
>* 库名区分字母大小写
>* 不能使用特殊字符和mysql关键字


### 数据表的管理

1. 表结构设计初步
   
    【1】 分析存储内容
    【2】 确定字段构成
    【3】 设计字段类型
  
2. 数据类型支持

>数字类型：
>>整数类型（精确值） - INTEGER，INT，SMALLINT，TINYINT，MEDIUMINT，BIGINT
>>定点类型（精确值） - DECIMAL
>>浮点类型（近似值） - FLOAT，DOUBLE
>>比特值类型 - BIT

![](mark_down_img/整型.png)

>对于精度比较高的东西，比如money，用decimal类型提高精度减少误差。列的声明语法是DECIMAL(M,D)。
>>M是数字的最大位数（精度）。其范围为1～65，M 的默认值是10。
>>D是小数点右侧数字的数目（标度）。其范围是0～30，但不得超过M。
>>比如 DECIMAL(6,2)最多存6位数字，小数点后占2位,取值范围-9999.99到9999.99。

> 比特值类型指0，1值表达2种情况，如真，假

----------------------------------

>字符串类型：
>>CHAR和VARCHAR类型
>>BINARY和VARBINARY类型
>>BLOB和TEXT类型
>>ENUM类型和SET类型

![](mark_down_img/字符串.PNG)

* char 和 varchar
>char：定长，效率高，一般用于固定长度的表单提交数据存储，默认1字符
>varchar：不定长，效率偏低

---------------------------------------

* text 和blob
>text用来存储非二进制文本
>blob用来存储二进制字节串

* enum 和 set
>enum用来存储给出的一个值
>set用来存储给出的值中一个或多个值
即 enum只能单选   set可以多选

-------------------------------------------


1. 表的基本操作
   
>创建表(指定字符集)
>>create table 表名(
	字段名 数据类型,
	字段名 数据类型,
	...
	字段名 数据类型
	);

字段名:表明这一列的含义


>>* 如果你想设置数字为无符号则加上 unsigned
  默认有符号,即有正数部分
>>* 如果你不想字段为 NULL 可以设置字段的属性为 NOT NULL， 在操作数据库时如果输入该字段的数据为NULL ，就会报错。
不允许为空 必须要填写
>>* DEFAULT 表示设置一个字段的默认值
defaul 与 not none不同时使用 没意义
>>* AUTO_INCREMENT定义列为自增的属性，一般用于主键，数值会自动加1。
主键:唯一确定一条记录的字段
不能为空,不能重复
>>* PRIMARY KEY关键字用于定义列为主键。主键的值不能重复。

```sql
e.g.  创建班级表
create table class_1 (id int primary key auto_increment,
name varchar(32) not null,
age int not null,
sex enum('w','m'),
score float default 0.0);

e.g. 创建兴趣班表
create table interest (id int primary key auto_increment,name varchar(32) not null,hobby set('sing','dance','draw'),course char not null,price decimal(6,2),comment text);
```

> 查看数据表
>
> >show tables；

>查看已有表的字符集
>
>>show create table 表名;

>查看表结构
>
>>desc 表名;

>删除表
>
>>drop table 表名;


## 数据基本操作
>读操作都带有语句from
>插入为into
>删除为set

### 插入(insert)

```SQL
insert into 表名 values(值1),(值2),...;
insert into 表名(字段1,...) values(值1),...;
```

```sql
e.g. 
insert into class_1 values (2,'Baron',10,'m',91),(3,'Jame',9,'m',90);
```

### 查询(select)

```SQL
select * from 表名 [where 条件];
select 字段1,字段名2 from 表名 [where 条件];
```

```sql
e.g. 
select * from class_1;

select name,age from class_1;
```

### where子句

where子句在sql语句中扮演了重要角色，主要通过一定的运算条件进行数据的筛选

MySQL 主要有以下几种运算符：
>算术运算符
>比较运算符
>逻辑运算符
>位运算符

#### 算数运算符

![](mark_down_img/算数.png)

```sql
e.g.
select * from class_1 where age % 2 = 0;
```


#### 比较运算符

![](mark_down_img/比较.png)

```sql
e.g.
select * from class_1 where age > 8;
select * from class_1 where between 8 and 10;
> between 两边都是闭区间 [8,10]

> select * from class_1 where age in (8,9);
```

#### 逻辑运算符
![](mark_down_img/逻辑.png)

```sql
e.g.
select * from class_1 where sex='m' and age>9;
```

#### 位运算符
![](mark_down_img/位.png)

![](mark_down_img/运算符.png)


### 更新表记录(update)

```SQL
update 表名 set 字段1=值1,字段2=值2,... where 条件;
```

```sql
e.g.
update class_1 set age=11 where name='Abby';
```


###　删除表记录（delete）

```SQL
delete from 表名 where 条件;

注意:delete语句后如果不加where条件,所有记录全部清空
```
```sql
e.g.
delete from class_1 where name='Abby';
```


### 表字段的操作(alter)

```SQL
语法 ：alter table 表名 执行动作;

* 添加字段(add)
    alter table 表名 add 字段名 数据类型;
    alter table 表名 add 字段名 数据类型 first;
    alter table 表名 add 字段名 数据类型 after 字段名;
* 删除字段(drop)
    alter table 表名 drop 字段名;
* 修改数据类型(modify)
    alter table 表名 modify 字段名 新数据类型;
* 修改字段名(change)
    alter table 表名 change 旧字段名 新字段名 新数据类型;
* 表重命名(rename)
    alter table 表名 rename 新表名;
```

```sql
e.g. 
alter table interest add date Date after course;
```

### 时间类型数据

mysql时间函数的使用

>时间和日期类型:
>>DATE，DATETIME和TIMESTAMP类型
>>TIME类型
>>年份类型YEAR

![](mark_down_img/时间.PNG)

#### 时间格式

> date ："YYYY-MM-DD"
> time ："HH:MM:SS"
> datetime ："YYYY-MM-DD HH:MM:SS"
> timestamp ："YYYY-MM-DD HH:MM:SS"

注意
insert into 是纯数字插入的

mysql> insert into test01 values(998,164000,20190816,20190816170000,null)
    -> ;
Query OK, 1 row affected (0.00 sec)

mysql> select * from test01;
+---------------------+----------+------------+---------------------+---------------------+
| content             | time     | date       | datetime            | timestamp           |
+---------------------+----------+------------+---------------------+---------------------+
| 998                 | NULL     | NULL       | NULL                | 2019-08-16 16:29:48 |
| 2019-08-16 16:08:53 | NULL     | NULL       | NULL                | 2019-08-16 16:29:48 |
| 998                 | 16:40:00 | 2019-08-16 | 2019-08-16 17:00:00 | 2019-08-16 16:33:56 |
+---------------------+----------+------------+---------------------+---------------------+







  1、datetime ：不给值默认返回NULL值
  
  2、timestamp ：不给值默认返回系统当前时间

#### 日期时间函数

在mysql内可以直接调用该函数,对返回值进行插入、比较等

  * now()  返回服务器当前时间
  * curdate() 返回当前日期
    对应date数据类型 若有时间则自动填充00:00:00

  * curtime() 返回当前时间
    对应time()类型 若有日期则自动填充当前日期
> ------------
  * date(date) 返回指定时间的日期

  * time(date) 返回指定时间的时间
>    用于创建表的时候,设定默认值
#### 时间操作

* 查找操作
```sql
  select * from timelog where Date = "2018-07-02";
  select * from timelog where Date>="2018-07-01" and Date<="2018-07-31";
```

* 日期时间运算

  - 语法格式

    select * from 表名  where 字段名 运算符 (时间-interval 时间间隔单位);

  - 时间间隔单位：  1 day | 2 hour | 1 minute | 2 year | 3 month

```sql
  select * from timelog where shijian > (now()-interval 1 day);
```

### 高级查询语句


#### 模糊查询和正则查询

LIKE用于在where子句中进行模糊查询，SQL LIKE 子句中使用百分号 %来表示任意0个或多个字符，下划线_表示任意一个字符。

使用 LIKE 子句从数据表中读取数据的通用语法：

```sql
SELECT field1, field2,...fieldN 
FROM table_name
WHERE field1 LIKE condition1
```

```sql
e.g. 
mysql> select * from class_1 where name like 'A%';
```

mysql中对正则表达式的支持有限，只支持部分正则元字符

```sql
SELECT field1, field2,...fieldN 
FROM table_name
WHERE field1 REGEXP condition1
```

```sql
e.g. 
select * from class_1 where name regexp 'B.+';
```

#### 排序

ORDER BY 子句来设定你想按哪个字段哪种方式来进行排序，再返回搜索结果。

使用 ORDER BY 子句将查询数据排序后再返回数据：

```sql
SELECT field1, field2,...fieldN from table_name1 where field1
ORDER BY field1 [ASC [DESC]]
```
默认情况ASC表示升序，DESC表示降序

```sql
select * from class_1 where sex='m' order by age;
```

#### 分页

LIMIT 子句用于限制由 SELECT 语句返回的数据数量 或者 UPDATE,DELETE语句的操作数量

带有 LIMIT 子句的 SELECT 语句的基本语法如下：

```sql
SELECT column1, column2, columnN 
FROM table_name
WHERE field
LIMIT [num]
```

#### 联合查询

UNION 操作符用于连接两个以上的 SELECT 语句的结果组合到一个结果集合中。多个 SELECT 语句会删除重复的数据。

UNION 操作符语法格式：

```sql
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions]
UNION [ALL | DISTINCT]
SELECT expression1, expression2, ... expression_n
FROM tables
[WHERE conditions];
```
>expression1, expression2, ... expression_n: 要检索的列。
>tables: 要检索的数据表。
>WHERE conditions: 可选， 检索条件。
>DISTINCT: 可选，删除结果集中重复的数据。默认情况下 UNION 操作符已经删除了重复数据，所以 DISTINCT 修饰符对结果没啥影响。
>ALL: 可选，返回所有结果集，包含重复数据。

```sql
select * from class_1 where sex='m' UNION ALL select * from class_1 where age > 9;
```




### 数据备份

1. 备份命令格式
>mysqldump -u用户名 -p 源库名 > ~/***.sql
>> --all-databases  备份所有库
>> 库名             备份单个库
>> -B 库1 库2 库3   备份多个库
>> 库名 表1 表2 表3 备份指定库的多张表

2. 恢复命令格式
>mysql -uroot -p 目标库名 < ***.sql
>从所有库备份中恢复某一个库(--one-database)
>
>>mysql -uroot -p --one-database 目标库名 < all.sql


## Python操作MySQL数据库

### pymysql安装

>sudo pip3 install pymysql


### pymysql使用流程

1. 建立数据库连接(db = pymysql.connect(...))
2. 创建游标对象(c = db.cursor())
3. 游标方法: c.execute("insert ....")
4. 提交到数据库 : db.commit()
5. 关闭游标对象 ：c.close()
6. 断开数据库连接 ：db.close()

#### 常用函数


>db = pymysql.connect(参数列表)
>>host ：主机地址,本地 localhost
>>port ：端口号,默认3306
>>user ：用户名
>>password ：密码
>>database ：库
>>charset ：编码方式,推荐使用 utf8

> 数据库连接对象(db)的方法
>>db.commit() 提交到数据库执行
>>db.rollback() 回滚
>>cur = db.cursor() 返回游标对象,用于执行具体SQL命令
>>db.close() 关闭连接

>游标对象(cur)的方法
>>cur.execute(sql命令,[列表]) 执行SQL命令
>>cur.close() 关闭游标对象
>>cur.fetchone() 获取查询结果集的第一条数据 (1,100001,"河北省")                  
>>cur.fetchmany(n) 获取n条 ((记录1),(记录2))                 
>>cur.fetchall() 获取所有记录







#mysql配置文件
1、sudo su
2、cd /etc/mysql/mysql.conf.d
3、cp mysqld.cnf mysqld.cnf.bak

#查看系统日志
cd /var/log

vim /var/log/syslog   /log 查找log  n 下一个  N 上一个

cat /var/log/syslog |grep 'MySQL'|more +

#cockie
充值数据  用-=  传复数
sql 注入 ;delete from user;
线上建索引或者改存储引擎


#查看mysql用户
select * from mysql.user \G


#int(xx)显示宽度
xx表示显示宽度,设置属性zerofill,则可以全显示

# MySQL基础回顾

WEB前端 + 后端  + 爬虫 + 数据分析 + 人工智能



## **1、数据库概念**

**数据库**
>并发量
>中国网络访问峰值: 16:00 19:00
- 存储数据的仓库（逻辑概念，并未真实存在）


**数据库软件**

- 真实软件，用来实现数据库这个逻辑概念

**数据仓库**

- 数据量更加庞大，更加侧重数据分析和数据挖掘，供企业决策分析之用，主要是数据查询，修改和删除很少
>数据库的瓶颈: 磁盘 数据格式 带宽

>pass 数仓与数据库的区别?
## **2、MySQL的特点**

- 关系型数据库
- 跨平台
- 支持多种编程语言（python、java、php）
- 基于磁盘存储，数据是以文件形式存放在数据库目录/var/lib/mysql下
>持久化,"落地":指数据被存入磁盘.
## **3、启动连接**

- 服务端启动 

>慎用!
```mysql
sudo /etc/init.d/mysql start|stop|restart|status
sudo service mysql start|stop|restart|status
```

- 客户端连接

```mysql
mysql -hIP地址 -u用户名 -p密码
本地连接可省略 -h 选项
```



## **4、基本SQL命令**

**库管理**

```mysql
    1、查看已有库；
      show databases;

    2、创建库并指定字符集；
      create database 库名 charset utf8;

    3、查看当前所在库；
      select database();

    4、切换库；
      use 库名;

    5、查看库中已有表；
      show tables;

    6、删除库；
      drop database 库名;
```

**表管理**

```mysql
    1、创建表并指定字符集；
      create table 表名(字段名 字段类型 xxx)charset=utf8
    2、查看创建表的语句 (字符集、存储引擎)；
      show create table 表名()
    3、查看表结构;
      desc 表名;
    4、删除表;
      drop table 表名1,表名2,表名3
```

**表记录管理**

```mysql
    1、增 ： insert into 表名(字段名) values(),();
    2、删 ： delete from 表名 where 条件;
    -删之前谨慎,用select检查一下
    -优先考虑伪删除
    3、改 ： update 表名 set 字段名=值,字段名=值 where 条件;
    4、查 ： select 字段名/* from 表名 where
```

**表字段管理（alter table 表名）**

```mysql
    1、增 ： alter table 表名 add 字段名 字段类型 first|after 字段名;
    2、删 ： alter table 表名 drop 字段名;
    -删除有风险
    3、改 ： alter table 表名 modify 字段名 新类型;
    4、表重命名：alter table 表名 rename 新表名;
```



## **5、数据类型**

**四大数据类型**

- 数值类型

####mysql数值位数与存储范围

bigint
从 -2^63 (-9223372036854775808) 到 2^63-1 (9223372036854775807) 的整型数据（所有数字）。存储大小为 8 个字节。
P.S. bigint已经有长度了，在mysql建表中的length，只是用于显示的位数
int
从 -2^31 (-2,147,483,648) 到 2^31 – 1 (2,147,483,647) 的整型数据（所有数字）。存储大小为 4 个字节。int
的 SQL-92 同义字为 integer。
smallint
从 -2^15 (-32,768) 到 2^15 – 1 (32,767) 的整型数据。存储大小为 2 个字节。
tinyint
从 0 到 255 的整型数据。存储大小为 1 字节。
注释
在支持整数值的地方支持 bigint 数据类型。但是，bigint 用于某些特殊的情况，当整数值超过
int 数据类型支持的范围时，就可以采用 bigint。在 SQL Server 中，int 数据类型是主要的整数数据类型。
在数据类型优先次序表中，bigint 位于 smallmoney 和 int 之间。
只有当参数表达式是 bigint 数据类型时，函数才返回 bigint。SQL Server 不会自动将其它整数数据类型（tinyint、smallint 和
int）提升为 bigint。
int(M) 在 integer 数据类型中，M 表示最大显示宽度。在 int(M) 中，M 的值跟 int(M) 所占多少存储空间并无任何关系。和数字位数也无关系 int(3)、int(4)、int(8) 在磁盘上都是占用 4 btyes 的存储空间。



```mysql
一个字节8位, 2字节能存2**16-1 =65535 
 int(4字节) smallint(2字节) bigint(8字节) tinyint[1](1字节)
 float(m,n) double decimal"货币"
```

- 字符类型

```mysql
char(4) xxxx  varchar隐藏字节:  vchar(4) xxx+1 小于255用一个字节表示计算当前长度占位
              vchar(400) 400+2 大于255用两个
              
char与vchar的区别:char(4)'xxx '一定申请四个,用空格补位,查询的时候删除空格,所以不能存末尾带空格的
              #优化  char(4)由3变4,大量update成本低    vchar(4)存储长度由3变4,update效率慢些
text"大文本,本身无长度限制" blob"复杂结构数据(列表,字典等)" 
pass char与varchar区别
选用:
```

- 枚举类型 

```mysql
enum(单选) set(多选)
>坑多,少用
```

- 
  日期时间类型

```mysql
date time year datetime timestamp
```

**日期时间函数** 

```mysql
NOW() CURDATE() YEAR(字段名) DATE(字段名) TIME(字段名)
```

**日期时间运算**

```mysql
select * from 表名 where 字段名 运算符(NOW()-interval 间隔);
间隔单位: 1 day | 3 month | 2 year
eg1:查询1年以前的用户充值信息
  select * from user where time < (NOW() - interval 1 year)
```

## 6、MySQL运算符

- **数值比较**

```mysql
> >= < <= = !=
eg1 : 查询成绩不及格的学生
      select * from student where score < 60;
eg2 : 删除成绩不及格的学生
      delete * from student where score < 60;      
eg3 : 把id为3的学生的姓名改为 周芷若
      update student set name='周芷若' where id = 3;
      
```

- **逻辑比较** 

```mysql
and  or
eg1 : 查询成绩不及格的男生
  select * from student where sex = "m" and socre < 60;
eg2 : 查询成绩在60-70之间的学生
  select * from student where score >= 60 and score <= 70;
  
```



- **范围内比较** 

```mysql
between 值1 and 值2 、in() 、not in()
eg1 : 查询不及格的学生姓名及成绩
  select name,score from student where socre between 0 and 59;
eg2 : 查询AID1905和AID1903班的学生姓名及成绩
  select name,score from where class in ("AID1905","AID1903");
  
```

- **模糊比较（like）**

```mysql
where 字段名 like 表达式(%_)  % 单个 _多个
eg1 : 查询北京的姓赵的学生信息
  select * from student where address = "北京" and name like "赵%";
```



- **NULL判断**

```mysql
is NULL 、is not NULL
eg1 : 查询姓名字段值为NULL的学生信息
  select * from ? where name is null;
```



## 7、查询

- **order by**

给查询的结果进行排序(永远放在SQL命令的倒数第二的位置写)

```mysql
order by 字段名 ASC/DESC
eg1 : 查询成绩从高到低排列
  select * from students order by score desc
```

- **limit**

限制显示查询记录的条数（永远放在SQL命令的最后写）

```mysql
limit n ：显示前n条
limit m,n ：从第(m+1)条记录开始，显示n条
分页：每页显示10条，显示第6页的内容
     limit (m-1)*n,n
     limit 50,10
```

******************************************************************************************
# MySQL高级-Day01

## **MySQL基础巩固**

- **创建库 ：country（指定字符编码为utf8）**
  create database country
- **创建表 ：sanguo 字段：id 、name、attack、defense、gender、country**
                   **要求 ：id设置为主键,并设置自增长属性**
               
               ​                **id int primary key auto_increment,**
               
- **插入5条表记录（id 1-5,name-诸葛亮、司马懿、貂蝉、张飞、赵云），攻击>100,防御<100）**
insert into sanguo values(5,"张飞",350,310,"m","蜀");
- **查找所有蜀国人的信息**

     ```mysql
      select * from sanguo  where country = "蜀" order by attack desc;
     ```

mysql> select * from sanguo where country = "蜀" \G;

     ```

- **将赵云的攻击力设置为360,防御力设置为68**

     ```mysql
     update sanguo set attack = 360,defense=68 where name ="赵云"
     ```

- **将吴国英雄中攻击值为xx的英雄的攻击值改为100,防御力改为60**

     ```mysql
     update sanguo set attack = 100,defense=60 where attack = 250 and country = "吴"
     ```

- **找出攻击值高于200的蜀国英雄的名字、攻击力**

     ```mysql
      select name,attack from sanguo where country = "蜀" and attack > 200;
     ```

- **将蜀国英雄按攻击值从高到低排序**

     ```mysql
     select * from sanguo  where country = "蜀" order by attack desc;
     ```

- **魏蜀两国英雄中名字为三个字的按防御值升序排列**

     ```mysql
    select * from sanguo where country in ("魏","蜀") and name like "___" order by defense asc;
    ```


     ```

- **在蜀国英雄中,查找攻击值前3名且名字不为 NULL 的英雄的姓名、攻击值和国家**

     ```mysql
     select name,attack,country from sanguo where name is not null and country="蜀" order by attack desc limit 3;
     ```

## MySQL普通查询

```mysql
    3、select ...聚合函数 from 表名
    1、where ...
    2、group by ...
    4、having ...
    5、order by ...
    6、limit ...;
```

- **聚合函数**

| 方法          | 功能                 |
| ------------- | -------------------- |
| avg(字段名)   | 该字段的平均值       |
| max(字段名)   | 该字段的最大值       |
| min(字段名)   | 该字段的最小值       |
| sum(字段名)   | 该字段所有记录的和   |
| count(字段名) | 统计该字段记录的个数 |
|               |                      |

eg1 : 找出表中的最大攻击力的值？
 select max(attack) from sanguo
```mysql
 
+-------------+
| max(attack) |
+-------------+
|         350 |
+-------------+


```

eg2 : 表中共有多少个英雄？

```mysql
  select count(id) as hero_count from sanguo
  count(空值)会被跳过,所以count(id)是最稳妥的
```

eg3 : 蜀国英雄中攻击值大于200的英雄的数量

```mysql
select count(id) as number from sanguo where attack > 200;
```

- **group by**

给查询的结果进行分组
eg1 : 计算每个国家的平均攻击力

```mysql
select country, avg(attack) from sanguo group by country;
--错误的--select id, avg(attack) from sanguo group by country;
```


eg2 : 所有国家的男英雄中 英雄数量最多的前2名的 国家名称及英雄数量

```mysql
select country, count(id) as number from sanguo where gender="m" group by country order by number desc limit 2
```

​	==group by后字段名与为select后的字段必须来自同一张表==
​	==查询字段和group by后字段不一致,则必须对该字段进行聚合处理(聚合函数)==
select id, avg(attack) from sanguo group by country;
- **having语句**
>分组,聚合,筛选 铁三角

对分组聚合后的结果进行进一步筛选

```mysql
eg1 : 找出平均攻击力大于105的国家的前2名,显示国家名称和平均攻击力

mysql> select country, avg(attack) from sanguo group by country 
having avg(attack)>105 
order by avg(attack) desc
limit 2 ;

>注意having和where的区别,where筛选的是分组前的数据,having筛选的是group by 后的数据
```

注意

```mysql
having语句通常与group by联合使用
having语句存在弥补了where关键字不能与聚合函数联合使用的不足,where只能操作表中实际存在的字段,having操作的是聚合函数生成的显示列
```

- **distinct语句**

不显示字段重复值

```mysql
eg1 : 表中都有哪些国家
  select distinct country from sanguo
+---------+
| country |
+---------+
| 蜀      |
| 魏      |
| 吴      |
+---------+
distinct后的字段不能聚合,distinct本身能聚合

eg2 : 计算一共有多少个国家
  select count(distinct country) from sanguo
+-------------------------+
| count(distinct country) |
+-------------------------+
|                       3 |
+-------------------------+

```


注意

```mysql
distinct和from之间所有字段都相同才会去重
distinct不能对任何字段做聚合处理
```

- **查询表记录时做数学运算**

运算符 ： +  -  *  /  %  **

```mysql
eg1: 查询时显示攻击力翻倍
    select name,attack*2 from sanguo
+-----------+----------+
| name      | attack*2 |
+-----------+----------+
| 诸葛亮    |      500 |
| 赵云      |      700 |
| 司马懿    |      300 |
| 貂蝉      |      200 |
| 张飞      |      700 |
+-----------+----------+

eg2: 更新蜀国所有英雄攻击力 * 2
    update sanguo set attack = attack * 2 where country = "蜀国"
```
价值:若从数据库取出数据处理后再存入库,在高并发的访问下,数据的累加会出差错(例如很多人同时点赞)
所以以这种方式进行处理可以保证"点赞数"的准确性



#索引小记
>moogoDB 纯B树
  范围查询时,永远走中序遍历,例如找4-11,要按顺序遍历4,5,6,7,8,9,10,11


mysql B+树
父节点是下一个子节点的最小值
非叶子节点只有索引指针无数据[树宽度降低]
叶子节点上的数据是排好序的,是相互排序的,链表结构的[范围查找效率高]

小结
  选择B+树优点:
    所以范围查找的效率高
    树的层数也可以变矮,数变胖,减少磁盘的IO次数
  反之,相同数据体量上,B树要比B+树高,意味着更多的IO次数


## 索引概述

- **定义**

对数据库表的一列或多列的值进行排序的一种结构(Btree方式)

- **优点**

加快数据检索速度

- **缺点**

```mysql
占用物理存储空间(/var/lib/mysql)
当对表中数据更新时,索引需要动态维护,降低数据维护速度
```

- **索引示例**

```mysql
# cursor.executemany(SQL,[data1,data2,data3])
# 以此IO执行多条表记录操作，效率高，节省资源
1、开启运行时间检测
  mysql>show vayeriables like '%pro%';
  mysql>set proyefiling=1;
2、执行查询语句ye(无索引)
  select name fyerom students where name='Tom99999';
3、查看执行时间ye
  show profilesye;
4、在name字段创ye建索引
  create index name on students(name);
5、再执行查询语句
  select name from students where name='Tom88888';
6、查看执行时间
  show profiles;
```
#优化,开完记得关

## 索引分类

#### 普通(MUL)  and 唯一(UNI)

- **使用规则**

```mysql
1、可设置多个字段
2、普通索引 ：字段值无约束,KEY标志为 MUL
3、唯一索引(unique) ：字段值不允许重复,但可为 NULL,null不算唯一的
                    KEY标志为 UNI
4、哪些字段创建索引:经常用来查询的字段、where条件判断字段、order by排序字段
```

- **创建普通索引and唯一索引**

创建表时

```mysql
create table 表名(
字段名 数据类型，
字段名 数据类型，
index(字段名),
index(字段名),
unique(字段名)
);
```

已有表中创建

```mysql
create [unique] index 索引名 on 表名(字段名);
```
tip:在线上建立索引是有风险的,会占用较长时间的IO

- **查看索引**

```mysql
1、desc 表名;  --> KEY标志为：MUL 、UNI
2、show index from 表名\G;
```

- **删除索引**

```mysql
drop index 索引名 on 表名;
```

#### **主键(PRI)and自增长(auto_increment)**

- **使用规则**

```mysql
1、只能有一个主键字段
2、所带约束 ：不允许重复,且不能为NULL
3、KEY标志(primary) ：PRI
4、通常设置记录编号字段id,能唯一锁定一条记录
```

- **创建**

创建表添加主键

```mysql
create table student(
id int auto_increment,
name varchar(20),
primary key(id)
)charset=utf8,auto_increment=10000;##设置自增长起始值
```

已有表添加主键

```mysql
alter table 表名 add primary key(id);
```

已有表操作自增长属性	

```mysql
1、已有表添加自增长属性
  alter table 表名 modify id int auto_increment;
2、已有表重新指定起始值：
  alter table 表名 auto_increment=20000;
```

- **删除**

```mysql
1、删除自增长属性(modify)
  alter table 表名 modify id int;
2、删除主键索引
  alter table 表名 drop primary key;
```



------

## 今日作业

- **1、把今天所有的课堂练习重新做一遍**

- **2、面试题**

有一张文章评论表comment如下

| **comment_id** | **article_id** | **user_id** | **date**            |
| -------------- | -------------- | ----------- | ------------------- |
| 1              | 10000          | 10000       | 2018-01-30 09:00:00 |
| 2              | 10001          | 10001       | ... ...             |
| 3              | 10002          | 10000       | ... ...             |
| 4              | 10003          | 10015       | ... ...             |
| 5              | 10004          | 10006       | ... ...             |
| 6              | 10025          | 10006       | ... ...             |
| 7              | 10009          | 10000       | ... ...             |

以上是一个应用的comment表格的一部分，请使用SQL语句找出在本站发表的所有评论数量最多的10位用户及评论数，并按评论数从高到低排序

    select user_id,count(user_id) as count from comment group by user_id order by count desc limit 10

备注：comment_id为评论id

​            article_id为被评论文章的id

​            user_id 指用户id

- **3、操作题**

综述：两张表，一张顾客信息表customers，一张订单表orders

表1：顾客信息表，完成后插入3条表记录

```mysql
c_id 类型为整型，设置为主键，并设置为自增长属性
c_name 字符类型，变长，宽度为20
c_age 微小整型，取值范围为0~255(无符号)
c_sex 枚举类型，要求只能在('M','F')中选择一个值
c_city 字符类型，变长，宽度为20
c_salary 浮点类型，要求整数部分最大为10位，小数部分为2位
```
源代码:
use homework
create table customers(
  c_id int primary key auto_increment,
  c_name varchar(20),
  c_age tinyint,
  c_sex enum("M","F"),
  c_city varchar(20),
  c_salary float(12,2)
);

insert into customers values(1,"alicinya",18,"M","chengdu",998);
 insert into customers values(2,"alice",18,"F","chengdu",998);
insert into customers values(3,"chocola meilleur",18,"F","chengdu",998)



表2：顾客订单表（在表中插入5条记录）

```mysql
o_id 整型
o_name 字符类型，变长，宽度为30
o_price 浮点类型，整数最大为10位，小数部分为2位
设置此表中的o_id字段为customers表中c_id字段的外键,更新删除同步
insert into orders values(1,"iphone",5288),(1,"ipad",3299),(3,"mate9",3688),(2,"iwatch",2222),(2,"r11",4400);
```
create table orders(
  o_id int,
  o_name varchar(30),
  o_price float(12,2),
  foreign key(o_id)
  references customers(c_id)
  on delete cascade
)

foreign key(参考字段名)
  references 主表(被参考字段名)
  on delete 级联动作
  on update 级联动作


增删改查题

```mysql
1、返回customers表中，工资大于4000元，或者年龄小于29岁，满足这样条件的前2条记录
2、把customers表中，年龄大于等于25岁，并且地址是北京或者上海，这样的人的工资上调15%
3、把customers表中，城市为北京的顾客，按照工资降序排列，并且只返回结果中的第一条记录
4、选择工资c_salary最少的顾客的信息
5、找到工资大于5000的顾客都买过哪些产品的记录明细			
6、删除外键限制			
7、删除customers主键限制
8、增加customers主键限制c_id
```


# MySQL高级-Day01回顾

- **SQL查询总结**

```mysql
    3、select ...聚合函数 from 表名
    1、where ...
    2、group by ...
    4、having ...
    5、order by ...
    6、limit ...;
```

- **聚合函数（铁三角之一）**

avg(...) sum(...) max(...) min(...) 
count(字段名)  # 空值NULL不会被统计

- **group by（铁三角之二）**

给查询结果进行分组
如果select之后的字段名和group by之后的字段不一致,则必须对该字段进行聚合处理(聚合函数)

- **having语句（铁三角之三）**

对查询的结果进行进一步筛选
**注意**
1、having语句通常和group by语句联合使用,过滤由group by语句返回的记录集
2、where只能操作表中实际存在字段,having可操作由聚合函数生成的显示列

- **distinct** 

select distinct 字段1,字段2 from 表名;

- **查询时做数学运算**

select 字段1*2,字段2+5 from 表名;

update 表名 set attack=attack*2 where 条件;

- **索引(BTree)**

优点 ：加快数据检索速度
缺点 ：占用物理存储空间,需动态维护,占用系统资源
SQL命令运行时间监测

​		mysql>show variables like '%pro%';

​		1、开启 ：mysql> set profiling=1;
​		2、查看 ：mysql> show profiles;
​		3、关闭 ：mysql> set profiling=0;

- **普通(MUL)、唯一(UNI,字段值不能重复,可为NULL)**

  **创建**
  		index(字段名),index(字段名)
  		unique(字段名),unique(字段名)
  		create [unique] index 索引名 on 表名(字段名);

  **查看**
  		desc 表名;
  		show index from 表名\G;  
  			Non_Unique:1 :index
  			Non_Unique:0 :unique

  **删除**
  		drop index 索引名 on 表名; (只能一个一个删)

# MySQL高级-Day02笔记

## **外键（foreign key）**

- **定义**

  让当前表字段的值在另一个表的范围内选择

  >有外键,肯定是指两张表

- **语法**

  ```mysql
  foreign key(参考字段名)
  references 主表(被参考字段名)
  on delete 级联动作
  on update 级联动作
       
  ```

- **使用规则**

1、主表、从表字段数据类型要一致
2、主表被参考字段 ：KEY的一种，一般为主键    

- **示例**

表1、缴费信息表(财务)

```mysql
id   姓名     班级     缴费金额
1   唐伯虎   AID1903     300
2   点秋香   AID1903     300
3   祝枝山   AID1903     300

```
------建表
create database db02 charset utf8
create table master(
  id int primary key,
  name varchar(20),
  class varchar(20),
  money decimal(6,2)
  );

-----插入数据
insert into master values(
  null,"唐伯虎","AID1903",300),
  (null,"点秋香","AID1903",300),
  (null,"祝枝山","AID1903",300)

注:auto_increment属性,删id=4后,仍然是下个id=5;
+----+-----------+---------+--------+
| id | name      | class   | money  |
+----+-----------+---------+--------+
|  1 | 唐伯虎    | AID1903 | 300.00 |
|  2 | 点秋香    | AID1903 | 300.00 |
|  3 | 祝枝山    | AID1903 | 300.00 |
|  5 | 唐伯虎    | AID1903 | 300.00 |
+----+-----------+---------+--------+



表2、学生信息表(班主任) -- 做外键关联

```mysql
stu_id   姓名   缴费金额
  1     唐伯虎    300
  2     点秋香    300

  4      XXX     XXX  假如此处插入了一个stu_id ,而主表没有这个id,那么此条数据插入不进去
```
create table slaver(
  stu_id int ,
  姓名 varchar(20),
  缴费金额 decimal(6,2)
  ,foreign key(stu_id) references master(id)
  on delete cascade on update cascade)

insert into slaver values(
  1,"唐伯虎",300),
  (2,"点秋香",300)



foreign key(参考字段名) references 主表(被参考字段名)
  on delete cascade on update cascade




- **删除外键**

```mysql
alter table 表名 drop foreign key 外键名;
​外键名 ：show create table 表名;
```

- **级联动作**

```mysql
cascade   "跪舔型"
​数据级联删除、更新(参考字段)
restrict(默认)  "真男人型"
​从表有相关联记录,不允许主表操作
set null    "认怂型"
​主表删除、更新,从表相关联记录字段值为NULL
```
> 建立新表slave_2
create table slave_2(
  stu_id int,
  name varchar(20),
  foreign key(stu_id) references master(id)

)charset=utf8

>insert into slave_2 values(
  10,"点秋香"
)
- **已有表添加外键**

```mysql
alter table 表名 add foreign key(参考字段) references 主表(被参考字段) on delete 级联动作 on update 级联动作
```



## 嵌套查询(子查询)

定义

把内层的查询结果作为外层的查询条件

语法格式

```mysql
select ... from 表名 where 条件(select ....);
```

示例

```mysql
1、把攻击值小于平均攻击值的英雄名字和攻击值显示出来
  select name,attack from sanguo where attack <( select avg(attack) from sanguo ) ;


2、找出每个国家攻击力最高的英雄的名字和攻击值(子查询)
  select name,attack from sanguo where country,attack in (select country,max(attack) from sanguo group by county) ;

 
```



## **多表查询**

**sql脚本资料：join_query.sql**

```mysql
mysql -uroot -p123456
mysql>source /home/tarena/join_query.sql
```

```mysql
create database if not exists db1 character set utf8;
use db1;

create table if not exists province(
id int primary key auto_increment,
pid int,
pname varchar(15)
)default charset=utf8;

insert into province values
(1, 130000, '河北省'),
(2, 140000, '陕西省'),
(3, 150000, '四川省'),
(4, 160000, '广东省'),
(5, 170000, '山东省'),
(6, 180000, '湖北省'),
(7, 190000, '河南省'),
(8, 200000, '海南省'),
(9, 200001, '云南省'),
(10,200002,'山西省');

create table if not exists city(
id int primary key auto_increment,
cid int,
cname varchar(15),
cp_id int
)default charset=utf8;

insert into city values
(1, 131100, '石家庄市', 130000),
(2, 131101, '沧州市', 130000),
(3, 131102, '廊坊市', 130000),
(4, 131103, '西安市', 140000),
(5, 131104, '成都市', 150000),
(6, 131105, '重庆市', 150000),
(7, 131106, '广州市', 160000),
(8, 131107, '济南市', 170000),
(9, 131108, '武汉市', 180000),
(10,131109, '郑州市', 190000),
(11,131110, '北京市', 320000),
(12,131111, '天津市', 320000),
(13,131112, '上海市', 320000),
(14,131113, '哈尔滨', 320001),
(15,131114, '雄安新区', 320002);

create table if not exists county(
id int primary key auto_increment,
coid int,
coname varchar(15),
copid int
)default charset=utf8;

insert into county values
(1, 132100, '正定县', 131100),
(2, 132102, '浦东新区', 131112),
(3, 132103, '武昌区', 131108),
(4, 132104, '哈哈', 131115),
(5, 132105, '安新县', 131114),
(6, 132106, '容城县', 131114),
(7, 132107, '雄县', 131114),
(8, 132108, '嘎嘎', 131115);
```

- **笛卡尔积**

```mysql
select 字段名列表 from 表名列表; 
```
create table tt1(
  tt1name varchar(20)
)

create table tt2(
  tt2name varchar(20)
)

insert into tt1 values("A1"),("A2"),("A3")

insert into tt2 values("B1"),("B2")
mysql> select * from tt1;
+---------+
| tt1name |
+---------+
| A1      |
| A2      |
| A3      |
+---------+
3 rows in set (0.00 sec)

mysql> select * from tt2;
+---------+
| tt2name |
+---------+
| B1      |
| B2      |
+---------+
3 rows in set (0.00 sec)

mysql> select * from tt1,tt2;
+---------+---------+
| tt1name | tt2name |
+---------+---------+
| A1      | B1      |
| A1      | B2      |
| A2      | B1      |
| A2      | B2      |
| A3      | B1      |
| A3      | B2      |
+---------+---------+
6 rows in set (0.00 sec)


select province.pname,city.name from province,city where province.pid = city.cp_id


select province.pname,city.cname,county.coname from province,city,county where province.pid = city.cp_id and city.cid = county.copid
+-----------+--------------+-----------+
| pname     | cname        | coname    |
+-----------+--------------+-----------+
| 河北省    | 石家庄市     | 正定县       |
| 湖北省    | 武汉市       | 武昌区       |
+-----------+--------------+-----------+





- **多表查询**

```mysql
select 字段名列表 from 表名列表 where 条件;
```

- **示例**

```mysql
1、显示省和市的详细信息
   河北省  石家庄市
   河北省  廊坊市
   湖北省  武汉市
   
2、显示 省 市 县 详细信息
  
```



## 连接查询

- **内连接（结果同多表查询，显示匹配到的记录）**

````mysql
select 字段名 from  表1 inner join 表2 on 条件 inner join 表3 on 条件;
eg1 : 显示省市详细信息
  select province.pname,city.cname from province inner join city on province.pid = city.cp_id 



eg2 : 显示 省 市 县 详细信息
  select province.pname,city.cname,county.coname from province inner join city on province.pid = city.cp_id inner join county on city.cid = county.copid

````

- **左外连接**

以 左表 为主显示查询结果

```mysql
select 字段名 from 表1 left join 表2 on 条件 left join 表3 on 条件;
eg1 : 显示 省 市 详细信息（要求省全部显示）
 select province.pname,city.cname from province left join city on province.pid = city.cp_id 

select province.pname,city.cname,county.coname from province left join city on province.pid = city.cp_id left join county on city.cid = county.copid



```

- **右外连接**

用法同左连接,以右表为主显示查询结果

```mysql
select 字段名 from 表1 right join 表2 on 条件 right join 表3 on 条件;
select province.pname,city.cname,county.coname from province right join city on province.pid = city.cp_id right join county on city.cid = county.copid
```

## **数据导入**

==掌握大体步骤==

==source 文件名.sql==

**作用**

把文件系统的内容导入到数据库中
**语法（方式一）**

load data infile "文件名"
into table 表名
fields terminated by "分隔符"
lines terminated by "\n"
**示例**
scoretable.csv文件导入到数据库db2的表

```mysql
1、将scoretable.csv放到数据库搜索路径中
   mysql>show variables like 'secure_file_priv';
         /var/lib/mysql-files/
   Linux: sudo cp /home/tarena/scoreTable.csv /var/lib/mysql-files/
2、在数据库中创建对应的表
  create table scoretab(
  rank int,
  name varchar(20),
  score float(5,2),
  phone char(11),
  class char(7)
  )charset=utf8;
3、执行数据导入语句
load data infile '/var/lib/mysql-files/scoreTable.csv'
into table scoretab
fields terminated by ','   分隔符需要严格控制,不然列数对不齐会报错
lines terminated by '\n'
4、练习
  添加id字段,要求主键自增长,显示宽度为3,位数不够用0填充
  alter table scoretab add id int(3) zerofill primary key auto_increment first;
```

**语法（方式二）**

source 文件名.sql

## **数据导出**

**作用**

将数据库中表的记录保存到系统文件里

**语法格式**

select ... from 表名
into outfile "文件名"
fields terminated by "分隔符"
lines terminated by "分隔符";

**练习**

```mysql
1、把sanguo表中英雄的姓名、攻击值和国家三个字段导出来,放到 sanguo.csv中
 select name,attack,country from sanguo 
 into outfile "/var/lib/mysql-files/scoreTable2222.csv" 
 fields terminated by ","
 lines terminated by "\n";

2、将mysql库下的user表中的 user、host两个字段的值导出到 user2.txt，将其存放在数据库目录下
 
```
查找文件权限
ll |grep "sc" 

更改文件权限为可读可写
/home/tarena# chmod 666 scoreTable.csv


**注意**

```
1、导出的内容由SQL查询语句决定
2、执行导出命令时路径必须指定在对应的数据库目录下
```

## **表的复制**

==1、表能根据实际需求复制数据==

==2、复制表时不会把KEY属性复制过来==

**语法**

```mysql
create table 表名 select 查询命令;
```

**练习**

```mysql
1、复制sanguo表的全部记录和字段,sanguo2
create table sanguo2 select * from sanguo

2、复制sanguo表的 id,name,country 三个字段的前3条记录,sanguo4
  
```

**注意**

复制表的时候不会把原有表的 KEY 属性复制过来

**复制表结构**
create table 表名 select 查询命令 where false;

## **锁（自动加锁和释放锁）**

==全程重点，理论和锁分类及特点==

**目的**

解决客户端并发访问的冲突问题

**锁类型分类**

```
读锁(共享锁)：select 加读锁之后别人不能更改表记录,但可以进行查询
写锁(互斥锁、排他锁)：加写锁之后别人不能查、不能改
```

**锁粒度分类**

表级锁 ：myisam   粒度大
行级锁 ：innodb   粒度小

# 今日作业

1、把 /etc/passwd 文件的内容导grant all privileges on *.* to 'work'@'%' identified by '123' with grant option;入到数据库的表中
 load data infile '/var/lib/mysql-files/passwd' into table hwork fields terminated by '' lines terminated by '\n'
    -> ;


```
tarena:x:1000:1000:tarena,,,:/home/tarena:/bin/bash
```

2、Day01的md文件中的外键及查询作业题




#day03
# **MySQL-Day02必须掌握**

## **外键**

**原理** 

```
让当前表字段的值在另一张表的范围内去选择
```

**使用规则**

```mysql
1、数据类型要一致
2、主表被参考字段必须为KEY的一种 : PRI
```

**级联动作**

```mysql
1、cascade : 删除 更新同步(被参考字段)
2、restrict(默认) : 不让主表删除 更新
3、set null : 删除 更新,从表该字段值设置为NULL
```

## **嵌套查询（子查询）**

**定义**

```
把内层的查询结果作为外层查询的条件
```

## **多表查询**

**笛卡尔积**

```
多表查询不加where条件,一张表的每条记录分别和另一张表的所有记录分别匹配一遍
```

## **连接查询**

**分类**

```mysql
1、内连接（表1 inner join 表2 on 条件）
2、外连接（表1 left|right join 表2 on 条件）
	1、左连接 ：以左表为主显示查询结果
	2、右连接 ：以右表为主显示查询结果
```

**语法**

```mysql
select 表名.字段名 from 表1 inner join 表2 on 条件；
```

## **锁**

**1、目的** ：解决客户端并发访问的冲突问题

**2、锁分类**

```mysql
1、锁类型 : 读锁 写锁
2、锁粒度 : 行级锁(InnoDB) 表级锁(MyISAM)
```

## **数据导入**

**方式一（使用source命令）**

```mysql
mysql> source /home/tarena/xxx.sql
```

**方式二（使用load命令）**

```mysql
1、将导入文件拷贝到数据库搜索路径中
   show variables like 'secure%';
2、在数据库中创建对应的表
3、执行数据导入语句
```

## **索引**

**定义**

```
对数据库表中一列或多列的值进行排序的一种结构(BTree)
```

**优点**

```mysql
加快数据的检索速度
```

**缺点**

```mysql
1、占用实际物理存储空间
2、索引需动态维护，消耗资源，降低数据的维护速度
```

**分类及约束**

```mysql
1、普通索引（MUL）: 无约束
2、唯一索引（UNI）：字段值不允许重复，但可为NULL
3、主键（PRI）	：字段值不允许重复，不可为NULL
4、外键		 ：让当前表字段的值在另一张表的范围内选择
```

# **MySQL-Day03笔记**

## **存储引擎**

**定义**

```mysql
处理表的处理器
```

**基本操作**

```mysql
1、查看所有存储引擎
   mysql> show engines;
2、查看已有表的存储引擎
   mysql> show create table 表名;
3、创建表指定
   create table 表名(...)engine=MyISAM,charset=utf8,auto_increment=10000;
4、已有表指定
   alter table 表名 engine=InnoDB;
```

mysql> show engines \G;
*************************** 1. row ***************************
      Engine: InnoDB
     Support: DEFAULT
     Comment: Supports transactions, row-level locking, and foreign keys
Transactions: YES
          XA: YES
  Savepoints: YES
*************************** 2. row ***************************
      Engine: MRG_MYISAM
     Support: YES
     Comment: Collection of identical MyISAM tables
Transactions: NO
          XA: NO
  Savepoints: NO


  create table test_myisam(id int)engine = MyISAM,charset = utf8
*************************** 3. row ***************************
      Engine: MEMORY
     Support: YES
     Comment: Hash based, stored in memory, useful for temporary tables
Transactions: NO
          XA: NO
  Savepoints: NO
  内存型   IO快  查找快


  use db02
  create table mem_test (id int)engine = MEMORY charset utf8
  insert into mem_test values(1),(2)

*************************** 4. row ***************************
      Engine: BLACKHOLE
     Support: YES
     Comment: /dev/null storage engine (anything you write to it disappears)
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 5. row ***************************
      Engine: MyISAM
     Support: YES
     Comment: MyISAM storage engine
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 6. row ***************************
      Engine: CSV
     Support: YES
     Comment: CSV storage engine
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 7. row ***************************
      Engine: ARCHIVE
     Support: YES
     Comment: Archive storage engine
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 8. row ***************************
      Engine: PERFORMANCE_SCHEMA
     Support: YES
     Comment: Performance Schema
Transactions: NO
          XA: NO
  Savepoints: NO
*************************** 9. row ***************************
      Engine: FEDERATED
     Support: NO
     Comment: Federated MySQL storage engine
Transactions: NULL
          XA: NULL
  Savepoints: NULL
9 rows in set (0.00 sec)



**==常用存储引擎及特点==**

- InnoDB		

```mysql
1、支持行级锁
2、支持外键、事务、事务回滚
3、表字段和索引同存储在一个文件中    此为聚集索引
   1、表名.frm ：表结构
   2、表名.ibd : 表记录及索引文件
```

- MyISAM

```mysql
1、支持表级锁
2、表字段和索引分开存储  非聚集索引,此B+树有些不同,叶子节点不存数据,只存指针
   1、表名.frm ：表结构
   2、表名.MYI : 索引文件(my index)
   3、表名.MYD : 表记录(my data)


```

- MEMORY

```mysql
1、表记录存储在内存中，效率高
2、服务或主机重启，表记录清除

例如一些可丢失的配置参数
```

**如何选择存储引擎**

```mysql
1、执行查操作多的表用 MyISAM(使用InnoDB浪费资源)
2、执行写操作多的表用 InnoDB 64
3、临时表 ： MEMORY
```

## **MySQL的用户账户管理**

**开启MySQL远程连接**

##查看编码配置信息

 show variables like"%chara%"

## vi 基础操作
命令行模式
从命令行切换到编辑模式，i、a、o

i 为从目前光标所在处输入， I 为在目前所在行的第一个非空格符处开始输入。 

a 为从目前光标所在的下一个字符处开始输入， A 为从光标所在行的最后一个字符处开始输入。

o英文字母 。o 为在目前光标所在的下一行处输入新的一行； O 为在目前光标所在处的上一行输入新的一行。

 

dd   删除游标所在的那一整行

ndd    n 为数字。删除光标所在的向下 n 行，例如 20dd 则是删除 20 行 

d1G  删除光标所在到第一行的所有数据

dG    删除光标所在到最后一行的所有数据

yy     复制游标所在的那一行

nyy   n 为数字。复制光标所在的向下 n 行，例如 20yy 则是复制 20 行

p      为将已复制的数据在光标下一行贴上

u      复原前一个动作，相当于撤销。

Ctrl+r    重复做上一个动作。

Shift+g  输入行号（120），按Shift+g，跳转到指定行（跳到120行）

gg           跳到文本首行

shift + g  跳到文本最后一行          

Shift+4   跳到光标所在的行尾

Shift+6   跳到光标所在的行首

Shift+D   删除当前行

 

输入模式
字符按键以及Shift组合，输入字符
ENTER，回车键，换行
BACK SPACE，退格键，删除光标前一个字符
DEL，删除键，删除光标后一个字符
方向键，在文本中移动光标
HOME/END，移动光标到行首/行尾
Page Up/Page Down，上/下翻页
Insert，切换光标为输入/替换模式，光标将变成竖线/下划线
ESC，退出输入模式，切换到命令模式


底线命令模式
按Esc键，再输入"："冒号，进入底线命令模式。

:wq  保存文件并退出

:wq!  强制保存退出

:q!     强制退出

:w     保存文件

:set nu   显示行号

:set nonu   为取消行号

:w [filename]   将编辑的数据储存成另一个文件（类似另存新档）

/name   向光标之下寻找一个名称为 name的字符串

?name  向光标之上寻找一个字符串名称为 name 的字符串。

	:n1,n2s/word1/word2/g   n1 与 n2 为数字。在第 n1 与 n2 行之间寻找 word1 这个字符串，并用word2替代word1 。
	
	:1,$s/word1/word2/g       从第一行到最后一行寻找 word1 字符串，并用word2替代word1 。
	
	:1,$s/word1/word2/gc     从第一行到最后一行寻找 word1 字符串，并用word2替代word1 。且在取代前显示提示字符给用户确认 (confirm) 是否需要取代。
---------------------
















'HJKL'方向键
:set number 添	加行号
"o"从光标当前行 换行 并进入插入模式
"3dd"删除指定行数的内容,3->制定行数
"u"撤销

```mysql
更改配置文件，重启服务！
1、sudo su
2、cd /etc/mysql/mysql.conf.d
3、cp mysqld.cnf mysqld.cnf.bak
4、vi mysqld.cnf #找到44行左右,加 # 注释
   #bind-address = 127.0.0.1


   [mysqld]
   character_set_server = utf8
5、保存退出
6、service mysql restart

vi使用 : 按a ->编辑文件 ->ESC ->shift+,64Mad 与 128MB
```
内存交换
**添加授权用户**

```mysql
1、用root用户登录mysql   
   mysql -uroot -p123456
2、授权
   grant 权限列表 on 库.表 to "用户名"@"%" identified by "密码" with grant option;
3、刷新权限
   flush privileges;
```

**权限列表**

```
all privileges 、select 、insert ... ... 
库.表 ： *.* 代表所有库的所有表
```

**示例**

```mysql
1、添加授权用户work,密码123,对所有库的所有表有所有权限
  mysql>grant all privileges on *.* to 'work'@'%' identified by '123' with grant option;
  mysql>flush privileges;
2、添加用户duty,对db2库中所有表有所有权限
```





## **==事务和事务回滚==**

**事务定义**

```mysql
 一件事从开始发生到结束的过程
```

**作用**

```mysql
确保数据的一致性、准确性、有效性
```

**事务操作**

```mysql
1、开启事务
   mysql>begin; # 方法1
   mysql>start transaction; # 方法2
2、开始执行事务中的1条或者n条SQL命令
3、终止事务
   mysql>commit; # 事务中SQL命令都执行成功,提交到数据库,结束!
   mysql>rollback; # 有SQL命令执行失败,回滚到初始状态,结束!
```

####事物举例:
```mysql
create tabele bank(
  name varchar(20),
  money decimal(20,2)
) 

insert into  bank values("vip1",20000),("vip2",2000)

select * from bank

begin

update bank set money = money -3000 where name = "vip1";
>此时新建一个终端 登录另外的账号 检查该表 可以发现数值未改变

update bank set money = money +3000 where name = "vip2";

commit
commit 后事物结束,数据改动生效
```



**==事务四大特性（ACID）==**

- **1、原子性（atomicity）**

```
一个事务必须视为一个不可分割的最小工作单元，整个事务中的所有操作要么全部提交成功，要么全部失败回滚，对于一个事务来说，不可能只执行其中的一部分操作
```
>注重结果


- **2、一致性（consistency）**

```
数据库总是从一个一致性的状态转换到另一个一致性的状态
```
>初始状态 操作状态 结束状态 没有中间状态  本着全部提交成功的原则


- **3、隔离性（isolation）**

```
一个事务所做的修改在最终提交以前，对其他事务是不可见的
```

- **4、持久性（durability）**

```
一旦事务提交，则其所做的修改就会永久保存到数据库中。此时即使系统崩溃，修改的数据也不会丢失
```

**注意**

```mysql
1、事务只针对于表记录操作(增删改)有效,对于库和表的操作无效
2、事务一旦提交结束，对数据库中数据的更改是永久性的
```

## **E-R模型(Entry-Relationship)**

**定义**		
 
```mysql
E-R模型即 实体-关系 数据模型,用于数据库设计
用简单的图(E-R图)反映了现实世界中存在的事物或数据以及他们之间的关系
```

**实体、属性、关系**

- 实体

```mysql
1、描述客观事物的概念
2、表示方法 ：矩形框
3、示例 ：一个人、一本书、一杯咖啡、一个学生
```

- 属性

```mysql
1、实体具有的某种特性
2、表示方法 ：椭圆形
3、示例
   学生属性 ：学号、姓名、年龄、性别、专业 ... 
   感受属性 ：悲伤、喜悦、刺激、愤怒 ...
```

- ==关系（重要）==

```mysql
1、实体之间的联系
2、一对一关联(1:1) ：老公对老婆
   A中的一个实体,B中只能有一个实体与其发生关联
   B中的一个实体,A中只能有一个实体与其发生关联
3、一对多关联(1:n) ：父亲对孩子
   A中的一个实体,B中有多个实体与其发生关联
   B中的一个实体,A中只能有一个与其发生关联
4、多对多关联(m:n) ：兄弟姐妹对兄弟姐妹、学生对课程
   A中的一个实体,B中有多个实体与其发生关联
   B中的一个实体,A中有多个实体与其发生关联
```

**ER图的绘制**

矩形框代表实体,菱形框代表关系,椭圆形代表属性

- 课堂示例（老师研究课题）

```mysql
1、实体 ：教师、课题
2、属性
   教师 ：教师代码、姓名、职称
   课题 ：课题号、课题名
3、关系
   多对多（m:n)
   # 一个老师可以选择多个课题，一个课题也可以被多个老师选
```

- 练习

设计一个学生选课系统的E-R图

```mysql
1、实体：学生、课程、老师
2、属性
3、关系
   学生 选择 课程 (m:n)
   课程 任课 老师 (1:n)
```

==**关系映射实现（重要）**==

```mysql
1:1实现 --> 主外键关联,外键字段添加唯一索引
  表t1 : id int primary key,
          1
  表t2 : t2_id int unique,
         foreign key(t2_id) references t1(id)
          1
1:n实现 --> 主外键关联
  表t1 : id int primary key,
         1
  表t2 : t2_id int,
         foreign key(t2_id) references t1(id)
         1
         1   


# 字表设外键实现一对多
父表         子表    外键父表
id           id      did
1             1       1
2             2       1
3             3       1

此方法可以实现一对多,但多对多不行,因为当子表要对应多个父表时,无法表示,得借助中间表


m:n实现(借助中间表):
   t1 : t1_id 
   t2 : t2_id 
```
中间表样式
id        父id       子id
1          1          1
2          1          2

3          10         10
4          20         10


**==多对多实现==**

- 老师研究课题

```
表1、老师表
表2、课题表
问题？如何实现老师和课程之间的多对多映射关系？
中间表：
```
样式:
mysql> select * from course;
+----+---------+
| id | cname   |
+----+---------+
|  1 | Django  |
|  2 | Mysql   |
|  3 | Project |
+----+---------+
3 rows in set (0.01 sec)

mysql> select * from teacher;
+----+-----------+-------+
| id | tname     | level |
+----+-----------+-------+
|  1 | 郭小闹    | 牛X   |
|  2 | 魏哥哥    | 牛XX  |
+----+-----------+-------+
2 rows in set (0.00 sec)

mysql> select * from middle;
+----+------+------+
| id | tid  | cid  |
+----+------+------+
|  1 |    1 |    1 |
|  2 |    1 |    2 |
|  3 |    2 |    1 |
|  4 |    2 |    2 |
|  5 |    1 |    3 |
+----+------+------+





- 后续

```mysql
1、每个老师都在研究什么课题？
    select teacher.tname,course.cname from teacher 
    inner join middle on teacher.id = middle.tid 
    inner join course on middle.cid = course.id
2、郭小闹在研究什么课题？
    select teacher.tname,course.cname from teacher 
    inner join middle on teacher.id = middle.tid 
    inner join course on middle.cid = course.id
    where tname = "郭小闹"


```

## **==MySQL调优==**

**存储引擎优化**

```mysql
1、读操作多：MyISAM
2、写操作多：InnoDB
```

**索引优化**

```
在 select、where、order by 常涉及到的字段建立索引
```

**SQL语句优化**

```mysql
1、单条查询最后添加 LIMIT 1，停止全表扫描
2、where子句中不使用 != ,否则放弃索引全表扫描    用>= 或者 <=
3、尽量避免 NULL 值判断,否则放弃索引全表扫描
   优化前：select number from t1 where number is null;
   优化后：select number from t1 where number=0;
   # 在number列上设置默认值0,确保number列无NULL值
4、尽量避免 or 连接条件,否则放弃索引全表扫描
   优化前：select id from t1 where id=10 or id=20;
   优化后： select id from t1 where id=10 union all 
           select id from t1 where id=20;
           
5、模糊查询尽量避免使用前置 % ,否则全表扫描
   select name from t1 where name like "c%";
   
6、尽量避免使用 in 和 not in,否则全表扫描    可以使用exists
	select num from a where num in(select num from b)
	优化为： select num from a where exists(select 1 from b where b.num = a.num)
	
   优化前：select id from t1 where id in(1,2,3,4);
   优化后：select id from t1 where id between 1 and 4;
   
7、尽量避免使用 select * ...;用具体字段代替 * ,不要返回用不到的任何字段
	用具体的字段或者 1

8、避免在索引字段上使用计算，也就是说尽量避免在where字句中对字段进行表达式操作和函数操作。这将导致引擎放弃使用索引，进行全表扫描
	select id from xx where num/2 = 100
	select id from xx where num = 200
	...

```



**作业讲解**

有一张文章评论表comment如下

| **comment_id** | **article_id** | **user_id** | **date**            |
| -------------- | -------------- | ----------- | ------------------- |
| 1              | 10000          | 10000       | 2018-01-30 09:00:00 |
| 2              | 10001          | 10001       | ... ...             |
| 3              | 10002          | 10000       | ... ...             |
| 4              | 10003          | 10015       | ... ...             |
| 5              | 10004          | 10006       | ... ...             |
| 6              | 10025          | 10006       | ... ...             |
| 7              | 10009          | 10000       | ... ...             |

以上是一个应用的comment表格的一部分，请使用SQL语句找出在本站发表的所有评论数量最多的10位用户及评论数，并按评论数从高到低排序

备注：comment_id为评论id

​            article_id为被评论文章的id

​            user_id 指用户id

```

```

2、把 /etc/passwd 文件的内容导入到数据库的表中

```mysql

```

**3、外键及查询题目**

综述：两张表，一张顾客信息表customers，一张订单表orders

表1：顾客信息表，完成后插入3条表记录

```
c_id 类型为整型，设置为主键，并设置为自增长属性
c_name 字符类型，变长，宽度为20
c_age 微小整型，取值范围为0~255(无符号)
c_sex 枚举类型，要求只能在('M','F')中选择一个值
c_city 字符类型，变长，宽度为20
c_salary 浮点类型，要求整数部分最大为10位，小数部分为2位
```

```mysql
create table customers(
c_id int primary key auto_increment,
c_name varchar(20),
c_age tinyint unsigned,
c_sex enum('M','F'),
c_city varchar(20),
c_salary decimal(12,2)
)charset=utf8;
insert into customers values(1,'Tom',25,'M','上海',10000),(2,'Lucy',23,'F','广州',12000),(3,'Jim',22,'M','北京',11000);
```

表2：顾客订单表（在表中插入5条记录）

```
o_id 整型
o_name 字符类型，变长，宽度为30
o_price 浮点类型，整数最大为10位，小数部分为2位
设置此表中的o_id字段为customers表中c_id字段的外键,更新删除同步
insert into orders values(1,"iphone",5288),(1,"ipad",3299),(3,"mate9",3688),(2,"iwatch",2222),(2,"r11",4400);
```

```mysql
create table orders(
o_id int,
o_name varchar(30),
o_price decimal(12,2),
foreign key(o_id) references customers(c_id) on delete cascade on update cascade
)charset=utf8;
insert into orders values(1,"iphone",5288),(1,"ipad",3299),(2,"iwatch",2222),(2,"r11",4400);
```

增删改查题

```mysql
1、返回customers表中，工资大于4000元，或者年龄小于29岁，满足这样条件的前2条记录

2、把customers表中，年龄大于等于25岁，并且地址是北京或者上海，这样的人的工资上调15%
  
3、把customers表中，城市为北京的顾客，按照工资降序排列，并且只返回结果中的第一条记录
  
4、选择工资c_salary最少的顾客的信息
  
5、找到工资大于5000的顾客都买过哪些产品的记录明细	
  
6、删除外键限制
 
7、删除customers主键限制
 
8、增加customers主键限制c_id
  
```

<<<<<<< HEAD



=======
>>>>>>> d296d4f798072d633ab61f370c741649018801a4
