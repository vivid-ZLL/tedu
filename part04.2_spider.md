# 王伟超
# wangweichao@tedu.cn
# DAY01
## 网络爬虫概述
- ### 定义

```
网络蜘蛛、网络机器人，抓取网络数据的程序
其实就是用Python程序模仿人点击浏览器并访问网站，而且模仿的越像越好，让Web站点无法发现你不是人
```

- ### 爬取数据目的

```python
1、公司项目测试数据
2、公司业务部门及其他部门所需数据
3、数据分析
```

- ### 企业获取数据方式

```python
1、公司自有数据
2、第三方数据平台购买(数据堂、贵阳大数据交易所)
3、爬虫爬取数据
```

- ### Python做爬虫优势

```python
1、Python ：请求模块、解析模块丰富成熟,强大的Scrapy网络爬虫框架
2、PHP ：对多线程、异步支持不太好
3、JAVA：代码笨重,代码量大

4、C/C++：虽然效率高,但是代码成型慢
```

- ### 爬虫分类

```python
1、通用网络爬虫(搜索引擎使用,遵守robots协议)
  robots协议 ：网站通过robots协议告诉搜索引擎哪些页面可以抓取,哪些页面不能抓取,通用网络爬虫需要遵守robots协议（君子协议）
	https://www.taobao.com/robots.txt
2、聚焦网络爬虫 ：自己写的爬虫程序
```

- ### 爬虫爬取数据步骤

```python
1、确定需要爬取的URL地址
2、由请求模块向URL地址发出请求,并得到网站的响应
3、从响应内容中提取所需数据
   1、所需数据,保存
   2、页面中有其他需要继续跟进的URL地址,继续第2步去发请求，如此循环
```

## 爬虫请求模块一

### 模块名及导入

```python
1、模块名：urllib.request
2、导入方式：
   1、import urllib.request
   2、from urllib import request
```

### 常用方法详解

#### urllib.request.urlopen

- **作用** 

向网站发起请求并获取响应对象

- **参数**

```python
1、url：需要爬取的URL地址
2、timeout: 设置等待超时时间,指定时间内未得到响应抛出超时异常
```

- **第一个爬虫程序 - 01_urlopen.py**

打开浏览器，输入百度地址(http://www.baidu.com/)，得到百度的响应

```python
import urllib.request

# urlopen() ： 向URL发请求,返回响应对象
response=urllib.request.urlopen('http://www.baidu.com/')
# 提取响应内容
html = response.read().decode('utf-8')
# 打印响应内容
print(html)
```

- **响应对象（response）方法**

```python
1、bytes = response.read() # read()得到结果为 bytes 数据类型
2、string = response.read().decode() # decode() 转为 string 数据类型
3、url = response.geturl() # 返回实际数据的URL地址
4、code = response.getcode() # 返回HTTP响应码
# 补充
5、string.encode() # bytes -> string
6、bytes.decode()  # string -> bytes
```

  **思考：网站如何来判定是人类正常访问还是爬虫程序访问？？？**
检查请求头-->user-agent:  
>python爬虫  "User-Agent": "Python-urllib/3.6"

>火狐浏览器    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:68.0) Gecko/20100101 Firefox/68.0"

```python
# 向测试网站： http://httpbin.org/get 发请求,查看自己请求头
# 代码如下
import urllib.request
response=urllib.request.urlopen('http://httpbin.org/get')
html = response.read().decode()
print(html)

# html中的请求头headers如下
"headers": {
    "Accept-Encoding": "identity", 
    "Host": "httpbin.org", 
    "User-Agent": "Python-urllib/3.6"
  }, 
发现请求头中User-Agent竟然是:Python-urllib/3.6!!!!!!!!!!!!!!!!!!!
我们需要重构User-Agent,发请求时带着User-Agent过去,但是 urlopen()方法不支持重构User-Agent,那我们怎么办？请看下面的方法！！！
```


**常见的user-agent,常用的user-agent**
1) Chrome
Win7:
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.163 Safari/535.1
 
2) Firefox
Win7:
Mozilla/5.0 (Windows NT 6.1; WOW64; rv:6.0) Gecko/20100101 Firefox/6.0
 
3) Safari
Win7:
Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.50 (KHTML, like Gecko) Version/5.1 Safari/534.50
 
4) Opera
Win7:
Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50
 
5) IE
Win7+ie9：
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; Trident/5.0; .NET CLR 2.0.50727; SLCC2; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; Tablet PC 2.0; .NET4.0E)
 
Win7+ie8：
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)
 
WinXP+ie8：
Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB7.0)
 
WinXP+ie7：
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1)
 
<<<<<<< HEAD

=======
>>>>>>> 415285dbdfa3453ae0cce9d8467b6f1d50034cf0
WinXP+ie6：
Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)
 
6) 傲游
傲游3.1.7在Win7+ie9,高速模式:
Mozilla/5.0 (Windows; U; Windows NT 6.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12
 
傲游3.1.7在Win7+ie9,IE内核兼容模式:
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)
 
7) 搜狗
搜狗3.0在Win7+ie9,IE内核兼容模式:
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E; SE 2.X MetaSr 1.0)
 
搜狗3.0在Win7+ie9,高速模式:
Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/6.0.472.33 Safari/534.3 SE 2.X MetaSr 1.0
 
8) 360
360浏览器3.0在Win7+ie9:
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E)
 
9) QQ浏览器
QQ浏览器6.9(11079)在Win7+ie9,极速模式:
Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/13.0.782.41 Safari/535.1 QQBrowser/6.9.11079.201
 
QQ浏览器6.9(11079)在Win7+ie9,IE内核兼容模式:
Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; InfoPath.3; .NET4.0C; .NET4.0E) QQBrowser/6.9.11079.201
 
10) 阿云浏览器
阿云浏览器1.3.0.1724 Beta(编译日期2011-12-05)在Win7+ie9:
Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)





#### urllib.request.Request

- **作用**

创建请求对象(包装请求，重构User-Agent，使程序更像正常人类请求)



- **参数**

```python
1、url：请求的URL地址
2、headers：添加请求头（爬虫和反爬虫斗争的第一步）
```

- **使用流程**

```python
1、构造请求对象(重构User-Agent)
	req = urllib.request.Request(
    	url = 'http://httpbin.org/get'
      headers={'User-Agent':'Mozilla/5.0'}
    )
2、发请求获取响应对象(urlopen)
	res = urllib.request.urlopen(req)
3、获取响应对象内容
	html = res.read().decode('utf-8')
```

- **示例 - 02_Request.py**

向测试网站（http://httpbin.org/get）发起请求，构造请求头并从响应中确认请求头信息

```python
from urllib import request

# 定义常用变量：URL 、headers
url = 'http://httpbin.org/get'
headers = {
  'User-Agent':'Opera/9.80 (Windows NT 6.1; U; zh-cn) Presto/2.9.168 Version/11.50'
}
# 1. 创建请求对象 - 包装,并没有真正发请求
req = request.Request(url=url,headers=headers)
# 2. 获取响应对象
res = request.urlopen(req)
# 3. 提取响应内容
html = res.read().decode('utf-8')

print(html)
```

## URL地址编码模块

### 模块名及导入

- **模块**

```python
# 模块名
urllib.parse

# 导入
import urllib.parse
from urllib import parse
```

- **作用**

给URL地址中查询参数进行编码

```python
编码前：https://www.baidu.com/s?wd=美女
编码后：https://www.baidu.com/s?wd=%E7%BE%8E%E5%A5%B3
```


'http://www.baidu.com/s?wd=爱丽丝·玛格特罗伊德'
'http://www.baidu.com/s?wd=%E7%88%B1%E4%B8%BD%E4%B8%9D%C2%B7%E7%8E%9B%E6%A0%BC%E7%89%B9%E7%BD%97%E4%BC%8A%E5%BE%B7'


page = pn=7 


### 常用方法

#### urllib.parse.urlencode({dict})

- **URL地址中一个查询参数**

```python
# 查询参数：{'wd' : '美女'}
# urlencode编码后：'wd=%e7%be%8e%e5%a5%b3'

# 示例代码
query_string = {'wd' : '美女'}
result = urllib.parse.urlencode(query_string)
# result: 'wd=%e7%be%8e%e5%a5%b3'
```

- **URL地址中多个查询参数**

```python
from urllib import parse
params = {
	'wd' : '美女',
	'pn' : '50'
}
params = parse.urlencode(query_string_dict)
url = 'http://www.baidu.com/s?{}'.format(params)
print(url)
```

-  **拼接URL地址的3种方式**

```python
# 1、字符串相加
  baseurl = 'http://www.baidu.com/s?'
  params = 'wd=%E7XXXX&pn=20'
  url = baseurl + params

# 2、字符串格式化（占位符）
  params = 'wd=%E7XXXX&pn=20'
  url = 'http://www.baidu.com/s?%s'% params

# 3、format()方法
  url = 'http://www.baidu.com/s?{}'
  params = 'wd=#E7XXXX&pn=20'
  url = url.format(params)
```

- **练习**
  在百度中输入要搜索的内容，把响应内容保存到本地文件

```python
请输入搜索内容: 赵丽颖
# 最终保存到本地文件 - 赵丽颖.html
```

​	**代码实现 - 03_parse_baidu.py** 

```python
from urllib import request
from urllib import parse

# 拼接URL地址
def get_url(word):
  url = 'http://www.baidu.com/s?{}'
  # params: wd=%E7XXXXX
  params = parse.urlencode({'wd':word})
  url = url.format(params)

  return url


# 发请求,保存本地文件
def request_url(url,filename):
  headers = {'User-Agent':'Mozilla/5.0'}
  # 请求对象 + 响应对象 + 提取内容
  req = request.Request(url=url,headers=headers)
  res = request.urlopen(req)
  html = res.read().decode('utf-8')
  # 保存数据
  with open(filename,'w',encoding='utf-8') as f:
    f.write(html)

# 主程序入口
if __name__ == '__main__':
  word = input('请输入搜索内容:')
  url = get_url(word)
  filename = word + '.html'
  request_url(url,filename)
```

#### quote(string)编码

- **示例1**

```python
from urllib import parse

string = '美女'
print(parse.quote(string))
# 结果: %E7%BE%8E%E5%A5%B3
```

改写之前urlencode()代码，使用quote()方法实现

```python
from urllib import parse

url = 'http://www.baidu.com/s?wd={}'
word = input('请输入要搜索的内容:')
query_string = parse.quote(word)
print(url.format(query_string))
```

#### unquote(string)解码

- **示例**

```python
from urllib import parse

string = '%E7%BE%8E%E5%A5%B3'
result = parse.unquote(string)
print(result)
```

#### 总结

```python
# 1、urllib.request
req = urllib.request.Request(url,headers)
res = urllib.request.urlopen(req)
html = res.read().decode('utf-8')

# 2、响应对象res方法
res.read()
res.getcode()
res.geturl()

# 3、urllib.parse
urllib.parse.urlencode({})
urllib.parse.quote(string)
urllib.parse.unquote(string)
```

## 百度贴吧数据抓取案例 

### 要求

```python
1、输入贴吧名称:赵丽颖吧
2、输入起始页:1
3、输入终止页:3
4、保存到本地文件
   赵丽颖吧-第1页.html、赵丽颖吧-第2页.html ...
```

### 实现步骤

- **1、查看是否为静态页面**

```python
右键 - 查看网页源代码 - 搜索数据关键字
```

- **2、找URL规律**

```python
第1页:http://tieba.baidu.com/f?kw=？？&pn=0
第2页:http://tieba.baidu.com/f?kw=？？&pn=50
第n页:pn=(n-1)*50
```

- **3、获取网页内容**

- **4、提取所需数据**

- **5、保存(本地文件、数据库)**

  **代码实现 - 04_tieba_spider.py**

  ```python
  from urllib import request,parse
  import time
  import random
  from useragents import ua_list
  
  class BaiduSpider(object):
    def __init__(self):
      self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'
  
  # 获取
    def get_html(self,url):
      headers = {
        'User-Agent': random.choice(ua_list)
      }
      req = request.Request(url=url,headers=headers)
      res = request.urlopen(req)
      html = res.read().decode('utf-8')
  
      return html
  
    # 解析
    def parse_html(self):
      pass
  
    # 保存
    def write_html(self,filename,html):
      with open(filename,'w',encoding='utf-8') as f:
        f.write(html)
  
  # 入口函数
    def run(self):
      name = input('请输入贴吧名:')
      begin = int(input('请输入起始页:'))
      end = int(input('请输入终止页:'))
  
      # 查询参数编码
  
      params = parse.quote(name)
      for page in range(begin,end+1):
        # URL拼接
        pn = (page-1)*50
        pn = (page-1)*50
        url = self.url.format(params,pn)
  
        # 调用类内函数进行页面抓取+保存
        filename = '{}-第{}页.html'.format(name,page)
        html = self.get_html(url)
        self.write_html(filename,html)
        # 控制爬取速度
        time.sleep(random.randint(1,3))
        print('第%d页爬取完成' % page)
  
  if __name__ == '__main__':
    start = time.time()
    spider = BaiduSpider()
    spider.run()
    end = time.time()
    print('执行时间:%.2f' % (end-start))
  ```

## 正则解析模块

### re模块使用流程

- **方法一**

  ```python
r_list=re.findall('正则表达式',html,re.S)
  ```

- **方法二**

```python
# 1、创建正则编译对象
pattern = re.compile(r'正则表达式',re.S)
r_list = pattern.findall(html)
```

### 正则表达式元字符

| 元字符 | 含义                     |
| ------ | ------------------------ |
| .      | 任意一个字符（不包括\n） |
| \d     | 一个数字                 |
| \s     | 空白字符                 |
| \S     | 非空白字符               |
| []     | 包含[]内容               |
| *      | 出现0次或多次            |
| +      | 出现1次或多次            |

**思考：请写出匹配任意一个字符的正则表达式？**

```python
import re
# 方法一
pattern = re.compile('.',re.S)
# 方法二
pattern = re.compile('[\s\S]')
```
### 贪婪匹配和非贪婪匹配

- **贪婪匹配（默认）**

```python
1、在整个表达式匹配成功的前提下,尽可能多的匹配 *
2、表示方式： .*
```

- **非贪婪匹配**

```python
1、在整个表达式匹配成功的前提下,尽可能少的匹配 *
2、表示方式：.*?
```

**示例代码 - 05_re_greed.py**

```python
import re

html = '''
<div><p>九霄龙吟惊天变</p></div>
<div><p>风云际汇潜水游</p></div>
'''
# 贪婪匹配 ： .*
pattern = re.compile('<div><p>.*</p></div>',re.S)
r_list = pattern.findall(html)
print(r_list)

# 非贪婪匹配 ：.*?
pattern = re.compile('<div><p>.*?</p></div>',re.S)
r_list = pattern.findall(html)
print(r_list)
```

### 正则表达式分组

- **作用**

在完整的模式中定义子模式，将每个圆括号中子模式匹配出来的结果提取出来

- **示例**

```python
import re

s = 'A B C D'
p1 = re.compile('\w+\s+\w+')
print(p1.findall(s))
# 结果: ['A B','C D']

p2 = re.compile('(\w+)\s+\w+')
print(p2.findall(s))
# 结果: ['A','C']

p3 = re.compile('(\w+)\s+(\w+)')
print(p3.findall(s))
# 结果: [('A','B'),('C','D')]
```

- **分组总结**

```python
1、在网页中,想要什么内容,就加()
2、先按整体正则匹配,然后再提取分组()中的内容
  如果有2个及以上分组(),则结果中以元组形式显示 [('小区1','500万'),('小区2','600万'),()]
```

- **练习**

页面结构如下：

```html
# <div class="animal">.*?title="(.*?)".*?
<div class="animal">
    <p class="name">
		<a title="Tiger"></a>
    </p>
    <p class="content">
		Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
		<a title="Rabbit"></a>
    </p>

    <p class="content">
		Small white rabbit white and white
    </p>
</div>
```

从以上html代码结构中完成如下内容信息的提取：

```python
# 问题1
[('Tiger',' Two...'),('Rabbit','Small..')]
# 问题2
动物名称 ：Tiger
动物描述 ：Two tigers two tigers run fast
***************************************
动物名称 ：Rabbit
动物描述 ：Small white rabbit white and white
```

**代码实现 - 06_re_exercise.py**

```python
import re

html = '''
<div class="animal">
    <p class="name">
		  <a title="Tiger"></a>
    </p>
    <p class="content">
		  Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
		  <a title="Rabbit"></a>
    </p>

    <p class="content">
		  Small white rabbit white and white
    </p>
</div>
'''
pattern = re.compile(r'<div class="animal">.*?<a title="(.*?)".*?content">(.*?)</p>',re.S)
r_list = pattern.findall(html)
# 问题1
if r_list:
  print(r_list)
# r_list: [('Tiger','\n\t\t Two tigers xxx'),()]
# 问题2
if r_list:
    for r in r_list:
      print('动物名称:',r[0].strip())
      print('动物描述:',r[1].strip())
      print('*' * 50)
else:
    print('未匹配到数据')
```

## 今日作业

1、把百度贴吧案例重写一遍,不要参照课上代码
2、爬取猫眼电影信息 ：猫眼电影-榜单-top100榜

```python
第1步完成：
	猫眼电影-第1页.html
	猫眼电影-第2页.html
	... ... 

第2步完成：
	1、提取数据 ：电影名称、主演、上映时间
	2、先打印输出,然后再写入到本地文件
```

3、复习任务

```python
pymysql、MySQL基本命令
MySQL　：建库建表普通查询等
```







# DAY02

## Day01回顾

### 请求模块(urllib.request)

```python
req = request.Request(url,headers=headers)
res = request.urlopen(req)
html = res.read().decode('utf-8')
```

### 编码模块(urllib.parse)

```python
1、urlencode({dict})
   urlencode({'wd':'美女','pn':'20'})
   编码后 ：'wd=%E8%D5XXX&pn=20'

2、quote(string)
   quote('织女')
   编码后 ：'%D3%F5XXX'

3、unquote('%D3%F5XXX')
```

### 解析模块(re)

- **使用流程**

```python
pattern = re.compile('正则表达式',re.S)
r_list = pattern.findall(html)
```

- **贪婪匹配和非贪婪匹配**

```python
贪婪匹配(默认) ： .*
非贪婪匹配     ： .*?
```

- **正则表达式分组**

```python
1、想要什么内容在正则表达式中加()
2、多个分组,先按整体正则匹配,然后再提取()中数据。结果：[(),(),(),(),()]
```

### 抓取步骤

```python
1、确定所抓取数据在响应中是否存在（右键 - 查看网页源码 - 搜索关键字）
2、数据存在: 查看URL地址规律
3、写正则表达式,来匹配数据
4、程序结构
	1、使用随机User-Agent
	2、每爬取1个页面后随机休眠一段时间
```

```python
# 程序结构
class xxxSpider(object):
    def __init__(self):
        # 定义常用变量,url,headers及计数等
        
    def get_html(self):
        # 获取响应内容函数,使用随机User-Agent
    
    def parse_html(self):
        # 使用正则表达式来解析页面，提取数据
    
    def write_html(self):
        # 将提取的数据按要求保存，csv、MySQL数据库等
        
    def main(self):
        # 主函数，用来控制整体逻辑
        
if __name__ == '__main__':
    # 程序开始运行时间戳
    start = time.time()
    spider = xxxSpider()
    spider.main()
    # 程序运行结束时间戳
    end = time.time()
    print('执行时间:%.2f' % (end-start))
```

## **Day02笔记**

## 作业讲解

**作业1 - 正则分组练习**

页面结构如下：

```html
<div class="animal">
    <p class="name">
		<a title="Tiger"></a>
    </p>
    <p class="content">
		Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
		<a title="Rabbit"></a>
    </p>

    <p class="content">
		Small white rabbit white and white
    </p>
</div>
```

从以上html代码结构中完成如下内容信息的提取：

```python
# 问题1
[('Tiger',' Two...'),('Rabbit','Small..')]
# 问题2
动物名称 ：Tiger
动物描述 ：Two tigers two tigers run fast
***************************************
动物名称 ：Rabbit
动物描述 ：Small white rabbit white and white
```

**代码实现**

```python
import re

html = '''
<div class="animal">
    <p class="name">
		  <a title="Tiger"></a>
    </p>
    <p class="content">
		  Two tigers two tigers run fast
    </p>
</div>

<div class="animal">
    <p class="name">
		  <a title="Rabbit"></a>
    </p>

    <p class="content">
		  Small white rabbit white and white
    </p>
</div>
'''
pattern = re.compile(r'<div class="animal">.*?<a title="(.*?)".*?content">(.*?)</p>',re.S)
r_list = pattern.findall(html)
# 问题1
if r_list:
  print(r_list)
# r_list: [('Tiger','\n\t\t Two tigers xxx'),()]
# 问题2
if r_list:
    for r in r_list:
      print('动物名称:',r[0].strip())
      print('动物描述:',r[1].strip())
      print('*' * 50)
else:
    print('未匹配到数据')
```

### 猫眼电影top100抓取案例

```python
猫眼电影 - 榜单 - top100榜
电影名称、主演、上映时间
```

**数据抓取实现**

- **1、确定响应内容中是否存在所需数据**

```python
右键 - 查看网页源代码 - 搜索关键字 - 存在！！
```

- **2、找URL规律**

```python
第1页：https://maoyan.com/board/4?offset=0
第2页：https://maoyan.com/board/4?offset=10
第n页：offset=(n-1)*10
```

- **3、正则表达式**

```python
<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>
```

- **4、编写程序框架，完善程序**

```python
from urllib import request
import re
import time
import random
from useragents import ua_list

class MaoyanSpider(object):
  def __init__(self):
    self.url = 'https://maoyan.com/board/4?offset={}'
    # 计数
    self.num = 0

  # 获取
  def get_html(self,url):
    headers = {
      'User-Agent' : random.choice(ua_list)
    }
    req = request.Request(url=url,headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8')
    # 直接调用解析函数
    self.parse_html(html)

  # 解析
  def parse_html(self,html):
    re_bds = r'<div class="movie-item-info">.*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>'
    pattern = re.compile(re_bds,re.S)
    # film_list: [('霸王别姬','张国荣','1993'),()]
    film_list = pattern.fin
    
    
    
    dall(html)
    # 直接调用写入函数
    self.write_html(film_list)

  def write_html(self,film_list):
    item = {}
    for film in film_list:
      item['name'] = film[0].strip()
      item['star'] = film[1].strip()
      item['time'] = film[2].strip()[5:15]
      print(item)

      self.num += 1

  def main(self):
    for offset in range(0,31,10):
      url = self.url.format(offset)
      self.get_html(url)
      time.sleep(random.randint(1,2))
    print('共抓取数据:',self.num)

if __name__ == '__main__':
  start = time.time()
  spider = MaoyanSpider()
  spider.main()
  end = time.time()
  print('执行时间:%.2f' % (end-start))
```

## 数据持久化存储

### 数据持久化存储 - csv文件

- #### 作用

```python
将爬取的数据存放到本地的csv文件中
```

- #### 使用流程

```python
1、导入模块
2、打开csv文件
3、初始化写入对象
4、写入数据(参数为列表)
import csv 

with open('film.csv','w') as f:
    writer = csv.writer(f)
    writer.writerow([])
```

- #### 示例代码

创建 test.csv 文件，在文件中写入数据

```python
# 单行写入（writerow([]))
import csv
# 在windows中会默认加入空行,设置newline = ''就不会有空行了
with open('test.csv','w',newline='') as f:
	writer = csv.writer(f)
	writer.writerow(['步惊云','36'])
	writer.writerow(['超哥哥','25'])

# 多行写入(writerows([(),(),()]
import csv
with open('test.csv','w',newline='') as f:
	writer = csv.writer(f)
	writer.writerows([('聂风','36'),('秦霜','25'),('孔慈','30')])
```

- #### 练习

猫眼电影数据存入本地 maoyanfilm.csv 文件 - 使用writerow()方法实现

```python
# 存入csv文件 - writerow()
def write_html(self,film_list):
  with open('film.csv','a') as f:
    # 初始化写入对象,注意参数f别忘了
    writer = csv.writer(f)
    for film in film_list:
      L = [
        film[0].strip(),
        film[1].strip(),
        film[2].strip()[5:15]
      ]
      # writerow()参数为列表
      writer.writerow(L)
```

思考：使用 writerows()方法实现？

```python
# 存入csv文件 - writerows()
def write_html(self,film_list):
  L = []
  with open('film.csv','a') as f:
    # 初始化写入对象,注意参数f别忘了
    writer = csv.writer(f)
    for film in film_list:
      t = (
        film[0].strip(),
        film[1].strip(),
        film[2].strip()[5:15]
      )
      L.append(t)
    # writerows()参数为列表
    writer.writerows(L)
```

### 数据持久化存储 - MySQL数据库

**1、在数据库中建库建表**

```mysql
# 连接到mysql数据库
mysql -h127.0.0.1 -uroot -p123456
# 建库建表
create database maoyandb charset utf8;
use maoyandb;
create table filmtab(
name varchar(100),
star varchar(300),
time varchar(50)
)charset=utf8;
```

- **2、回顾pymysql基本使用**

```python
import pymysql

# 创建2个对象
db = pymysql.connect('localhost','root','123456','maoyandb',charset='utf8')
cursor = db.cursor()

# 执行SQL命令并提交到数据库执行
# execute()方法第二个参数为列表传参补位
ins = 'insert into filmtab values(%s,%s,%s)'
cursor.execute(ins,['霸王别姬','张国荣','1993'])
db.commit()

# 关闭
cursor.close()
db.close()
```

- **来试试高效的executemany()方法？**

```python
import pymysql

# 创建2个对象
db = pymysql.connect('192.168.153.137','tiger','123456','maoyandb',charset='utf8')
cursor = db.cursor()

# 抓取的数据
film_list = [('月光宝盒','周星驰','1994'),('大圣娶亲','周星驰','1994')]

# 执行SQL命令并提交到数据库执行
# execute()方法第二个参数为列表传参补位
cursor.executemany('insert into filmtab values(%s,%s,%s)',film_list)
db.commit()

# 关闭
cursor.close()
db.close()
```

- **3、将电影信息存入MySQL数据库（尽量使用executemany方法）**

```python
# mysql - executemany([(),(),()])
def write_html(self, film_list):
  L = []
  ins = 'insert into filmtab values(%s,%s,%s)'
  for film in film_list:
    t = (
      film[0].strip(),
      film[1].strip(),
      film[2].strip()[5:15]
    )
    L.append(t)

    self.cursor.executemany(ins, L)
    # 千万别忘了提交到数据库执行
    self.db.commit()
```

- **4、做个SQL查询**

```mysql
1、查询20年以前的电影的名字和上映时间
  select name,time from filmtab where time<(now()-interval 20 year);
2、查询1990-2000年的电影名字和上映时间
  select name,time from filmtab where time>='1990-01-01' and time<='2000-12-31';
```

### 数据持久化存储 - MongoDB数据库

**pymongo操作mongodb数据库**

> mongoDB是一个基于磁盘的非关系型(key-value)数据库,value为json串

mysql: 库   表   表记录

mongo: 库   集合  文档


```python
import pymongo

# 1.数据库连接对象
conn=pymongo.MongoClient('localhost',27017)
# 2.库对象
db = conn['库名']
# 3.集合对象
myset = db['集合名']
# 4.插入数据
myset.insert_one({字典})
```

mongodb常用命令

1.mongo
2.showdbs
3.use 库名   
4.show collections /  show tables   # 查看当前库中所有集合
5.db.集合名.find().pretty()  # 格式化输出文档
6.db.集合名.count()      同意集合中有多少条记录
7.db.dropdatabase()     删库


**思考**

```python
1、能否到电影详情页把评论抓取下来？
2、能否到电影详情页把电影图片抓取下来？ - 并按照电影名称分别创建文件夹
```

**代码实现**

```python
from urllib import request
import re
import time
import random
from useragents import ua_list
import os

class MaoyanSpider(object):
  def __init__(self):
    self.url = 'https://maoyan.com/board/4?offset={}'
    # 计数
    self.num = 0

  # 获取
  def get_html(self,url):
    headers = {
      'User-Agent' : random.choice(ua_list)
    }
    req = request.Request(url=url,headers=headers)
    res = request.urlopen(req)
    html = res.read().decode('utf-8','ignore')

    return html

  def re_func(self,re_bds,html):
    pattern = re.compile(re_bds,re.S)
    r_list = pattern.findall(html)

    return r_list

  # 解析
  def parse_html(self,url):
    re_bds = r'<div class="movie-item-info">.*?href="(.*?)".*?title="(.*?)".*?class="star">(.*?)</p>.*?releasetime">(.*?)</p>'
    # html获取 + re解析
    html = self.get_html(url)
    film_list = self.re_func(re_bds,html)
    # 直接调用写入函数
    self.write_html(film_list)

  def write_html(self,film_list):
    film_dict = {}
    for film in film_list:
      film_dict['name'] = film[1].strip()
      film_dict['star'] = film[2].strip()
      film_dict['time'] = film[3].strip()[5:15]
      two_url = 'https://maoyan.com{}'.format(film[0].strip())
      film_dict['comment'] = self.get_comment(two_url)
      self.save_image(two_url,film)
      print(film_dict)

      self.num += 1

  def get_comment(self,two_url):
    # 获取 + 解析
    html = self.get_html(two_url)
    re_bds = r'<div class="comment-content">(.*?)</div>'
    comment_list = self.re_func(re_bds,html)

    return comment_list
常用
常用
常用-img" data-src="(.*?)" alt=""></div>'
    html = self.get_html(two_url)
    img_link_list = self.re_func(re_bds,html)


    for img_link in img_link_list:
      req = request.Request(img_link)
      res = request.urlopen(req)
      html = res.read()
      # 处理文件名
      directory = 'D:\\猫眼\\{}\\'.format(film[1].strip())
      if not os.path.exists(directory):
        os.makedirs(directory)

      filename=directory + img_link.split('/')[-1].split('@')[0]
      with open(filename,'wb') as f:
        f.write(html)


  # 入口函数
  def run(self):
    for offset in range(0,31,10):
      url = self.url.format(offset)
      self.parse_html(url)
      time.sleep(random.randint(1,2))
    print('共抓取数据:',self.num)

if __name__ == '__main__':
  start = time.time()
  spider = MaoyanSpider()
  spider.run()
  end = time.time()
  print('执行时间:%.2f' % (end-start))
```

## 电影天堂二级页面抓取案例

### **领取任务**

```python
# 地址
电影天堂 - 2019年新片精品 - 更多
# 目标
电影名称、下载链接

# 分析
*********一级页面需抓取***********
        1、电影详情页链接
        
*********二级页面需抓取***********
        1、电影名称
  			2、电影下载链接
```

### 实现步骤

- **1、确定响应内容中是否存在所需抓取数据**

- **2、找URL规律**

```python
第1页 ：https://www.dytt8.net/html/gndy/dyzz/list_23_1.html
第2页 ：https://www.dytt8.net/html/gndy/dyzz/list_23_2.html
第n页 ：https://www.dytt8.net/html/gndy/dyzz/list_23_n.html
```

- **3、写正则表达式**

```python
1、一级页面正则表达式
   <table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>
2、二级页面正则表达式
   <div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>.*?<td style="WORD-WRAP.*?>.*?>(.*?)</a> 
```

- **4、代码实现**

```python
from urllib import request
import re
from useragents import ua_list
import time
import random

class FilmSkySpider(object):
  def __init__(self):
    # 一级页面url地址
    self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'

  # 获取html功能函数
  def get_html(self,url):
    headers = {
      'User-Agent':random.choice(ua_list)
    }
    req = request.Request(url=url,headers=headers)
    res = request.urlopen(req)
    # 通过网站查看网页源码,查看网站charset='gb2312'
    # 如果遇到解码错误,识别不了一些字符,则 ignore 忽略掉
    html = res.read().decode('gb2312','ignore')

    return html

  # 正则解析功能函数
  def re_func(self,re_bds,html):
    pattern = re.compile(re_bds,re.S)
    r_list = pattern.findall(html)

    return r_list

  # 获取数据函数 - html是一级页面响应内容
  def parse_page(self,one_url):
    html = self.get_html(one_url)
    re_bds = r'<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>'
    # one_page_list: ['/html/xxx','/html/xxx','/html/xxx']
    one_page_list = self.re_func(re_bds,html)

    for href in one_page_list:
      two_url = 'https://www.dytt8.net' + href
      self.parse_two_page(two_url)
      # uniform: 浮点数,爬取1个电影信息后sleep
      time.sleep(random.uniform(1, 3))


  # 解析二级页面数据
  def parse_two_page(self,two_url):
    item = {}
    html = self.get_html(two_url)
    re_bds = r'<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>.*?<td style="WORD-WRAP.*?>.*?>(.*?)</a>'
    # two_page_list: [('名称1','ftp://xxxx.mkv')]
    two_page_list = self.re_func(re_bds,html)

    item['name'] = two_page_list[0][0].strip()
    item['download'] = two_page_list[0][1].strip()

    print(item)


  def main(self):
    for page in range(1,201):
      one_url = self.url.format(page)
      self.parse_page(one_url)
      # uniform: 浮点数
      time.sleep(random.uniform(1,3))

if __name__ == '__main__':
  spider = FilmSkySpider()
  spider.main()
```

- **5、练习**

   把电影天堂数据存入MySQL数据库 - 增量爬取

  ```python
  # 思路
  # 1、MySQL中新建表 urltab,存储所有爬取过的链接的指纹
  # 2、在爬取之前,先判断该指纹是否爬取过,如果爬取过,则不再继续爬取
  ```
  
  **练习代码实现**
  
  ```mysql
  # 建库建表
  create database filmskydb charset utf8;
  use filmskydb;
  create table request_finger(
  finger char(32)
  )charset=utf8;
  create table filmtab(
  name varchar(200),
  download varchar(500)
  )charset=utf8;
  ```
  
  ```python
  from urllib import request
  import re
  from useragents import ua_list
  import time
  import random
  import pymysql
  from hashlib import md5
  
  
  class FilmSkySpider(object):
      def __init__(self):
          # 一级页面url地址
          self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
          self.db = pymysql.connect('192.168.153.151', 'tiger', '123456', 'filmskydb', charset='utf8')
          self.cursor = self.db.cursor()
  
      # 获取html功能函数
      def get_html(self, url):
          headers = {
              'User-Agent': random.choice(ua_list)
          }
          req = request.Request(url=url, headers=headers)
          res = request.urlopen(req)
          # 通过网站查看网页源码,查看网站charset='gb2312'
          # 如果遇到解码错误,识别不了一些字符,则 ignore 忽略掉
          html = res.read().decode('gb2312', 'ignore')
  
          return html
  
      # 正则解析功能函数
      def re_func(self, re_bds, html):
          pattern = re.compile(re_bds, re.S)
          r_list = pattern.findall(html)
  
          return r_list
  
      # 获取数据函数
      def parse_page(self, one_url):
          html = self.get_html(one_url)
          re_bds = r'<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>'
          # one_page_list: ['/html/xxx','/html/xxx','/html/xxx']
          one_page_list = self.re_func(re_bds, html)
  
          for href in one_page_list:
              two_url = 'https://www.dytt8.net' + href
              # 生成指纹 - md5加密
              s = md5()
              s.update(two_url.encode())
              two_url_md5 = s.hexdigest()
              # 判断链接是否需要抓取
              if self.is_go_on(two_url_md5):
                  self.parse_two_page(two_url)
                  # 爬取完成此链接后将指纹放到数据库表中
                  ins = 'insert into request_finger values(%s)'
                  self.cursor.execute(ins, [two_url_md5])
                  self.db.commit()
                  # uniform: 浮点数,爬取1个电影信息后sleep
                  time.sleep(random.uniform(1, 3))
  
  
      def is_go_on(self, two_url_md5):
          # 爬取之前先到数据库中查询比对
          sel = 'select finger from request_finger where finger=%s'
          # 开始抓取之前,先来判断该链接之前是否抓取过
          result = self.cursor.execute(sel, [two_url_md5])
          if not result:
              return True
  
  
      # 解析二级页面数据
      def parse_two_page(self, two_url):
          item = {}
          html = self.get_html(two_url)
          re_bds = r'<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>.*?<td style="WORD-WRAP.*?>.*?>(.*?)</a>'
          # two_page_list: [('名称1','ftp://xxxx.mkv')]
          two_page_list = self.re_func(re_bds, html)
  
          item['name'] = two_page_list[0][0].strip()
          item['download'] = two_page_list[0][1].strip()
  
          ins = 'insert into filmtab values(%s,%s)'
          film_list = [
              item['name'], item['download']
          ]
          self.cursor.execute(ins, film_list)
          self.db.commit()
          print(film_list)
  
  
      def main(self):
          for page in range(1, 201):
              one_url = self.url.format(page)
              self.parse_page(one_url)
              # uniform: 浮点数
              time.sleep(random.uniform(1, 3))
  
  
  if __name__ == '__main__':
      spider = FilmSkySpider()
      spider.main()
  ```

## requests模块

### 安装

- **Linux**

```python
sudo pip3 install requests
```

- **Windows**

```python
# 方法一
   进入cmd命令行 ：python -m pip install requests
# 方法二
   右键管理员进入cmd命令行 ：pip install requests
```

### requests.get()

- **作用**

```python
# 向网站发起请求,并获取响应对象
res = requests.get(url,headers=headers)
```

- **参数**

```python
1、url ：需要抓取的URL地址
2、headers : 请求头
3、timeout : 超时时间，超过时间会抛出异常
```

- **响应对象(res)属性**

```python
1、encoding ：响应字符编码
   res.encoding = 'utf-8'
2、text ：字符串
3、content ：字节流
4、status_code ：HTTP响应码
5、url ：实际数据的URL地址
```

- **非结构化数据保存**

```python
with open('xxx.jpg','wb') as f:
	f.write(res.content)
```

- **示例**

保存赵丽颖图片到本地

```python
import requests

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1567090051520&di=77e8b97b3280f999cf51340af4315b4b&imgtype=jpg&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20171121%2F4e6759d153d04c6badbb0a5262ec103d.jpeg'
headers = {'User-Agent':'Mozilla/5.0'}

html = requests.get(url=url,headers=headers).content
with open('花千骨.jpg','wb') as f:
    f.write(html)
```

- **练习**

```python
1、将猫眼电影案例改写为 requests 模块实现
2、将电影天堂案例改写为 requests 模块实现
```

## Chrome浏览器安装插件

### 安装方法

```python
1、把下载的相关插件（对应操作系统浏览器）后缀改为 .zip 
2、解压,打开Chrome浏览器 -> 右上角设置 -> 更多工具 -> 扩展程序 -> 点开开发者模式
#3、把相关插件文件夹拖拽到浏览器中,释放鼠标即可安装
#3、有的插件直接拖拽 .zip 文件释放即可
```

### 需要安装插件

```python
1、Xpath Helper: 轻松获取HTML元素的xPath路径
  # 开启/关闭: Ctrl + Shift + x
2、Proxy SwitchyOmega: Chrome浏览器中的代理管理扩展程序
3、JsonView: 格式化输出json格式数据
```

## 今日作业

```python
1、把之前所有代码改为 requests 模块
2、电影天堂数据,存入MySQL、MongoDB、CSV文件
3、百度图片抓取: 输入要抓取的图片内容,抓取首页的30张图片,保存到对应的文件夹，比如:
   你想要谁的照片，请输入: 赵丽颖
   创建文件夹到指定目录: 赵丽颖  并把首页30张图片保存到此文件夹下
4、抓取链家二手房房源信息（房源名称、总价）,把结果存入到MySQL数据库,MongoDB数据库,CSV文件
  # 小区名 、总价 、单价
```



# DAY03

## Day02回顾

### 爬取网站思路

```python
1、先确定是否为动态加载网站
2、找URL规律
3、正则表达式
4、定义程序框架，补全并测试代码
```

### 数据持久化 - csv

```python
 import csv
 with open('xxx.csv','w') as f:
	writer = csv.writer(f)
 	writer.writerow([])
	writer.writerows([(),(),()])
```

### 数据持久化 - MySQL

```mysql
import pymysql

# __init__(self)：
	self.db = pymysql.connect('IP',... ...)
	self.cursor = self.db.cursor()
# write_data(self):
	self.cursor.execute('sql',[data1])
	self.cursor.executemany('sql',[(data1),(data2),(data3)])
	self.db.commit()
# main(self):
	self.cursor.close()
	self.db.close()
```

### 数据持久化 - MongoDB

```mysql
import pymongo

# __init__(self)：
	self.conn = pymongo.MongoClient('IP',27017)
	self.db = self.conn['db_name']
	self.myset = self.db['set_name']
	
# write_data(self):
	self.myset.insert_one(dict)
	self.myset.insert_many([{},{},{}])

# MongoDB - Commmand
>show dbs
>use db_name
>show collections
>db.collection_name.find().pretty()
>db.collection_name.count()
>db.collection_name.drop()
>db.dropDatabase()
```

### 多级页面数据抓取

```python
# 整体思路 
1、爬取一级页面,提取 所需数据+链接,继续跟进
2、爬取二级页面,提取 所需数据+链接,继续跟进
3、... ... 
# 代码实现思路
1、所有数据最终都会在一级页面遍历每条数据时全部拿到
2、避免重复代码 - 请求、解析需定义函数
```

## **Day03笔记**
## 电影天堂二级页面抓取案例



### **领取任务**

```python
# 地址
电影天堂 - 2019年新片精品 - 更多
# 目标
电影名称、下载链接

# 分析
*********一级页面需抓取***********
        1、电影详情页链接
        
*********二级页面需抓取***********
        1、电影名称
  		  2、电影下载链接
```

### 实现步骤

- **1、确定响应内容中是否存在所需抓取数据**
- **2、找URL规律**

```python
第1页 ：https://www.dytt8.net/html/gndy/dyzz/list_23_1.html
第2页 ：https://www.dytt8.net/html/gndy/dyzz/list_23_2.html
第n页 ：https://www.dytt8.net/html/gndy/dyzz/list_23_n.html
```

- **3、写正则表达式**

```python
1、一级页面正则表达式
   <table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>
2、二级页面正则表达式
   <div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>.*?<td style="WORD-WRAP.*?>.*?>(.*?)</a> 
```

- **4、代码实现**

```python
from urllib import request
import re
from useragents import ua_list
import time
import random

class FilmSkySpider(object):
  def __init__(self):
    # 一级页面url地址
    self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'

  # 获取html功能函数
  def get_html(self,url):
    headers = {
      'User-Agent':random.choice(ua_list)
    }
    req = request.Request(url=url,headers=headers)
    res = request.urlopen(req)
    # 通过网站查看网页源码,查看网站charset='gb2312'
    # 如果遇到解码错误,识别不了一些字符,则 ignore 忽略掉
    html = res.read().decode('gb2312','ignore')

    return html

  # 正则解析功能函数
  def re_func(self,re_bds,html):
    pattern = re.compile(re_bds,re.S)
    r_list = pattern.findall(html)

    return r_list

  # 获取数据函数 - html是一级页面响应内容
  def parse_page(self,one_url):
    html = self.get_html(one_url)
    re_bds = r'<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>'
    # one_page_list: ['/html/xxx','/html/xxx','/html/xxx']
    one_page_list = self.re_func(re_bds,html)

    for href in one_page_list:
      two_url = 'https://www.dytt8.net' + href
      self.parse_two_page(two_url)
      # uniform: 浮点数,爬取1个电影信息后sleep
      time.sleep(random.uniform(1, 3))


  # 解析二级页面数据
  def parse_two_page(self,two_url):
    item = {}
    html = self.get_html(two_url)
    re_bds = r'<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>.*?<td style="WORD-WRAP.*?>.*?>(.*?)</a>'
    # two_page_list: [('名称1','ftp://xxxx.mkv')]
    two_page_list = self.re_func(re_bds,html)

    item['name'] = two_page_list[0][0].strip()
    item['download'] = two_page_list[0][1].strip()

    print(item)


  def main(self):
    for page in range(1,201):
      one_url = self.url.format(page)
      self.parse_page(one_url)
      # uniform: 浮点数
      time.sleep(random.uniform(1,3))

if __name__ == '__main__':
  spider = FilmSkySpider()
  spider.main()
```

- **5、练习**

  把电影天堂数据存入MySQL数据库 - 增量爬取

  ```python
  # 思路
  # 1、MySQL中新建表 request_finger,存储所有爬取过的链接的指纹
  # 2、在爬取之前,先判断该指纹是否爬取过,如果爬取过,则不再继续爬取
  ```

  **练习代码实现**

  ```mysql
  # 建库建表
  create database filmskydb charset utf8;
  use filmskydb;
  create table request_finger(
  finger char(32)
  )charset=utf8;
  create table filmtab(
  name varchar(200),
  download varchar(500)
  )charset=utf8;
  ```
  ```python
  from urllib import request
  import re
  from useragents import ua_list
  import time
  import random
  import pymysql
  from hashlib import md5
  
  
  class FilmSkySpider(object):
      def __init__(self):
          # 一级页面url地址
          self.url = 'https://www.dytt8.net/html/gndy/dyzz/list_23_{}.html'
          self.db = pymysql.connect('192.168.153.151', 'tiger', '123456', 'filmskydb', charset='utf8')
          self.cursor = self.db.cursor()
  
      # 获取html功能函数
      def get_html(self, url):
          headers = {
              'User-Agent': random.choice(ua_list)
          }
          req = request.Request(url=url, headers=headers)
          res = request.urlopen(req)
          # 通过网站查看网页源码,查看网站charset='gb2312'
          # 如果遇到解码错误,识别不了一些字符,则 ignore 忽略掉
          html = res.read().decode('gb2312', 'ignore')
  
          return html
  
      # 正则解析功能函数
      def re_func(self, re_bds, html):
          pattern = re.compile(re_bds, re.S)
          r_list = pattern.findall(html)
  
          return r_list
  
      # 获取数据函数
      def parse_page(self, one_url):
          html = self.get_html(one_url)
          re_bds = r'<table width="100%".*?<td width="5%".*?<a href="(.*?)".*?ulink">.*?</table>'
          # one_page_list: ['/html/xxx','/html/xxx','/html/xxx']
          one_page_list = self.re_func(re_bds, html)
  
          for href in one_page_list:
              two_url = 'https://www.dytt8.net' + href
              # 生成指纹 - md5加密
              s = md5()
              s.update(two_url.encode())
              two_url_md5 = s.hexdigest()
              # 判断链接是否需要抓取
              if self.is_go_on(two_url_md5):
                  self.parse_two_page(two_url)
                  # 爬取完成此链接后将指纹放到数据库表中
                  ins = 'insert into request_finger values(%s)'
                  self.cursor.execute(ins, [two_url_md5])
                  self.db.commit()
                  # uniform: 浮点数,爬取1个电影信息后sleep
                  time.sleep(random.uniform(1, 3))
  
  
      def is_go_on(self, two_url_md5):
          # 爬取之前先到数据库中查询比对
          sel = 'select finger from request_finger where finger=%s'
          # 开始抓取之前,先来判断该链接之前是否抓取过
          result = self.cursor.execute(sel, [two_url_md5])
          if not result:
              return True
  
  
      # 解析二级页面数据
      def parse_two_page(self, two_url):
          item = {}
          html = self.get_html(two_url)
          re_bds = r'<div class="title_all"><h1><font color=#07519a>(.*?)</font></h1></div>.*?<td style="WORD-WRAP.*?>.*?>(.*?)</a>'
          # two_page_list: [('名称1','ftp://xxxx.mkv')]
          two_page_list = self.re_func(re_bds, html)
  
          item['name'] = two_page_list[0][0].strip()
          item['download'] = two_page_list[0][1].strip()
  
          ins = 'insert into filmtab values(%s,%s)'
          film_list = [
              item['name'], item['download']
          ]
          self.cursor.execute(ins, film_list)
          self.db.commit()
          print(film_list)
  
  
      def main(self):
          for page in range(1, 201):
              one_url = self.url.format(page)
              self.parse_page(one_url)
              # uniform: 浮点数
              time.sleep(random.uniform(1, 3))
  
  
  if __name__ == '__main__':
      spider = FilmSkySpider()
      spider.main()
  ```

## requests模块

### 安装

- **Linux**

```python
sudo pip3 install requests
```

- **Windows**

```python
# 方法一
   进入cmd命令行 ：python -m pip install requests
# 方法二
   右键管理员进入cmd命令行 ：pip install requests
```

### requests.get()

- **作用**

```python
# 向网站发起请求,并获取响应对象
res = requests.get(url,headers=headers)
```

- **参数**

```python
1、url ：需要抓取的URL地址
2、headers : 请求头
3、timeout : 超时时间，超过时间会抛出异常
```

- **响应对象(res)属性**

```python
1、encoding ：响应字符编码
   res.encoding = 'utf-8'
2、text ：字符串
3、content ：字节流
4、status_code ：HTTP响应码
5、url ：实际数据的URL地址
```

- **非结构化数据保存**

```python
with open('xxx.jpg','wb') as f:
	f.write(res.content)
```

- **示例**

保存赵丽颖图片到本地

```python
import requests

url = 'https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1567090051520&di=77e8b97b3280f999cf51340af4315b4b&imgtype=jpg&src=http%3A%2F%2F5b0988e595225.cdn.sohucs.com%2Fimages%2F20171121%2F4e6759d153d04c6badbb0a5262ec103d.jpeg'
headers = {'User-Agent':'Mozilla/5.0'}

html = requests.get(url=url,headers=headers).content
with open('花千骨.jpg','wb') as f:
    f.write(html)
```

- **练习**

```python
1、将猫眼电影案例改写为 requests 模块实现
2、将电影天堂案例改写为 requests 模块实现
3、百度图片抓取: 输入要抓取的图片内容,抓取首页的30张图片,保存到对应的文件夹，比如:
   你想要谁的照片，请输入: 赵丽颖
   创建文件夹到指定目录: 赵丽颖  并把首页30张图片保存到此文件夹下
```

**百度图片练习代码实现**

```python
import requests
import re
from urllib import parse
import os

class BaiduImageSpider(object):
    def __init__(self):
        self.url = 'https://image.baidu.com/search/index?tn=baiduimage&word={}'
        self.headers = {'User-Agent':'Mozilla/5.0'}

    # 获取图片
    def get_image(self,url,word):
        html = requests.get(url,headers=self.headers).text
        pattern = re.compile('"hoverURL":"(.*?)"',re.S)
        img_link_list = pattern.findall(html)

        # 创建目录，准备保存图片
        directory = 'E:\\{}\\'.format(word)
        if not os.path.exists(directory):
            os.makedirs(directory)

        i = 1
        for img_link in img_link_list:
            filename = '{}{}_{}.jpg'.format(directory, word, i)
            self.save_image(img_link,filename)
            i += 1

    def save_image(self,img_link,filename):
        html = requests.get(url=img_link,headers=self.headers).content
        with open(filename,'wb') as f:
            f.write(html)
        print(filename,'下载成功')

    def run(self):
        word = input('你要谁的照片：')
        word_parse = parse.quote(word)
        url = self.url.format(word)
        self.get_image(url,word)

if __name__ == '__main__':
    spider = BaiduImageSpider()
    spider.run()
```

## Chrome浏览器安装插件

### 安装方法

```python
1、把下载的相关插件（对应操作系统浏览器）后缀改为 .zip 
2、解压,打开Chrome浏览器 -> 右上角设置 -> 更多工具 -> 扩展程序 -> 点开开发者模式
#3、把相关插件文件夹拖拽到浏览器中,释放鼠标即可安装
#3、有的插件直接拖拽 .zip 文件释放即可
```

### 需要安装插件

```python
1、Xpath Helper: 轻松获取HTML元素的xPath路径
  # 开启/关闭: Ctrl + Shift + x
2、Proxy SwitchyOmega: Chrome浏览器中的代理管理扩展程序
3、JsonView: 格式化输出json格式数据
```

## xpath解析

### 定义

```python
XPath即为XML路径语言，它是一种用来确定XML文档中某部分位置的语言，同样适用于HTML文档的检索
```

### 示例

```html
<ul class="CarList">
	<li class="bjd" id="car_001" href="http://www.bjd.com/">
        <p class="name">布加迪</p>
        <p class="model">威航</p>
        <p class="price">2500万</p>
        <p class="color">红色</p>
    </li>
    
    <li class="byd" id="car_002" href="http://www.byd.com/">
        <p class="name">比亚迪</p>
        <p class="model">秦</p>
        <p class="price">15万</p>
        <p class="color">白色</p>
    </li>
</ul>
```

### 匹配演示

```python
1、查找所有的li节点
  //li
2、获取所有汽车的名称: 所有li节点下的子节点p的值 (class属性值为name）
  //li/p[@class="name"]  
3、找比亚迪车的信息: 获取ul节点下第2个li节点的汽车信息
  //ul/li[2]                          
4、获取所有汽车的链接: ul节点下所有li子节点的href属性的值
  //ul/li/@href

# 只要涉及到条件,加 []
# 只要获取属性值,加 @
```

### 选取节点

```python
1、// ：从所有节点中查找（包括子节点和后代节点）
2、@  ：获取属性值
   # 使用场景1（属性值作为条件）
   # 获取所有class属性值为'movie-item-info'的div节点
     //div[@class="movie-item-info"]
   # 使用场景2（直接获取属性值）
   # 获取所有电影的标题
     //div[@class="movie-item-info"]/p/a/@title
```

### 匹配多路径（或）

```python
xpath表达式1 | xpath表达式2 | xpath表达式3
```

### 常用函数

```python
1、contains() ：匹配属性值中包含某些字符串节点
   # 查找id属性值中包含字符串 "car_" 的 li 节点
   //li[contains(@id,"car_")]
2、text() ：获取节点的文本内容
   # 查找所有汽车的价格
   //li/p[@class="price"]/text()
```

## lxml解析库

### 安装

```python
sudo pip3 install lxml
```

### 使用流程

```python
1、导模块
   from lxml import etree
2、创建解析对象
   parse_html = etree.HTML(html)
3、解析对象调用xpath
   r_list = parse_html.xpath('xpath表达式')
```

### html样本

```html
<div class="wrapper">
	<a href="/" id="channel">新浪社会</a>
	<ul id="nav">
		<li><a href="http://domestic.sina.com/" title="国内">国内</a></li>
		<li><a href="http://world.sina.com/" title="国际">国际</a></li>
		<li><a href="http://mil.sina.com/" title="军事">军事</a></li>
		<li><a href="http://photo.sina.com/" title="图片">图片</a></li>
		<li><a href="http://society.sina.com/" title="社会">社会</a></li>
		<li><a href="http://ent.sina.com/" title="娱乐">娱乐</a></li>
		<li><a href="http://tech.sina.com/" title="科技">科技</a></li>
		<li><a href="http://sports.sina.com/" title="体育">体育</a></li>
		<li><a href="http://finance.sina.com/" title="财经">财经</a></li>
		<li><a href="http://auto.sina.com/" title="汽车">汽车</a></li>
<!DOCTYPE html>

<!--[if IE 8]><html class="ie8"><![endif]-->
<!--[if IE 9]><html class="ie9"><![endif]-->
<!--[if gt IE 9]><!--><html><!--<![endif]-->
<head>
  <title>TOP100榜 - 猫眼电影 - 一网打尽好电影</title>
  
  <link rel="dns-prefetch" href="//p0.meituan.net"  />
  <link rel="dns-prefetch" href="//p1.meituan.net"  />
  <link rel="dns-prefetch" href="//ms0.meituan.net" />
  <link rel="dns-prefetch" href="//s0.meituan.net" />
  <link rel="dns-prefetch" href="//ms1.meituan.net" />
  <link rel="dns-prefetch" href="//analytics.meituan.com" />
  <link rel="dns-prefetch" href="//report.meituan.com" />
  <link rel="dns-prefetch" href="//frep.meituan.com" />

  
  <meta charset="utf-8">
  <meta name="keywords" content="猫眼电影,电影排行榜,热映口碑榜,最受期待榜,国内票房榜,北美票房榜,猫眼TOP100">
  <meta name="description" content="猫眼电影热门榜单,包括热映口碑榜,最受期待榜,国内票房榜,北美票房榜,猫眼TOP100,多维度为用户进行选片决策">
  <meta http-equiv="cleartype" content="yes" />
  <meta http-equiv="X-UA-Compatible" content="IE=edge" />
  <meta name="renderer" content="webkit" />

  <meta name="HandheldFriendly" content="true" />
  <meta name="format-detection" content="email=no" />
  <meta name="format-detection" content="telephone=no" />
  <meta name="viewport" content="width=device-width, initial-scale=1">

  
  <script>"use strict";!function(){var i=0<arguments.length&&void 0!==arguments[0]?arguments[0]:"_Owl_",n=window;n[i]||(n[i]={isRunning:!1,isReady:!1,preTasks:[],dataSet:[],use:function(i,t){this.isReady&&n.Owl&&n.Owl[i](t),this.preTasks.push({api:i,data:[t]})},add:function(i){this.dataSet.push(i)},run:function(){var t=this;if(!this.isRunning){this.isRunning=!0;var i=n.onerror;n.onerror=function(){this.isReady||this.add({type:"jsError",data:arguments}),i&&i.apply(n,arguments)}.bind(this),(n.addEventListener||n.attachEvent)("error",function(i){t.isReady||t.add({type:"resError",data:[i]})},!0)}}},n[i].run())}();</script>
  <script>
  cid = "c_wx6zb55";
  ci = 59;
val = {"subnavId":4};    window.system = {};

  window.openPlatform = '';
  window.openPlatformSub = '';
  window.$mtsiFlag = '0';

  </script>
  <link rel="stylesheet" href="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/common.0a548310.css"/>
<link rel="stylesheet" href="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/board-index.92a06072.css"/>
  <script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/stat.88d57c80.js"></script>
  <script>if(window.devicePixelRatio >= 2) { document.write('<link rel="stylesheet" href="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image-2x.8ba7074d.css"/>') }</script>
  <style>
    @font-face {
      font-family: stonefont;
      src: url('//vfile.meituan.net/colorstone/5e368763cd983dcc8d47afbb088607ae3436.eot');
      src: url('//vfile.meituan.net/colorstone/5e368763cd983dcc8d47afbb088607ae3436.eot?#iefix') format('embedded-opentype'),
           url('//vfile.meituan.net/colorstone/4939a1422248b3cf6b382554368dafb52292.woff') format('woff');
    }

    .stonefont {
      font-family: stonefont;
    }
  </style>
</head>
<body>


<div class="header">
  <div class="header-inner">
        <a href="/" class="logo" data-act="icon-click"></a>
        <div class="city-container" data-val="{currentcityid:59 }">
            <div class="city-selected">
                <div class="city-name">
                  成都
                  <span class="caret"></span>
                </div>
            </div>
            <div class="city-list" data-val="{ localcityid: 59 }">
                <div class="city-list-header">定位城市：<a class="js-geo-city">成都</a></div>
                
            </div>
        </div>


        <div class="nav">
            <ul class="navbar">
                <li><a href="/" data-act="home-click"  >首页</a></li>
                <li><a href="/films" data-act="movies-click" >电影</a></li>
                <li><a href="/cinemas" data-act="cinemas-click" >影院</a></li> 
                <li><a href="http://www.gewara.com">演出</a></li>
                
                <li><a href="/board" data-act="board-click"  class="active" >榜单</a></li>
                <li><a href="/news" data-act="hotNews-click" >热点</a></li>
                <li><a href="/edimall"  >商城</a></li>
            </ul>
        </div>

        <div class="user-info">
            <div class="user-avatar J-login">
              <img src="https://p0.meituan.net/movie/7dd82a16316ab32c8359debdb04396ef2897.png">
              <span class="caret"></span>
              <ul class="user-menu">
                <li><a href="javascript:void 0">登录</a></li>
              </ul>
            </div>
        </div>

        <form action="/query" target="_blank" class="search-form" data-actform="search-click">
            <input name="kw" class="search" type="search" maxlength="32" placeholder="找影视剧、影人、影院" autocomplete="off">
            <input class="submit" type="submit" value="">
        </form>

        <div class="app-download">
          <a href="/app" target="_blank">
            <span class="iphone-icon"></span>
            <span class="apptext">APP下载</span>
            <span class="caret"></span>
            <div class="download-icon">
                <p class="down-title">扫码下载APP</p>
                <p class='down-content'>选座更优惠</p>
            </div>
          </a>
        </div>
    
  </div>
</div>
<div class="header-placeholder"></div>

<div class="subnav">
  <ul class="navbar">
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:7}"
          href="/board/7"
      >热映口碑榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:6}"
          href="/board/6"
      >最受期待榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:1}"
          href="/board/1"
      >国内票房榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:2}"
          href="/board/2"
      >北美票房榜</a>
    </li>
    <li>
      <a data-act="subnav-click" data-val="{subnavClick:4}"
          data-state-val="{subnavId:4}"
          class="active" href="javascript:void(0);"
      >TOP100榜</a>
    </li>
  </ul>
</div>


    <div class="container" id="app" class="page-board/index" >

<div class="content">
    <div class="wrapper">
        <div class="main">
            <p class="update-time">2019-09-10<span class="has-fresh-text">已更新</span></p>
            <p class="board-content">榜单规则：将猫眼电影库中的经典影片，按照评分和评分人数从高到低综合排序取前100名，每天上午10点更新。相关数据来源于“猫眼电影库”。</p>
            <dl class="board-wrapper">
                <dd>
                        <i class="board-index board-index-1">1</i>
    <a href="/films/1203" title="霸王别姬" class="image-link" data-act="boarditem-click" data-val="{movieId:1203}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/20803f59291c47e1e116c11963ce019e68711.jpg@160w_220h_1e_1c" alt="霸王别姬" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1203" title="霸王别姬" data-act="boarditem-click" data-val="{movieId:1203}">霸王别姬</a></p>
        <p class="star">
                主演：张国荣,张丰毅,巩俐
        </p>
<p class="releasetime">上映时间：1993-01-01</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-2">2</i>
    <a href="/films/1297" title="肖申克的救赎" class="image-link" data-act="boarditem-click" data-val="{movieId:1297}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/283292171619cdfd5b240c8fd093f1eb255670.jpg@160w_220h_1e_1c" alt="肖申克的救赎" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1297" title="肖申克的救赎" data-act="boarditem-click" data-val="{movieId:1297}">肖申克的救赎</a></p>
        <p class="star">
                主演：蒂姆·罗宾斯,摩根·弗里曼,鲍勃·冈顿
        </p>
<p class="releasetime">上映时间：1994-09-10(加拿大)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-3">3</i>
    <a href="/films/2641" title="罗马假日" class="image-link" data-act="boarditem-click" data-val="{movieId:2641}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/289f98ceaa8a0ae737d3dc01cd05ab052213631.jpg@160w_220h_1e_1c" alt="罗马假日" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/2641" title="罗马假日" data-act="boarditem-click" data-val="{movieId:2641}">罗马假日</a></p>
        <p class="star">
                主演：格利高里·派克,奥黛丽·赫本,埃迪·艾伯特
        </p>
<p class="releasetime">上映时间：1953-09-02(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">1</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-4">4</i>
    <a href="/films/4055" title="这个杀手不太冷" class="image-link" data-act="boarditem-click" data-val="{movieId:4055}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/6bea9af4524dfbd0b668eaa7e187c3df767253.jpg@160w_220h_1e_1c" alt="这个杀手不太冷" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/4055" title="这个杀手不太冷" data-act="boarditem-click" data-val="{movieId:4055}">这个杀手不太冷</a></p>
        <p class="star">
                主演：让·雷诺,加里·奥德曼,娜塔莉·波特曼
        </p>
<p class="releasetime">上映时间：1994-09-14(法国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-5">5</i>
    <a href="/films/267" title="泰坦尼克号" class="image-link" data-act="boarditem-click" data-val="{movieId:267}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/b607fba7513e7f15eab170aac1e1400d878112.jpg@160w_220h_1e_1c" alt="泰坦尼克号" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/267" title="泰坦尼克号" data-act="boarditem-click" data-val="{movieId:267}">泰坦尼克号</a></p>
        <p class="star">
                主演：莱昂纳多·迪卡普里奥,凯特·温丝莱特,比利·赞恩
        </p>
<p class="releasetime">上映时间：1998-04-03</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">5</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-6">6</i>
    <a href="/films/837" title="唐伯虎点秋香" class="image-link" data-act="boarditem-click" data-val="{movieId:837}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/da64660f82b98cdc1b8a3804e69609e041108.jpg@160w_220h_1e_1c" alt="唐伯虎点秋香" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/837" title="唐伯虎点秋香" data-act="boarditem-click" data-val="{movieId:837}">唐伯虎点秋香</a></p>
        <p class="star">
                主演：周星驰,巩俐,郑佩佩
        </p>
<p class="releasetime">上映时间：1993-07-01(中国香港)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">1</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-7">7</i>
    <a href="/films/2760" title="魂断蓝桥" class="image-link" data-act="boarditem-click" data-val="{movieId:2760}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/46c29a8b8d8424bdda7715e6fd779c66235684.jpg@160w_220h_1e_1c" alt="魂断蓝桥" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/2760" title="魂断蓝桥" data-act="boarditem-click" data-val="{movieId:2760}">魂断蓝桥</a></p>
        <p class="star">
                主演：费雯·丽,罗伯特·泰勒,露塞尔·沃特森
        </p>
<p class="releasetime">上映时间：1940-05-17(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">2</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-8">8</i>
    <a href="/films/7431" title="乱世佳人" class="image-link" data-act="boarditem-click" data-val="{movieId:7431}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/223c3e186db3ab4ea3bb14508c709400427933.jpg@160w_220h_1e_1c" alt="乱世佳人" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/7431" title="乱世佳人" data-act="boarditem-click" data-val="{movieId:7431}">乱世佳人</a></p>
        <p class="star">
                主演：费雯·丽,克拉克·盖博,奥利维娅·德哈维兰
        </p>
<p class="releasetime">上映时间：1939-12-15(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">1</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-9">9</i>
    <a href="/films/1228" title="天空之城" class="image-link" data-act="boarditem-click" data-val="{movieId:1228}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p1.meituan.net/movie/ba1ed511668402605ed369350ab779d6319397.jpg@160w_220h_1e_1c" alt="天空之城" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/1228" title="天空之城" data-act="boarditem-click" data-val="{movieId:1228}">天空之城</a></p>
        <p class="star">
                主演：寺田农,鹫尾真知子,龟山助清
        </p>
<p class="releasetime">上映时间：1992-05-01</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">0</i></p>        
    </div>

      </div>
    </div>

                </dd>
                <dd>
                        <i class="board-index board-index-10">10</i>
    <a href="/films/3667" title="辛德勒的名单" class="image-link" data-act="boarditem-click" data-val="{movieId:3667}">
      <img src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/image/loading_2.e3d934bf.png" alt="" class="poster-default" />
      <img data-src="https://p0.meituan.net/movie/b0d986a8bf89278afbb19f6abaef70f31206570.jpg@160w_220h_1e_1c" alt="辛德勒的名单" class="board-img" />
    </a>
    <div class="board-item-main">
      <div class="board-item-content">
              <div class="movie-item-info">
        <p class="name"><a href="/films/3667" title="辛德勒的名单" data-act="boarditem-click" data-val="{movieId:3667}">辛德勒的名单</a></p>
        <p class="star">
                主演：连姆·尼森,拉尔夫·费因斯,本·金斯利
        </p>
<p class="releasetime">上映时间：1993-12-15(美国)</p>    </div>
    <div class="movie-item-number score-num">
<p class="score"><i class="integer">9.</i><i class="fraction">2</i></p>        
    </div>

      </div>
    </div>

                </dd>
            </dl>

        </div>
            <div class="pager-main">
                
  
  <ul class="list-pager">



  
      <li class="active">
    <a class="page_1"
      href="javascript:void(0);" style="cursor: default"
  >1</a>

</li>
  <li >
    <a class="page_2"
      href="?offset=10"
  >2</a>

</li>
  <li >
    <a class="page_3"
      href="?offset=20"
  >3</a>

</li>
  <li >
    <a class="page_4"
      href="?offset=30"
  >4</a>

</li>
  <li >
    <a class="page_5"
      href="?offset=40"
  >5</a>

</li>

    <li class="sep">...</li>
      <li >
    <a class="page_10"
      href="?offset=90"
  >10</a>

</li>

  

<li>  <a class="page_2"
      href="?offset=10"
  >下一页</a>
</li>
</ul>


            </div>
    </div>
</div>

    </div>

<div class="footer">
  <p class="friendly-links">
    关于猫眼 :
    <a href="http://ir.maoyan.com/s/index.php#pageScroll0" target="_blank">关于我们</a>
    <span></span>
    <a href="http://ir.maoyan.com/s/index.php#pageScroll1" target="_blank">管理团队</a>
    <span></span>
    <a href="http://ir.maoyan.com/s/index.php#pageScroll2" target="_blank">投资者关系</a>
    &nbsp;&nbsp;&nbsp;&nbsp;
    友情链接 :
    <a href="http://www.meituan.com" data-query="utm_source=wwwmaoyan" target="_blank">美团网</a>
    <span></span>
    <a href="http://www.gewara.com" data-query="utm_source=wwwmaoyan">格瓦拉</a>
    <span></span>
    <a href="http://i.meituan.com/client" data-query="utm_source=wwwmaoyan" target="_blank">美团下载</a>
    <span></span>
    <a href="https://www.huanxi.com" data-query="utm_source=maoyan_pc" target="_blank">欢喜首映</a>
  </p>
  <p class="friendly-links">
    商务合作邮箱：v@maoyan.com
    客服电话：10105335
    违法和不良信息举报电话：4006018900
  </p>
  <p class="friendly-links">
    用户投诉邮箱：tousujubao@meituan.com
    舞弊线索举报邮箱：wubijubao@maoyan.com
  </p>
  <p class="friendly-links  credentials">
    <a href="/about/licence/1" target="_blank">中华人民共和国增值电信业务经营许可证 京B2-20190350</a>
    <span></span>
    <a href="/about/licence/4" target="_blank">营业性演出许可证 京演（机构）（2019）4094号</a>
  </p>
  <p class="friendly-links  credentials">
    <a href="/about/licence/3" target="_blank">广播电视节目制作经营许可证 （京）字第08478号</a>
    <span></span>
    <a href="/about/licence/2" target="_blank">网络文化经营许可证 京网文（2019）3837-369号 </a>
  </p>
  <p class="friendly-links  credentials">
    <a href="/rules/agreement" target="_blank">猫眼用户服务协议 </a>
    <span></span>
    <a href="/rules/rule" target="_blank">猫眼平台交易规则总则 </a>
    <span></span>
    <a href="/rules/privacy" target="_blank">隐私政策 </a>
  </p>
  <p class="friendly-links  credentials">
    <a href="http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010102003232" target="_blank">京公网安备
      11010102003232号</a>
  </p>
  <p>北京猫眼文化传媒有限公司</p>
  <p>
    &copy;2016
    猫眼电影 maoyan.com</p>
  <div class="certificate">
    <a href="http://sq.ccm.gov.cn:80/ccnt/sczr/service/business/emark/toDetail/350CF8BCA8416C4FE0530140A8C0957E"
      target="_blank">
      <img src="http://p0.meituan.net/moviemachine/e54374ccf134d1f7b2c5b075a74fca525326.png" />
    </a>
    <a href="/about/licence/5" target="_blank">
      <img src="http://p1.meituan.net/moviemachine/805f605d5cf1b1a02a4e3a5e29df003b8376.png" />
    </a>
  </div>
</div>

    <script crossorigin="anonymous" src="//www.dpfile.com/app/owl/static/owl_1.7.11.js"></script>
    <script>
      Owl.start({
        project: 'com.sankuai.movie.fe.mywww', 
        pageUrl: location.href.split('?')[0].replace(/\/\d+/g, '/:id'),
        devMode: false
      })
    </script>
    <!--[if IE 8]><script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/es5-shim.bbad933f.js"></script><![endif]-->
    <!--[if IE 8]><script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/es5-sham.d6ea26f4.js"></script><![endif]-->
    <script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/common.9fc677f9.js"></script>
<script crossorigin="anonymous" src="//s3plus.meituan.net/v1/mss_e2821d7f0cfe4ac1bf9202ecf9590e67/cdn-prod/file:5788b470/board-index.0cdf8e36.js"></script>
</body>
</html>

	</ul>
</div>
```

### 示例+练习

```python
from lxml import etree

html = '''
<div class="wrapper">
	<a href="/" id="channel">新浪社会</a>
	<ul id="nav">
		<li><a href="http://domestic.sina.com/" title="国内">国内</a></li>
		<li><a href="http://world.sina.com/" title="国际">国际</a></li>
		<li><a href="http://mil.sina.com/" title="军事">军事</a></li>
		<li><a href="http://photo.sina.com/" title="图片">图片</a></li>
		<li><a href="http://society.sina.com/" title="社会">社会</a></li>
		<li><a href="http://ent.sina.com/" title="娱乐">娱乐</a></li>
		<li><a href="http://tech.sina.com/" title="科技">科技</a></li>
		<li><a href="http://sports.sina.com/" title="体育">体育</a></li>
		<li><a href="http://finance.sina.com/" title="财经">财经</a></li>
		<li><a href="http://auto.sina.com/" title="汽车">汽车</a></li>
	</ul>
</div>'''
# 创建解析对象
parse_html = etree.HTML(html)
# 调用xpath返回结束,text()为文本内容
a_list = parse_html.xpath('//a/text()')
print(a_list)

# 提取所有的href的属性值
href_list = parse_html.xpath('//a/@href')
print(href)
# 提取所有href的值,不包括 / 
href_list = parse_html.xpath('//ul[@id="nav"]/li/a/@href')
print(href_list)
# 获取 图片、军事、...,不包括新浪社会
a_list = parse_html.xpath('//ul[@id="nav"]/li/a/text()')
for a in a_list:
  print(a)
```

### xpath最常使用方法

```python
1、先匹配节点对象列表
  # r_list: ['节点对象1','节点对象2']
  r_list = parse_html.xpath('基准xpath表达式')
2、遍历每个节点对象,利用节点对象继续调用 xpath
  for r in r_list:
        name = r.xpath('./xxxxxx')
        star = r.xpath('.//xxxxx')
        time = r.xpath('.//xxxxx')
```

## 链家二手房案例（xpath）

### 实现步骤

- 确定是否为静态

```python
打开二手房页面 -> 查看网页源码 -> 搜索关键字
```

- xpath表达式

```python
1、基准xpath表达式(匹配每个房源信息节点列表)
   此处滚动鼠标滑轮时,li节点的class属性值会发生变化,通过查看网页源码确定xpath表达式
  //ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]

2、依次遍历后每个房源信息xpath表达式
   * 名称: './/a[@data-el="region"]/text()'
   
   # 户型+面积+方位+是否精装
   info_list = './/div[@class="houseInfo"]/text()'  [0].strip().split('|')
   * 户型: info_list[1]
   * 面积: info_list[2]
   * 方位: info_list[3]
   * 精装: info_list[4]
   

   * 楼层: './/div[@class="positionInfo"]/text()'
   * 区域: './/div[@class="positionInfo"]/a/text()'
   * 总价: './/div[@class="totalPrice"]/span/text()'
   * 单价: './/div[@class="unitPrice"]/span/text()'
```

### 代码实现

```python
import requests
from lxml import etree
import time
import random
from useragents import ua_list

class LianjiaSpider(object):
  def __init__(self):
    self.url='https://bj.lianjia.com/ershoufang/pg{}/'
    self.blog = 1

  def get_html(self,url):
    headers = {'User-Agent':random.choice(ua_list)}
    # 尝试3次,否则换下一页地址
    if self.blog <= 3:
      try:
        res = requests.get(url=url,headers=headers,timeout=5)
        res.encoding = 'utf-8'
        html = res.text
        # 直接调用解析函数
        self.parse_page(html)
      except Exception as e:
        print('Retry')
        self.blog += 1
        self.get_html(url)


  def parse_page(self,html):
    parse_html = etree.HTML(html)
    # li_list: [<element li at xxx>,<element li at xxx>]
    li_list = parse_html.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
    item = {}
    for li in li_list:
      # 名称
      xpath_name = './/a[@data-el="region"]/text()'
      name_list = li.xpath(xpath_name)
      item['name'] = [
        name_list[0].strip() if name_list else None
      ][0]
      # 户型+面积+方位+是否精装
      info_xpath = './/div[@class="houseInfo"]/text()'
      info_list = li.xpath(info_xpath)
      if info_list:
        info_list = info_list[0].strip().split('|')
        if len(info_list) == 5:
          item['model'] = info_list[1].strip()
          item['area'] = info_list[2].strip()
          item['direction'] = info_list[3].strip()
          item['perfect'] = info_list[4].strip()
        else:
          item['model']=item['area']=item['direction']=item['perfect']=None
      else:
        item['model'] = item['area'] = item['direction'] = item['perfect'] = None

      # 楼层
      xpath_floor = './/div[@class="positionInfo"]/text()'
      floor_list = li.xpath(xpath_floor)
      item['floor'] = [
        floor_list[0].strip().split()[0] if floor_list else None
      ][0]

      # 地区
      xpath_address = './/div[@class="positionInfo"]/a/text()'
      address_list = li.xpath(xpath_address)
      item['address'] = [
        address_list[0].strip() if address_list else None
      ][0]
      # 总价
      xpath_total = './/div[@class="totalPrice"]/span/text()'
      total_list = li.xpath(xpath_total)
      item['total_price'] = [
        total_list[0].strip() if total_list else None
      ][0]
      # 单价
      xpath_unit = './/div[@class="unitPrice"]/span/text()'
      unit_list = li.xpath(xpath_unit)
      item['unit_price'] = [
        unit_list[0].strip() if unit_list else None
      ][0]

      print(item)

  def main(self):
    for pg in range(1,101):
      url = self.url.format(pg)
      self.get_html(url)
      time.sleep(random.randint(1,3))
      # 对self.blog进行一下初始化
      self.blog = 1


if __name__ == '__main__':
  start = time.time()
  spider = LianjiaSpider()
  spider.main()
  end = time.time()
  print('执行时间:%.2f' % (end-start))
```

## 作业1 - 猫眼电影数据抓取

**实现分析**

```python
1、基准xpath: 匹配所有电影信息的节点对象列表
    
    
2、遍历对象列表，依次获取每个电影信息
   for dd in dd_list:
	   电影名称 ： .//p[@class = 'name']/a/text()
	   电影主演 ：dd.xpath('.//p[@class="star"]/text()')[0].strip()
	   上映时间 ：dd.xpath('.//p[@class="releasetime"]/text()')[0].strip()[5:15]
```

## 作业2 - 百度贴吧图片抓取

### 目标思路

* 目标

```python
抓取指定贴吧所有图片
```

* 思路

```python
1、获取贴吧主页URL,下一页,找到不同页的URL规律
2、获取1页中所有帖子URL地址: [帖子链接1,帖子链接2,...]
3、对每个帖子链接发请求,获取图片URL
4、向图片的URL发请求,以wb方式写入本地文件
```

### 实现步骤

- 贴吧URL规律

```python
http://tieba.baidu.com/f?kw=??&pn=50
```

- xpath表达式

```python
1、帖子链接xpath
   //div[@class="t_con cleafix"]/div/div/div/a/@href
    
2、图片链接xpath
   //div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src
    
3、视频链接xpath
   //div[@class="video_src_wrapper"]/embed/@data-video
   # 注意: 此处视频链接前端对响应内容做了处理,需要查看网页源代码来查看，复制HTML代码在线格式化
```

## 作业3 - 电影天堂（xpath）

## 作业4 - 糗事百科（xpath）

```python
1、URL地址: https://www.qiushibaike.com/text/
2、目标 ：用户昵称、段子内容、好笑数量、评论数量
```

# **Day04**

## **Day03回顾**

### **目前反爬总结**

- **基于User-Agent反爬**

```python
1、发送请求携带请求头: headers={'User-Agent' : 'Mozilla/5.0 xxxxxx'}
2、多个请求随机切换User-Agent
   1、定义列表存放大量User-Agent，使用random.choice()每次随机选择
   2、定义py文件存放大量User-Agent，使用random.choice()每次随机选择
   3、使用fake_useragent模块每次访问随机生成User-Agent
    # sudo pip3 install fake_useraget
    
    * from fake_useragent import UserAgent
    * ua = UserAgent()
    * user_agent = ua.random
    * print(user_agent)
```

- **响应内容前端JS做处理反爬**

```python
1、html页面中可匹配出内容，程序中匹配结果为空
   * 响应内容中嵌入js，对页面结构做了一定调整导致，通过查看网页源代码，格式化输出查看结构，更改xpath或者正则测试
2、如果数据出不来可考虑更换 IE 的User-Agent尝试，数据返回最标准
```

### **请求模块总结**

- **urllib库使用流程**

```python
# 编码
params = {
    '':'',
    '':''
}
params = urllib.parse.urlencode(params)
url = baseurl + params

# 请求
request = urllib.request.Request(url,headers=headers)
response = urllib.request.urlopen(request)
html = response.read().decode('utf-8')
```

- **requests模块使用流程**

```python
baseurl = 'http://tieba.baidu.com/f?'
html = requests.get(url,headers=headers).content.decode('utf-8','ignore')
```

- **响应对象res属性**

```python
res.text ：字符串
res.content ：bytes
res.encoding：字符编码 res.encoding='utf-8'
res.status_code ：HTTP响应码
res.url ：实际数据URL地址
```

### **解析模块总结**

- **正则解析re模块**

```python
import re 

pattern = re.compile(r'正则表达式',re.S)
r_list = pattern.findall(html)
```

- **lxml解析库**

```python
from lxml import etree

parse_html = etree.HTML(res.text)
r_list = parse_html.xpath('xpath表达式')
```

### **xpath表达式**

- **匹配规则**

```python
1、节点对象列表
   # xpath示例: //div、//div[@class="student"]、//div/a[@title="stu"]/span
2、字符串列表
   # xpath表达式中末尾为: @src、@href、text()
```

- **xpath高级**

```python
1、基准xpath表达式: 得到节点对象列表
2、for r in [节点对象列表]:
       username = r.xpath('./xxxxxx')  

# 此处注意遍历后继续xpath一定要以:  . 开头，代表当前节点
```

**写程序注意**

```python
# 最终目标: 不要使你的程序因为任何异常而终止
1、页面请求设置超时时间,并用try捕捉异常,超过指定次数则更换下一个URL地址
2、所抓取任何数据,获取具体数据前先判断是否存在该数据,可使用列表推导式
# 多级页面数据抓取注意
1、主线函数: 解析一级页面函数(将所有数据从一级页面中解析并抓取)
```

### **增量爬虫如何实现**

```python
1、数据库中创建指纹表,用来存储每个请求的指纹
2、在抓取之前,先到指纹表中确认是否之前抓取过
```
  若果数据库中没有finger:
    开抓
### **Chrome浏览器安装插件**

- **安装方法**

```python
# 在线安装
1、下载插件 - google访问助手
2、安装插件 - google访问助手: Chrome浏览器-设置-更多工具-扩展程序-开发者模式-拖拽(解压后的插件)
3、在线安装其他插件 - 打开google访问助手 - google应用商店 - 搜索插件 - 添加即可

# 离线安装
1、下载插件 - xxx.crx 重命名为 xxx.zip
2、输入地址: chrome://extensions/   打开- 开发者模式
3、拖拽 插件(或者解压后文件夹) 到浏览器中
4、重启浏览器，使插件生效
```

## **Day04笔记**



### 链家二手房案例（xpath）

**实现步骤**

- 确定是否为静态

```python
打开二手房页面 -> 查看网页源码 -> 搜索关键字
```

- xpath表达式

```python
1、基准xpath表达式(匹配每个房源信息节点列表)
   此处滚动鼠标滑轮时,li节点的class属性值会发生变化,通过查看网页源码确定xpath表达式
  //ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]

2、依次遍历后每个房源信息xpath表达式
   * 名称: './/a[@data-el="region"]/text()'
   
   # 户型+面积+方位+是否精装
   info_list = './/div[@class="houseInfo"]/text()'  [0].strip().split('|')
   * 户型: info_list[1]
   * 面积: info_list[2]
   * 方位: info_list[3]
   * 精装: info_list[4]
   

   * 楼层: './/div[@class="positionInfo"]/text()'
   * 区域: './/div[@class="positionInfo"]/a/text()'
   * 总价: './/div[@class="totalPrice"]/span/text()'
   * 单价: './/div[@class="unitPrice"]/span/text()'
```

**代码实现**

```python
import requests
from lxml import etree
import time
import random
from useragents import ua_list

class LianjiaSpider(object):
  def __init__(self):
    self.url='https://bj.lianjia.com/ershoufang/pg{}/'
    self.blog = 1

  def get_html(self,url):
    headers = {'User-Agent':random.choice(ua_list)}
    # 尝试3次,否则换下一页地址
    if self.blog <= 3:
      try:
        res = requests.get(url=url,headers=headers,timeout=5)
        res.encoding = 'utf-8'
        html = res.text
        # 直接调用解析函数
        self.parse_page(html)
      except Exception as e:
        print('Retry')
        self.blog += 1
        self.get_html(url)


  def parse_page(self,html):
    parse_html = etree.HTML(html)
    # li_list: [<element li at xxx>,<element li at xxx>]
    li_list = parse_html.xpath('//ul[@class="sellListContent"]/li[@class="clear LOGVIEWDATA LOGCLICKDATA"]')
    item = {}
    for li in li_list:
      # 名称
      xpath_name = './/a[@data-el="region"]/text()'
      name_list = li.xpath(xpath_name)
      item['name'] = [
        name_list[0].strip() if name_list else None
      ][0]
      # 户型+面积+方位+是否精装
      info_xpath = './/div[@class="houseInfo"]/text()'
      info_list = li.xpath(info_xpath)
      if info_list:
        info_list = info_list[0].strip().split('|')
        if len(info_list) == 5:
          item['model'] = info_list[1].strip()
          item['area'] = info_list[2].strip()
          item['direction'] = info_list[3].strip()
          item['perfect'] = info_list[4].strip()
        else:
          item['model']=item['area']=item['direction']=item['perfect']=None
      else:
        item['model'] = item['area'] = item['direction'] = item['perfect'] = None

      # 楼层
      xpath_floor = './/div[@class="positionInfo"]/text()'
      floor_list = li.xpath(xpath_floor)
      item['floor'] = [
        floor_list[0].strip().split()[0] if floor_list else None
      ][0]

      # 地区
      xpath_address = './/div[@class="positionInfo"]/a/text()'
      address_list = li.xpath(xpath_address)
      item['address'] = [
        address_list[0].strip() if address_list else None
      ][0]
      # 总价
      xpath_total = './/div[@class="totalPrice"]/span/text()'
      total_list = li.xpath(xpath_total)
      item['total_price'] = [
        total_list[0].strip() if total_list else None
      ][0]
      # 单价
      xpath_unit = './/div[@class="unitPrice"]/span/text()'
      unit_list = li.xpath(xpath_unit)
      item['unit_price'] = [
        unit_list[0].strip() if unit_list else None
      ][0]

      print(item)

  def main(self):
    for pg in range(1,101):
      url = self.url.format(pg)
      self.get_html(url)
      time.sleep(random.randint(1,3))
      # 对self.blog进行一下初始化
      self.blog = 1


if __name__ == '__main__':
  start = time.time()
  spider = LianjiaSpider()
  spider.main()
  end = time.time()
  print('执行时间:%.2f' % (end-start))
```



### 百度贴吧图片抓取

**目标思路**

- 目标

```python
抓取指定贴吧所有图片
```

- 思路

```python
1、获取贴吧主页URL,下一页,找到不同页的URL规律
2、获取1页中所有帖子URL地址: [帖子链接1,帖子链接2,...]
3、对每个帖子链接发请求,获取图片URL
4、向图片的URL发请求,以wb方式写入本地文件
```

**实现步骤**

- 贴吧URL规律

```python
http://tieba.baidu.com/f?kw=??&pn=50
```

- xpath表达式

```python
1、帖子链接xpath
   //div[@class="t_con cleafix"]/div/div/div/a/@href
    
2、图片链接xpath
   //div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src
    
3、视频链接xpath
   //div[@class="video_src_wrapper"]/embed/@data-video
   # 注意: 此处视频链接前端对响应内容做了处理,需要查看网页源代码来查看，复制HTML代码在线格式化
```

**代码实现**

```python
import requests
from lxml import etree
import random
import time
from useragents import ua_list
from urllib import parse
import os

class BaiduImageSpider(object):
  def __init__(self):
    self.url = 'http://tieba.baidu.com/f?kw={}&pn={}'

  # 获取html功能函数
  def get_html(self,url):
    html = requests.get(
      url=url,
      headers={'User-Agent':'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; WOW64; Trident/4.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; InfoPath.3)'}
    ).content.decode('utf-8','ignore')
    return html

  # 解析html功能函数
  def xpath_func(self,html,xpath_bds):
    parse_html = etree.HTML(html)
    r_list = parse_html.xpath(xpath_bds)
    return r_list

  # 解析函数 - 实现最终图片抓取
  def parse_html(self,one_url):
    html = self.get_html(one_url)
    # 准备提取帖子链接:xpath_list ['/p/32323','','']
    xpath_bds = '//div[@class="t_con cleafix"]/div/div/div/a/@href'
    r_list = self.xpath_func(html,xpath_bds)
    for r in r_list:
      # 拼接帖子的URL地址
      t_url = 'http://tieba.baidu.com' + r
      # 把帖子中所有图片保存到本地
      self.get_image(t_url)
      # 爬完1个帖子中所有图片,休眠0-2秒钟
      time.sleep(random.uniform(0,2))

  # 功能:给定1个帖子URL,把帖子中所有图片保存到本地
  def get_image(self,t_url):
    html = self.get_html(t_url)
    # 图片链接的xpath表达式:img_list ['http://xxx.jpg','']
    # 使用xpath表达式的或| : 图片链接 + 视频链接
    xpath_bds = '//div[@class="d_post_content j_d_post_content  clearfix"]/img[@class="BDE_Image"]/@src | //div[@class="video_src_wrapper"]/embed/@data-video'
    img_list = self.xpath_func(html,xpath_bds)
    for img in img_list:
      html_bytes = requests.get(
        url=img,
        headers={'User-Agent':random.choice(ua_list)}
      ).content
      self.save_img(html_bytes,img)

  # 保存图片函数
  def save_img(self,html_bytes,img):
    filename = img[-10:]
    with open(filename,'wb') as f:
      f.write(html_bytes)
      print('%s下载成功' % filename)

  # 主函数
  def main(self):
    name = input('请输入贴吧名:')
    begin = int(input('请输入起始页:'))
    end = int(input('请输入终止页:'))

    # 对贴吧名进行编码
    kw = parse.quote(name)
    for page in range(begin,end+1):
      pn = (page-1)*50
      url = self.url.format(kw,pn)
      # 调用主线函数
      self.parse_html(url)

if __name__ == '__main__':
  spider = BaiduImageSpider()
  spider.main()
```

### **requests.get()参数**

#### 查询参数-params

- **参数类型**

```python
字典,字典中键值对作为查询参数
```

- **使用方法**

```python
1、res = requests.get(url,params=params,headers=headers)
2、特点: 
   * url为基准的url地址，不包含查询参数
   * 该方法会自动对params字典编码,然后和url拼接
```

- **示例**

```python
import requests

baseurl = 'http://tieba.baidu.com/f?'
params = {
  'kw' : '赵丽颖吧',
  'pn' : '50'
}
headers = {'User-Agent' : 'Mozilla/4.0'}
# 自动对params进行编码,然后自动和url进行拼接,去发请求
res = requests.get(url=baseurl,params=params,headers=headers)
res.encoding = 'utf-8'
print(res.text)
```

#### **Web客户端验证参数-auth**

- **作用及类型**

```python
1、针对于需要web客户端用户名密码认证的网站
2、auth = ('username','password')
```

- **达内code课程方向案例**

```python
# xpath表达式
//a/@href
# url 
http://code.tarena.com.cn/AIDCode/aid1904/14-redis/
```

思考：爬取具体的笔记文件？

```python
import os

# 保存在: /home/tarena/redis
# 先判断 /home/tarena/redis 是否存在
  1、不存在: 先创建目录,然后再保存 .zip
  2、存在:  直接保存 .zip
    
# 使用频率很高
if not os.path.exists('路径'):
      os.makedirs('路径')
```

**代码实现**

```python
import requests
from lxml import etree
import random
from useragents import ua_list
import os

class CodeSpider(object):
  def __init__(self):
    self.url = 'http://code.tarena.com.cn/AIDCode/aid1904/14-redis/'
    self.auth = ('tarenacode','code_2013')

  def get_headers(self):
      headers = {'User-Agent':random.choice(ua_list)}
      return headers

  def get_html(self,url):
      res = requests.get(url,headers=self.get_headers(),auth=self.auth)
      html = res.content
      return html

  def parse_html(self):
    # 获取响应内容
    html = self.get_html(self.url).decode()
    # 解析
    parse_html = etree.HTML(html)
    # r_list: ['../','day01/','redis-xxx.zip']
    r_list = parse_html.xpath('//a/@href')
    
    directory = '/home/tarena/myredis/'
    if not os.path.exists(directory):
      os.makedirs(directory)
      
    for r in r_list:
      if r.endswith('.zip') or r.endswith('.rar'):
        self.save_files(r,directory)

  def save_files(self,r,directory):
    # 拼接地址,把zip文件保存到指定目录
    url = self.url + r
    # filename: /home/tarena/AID/redis/xxx.zip
    filename = directory + r
    html = self.get_html(url)

    with open(filename,'wb') as f:
      f.write(html)
      print('%s下载成功' % r)


if __name__ == '__main__':
  spider = CodeSpider()
  spider.parse_html()
```

#### **SSL证书认证参数-verify**

- **适用网站及场景**

```python
1、适用网站: https类型网站但是没有经过 证书认证机构 认证的网站
2、适用场景: 抛出 SSLError 异常则考虑使用此参数
```

- **参数类型**

  ```python
  1、verify=True(默认)   : 检查证书认证
  2、verify=False（常用）: 忽略证书认证
  # 示例
  response = requests.get(
  	url=url,
  	params=params,
  	headers=headers,
  	verify=False
  )
  ```

#### **代理参数-proxies**

- **定义**

```python
1、定义: 代替你原来的IP地址去对接网络的IP地址。
2、作用: 隐藏自身真实IP,避免被封。
```

**普通代理**

- **获取代理IP网站**

```python
西刺代理、快代理、全网代理、代理精灵、... ...
```

- **参数类型**

```python
1、语法结构
   	proxies = {
       	'协议':'协议://IP:端口号'
   	}
2、示例
    proxies = {
    	'http':'http://IP:端口号',
    	'https':'https://IP:端口号'
	}
```

- **示例**

使用免费普通代理IP访问测试网站: http://httpbin.org/get

```python
import requests

url = 'http://httpbin.org/get'
headers = {
    'User-Agent':'Mozilla/5.0'
}
# 定义代理,在代理IP网站中查找免费代理IP
proxies = {
    'http':'http://112.85.164.220:9999',
    'https':'https://112.85.164.220:9999'
}
html = requests.get(url,proxies=proxies,headers=headers,timeout=5).text
print(html)
```

**思考: 建立一个自己的代理IP池，随时更新用来抓取网站数据**

```python
1、从西刺代理IP网站上,抓取免费代理IP
2、测试抓取的IP,可用的保存在文件中
```

**思考 - 代码实现**

```python
import requests
from lxml import etree
import time
import random
from fake_useragent import UserAgent

class GetProxyIP(object):
  def __init__(self):
    self.url = 'https://www.xicidaili.com/nn/{}'

  # 随机生成1个User-Agent
  def get_headers(self):
    ua = UserAgent()
    useragent = ua.random
    headers = {'User-Agent':useragent}
    return headers

  # 获取可用代理IP文件
  def get_ip_file(self,url):
    headers = self.get_headers()
    html = requests.get(url=url,headers=headers,timeout=5).text


    parse_html = etree.HTML(html)
    tr_list = parse_html.xpath('//tr')
    for tr in tr_list[1:]:
      ip = tr.xpath('./td[2]/text()')[0]
      port = tr.xpath('./td[3]/text()')[0]
      # 测试ip:port是否可用
      self.test_ip(ip,port)

  def test_ip(self,ip,port):
    proxies = {
      'http':'http://{}:{}'.format(ip,port),
      'https': 'https://{}:{}'.format(ip, port),
    }
    test_url = 'http://www.baidu.com/'
    try:
      res = requests.get(url = test_url,proxies = proxies,timeout = 8)
      if res.status_code == 200:
        print(ip,port,'Success')
        with open('proxies.txt','a') as f:
          f.write(ip + ':' + port + '\n')
    except Exception as e:
      print(ip,port,'Failed')

  # 主函数
  def main(self):
    for i in range(1,1001):
      url = self.url.format(i)
      self.get_ip_file(url)
      time.sleep(random.randint(5,10))

if __name__ == '__main__':
  spider = GetProxyIP()
  spider.main()
```

写一个获取收费开放代理的接口

```python
# 获取开放代理的接口
import requests

def test_ip(ip):
    url = 'http://www.baidu.com/'
    proxies = {     
        'http':'http://{}'.format(ip),
        'https':'https://{}'.format(ip),
    }
    
    try:
    	res = requests.get(url=url,proxies=proxies,timeout=8 )
    	if res.status_code == 200:
        	return True
    except Exception as e:
        return False

# 提取代理IP
def get_ip_list():
  api_url = 'http://dev.kdlapi.com/api/getproxy/?orderid=946562662041898&num=100&protocol=1&method=2&an_an=1&an_ha=1&sep=2'
  html = requests.get(api_url).content.decode('utf-8','ignore')
  # ip_port_list: ['IP:PORT','IP:PORT','']
  ip_port_list = html.split('\r\n')

  # 依次遍历代理IP,并进行测试
  for ip in ip_port_list:
    with open('proxy_ip.txt','a') as f:
    	if test_ip(ip):
            f.write(ip + '\n')

if __name__ == '__main__':
    get_ip_list()
```

**私密代理**

- **语法格式**

```python
1、语法结构
proxies = {
    '协议':'协议://用户名:密码@IP:端口号'
}

2、示例
proxies = {
	'http':'http://用户名:密码@IP:端口号',
  'https':'https://用户名:密码@IP:端口号'
}
```

**示例代码**

```python
import requests
url = 'http://httpbin.org/get'
proxies = {
    'http': 'http://309435365:szayclhp@106.75.71.140:16816',
    'https':'https://309435365:szayclhp@106.75.71.140:16816',
}
headers = {
    'User-Agent' : 'Mozilla/5.0',
}

html = requests.get(url,proxies=proxies,headers=headers,timeout=5).text
print(html)
```

## **今日作业**

```python
1、总结前几天内容,理顺知识点
2、代理参数 - 如何建立自己的IP代理池,并使用随机代理IP访问网站
3、Web客户端验证 - 如何下载、保存
```

# DAY06

## Day05回顾

### 控制台抓包

打开方式及常用选项

```python
1、打开浏览器，F12打开控制台，找到Network选项卡
2、控制台常用选项
   1、Network: 抓取网络数据包
        1、ALL: 抓取所有的网络数据包
        2、XHR：抓取异步加载的网络数据包
        3、JS : 抓取所有的JS文件 
   2、Sources: 格式化输出并打断点调试JavaScript代码，助于分析爬虫中一些参数
   3、Console: 交互模式，可对JavaScript中的代码进行测试
3、抓取具体网络数据包后
   1、单击左侧网络数据包地址，进入数据包详情，查看右侧
   2、右侧:
       1、Headers: 整个请求信息
            General、Response Headers、Request Headers、Query String、Form Data
       2、Preview: 对响应内容进行预览
       3、Response：响应内容
```

### 有道翻译过程梳理

```python
1. 打开首页
2. 准备抓包: F12开启控制台
  3. 寻找地址
  页面中输入翻译单词，控制台中抓取到网络数据包，查找并分析返回翻译数据的地址
  4. 发现规律
  找到返回具体数据的地址，在页面中多输入几个单词，找到对应URL地址，分析对比 Network - All(或者XHR) - Form Data，发现对应的规律
  5. 寻找JS文件
  右上角 ... -> Search -> 搜索关键字 -> 单击 -> 跳转到Sources，左下角格式化符号{}
  6、查看JS代码
  搜索关键字，找到相关加密方法
  7、断点调试
  8、完善程序
```

### 增量爬取思路

```python
1、将爬取过的地址存放到数据库中
2、程序爬取时先到数据库中查询比对，如果已经爬过则不会继续爬取
```

### 动态加载网站数据抓取

```python
1、F12打开控制台，页面动作抓取网络数据包
2、抓取json文件URL地址
# 控制台中 XHR ：异步加载的数据包
# XHR -> Query String Parameters(查询参数)
```

### **数据抓取最终梳理**

```python
# 响应内容中存在
1、确认抓取数据在响应内容中是否存在
2、分析页面结构，观察URL地址规律
   1、大体查看响应内容结构,查看是否有更改 -- (百度视频案例)
   2、查看页面跳转时URL地址变化,查看是否新跳转 -- (民政部案例)
3、开始码代码进行数据抓取

# 响应内容中不存在
1、确认抓取数据在响应内容中是否存在
2、F12抓包,开始刷新页面或执行某些行为,主要查看XHR异步加载数据包
   1、GET请求: Request Headers、Query String Paramters
   2、POST请求:Request Headers、FormData
3、观察查询参数或者Form表单数据规律,如果需要进行进一步抓包分析处理
   1、比如有道翻译的 salt+sign,抓取并分析JS做进一步处理
   2、此处注意请求头中的cookie和referer以及User-Agent
4、使用res.json()获取数据,利用列表或者字典的方法获取所需数据
```



## **Day06笔记**

### 豆瓣电影数据抓取案例

- **目标**

```python
1、地址: 豆瓣电影 - 排行榜 - 剧情
2、目标: 电影名称、电影评分
```

- **F12抓包（XHR）**

```python
1、Request URL(基准URL地址) ：https://movie.douban.com/j/chart/top_list?
2、Query String(查询参数)

# 抓取的查询参数如下：
type: 13 # 电影类型
interval_id: 100:90
action: ''
start: 0  # 每次加载电影的起始索引值 0 20 40 60 
limit: 20 # 每次加载的电影数量
```

- **代码实现 - 全站抓取 - 完美接口 - 指定类型所有电影信息**

```python
import requests
import time
import random
import re
from useragents import ua_list

class DoubanSpider(object):
    def __init__(self):
        self.url = 'https://movie.douban.com/j/chart/top_list?'
        self.i = 0

    # 获取随机headers
    def get_headers(self):
        headers = {'User-Agent':random.choice(ua_list)}

        return headers

    # 获取页面
    def get_page(self,params):
        headers = self.get_headers()
        res = requests.get(url=self.url,params=params,headers=headers)
        res.encoding = 'utf-8'
        # 返回 python 数据类型
        html = res.json()
        self.parse_page(html)

    # 解析并保存数据
    def parse_page(self,html):
        item = {}
        # html为大列表 [{电影1信息},{},{}]
        for one in html:
            # 名称 + 评分
            item['name'] = one['title'].strip()
            item['score'] = float(one['score'].strip())
            # 打印测试
            print(item)
            self.i += 1

    # 获取电影总数
    def total_number(self,type_number):
        # F12抓包抓到的地址
        url = 'https://movie.douban.com/j/chart/top_list_count?type={}&interval_id=100%3A90'.format(type_number)
        headers = self.get_headers()
        html = requests.get(url=url,headers=headers).json()
        total = int(html['total'])

        return total

    # 获取所有电影的名字和对应type值
    def get_all_type_films(self):
        # 获取 类型和类型码
        url = 'https://movie.douban.com/chart'
        headers = self.get_headers()
        html = requests.get(url=url,headers=headers).text
        re_bds = r'<a href=.*?type_name=(.*?)&type=(.*?)&.*?</a>'
        pattern = re.compile(re_bds,re.S)
        r_list = pattern.findall(html)
        # 存放所有类型和对应类型码大字典
        type_dict = {}
        menu = ''
        for r in r_list:
            type_dict[r[0].strip()] = r[1].strip()
            # 获取input的菜单，显示所有电影类型
            menu += r[0].strip() + '|'

        return type_dict,menu


    # 主函数
    def main(self):
        # 获取type的值
        type_dict,menu = self.get_all_type_films()
        menu = menu + '\n请做出你的选择:'
        name = input(menu)
        type_number = type_dict[name]
        # 获取电影总数
        total = self.total_number(type_number)
        for start in range(0,(total+1),20):
            params = {
                'type' : type_number,
                'interval_id' : '100:90',
                'action' : '',
                'start' : str(start),
                'limit' : '20'
            }
            # 调用函数,传递params参数
            self.get_page(params)
            # 随机休眠1-3秒
            time.sleep(random.randint(1,3))
        print('电影数量:',self.i)

if __name__ == '__main__':
    spider = DoubanSpider()
    spider.main()
```

### 腾讯招聘数据抓取

- **确定URL地址及目标**

```python
1、URL: 百度搜索腾讯招聘 - 查看工作岗位
2、目标: 职位名称、工作职责、岗位要求
```

- **要求与分析**

```python
1、通过查看网页源码,得知所需数据均为 Ajax 动态加载
2、通过F12抓取网络数据包,进行分析
3、一级页面抓取数据: 职位名称
4、二级页面抓取数据: 工作职责、岗位要求
```

- **一级页面json地址(index在变,timestamp未检查)**

```python
https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1563912271089&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn
```

- **二级页面地址(postId在变,在一级页面中可拿到)**

```python
https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1563912374645&postId={}&language=zh-cn
```

- **代码实现**

```python
import requests
import json
import time
import random
from useragents import ua_list

class TencentSpider(object):
  def __init__(self):
    self.one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1563912271089&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    self.two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1563912374645&postId={}&language=zh-cn'
    # 打开文件
    self.f = open('tencent.json','a')
    # 存放抓取的item字典数据
    self.item_list = []

  # 获取响应内容函数
  def get_page(self,url):
    headers = {'User-Agent':random.choice(ua_list)}
    html = requests.get(url=url,headers=headers).text
    # json格式字符串 -> Python
    html = json.loads(html)

    return html

  # 主线函数: 获取所有数据
  def parse_page(self,one_url):
    html = self.get_page(one_url)
    item = {}
    for job in html['Data']['Posts']:
      # postId
      post_id = job['PostId']
      # 拼接二级地址,获取职责和要求
      two_url = self.two_url.format(post_id)
      item['name'],item['duty'],item['require'] = self.parse_two_page(two_url)

      print(item)
      # 添加到大列表中
      self.item_list.append(item)

  # 解析二级页面函数
  def parse_two_page(self,two_url):
    html = self.get_page(two_url)
    # 职位名称
    name = html['Data']['RecruitPostName']
    # 用replace处理一下特殊字符
    duty = html['Data']['Responsibility']
    duty = duty.replace('\r\n','').replace('\n','')
    # 处理要求
    require = html['Data']['Requirement']
    require = require.replace('\r\n','').replace('\n','')

    return name,duty,require

  # 获取总页数
  def get_numbers(self):
    url = self.one_url.format(1)
    html = self.get_page(url)
    numbers = int(html['Data']['Count']) // 10 + 1

    return numbers

  def main(self):
    number = self.get_numbers()
    for page in range(1,3):
      one_url = self.one_url.format(page)
      self.parse_page(one_url)

    # 保存到本地json文件:json.dump
    json.dump(self.item_list,self.f,ensure_ascii=False)
    self.f.close()

if __name__ == '__main__':
  spider = TencentSpider()
  spider.main()
```

### 多线程爬虫

**应用场景**

```python
1、多进程 ：CPU密集程序
2、多线程 ：爬虫(网络I/O)、本地磁盘I/O
```

**知识点回顾**

- **队列**

```python
# 导入模块
from queue import Queue
# 使用
q = Queue()
q.put(url)
q.get() # 当队列为空时，阻塞
q.empty() # 判断队列是否为空，True/False

q.get(block = False) # 队列为空时,抛异常


python GIL 作用: 解决多线程对共享资源的争夺


```



- **线程模块**

```python
# 导入模块
from threading import Thread

# 使用流程  
t = Thread(target=函数名) # 创建线程对象
t.start() # 创建并启动线程
t.join()  # 阻塞等待回收线程

# 如何创建多线程
t_list = []

for i in range(5):
    t = Thread(target=函数名)
    t_list.append(t)
    t.start()

for t in t_list:
    t.join()
```

### 小米应用商店抓取(多线程)

**目标**

```python
1、网址 ：百度搜 - 小米应用商店，进入官网
2、目标 ：所有应用分类
   应用名称
   应用链接
```

**实现步骤**

- **1、确认是否为动态加载**

```python
1、页面局部刷新
2、右键查看网页源代码，搜索关键字未搜到
# 此网站为动态加载网站，需要抓取网络数据包分析
```

- **2、F12抓取网络数据包**

```python
1、抓取返回json数据的URL地址（Headers中的Request URL）
   http://app.mi.com/categotyAllListApi?page={}&categoryId=2&pageSize=30
        
2、查看并分析查询参数（headers中的Query String Parameters）
   page: 1
   categoryId: 2
   pageSize: 30
   # 只有page在变，0 1 2 3 ... ... ，这样我们就可以通过控制page的值拼接多个返回json数据的URL地址
```

- **将抓取数据保存到csv文件**

```python
# 注意多线程写入的线程锁问题
from threading import Lock
lock = Lock()
# 加锁
lock.acquire()
python语句
# 释放锁
lock.release()
```

- **整体思路**

```python
1、在 __init__(self) 中创建文件对象，多线程操作此对象进行文件写入
  self.f = open('xiaomi.csv','a',newline='')
  self.writer = csv.writer(self.f)
  self.lock = Lock()
2、每个线程抓取1页数据后将数据进行文件写入，写入文件时需要加锁
  def parse_html(self):
    app_list = []
    for xxx in xxx:
        app_list.append([name,link,typ])
    self.lock.acquire()
    self.wirter.writerows(app_list)
    self.lock.release()
3、所有数据抓取完成关闭文件
  def main(self):
    self.f.close()
```

- **代码实现**

```python
import requests
from threading import Thread
from queue import Queue
import time
from useragents import ua_list
from lxml import etree
import csv
from threading import Lock
import random

class XiaomiSpider(object):
  def __init__(self):
    self.url = 'http://app.mi.com/categotyAllListApi?page={}&categoryId={}&pageSize=30'
    # 存放所有URL地址的队列
    self.q = Queue()
    self.i = 0
    # 存放所有类型id的空列表
    self.id_list = []
    # 打开文件
    self.f = open('xiaomi.csv','a')
    self.writer = csv.writer(self.f)
    # 创建锁
    self.lock = Lock()


  def get_cateid(self):
    # 请求
    url = 'http://app.mi.com/'
    headers = { 'User-Agent': random.choice(ua_list)}
    html = requests.get(url=url,headers=headers).text
    # 解析
    parse_html = etree.HTML(html)
    xpath_bds = '//ul[@class="category-list"]/li'
    li_list = parse_html.xpath(xpath_bds)
    for li in li_list:
      typ_name = li.xpath('./a/text()')[0]
      typ_id = li.xpath('./a/@href')[0].split('/')[-1]
      # 计算每个类型的页数
      pages = self.get_pages(typ_id)
      self.id_list.append( (typ_id,pages) )

    # 入队列
    self.url_in()

  # 获取counts的值并计算页数
  def get_pages(self,typ_id):
    # 每页返回的json数据中,都有count这个key
    url = self.url.format(0,typ_id)
    html = requests.get(
      url=url,
      headers={'User-Agent':random.choice(ua_list)}
    ).json()
    count = html['count']
    pages = int(count) // 30 + 1

    return pages

  # url入队列
  def url_in(self):
    for id in self.id_list:
      # id为元组,('2',pages)
      for page in range(1,id[1]+1):
        url = self.url.format(page,id[0])
        # 把URL地址入队列
        self.q.put(url)

  # 线程事件函数: get() - 请求 - 解析 - 处理数据
  def get_data(self):
    while True:
      if not self.q.empty():
        url = self.q.get()
        headers = {'User-Agent':random.choice(ua_list)}
        html = requests.get(url=url,headers=headers).json()
        self.parse_html(html)
      else:
        break

  # 解析函数
  def parse_html(self,html):
    # 存放1页的数据 - 写入到csv文件
    app_list = []

    for app in html['data']:
      # 应用名称 + 链接 + 分类
      name = app['displayName']
      link = 'http://app.mi.com/details?id=' + app['packageName']
      typ_name = app['level1CategoryName']
      # 把每一条数据放到app_list中,目的为了 writerows()
      app_list.append([name,typ_name,link])

      print(name,typ_name)
      self.i += 1

    # 开始写入1页数据 - app_list
    self.lock.acquire()
    self.writer.writerows(app_list)
    self.lock.release()

  # 主函数
  def main(self):
    # URL入队列
    self.get_cateid()
    t_list = []
    # 创建多个线程
    for i in range(1):
      t = Thread(target=self.get_data)
      t_list.append(t)
      t.start()

    # 回收线程
    for t in t_list:
      t.join()

    # 关闭文件
    self.f.close()
    print('数量:',self.i)

if __name__ == '__main__':
  start = time.time()
  spider = XiaomiSpider()
  spider.main()
  end = time.time()
  print('执行时间:%.2f' % (end-start))
```

### cookie模拟登录

**适用网站及场景**

```python
抓取需要登录才能访问的页面
```

**cookie和session机制**

```python
# http协议为无连接协议
cookie: 存放在客户端浏览器
session: 存放在Web服务器
```

### 人人网登录案例

* **方法一 - 登录网站手动抓取Cookie**

```python
1、先登录成功1次,获取到携带登录信息的Cookie
   登录成功 - 个人主页 - F12抓包 - 刷新个人主页 - 找到主页的包(profile)
2、携带着cookie发请求
   ** Cookie
   ** User-Agent
```

```python
# 1、将self.url改为 个人主页的URL地址
# 2、将Cookie的值改为 登录成功的Cookie值
import requests
from lxml import etree

class RenrenLogin(object):
  def __init__(self):
    self.url = 'xxxxxxx'
    self.headers = {
      'Cookie':'xxxxxx',
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }

  def get_html(self):
    html = requests.get(url=self.url,headers=self.headers).text
    self.parse_html(html)

  def parse_html(self,html):
    parse_html = etree.HTML(html)
    r_list = parse_html.xpath('//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()')
    print(r_list)

if __name__ == '__main__':
  spider = RenrenLogin()
  spider.get_html()
```

- **方法二 - requests模块处理Cookie**

原理思路及实现

```python
# 1. 思路
requests模块提供了session类,来实现客户端和服务端的会话保持

# 2. 原理
1、实例化session对象
   session = requests.session()
2、让session对象发送get或者post请求
   res = session.post(url=url,data=data,headers=headers)
> cookie 保存在session对象中,可以做会话保持
   res = session.get(url=url,headers=headers)

# 3. 思路梳理
浏览器原理: 访问需要登录的页面会带着之前登录过的cookie
程序原理: 同样带着之前登录的cookie去访问 - 由session对象完成
1、实例化session对象
2、登录网站: session对象发送请求,登录对应网站,把cookie保存在session对象中
3、访问页面: session对象请求需要登录才能访问的页面,session能够自动携带之前的这个cookie,进行请求
```

具体步骤

```python
1、寻找Form表单提交地址 - 寻找登录时POST的地址
   查看网页源码,查看form表单,找action对应的地址: http://www.renren.com/PLogin.do

2、发送用户名和密码信息到POST的地址
   * 用户名和密码信息以什么方式发送？ -- 字典
     键 ：<input>标签中name的值(email,password)
     值 ：真实的用户名和密码
     post_data = {'email':'','password':''}

session = requests.session()        
session.post(url=url,data=data)
```

程序实现

```python
# 把Formdata中的 email 和 password 的改为自己真实的用户名和密码
import requests
from lxml import etree

class RenrenSpider(object):
  def __init__(self):
    self.post_url = 'http://www.renren.com/PLogin.do'
    self.get_url = 'http://www.renren.com/967469305/profile'
    # 实例化session对象
    self.session = requests.session()

  def get_html(self):
    # email和password为<input>节点中name的属性值
    form_data = {
      'email' : 'xxxx',
      'password' : 'xxxx'
    }
    # 先session.post()
    self.session.post(url=self.post_url,data=form_data)
    # 再session.get()
    html = self.session.get(url=self.get_url).text
    self.parse_html(html)

  def parse_html(self,html):
    parse_html = etree.HTML(html)
    r_list = parse_html.xpath('//li[@class="school"]/span/text()')
    print(r_list)

if __name__ == '__main__':
  spider = RenrenSpider()
  spider.get_html()
```

* **方法三**

原理

```python
1、把抓取到的cookie处理为字典
2、使用requests.get()中的参数:cookies
```

处理cookie为字典

```python
# 处理cookies为字典
cookies_dict = {}
cookies = 'xxxx'
for kv in cookies.split('; ')
  cookies_dict[kv.split('=')[0]] = kv.split('=')[1]
```

代码实现

```python
import requests
from lxml import etree

class RenrenLogin(object):
  def __init__(self):
    self.url = 'http://www.renren.com/967469305/profile'
    self.headers = {
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }

  # 获取字典形式cookie的函数
  def get_cookie_dict(self):
    cookie_dict = {}
    cookies = 'anonymid=jy87mc5fx4xvjj; _r01_=1; jebe_key=a04238bc-adc0-4418-a770-519d74219f15%7C2e9beece3ead42fe6a26739d515f14df%7C1563911475551%7C1%7C1563911475689; ln_uact=13603263409; depovince=GW; jebecookies=3720f008-2502-4422-acfe-8b78b4c3611d|||||; JSESSIONID=abcUijruA6U375Qz-tHZw; ick_login=60cb66a4-e407-4fd5-a2ee-1eae3220a102; _de=4DBCFCC17D9E50C8C92BCDC45CC5C3B7; p=415429a0f0b3067e9061fd8387c269c45; first_login_flag=1; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20190815/1435/main_91u0_81d40000ca0d1986.jpg; t=da27ae8094836b90d439e88e21ed73ac5; societyguester=da27ae8094836b90d439e88e21ed73ac5; id=967469305; xnsid=1eafd54d; ver=7.0; loginfrom=null; jebe_key=a04238bc-adc0-4418-a770-519d74219f15%7C2012cb2155debcd0710a4bf5a73220e8%7C1567148226573%7C1%7C1567148227902; wp_fold=0'
    for kv in cookies.split('; '):
      # kv: 'td_cookie=184xxx'
      key = kv.split('=')[0]
      value = kv.split('=')[1]
      cookie_dict[key] = value

    return cookie_dict

  def get_html(self):
    # 获取cookies
    cookies = self.get_cookie_dict()
    html = requests.get(
      url=self.url,
      headers=self.headers,
      cookies=cookies,
    ).text
    self.parse_html(html)

  def parse_html(self,html):
    parse_html = etree.HTML(html)
    r_list = parse_html.xpath('//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()')
    print(r_list)

if __name__ == '__main__':
  spider = RenrenLogin()
  spider.get_html()
```

### json解析模块

#### json.loads(json)

* **作用**

```python
把json格式的字符串转为Python数据类型
```

* **示例**

```python
html_json = json.loads(res.text)
```

#### json.dumps(python)

* **作用**

```python
把 python 类型 转为 json 类型
```

* **示例**

```python
import json

# json.dumps()之前
item = {'name':'QQ','app_id':1}
print('before dumps',type(item)) # dict
# json.dumps之后
item = json.dumps(item)
print('after dumps',type(item)) # str
```

#### json.load(f)

**作用**

```python
将json文件读取,并转为python类型
```

示例

```python
import json

with open('D:\\spider_test\\xiaomi.json','r') as f:
    data = json.load(f)
    
print(data)
```

#### json.dump(python,f,ensure_ascii=False)

* **作用**

```python
把python数据类型 转为 json格式的字符串
# 一般让你把抓取的数据保存为json文件时使用
```

* **参数说明**

```python
第1个参数: python类型的数据(字典，列表等)
第2个参数: 文件对象
第3个参数: ensure_ascii=False # 序列化时编码
```

* **示例1**

```python
import json

item = {'name':'QQ','app_id':1}
with open('小米.json','a') as f:
  json.dump(item,f,ensure_ascii=False)
```

* **示例2**

```python
import json

item_list = []
for i in range(3):
  item = {'name':'QQ','id':i}
  item_list.append(item)
    
with open('xiaomi.json','a') as f:
	json.dump(item_list,f,ensure_ascii=False)
```

练习: 将腾讯招聘数据存入到json文件

#### json模块总结

```python
# 爬虫最常用
1、数据抓取 - json.loads(html)
   将响应内容由: json 转为 python
2、数据保存 - json.dump(item_list,f,ensure_ascii=False)
   将抓取的数据保存到本地 json文件

# 抓取数据一般处理方式
1、txt文件
2、csv文件
3、json文件
4、MySQL数据库
5、MongoDB数据库
6、Redis数据库
```

## 今日作业

```python
1、多线程改写 - 腾讯招聘案例
2、多线程改写 - 链家二手房案例
3、尝试破解百度翻译
```



# DAY07

## Day06回顾

### **多线程爬虫**

- **思路**

```python
1、将待爬取的URL地址存放到队列中
2、多个线程从队列中获取地址,进行数据抓取
3、注意获取地址过程中程序阻塞问题
   while True:
      if not q.empty():
         url = q.get()
         ... ... 
      else:
        break 
```

- **将抓取数据保存到同一文件**

```python
# 注意多线程写入的线程锁问题
from threading import Lock
lock = Lock()
lock.acquire()
python代码块
lock.release()
```

- **代码实现思路**

```python
# 1、在 __init__(self) 中创建文件对象，多线程操作此对象进行文件写入
  self.f = open('xiaomi.csv','a',newline='')
  self.writer = csv.writer(self.f)
  self.lock = Lock()
# 2、每个线程抓取1页数据后将数据进行文件写入，写入文件时需要加锁
  def parse_html(self):
    app_list = []
    for xxx in xxx:
        app_list.append([name,link,typ])
    self.lock.acquire()
    self.wirter.writerows(app_list)
    self.lock.release()
# 3、所有数据抓取完成关闭文件
  def main(self):
    self.f.close()
```

### **解析模块汇总**

**re、lxml+xpath、json**

```python
# re
import re
pattern = re.compile(r'',re.S)
r_list = pattern.findall(html)

# lxml+xpath
from lxml import etree
parse_html = etree.HTML(html)
r_list = parse_html.xpath('')

# json
# 响应内容由json转为python
html = json.loads(res.text) 
# 所抓数据保存到json文件
with open('xxx.json','a') as f:
  json.dump(item_list,f,ensure_ascii=False)

# 或
f = open('xxx.json','a')
json.dump(item_list,f,ensure_ascii=False)
f.close()
```

## **Day07笔记**

### cookie模拟登录

**适用网站及场景**

```python
抓取需要登录才能访问的页面
```

**cookie和session机制**

```python
# http协议为无连接协议
cookie: 存放在客户端浏览器
session: 存放在Web服务器
```

### 人人网登录案例

* **方法一 - 登录网站手动抓取Cookie**

```python
1、先登录成功1次,获取到携带登录信息的Cookie
   登录成功 - 个人主页 - F12抓包 - 刷新个人主页 - 找到主页的包(profile)
2、携带着cookie发请求
   ** Cookie
   ** User-Agent
```

```python
# 1、将self.url改为 个人主页的URL地址
# 2、将Cookie的值改为 登录成功的Cookie值
import requests
from lxml import etree

class RenrenLogin(object):
  def __init__(self):
    self.url = 'xxxxxxx'
    self.headers = {
      'Cookie':'xxxxxx',
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }

  def get_html(self):
    html = requests.get(url=self.url,headers=self.headers).text
    self.parse_html(html)

  def parse_html(self,html):
    parse_html = etree.HTML(html)
    r_list = parse_html.xpath('//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()')
    print(r_list)

if __name__ == '__main__':
  spider = RenrenLogin()
  spider.get_html()
```

- **方法二 - requests模块处理Cookie**

原理思路及实现

```python
# 1. 思路
requests模块提供了session类,来实现客户端和服务端的会话保持

# 2. 原理
1、实例化session对象
   session = requests.session()
2、让session对象发送get或者post请求
   res = session.post(url=url,data=data,headers=headers)
   res = session.get(url=url,headers=headers)

# 3. 思路梳理
浏览器原理: 访问需要登录的页面会带着之前登录过的cookie
程序原理: 同样带着之前登录的cookie去访问 - 由session对象完成
1、实例化session对象
2、登录网站: session对象发送请求,登录对应网站,把cookie保存在session对象中
3、访问页面: session对象请求需要登录才能访问的页面,session能够自动携带之前的这个cookie,进行请求
```

具体步骤

```python
1、寻找Form表单提交地址 - 寻找登录时POST的地址
   查看网页源码,查看form表单,找action对应的地址: http://www.renren.com/PLogin.do

2、发送用户名和密码信息到POST的地址
   * 用户名和密码信息以什么方式发送？ -- 字典
     键 ：<input>标签中name的值(email,password)
     值 ：真实的用户名和密码
     post_data = {'email':'','password':''}

session = requests.session()        
session.post(url=url,data=data)
```

程序实现

```python
# 把Formdata中的 email 和 password 的改为自己真实的用户名和密码
import requests
from lxml import etree

class RenrenSpider(object):
  def __init__(self):
    self.post_url = 'http://www.renren.com/PLogin.do'
    self.get_url = 'http://www.renren.com/967469305/profile'
    # 实例化session对象
    self.session = requests.session()

  def get_html(self):
    # email和password为<input>节点中name的属性值
    form_data = {
      'email' : 'xxxx',
      'password' : 'xxxx'
    }
    # 先session.post()
    self.session.post(url=self.post_url,data=form_data)
    # 再session.get()
    html = self.session.get(url=self.get_url).text
    self.parse_html(html)

  def parse_html(self,html):
    parse_html = etree.HTML(html)
    r_list = parse_html.xpath('//li[@class="school"]/span/text()')
    print(r_list)

if __name__ == '__main__':
  spider = RenrenSpider()
  spider.get_html()
```

* **方法三**

原理

```python
1、把抓取到的cookie处理为字典
2、使用requests.get()中的参数:cookies
```

处理cookie为字典

```python
# 处理cookies为字典
cookies_dict = {}
cookies = 'xxxx'
for kv in cookies.split('; ')
  cookies_dict[kv.split('=')[0]] = kv.split('=')[1]
```

代码实现

```python
import requests
from lxml import etree

class RenrenLogin(object):
  def __init__(self):
    self.url = 'http://www.renren.com/967469305/profile'
    self.headers = {
      'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36'
    }

  # 获取字典形式cookie的函数
  def get_cookie_dict(self):
    cookie_dict = {}
    cookies = 'anonymid=jy87mc5fx4xvjj; _r01_=1; jebe_key=a04238bc-adc0-4418-a770-519d74219f15%7C2e9beece3ead42fe6a26739d515f14df%7C1563911475551%7C1%7C1563911475689; ln_uact=13603263409; depovince=GW; jebecookies=3720f008-2502-4422-acfe-8b78b4c3611d|||||; JSESSIONID=abcUijruA6U375Qz-tHZw; ick_login=60cb66a4-e407-4fd5-a2ee-1eae3220a102; _de=4DBCFCC17D9E50C8C92BCDC45CC5C3B7; p=415429a0f0b3067e9061fd8387c269c45; first_login_flag=1; ln_hurl=http://hdn.xnimg.cn/photos/hdn421/20190815/1435/main_91u0_81d40000ca0d1986.jpg; t=da27ae8094836b90d439e88e21ed73ac5; societyguester=da27ae8094836b90d439e88e21ed73ac5; id=967469305; xnsid=1eafd54d; ver=7.0; loginfrom=null; jebe_key=a04238bc-adc0-4418-a770-519d74219f15%7C2012cb2155debcd0710a4bf5a73220e8%7C1567148226573%7C1%7C1567148227902; wp_fold=0'
    for kv in cookies.split('; '):
      # kv: 'td_cookie=184xxx'
      key = kv.split('=')[0]
      value = kv.split('=')[1]
      cookie_dict[key] = value

    return cookie_dict

  def get_html(self):
    # 获取cookies
    cookies = self.get_cookie_dict()
    html = requests.get(
      url=self.url,
      headers=self.headers,
      cookies=cookies,
    ).text
    self.parse_html(html)

  def parse_html(self,html):
    parse_html = etree.HTML(html)
    r_list = parse_html.xpath('//*[@id="operate_area"]/div[1]/ul/li[1]/span/text()')
    print(r_list)

if __name__ == '__main__':
  spider = RenrenLogin()
  spider.get_html()
```

### **json解析模块**

**json.loads(json)**

* **作用**

```python
把json格式的字符串转为Python数据类型
```

* **示例**

```python
html_json = json.loads(res.text)
```

**json.dumps(python)**

* **作用**

```python
把 python 类型 转为 json 类型
```

* **示例**

```python
import json

# json.dumps()之前
item = {'name':'QQ','app_id':1}
print('before dumps',type(item)) # dict
# json.dumps之后
item = json.dumps(item)
print('after dumps',type(item)) # str
```

**json.load(f)**

**作用**

```python
将json文件读取,并转为python类型
```

示例

```python
import json

with open('D:\\spider_test\\xiaomi.json','r') as f:
    data = json.load(f)
    
print(data)
```

**json.dump(python,f,ensure_ascii=False)**

* **作用**

```python
把python数据类型 转为 json格式的字符串
# 一般让你把抓取的数据保存为json文件时使用
```

* **参数说明**

```python
第1个参数: python类型的数据(字典，列表等)
第2个参数: 文件对象
第3个参数: ensure_ascii=False # 序列化时编码
```

* **示例1**

```python
import json

item = {'name':'QQ','app_id':1}
with open('小米.json','a') as f:
  json.dump(item,f,ensure_ascii=False)
```

* **示例2**

```python
import json

item_list = []
for i in range(3):
  item = {'name':'QQ','id':i}
  item_list.append(item)
    
with open('xiaomi.json','a') as f:
	json.dump(item_list,f,ensure_ascii=False)
```

**json模块总结**

```python
# 爬虫最常用
1、数据抓取 - json.loads(html)
   将响应内容由: json 转为 python
2、数据保存 - json.dump(item_list,f,ensure_ascii=False)
   将抓取的数据保存到本地 json文件

# 抓取数据一般处理方式
1、txt文件
2、csv文件
3、json文件
4、MySQL数据库
5、MongoDB数据库
6、Redis数据库
```

### **selenium+phantomjs/Chrome/Firefox**

**selenium**

* **定义**

```python
1、Web自动化测试工具，可运行在浏览器,根据指令操作浏览器
2、只是工具，必须与第三方浏览器结合使用
```

* **安装**

```python
Linux: sudo pip3 install selenium
Windows: python -m pip install selenium
```

**phantomjs浏览器**

* **定义**

```python
无界面浏览器(又称无头浏览器)，在内存中进行页面加载,高效
```

* **安装(phantomjs、chromedriver、geckodriver)**

Windows

```python
1、下载对应版本的phantomjs、chromedriver、geckodriver
2、把chromedriver.exe拷贝到python安装目录的Scripts目录下(添加到系统环境变量)
   # 查看python安装路径: where python
3、验证
   cmd命令行: chromedriver

# 下载地址
1、chromedriver : 下载对应版本
http://chromedriver.storage.googleapis.com/index.html
2、geckodriver
https://github.com/mozilla/geckodriver/releases
3、phantomjs
https://phantomjs.org/download.html
```

Linux

```python
1、下载后解压
   tar -zxvf geckodriver.tar.gz 
2、拷贝解压后文件到 /usr/bin/ （添加环境变量）
   sudo cp geckodriver /usr/bin/
3、更改权限
   sudo -i
   cd /usr/bin/
   chmod 777 geckodriver
```

* **使用**

示例代码一：使用 selenium+浏览器 打开百度

```python
# 导入seleinum的webdriver接口
from selenium import webdriver
import time

# 创建浏览器对象
browser = webdriver.PhantomJS()
browser.get('http://www.baidu.com/')

time.sleep(5)

# 关闭浏览器
browser.quit()
```

示例代码二：打开百度，搜索赵丽颖，点击搜索，查看

```python
from selenium import webdriver
import time

# 1.创建浏览器对象 - 已经打开了浏览器
browser = webdriver.Chrome()
# 2.输入: http://www.baidu.com/
browser.get('http://www.baidu.com/')
# 3.找到搜索框,向这个节点发送文字: 赵丽颖
browser.find_element_by_xpath('//*[@id="kw"]').send_keys('赵丽颖')
# 4.找到 百度一下 按钮,点击一下
browser.find_element_by_xpath('//*[@id="su"]').click()
```

* **浏览器对象(browser)方法**

```python
# from selenium import webdriver
1、browser = webdriver.Chrome(executable_path='path')
2、browser.get(url) # 此方法是阻塞的
3、browser.page_source # HTML结构源码
4、browser.page_source.find('字符串')
   # 从html源码中搜索指定字符串,没有找到返回：-1
5、browser.quit() # 关闭浏览器
```

* **定位节点**

单元素查找(1个节点对象)

```python
1、browser.find_element_by_id('')
2、browser.find_element_by_name('')
3、browser.find_element_by_class_name('')
4、browser.find_element_by_xpath('')
... ...
```

多元素查找([节点对象列表])

```python
1、browser.find_elements_by_id('')
2、browser.find_elements_by_name('')
3、browser.find_elements_by_class_name('')
4、browser.find_elements_by_xpath('')
... ...
```

* 节点对象操作

```python
1、ele.send_keys('') # 搜索框发送内容
2、ele.click()
3、ele.text # 获取文本内容，包含子节点和后代节点的文本内容
4、ele.get_attribute('src') # 获取属性值
```

### 京东爬虫案例

* **目标**

```python
1、目标网址 ：https://www.jd.com/
2、抓取目标 ：商品名称、商品价格、评价数量、商品商家
```

* **思路提醒**

```python
1、打开京东，到商品搜索页
2、匹配所有商品节点对象列表
3、把节点对象的文本内容取出来，查看规律，是否有更好的处理办法？
4、提取完1页后，判断如果不是最后1页，则点击下一页
   # 如何判断是否为最后1页？？？
```

* **实现步骤**

找节点

```python
1、首页搜索框 : //*[@id="key"]
2、首页搜索按钮   ://*[@id="search"]/div/div[2]/button
3、商品页的 商品信息节点对象列表 ://*[@id="J_goodsList"]/ul/li
4、for循环遍历后
  名称: .//div[@class="p-name"]/a/em
  价格: .//div[@class="p-price"]
  评论: .//div[@class="p-commit"]/strong
  商家: .//div[@class="p-shopnum"]
```

执行JS脚本，获取动态加载数据

```python
browser.execute_script(
  'window.scrollTo(0,document.body.scrollHeight)'
)
```

代码实现

```python
from selenium import webdriver
import time

class JdSpider(object):
  def __init__(self):
    self.url = 'https://www.jd.com/'
    # 设置无界面
    self.options = webdriver.ChromeOptions()
    self.options.add_argument('--headless')
    # 正常创建浏览器对象即可
    self.browser = webdriver.Chrome(options=self.options)
    # 计数
    self.i = 0

  # 获取页面信息 - 到具体商品的页面
  def get_html(self):
    self.browser.get(self.url)
    # 找两个节点
    self.browser.find_element_by_xpath('//*[@id="key"]').send_keys('爬虫书')
    self.browser.find_element_by_xpath('//*[@id="search"]/div/div[2]/button').click()
    # 给商品页面加载时间
    time.sleep(3)

  def parse_html(self):
    # 把进度条拉到底部,使所有数据动态加载
    self.browser.execute_script(
      'window.scrollTo(0,document.body.scrollHeight)'
    )
    # 等待动态数据加载完成
    time.sleep(2)

    # 提取所有商品节点对象列表 li列表
    li_list = self.browser.find_elements_by_xpath('//*[@id="J_goodsList"]/ul/li')
    item = {}
    for li in li_list:
      # find_element: 查找单元素
      item['name'] = li.find_element_by_xpath('.//div[@class="p-name"]/a/em').text.strip()
      item['price'] = li.find_element_by_xpath('.//div[@class="p-price"]').text.strip()
      item['comment'] = li.find_element_by_xpath('.//div[@class="p-commit"]/strong').text.strip()
      item['shop'] = li.find_element_by_xpath('.//div[@class="p-shopnum"]').text.strip()

      print(item)
      self.i += 1


  def main(self):
    self.get_html()
    while True:
      self.parse_html()
      # 判断是否为最后一页
      if self.browser.page_source.find('pn-next disabled') == -1:
        self.browser.find_element_by_class_name('pn-next').click()
        time.sleep(3)
      else:
        break
    print('商品数量:',self.i)
    self.browser.quit()


if __name__ == '__main__':
  spider = JdSpider()
  spider.main()
```

### **chromedriver设置无界面模式**

```python
from selenium import webdriver

options = webdriver.ChromeOptions()
# 添加无界面参数
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
browser.get('http://www.baidu.com/')
browser.save_screenshot('baidu.png')
```

### **selenium - 键盘操作**

```python
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
# 1、在搜索框中输入"selenium"
browser.find_element_by_id('kw').send_keys('赵丽颖')
# 2、输入空格
browser.find_element_by_id('kw').send_keys(Keys.SPACE)
# 3、Ctrl+a 模拟全选
browser.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# 4、Ctrl+c 模拟复制
browser.find_element_by_id('kw').send_keys(Keys.CONTROL, 'c')
# 5、Ctrl+v 模拟粘贴
browser.find_element_by_id('kw').send_keys(Keys.CONTROL, 'v')
# 6、输入回车,代替 搜索 按钮
browser.find_element_by_id('kw').send_keys(Keys.ENTER)
```

### **selenium - 鼠标操作**

```python
from selenium import webdriver
# 导入鼠标事件类
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')

#移动到 设置，perform()是真正执行操作，必须有
element = driver.find_element_by_xpath('//*[@id="u1"]/a[8]')
ActionChains(driver).move_to_element(element).perform()

#单击，弹出的Ajax元素，根据链接节点的文本内容查找
driver.find_element_by_link_text('高级搜索').click()
```

### selenium - 切换页面

* **适用网站**

```python
页面中点开链接出现新的页面，但是浏览器对象browser还是之前页面的对象
```

* **应对方案**

```python
# 获取当前所有句柄（窗口）
all_handles = browser.window_handles
# 切换browser到新的窗口，获取新窗口的对象
browser.switch_to.window(all_handles[1])
```

#### 民政部网站案例

目标

```python
将民政区划代码爬取到数据库中，按照层级关系（分表 -- 省表、市表、县表）
```

数据库中建表

```mysql
# 建库
create database govdb charset utf8;
use govdb;
# 建表
create table province(
p_name varchar(20),
p_code varchar(20)
)charset=utf8;
create table city(
c_name varchar(20),
c_code varchar(20),
c_father_code varchar(20)
)charset=utf8;
create table county(
x_name varchar(20),
x_code varchar(20),
x_father_code varchar(20)
)charset=utf8;
```

思路

```python
1、selenium+Chrome打开一级页面，并提取二级页面最新链接
2、增量爬取: 和数据库version表中进行比对，确定之前是否爬过（是否有更新）
3、如果没有更新，直接提示用户，无须继续爬取
4、如果有更新，则删除之前表中数据，重新爬取并插入数据库表
5、最终完成后: 断开数据库连接，关闭浏览器
```

代码实现

```python
from selenium import webdriver
import pymysql

class GovSpider(object):
  def __init__(self):
    # 设置无界面
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # 添加参数
    self.browser = webdriver.Chrome(options=options)
    self.one_url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
    self.db = pymysql.connect(
      'localhost','root','123456','govdb',charset='utf8'
    )
    self.cursor = self.db.cursor()
    # 创建3个列表,用来executemany()往3张表中插入记录
    self.province_list = []
    self.city_list = []
    self.county_list = []

  def get_incr_url(self):
    self.browser.get(self.one_url)
    # 提取最新链接,判断是否需要增量爬
    td = self.browser.find_element_by_xpath(
      '//td[@class="arlisttd"]/a[contains(@title,"代码")]'
    )
    # 提取链接 和 数据库中做比对,确定是否需要怎俩那个抓取
    # get_attribute()会自动补全提取的链接
    two_url = td.get_attribute('href')
    sel = 'select url from version where url=%s'
    # result为返回的受影响的条数
    result = self.cursor.execute(sel,[two_url])
    if result:
      print('无须爬取')
    else:
      td.click()
      # 切换句柄
      all_handlers = self.browser.window_handles
      self.browser.switch_to.window(all_handlers[1])
      self.get_data()
      # 把URL地址存入version表
      dele = 'delete from version'
      ins = 'insert into version values(%s)'
      self.cursor.execute(dele)
      self.cursor.execute(ins,[two_url])
      self.db.commit()

  def get_data(self):
    tr_list = self.browser.find_elements_by_xpath(
      '//tr[@height="19"]'
    )
    for tr in tr_list:
      code = tr.find_element_by_xpath('./td[2]').text.strip()
      name = tr.find_element_by_xpath('./td[3]').text.strip()
      print(name,code)
      # 把数据添加到对应的表中
      if code[-4:] == '0000':
        self.province_list.append([name,code])
        if name in ['北京市','天津市','上海市','重庆市']:
          self.city_list.append([name,code,code])

      elif code[-2:] == '00':
        self.city_list.append([name,code,(code[:2]+'0000')])

      else:
        if code[:2] in ['11','12','31','50']:
          self.county_list.append([name,code,(code[:2]+'0000')])
        else:
          self.county_list.append([name,code,(code[:4]+'00')])

    # 执行数据库插入语句
    self.insert_mysql()

  def insert_mysql(self):
    # 1. 先删除原有数据
    del_province = 'delete from province'
    del_city = 'delete from city'
    del_county = 'delete from county'
    self.cursor.execute(del_province)
    self.cursor.execute(del_city)
    self.cursor.execute(del_county)
    # 2. 插入新数据
    ins_province = 'insert into province values(%s,%s)'
    ins_city = 'insert into city values(%s,%s,%s)'
    ins_county = 'insert into county values(%s,%s,%s)'
    self.cursor.executemany(ins_province,self.province_list)
    self.cursor.executemany(ins_city,self.city_list)
    self.cursor.executemany(ins_county,self.county_list)
    # 3.提交到数据库执行
    self.db.commit()

  def main(self):
    self.get_incr_url()
    self.cursor.close()
    self.db.close()
    self.browser.quit()

if __name__ == '__main__':
  spider = GovSpider()
  spider.main()
```

SQL命令练习

```mysql
# 1. 查询所有省市县信息（多表查询实现）
select province.p_name,city.c_name,county.x_name from province,city,county  where  province.p_code=city.c_father_code and  city.c_code=county.x_father_code;
# 2. 查询所有省市县信息（连接查询实现）
select province.p_name,city.c_name,county.x_name from province inner join city on  province.p_code=city.c_father_code inner join county on  city.c_code=county.x_father_code;
```

### selenium - Web客户端验证

弹窗中的用户名和密码如何输入？

```python
不用输入，在URL地址中填入就可以
```

示例: 爬取某一天笔记

```python
from selenium import webdriver

url = 'http://tarenacode:code_2013@code.tarena.com.cn/AIDCode/aid1904/15-spider/spider_day06_note.zip'
browser = webdriver.Chrome()
browser.get(url)
```

### **selenium - iframe子框架**

特点

```python
网页中嵌套了网页，先切换到iframe子框架，然后再执行其他操作
```

方法

```python
browser.switch_to.iframe(iframe_element)
```

示例 - 登录qq邮箱

```python
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')

# 切换到iframe子框架
login_frame = driver.find_element_by_id('login_frame')
driver.switch_to.frame(login_frame)

# 用户名+密码+登录
driver.find_element_by_id('u').send_keys('qq号')
driver.find_element_by_id('p').send_keys('qq密码')
driver.find_element_by_id('login_button').click()

# 预留页面记载时间
time.sleep(5)

# 提取数据
ele = driver.find_element_by_id('useralias')
print(ele.text)
```

### 百度翻译破解案例

目标

```python
破解百度翻译接口，抓取翻译结果数据
```

实现步骤

1、F12抓包,找到json的地址,观察查询参数

```python
1、POST地址: https://fanyi.baidu.com/v2transapi
2、Form表单数据（多次抓取在变的字段）
   from: zh
   to: en
   sign: 54706.276099  #这个是如何生成的？
   token: a927248ae7146c842bb4a94457ca35ee # 基本固定,但也想办法获取
```

2、抓取相关JS文件

```python
右上角 - 搜索 - sign: - 找到具体JS文件(index_c8a141d.js) - 格式化输出
```

3、在JS中寻找sign的生成代码

```python
1、在格式化输出的JS代码中搜索: sign: 找到如下JS代码：sign: m(a),
2、通过设置断点，找到m(a)函数的位置，即生成sign的具体函数
   # 1. a 为要翻译的单词
   # 2. 鼠标移动到 m(a) 位置处，点击可进入具体m(a)函数代码块
```

4、生成sign的m(a)函数具体代码如下(在一个大的define中)

```javascript
function a(r) {
        if (Array.isArray(r)) {
            for (var o = 0, t = Array(r.length); o < r.length; o++)
                t[o] = r[o];
            return t
        }
        return Array.from(r)
    }
function n(r, o) {
    for (var t = 0; t < o.length - 2; t += 3) {
        var a = o.charAt(t + 2);
        a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
            a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
            r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
    }
    return r
}
function e(r) {
    var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
    if (null === o) {
        var t = r.length;
        t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
    } else {
        for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++)
            "" !== e[C] && f.push.apply(f, a(e[C].split(""))),
                C !== h - 1 && f.push(o[C]);
        var g = f.length;
        g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
    }
//    var u = void 0
//    , l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
//    u = null !== i ? i : (i = window[l] || "") || "";
//  断点调试,然后从网页源码中找到 window.gtk的值    
    var u = '320305.131321201'
    
    for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
        var A = r.charCodeAt(v);
        128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)),
            S[c++] = A >> 18 | 240,
            S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224,
                                                                    S[c++] = A >> 6 & 63 | 128),
                                S[c++] = 63 & A | 128)
    }
    for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)
        p += S[b],
            p = n(p, F);
    return p = n(p, D),
        p ^= s,
        0 > p && (p = (2147483647 & p) + 2147483648),
        p %= 1e6,
        p.toString() + "." + (p ^ m)
}
```

5、直接将代码写入本地js文件,利用pyexecjs模块执行js代码进行调试

```python
# 安装pyexecjs模块
sudo pip3 install pyexecjs

# 使用
import execjs

with open('translate.js','r') as f:
    js_data = f.read()
    
# 创建对象
exec_object = execjs.compile(js_data)
sign = exec_object.eval('e("hello")')
print(sign)
```

获取token

```python
# 在js中
token: window.common.token
# 在响应中想办法获取此值
token_url = 'https://fanyi.baidu.com/?aldtype=16047'
regex: "token: '(.*?)'"
```

具体代码实现

```python
import requests
import re
import execjs

class BaiduTranslateSpider(object):
    def __init__(self):
        self.token_url = 'https://fanyi.baidu.com/?aldtype=16047'
        self.post_url = 'https://fanyi.baidu.com/v2transapi'
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 'BAIDUID=52920E829C1F64EE98183B703F4E37A9:FG=1; BIDUPSID=52920E829C1F64EE98183B703F4E37A9; PSTM=1562657403; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID=6890774803653935935; BDSFRCVID=4XAsJeCCxG3DLCbwbJrKDGwjNA0UN_I3KhXZ3J; H_BDCLCKID_SF=tRk8oIDaJCvSe6r1MtQ_M4F_qxby26nUQ5neaJ5n0-nnhnL4W46bqJKFLtozKMoI3C7fotJJ5nololIRy6CKjjb-jaDqJ5n3bTnjstcS2RREHJrg-trSMDCShGRGWlO9WDTm_D_KfxnkOnc6qJj0-jjXqqo8K5Ljaa5n-pPKKRAaqD04bPbZL4DdMa7HLtAO3mkjbnczfn02OP5P5lJ_e-4syPRG2xRnWIvrKfA-b4ncjRcTehoM3xI8LNj405OTt2LEoDPMJKIbMI_rMbbfhKC3hqJfaI62aKDs_RCMBhcqEIL4eJOIb6_w5gcq0T_HttjtXR0atn7ZSMbSj4Qo5pK95p38bxnDK2rQLb5zah5nhMJS3j7JDMP0-4rJhxby523i5J6vQpnJ8hQ3DRoWXPIqbN7P-p5Z5mAqKl0MLIOkbC_6j5DWDTvLeU7J-n8XbI60XRj85-ohHJrFMtQ_q4tehHRMBUo9WDTm_DoTttt5fUj6qJj855jXqqo8KMtHJaFf-pPKKRAashnzWjrkqqOQ5pj-WnQr3mkjbn5yfn02OpjPX6joht4syPRG2xRnWIvrKfA-b4ncjRcTehoM3xI8LNj405OTt2LEoC0XtIDhMDvPMCTSMt_HMxrKetJyaR0JhpjbWJ5TEPnjDUOdLPDW-46HBM3xbKQw5CJGBf7zhpvdWhC5y6ISKx-_J68Dtf5; ZD_ENTRY=baidu; PSINO=2; H_PS_PSSID=26525_1444_21095_29578_29521_28518_29098_29568_28830_29221_26350_29459; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1563426293,1563996067; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1563999768; yjs_js_security_passport=2706b5b03983b8fa12fe756b8e4a08b98fb43022_1563999769_js',
            'pragma': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        }

    # 获取token和gtk
    def get_token(self):
        token_url = 'https://fanyi.baidu.com/?aldtype=16047'
        # 定义请求头
        r = requests.get(self.token_url,headers=self.headers)
        token = re.findall(r"token: '(.*?)'",r.text)
        window_gtk = re.findall(r"window.*?gtk = '(.*?)';</script>",r.text)
        if token:
            return token[0],window_gtk[0]

    # 获取sign
    def get_sign(self,word,gtk):
        with open('translate.js','r') as f:
            js_data = f.read()

        exec_object = execjs.compile(js_data)
        sign = exec_object.eval('e("{}","{}")'.format(word,gtk))

        return sign

    # 主函数
    def main(self,word,fro,to):
        token,gtk = self.get_token()
        sign = self.get_sign(word,gtk)
        # 找到form表单数据如下,sign和token需要想办法获取
        form_data = {
            'from': fro,
            'to': to,
            'query': word,
            'transtype': 'realtime',
            'simple_means_flag': '3',
            'sign': sign,
            'token': token
        }
        r = requests.post(self.post_url,data=form_data,headers=self.headers)
        print(r.json()['trans_result']['data'][0]['dst'])

if __name__ == '__main__':
    spider = BaiduTranslateSpider()
    choice = input('1. 英译汉 2. 汉译英 : ')
    word = input('请输入要翻译的单词:')
    if choice == '1':
        fro,to = 'en','zh'
    elif choice == '2':
        fro,to = 'zh','en'

    spider.main(word,fro,to)
```


# **DAY08**

## **Day07回顾**

### **cookie模拟登陆**

```python
1、适用网站类型: 爬取网站页面时需要登录后才能访问，否则获取不到页面的实际响应数据
2、方法1（利用cookie）
   1、先登录成功1次,获取到携带登陆信息的Cookie（处理headers） 
   2、利用处理的headers向URL地址发请求
3、方法2(利用requests.get()中cookies参数)
   1、先登录成功1次,获取到cookie,处理为字典
   2、res=requests.get(xxx,cookies=cookies)
4、方法3（利用session会话保持）
   1、实例化session对象
      session = requests.session()
   2、先post : session.post(post_url,data=post_data,headers=headers)
      1、登陆，找到POST地址: form -> action对应地址
      2、定义字典，创建session实例发送请求
         # 字典key ：<input>标签中name的值(email,password)
         # post_data = {'email':'','password':''}
   3、再get : session.get(url,headers=headers)
```

### **三个池子**

```python
1、User-Agent池
2、代理IP池
3、cookie池
```

### **selenium+phantomjs/chrome/firefox**

* **特点**

```python
1、简单，无需去详细抓取分析网络数据包，使用真实浏览器
2、需要等待页面元素加载，需要时间，效率低
```

* **安装**

```python
1、下载、解压
2、添加到系统环境变量
   # windows: 拷贝到Python安装目录的Scripts目录中
   # Linux :  拷贝到/usr/bin目录中
3、Linux中修改权限
   # sudo -i
   # cd /usr/bin/
   # chmod +x phantomjs
     改权限前: rwxr--r--
     改权限后: rwxr-xr-x
```

* **使用流程**

```python
from selenium import webdriver

# 1、创建浏览器对象
browser = webdriver.Firefox(executable_path='/xxx/geckodriver')
# 2、输入网址
browser.get('URL')
# 3、查找节点
brower.find_xxxx
# 4、做对应操作
element.send_keys('')
element.click()
# 5、关闭浏览器
browser.quit()
```

* 重要知识点

```python
1、browser.page_source
2、browser.page_source.find('')
3、node.send_keys('')
4、node.click()
5、find_element AND find_elements
6、browser.execute_script('javascript')
7、browser.quit()
```

## **Day08笔记**

### **chromedriver设置无界面模式**

```python
from selenium import webdriver

options = webdriver.ChromeOptions()
# 添加无界面参数
options.add_argument('--headless')
browser = webdriver.Chrome(options=options)
browser.get('http://www.baidu.com/')
browser.save_screenshot('baidu.png')
```

### **selenium - 键盘操作**

```python
from selenium.webdriver.common.keys import Keys

browser = webdriver.Chrome()
browser.get('http://www.baidu.com/')
# 1、在搜索框中输入"selenium"
browser.find_element_by_id('kw').send_keys('赵丽颖')
# 2、输入空格
browser.find_element_by_id('kw').send_keys(Keys.SPACE)
# 3、Ctrl+a 模拟全选
browser.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')
# 4、Ctrl+c 模拟复制
browser.find_element_by_id('kw').send_keys(Keys.CONTROL, 'c')
# 5、Ctrl+v 模拟粘贴
browser.find_element_by_id('kw').send_keys(Keys.CONTROL, 'v')
# 6、输入回车,代替 搜索 按钮
browser.find_element_by_id('kw').send_keys(Keys.ENTER)
```

### **selenium - 鼠标操作**

```python
from selenium import webdriver
# 导入鼠标事件类
from selenium.webdriver import ActionChains

driver = webdriver.Chrome()
driver.get('http://www.baidu.com/')

#移动到 设置，perform()是真正执行操作，必须有
element = driver.find_element_by_xpath('//*[@id="u1"]/a[8]')
ActionChains(driver).move_to_element(element).perform()

#单击，弹出的Ajax元素，根据链接节点的文本内容查找
driver.find_element_by_link_text('高级搜索').click()
```

### **selenium - 切换页面**

- **适用网站**

```python
页面中点开链接出现新的页面，但是浏览器对象browser还是之前页面的对象
```

- **应对方案**

```python
# 获取当前所有句柄（窗口）
all_handles = browser.window_handles
# 切换browser到新的窗口，获取新窗口的对象
browser.switch_to.window(all_handles[1])
```

#### 民政部网站案例

- **目标**

```python
将民政区划代码爬取到数据库中，按照层级关系（分表 -- 省表、市表、县表）
```

- **数据库中建表**

```mysql
# 建库
create database govdb charset utf8;
use govdb;
# 建表
create table province(
p_name varchar(20),
p_code varchar(20)
)charset=utf8;
create table city(
c_name varchar(20),
c_code varchar(20),
c_father_code varchar(20)
)charset=utf8;
create table county(
x_name varchar(20),
x_code varchar(20),
x_father_code varchar(20)
)charset=utf8;
```

- **思路**

```python
1、selenium+Chrome打开一级页面，并提取二级页面最新链接
2、增量爬取: 和数据库version表中进行比对，确定之前是否爬过（是否有更新）
3、如果没有更新，直接提示用户，无须继续爬取
4、如果有更新，则删除之前表中数据，重新爬取并插入数据库表
5、最终完成后: 断开数据库连接，关闭浏览器
```

- **代码实现**

```python
from selenium import webdriver
import pymysql

class GovSpider(object):
  def __init__(self):
    # 设置无界面
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    # 添加参数
    self.browser = webdriver.Chrome(options=options)
    self.one_url = 'http://www.mca.gov.cn/article/sj/xzqh/2019/'
    self.db = pymysql.connect(
      'localhost','root','123456','govdb',charset='utf8'
    )
    self.cursor = self.db.cursor()
    # 创建3个列表,用来executemany()往3张表中插入记录
    self.province_list = []
    self.city_list = []
    self.county_list = []

  def get_incr_url(self):
    self.browser.get(self.one_url)
    # 提取最新链接,判断是否需要增量爬
    td = self.browser.find_element_by_xpath(
      '//td[@class="arlisttd"]/a[contains(@title,"代码")]'
    )
    # 提取链接 和 数据库中做比对,确定是否需要抓取
    # get_attribute()会自动补全提取的链接
    two_url = td.get_attribute('href')
    sel = 'select url from version where url=%s'
    # result为返回的受影响的条数
    result = self.cursor.execute(sel,[two_url])
    if result:
      print('无须爬取')
    else:
      td.click()
      # 切换句柄
      all_handlers = self.browser.window_handles
      self.browser.switch_to.window(all_handlers[1])
      self.get_data()
      # 把URL地址存入version表
      dele = 'delete from version'
      ins = 'insert into version values(%s)'
      self.cursor.execute(dele)
      self.cursor.execute(ins,[two_url])
      self.db.commit()

  def get_data(self):
    tr_list = self.browser.find_elements_by_xpath(
      '//tr[@height="19"]'
    )
    for tr in tr_list:
      code = tr.find_element_by_xpath('./td[2]').text.strip()
      name = tr.find_element_by_xpath('./td[3]').text.strip()
      print(name,code)
      # 把数据添加到对应的表中
      if code[-4:] == '0000':
        self.province_list.append([name,code])
        if name in ['北京市','天津市','上海市','重庆市']:
          self.city_list.append([name,code,code])

      elif code[-2:] == '00':
        self.city_list.append([name,code,(code[:2]+'0000')])

      else:
        if code[:2] in ['11','12','31','50']:
          self.county_list.append([name,code,(code[:2]+'0000')])
        else:
          self.county_list.append([name,code,(code[:4]+'00')])

    # 执行数据库插入语句
    self.insert_mysql()

  def insert_mysql(self):
    # 1. 先删除原有数据
    del_province = 'delete from province'
    del_city = 'delete from city'
    del_county = 'delete from county'
    self.cursor.execute(del_province)
    self.cursor.execute(del_city)
    self.cursor.execute(del_county)
    # 2. 插入新数据
    ins_province = 'insert into province values(%s,%s)'
    ins_city = 'insert into city values(%s,%s,%s)'
    ins_county = 'insert into county values(%s,%s,%s)'
    self.cursor.executemany(ins_province,self.province_list)
    self.cursor.executemany(ins_city,self.city_list)
    self.cursor.executemany(ins_county,self.county_list)
    # 3.提交到数据库执行
    self.db.commit()

  def main(self):
    self.get_incr_url()
    self.cursor.close()
    self.db.close()
    self.browser.quit()

if __name__ == '__main__':
  spider = GovSpider()
  spider.main()
```

SQL命令练习

```mysql
# 1. 查询所有省市县信息（多表查询实现）
select province.p_name,city.c_name,county.x_name from province,city,county  where  province.p_code=city.c_father_code and  city.c_code=county.x_father_code;
# 2. 查询所有省市县信息（连接查询实现）
select province.p_name,city.c_name,county.x_name from province inner join city on  province.p_code=city.c_father_code inner join county on  city.c_code=county.x_father_code;
```

### **selenium - Web客户端验证**

弹窗中的用户名和密码如何输入？

```python
不用输入，在URL地址中填入就可以
```

示例: 爬取某一天笔记

```python
from selenium import webdriver

url = 'http://tarenacode:code_2013@code.tarena.com.cn/AIDCode/aid1905/14_spider/spider_day06.zip'
browser = webdriver.Chrome()
browser.get(url)
```

### **selenium - iframe子框架**

- **特点**

```python
网页中嵌套了网页，先切换到iframe子框架，然后再执行其他操作
```

- **方法**

```python
browser.switch_to.iframe(iframe_element)
```

- **示例 - 登录qq邮箱**

```python
from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://mail.qq.com/')

# 切换到iframe子框架
login_frame = driver.find_element_by_id('login_frame')
driver.switch_to.frame(login_frame)

# 用户名+密码+登录
driver.find_element_by_id('u').send_keys('qq邮箱账号')
driver.find_element_by_id('p').send_keys('qq密码')
driver.find_element_by_id('login_button').click()

# 预留页面记载时间
time.sleep(5)

# 提取数据
ele = driver.find_element_by_id('useralias')
print(ele.text)
```

### **百度翻译破解案例**

- **目标**

```python
破解百度翻译接口，抓取翻译结果数据
```

- **实现步骤**

1、F12抓包,找到json的地址,观察查询参数

```python
1、POST地址: https://fanyi.baidu.com/v2transapi
2、Form表单数据（多次抓取在变的字段）
   from: zh
   to: en
   sign: 54706.276099  #这个是如何生成的？
   token: a927248ae7146c842bb4a94457ca35ee # 基本固定,但也想办法获取
```

2、抓取相关JS文件

```python
右上角 - 搜索 - sign: - 找到具体JS文件(index_c8a141d.js) - 格式化输出
```

3、在JS中寻找sign的生成代码

```python
1、在格式化输出的JS代码中搜索: sign: 找到如下JS代码：sign: m(a),
2、通过设置断点，找到m(a)函数的位置，即生成sign的具体函数
   # 1. a 为要翻译的单词
   # 2. 鼠标移动到 m(a) 位置处，点击可进入具体m(a)函数代码块
```

4、生成sign的m(a)函数具体代码如下(在一个大的define中)

```javascript
function a(r) {
        if (Array.isArray(r)) {
            for (var o = 0, t = Array(r.length); o < r.length; o++)
                t[o] = r[o];
            return t
        }
        return Array.from(r)
    }
function n(r, o) {
    for (var t = 0; t < o.length - 2; t += 3) {
        var a = o.charAt(t + 2);
        a = a >= "a" ? a.charCodeAt(0) - 87 : Number(a),
            a = "+" === o.charAt(t + 1) ? r >>> a : r << a,
            r = "+" === o.charAt(t) ? r + a & 4294967295 : r ^ a
    }
    return r
}
function e(r) {
    var o = r.match(/[\uD800-\uDBFF][\uDC00-\uDFFF]/g);
    if (null === o) {
        var t = r.length;
        t > 30 && (r = "" + r.substr(0, 10) + r.substr(Math.floor(t / 2) - 5, 10) + r.substr(-10, 10))
    } else {
        for (var e = r.split(/[\uD800-\uDBFF][\uDC00-\uDFFF]/), C = 0, h = e.length, f = []; h > C; C++)
            "" !== e[C] && f.push.apply(f, a(e[C].split(""))),
                C !== h - 1 && f.push(o[C]);
        var g = f.length;
        g > 30 && (r = f.slice(0, 10).join("") + f.slice(Math.floor(g / 2) - 5, Math.floor(g / 2) + 5).join("") + f.slice(-10).join(""))
    }
//    var u = void 0
//    , l = "" + String.fromCharCode(103) + String.fromCharCode(116) + String.fromCharCode(107);
//    u = null !== i ? i : (i = window[l] || "") || "";
//  断点调试,然后从网页源码中找到 window.gtk的值    
    var u = '320305.131321201'
    
    for (var d = u.split("."), m = Number(d[0]) || 0, s = Number(d[1]) || 0, S = [], c = 0, v = 0; v < r.length; v++) {
        var A = r.charCodeAt(v);
        128 > A ? S[c++] = A : (2048 > A ? S[c++] = A >> 6 | 192 : (55296 === (64512 & A) && v + 1 < r.length && 56320 === (64512 & r.charCodeAt(v + 1)) ? (A = 65536 + ((1023 & A) << 10) + (1023 & r.charCodeAt(++v)),
            S[c++] = A >> 18 | 240,
            S[c++] = A >> 12 & 63 | 128) : S[c++] = A >> 12 | 224,
                                                                    S[c++] = A >> 6 & 63 | 128),
                                S[c++] = 63 & A | 128)
    }
    for (var p = m, F = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(97) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(54)), D = "" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(51) + ("" + String.fromCharCode(94) + String.fromCharCode(43) + String.fromCharCode(98)) + ("" + String.fromCharCode(43) + String.fromCharCode(45) + String.fromCharCode(102)), b = 0; b < S.length; b++)
        p += S[b],
            p = n(p, F);
    return p = n(p, D),
        p ^= s,
        0 > p && (p = (2147483647 & p) + 2147483648),
        p %= 1e6,
        p.toString() + "." + (p ^ m)
}
```

5、直接将代码写入本地js文件,利用pyexecjs模块执行js代码进行调试

```python
# 安装pyexecjs模块
sudo pip3 install pyexecjs

# 使用
import execjs

with open('translate.js','r') as f:
    js_data = f.read()
    
# 创建对象
exec_object = execjs.compile(js_data)
sign = exec_object.eval('e("hello")')
print(sign)
```

获取token

```python
# 在js中
token: window.common.token
# 在响应中想办法获取此值
token_url = 'https://fanyi.baidu.com/?aldtype=16047'
regex: "token: '(.*?)'"
```

具体代码实现

```python
import requests
import re
import execjs

class BaiduTranslateSpider(object):
    def __init__(self):
        self.token_url = 'https://fanyi.baidu.com/?aldtype=16047'
        self.post_url = 'https://fanyi.baidu.com/v2transapi'
        self.headers = {
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
            'accept-language': 'zh-CN,zh;q=0.9',
            'cache-control': 'no-cache',
            'cookie': 'BAIDUID=52920E829C1F64EE98183B703F4E37A9:FG=1; BIDUPSID=52920E829C1F64EE98183B703F4E37A9; PSTM=1562657403; to_lang_often=%5B%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%2C%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%5D; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; delPer=0; BDORZ=B490B5EBF6F3CD402E515D22BCDA1598; BCLID=6890774803653935935; BDSFRCVID=4XAsJeCCxG3DLCbwbJrKDGwjNA0UN_I3KhXZ3J; H_BDCLCKID_SF=tRk8oIDaJCvSe6r1MtQ_M4F_qxby26nUQ5neaJ5n0-nnhnL4W46bqJKFLtozKMoI3C7fotJJ5nololIRy6CKjjb-jaDqJ5n3bTnjstcS2RREHJrg-trSMDCShGRGWlO9WDTm_D_KfxnkOnc6qJj0-jjXqqo8K5Ljaa5n-pPKKRAaqD04bPbZL4DdMa7HLtAO3mkjbnczfn02OP5P5lJ_e-4syPRG2xRnWIvrKfA-b4ncjRcTehoM3xI8LNj405OTt2LEoDPMJKIbMI_rMbbfhKC3hqJfaI62aKDs_RCMBhcqEIL4eJOIb6_w5gcq0T_HttjtXR0atn7ZSMbSj4Qo5pK95p38bxnDK2rQLb5zah5nhMJS3j7JDMP0-4rJhxby523i5J6vQpnJ8hQ3DRoWXPIqbN7P-p5Z5mAqKl0MLIOkbC_6j5DWDTvLeU7J-n8XbI60XRj85-ohHJrFMtQ_q4tehHRMBUo9WDTm_DoTttt5fUj6qJj855jXqqo8KMtHJaFf-pPKKRAashnzWjrkqqOQ5pj-WnQr3mkjbn5yfn02OpjPX6joht4syPRG2xRnWIvrKfA-b4ncjRcTehoM3xI8LNj405OTt2LEoC0XtIDhMDvPMCTSMt_HMxrKetJyaR0JhpjbWJ5TEPnjDUOdLPDW-46HBM3xbKQw5CJGBf7zhpvdWhC5y6ISKx-_J68Dtf5; ZD_ENTRY=baidu; PSINO=2; H_PS_PSSID=26525_1444_21095_29578_29521_28518_29098_29568_28830_29221_26350_29459; locale=zh; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1563426293,1563996067; from_lang_often=%5B%7B%22value%22%3A%22zh%22%2C%22text%22%3A%22%u4E2D%u6587%22%7D%2C%7B%22value%22%3A%22en%22%2C%22text%22%3A%22%u82F1%u8BED%22%7D%5D; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1563999768; yjs_js_security_passport=2706b5b03983b8fa12fe756b8e4a08b98fb43022_1563999769_js',
            'pragma': 'no-cache',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36',
        }

    # 获取token和gtk
    def get_token(self):
        token_url = 'https://fanyi.baidu.com/?aldtype=16047'
        # 定义请求头
        r = requests.get(self.token_url,headers=self.headers)
        token = re.findall(r"token: '(.*?)'",r.text)
        window_gtk = re.findall(r"window.*?gtk = '(.*?)';</script>",r.text)
        if token:
            return token[0],window_gtk[0]

    # 获取sign
    def get_sign(self,word,gtk):
        with open('translate.js','r') as f:
            js_data = f.read()

        exec_object = execjs.compile(js_data)
        sign = exec_object.eval('e("{}","{}")'.format(word,gtk))

        return sign

    # 主函数
    def main(self,word,fro,to):
        token,gtk = self.get_token()
        sign = self.get_sign(word,gtk)
        # 找到form表单数据如下,sign和token需要想办法获取
        form_data = {
            'from': fro,
            'to': to,
            'query': word,
            'transtype': 'realtime',
            'simple_means_flag': '3',
            'sign': sign,
            'token': token
        }
        r = requests.post(self.post_url,data=form_data,headers=self.headers)
        print(r.json()['trans_result']['data'][0]['dst'])

if __name__ == '__main__':
    spider = BaiduTranslateSpider()
    choice = input('1. 英译汉 2. 汉译英 : ')
    word = input('请输入要翻译的单词:')
    if choice == '1':
        fro,to = 'en','zh'
    elif choice == '2':
        fro,to = 'zh','en'

    spider.main(word,fro,to)
```

### **scrapy框架**

- **定义**

```
异步处理框架,可配置和可扩展程度非常高,Python中使用最广泛的爬虫框架
```

- **安装**

```python
# Ubuntu安装
1、安装依赖包
	1、sudo apt-get install libffi-dev
	2、sudo apt-get install libssl-dev
	3、sudo apt-get install libxml2-dev
	4、sudo apt-get install python3-dev
	5、sudo apt-get install libxslt1-dev
	6、sudo apt-get install zlib1g-dev
	7、sudo pip3 install -I -U service_identity
2、安装scrapy框架
	1、sudo pip3 install Scrapy
```

```python
# Windows安装
cmd命令行(管理员): python -m pip install Scrapy
# Error: Microsoft Visual C++ 14.0 is required xxx
```

- **Scrapy框架五大组件**

```python
1、引擎(Engine)      ：整个框架核心
2、调度器(Scheduler) ：维护请求队列
3、下载器(Downloader)：获取响应对象  此组件是基于多线程的
4、爬虫文件(Spider)  ：数据解析提取
5、项目管道(Pipeline)：数据入库处理
**********************************
# 下载器中间件(Downloader Middlewares) : 下载器执行之前,包装请求(随机代理、随机user-agent等),大量使用
# 蜘蛛中间件(Spider Middlewares) : 下载器执行之后,可修改响应对象属性.使用较少
```

- **scrapy爬虫工作流程**

```python
# 爬虫项目启动
1、由引擎向爬虫程序索要第一个要爬取的URL,交给调度器去入队列
2、调度器处理请求后出队列,通过下载器中间件交给下载器去下载
3、下载器得到响应对象后,通过蜘蛛中间件交给爬虫程序
4、爬虫程序进行数据提取：
   1、数据交给管道文件去入库处理
   2、对于需要继续跟进的URL,再次交给调度器入队列，依次循环
```

### **今日作业**

```python
1、将链家二手房案例、小米应用商店案例、猫眼电影案例等使用selenium+Chrome实现
2、熟记scrapy框架的组件及工作流程 - 要求能口头描述清楚
```

# **Day09**

## **Day08回顾**

### **selenium+phantomjs/chrome/firefox**

- **设置无界面模式（chromedriver | firefox）**

```python
options = webdriver.ChromeOptions()
options.add_argument('--headless')

browser = webdriver.Chrome(options=options)
browser.get(url)
```

- **browser执行JS脚本**

```python
browser.execute_script(
'window.scrollTo(0,document.body.scrollHeight)'
)
time.sleep(2)
```

- **selenium常用操作**

```python
# 1、键盘操作
from selenium.webdriver.common.keys import Keys
node.send_keys(Keys.SPACE)
node.send_keys(Keys.CONTROL, 'a')
node.send_keys(Keys.CONTROL, 'c')
node.send_keys(Keys.CONTROL, 'v')
node.send_keys(Keys.ENTER)

# 2、鼠标操作
from selenium.webdriver import ActionChains
mouse_action = ActionChains(browser)
mouse_action.move_to_element(node)
mouse_action.perform()

# 3、切换句柄
all_handles = browser.window_handles
browser.switch_to.window(all_handles[1])

# 4、iframe子框架
browser.switch_to.iframe(iframe_element)

# 5、Web客户端验证
url = 'http://用户名:密码@正常地址'
```

## **execjs模块使用**

```python
# 1、安装
sudo pip3 install pyexecjs

# 2、使用
with open('file.js','r') as f:
    js = f.read()

obj = execjs.compile(js)
result = obj.eval('string')
```



## **Day09笔记**

## **scrapy框架**

- **定义**

```python
异步处理框架,可配置和可扩展程度非常高,Python中使用最广泛的爬虫框架
```

- **安装**

```python
# Ubuntu安装
1、安装依赖包
	1、sudo apt-get install libffi-dev
	2、sudo apt-get install libssl-dev
	3、sudo apt-get install libxml2-dev
	4、sudo apt-get install python3-dev
	5、sudo apt-get install libxslt1-dev
	6、sudo apt-get install zlib1g-dev
	7、sudo pip3 install -I -U service_identity
2、安装scrapy框架
	1、sudo pip3 install Scrapy
```

```python
# Windows安装
cmd命令行(管理员): python -m pip install Scrapy
# Error: Microsoft Visual C++ 14.0 is required xxx
```

- **Scrapy框架五大组件**

```python
1、引擎(Engine)      ：整个框架核心
2、调度器(Scheduler) ：维护请求队列
3、下载器(Downloader)：获取响应对象
4、爬虫文件(Spider)  ：数据解析提取
5、项目管道(Pipeline)：数据入库处理
**********************************
# 下载器中间件(Downloader Middlewares) : 引擎->下载器,包装请求(随机代理等)
# 蜘蛛中间件(Spider Middlewares) : 引擎->爬虫文件,可修改响应对象属性
```

- **scrapy爬虫工作流程**

```python
# 爬虫项目启动
1、由引擎向爬虫程序索要第一个要爬取的URL,交给调度器去入队列
2、调度器处理请求后出队列,通过下载器中间件交给下载器去下载
3、下载器得到响应对象后,通过蜘蛛中间件交给爬虫程序
4、爬虫程序进行数据提取：
   1、数据交给管道文件去入库处理
   2、对于需要继续跟进的URL,再次交给调度器入队列，依次循环
```

- **scrapy常用命令**

```python
# 1、创建爬虫项目
scrapy startproject 项目名
# 2、创建爬虫文件
scrapy genspider 爬虫名 域名
# 3、运行爬虫
scrapy crawl 爬虫名
```

- **scrapy项目目录结构**

```python
Baidu                   # 项目文件夹
├── Baidu               # 项目目录
│   ├── items.py        # 定义数据结构
│   ├── middlewares.py  # 中间件
│   ├── pipelines.py    # 数据处理
│   ├── settings.py     # 全局配置
│   └── spiders
│       ├── baidu.py    # 爬虫文件
└── scrapy.cfg          # 项目基本配置文件
```

- **全局配置文件settings.py详解**
> 必须配置 robots 和 请求头
```python
# 1、定义User-Agent
USER_AGENT = 'Mozilla/5.0'
# 2、是否遵循robots协议，一般设置为False
ROBOTSTXT_OBEY = False
# 3、最大并发量，默认为16
CONCURRENT_REQUESTS = 32
# 4、下载延迟时间
DOWNLOAD_DELAY = 1
# 5、请求头，此处也可以添加User-Agent
DEFAULT_REQUEST_HEADERS={}
# 6、项目管道
ITEM_PIPELINES={
	'项目目录名.pipelines.类名':300
}
```

- **创建爬虫项目步骤**

```python
1、新建项目 ：scrapy startproject 项目名
2、cd 项目文件夹
3、新建爬虫文件 ：scrapy genspider 文件名 域名
4、明确目标(items.py)
5、写爬虫程序(文件名.py)
6、管道文件(pipelines.py)
7、全局配置(settings.py)
8、运行爬虫 ：scrapy crawl 爬虫名
```

- **pycharm运行爬虫项目**

```python
1、创建begin.py(和scrapy.cfg文件同目录)
2、begin.py中内容：
	from scrapy import cmdline
	cmdline.execute('scrapy crawl maoyan'.split())
```

## **小试牛刀**

- **目标**

```python
打开百度首页，把 '百度一下，你就知道' 抓取下来，从终端输出
/html/head/title/text()
```

- **实现步骤**

**1、创建项目Baidu 和 爬虫文件baidu**

```python
1、scrapy startproject Baidu
2、cd Baidu
3、scrapy genspider baidu www.baidu.com
```

**2、编写爬虫文件baidu.py，xpath提取数据**

```python
# -*- coding: utf-8 -*-
import scrapy

class BaiduSpider(scrapy.Spider):
    name = 'baidu'
    allowed_domains = ['www.baidu.com']
    start_urls = ['http://www.baidu.com/']

    def parse(self, response):
        result = response.xpath('/html/head/title/text()').extract_first()
        print('*'*50)
        print(result)
        print('*'*50)
```

**3、全局配置settings.py**

```python
USER_AGENT = 'Mozilla/5.0'
ROBOTSTXT_OBEY = False
DEFAULT_REQUEST_HEADERS = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en',
}
```

**4、创建run.py（和scrapy.cfg同目录）**

```python
from scrapy import cmdline

cmdline.execute('scrapy crawl baidu'.split())
```

**5、启动爬虫**

```python
直接运行 run.py 文件即可
```

**思考运行过程**

## **猫眼电影案例**

- **目标**

```python
URL: 百度搜索 -> 猫眼电影 -> 榜单 -> top100榜
内容:电影名称、电影主演、上映时间
```

- **实现步骤**

**1、创建项目和爬虫文件**

```python
# 创建爬虫项目
scrapy startproject Maoyan
cd Maoyan
# 创建爬虫文件
scrapy genspider maoyan maoyan.com

# https://maoyan.com/board/4?offset=0
```

**2、定义要爬取的数据结构（items.py）**

```python
name = scrapy.Field()
star = scrapy.Field()
time = scrapy.Field()
```

**3、编写爬虫文件（maoyan.py）**

```python
1、基准xpath,匹配每个电影信息节点对象列表
	dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
2、for dd in dd_list:
	电影名称 = dd.xpath('./a/@title')
	电影主演 = dd.xpath('.//p[@class="star"]/text()')
	上映时间 = dd.xpath('.//p[@class="releasetime"]/text()')
```

   **代码实现一**

```python
# -*- coding: utf-8 -*-
import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/board/4?offset=0']
    offset = 0


    def parse(self, response):
        # 给items.py中的类:MaoyanItem(scrapy.Item)实例化
        item = MaoyanItem()

        # 基准xpath
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        # 依次遍历
        for dd in dd_list:
            # 是在给items.py中那些类变量赋值
            item['name'] = dd.xpath('./a/@title').get().strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get().strip()

            # 把item对象交给管道文件处理
            yield item

        self.offset += 10
        if self.offset <= 91:
            url = 'https://maoyan.com/board/4?offset={}'.format(self.offset)
            # 交给调度器入队列
            yield scrapy.Request(
                url = url,
                callback = self.parse
            )
```

   **代码实现二**

```python
import scrapy
from ..items import MaoyanItem

class MaoyanSpider(scrapy.Spider):
    name = 'maoyan3'
    allowed_domains = ['maoyan.com']
    # 去掉start_urls变量

    # 重写start_requests()方法
    def start_requests(self):
        for offset in range(0,91,10):
            url = 'https://maoyan.com/board/4?offset={}'.format(offset)
            yield scrapy.Request(url=url,callback=self.parse)

    def parse(self, response):
        # 给items.py中的类:MaoyanItem(scrapy.Item)实例化
        item = MaoyanItem()

        # 基准xpath
        dd_list = response.xpath('//dl[@class="board-wrapper"]/dd')
        # 依次遍历
        for dd in dd_list:
            # 是在给items.py中那些类变量赋值
            item['name'] = dd.xpath('./a/@title').get().strip()
            item['star'] = dd.xpath('.//p[@class="star"]/text()').get().strip()
            item['time'] = dd.xpath('.//p[@class="releasetime"]/text()').get().strip()

            # 把item对象交给管道文件处理
            yield item
```

**4、定义管道文件（pipelines.py）**

```python
class MaoyanPipeline(object):
    # item: 从爬虫文件maoyan.py中yield的item数据
    def process_item(self, item, spider):
        print(item['name'],item['time'],item['star'])

        return item


import pymysql
from .settings import *

# 自定义管道 - MySQL数据库
class MaoyanMysqlPipeline(object):
    # 爬虫项目开始运行时执行此函数
    def open_spider(self,spider):
        print('我是open_spider函数输出')
        # 一般用于建立数据库连接
        self.db = pymysql.connect(
            host = MYSQL_HOST,
            user = MYSQL_USER,
            password = MYSQL_PWD,
            database = MYSQL_DB,
            charset = MYSQL_CHAR
        )
        self.cursor = self.db.cursor()

    def process_item(self,item,spider):
        ins = 'insert into filmtab values(%s,%s,%s)'
        # 因为execute()的第二个参数为列表
        L = [
            item['name'],item['star'],item['time']
        ]
        self.cursor.execute(ins,L)
        self.db.commit()

        return item

    # 爬虫项目结束时执行此函数
    def close_spider(self,spider):
        print('我是close_spider函数输出')
        # 一般用于断开数据库连接
        self.cursor.close()
        self.db.close()
```

**5、全局配置文件（settings.py）**

```python
USER_AGENT = 'Mozilla/5.0'
ROBOTSTXT_OBEY = False
DEFAULT_REQUEST_HEADERS = {
	'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
	'Accept-Language': 'en',
}
ITEM_PIPELINES = {
   'Maoyan.pipelines.MaoyanPipeline': 300,
   'Maoyan.pipelines.MaoyanMysqlPipeline':200,
}
# 定义MySQL相关变量
MYSQL_HOST = '127.0.0.1'
MYSQL_USER = 'root'
MYSQL_PWD = '123456'
MYSQL_DB = 'maoyandb'
MYSQL_CHAR = 'utf8'
```

6. **创建并运行文件（run.py）**

```python
from scrapy import cmdline
cmdline.execute('scrapy crawl maoyan'.split())
```

## **知识点汇总**

- **节点对象.xpath('')**

```python
1、列表,元素为选择器 ['<selector data='A'>]
2、列表.extract() ：序列化列表中所有选择器为Unicode字符串 ['A','B','C']
3、列表.extract_first() 或者 get() :获取列表中第1个序列化的元素(字符串)
```

- **pipelines.py中必须有1个函数叫process_item**

```python
def process_item(self,item,spider):
	return item
# 必须返回item,此返回值会传给下一个管道的此函数继续处理
```

- **日志变量及日志级别(settings.py)**     

```python
# 日志相关变量
LOG_LEVEL = ''
LOG_FILE = '文件名.log'

# 日志级别
5 CRITICAL ：严重错误
4 ERROR    ：普通错误
3 WARNING  ：警告
2 INFO     ：一般信息
1 DEBUG    ：调试信息
# 注意: 只显示当前级别的日志和比当前级别日志更严重的
```

- **管道文件使用**

```python
1、在爬虫文件中为items.py中类做实例化，用爬下来的数据给对象赋值
	from ..items import MaoyanItem
	item = MaoyanItem()
2、管道文件（pipelines.py）
3、开启管道（settings.py）
	ITEM_PIPELINES = { '项目目录名.pipelines.类名':优先级 }
```

## **数据持久化存储(MySQL)**

### **实现步骤**

```python
1、在setting.py中定义相关变量
2、pipelines.py中导入settings模块
	def open_spider(self,spider):
		# 爬虫开始执行1次,用于数据库连接
	def close_spider(self,spider):
		# 爬虫结束时执行1次,用于断开数据库连接
3、settings.py中添加此管道
	ITEM_PIPELINES = {'':200}

# 注意 ：process_item() 函数中一定要 return item ***
```

## **保存为csv、json文件**

- 命令格式

```python
scrapy crawl maoyan -o maoyan.csv
scrapy crawl maoyan -o maoyan.json
# settings.py中设置导出编码
FEED_EXPORT_ENCODING = 'utf-8'
```

## **盗墓笔记小说抓取案例（三级页面）**

-   目标

```python
# 抓取目标网站中盗墓笔记1-8中所有章节的所有小说的具体内容，保存到本地文件
1、网址 ：http://www.daomubiji.com/
```

- 准备工作xpath

```python
1、一级页面xpath：
a节点: //li[contains(@id,"menu-item-20")]/a
title: ./text()
link : ./@href
    
2、二级页面
  基准xpath ：//article
  for循环遍历后:
    name=article.xpath('./a/text()').get()
    link=article.xpath('./a/@href').get()
    
3、三级页面xpath：response.xpath('//article[@class="article-content"]//p/text()').extract()
# 结果: ['p1','p2','p3','']
```

- **项目实现**

**1、创建项目及爬虫文件**

```python
1、创建项目 ：scrapy startproject Daomu
2、创建爬虫 ：
   1、cd Daomu
   2、scrapy genspider daomu www.daomubiji.com
```

**2、定义要爬取的数据结构 - items.py**

```python
import scrapy


class DaomuItem(scrapy.Item):
    # 想想你最终想要什么 - pipelines中用什么
    # 1. 一级页面标题
    title = scrapy.Field()
    # 2. 二级页面标题
    name = scrapy.Field()
    # 3. 三级页面小说内容
    content = scrapy.Field()
    # 4. 完整文件名
    filename = scrapy.Field()
```

**3、爬虫文件实现数据抓取 - daomu.py**

```python
import scrapy
from ..items import DaomuItem
import os

class DaomuSpider(scrapy.Spider):
    name = 'daomu'
    allowed_domains = ['www.daomubiji.com']
    start_urls = ['http://www.daomubiji.com/']
    basedir = '/home/tarena/novel/'

    # 解析一级页面函数: 链接+名字
    def parse(self, response):
        # 基准xpath,匹配所有a节点
        a_list = response.xpath('//li[contains(@id,"menu-item-20")]/a')

        for a in a_list:
            item = DaomuItem()
            item['title'] = a.xpath('./text()').get()
            one_link = a.xpath('./@href').get()
            # 创建一级文件夹(11个)
            # onedir: '/home/tarena/novel/盗墓笔记1/'
            onedir = self.basedir + item['title'] + '/'
            print(onedir)
            if not os.path.exists(onedir):
                os.makedirs(onedir)

            # 交给调度器入队列
            yield scrapy.Request(
                url=one_link,
                meta={'item':item,'onedir':onedir},
                callback=self.parse_two_html
            )

    def parse_two_html(self,response):
        # 取出上一个函数传递过来的item对象
        item = response.meta['item']
        onedir = response.meta['onedir']

        article_list = response.xpath('//article')
        for article in article_list:
            item['name'] = article.xpath('./a/text()').get().replace(' ','-')
            # Windows下如果文件名中有特殊字符如何处理
            all_chars = '*<>|?\/:"'
            for char in item['name']:
                if char in all_chars:
                    item['name'] = item['name'].replace(char,'_')

            two_link = article.xpath('./a/@href').get()
            # 1.创建二级文件夹
            twodir = onedir + item['name'] + '/'
            if not os.path.exists(twodir):
                os.makedirs(twodir)

            # 2.交给调度器
            yield scrapy.Request(
                url=two_link,
                meta={'item':item,'twodir':twodir},
                callback=self.parse_three_html
            )
    # 解析三级页面: 小说内容
    def parse_three_html(self,response):
        item = response.meta['item']
        twodir = response.meta['twodir']

        # p_list: ['段落1','段落2','段落3']
        p_list = response.xpath('//article[@class="article-content"]//p/text()').extract()
        item['content'] = '\n'.join(p_list)
        # 想办法拼接绝对路径文件名 xxx.txt
        item['filename'] = twodir+item['name']+'.txt'

        yield item
```

**4、管道文件实现数据处理 - pipelines.py**


```python
class DaomuPipeline(object):
    def process_item(self, item, spider):
        filename = item['filename']
        with open(filename,'w') as f:
            f.write(item['content'])
        print('%s下载成功' % filename)

        return item
```

**5、全局配置 - setting.py**

**6、运行文件 - run.py**

## **今日作业**

```python
1、scrapy框架有哪几大组件？以及各个组件之间是如何工作的？
2、腾讯招聘尝试改写为scrapy
   response.text ：获取页面响应内容
3、豆瓣电影尝试改为scrapy
```

# DAY10



## **Day09回顾**

### **scrapy框架**

- 五大组件

```python
引擎（Engine）
爬虫程序（Spider）
调度器（Scheduler）
下载器（Downloader）
管道文件（Pipeline）
# 两个中间件
下载器中间件（Downloader Middlewares）
蜘蛛中间件（Spider Middlewares）
```

- 工作流程

```python
1、Engine向Spider索要URL,交给Scheduler入队列
2、Scheduler处理后出队列,通过Downloader Middlewares交给Downloader去下载
3、Downloader得到响应后,通过Spider Middlewares交给Spider
4、Spider数据提取：
   1、数据交给Pipeline处理
   2、需要跟进URL,继续交给Scheduler入队列，依次循环
```

- 常用命令

```python
# 创建爬虫项目
scrapy startproject 项目名

# 创建爬虫文件
cd 项目文件夹
scrapy genspider 爬虫名 域名

# 运行爬虫
scrapy crawl 爬虫名
```

- scrapy项目目录结构

```
Baidu
├── Baidu               # 项目目录
│   ├── items.py        # 定义数据结构
│   ├── middlewares.py  # 中间件
│   ├── pipelines.py    # 数据处理
│   ├── settings.py     # 全局配置
│   └── spiders
│       ├── baidu.py    # 爬虫文件
└── scrapy.cfg          # 项目基本配置文件
```

- settings.py全局配置

```python
1、USER_AGENT = 'Mozilla/5.0'
2、ROBOTSTXT_OBEY = False
3、CONCURRENT_REQUESTS = 32
4、DOWNLOAD_DELAY = 1
5、DEFAULT_REQUEST_HEADERS={}
6、ITEM_PIPELINES={'项目目录名.pipelines.类名':300}
```

### **创建项目流程**

```python
1、scrapy startproject Tencent
2、cd Tencent
3、scrapy genspider tencent tencent.com
4、items.py(定义爬取数据结构)
   import scrapy
   class TencentItem(scrapy.Item):
       job_name = scrapy.Field()
5、tencent.py（写爬虫文件）
   import scrapy
   class TencentSpider(scarpy.Spider):
      name = 'tencent'
      allowed_domains = ['tencent.com']
      start_urls = ['http://tencent.com/']
      def parse(self,response):
        xxx 
        yield item
6、pipelines.py(数据处理)
   class TencentPipeline(object):
      def process_item(self,item,spider):
          return item
7、settings.py(全局配置)
  LOG_LEVEL = ''
  LOG_FILE = ''
  FEED_EXPORT_ENCODING = ''
8、终端：scrapy crawl tencent
```

### **响应对象属性及方法**

```python
# 属性
1、response.text ：获取响应内容 - 字符串
2、response.body ：获取bytes数据类型
3、response.xpath('')

# response.xpath('')调用方法
1、结果 ：列表,元素为选择器对象
  # <selector xpath='//article' data=''>
2、.extract() ：提取文本内容,将列表中所有元素序列化为Unicode字符串
3、.extract_first() ：提取列表中第1个文本内容
4、.get() ： 提取列表中第1个文本内容
```

### **爬虫项目启动方式**

- **方式一**

```python
从爬虫文件(spider)的start_urls变量中遍历URL地址，把下载器返回的响应对象（response）交给爬虫文件的parse()函数处理
# start_urls = ['http://www.baidu.com/']
```

- **方式二**

```python
重写start_requests()方法，从此方法中获取URL，交给指定的callback解析函数处理

1、去掉start_urls变量
2、def start_requests(self):
      # 生成要爬取的URL地址，利用scrapy.Request()方法交给调度器 **
```

### **日志级别**

```python
DEBUG < INFO < WARNING < ERROR < CRITICAL
```

### **数据持久化存储(MySQL、MongoDB)**

```python
1、在setting.py中定义相关变量
2、pipelines.py中新建管道类，并导入settings模块
	def open_spider(self,spider):
		# 爬虫开始执行1次,用于数据库连接
	def process_item(self,item,spider):
        # 用于处理抓取的item数据
	def close_spider(self,spider):
		# 爬虫结束时执行1次,用于断开数据库连接
3、settings.py中添加此管道
	ITEM_PIPELINES = {'':200}

# 注意 ：process_item() 函数中一定要 return item ***
```

### **保存为csv、json文件**

- 命令格式

```python
scrapy crawl maoyan -o maoyan.csv
scrapy crawl maoyan -o maoyan.json
# settings.py  FEED_EXPORT_ENCODING = 'utf-8'
```

### **settings.py常用变量**

```python
# 1、设置日志级别
LOG_LEVEL = ''
# 2、保存到日志文件(不在终端输出)
LOG_FILE = ''
# 3、设置数据导出编码(主要针对于json文件)
FEED_EXPORT_ENCODING = ''
# 4、非结构化数据存储路径
IMAGES_STORE = '路径'
# 5、设置User-Agent
USER_AGENT = ''
# 6、设置最大并发数(默认为16)
CONCURRENT_REQUESTS = 32
# 7、下载延迟时间(每隔多长时间请求一个网页)
# DOWNLOAD_DELAY 会影响 CONCURRENT_REQUESTS，不能使并发显现
# 有CONCURRENT_REQUESTS，没有DOWNLOAD_DELAY： 服务器会在同一时间收到大量的请求
# 有CONCURRENT_REQUESTS，有DOWNLOAD_DELAY 时，服务器不会在同一时间收到大量的请求
DOWNLOAD_DELAY = 3
# 8、请求头
DEFAULT_REQUEST_HEADERS = {}
# 9、添加项目管道
ITEM_PIPELINES = {}
# 10、添加下载器中间件
DOWNLOADER_MIDDLEWARES = {}
```

### **scrapy.Request()参数**

```python
1、url
2、callback
3、meta ：传递数据,定义代理
```

## **Day10笔记**

## **作业讲解 - 腾讯招聘**

- **1、创建项目+爬虫文件**

```python
scrapy startproject Tencent
cd Tencent
scrapy genspider tencent hr.tencent.com

# 一级页面(postId):
https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566266592644&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword=&pageIndex={}&pageSize=10&language=zh-cn&area=cn

# 二级页面
https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1566266695175&postId={}&language=zh-cn
```

- **2、定义爬取的数据结构**

```python
# 名称+类别+职责+要求+地址+时间
job_name = scrapy.Field()
job_type = scrapy.Field()
job_duty = scrapy.Field()
job_require = scrapy.Field()
job_address = scrapy.Field()
job_time = scrapy.Field()
```

- **3、爬虫文件**

```python
import scrapy
import json
from ..items import TencentItem
from urllib import parse
import requests

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['careers.tencent.com']
    one_url = 'https://careers.tencent.com/tencentcareer/api/post/Query?timestamp=1566266592644&countryId=&cityId=&bgIds=&productId=&categoryId=&parentCategoryId=&attrId=&keyword={}&pageIndex={}&pageSize=10&language=zh-cn&area=cn'
    two_url = 'https://careers.tencent.com/tencentcareer/api/post/ByPostId?timestamp=1566266695175&postId={}&language=zh-cn'
    user_input = input('请输入工作类型:')

    # 重写start_requests()方法,把一级页面所有地址交给调度器
    def start_requests(self):
        # 给user_input进行编码
        user_input = parse.quote(self.user_input)
        # 获取到总页数:total
        total = self.get_total(user_input)
        for index in range(1,total):
            url = self.one_url.format(user_input,index)
            yield scrapy.Request(
                url = url,
                callback = self.parse_one_page
            )
    # 获取总页数
    def get_total(self,user_input):
        url = self.one_url.format(user_input,1)
        html = requests.get(url=url).json()
        total = html['Data']['Count'] // 10 + 1

        return total

    def parse_one_page(self, response):
        html = response.text
        html = json.loads(html)
        for job in html['Data']['Posts']:

            post_id = job['PostId']
            url = self.two_url.format(post_id)
            yield scrapy.Request(
                url = url,
                callback = self.parse_two_page
            )

    # 解析二级页面
    def parse_two_page(self,response):
        item = TencentItem()
        html = json.loads(response.text)['Data']
        item['job_name'] = html['RecruitPostName']
        item['job_type'] = html['CategoryName']
        item['job_duty'] = html['Responsibility']
        item['job_require'] = html['Requirement']
        item['job_address'] = html['LocationName']
        item['job_time'] = html['LastUpdateTime']

        yield item
```

- **4、管道文件**

```mysql
create database tencentdb charset utf8;
use tencentdb;
create table tencenttab(
job_name varchar(500),
job_type varchar(100),
job_duty varchar(1000),
job_require varchar(1000),
job_address varchar(100),
job_time varchar(100)
)charset=utf8;
```

   管道文件pipelines实现

```python
class TencentPipeline(object):
    def process_item(self, item, spider):
        print(dict(item))
        return item

import pymysql

class TencentMysqlPipeline(object):
    def open_spider(self,spider):
        self.db = pymysql.connect(
          'localhost','root','123456','tencentdb',charset='utf8'
        )
        self.cursor = self.db.cursor()

    def process_item(self,item,spider):
        ins='insert into tencenttab values(%s,%s,%s,%s,%s,%s)'
        L = [
            item['job_name'],
            item['job_type'],
            item['job_duty'],
            item['job_require'],
            item['job_address'],
            item['job_time']
        ]
        self.cursor.execute(ins,L)
        self.db.commit()

        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.db.close()
```

- **5、settings.py**

```python
# 定义常用变量，添加管道即可
```

## **图片管道(360图片抓取案例)**

- **目标** 

```python
www.so.com -> 图片 -> 美女
```

- **抓取网络数据包**

```python
2、F12抓包,抓取到json地址 和 查询参数(QueryString)
      url = 'http://image.so.com/zjl?ch=beauty&sn={}&listtype=new&temp=1'.format(sn)
      ch: beauty
      sn: 90
      listtype: new
      temp: 1
```

- **项目实现**

**1、创建爬虫项目和爬虫文件**

```python
scrapy startproject So
cd So
scrapy genspider so image.so.com
```

**2、定义要爬取的数据结构(items.py)**

```python
img_link = scrapy.Field()
img_title = scrapy.Field()
```

**3、爬虫文件实现图片链接+名字抓取**

```python
import scrapy
import json
from ..items import SoItem

class SoSpider(scrapy.Spider):
    name = 'so'
    allowed_domains = ['image.so.com']
    url = 'http://image.so.com/zjl?ch=beauty&sn={}&listtype=new&temp=1'

    def start_requests(self):
        for sn in range(0,100,30):
            url = self.url.format(sn)
            yield scrapy.Request(
                url = url,
                callback = self.parse_page,
                dont_filter=False
            )

    def parse_page(self, response):
        html = json.loads(response.text)
        item = SoItem()
        for img in html['list']:
            item['img_url'] = img['qhimg_url']
            item['img_title'] = img['title']

            yield item
```

**4、管道文件（pipelines.py）**

```python
from scrapy.pipelines.images import ImagesPipeline

class SoPipeline(ImagesPipeline):
  	# 重写 get_media_requests()方法
    def get_media_requests(self,item,info):
        yield scrapy.Request(
          url = item['img_url'],
          meta = {'item':item['img_title']}
        )
    
    # 重写 file_path()方法
    def file_path(self,request,response=None,info=None):
        title = request.meta['item']
        filename = title+'.'+request.url.split('.')[-1]
        return filename
```

**5、设置settings.py**

```python
IMAGES_STORE = '/home/tarena/images/'
```

**6、创建run.py运行爬虫**

**字符串方法总结**

```python
1、strip()
2、split()
3、replace('','')
4、''.join()
5、字符串切片(正向切,反向切) : S[-10:]
```

## **scrapy shell的使用**

- **基本使用**

```python
# scrapy shell URL地址
*1、request.url     : 请求URL地址
*2、request.headers ：请求头(字典)
*3、reqeust.meta  ：item数据传递，定义代理(字典)

4、response.text    ：字符串
5、response.body    ：bytes
6、response.xpath('')
```

- **scrapy.Request()参数**

```python
1、url
2、callback
3、headers
4、meta ：传递数据,定义代理
5、dont_filter ：是否忽略域组限制
   默认False,检查allowed_domains['']
```

## **设置中间件(随机User-Agent)**

### **少量User-Agent切换**

- **方法一**

```python
# settings.py
USER_AGENT = ''
DEFAULT_REQUEST_HEADERS = {}
```

- **方法二**

```python
# spider
yield scrapy.Request(url,callback=函数名,headers={})
```

### **大量User-Agent切换（中间件）**

- **middlewares.py设置中间件**

```python
1、获取User-Agent
   # 方法1 ：新建useragents.py,存放大量User-Agent，random模块随机切换
   # 方法2 ：安装fake_useragent模块(sudo pip3 install fack_useragent)
       from fake_useragent import UserAgent
       ua_obj = UserAgent()
       ua = ua_obj.random
2、middlewares.py新建中间件类
	class RandomUseragentMiddleware(object):
		def process_request(self,reuqest,spider):
    		ua = UserAgent()
    		request.headers['User-Agent'] = ua.random
3、settings.py添加此下载器中间件
	DOWNLOADER_MIDDLEWARES = {'' : 优先级}
```

## **设置中间件(随机代理)**

```python
class RandomProxyDownloaderMiddleware(object):
    def process_request(self,request,spider):
    	request.meta['proxy'] = xxx
        
    def process_exception(self,request,exception,spider):
        return request
```

## **Fiddler抓包工具**

- **配置Fiddler**

```python
# 添加证书信任
1、Tools - Options - HTTPS
   勾选 Decrypt Https Traffic 后弹出窗口，一路确认
# 设置只抓取浏览器的数据包
2、...from browsers only
# 设置监听端口（默认为8888）
3、Tools - Options - Connections
# 配置完成后重启Fiddler（重要）
4、关闭Fiddler,再打开Fiddler
```

- **配置浏览器代理**

```python
1、安装Proxy SwitchyOmega插件
2、浏览器右上角：SwitchyOmega->选项->新建情景模式->AID1904(名字)->创建
   输入 ：HTTP://  127.0.0.1  8888
   点击 ：应用选项
3、点击右上角SwitchyOmega可切换代理
```

- **Fiddler常用菜单**

```python
1、Inspector ：查看数据包详细内容
   整体分为请求和响应两部分
2、常用菜单
   Headers ：请求头信息
   WebForms
     # 1. POST请求Form表单数据 ：<body>
     # 2. GET请求查询参数: <QueryString>
   Raw
   将整个请求显示为纯文本
```


# **Day10回顾**

## **settings.py常用变量**

```python
# 1、设置日志级别
LOG_LEVEL = ''
# 2、保存到日志文件(不在终端输出)
LOG_FILE = ''
# 3、设置数据导出编码(主要针对于json文件)
FEED_EXPORT_ENCODING = ''
# 4、非结构化数据存储路径
IMAGES_STORE = '路径'
# 5、设置User-Agent
USER_AGENT = ''
# 6、设置最大并发数(默认为16)
CONCURRENT_REQUESTS = 32
# 7、下载延迟时间(每隔多长时间请求一个网页)
DOWNLOAD_DELAY = 3
# 8、请求头
DEFAULT_REQUEST_HEADERS = {}
# 9、添加项目管道
ITEM_PIPELINES = {}
# 10、添加下载器中间件
DOWNLOADER_MIDDLEWARES = {}
```

## **非结构化数据抓取**

```python
1、spider
   yield item['链接']
2、pipelines.py
   from scrapy.pipelines.images import ImagesPipeline
   import scrapy
   class TestPipeline(ImagesPipeline):
      def get_media_requests(self,item,info):
            yield scrapy.Request(url=item['url'],meta={'item':item['name']})
      def file_path(self,request,response=None,info=None):
            name = request.meta['item']
            filename = name
            return filename
3、settings.py
   IMAGES_STORE = 'D:\\Spider\\images'
```

## **scrapy.Request()**

```python
# 参数
1、url
2、callback
3、headers
4、meta ：传递数据,定义代理
5、dont_filter ：是否忽略域组限制 - 默认False,检查allowed_domains['']
# request属性
1、request.url
2、request.headers
3、request.meta
4、request.method
# response属性
1、response.url
2、response.text
3、response.body
4、response.meta
5、response.encoding
```

## **设置中间件**

**随机User-Agent**

```python
# 1、middlewares.py
class RandomUaDownloaderMiddleware(object):
    def process_request(self,request,spider):
    	request.header['User-Agent'] = xxx
# 2、settings.py
DOWNLOADER_MIDDLEWARES = {'xxx.middlewares.xxx':300}
```

**随机代理**

```python
# 1、middlewares.py
class RandomProxyDownloaderMiddleware(object):
    def process_request(self,request,spider):
    	request.meta['proxy'] = xxx
        
    def process_exception(self,request,exception,spider):
        return request
# 2、settings.py
DOWNLOADER_MIDDLEWARES = {'xxx.middlewares.xxx':200}
```

## **item对象到底该在何处创建？**

```python
1、一级页面:  都可以,建议在for循环外
2、>=2级页面: for循环内
```

# **Day11笔记**

## **分布式爬虫**

### **分布式爬虫介绍**

> 什么是分布式爬虫
>默认情况下scrapy是单机爬虫,只能在一台电脑上运行
>分布式爬虫用一个共同的程序,同时部署到多台电脑上运行,所有程序 共享爬取队列




- **原理**

```python
多台主机共享1个爬取队列
```

- **实现** 

```python
重写scrapy调度器(scrapy_redis模块)
```

- **为什么使用redis**

```python
1、Redis基于内存,速度快
2、Redis非关系型数据库,Redis中集合,存储每个request的指纹
3、scrapy_redis安装
	sudo pip3 install scrapy_redis
```

## **scrapy_redis详解**

- **GitHub地址**

  ```python
  https://github.com/rmax/scrapy-redis
  ```

- **settings.py说明**

  ```python
  # 重新指定调度器: 启用Redis调度存储请求队列
  SCHEDULER = "scrapy_redis.scheduler.Scheduler"
  
  # 重新指定去重机制: 确保所有的爬虫通过Redis去重
  DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
  
  # 不清除Redis队列: 暂停/恢复/断点续爬
  SCHEDULER_PERSIST = True
  
  # 优先级队列 （默认）
  SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.PriorityQueue'
  #可选用的其它队列
  # 先进先出队列
  SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.FifoQueue'
  # 后进先出队列
  SCHEDULER_QUEUE_CLASS = 'scrapy_redis.queue.LifoQueue'
  
  # redis管道
  ITEM_PIPELINES = {
      'scrapy_redis.pipelines.RedisPipeline': 300
  }
  
  #指定连接到redis时使用的端口和地址
  REDIS_HOST = 'localhost'
  REDIS_PORT = 6379
  ```

## **腾讯招聘分布式改写**

### **1、正常项目数据抓取（非分布式）**

### **2、改写为分布式（同时存入redis）**

**1、settings.py**

```python
# 使用scrapy_redis的调度器
SCHEDULER = "scrapy_redis.scheduler.Scheduler"
# 使用scrapy_redis的去重机制
DUPEFILTER_CLASS = "scrapy_redis.dupefilter.RFPDupeFilter"
# 是否清除请求指纹,True:不清除 False:清除
SCHEDULER_PERSIST = True
# 在ITEM_PIPELINES中添加redis管道
'scrapy_redis.pipelines.RedisPipeline': 200
# 定义redis主机地址和端口号
REDIS_HOST = '111.111.111.111'
REDIS_PORT = 6379
```

#### **改写为分布式（同时存入mysql）**

- **修改管道**

```python
ITEM_PIPELINES = {
   'Tencent.pipelines.TencentPipeline': 300,
   # 'scrapy_redis.pipelines.RedisPipeline': 200
   'Tencent.pipelines.TencentMysqlPipeline':200,
}
```

- **清除redis数据库**

```python
flushdb
```

- **代码拷贝一份到分布式中其他机器，两台或多台机器同时执行此代码**

## **腾讯招聘分布式改写- 方法二**

- **使用redis_key改写**

  ```python
  # 第一步: settings.py无须改动
  settings.py和上面分布式代码一致
  # 第二步:tencent.py
  from scrapy_redis.spiders import RedisSpider
  class TencentSpider(RedisSpider):
      # 1. 去掉start_urls
      # 2. 定义redis_key
      redis_key = 'tencent:spider'
      def parse(self,response):
          pass
  # 第三步:把代码复制到所有爬虫服务器，并启动项目
  # 第四步
    到redis命令行，执行LPUSH命令压入第一个要爬取的URL地址
    >LPUSH tencent:spider 第1页的URL地址
  
  # 项目爬取结束后无法退出，如何退出？
  setting.py
  CLOSESPIDER_TIMEOUT = 3600
  # 到指定时间(3600秒)时,会自动结束并退出
  ```

## **scrapy - post请求**

- **方法+参数**

```python
scrapy.FormRequest(
    url=posturl,
    formdata=formdata,
    callback=self.parse
)
```

- **有道翻译案例实现**

**1、创建项目+爬虫文件**

```python
scrapy startproject Youdao
cd Youdao
scrapy genspider youdao fanyi.youdao.com
```

**2、items.py**

```python
result = scrapy.Field()
```

**3、youdao.py**

```python
# -*- coding: utf-8 -*-
import scrapy
import time
import random
from hashlib import md5
import json
from ..items import YoudaoItem

class YoudaoSpider(scrapy.Spider):
    name = 'youdao'
    allowed_domains = ['fanyi.youdao.com']
    word = input('请输入要翻译的单词:')

    def start_requests(self):
        post_url = 'http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule'
        salt, sign, ts = self.get_salt_sign_ts(self.word)
        formdata = {
                  'i': self.word,
                  'from': 'AUTO',
                  'to': 'AUTO',
                  'smartresult': 'dict',
                  'client': 'fanyideskweb',
                  'salt': salt,
                  'sign': sign,
                  'ts': ts,
                  'bv': 'cf156b581152bd0b259b90070b1120e6',
                  'doctype': 'json',
                  'version': '2.1',
                  'keyfrom': 'fanyi.web',
                  'action': 'FY_BY_REALTlME'
            }
	   # 发送post请求的方法
        yield scrapy.FormRequest(url=post_url,formdata=formdata)

    def get_salt_sign_ts(self, word):
        # salt
        salt = str(int(time.time() * 1000)) + str(random.randint(0, 9))
        # sign
        string = "fanyideskweb" + word + salt + "n%A-rKaT5fb[Gy?;N5@Tj"
        s = md5()
        s.update(string.encode())
        sign = s.hexdigest()
        # ts
        ts = str(int(time.time() * 1000))
        return salt, sign, ts

    def parse(self, response):
        item = YoudaoItem()
        html = json.loads(response.text)
        item['result'] = html['translateResult'][0][0]['tgt']

        yield item
```

**4、settings.py**

```python
1、ROBOTSTXT_OBEY = False
2、LOG_LEVEL = 'WARNING'
3、COOKIES_ENABLED = False
4、DEFAULT_REQUEST_HEADERS = {
      "Cookie": "OUTFOX_SEARCH_USER_ID=970246104@10.169.0.83; OUTFOX_SEARCH_USER_ID_NCOO=570559528.1224236; _ntes_nnid=96bc13a2f5ce64962adfd6a278467214,1551873108952; JSESSIONID=aaae9i7plXPlKaJH_gkYw; td_cookie=18446744072941336803; SESSION_FROM_COOKIE=unknown; ___rl__test__cookies=1565689460872",
      "Referer": "http://fanyi.youdao.com/",
      "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.100 Safari/537.36",
    }
```

**scrapy添加cookie的三种方式**

```python
# 1、修改 settings.py 文件
1、COOKIES_ENABLED = False  取消注释
2、DEFAULT_REQUEST_HEADERS = {}   添加Cookie

# 2、DownloadMiddleware
def process_request(self,request,spider):
    request.cookies={}

# 3、爬虫文件
def start_requests(self):
    yield scrapy.Request(url=url,cookies={},callback=xxx)
```



## **机器视觉与tesseract**

### **作用**

```python
处理图形验证码
```

### **三个重要概念**

- OCR

```python
# 定义
OCR: 光学字符识别(Optical Character Recognition)
# 原理
通过扫描等光学输入方式将各种票据、报刊、书籍、文稿及其它印刷品的文字转化为图像信息，再利用文字识别技术将图像信息转化为电子文本
```

- 
  tesserct-ocr

```python
OCR的一个底层识别库（不是模块，不能导入）
# Google维护的开源OCR识别库
```

- pytesseract

```python
Python模块,可调用底层识别库
# 对tesseract-ocr做的一层Python API封装
```

### **安装tesseract-ocr**

- Ubuntu

```python
sudo apt-get install tesseract-ocr
```

- Windows

```python
1、下载安装包
2、添加到环境变量(Path)
```

- 测试

```python
# 终端 | cmd命令行
tesseract xxx.jpg 文件名
```

### **安装pytesseract**

- 安装

```python
sudo pip3 install pytesseract
```

- 使用

```python
import pytesseract
# Python图片处理标准库
from PIL import Image

# 创建图片对象
img = Image.open('test1.jpg')
# 图片转字符串
result = pytesseract.image_to_string(img)
print(result)
```

- 爬取网站思路（验证码）

```python
1、获取验证码图片
2、使用PIL库打开图片
3、使用pytesseract将图片中验证码识别并转为字符串
4、将字符串发送到验证码框中或者某个URL地址
```

### **在线打码平台**

- **为什么使用在线打码**

```python
tesseract-ocr识别率很低,文字变形、干扰，导致无法识别验证码
```

- **云打码平台使用步骤**

```python
1、下载并查看接口文档
2、调整接口文档，调整代码并接入程序测试
3、真正接入程序，在线识别后获取结果并使用
```

- **破解云打码网站验证码**

  **1、下载并调整接口文档，封装成函数，打码获取结果**

```python
def get_result(filename):
    # 用户名
    username    = 'yibeizi001'

    # 密码
    password    = 'zhanshen002'

    # 软件ＩＤ，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appid       = 1

    # 软件密钥，开发者分成必要参数。登录开发者后台【我的软件】获得！
    appkey      = '22cc5376925e9387a23cf797cb9ba745'

    # 图片文件
    # filename    = 'getimage.jpg'

    # 验证码类型，# 例：1004表示4位字母数字，不同类型收费不同。请准确填写，否则影响识别率。在此查询所有类型 http://www.yundama.com/price.html
    codetype    = 5000

    # 超时时间，秒
    timeout     = 60

    # 初始化
    yundama = YDMHttp(username, password, appid, appkey)

    # 登陆云打码
    uid = yundama.login();

    # 查询余额
    balance = yundama.balance();

    # 开始识别，图片路径，验证码类型ID，超时时间（秒），识别结果
    cid, result = yundama.decode(filename, codetype, timeout);

    return result

######################################################################
```
​	**2、访问云打码网站，获取验证码并在线识别**

```python
from selenium import webdriver
from ydmapi import *
# 处理图片
from PIL import Image

# options = webdriver.ChromeOptions()
# options.add_argument('windows-size=1900x3000')

class AttackYdm(object):
    def __init__(self):
        self.browser = webdriver.Chrome()


    # 获取网站首页截图
    def get_screen_shot(self):
        self.browser.get('http://www.yundama.com')
        self.browser.save_screenshot('index.png')

    # 从首页截图中截取验证码图片
    def get_caphe(self):
        # 定位验证码元素的位置(x y坐标)
        location = self.browser.find_element_by_xpath(
            '//*[@id="verifyImg"]'
        ).location
        # 大小(宽度和高度)
        size = self.browser.find_element_by_xpath(
            '//*[@id="verifyImg"]'
        ).size
        # 左上角x坐标
        left = location['x']
        # 左上角y坐标
        top = location['y']
        # 右下角x坐标
        right = location['x']  + size['width']
        # 右下角y坐标
        bottom = location['y'] + size['height']

        # 截图验证码图片(crop()):对图片进行剪切,参数为元组
        img = Image.open('index.png').crop((left,top,right,bottom))
        # 保存截取后的图片
        img.save('yzm.png')

        # 调用在线打码平台进行识别
        result = get_result('yzm.png')

        return result

    # 主函数
    def main(self):
        self.get_screen_shot()
        result = self.get_caphe()

        return result
if __name__ == '__main__':
    spider = AttackYdm()
    result = spider.main()
    print('识别结果为:',result)
```

## **Fiddler抓包工具**

- **配置Fiddler**

```python
# 添加证书信任
1、Tools - Options - HTTPS
   勾选 Decrypt Https Traffic 后弹出窗口，一路确认
# 设置只抓取浏览器的数据包
2、...from browsers only
# 设置监听端口（默认为8888）
3、Tools - Options - Connections
# 配置完成后重启Fiddler（重要）
4、关闭Fiddler,再打开Fiddler
```

- **配置浏览器代理**

```python
1、安装Proxy SwitchyOmega插件
2、浏览器右上角：SwitchyOmega->选项->新建情景模式->AID1901(名字)->创建
   输入 ：HTTP://  127.0.0.1  8888
   点击 ：应用选项
3、点击右上角SwitchyOmega可切换代理
```

- **Fiddler常用菜单**

```python
1、Inspector ：查看数据包详细内容
   整体分为请求和响应两部分
2、常用菜单
   Headers ：请求头信息
   WebForms: POST请求Form表单数据 ：<body>
   GET请求查询参数: <QueryString>
   Raw
   将整个请求显示为纯文本
```

## **移动端app数据抓取**

**方法1 - 手机 + Fiddler**

```python
设置方法见文件夹 - 移动端抓包配置
```

**方法2 - F12浏览器工具**

**有道翻译手机版破解案例**

```python
import requests
from lxml import etree

word = input('请输入要翻译的单词:')

post_url = 'http://m.youdao.com/translate'
post_data = {
  'inputtext':word,
  'type':'AUTO'
}

html = requests.post(url=post_url,data=post_data).text
parse_html = etree.HTML(html)
xpath_bds = '//ul[@id="translateResult"]/li/text()'
result = parse_html.xpath(xpath_bds)[0]

print(result)
```

## **爬虫总结**

```python
# 1、什么是爬虫
  爬虫是请求网站并提取数据的自动化程序

# 2、robots协议是什么
  爬虫协议或机器人协议,网站通过robots协议告诉搜索引擎哪些页面可以抓取，哪些页面不能抓取

# 3、爬虫的基本流程
  1、请求得到响应
  2、解析
  3、保存数据

# 4、请求
  1、urllib
  2、requests
  3、scrapy

# 5、解析
  1、re正则表达式
  2、lxml+xpath解析
  3、json解析模块

# 6、selenium+browser

# 7、常见反爬策略
  1、Headers : 最基本的反爬手段，一般被关注的变量是UserAgent和Referer，可以考虑使用浏览器中
  2、UA ： 建立User-Agent池,每次访问页面随机切换
  3、拉黑高频访问IP
     数据量大用代理IP池伪装成多个访问者,也可控制爬取速度
  4、Cookies
     建立有效的cookie池，每次访问随机切换
  5、验证码
    验证码数量较少可人工填写
    图形验证码可使用tesseract识别
    其他情况只能在线打码、人工打码和训练机器学习模型
  6、动态生成
    一般由js动态生成的数据都是向特定的地址发get请求得到的，返回的一般是json
  7、签名及js加密
    一般为本地JS加密,查找本地JS文件,分析,或者使用execjs模块执行JS
  8、js调整页面结构
  9、js在响应中指向新的地址

# 8、scrapy框架的运行机制

# 9、分布式爬虫的原理
  多台主机共享一个爬取队列
```














