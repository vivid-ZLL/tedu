#### 重要的linux命令
* 管道 |
* tar -zcvf filename.tar.gz file1 file2 directory3 
        将文件|目录打包并压缩
 
    tar -zxvf filename.tar.gz [-C path]
        解压缩,默认解压到当前路径,-C可指定路径
* cp mv
* chmod
* vi awk


#### 组与用户
```
chmod 666 abc.py
```

-rw-r--r--
分三组   所有者  所属组  其他的用户
前三位(数字): 所有者 >>> 当前用户
中三位:  所属组的用户 >>> 例如当前组的用户tarena2
后三位:  其他组的其他用户 >>>  例如开发组、运维组
r  读(4)
w  写(2)
x  可执行(1)
```
# 777  rwxrwxrwxmv
# 666  rw-rw-rw-
# 644  rw-r--r--
```



####虚拟化系统 exsi-6.5
一个服务器部署多个操作系统 >>> ubuntu18.04  RedHat7 CentOS 7 Windows server 2010
为什么要熟悉linux命令? >>>服务器无图形化界面,它通过输入命令实现人机交互

CentOS RedHat7 安装软件用yum源  配置文件的路径与ubuntu不同
自己笔记本安装xshell secureCRT

使用xshell与远程服务器连接 与服务器传输数据
配置: ip地址
     ssh协议 端口22
     服务器端安装openssh-server  打开22端口
     密钥 141212-


# **Linux**

## **常用Linux操作系统**

```python
RedHat(红帽)：6.5、7 
CentOS：6.5、7
Ubuntu：16.04、18.04
```

## **远程连接工具-xshell**

```python
# 1、定义
xshell: 安装终端模拟软件
# 2、使用
文件-新建-输入服务器IP地址-输入用户名-输入密码-确认连接
# 3、文件互传
sudo apt-get install lrzsz
Windows -> Linux：rz 
Linux -> Windows: sz filename
```

## **默认已熟练使用的Linux命令**

```python
1、pwd
2、cd    -- cd .. 、cd
3、ls    -- ll
4、mkdir -p
    -p递归创建目录
5、touch
    touch命令不常用，一般用于更改文件时间戳，或创建一个空文件

    命令选项

    -a：只更改访问时间
    -c：--no-create	不创建任何文件
    -d：--date=字符串	使用指定字符串表示时间而非当前时间
    -m：只更改修改时间
    -r：把指定文件或目录的时间，统统设成和参考文件或目录的时间相同
    -t：使用指定的时间，而非当前时间，时间格式为：[[CC]YY]MMDDhhmm[.ss]
    --help：显示帮助信息
    --version：显示版本信息


6、tar   
    tar -zcvf filename.tar.gz file1 file2 directory3 
        将文件|目录打包并压缩
 
    tar -zxvf filename.tar.gz [-C path]
        解压缩,默认解压到当前路径,-C可指定路径


7、cp    -- cp -r     
    r 递归复制
8、mv
    mv  dir1 /home/tarena/...
    move dir1 dir2 用剪切实现重命名

```



## **常用命令**

```python
1、ifconfig
  查看IP地址和MAC地址,Windows中命令为:ipconfig

2、ping IP/域名 [-c n]
  测试网络连通性,-c指定连接次数

3、nslookup 域名
  解析域名对应的IP地址

4、ls -lh file|directory
  显示文件权限及详细信息
  h 提供易读的容量单位
ssh user@IP
ssh user@IPe1 file2 directory3 
ssh user@IP
ssh user@IP
ssh user@IP path]
  解压缩,默认解压到当前路径,-C可指定路径

7、ps -aux
  显示进程命令(包含PID号)  ps -aux | grep 'mysql'
    grep 筛选


8、kill PID
  杀死某个进程
  eg: ps -aux | grep 'mysql'
      sudo kill PID号ssh user@IP

9、chmod 权限 file
  给文件指定或者增加某权限

10、chown user:group file
  更改属主和属组
  eg: chown root:root file
       
11、 
  在某个路径下查找文件
  eg: find /home/tarena/ -name ssh user@IP'*.avi'
    ssh user@IP
12、ssh user@IPssh user@IP
  远程连接到服务器ssh user@IP
  eg: ssh tarena@172.40.91.138
    
13、scp file user@IP:绝对路径
  本地文件复制到远程
  eg: scp python.tar.gz tarena@172.40.91.138:/home/tarena/
```

## **vi及vim使用**

```python
文本编辑器,vim是vi的升级版
# 使用流程
1、vi filename
初始(不能编辑,浏览模式)  -> 按 a(可编辑,插入模式) -> 编辑内容 -> 按ESC,然后shift+:(命令行模式) -> 输入wq!(保存并退出)、或q!(不保存直接退出)

# 常用
1、查找
  浏览模式 -> 输入 /  -> 输入查找内容 -> Enter  (n表示下1个,shift+n表示上1个)
2、复制+删除+粘贴+撤销
  yy：复制光标所在行(2yy复制两行内容)
   p：粘贴
  dd：删除(剪切)光标所在行(3dd删除(剪切)3行内容）
   u: 撤销

# 光标的跳转(浏览模式)：
  行首： home
  行尾： end
  全文的首行：gg
  全文的最后一行：G
  全文的12行：12G
```

**练习**		

```python
1、在用户主目录下新建目录(mkdir):  你的名字(比如:MrRight)
2、在目录MrRight中新建文件song.txt(可使用touch命令,或者直接使用vim)
3、在song.txt中写入一首你最喜欢的诗,保存并退出
4、把/etc/passwd文件拷贝到 MrRight 目录一份(cp命令)
5、在 /home/tarena/MrRight/passwd 文件中筛选 tarena 用户的信息(grep命令)
6、查看passwd文件的权限,并将其权限修改为所有用户都可读可写但是不可执行(chmod命令)
7、将 MrRight 目录打包压缩,MrRight-你的名字.tar.gz
8、将此压缩包远程复制到 主讲机 | 同桌 计算机的电脑上

```

## **Linux命令-Go on**

```python
# 14、管道操作  | ：  
  将前面命令的输出，专递给后面命令，作为后面命令的参数
  查看 /etc/passwd 文件的 第6-10行？ - cat、head、tail
  
# 15、统计目录总共的占用空间的大小
  du -sh 目录

# 16、查看磁盘使用情况(根分区使用情况)
  df -h

# 17、常见通配符使用
  *：任意多个字符
  ？：单个字符
  eg1: rm -rf /home/tarena/test/*
  eg2: ls *.jpg

# 18、重定向: 将前面命令的输出，写入到文本文件中
  >：覆盖重定向
  >>：追加重定向
    
# 19、创建用户(会创建同名组)
  useradd username

# 20、设置密码
  sudo passwd 用户名

# 21、删除用户
  userdel
  -r：递归删除，删除用户的家目录以及用户的邮件文件
```

## **raid0 raid1 raid5的区别**

```python
# 1、什么是raid？
由一系列硬盘组成的阵列,简单说:一个服务器有10个一硬盘,你如何能保证坏掉1个硬盘后数据不丢,业务不断

# raid分类:raid0 、raid1、raid5
raid0
  1、特点:数据分散存储在多个硬盘
  2、优点:读写并发,速度超ssh user@IP升数倍
  3、缺点:一旦一个硬盘挂掉ssh user@IP损坏全部数据
raid1:
  1、特点:数据分别写入两个ssh user@IP(写了两份)
  2、优点:实现了数据备份
  3、缺点:磁盘使用率只能到50%
raid5:
  1、特点:提供热备盘实现故障恢复
  2、优点:只损坏1块磁盘,数据不会损坏
  3、缺点:同时坏2块磁盘,数据损坏
```

## **Linux-Go on**
ssh user@IP
ssh user@IP
ssh user@IP
ssh user@IP
ssh user@IP
	
# 23、对文件中内容进行排序
  sort 文件名
  
# 24、去除重复行,并统计每行出现的次数(相邻行)
  uniq -c
  sort 文件名 | uniq -c
```

## **周期性计划任务**

```python
# 1、进入周期性计划任务
crontab -e (首次进入按2 - 找vim)

# 设置周期性计划任务
* * * * *  : 五个*号代表  分 时 日 月 周
分 ：0-59
时 ：0-23
日 ：1-31
月 ：1-12
周 ：0-6

# 开始设置 : 
1、'*' 代表所有可能值
2、',' 指定多个时间点
3、'/' 指定时间间隔频率
4、'-' 指定一个时间段
ssh user@IP
ssh user@IP
ssh user@IP 1,5 * * 
ssh user@IP
ssh user@IP6/1 * * *
4、每分钟执行: * * * * *

# 练习
1、每小时的第3分钟和第15分钟执行
  3,15 * * * *
2、每周六、周日的0点执行一个 01.py 文件
  0 0 * * 6,0
6、每天18:00到23:00之间每小时执行 01.py 文件
  0 18-23/1 * * *
```

## **文本处理工具 - awk**

**语法格式**

```python
awk 选项 '动作' 文件列表
```

**常用方式**

```python
Linux命令  |   awk  选项  '动作'
```

**使用方法**

```python
# 示例
awk '{print "abc"}' ip.txt
# 思考: 这个会输出什么？
df -h | awk '{print $1}'  $ 以空白作为切割

# -F：指定分隔符
awk -F ":" '{print $2}'  # 显示 : 分隔后的第2列
# 练习
输出本机的IP地址

```

**作业**

```python
# nginx的访问日志目录 ： /var/log/nginx/access.log
问题1: 把访问过自己的IP地址输出
       # awk '{print $1}' access.log  
问题2: 统计有多少个IP访问过我
       # awk '{print $1}' access.log | sort | uniq | wc -l
问题3: 统计每个IP地址的访问次数,输出前10个访问量最大的用户IP
       # awk '{print $1}' access.log | sort | uniq -c | sort  -rn -k 1 | head -10
```

**grep命令之正则表达式**

```python
# 正则表达式元字符集 - 使用grep命令
^    :   以 ... 开头
$    :   以 ... 结尾
.     :   任何1个字符
*    :   0次或多次

# 正则表达式扩展字符集 - 使用 egrep 命令
+    :   1次或多次
{n} :   出现n次
()  ：  分组

[a-z]   :  所有小写字母
[A-Z]  :  所有大写字母
[a-Z]  :  所有字母
[0-9]  : 所有数字
[a-Z0-9]  : 所有的字母和数字
```

**应用场景**

```python
# Mac地址正则匹配
([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}
```


# **Linux-day02笔记**

## **使用命令必须养成的习惯**

```python
1、tab键自动补全
2、Ctrl + l : 清理屏幕
3、Ctrl + c : 终止当前命令的执行
```

## **常用远程连接软件**

```python
# 终端仿真程序，其实就是Windows下登录UNIX或Linux服务器主机的软件，支持ssh、telnet
1、Xshell
2、Secure CRT

# xshell实现文件互传
1、xshell图形界面: 新建文件传输
2、安装: lrzsz,是一款可在linux里可代替ftp上传和下载的程序
```

## **常见服务的端口号**

```python
MySQL - 3306
MongoDB - 27017
Redis - 6379
redis-sentinel - 26379
SSH - 22
HHTP - 80 
NGINX - 80
HTTPS - 443
TELNET - 23
FTP - 21
```

## **文本处理工具 - awk**

**语法格式**

```python
awk 选项 '动作' 文件列表
```

**常用方式**

```python
Linux命令  |   awk  选项  '动作'
```

**作业**

```python
# nginx的访问日志目录 ： /var/log/nginx/access.log
问题1: 把访问过自己的IP地址输出
       # awk '{print $1}' access.log  
问题2: 统计有多少个IP访问过我
       # awk '{print $1}' access.log | sort | uniq | wc -l
问题3: 统计每个IP地址的访问次数,输出前10个访问量最大的用户IP
       # awk '{print $1}' access.log | sort | uniq -c | sort  -rn -k 1 | head -10
```


**grep命令之正则表达式**

```python
# 正则表达式元字符集 - 使用grep命令
^    :   以 ... 开头
$    :   以 ... 结尾
.     :   任何1个字符
*    :   0次或多次

# 正则表达式扩展字符集 - 使用 egrep 命令
+    :   1次或多次
{n} :   出现n次
()  ：  分组

[a-z]   :  所有小写字母
[A-Z]  :  所有大写字母
[a-Z]  :  所有字母
[0-9]  : 所有数字
[a-Z0-9]  : 所有的字母和数字
```

**应用场景**

```python
# Mac地址正则匹配
([0-9a-fA-F]{2}:){5}[0-9a-fA-F]{2}
```

## **shell编程**

### **Shell格式**

```shell
1、扩展名: xxx.sh
2、正文第一行必须指定解释器: #!/bin/bash
```

### **shell执行方式**

```shell
# 方式一: 加权限,  ./xxx.sh 执行
1、chmod +x  xxx.sh
2、./xxx.sh

# 方式二: 手动指定解释器
bash xxx.sh
```

### **变量**

- **自定义变量**

```shell
# 1. 定义变量
变量名=值    ---->  注意: =两侧绝对不能有空格
eg1: name="take me to your heart"

# 2. 调用变量的格式
echo $变量名
     
# 3. 小细节: 单引号和双引号的区别
单引号: 无法获取变量的值
双引号: 可以获取变量的值
```

- **环境变量+位置变量+预设变量**

```shell
# 环境变量
echo $USER   --  当前用户
echo $UID    --  当前用户的UID号
echo $PWD    --  当前路径
echo $PATH   --  命令搜索路径

# 位置变量
$1 $2 $3 ... ... shell的位置变量

# 预定义变量
$# $* $?

# $? : 返回上一条命令执行的状态(0代表正确,非0代表失败)
```

**示例**

```shell
输出$1+$2,例如输出结果: 3+5
#!/bin/bash
echo $1+$2
```

- **变量赋值 - 接收用户从终端输入的值**

```shell
# 语法格式
read -p 提示信息 变量名

# 示例
#!/bin/bash
read -p 请输入姓名: name
echo "您输入的姓名是:$name"

# 指定超时时间
read -p 提示信息 变量名
read -t n -p 提示信息 变量名

# 示例
#!/bin/bash
read -t 3 -p 请输入用户名: username
```

**练习**

```shell
1、输入学生姓名: 赵敏
2、输入学生成绩: 88
3、输出: 赵敏的成绩为88分
```

### **shell - 算术运算符**

```shell
# 运算符
1、+ - * / % 
2、++ : 自加1运算,类似于python中 i++  等同于 i+=1
3、-- : 同++
			
# 运算命令
1、let 运算表达式
	i=1
	let i++
	echo $i
2、expr 运算表达式
	i=1
	sum=`expr $i + 5` # +两侧要有空格
	echo $sum
3、$[]
	echo $[1+1]
	echo $[1-1]
	echo $[a+a] # 调用变量不用多次添加$符号
	echo $[1*1] # 乘法无需转义
```

**练习**

```shell
使用 位置变量+以上方法一、二中任何一种,实现2个数字的相加
#!/bin/bash
echo $[$1+$2]
echo `expr $1 + $2`
```

### **shell - 比较运算符**

```shell
# 语法格式
	[  判断语句  ]	# 注意括号必须有空格

# 1、字符比较
	[ A == A ]	#相等(等号两边需要有空格)
	[ A != B ]	#不相等
	[ -z $变量 ]	#判断是否为空

# 2、数字比较
	-eq	等于(equal)
	-ne	不等于(not equal)
	-gt	大于(greater than)
	-ge	大于等于(great or equal)
	-lt	小于(less than)
	-le	小于等于(less or equal)

# 3、文件|目录比较
   [ -e 文件或目录 ]    #是否存在exist
   [ -f  文件      ]    #存在且为文件file
   [ -d  目录      ]    #存在且为目录directory
   [ -r 文件或目录 ]    #判断是否可读read
   [ -w 文件或目录 ]    #判断是否可写write
   [ -x 文件或目录 ]    #判断是否可执行
```

### **shell - if分支结构**

```shell
# 1、单分支语法格式
     if 判断 ;then
        命令
        命令
     fi
# 2、双分支语法格式
	if 判断 ;then
		命令1
	else
		命令2
	fi
# 3、多分支语法格式
  if 判断;then
    命令1
  elif 判断 ;then
    命令2
  else
    命令3
  fi
# 示例
#!/bin/bash
if [ $USER == tarena ];then
	echo "Yes,You are Tarena."
else
	echo "You are other man."
fi
```

**练习:使用shell编写猜数字游戏,无须循环**

```shell
#!/bin/bash
num=$RANDOM
read -p "我有一个随机数,你猜:"  guess
if [ $guess -eq $num ];then
	echo "恭喜,猜对了."
	exit
elif [ $guess -gt $num ];then
	echo "你猜大了"
else
	echo "你猜小了"
fi
```

### **shell - for循环**

```shell
# 语法格式
for 变量 in 值序列
do
	命令
done
# 示例
for i in 1 2 3 4 5
do
	echo "hello world"
done
```

**练习:判断指定网段的IP地址哪些可以用,哪些不能用？**

```shell
#!/bin/bash

for i in {1..254}
do
   ping -c 2 172.40.91.$i &>/dev/null
   if [ $? -eq 0 ];then
		echo "172.40.91.$i is up."
   else
		echo "172.40.91.$i is down"
   fi
done
```

### **shell - while循环**

```python
# 语法格式
while 条件判断
do
	命令
done

# 示例
#!/bin/bash
i=1
while [ $i -lt 5 ]
do
   echo baby
   let i++
done
```

### **sehll - case分支结构**

```shell
# 1、特点
根据变量值的不同,执行不同的操作

# 2、语法格式
case $变量名 in
模式1)
	代码块 
	;;
模式2)
	代码块
	;;
*)
	代码块
	;;
esac
```

**练习:编写1个nginx的启动脚本，包含: start stop restart**

```shell
#!/bin/bash

read -p "操作(start|stop|restart):" op
case $op in
"start")
	sudo /etc/init.d/nginx restart
	;;
"stop")
	sudo /etc/init.d/nginx stop
	;;
"restart")
	sudo /etc/init.d/nginx restart
	;;
*)
	echo "Please choice in start|stop|restart"
	;;
esac
```

**知识点总结**

```shell
# 1、获取字符串长度
${#变量名}

# 2、字符串索引及切片
${string:index:number}
key='ABCDE'
${key:0:1} # A 获取下表索引为0的元素
${key:1:2} # BC

# 3、vim批量缩进
1、进入命令行模式 : shift + :
2、1,3> + Enter  : 1-3行缩进
3、1,3< + Enter  : 1-3行往回缩进
```

### **shell实战**

**1、每2秒中检测一次MySQL数据库的连接数量**

```shell
# mysqladmin命令
mysql服务器管理任务的工具，它可以检查mysql服务器的配置和当前工作状态
```

​	**代码实现**

```shell
#!/bin/bash
#每2秒检测一次MySQL并发连接数

user="root" 
passwd="123456" 

while : 
do         
	sleep 2         
	count=`mysqladmin  -u"$user"  -p"$passwd" status |  awk '{print $4}'`
	echo "`date %F` 并发连接数为:$count"
done
```

**2、根据md5校验码，检测文件是否被修改**

```shell
# 1、生成md5的文件校验码
md5sum nginx.conf
```

​	**代码实现**

```shell
#!/bin/bash 
#本示例脚本检测的是/etc 目录下所有的conf结尾的文件
#本脚本在目标数据没有被修改时执行一次，当怀疑数据被人篡改，再执行一次 
#将两次执行的结果做对比，MD5码发生改变的文件，就是被人篡改的文件 
for  i  in  $(ls /etc/*.conf) 
do  
	md5sum "$i" >> /home/tarena/md5log.txt
done 
```

**3、备份MySQL数据库**

>> db_bak.sh
```shell
# 备份MySQL数据库中的mysql库
#!/bin/bash 
 
user="root" 
passwd="123456" 
dbname="mysql"
date=$(date +%Y%m%d) 
 
#[ ! -d dir]测试目录是否存在，不存在则创建目录 
# mkdir -p 递归创建目录
if [  ! -d  /home/tarena/mysqlbackup ];then
		mkdir -p  /home/tarena/mysqlbackup
fi

#使用mysqldump命令备份数据库 
mysqldump -u"$user"  -p"$passwd" "$dbname" > /home/tarena/mysqlbackup/"$dbname"-${date}.sql 

```

**4、随机生成8位密码**

```shell
#!/bin/bash 
#设置变量key，存储密码的所有可能性（密码库），如果还需要其他字符请自行添加其他密码字符 
#使用$#统计密码库的长度 

key="0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ" 
num=${#key} 
#设置初始密码为空 
pass='' 
#循环8次，生成 8为随机密码 
#每次都是随机数对密码库的长度取余，确保提取的密码字符不超过密码库的长度 
#每次循环提取一位随机密码，并将该随机密码追加到pass变量的最后 
RANDOM生成数的范围是[0,2**8 - 1]
for i in {1..8} 
do   
	index=$[RANDOM%num]  
	pass=$pass${key:$index:1} 
done 
echo $pass 
```

**shell函数**
f1(){
  代码块
}

f1

