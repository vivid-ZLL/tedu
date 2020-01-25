django APPEND_SLASH参数，若为False，django框架不再处理与‘/’有关的信息

# 1，前后端分离

## 1.1 什么是前后端分离

​	前端： 即客户端，负责渲染用户显示界面【如web的js动态渲染页面, 安卓， IOS，pc客户端等】

​	后端：即服务器端，负责接收http请求，处理数据

​	API：Application Programming Interface  是一些预先定义的函数，或指软件系统不同组成部分衔接的约定

​	前后端分离 完整请求过程

​    		1，前端通过http请求后端API

​			2，后端以json形式返回前端数据

​			3，前端生成用户显示界面【如html , ios , android】

​	**判断前后端分离得核心标准： 谁生成显示页面**

​    1，后端生成【前后端未分离】  ex: flask->render_template  django -> HttpResponse(html)

​	2,   前端生成【前后端分离】



## 1.2 优点

​	1，各司其职

​		前端：视觉层面，兼容性，前端性能优化

​		后端：并发，可用性，性能

​	2，解耦，前端和后端均易于扩展

​	3，后端灵活搭配各类前端 - 如安卓等

​	4，提高用户体验

​	5，前端+后端可完全并行开发，加快开发效率



## 1.3 分离常见问题

| 问题                                                         | 答案                                                         |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| 如何解决http无状态？                                         | 采用token(详情见下方章节)                                    |
| 如果前端为JS，如何解决跨域问题？                             | 采用CORS(详情见下方章节)                                     |
| 如何解决csrf问题                                             | 采用token                                                    |
| Single Page web Application 是否会影响Search Engine Optimization效果 | 会，前后端分离后，往往页面不存在静态文字【例如新闻的详细内容】 |
| ”老板，这个逻辑到底是让前端做还是后端做啊?“                  | 底线原则: 数据校验需要前后端都做                             |
| ”老板，前端工作压力太大了啊“                                 | 团队协作不能只是嘴上说说                                     |
| 动静分离和前后端分离是一个意思么？                           | 动静分离指的是 css/js/img这类静态资源跟服务器拆开部署，典型方案-静态资源交由CDN厂商处理 |



## 1.4  实现方式

1，Django/Flask 后端只返回json

2,	前端 ->  ex: js向服务器发出ajax请求，获取数据，拿到数据后动态生成html

3,	前端服务和后端服务 分开部署



# 2，token - 令牌

## 学前须知：

​	1，base64 '防君子不防小人' 

| 方法              | 作用                                                  | 参数                                           | 返回值                                                    |
| ----------------- | ----------------------------------------------------- | ---------------------------------------------- | --------------------------------------------------------- |
| b64encode         | 将输入的参数转化为base64规则的串                      | 预加密的明文，类型为bytes；例：b‘guoxiaonao’   | base64对应编码的密文，类型为bytes；例:b'Z3VveGlhb25hbw==' |
| b64decode         | 将base64串 解密回 明文                                | base64密文,类型为bytes;例：b'Z3VveGlhb25hbw==' | 参数对应的明文，类型为bytes；例：b'guoxiaonao'            |
| urlsafe_b64encode | 作用同b64encode,但是会将 '+'替换成 '-',将'/'替换成'_' | 同b64encode                                    | 同b64encode                                               |
| urlsafe_b64decode | 作用同b64decode                                       | 同b64decode                                    | 同b64decode                                               |

代码演示:

```python
import base64
#base64加密
s = b'guoxiaonao'
b_s = base64.b64encode(s)
#b_s打印结果为 b'Z3VveGlhb25hbw=='

#base64解密
ss = base64.b64decode(b_s)
#ss打印结果为 b'guoxiaonao'

```

​	2，SHA-256  安全散列算法的一种（hash）

​	hash三大特点：

​	1）定长输出    2）不可逆    3） 雪崩

```python
import hashlib
s = hashlib.sha256() #创建sha256对象
s.update(b'xxxx')  #添加欲hash的内容，类型为 bytes
s.digest()  #获取最终结果


```

​	3，HMAC-SHA256 是一种通过特别计算方式之后产生的消息认证码，使用**散列算法**同时结合一个**加密密钥**。它可以用来保证数据的完整性，同时可以用来作某个消息的身份验证

```python
import hmac
#生成hmac对象
#第一个参数为加密的key，bytes类型，
#第二个参数为欲加密的串，bytes类型
#第三个参数为hmac的算法，指定为SHA256
h = hmac.new(key, str, digestmod='SHA256 ') 
h.digest() #获取最终结果
```

​	4，RSA256 非对称加密

​		1，加密： 公钥加密，私钥解密

​		2，签名： 私钥签名， 公钥验签

## 2.1 JWT -  json-web-token  

### 1，三大组成

​	1，header

​		格式为字典-元数据格式如下

```python
{'alg':'HS256', 'typ':'JWT'}
#alg代表要使用的 算法
#typ表明该token的类别 - 此处必须为 大写的 JWT
```

​		 该部分数据需要转成json串并用base64 加密



​	2，payload

​		格式为字典-此部分分为公有声明和私有声明

  	  公共声明：JWT提供了内置关键字用于描述常见的问题

此部分均为**可选项**，用户根据自己需求 按需添加key，常见公共声明如下：

```python
{'exp':xxx, # Expiration Time 此token的过期时间的时间戳
 'iss':xxx，# (Issuer) Claim 指明此token的签发者
 'aud':xxx, #(Audience) Claim 指明此token的
 'iat':xxx, # (Issued At) Claim 指明此创建时间的时间戳
 'aud':xxx, # (Audience) Claim	指明此token签发面向群体
}
```

​		私有声明：用户可根据自己业务需求，添加自定义的key，例如如下：

```python
{'username': 'guoxiaonao'}
```

​		公共声明和私有声明均在同一个字典中；转成json串并用base64加密

​	3，signature 签名

​		签名规则如下：

​		根据header中的alg确定 具体算法，以下用 HS256为例

​		HS256(自定义的key ,   base64后的header + '.' + base64后的payload)

​        解释：用自定义的key, 对base64后的header + '.' + base64后的payload进行hmac计算

### 2，jwt结果格式

​		base64(header) + '.' + base64(payload) + '.' +  base64(sign)

​		最终结果如下： b'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ1c2VybmFtZSI6Imd1b3hpYW9uYW8iLCJpc3MiOiJnZ2cifQ.Zzg1u55DCBqPRGf9z3-NAn4kbA-MJN83SxyLFfc5mmM'

### 3，校验jwt规则

​		1，解析header, 确认alg

​		2，签名校验 - 根据传过来的header和payload按 alg指明的算法进行签名，将签名结果和传过来的sign进行对比，若对比一致，则校验通过

​		3，获取payload自定义内容

### 4，pyjwt 

​	1，安装 pip3 install pyjwt

| 方法                            | 参数说明                                                     | 返回值                                        |
| ------------------------------- | ------------------------------------------------------------ | --------------------------------------------- |
| encode(payload, key, algorithm) | payload:  jwt三大组成中的payload,需要组成字典，按需添加公有声明和私有声明<br />例如: {'username': 'guoxiaonao', 'exp': 1562475112}<br />参数类型： dict | token串<br />返回类型：bytes                  |
|                                 | key : 自定义的加密key<br />参数类型：str                     |                                               |
|                                 | algorithm:  需要使用的加密算法[HS256, RSA256等] <br />参数类型：str |                                               |
| decode(token,key,algorithm,)    | token:   token串<br />参数类型： bytes/str                   | payload明文<br />返回类型：dict               |
|                                 | key : 自定义的加密key ,需要跟encode中的key保持一致<br />参数类型：str |                                               |
|                                 | algorithm:  同encode                                         |                                               |
|                                 | issuer:  发布者，若encode payload中添加 'iss' 字段，则可针对该字段校验<br />参数类型：str | 若iss校验失败，则抛出jwt.InvalidIssuerError   |
|                                 | audience：签发的受众群体，若encode payload中添加'aud'字段，则可针对该字段校验<br />参数类型：str | 若aud校验失败，则抛出jwt.InvalidAudienceError |

**PS**:  若encode得时候 payload中添加了exp字段; 则exp字段得值需为 当前时间戳+此token得有效期时间， 例如希望token 300秒后过期  {'exp': time.time() + 300};  在执行decode时，若检查到exp字段，且token过期，则抛出jwt.ExpiredSignatureError



# 3， CORS - Cross-origin resource sharing - 跨域资源共享

## 1，什么是CORS

​		允许浏览器向跨源(协议 + 域名 + 端口)服务器，发出XMLHttpRequest请求，从而克服了AJAX只能同源使用的限制

## 2，特点

​		1，浏览器自动完成（在请求头中加入特殊头 或 发送特殊请求）

​		2，服务器需要支持（响应头中需要有特殊头）

## 3，简单请求(Simple requests)和预检请求(Preflighted requests)

​		**满足以下全部条件**的请求为 **简单请求**

​			1，请求方法如下：

​					GET  or HEAD or POST

​			2，请求头仅包含如下：

​					Accept

​					Accept-Language

​					Content-Language

​					Content-Type

​			3，Content-Type 仅支持如下三种：

​					application/x-www-form-urlencoded

​					multipart/form-data

​					text/plain

​			**不满足以上任意一点的请求都是 预检请求**

## 4，简单请求发送流程

​		1，请求

​				请求头中 携带 Origin，该字段表明自己来自哪个域

​		2，响应

​				如果请求头中的Origin在服务器接受范围内， 则返回如下头

| 响应头                           | 作用                                                         | 备注 |
| -------------------------------- | ------------------------------------------------------------ | ---- |
| Access-Control-Allow-Origin      | 服务器接受得域                                               |      |
| Access-Control-Allow-Credentials | 是否接受Cooike                                               | 可选 |
| Access-Control-Expose-Headers    | 默认情况下，xhr只能拿到如下响应头：Cache-Control，Content-Language，Content-Type，Expires，Last-Modified；如果有需要获取其他头，需在此指定 | 可选 |

​		如果服务器不接受此域，则响应头中不包含 Access-Control-Allow-Origin

## 5，预检请求发送流程

​	1，OPTION 请求发起，携带如下请求头

| 请求头                         | 作用                 | 备注 |
| ------------------------------ | -------------------- | ---- |
| Origin                         | 表明此请求来自哪个域 | 必选 |
| Access-Control-Request-Method  | 此次请求使用方法     | 必选 |
| Access-Control-Request-Headers | 此次请求使用的头     | 必选 |

​	2，OPTION 接受响应阶段，携带如下响应头

| 响应头                           | 作用                                                         | 备注 |
| -------------------------------- | ------------------------------------------------------------ | ---- |
| Access-Control-Allow-Origin      | 同简单请求                                                   | 必选 |
| Access-Control-Allow-Methods     | 告诉浏览器，服务器接受得跨域请求方法                         | 必选 |
| Access-Control-Allow-Headers     | 返回所有支持的头部，当request有<br/>			‘Access-Control-Request-Headers’时，该响应头必然回复 | 必选 |
| Access-Control-Allow-Credentials | 同简单请求                                                   | 可选 |
| Access-Control-Max-Age           | OPTION请求缓存时间，单位s                                    | 可选 |

​	3，主请求阶段 

| 请求头 | 作用                 | 备注 |
| ------ | -------------------- | ---- |
| Origin | 表明此请求来自哪个域 |      |

​	4，主请求响应阶段

| 响应头                      | 作用               | 备注 |
| --------------------------- | ------------------ | ---- |
| Access-Control-Allow-Origin | 当前服务器接受得域 |      |



## 6，Django支持		   

django-cors-headers官网 https://pypi.org/project/django-cors-headers/

**直接pip 将把django升级到2.0以上，强烈建议用离线安装方式**

配置流程

```python
		1，INSTALLED_APPS 中添加 corsheaders
		2，MIDDLEWARE 中添加 corsheaders.middleware.CorsMiddleware
		   位置尽量靠前，官方建议 ‘django.middleware.common.CommonMiddleware’ 上方
		3，CORS_ORIGIN_ALLOW_ALL  布尔值  如果为True 白名单不启用
		4，CORS_ORIGIN_WHITELIST =[
			"https://example.com"
		]
		5, CORS_ALLOW_METHODS = (
				'DELETE',
				'GET',
				'OPTIONS',
				'PATCH',
				'POST',
				'PUT',
				)
		6, CORS_ALLOW_HEADERS = (
				'accept-encoding',
				'authorization',
				'content-type',
				'dnt',
				'origin',
				'user-agent',
				'x-csrftoken',
				'x-requested-with',
			)
		7, CORS_PREFLIGHT_MAX_AGE  默认 86400s
		8, CORS_EXPOSE_HEADERS  []
		9, CORS_ALLOW_CREDENTIALS  布尔值， 默认False
```


# 4，RESTful -Representational State Transfer

## 4.1，什么是RESTful

​	1，资源 **（Resources）**

​		**网络上的一个实体，或者说是网络上的一个具体信息**，并且每个资源都有一个独一无二得URI与之对应；获取资源-直接访问URI即可

​	2，**表现层（Representation）**

​		如何去表现资源  - 即资源得表现形式；如HTML , xml  , JPG , json等

​	3，**状态转化（State Transfer）**

​		访问一个URI即发生了一次 客户端和服务端得交互；此次交互将会涉及到数据和状态得变化

​		客户端需要通过某些方式触发具体得变化  -  HTTP method 如 GET， POST，PUT，PATCH，DELETE 等



## 4.2 RESTful的特征

​	1，每一个URI代表一种资源

​	2，客户端和服务器端之前传递着资源的某种表现

​	3，客户端通过HTTP的几个动作 对 资源进行操作 - 发生‘状态转化’



## 4.3 如何设计符合RESTful 特征的API

​	1，协议  - http/https

​	2，域名：

​		域名中体现出api字样，如

​		https://api.example.com

​		or

​		https://example.org/api/

​	3,  版本:

​		https://api.example.com/v1/

​	4，路径 -

​		路径中避免使用动词，资源用名词表示，案例如下

```python
https://api.example.com/v1/users
https://api.example.com/v1/animals
```

​	5，HTTP动词语义

- GET（SELECT）：从服务器取出资源（一项或多项）。

- POST（CREATE）：在服务器新建一个资源。

- PUT（UPDATE）：在服务器更新资源（客户端提供改变后的完整资源）。

- PATCH（UPDATE）：在服务器更新资源（客户端提供改变的属性）。

- DELETE（DELETE）：从服务器删除资源。

  具体案例如下：

  ```python
  GET /zoos：列出所有动物园
  POST /zoos：新建一个动物园
  GET /zoos/ID：获取某个指定动物园的信息
  PUT /zoos/ID：更新某个指定动物园的信息（提供该动物园的全部信息）
  PATCH /zoos/ID：更新某个指定动物园的信息（提供该动物园的部分信息）
  DELETE /zoos/ID：删除某个动物园
  GET /zoos/ID/animals：列出某个指定动物园的所有动物
  DELETE /zoos/ID/animals/ID：删除某个指定动物园的指定动物
  ```

  

  ​	6，巧用查询字符串

  ```python
  ?limit=10：指定返回记录的数量
  ?offset=10：指定返回记录的开始位置。
  ?page=2&per_page=100：指定第几页，以及每页的记录数。
  ?sortby=name&order=asc：指定返回结果按照哪个属性排序，以及排序顺序。
  ?type_id=1：指定筛选条件
  ```

  ​	

  ​	7，状态码

  ​		1，用HTTP响应码表达 此次请求结果，例如

  ```python
  200 OK - [GET]：服务器成功返回用户请求的数据
  201 CREATED - [POST/PUT/PATCH]：用户新建或修改数据成功。
  202 Accepted - [*]：表示一个请求已经进入后台排队（异步任务）
  204 NO CONTENT - [DELETE]：用户删除数据成功。
  400 INVALID REQUEST - [POST/PUT/PATCH]：用户发出的请求有错误，服务器没有进行新建或修改数据的操作，该操作是幂等的。
  401 Unauthorized - [*]：表示用户没有权限（令牌、用户名、密码错误）。
  403 Forbidden - [*] 表示用户得到授权（与401错误相对），但是访问是被禁止的。
  404 NOT FOUND - [*]：用户发出的请求针对的是不存在的记录，服务器没有进行操作，该操作是幂等的。
  406 Not Acceptable - [GET]：用户请求的格式不可得（比如用户请求JSON格式，但是只有XML格式）。
  410 Gone -[GET]：用户请求的资源被永久删除，且不会再得到的。
  422 Unprocesable entity - [POST/PUT/PATCH] 当创建一个对象时，发生一个验证错误。
  500 INTERNAL SERVER ERROR - [*]：服务器发生错误
  ```

  ​		2, 自定义内部code 进行响应

  ​		如 返回结构如下  {'code':200,  'data': {}, 'error': xxx}

  

  ​	8，返回结果

  ​	根据HTTP 动作的不同，返回结果的结构也有所不同

  ```python
  GET /users：返回资源对象的列表（数组）
  GET /users/guoxiaonao：返回单个资源对象
  POST /users：返回新生成的资源对象
  PUT /users/guoxiaonao：返回完整的资源对象
  PATCH /users/guoxiaonao：返回完整的资源对象
  DELETE /users/guoxiaonao：返回一个空文档
  ```

  

  

####中间件

中间件类须实现下列五个方法中的一个或多个:
`def process_request(self, request):` 执行视图之前被调用，在每个请求上调用，返回None或HttpResponse对象 
`def process_view(self, request, callback, callback_args, callback_kwargs):` 调用视图之前被调用，在每个请求上调用，返回None或HttpResponse对象
`def process_response(self, request, response):` 所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象
`def process_exception(self, request, exception):` 当处理过程中抛出异常时调用，返回一个HttpResponse对象
`def process_template_response(self, request, response):` 在视图刚好执行完毕之后被调用，在每个请求上调用，返回实现了render方法的响应对象



####cookie和session
HTTP是脸盲的
为了保持器回话,两者被设计出
保持回话的原理



django:内容回顾
MTV:
    模型
    视图
    模板
ORM:
    用类操作数据库
应用:
把一部分功能分离到子应用中
分布式路由 把相关路由分配到子路由处理
模型类的增删改查
模型类的关系映射
中间件
form表单验证
分页
文件上传
django认证系统
项目的部署


冷数据:

不经常访问的数据,设计成另一个表

热数据:

经常访问或者查找的数据,设计成一个表


##绝对路径与相对路径

路径前加"/"表示绝对路径,表示路径从端口号开始

路径前不加"/"表示相对路径,表示路径从当前开始


##get请求与post请求
get请求是放在地址栏提交的
post是不可见的

##重量级与轻量级
重量级功能齐全
轻量级更灵活


# 《Django Web框架教学笔记》 day01
## 面向视图的编程

 - 讲师: 魏明择
 - 时间: 2019

## 目录
[TOC]

- 课程特点：
    1. 学习难度大，大部分内容需要理解并记忆
    2. 文件较多易混淆
    3. 学习阶段注重框架使用，工作阶段注重实现业务逻辑
    4. 综合应用强，小练习少

## Django框架的介绍
- 2005年发布,采用Python语言编写的开源web框架
- 早期的时候Django主做新闻和内容管理的
- 一个重量级的 Python Web框架(功能齐全,运行略显臃肿)，Django 配备了常用的大部分组件
    1. 基本配置
    1. 路由系统
    1. 原生HTML模板系统
    1. 视图 view
    1. Model模型,数据库连接和ORM数据库管理
    1. 中间件
    1. Cookie & Seesion
    1. 分页
    1. 数据库后台管理系统admin

- Django的用途
    - 网站后端开发
    - 微信公众号、微信小程序等后台开发
    - 基于HTTP/HTTPS协议的后台服务器开发
        - 在线语音/图像识别服务器
        - 在线第三方身份验证服务器等
- Django的版本
    - 最新版本:2.2.x(企业开发不一定用最新的,稳定更好)
    - 当前教学版本:1.11.8(企业常用的)

- Django的官网
    - 官方网址: <http://www.djangoproject.com>
    - 中文文档(第三方):
        - <https://yiyibooks.cn/>
        - <http://djangobook.py3k.cn/>
    - Django的离线文档
        1. 解压缩数据包 `django-docs-1.11-en.zip`
        2. 用浏览器打开 `django-docs-1.11-en/index.html`


### Django的安装
- 查看已安装的版本
    ```python
    >>> import django
    >>> print(django.VERSION)
    (1, 11, 8, 'final', 0)
    ```
- 安装
    1. 在线安装
        - `$ sudo pip3 install django`  安装django的最新版本
        - 或
        - `$ sudo pip3 install django[==版本]` 安装django的指定版本
        - 如:
            - `$ sudo pip3 install django==1.11.8`
    2. 离线安装
        - 下载安装包:
        - 安装离线包
            - `$ tar -xvf Django-1.11.8.tar.gz`
            - `$ cd Django-1.11.8`
            - `$ sudo python3 setup.py install`
    3. 用wheel离线安装
        - 下载安装包:
            - `pip3 download -d /home/weimz/django_packs django==1.11.8`
        - 安装离线包
          - $ pip3 install Django-1.11.8.whl
- Django的卸载
  
- $ pip3 uninstall django
  
- Django 的开发环境
    - Django 1.11.x 支持 Python 2.7, 3.4, 3.5 和 3.6（长期支持版本 LTS)
    - 注: Django 1.11.x 不支持 Python 3.7



## Django框架开发
### 创建项目的指令
  - $ django-admin startproject 项目名称
  - 如:
    
    - $ django-admin startproject mysite1
  - 运行
    ```shell
    $ cd mysite1
    $ python3 manage.py runserver
    # 或
    $ python3 manage.py runserver 5000  # 指定只能本机使用127.0.0.1的5000端口访问本机
    ```
### Django项目的目录结构
- 示例:
    ```shell
    $ django-admin startproject mysite1
    $ tree mysite1/
    mysite1/
    ├── manage.py
    └── mysite1
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py

    1 directory, 5 files
    ```
- 项目目录结构解析:
    - manage.py
        - 此文件是项目管理的主程序,在开发阶段用于管理整个项目的开发运行的调式
        - `manage.py` 包含项目管理的子命令, 如:
            - `python3 manage.py runserver` 启动服务
            - `python3 manage.py startapp` 创建应用
            - `python3 manage.py migrate` 数据库迁移
            - `...`
    - mysite1 项目包文件夹
        - 项目包的主文件夹(默认与项目名称一致)
        1. `__init__.py`
            - 包初始化文件,当此项目包被导入(import)时此文件会自动运行
        2. `wsgi.py`
            - WSGI 即 Web Server Gateway Interface
            - WEB服务网关接口的配置文件，仅部署项目时使用
        3. `urls.py`
            - 项目的基础路由配置文件，所有的动态路径必须先走该文件进行匹配
        4. `settings.py`
            - Django项目的配置文件, 此配置文件中的一些全局变量将为Django框架的运行传递一些参数
            - setting.py 配置文件,启动服务时自动调用，
            - 此配置文件中也可以定义一些自定义的变量用于作用全局作用域的数据传递

- `settings.py` 文件介绍
    1. `BASE_DIR`
       
        - 用于绑定当前项目的绝对路径(动态计算出来的), 所有文件都可以依懒此路径
    2. `DEBUG`
        - 用于配置Django项目的启用模式, 取值:
            1. True 表示开发环境中使用 `调试模式`(用于开发中)
            2. False 表示当前项目运行在`生产环境中`(不启用调试)
    3. `ALLOWED_HOSTS`
        - 设置允许访问到本项目的网络地址列表,取值:
            1. [] 空列表,表示只有`127.0.0.1`, `localhost`, '[::1]' 能访问本项目
            2. ['*']，表示任何网络地址都能访问到当前项目
            3. ['*.tedu.cn', 'weimingze.com'] 表示只有当前两个主机能访问当前项目
            - 注意:
                - 如果要在局域网其它主机也能访问此主机,启动方式应使用如下模式:
            - `python3 manage.py runserver 0.0.0.0:5000` # 指定网络设备所有主机都可以通过5000端口访问(需加`ALLOWED_HOSTS = ['*']`) 
    
    4. `INSTALLED_APPS`
       
        - 指定当前项目中安装的应用列表
    5. `MIDDLEWARE`
       
        - 用于注册中间件
    6. `TEMPLATES`
       
        - 用于指定模板的配置信息
    7. `DATABASES`
       
        - 用于指定数据库的配置信息
    8. `LANGUAGE_CODE`
        - 用于指定语言配置
        - 取值:
            - 英文 : `"en-us"`
            - 中文 : `"zh-Hans"`
    9. `TIME_ZONE`
        - 用于指定当前服务器端时区
        - 取值:
            - 世界标准时间: `"UTC"`
            - 中国时区 : `"Asia/Shanghai"`
    10. `ROOT_URLCONF`
        - 用于配置根级 url 配置 'mysite1.urls'
        - 如:
            - `ROOT_URLCONF = 'mysite1.urls'`
    > 注: 此模块可以通过 `from django.conf import settings` 导入和使用


### URL 介绍
- url 即统一资源定位符 Uniform Resource Locator
- 作用:
  
    - 用来表示互联网上某个资源的地址。
- 说明:
  
    - 互联网上的每个文件都有一个唯一的URL，它包含的信息指出文件的位置以及浏览器应该怎么处理它。
- URL的一般语法格式为：
    ```
    protocol :// hostname[:port] / path [?query][#fragment]
    ```
- 如:
    ```
    http://tts.tmooc.cn/video/showVideo?menuId=657421&version=AID201908#subject
    ```

- 说明:
    - protocol（协议）
        - http 通过 HTTP 访问该资源。 格式 `HTTP://`
        - https 通过安全的 HTTPS 访问该资源。 格式 `HTTPS://`
        - file 资源是本地计算机上的文件。格式: `file:///`
        - ...

    - hostname（主机名）
        - 是指存放资源的服务器的域名系统(DNS) 主机名、域名 或 IP 地址。
        
    - port（端口号）
        - 整数，可选，省略时使用方案的默认端口；
        - 各种传输协议都有默认的端口号，如http的默认端口为80。
    - path（路由地址）
        - 由零或多个“/”符号隔开的字符串，一般用来表示主机上的一个目录或文件地址。路由地址决定了服务器端如何处理这个请求

    - query(查询)
        - 可选，用于给动态网页传递参数，可有多个参数，用“&”符号隔开，每个参数的名和值用“=”符号隔开。
    - fragment（信息片断）
        - 字符串，用于指定网络资源中的片断。例如一个网页中有多个名词解释，可使用fragment直接定位到某一名词解释。
    - 注: [] 代表其中的内容可省略


### 视图函数(view)
- 视图函数是用于接收一个浏览器请求并通过HttpResponse对象返回数据的函数。此函数可以接收浏览器请求并根据业务逻辑返回相应的内容给浏览器
- 视图处理的函数的语法格式:
    ```python
    def xxx_view(request[, 其它参数...]):
        return HttpResponse对象
    ```
- 参数:
  
    - request用于绑定HttpRequest对象，通过此对象可以获取浏览器的参数和数据
- 示例:
    - 视图处理函数 `views.py`
        ```python
        # file : <项目名>/views.py
        from django.http import HttpResponse
        def page1_view(request):
            html = "<h1>这是第1个页面</h1>"
            return HttpResponse(html)
        ```

### Django 中的路由配置
- settings.py 中的`ROOT_URLCONF` 指定了主路由配置列表urlpatterns的文件位置
- urls.py 主路由配置文件
    ```python
    # file : <项目名>/urls.py
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        ...  # 此处配置主路由
    ]
    ```
    > urlpatterns 是一个路由-视图函数映射关的列表,此列表的映射关系由url函数来确定

3. url() 函数
    - 用于描述路由与视图函数的对应关系
    - 模块
        - `from django.conf.urls import url`
    - 语法:
        - url(regex, views, name=None)
        - 参数：
            1. regex: 字符串类型，匹配的请求路径，允许是正则表达式
            2. views: 指定路径所对应的视图处理函数的名称
            3. name: 为地址起别名，在模板中地址反向解析时使用
    
    > 每个正则表达式前面的r表示`'\'`不转义的原始字符串



- 练习
    - 建立一个小网站:
        - 输入网址: http://127.0.0.1:8000, 在网页中输出 : 这是我的首页
        - 输入网址: http://127.0.0.1:8000/page1, 在网页中输出 : 这是编号为1的网页
        - 输入网址: http://127.0.0.1:8000/page2, 在网页中输出 : 这是编号为2的网页
        > 提示: 主面路由的正则是  `r'^$'`
        - 思考
            - 建立如上一百个网页该怎么办？

#### 带有分组的路由和视图函数
- 在视图函数内，可以用正则表达式分组 `()` 提取参数后用函数位置传参传递给视图函数
- 一个分组表示一个参数,多个参数需要使用多个分组,并且使用个/隔开
    - 如:
        - http://127.0.0.1:8000/year/2018
        - http://127.0.0.1:8000/year/2019
        - http://127.0.0.1:8000/year/????  # 四位数字
- 练习：
    - 定义一个路由的格式为:
        - http://127.0.0.1:8000/整数/操作字符串/整数

    - 从路由中提取数据，做相应的操作后返回给浏览器
    - 如：
    ```
    输入: 127.0.0.1:8000/100/add/200
        页面显示结果：300
    输入: 127.0.0.1:8000/100/sub/200
        页面显示结果：-100
    输入: 127.0.0.1:8000/100/mul/200
        页面显示结果：20000
    ```

#### 带有命名分组的路由和视图函数
- 在url 的正则表达式中可以使用命名分组(捕获分组)
- 说明:
  
    - 在视图函数内，可以用正则表达式分组 `(?P<name>pattern)` 提取参数后用函数关键字传参传递给视图函数
- 示例:
    - 路由配置文件
        ```python
        # file : <项目名>/urls.py
        # 以下示例匹配
        # http://127.0.0.1:8000/person/weimingze/35
        # http://127.0.0.1:8000/person/shibowen/29
        # http://127.0.0.1:8000/person/xiaowei/9
        urlpatterns = [
            url(r'^admin/', admin.site.urls),
            url(r'^person/(?P<name>\w+)/(?P<age>\d{1,2})',views.person_view),
        ]
        ```
- 练习:
    - 访问地址:http://127.0.0.1:8000/birthday/四位数字/一到两位数字/一到两位数字
    - 最终输出: 生日为: xxxx年xx月xx日
    - 如:
        输入网址: http://127.0.0.1:8000/birthday/2015/12/11
        显示为: 生日为:2015年12月11日
        输入网址: http://127.0.0.1:8000/birthday/2/28/2008
        显示为: 生日为:2008年2月28日


- PyCharm 社区版针对Django项目调试方法
    1. 添加自己调式配置
        - 选择 Add Configuration...
    2. 点击 `+` 号添加一个自己的配置
        - 选择运行的项目的主模块位置 manage.py
        - 添加 runserver 命令行参数


## HTTP协议的请求和响应
- 请求是指浏览器端通过HTTP协议发送给服务器端的数据
- 响应是指服务器端接收到请求后做相应的处理后再回复给浏览器端的数据

![请求和向应](images/request_response.png)


### HTTP 请求
- 根据HTTP标准，HTTP请求可以使用多种请求方法。
- HTTP1.0定义了三种请求方法： GET, POST 和 HEAD方法(最常用)
- HTTP1.1新增了五种请求方法：OPTIONS, PUT, DELETE, TRACE 和 CONNECT 方法。
- HTTP1.1 请求详述
    | 序号 | 方法 | 描述 |
    |:-:|:-:|:-|
    | 1 | GET | 请求指定的页面信息，并返回实体主体。 |
    | 2 | HEAD | 类似于get请求，只不过返回的响应中没有具体的内容，用于获取报头 |
    | 3 | POST | 向指定资源提交数据进行处理请求（例如提交表单或者上传文件）。数据被包含在请求体中。POST请求可能会导致新的资源的建立和/或已有资源的修改。 |
    | 4 | PUT | 从客户端向服务器传送的数据取代指定的文档的内容。 |
    | 5 | DELETE | 请求服务器删除指定的页面。 |
    | 6 | CONNECT | HTTP/1.1协议中预留给能够将连接改为管道方式的代理服务器。 |
    | 7 | OPTIONS | 允许客户端查看服务器的性能。 |
    | 8 | TRACE | 回显服务器收到的请求，主要用于测试或诊断。 |


- HttpRequest对象
    - 视图函数的第一个参数是HttpRequest对象
    - 服务器接收到http协议的请求后，会根据请求数据报文创建HttpRequest对象
    - HttpRequest属性
        - path：字符串，表示请求的路由信息
        - path_info: URL字符串
        - method：字符串，表示HTTP请求方法，常用值：'GET'、'POST'
        - encoding：字符串，表示提交的数据的编码方式
            - 如果为None则表示使用浏览器的默认设置，一般为'utf-8'
            - 这个属性是可写的，可以通过修改它来修改访问表单数据使用的编码，接下来对属性的任何访问将使用新的encoding值
        - GET：QueryDict查询字典的对象，包含get请求方式的所有数据
        - POST：QueryDict查询字典的对象，包含post请求方式的所有数据
        - FILES：类似于字典的对象，包含所有的上传文件信息
        - COOKIES：Python字典，包含所有的cookie，键和值都为字符串
        - session：似于字典的对象，表示当前的会话，
        - body: 字符串，请求体的内容(POST或PUT)
        - environ: 字符串,客户端运行的环境变量信息
        - scheme : 请求协议('http'/'https')
        - request.get_full_path() : 请求的完整路径
        - request.get_host() : 请求的主机
        - request.META : 请求中的元数据(消息头)
            - request.META['REMOTE_ADDR']  : 客户端IP地址

### HTTP 响应
- 当浏览者访问一个网页时，浏览者的浏览器会向网页所在服务器发出请求。当浏览器接收并显示网页前，此网页所在的服务器会返回一个包含HTTP状态码的信息头用以响应浏览器的请求。
- HTTP状态码的英文为HTTP Status Code。
- 下面是常见的HTTP状态码：
    - 200 - 请求成功
    - 301 - 资源（网页等）被永久转移到其它URL
    - 404 - 请求的资源（网页等）不存在
    - 500 - 内部服务器错误

- HTTP状态码分类
    - HTTP状态码由三个十进制数字组成，第一个十进制数字定义了状态码的类型，后两个数字没有分类的作用。HTTP状态码共分为5种类型：

        | 分类 | 分类描述 |
        |:-:|-|
        | 1** | 信息，服务器收到请求，需要请求者继续执行操作 |
        | 2** | 成功，操作被成功接收并处理 |
        | 3** | 重定向，需要进一步的操作以完成请求 |
        | 4** | 客户端错误，请求包含语法错误或无法完成请求 |
        | 5** | 服务器错误，服务器在处理请求的过程中发生了错误 |

- Django中的响应对象HttpResponse:
    - 构造函数格式:
      
        - `HttpResponse(content=响应体, content_type=响应体数据类型, status=状态码)`
    - 作用:
      
        - 向客户端浏览器返回响应，同时携带响应体内容
    - 参数:
        - content：表示返回的内容。
        - status_code：返回的HTTP响应状态码(默认为200)。
        - content_type：指定返回数据的的MIME类型(默认为"text/html")。浏览器会根据这个属性，来显示数据。如果是text/html，那么就会解析这个字符串，如果text/plain，那么就会显示一个纯文本。
            - 常用的Content-Type如下：
                - `'text/html'`（默认的，html文件）
                - `'text/plain'`（纯文本）
                - `'text/css'`（css文件）
                - `'text/javascript'`（js文件）
                - `'multipart/form-data'`（文件提交）
                - `'application/json'`（json传输）
            - `'application/xml'`（xml文件）
            > 注： 关键字MIME(Multipurpose Internet Mail Extensions)是指多用途互联网邮件扩展类型。
    
- HttpResponse 子类
    | 类型 | 作用 | 状态码 |
    |-|-|-|
    | HttpResponseRedirect | 重定响 | 301 |
    | HttpResponseNotModified | 未修改 | 304 |
    | HttpResponseBadRequest | 错误请求 | 400 |
    | HttpResponseNotFound | 没有对应的资源 | 404 |
    | HttpResponseForbidden | 请求被禁止 | 403 |
    | HttpResponseServerError | 服务器错误 | 500 |



### GET方式传参
- GET请求方式中可以通过查询字符串(Query String)将数据传递给服务器    
- URL 格式: `xxx?参数名1=值1&参数名2=值2...`
  
    - 如: `http://127.0.0.1:8000/page1?a=100&b=200`
- 服务器端接收参数
    1. 判断 request.method 的值判断请求方式是否是get请求
        ```python
        if request.method == 'GET':
            处理GET请求时的业务逻辑
        else:
            处理其它请求的业务逻辑
        ```
    2. 获取客户端请求GET请求提交的数据
        1. 语法
            ```python
            request.GET['参数名']
            request.GET.get('参数名','默认值')
            request.GET.getlist('参数名')
            # mypage?a=100&b=200&c=300&b=400
            request.GET = Querydict({a:[100],b:[200,400],c:[300]})
            ```
        2. 能够产生get请求方式的场合
            1. 地址栏手动输入, 如: http://www.sina.com.cn/?a=100&b=200
            2. `<a href="地址?参数=值&参数=值">`
            3. form表单中的method为get
                ```html
                <form method='get' action="/user/login">
                    姓名:<input type="text" name="uname">
                </form>
                ```
> 一般查询字符串的大小会受到浏览器的的限制(不建议超过2048字节)

- 练习:
    - 访问地址:<http://127.0.0.1:8000/sum?start=整数&stop=整数&step整=字>
    - 输出结果为sum(range(start, step, stop)) 和:
    - 如:
        - 输入网址: http://127.0.0.1:8000/sum?start=1&stop=101&step=1
        - 页面显示: 结果: 5050
        - 输入网址: http://127.0.0.1:8000/sum?stop=101&step=2
        - 页面显示: 结果: 2550
        - 输入网址: http://127.0.0.1:8000/sum?start=1&stop=101&step=2
        - 页面显示: 结果: 2500

- 练习:
    - 访问地址:<http://127.0.0.1:8000/birthday?year=四位整数&month=整数&day=整数>
    - 最终输出: 生日为: xxxx年xx月xx日
    - 如:
        - 输入网址: http://127.0.0.1:8000/birthday?year=2015&month=12&day=11
        - 显示为: 生日为:2015年12月11日

- PyCharm社区版调试Django程序配置
    1. 选择 Add Configuration
    2. 选择 左上角 + 号 选择 "Python"
        1. script path 里选 manage.py 的路径 
        2. 在 parameters 里填入runserver
    3. 设置断点
    4. 点击开始调式按钮开始调式操作

### POST传递参数
- 客户端通过表单等POST请求将数据传递给服务器端,如:
```html
<form method='post' action="/user/login">
    姓名:<input type="text" name="username">
    <input type = "submit" value="登录">
</form>
```
- 服务器端接收参数
    - 通过 request.method 来判断是否为POST请求,如:
    ```python
    if request.method == 'POST':
        处理POST请求的数据并响应
    else:
        处理非POST 请求的响应
    ```

- 使用post方式接收客户端数据
    1. 方法
    ```python
    request.POST['参数名']
    request.POST.get('参数名','')      -->参数后面可以给默认参数,查询不到则返回默认参数
    request.POST.getlist('参数名')   pass
    ```
- 取消csrf验证(中间键),否则Django将会拒绝客户端发来的POST请求
    - 取消 csrf 验证
        - 删除 settings.py 中 MIDDLEWARE 中的 CsrfViewsMiddleWare 的中间件
        ```python
        MIDDLEWARE = [
            ...
            # 'django.middleware.csrf.CsrfViewMiddleware',
            ...
        ]
        ```

### form 表单的name属性
- 在form表单控件提交数据时，会自动搜索本表单控件内部的子标签的name属性及相应的值，再将这些名字和值以键-值对的形式提交给action指定的服务器相关位置
- 在form内能自动搜集到的name属性的标签的控件有
    ```html
    <input name='xxx'>
    <select name='yyy'></select>
    <textarea name='zzz'></textarea>
    ```
    - 如:
    ```html
    <form action="/page1" method="POST">
        <input name="title" type="text" value="请输入">
        <select name="gender">
            <option value=1>男</option>
            <option value=0>女</option>
        </select>
        <textarea name="comment" rows="5" cols="10">附言...</textarea>
        <input type="submit" value="提交">
    </form>
    ```

- 小结:
    - URL
    - 视图
    - 路由
    - 从URL的路由中用正则分组提取数据
    - 从GET请求的查询字符串中用 request.GET 获取数据
    - 从POST请求的表单中用request.POST获取数据



#day2
面向模板的编程

标签
if
for 
extends
block
url

### POST传递参数
- 客户端通过表单等POST请求将数据传递给服务器端,如:
```html
<form method='post' action="/user/login">
    姓名:<input type="text" name="username">
</form>
```
- 服务器端接收参数
    - 通过 request.method 来判断是否为POST请求,如:
    ```python
    if request.method == 'POST':
        处理POST请求的数据并响应
    else:
        处理非POST 请求的响应
    ```

- 使用post方式接收客户端数据
    1. 方法
    ```python
    request.POST['参数名']
    request.POST.get('参数名','')
    request.POST.getlist('参数名')
    ```
- 取消csrf验证,否则Django将会拒绝客户端发来的POST请求
    - 取消 csrf 验证
        - 删除 settings.py 中 MIDDLEWARE 中的 CsrfViewsMiddleWare 的中间件
        ```python
        MIDDLEWARE = [
            ...
            # 'django.middleware.csrf.CsrfViewMiddleware',
            ...
        ]
        ```

### form 表单的name属性
- 在form表单控件提交数据时，会自动搜索本表单控件内部的子标签的name属性及相应的值，再将这些名字和值以键-值对的形式提交给action指定的服务器相关位置
- 在form内能自动搜集到的name属性的标签的控件有
    ```html
    <input name='xxx'>
    <select name='yyy'></select>
    <textarea name='zzz'></textarea>
    ```
    - 如:
    ```html
    <form action="/page1" method="POST">
        <input name="title" type="text" value="请输入">
        <select name="gender">
            <option value=1>男</option>
            <option value=0>女</option>
        </select>
        <textarea name="comment" rows="5" cols="10">附言...</textarea>
        <input type="submit" value="提交">
    </form>
    ```






- day02
                    

## Django的框架模式
- MVC 设计模式
    - MVC 代表 Model-View-Controller（模型-视图-控制器） 模式。
    - 作用: 降低模块间的耦合度(解耦)
    - MVC
        - M 模型层(Model), 主要用于对数据库层的封装
        - V 视图层(View), 用于向用户展示结果
        - C 控制(Controller ，用于处理请求、获取数据、返回结果(重要)
    - MVC模式如图:
        ![](images/mvc.png)
- MTV 模式
    MTV 代表 Model-Template-View（模型-模板-视图） 模式。这种模式用于应用程序的分层开发
    - 作用: 
        - 降低模块间的耦合度(解耦)
    - MTV 
        - M -- 模型层(Model)  负责与数据库交互
        - T -- 模板层(Template)  负责呈现内容到浏览器    生成html
        - V -- 视图层(View)  是核心，负责接收请求、获取数据、返回结果
    - MTV模式如图:
        ![](images/mtv.png)

## 模板 Templates
- 什么是模板
    1. 模板是可以根据字典数据[动态变化]的html网页
    2. 模板可以根据视图中传递的字典数据[动态生成]相应的HTML网页。

- 模板的配置
    - 创建模板文件夹`<项目名>/templates`
    - 在 settings.py 中有一个 TEMPLATES 变量
        1. BACKEND : 指定模板的引擎
        2. DIRS : 模板的搜索目录(可以是一个或多个)
        3. APP_DIRS : 是否要在应用中的 `templates` 文件夹中搜索模板文件
        4. OPTIONS : 有关模板的选项

- 默认的模块文件夹`templates`
- 修改settings.py文件，设置TEMPLATES的DIRS值为`'DIRS': [os.path.join(BASE_DIR, 'templates')],`
```python
# file: settings.py
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # 'DIRS': [],
        'DIRS': [os.path.join(BASE_DIR, 'templates')],  # 添加模板路径
        'APP_DIRS': True,  # 是否索引各app里的templates目录
        ...
    },
]
```

3. 模板的加载方式
    1. 通过 loader 获取模板,通过HttpResponse进行响应
        ```python
        from django.template import loader
        # 1.通过loader加载模板
        t = loader.get_template("模板文件名")
        # 2.将t转换成 HTML 字符串
        html = t.render(字典数据)
        # 3.用响应对象将转换的字符串内容返回给浏览器
        return HttpResponse(html)
        ```
    2. 使用 render() 直接加载并响应模板
        ```python
        from django.shortcuts import render
        return render(request,'模板文件名')
        ```

### Django 模板语言

os.path.join(BASE_DIR, 'templates')> 容器的索引、键值使用"."语法
- 模板传参是指把数据形成字典，传参给模板，为模板渲染提供数据
1. 使用 loader 加载模板
    ```python
    t = loader.get_template('xxx.html')
    html = t.render(字典数据)
    return HttpResponse(html)
    ```
2. 使用render加载模板
    ```python
    return render(request,'xxx.html',字典数据)
    ```

#### 模板的变量
1. 在模板中使用变量语法
    - `{{ 变量名 }}`
    - `{{ 变量名.index }}`
    - `{{ 变量名.key}}`
    - `{{ 对象.方法 }}`
    - `{{ 函数名 }}`

    1. 视图函数中必须将变量封装到字典中才允许传递到模板上
        ```python
        def xxx_view(request)
            dic = {
                "变量1":"值1",
                "变量2":"值2",
            }
            return render(request, 'xxx.html', dic)
        ```
- 练习
    - 写一个简单的计算器页面，能够在服务端进行简单加减乘除计算
        <form action='/mycal' method='POST'>
            <input type='text' name="x" value="1">
            <select>
                <option value="add"> +加 </option>
                <option value="sub"> -减 </option>
                <option value="mul"> *乘 </option>
                <option value="div"> /除 </option>
            </select>
            <input type='text' name="y" value="2"> = <span>3</span>
            <div>
                <input type="submit" value='开始计算'>
            <div>
        </form>

    - 参考代码
        ```html
        <form action='/mycal' method='POST'>
            <input type='text' name="x" value="1">
            <select>
                <option value="add"> +加 </option>
                <option value="sub"> -减 </option>
                <option value="mul"> *乘 </option>
                <option value="div"> /除 </option>
            </select>
            <input type='text' name="y" value="2"> = <span>3</span>
            <div>
                <input type="submit" value='开始计算'>
            <div>
        </form>
        ```


#### 模板的标签
1. 作用
   
    - 将一些服务器端的功能嵌入到模板中
2. 标签语法
    ```
    {% 标签 %}
    ...
    {% 结束标签 %}
    ```
3. if 标签
    ```
    {% if 条件表达式1 %}
    ...
    {% elif 条件表达式2 %}
    ...
    {% elif 条件表达式3 %}
    ...
    {% else %}
    ...
    {% endif %}
    ```
4. if 标签里的布尔运算符
    - if 条件表达式里可以用的运算符 ==, !=, <, >, <=, >=, in, not in, is, is not, not、and、or
    - 在if标记中使用实际括号是无效的语法。 如果您需要它们指示优先级，则应使用嵌套的if标记。
5. locals()函数的使用
    locals()返回字典,包括当前作用域的全部局部变量,结合if语句使用


6. for 标签    1. 语法
        ```
        {% for 变量 in 可迭代对象 %}
            ... 循环语句
        {% empty %}
            ... 可迭代对象无数据时填充的语句
        {% endfor %}
        ```
    
    2. 内置变量 - forloop
        | 变量 | 描述 |
        |:-:|:-:|
        | forloop.counter | 循环的当前迭代（从1开始索引） |
        | forloop.counter0 | 循环的当前迭代（从0开始索引） |
        | forloop.revcounter | 循环结束的迭代次数（从1开始索引） |
        | forloop.revcounter0 | 循环结束的迭代次数（从0开始索引） |
        | forloop.first | 如果这是第一次通过循环，则为真 |
        | forloop.last | 如果这是最后一次循环，则为真 |
        | forloop.parentloop | 当嵌套循环，parentloop 表示外层循环 |


#### 过滤器
1. 作用
    - 在变量输出时对变量的值进行处理
    - 您可以通过使用 过滤器来改变变量的输出显示。
2. 语法
   
    - {{ 变量 | 过滤器1:参数值1 | 过滤器2:参数值2 ... }}
3. 常用的过滤器
    | 过滤器 | 说明 |
    |:-:|:-:|
    | lower | 将字符串转换为全部小写。|
    | upper | 将字符串转换为大写形式 |
    | safe | 默认不对变量内的字符串进行html转义 |
    | add: "n" | 将value的值增加 n |
    | truncatechars:'n' | 如果字符串字符多于指定的字符数量，那么会被截断。 截断的字符串将以可翻译的省略号序列（“...”）结尾。 |
    | ... | |

5. 文档参见:
   
    - <https://docs.djangoproject.com/en/1.11/ref/templates/builtins/>


### 模板的继承
- 模板继承可以使父模板的内容重用,子模板直接继承父模板的全部内容并可以覆盖父模板中相应的块
- 定义父模板中的块 `block`标签
    - 标识出哪些在子模块中是允许被修改的
    - block标签：在父模板中定义，可以在子模板中覆盖
        ```
        {% block block_name %}
        定义模板块，此模板块可以被子模板重新定义的同名块覆盖
        {% endblock block_name %}
        ```
- 继承模板 `extends` 标签(写在模板文件的第一行)
    - 子模板继承语法标签
        - `{% extends '父模板名称' %}`
        - 如:
            - `{% extends 'base.html' %}`
    - 子模板 重写父模板中的内容块
    ```
    {% block block_name %}
    子模板块用来覆盖父模板中 block_name 块的内容
    {% endblock block_name %}
    ```
    - 重写的覆盖规则
        - 不重写,将按照父模板的效果显示
        - 重写,则按照重写效果显示
    - 注意
        - 模板继承时,服务器端的动态内容无法继承

- 参考文档
  
- <https://docs.djangoproject.com/en/1.11/ref/templates/>
  
- 模板的继承示例:
  
    - ![](images/template_inherit.png)

### url 反向解析
- url 反向解析是指在视图或模板中，用为url定义的名称来查找或计算出相应的路由
- url 函数的语法
    - url(regex, views, kwargs=None, name="别名")
    - 例如:
        - url(r'^user_login$', views.login_view, name="login")

- url() 的`name`关键字参数
    - 作用:
      
        - 根据url 列表中的`name=`关键字传参给 url确定了个唯一确定的名字，在模板中，可以通过这个名字反向推断出此url信息
    - 在模板中通过别名实现地址的反向解析
        ```
        {% url '别名' %}
        {% url '别名' '参数值1' '参数值2' %} pass
        ```
- 练习:
    ```
    写一个有四个自定义页面的网站，对分对应路由:
    /       主页
    /page1   页面1
    /page2   页面2
    /page3   页面3
    功能: 是主页加 三个页面的连接分别跳转到一个页面，三个页面每个页面加入一个链接用于返回主页
    ```



#day3

# 《Django Web框架教学笔记》
 - 讲师: 魏明择
 - 时间: 2019


## 静态文件
1. 什么是静态文件
    - 不能与服务器端做动态交互的文件都是静态文件
    - 如:图片,css,js,音频,视频,html文件(部分)
2. 静态文件配置
    - 在 settings.py 中配置一下两项内容:
    1. 配置静态文件的访问路径
        - 通过哪个url地址找静态文件
        - STATIC_URL = '/static/'
        - 说明:
            - 指定访问静态文件时是需要通过 /static/xxx或 127.0.0.1:8000/static/xxx
            - xxx 表示具体的静态资源位置
    2. 配置静态文件的存储路径 `STATICFILES_DIRS`
      
        - STATICFILES_DIRS保存的是静态文件在服务器端的存储位置
    3. 示例:
        ```python
        # file: setting.py
        STATICFILES_DIRS = (
            os.path.join(BASE_DIR, "static"),
        )
        ```
3. 访问静态文件
    1. 使用静态文件的访问路径进行访问
        - 访问路径: STATIC_URL = '/static/'
        -  示例:
            ```python
            <img src="/static/images/lena.jpg">
            <img src="http://127.0.0.1:8000/static/images/lena.jpg">
            ```
    2. 通过 {% static %}标签访问静态文件
        - `{% static %}` 表示的就是静态文件访问路径

        1. 加载 static
            - `{% load static %}`
        2. 使用静态资源时
            - 语法:
                - `{% static '静态资源路径' %}`
            - 示例:
                - `<img src="{% static 'images/lena.jpg' %}">`

## Django中的应用 - app
- 应用在Django项目中是一个独立的业务模块,可以包含自己的路由,视图,模板,模型

###  创建应用app
- 创建步骤
    1. 用manage.py 中的子命令 startapp 创建应用文件夹
    2. 在settings.py 的 INSTALLED_APPS 列表中配置安装此应用

- 创建应用的子命令
    - python3 manage.py startapp 应用名称(必须是标识符命令规则)
    - 如:
        - python3 manage.py startapp music

- Django应用的结构组成
    1. `migrations` 文件夹
        - 保存数据迁移的中间文件
    2. `__init__.py`
        - 应用子包的初始化文件
    3. `admin.py`
        - 应用的后台管理配置文件
    4. `apps.py`
        - 应用的属性配置文件
    5. `models.py`
        - 与数据库相关的模型映射类文件
    6. `tests.py`
        - 应用的单元测试文件
    7. `views.py`
        - 定义视图处理函数的文件

- 配置安装应用
    - 在 settings.py 中配置应用, 让此应用能和整个项目融为一体
        ```python
        # file : settings.py 
        INSTALLED_APPS = [
            ... ...,
            '自定义应用名称'
        ]

        ```
    - 如:
        ```python
        INSTALLED_APPS = [
            # ....
            'user',  # 用户信息模块
            'music',  # 收藏模块
        ]
        ```

### 应用的分布式路由
- Django中，基础路由配置文件(urls.py)可以不处理用户具体路由，基础路由配置文件的可以做请求的分发(分布式请求处理)。具体的请求可以由各自的应用来进行处理
- 如图:
    - ![](images/urls.png)
#### include 函数
- 作用:
  
    - 用于分发将当前路由转到各个应用的路由配置文件的 urlpatterns 进行分布式处理
- 函数格式
    - include('app命字.url模块名')
    > 模块`app命字/url模块名.py` 文件件里必须有urlpatterns 列表
    > 使用前需要使用 `from django.conf.urls import include` 导入此函数

- 练习:
    ```
    1.创建四个应用
        1.创建 index 应用,并注册
        2.创建 sport 应用,并注册
        3.创建 news  应用,并注册
        4.创建 music 应用,并注册
    2.创建分布式路由系统
        主路由配置只做分发
        每个应用中处理具体访问路径和视图
        1. 127.0.0.1:8000/music/index
            交给 music 应用中的 index_view() 函数处理
        2. 127.0.0.1:8000/sport/index
            交给 sport 应用中的 index_view() 函数处理
        3. 127.0.0.1:8000/news/index
            交给 news  应用中的 index_view() 处理处理
    ```

## 数据库 和 模型
### Django下配置使用 mysql 数据库
1. 安装 pymysql包
    - 用作 python 和 mysql 的接口
        - `$ sudo pip3 install pymysql`
    - 安装 mysql 客户端(非必须)
        `$ sudo pip3 install mysqlclient`

2. 创建 和 配置数据库
    1. 创建数据库
        - 创建 `create database 数据库名 default charset utf8 collate utf8_general_ci;`
        ```sql
        create database mywebdb default charset utf8 collate utf8_general_ci;
        ```
    2. 数据库的配置
        - sqlite 数据库配置
            ```python
            # file: settings.py
            DATABASES = {
                'default': {
                        'ENGINE': 'django.db.backends.sqlite3',
                        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
                }
            }
            ```
        - mysql 数据库配置
            ```python
            DATABASES = {
                'default' : {
                    'ENGINE': 'django.db.backends.mysql',
                    'NAME': 'mywebdb',  # 数据库名称,需要自己定义
                    'USER': 'root',
                    'PASSWORD': '123456',  # 管理员密码
                    'HOST': '127.0.0.1',
                    'PORT': 3306,
                }
            }
            ```
    3. 关于数据为的SETTING设置
        1. ENGINE
            - 指定数据库的后端引擎
            ```
            'django.db.backends.mysql'
            'django.db.backends.sqlite3'
            'django.db.backends.oracle'
            'django.db.backends.postgresql'
            ```
            - mysql引擎如下:
                - 'django.db.backends.mysql'

        2. NAME
            - 指定要连接的数据库的名称
            - `'NAME': 'mywebdb'`
        3. USER
            - 指定登录到数据库的用户名
            - `'USER':'root'`
        4. PASSWORD
            - 接数据库时使用的密码。
            - `'PASSWORD':'123456'`
        5. HOST
            - 连接数据库时使用哪个主机。
            - `'HOST':'127.0.0.1'`
        6. PORT
            - 连接数据库时使用的端口。
            - `'PORT':'3306'`
    3. 添加 mysql 支持
        - 安装pymysql 模块
          
            - `$ sudo pip install pymysql`
        - 修改项目中__init__.py 加入如下内容来提供pymysql引擎的支持
            ```python
            import pymysql
            pymysql.install_as_MySQLdb()   # 此处的init.py位于项目根目录，随项目的导入执行
            ```

### 模型（Models）
- 模型是一个Python类，它是由django.db.models.Model派生出的子类。
- 一个模型类代表数据库中的一张数据表
- 模型类中每一个类属性都代表数据库中的一个字段。
- 模型是数据交互的接口，是表示和操作数据库的方法和方式


### Django 的 ORM框架
- ORM（Object Relational Mapping）即对象关系映射，它是一种程序技术，它允许你使用类和对象对数据库进行操作,从而避免通过SQL语句操作数据库
- ORM框架的作用
    1. 建立模型类和表之间的对应关系，允许我们通过面向对象的方式来操作数据库。
    2. 根据设计的模型类生成数据库中的表格。
    3. 通过简单的配置就可以进行数据库的切换。
- ORM 好处:
    1. 只需要面向对象编程, 不需要面向数据库编写代码.
        - 对数据库的操作都转化成对类属性和方法的操作.
        - 不用编写各种数据库的sql语句.
    2. 更灵活----实现了数据模型与数据库的解耦, 屏蔽了不同数据库操作上的差异.
        - 不在关注用的是mysql、oracle...等数据库的内部细节.
        - 通过简单的配置就可以轻松更换数据库, 而不需要修改代码.
- ORM 缺点
    1. 相比较直接使用SQL语句操作数据库,有性能损失.
    2. 根据对象的操作转换成SQL语句,根据查询的结果转化成对象, 在映射过程中有性能损失.
- ORM 示意
    - ![](images/orm.png)


2. 模型示例:
    - 此示例为添加一个 bookstore_book 数据表来存放图书馆中书目信息
    - 添加一个 bookstore 的 app
        ```shell
        $ python3 manage.py startapp bookstore
        ```
    - 添加模型类并注册app
        ```python
        # file : bookstore/models.py
        from django.db import models

        class Book(models.Model):
            title = models.CharField("书名", max_length=50, default='')
            price = models.DecimalField('定价', max_digits=7, decimal_places=2, default=0.0)
        ```
    - 注册app
        ```python
        # file : setting.py
        INSTALLED_APPS = [
            ...
            'bookstore',
        ]
        ```
3. 数据库的迁移
    - 迁移是Django同步您对模型所做更改（添加字段，删除模型等） 到您的数据库模式的方式
    1. 生成或更新迁移文件
        - 将每个应用下的models.py文件生成一个中间文件,并保存在migrations文件夹中
        - `python3 manage.py makemigrations`
    2. 执行迁移脚本程序
        - 执行迁移程序实现迁移。将每个应用下的migrations目录中的中间文件同步回数据库
        - `python3 manage.py migrate`
    - 注:
      
- ## **每次修改完模型类再对服务程序运行之前都需要做以上两步迁移操作。**
  
    ​      
    
    - 生成迁移脚本文件`bookstore/migrations/0001_initial.py`并进行迁移
        ```shell
        $ python3 manage.py makemigrations  
        $ python3 manage.py migrate  
        ```

2. 编写模型类Models
    - 模型类需继承自`django.db.models.Model`
        1. Models的语法规范
            ```
            from django.db import models
            class 模型类名(models.Model):
                字段名 = models.字段类型(字段选项)
            ```
        > 模型类名是数据表名的一部分，建议类名首字母大写
        > 字段名又是当前类的类属性名，此名称将作为数据表的字段名
        > 字段类型用来映射到数据表中的字段的类型
        > 字段选项为这些字段提供附加的参数信息
    
3. 字段类型
   
    1. BooleanField()
        - 数据库类型:tinyint(1)
        - 编程语言中:使用True或False来表示值
        - 在数据库中:使用1或0来表示具体的值
    2. CharField()
        - 数据库类型:varchar
        - 注意:
            - 必须要指定max_length参数值
    3. DateField()
        - 数据库类型:date
        - 作用:表示日期
        - 编程语言中:使用字符串来表示具体值
        - 参数:
            - DateField.auto_now: 每次保存对象时，自动设置该字段为当前时间(取值:True/False)。
            - DateField.auto_now_add: 当对象第一次被创建时自动设置当前时间(取值:True/False)。
            - DateField.default: 设置当前时间(取值:字符串格式时间如: '2019-6-1')。
            - 以上三个参数只能多选一
    4. DateTimeField()
        - 数据库类型:datetime(6)
        - 作用:表示日期和时间
    - auto_now_add=True
    
    5. DecimalField()
        - 数据库类型:decimal(x,y)
        - 编程语言中:使用小数表示该列的值
        - 在数据库中:使用小数
        - 参数:
          
            - DecimalField.max_digits: 位数总数，包括小数点后的位数。 该值必须大于等于decimal_places.
    - DecimalField.decimal_places: 小数点后的数字数量
      
        - 示例:
            ```
            money=models.DecimalField(
                max_digits=7,
                decimal_places=2,
                default=0.0
            )
            ```
    6. FloatField()
        - 数据库类型:double
        - 编程语言中和数据库中都使用小数表示值
    7. EmailField()
        - 数据库类型:varchar
        - 编程语言和数据库中使用字符串
    8. IntegerField()
        - 数据库类型:int
        - 编程语言和数据库中使用整数
    9. URLField()
        - 数据库类型:varchar(200)
        - 编程语言和数据库中使用字符串
    10. ImageField()
        - 数据库类型:varchar(100)
        - 作用:在数据库中为了保存图片的路径
        - 编程语言和数据库中使用字符串
        - 示例:
            ```
            image=models.ImageField(
                upload_to="static/images"
            )
            ```
        - upload_to:指定图片的上传路径
            在后台上传时会自动的将文件保存在指定的目录下
    11. TextField()
        - 数据库类型:longtext
        - 作用:表示不定长的字符数据
- 参考文档 <https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-types>
  
4. 字段选项FIELD_OPTIONS
    - 字段选项, 指定创建的列的额外的信息
    - 允许出现多个字段选项,多个选项之间使用,隔开
    1. primary_key
        - 如果设置为True,表示该列为主键,**如果指定一个字段为主键，则此数库表不会创建id字段**
    2. blank 
        - 设置为True时，字段可以为空。设置为False时，字段是必须填写的。字符型字段CharField和TextField是用空字符串来存储空值的。 默认值是False。
    3. null
        - 如果设置为True,表示该列值允许为空。日期型、时间型和数字型字段不接受空字符串。所以设置IntegerField，DateTimeField型字段可以为空时，需要将blank，null均设为True。
        - 默认为False,如果此选项为False建议加入default选项来设置默认值
    4. default
        - 设置所在列的默认值,如果字段选项null=False建议添加此项
    5. db_index
        - 如果设置为True,表示为该列增加索引
    6. unique
        - 如果设置为True,表示该字段在数据库中的值必须是唯一(不能重复出现的)
    7. db_column
        - 指定列的名称,如果不指定的话则采用属性名作为列名
    8. verbose_name
        - 设置此字段在admin界面上的显示名称。
    - 示例:
        ```python
        # 创建一个属性,表示用户名称,长度30个字符,必须是唯一的,不能为空,添加索引
        name = models.CharField(max_length=30, unique=True, null=False, db_index=True)
        ```
- 文档参见:
    - <https://docs.djangoproject.com/en/1.11/ref/models/fields/#field-options>


### 数据库迁移的错误处理方法
- 当执行 `$ python3 manage.py makemigrations` 出现如下迁移错误时的处理方法
    - 错误信息
        ```
        $ python3 manage.py makemigrations
        You are trying to change the nullable field 'title' on book to non-nullable without a default; we can't do that (the database needs something to populate existing rows).
        Please select a fix:
        1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
        2) Ignore for now, and let me handle existing rows with NULL myself (e.g. because you added a RunPython or RunSQL operation to handle NULL values in a previous data migration)
        3) Quit, and let me add a default in models.py
        Select an option: 
        ```
    - 翻译为中文如下:
        ```
        $ python3 manage.py makemigrations
        您试图将图书上的可空字段“title”更改为非空字段(没有默认值);我们不能这样做(数据库需要填充现有行)。
        请选择修复:
        1)现在提供一次性默认值(将对所有现有行设置此列的空值)
        2)暂时忽略，让我自己处理空值的现有行(例如，因为您在以前的数据迁移中添加了RunPython或RunSQL操作来处理空值)
        3)退出，让我在models.py中添加一个默认值
        选择一个选项:
        ```
    - 错误原因
        - 当将如下代码
        ```
        class Book(models.Model):
            title = models.CharField("书名", max_length=50, null=True)
        ```
        - 去掉 null=True 改为如下内容时会出现上述错误
        ```
        class Book(models.Model):
            title = models.CharField("书名", max_length=50)
        ```
        - 原理是 此数据库的title 字段由原来的可以为NULL改为非NULL状态,意味着原来这个字段可以不填值，现在改为必须填定一个值，那填什么值呢？此时必须添加一个缺省值。
    - 处理方法:
        1. 选择1 手动给出一个缺省值，在生成 bookstore/migrations/000x_auto_xxxxxxxx_xxxx.py 文件时自动将输入的值添加到default参数中
        2. 暂时忽略，以后用其它的命令处理缺省值问题(不推荐)
        3. 退出当前生成迁移文件的过程，自己去修改models.py, 新增加一个`default=XXX` 的缺省值(推荐使用)

- 数据库的迁移文件混乱的解决办法
  
    数据库混乱： class Migration对应不上
    
    1. 删除 所有 migrations 里所有的 000?_XXXX.py (`__init__.py`除外)
    2. 删除 数据表
        - sql> drop database mywebdb;
    3. 重新创建 数据表
        - sql> create datebase mywebdb default charset...;
    4. 重新生成migrations里所有的 000?_XXXX.py
        - python3 manage.py makemigrations
    5. 重新更新数据库
        - python3 manage.py migrate

## 数据库的基本操作

用ORM对象进行数据库的增删改查操作    

- 数据库的基本操作包括增删改查操作，即(CRUD操作)
- CRUD是指在做计算处理时的增加(Create)、读取查询(Read)、更新(Update)和删除(Delete)
- 删、改、查操作基础是获取一个查询结果集,用于定位

### 管理器对象
- 每个继承自 models.Model 的模型类，都会有一个 objects 对象被同样继承下来。这个对象叫管理器对象
- 数据库的增删改查可以通过模型的管理器实现
    ```python
    class MyModel(models.Model):
        ...
    MyModel.objects.create(...) # objects 是管理器对象
    ```

### 创建数据对象
- Django 使用一种直观的方式把数据库表中的数据表示成Python 对象
- 创建数据中每一条记录就是创建一个数据对象
    1. 方法1  MyModel.objects.create(属性1=值1, 属性2=值1,...)
        - 成功: 返回创建好的实体对象
        - 失败: 抛出异常
    2. 创建 MyModel 实例对象,并调用 save() 进行保存
        ```python
        obj = MyModel(属性=值,属性=值)
        obj.属性=值
        obj.save()
        无返回值,保存成功后,obj会被重新赋值
        ```



### Django shell 的使用

- 在Django提供了一个交互式的操作项目叫 `Django Shell` 它能够在交互模式用项目工程的代码执行相应的操作
- 利用 Django Shell 可以代替编写View的代码来进行直接操作
- 在Django Shell 下只能进行简单的操作，不能运行远程调式
- 启动方式:
    ```shell
    $ python3 manage.py shell
    ```

- 练习:
    ```
    在 bookstore/models.py 应用中添加两个model类
    1. Book - 图书
        1. title - CharField 书名,非空,唯一
        2. pub - CharField 出版社,字符串,非空
        3. price - 图书定价,,
        4. market_price - 图书零售价
    2. Author - 作者
        1. name - CharField 姓名,非空
        2. age - IntegerField, 年龄,非空，缺省值为1
        3. email - EmailField, 邮箱,允许为空
    ```
    - 然后用 Django Shell 添加如下数据
        - 图书信息
            | 书名   | 定价 | 零售价 | 出版社      |
            |---------|-------|--------------|----------------|
            | Python  | 20.00 |        25.00 | 清华大学出版社 |
            | Python3 | 60.00 |        65.00 | 清华大学出版社 |
            | Django  | 70.00 |        75.00 | 清华大学出版社 |
            | JQuery  | 90.00 |        85.00 | 机械工业出版社 |
            | Linux   | 80.00 |        65.00 | 机械工业出版社 |
            | Windows | 50.00 |        35.00 | 机械工业出版社 |
            | HTML5   | 90.00 |       105.00 | 清华大学出版社 |
        - 作者信息:
            | 姓名   | 年龄 | 邮箱 |
            |-------|------|-----|
            | 王老师 | 28 | wangweichao@tedu.cn |
            | 吕老师 | 31 | lvze@tedu.cn |
            | 祁老师 | 30 | qitx@tedu.cn |
        





# day4《Django Web框架教学笔记》

- 讲师: 魏明择
- 时间: 2019





#### 查询数据

- 数据库的查询需要使用管理器对象进行

- 通过 MyModel.objects 管理器方法调用查询接口

  | 方法      | 说明                              |
  | --------- | --------------------------------- |
  | all()     | 查询全部记录,返回QuerySet查询对象 |
  | get()     | 查询符合条件的单一记录            |
  | filter()  | 查询符合条件的多条记录            |
  | exclude() | 查询符合条件之外的全部记录        |
  | ...       |                                   |

1. all()方法

   - 方法: all()

   - 用法: MyModel.objects.all()

   - 作用: 查询MyModel实体中所有的数据

     - 等同于
       - select * from tabel

   - 返回值: QuerySet容器对象,内部存放 MyModel 实例

   - 示例:

     ```python
     from bookstore import models
     books = models.Book.objects.all()
     for book in books:
         print("书名", book.title, '出版社:', book.pub)
     ```

2. 在模型类中定义 `def __str__(self): ` 方法可以将自定义默认的字符串

   ```python
   class Book(models.Model):
       title = ...
       def __str__(self):
           return "书名: %s, 出版社: %s, 定价: %s" % (self.title, self.pub, self.price)
   ```

3. 查询返回指定列(字典表示)

   - 方法: values('列1', '列2')

   - 用法: MyModel.objects.values(...)

   - 作用: 查询部分列的数据并返回

     - select 列1,列2 from xxx

   - 返回值: QuerySet

     - 返回查询结果容器，容器内存字典，每个字典代表一条数据,
     - 格式为: {'列1': 值1, '列2': 值2}

   - 示例:

     ```python
     from bookstore import models
     books = models.Book.objects.values("title", "pub")
     for book in books:
         print("书名", book["title"], '出版社:', book['pub'])
         print("book=", book)
     ```

4. 查询返回指定列（元组表示)

   - 方法:values_list('列1','列2')

   - 用法:MyModel.objects.values_list(...)

   - 作用:

     - 返回元组形式的查询结果

   - 返回值: QuerySet容器对象,内部存放 `元组`

     - 会将查询出来的数据封装到元组中,再封装到查询集合QuerySet中

   - 示例:

     ```python
     from bookstore import models
     books = models.Book.objects.values_list("title", "pub")
     for book in books:
     print("book=", book)  # ('Python', '清华大学出版社')...
     ```

5. 排序查询

   - 方法:order_by

   - 用法:MyModel.objects.order_by('-列','列')

   - 作用:

     - 与all()方法不同，它会用SQL 语句的ORDER BY 子句对查询结果进行根据某个字段选择性的进行排序

   - 说明:

   - 默认是按照升序排序,降序排序则需要在列前增加'-'表示

   - 示例:

     ```python
     from bookstore import models
     books = models.Book.objects.order_by("price")
     for book in books:
     print("书名:", book.title, '定价:', book.price)
     ```

6. 根据条件查询多条记录

   - 方法: filter(条件)

   - 语法: 

     ```python
     MyModel.objects.filter(属性1=值1, 属性2=值2)
     ```

   - 返回值:

     - QuerySet容器对象,内部存放 MyModel 实例

   - 说明:

     - 当多个属性在一起时为"与"关系，即当`Books.objects.filter(price=20, pub="清华大学出版社")` 返回定价为20 `且` 出版社为"清华大学出版社"的全部图书

   - 示例:

     ```python
     # 查询书中出版社为"清华大学出版社"的图书
     from bookstore import models
     books = models.Book.objects.filter(pub="清华大学出版社")
     for book in books:
         print("书名:", book.title)
     
     2. 查询Author实体中id为1并且isActive为True的
         - authors=Author.objects.filter(id=1,isActive=True)
     ```

### 字段查找

- 字段查询是指如何指定SQL语句中 WHERE 子句的内容。

- 字段查询需要通过QuerySet的filter(), exclude() and get()的关键字参数指定。

- 非等值条件的构建,需要使用字段查询

- 示例:

  ```python
  # 查询作者中年龄大于30
  Author.objects.filter(age__gt=30)
  # 对应
  # SELECT .... WHERE AGE > 35;
  ```

#### 查询谓词

- 每一个查询谓词是一个独立的查询功能

1. `__exact` : 等值匹配

   ```python
   Author.objects.filter(id__exact=1)
   # 等同于select * from author where id = 1
   
   ```

2. `__contains` : 包含指定值

   ```python
   Author.objects.filter(name__contains='w')
   # 等同于 select * from author where name like '%w%'
   
   ```

3. `__startswith` : 以 XXX 开始

   ```
   #  等同于 xxx%
   ```

   

4. `__endswith` : 以 XXX 结束

   ```
   # 等同于  %xxx
   ```

   

5. `__gt` : 大于指定值

   ```python
   Author.objects.filer(age__gt=50)
   # 等同于 select * from author where age > 50
   
   ```

6. `__gte` : 大于等于

7. `__lt` : 小于

8. `__lte` : 小于等于

9. `__in` : 查找数据是否在指定范围内

   - 示例

   ```python
   Author.objects.filter(country__in=['中国','日本','韩国'])
   # 等同于 select * from author where country in ('中国','日本','韩国')
   
   ```

10. `__range`: 查找数据是否在指定的区间范围内

    ```python
    # 查找年龄在某一区间内的所有作者
    Author.objects.filter(age__range=(35,50))
    # 等同于 SELECT ... WHERE Author BETWEEN 35 and 50;
    
    ```

11. 详细内容参见: <https://docs.djangoproject.com/en/1.11/ref/models/querysets/#field-lookups>

- 示例

  ```python
  MyModel.objects.filter(id__gt=4)
  # 等同于 SELECT ... WHERE id > 4;
  
  ```

- 练习:

  1. 查询Author表中age大于等于85的信息
     - `Author.objects.filter(age__gte=85)`
  2. 查询Author表中姓王的人的信息
     - `Author.objects.filter(name__startswith='王')`
  3. 查询Author表中Email中包含"wc"的人的信息
     - `Author.objects.filter(email__contains='wc')`

2. 不等的条件筛选

   - 语法:
     MyModel.objects.exclude(条件)

   - 作用:

     - 返回不包含此 `条件` 的 全部的数据集

   - 示例:

     - 查询 `清华大学出版社，定价大于50` 以外的全部图书

     ```python
     books = models.Book.objects.exclude(pub="清华大学出版社", price__gt=50)
     for book in books:
         print(book)
     
     ```

3. 查询指定的一条数据

   - 语法:
     MyModel.objects.get(条件)

   - 作用：

     - 返回满足条件的唯一一条数据

   - 返回值:

     - MyModel 对象

   - 

   - 说明:

     - 该方法只能返回一条数据
     - 查询结果多余一条数据则抛出,Model.MultipleObjectsReturned异常
     - 查询结果如果没有数据则抛出Model.DoesNotExist异常

   - 示例:

     ```python
     from bookstore import models
     try:
         book = models.Book.objects.get(id=1)
         print(book.title)
     except:
         ...
     
     ```

### 修改数据记录

1. 修改单个实体的某些字段值的步骤:

   1. 查
      - 通过 get() 得到要修改的实体对象
   2. 改
      - 通过 对象.属性 的方式修改数据过 对象.属性 的方式修改
   3. 保存
      - 通过 对象.save() 保存数据

   - 如:

     ```python
     from bookstore import models
     abook = models.Book.objects.get(id=10)
     abook.market_price = "10.5"
     abook.save()
     
     ```

2. 通过 QuerySet 批量修改 对应的全部字段

   - 直接调用QuerySet的update(属性=值) 实现批量修改

   - 如:

     ```python
     # 将 id大于3的所有图书价格定为0元
     books = Book.objects.filter(id__gt=3)
     books.update(price=0)
     # 将所有书的零售价定为100元
     books = Book.objects.all()
     books.update(market_price=100)
     
     ```

### 删除记录

- 删除记录是指删除数据库中的一条或多条记录
- 删除单个MyModel对象或删除一个查询结果集(QuerySet)中的全部对象都是调用 delete()方法

1. 删除单个对象

   - 步骤

     1. 查找查询结果对应的一个数据对象
     2. 调用这个数据对象的delete()方法实现删除

   - 示例:

     ```python
     try:
         auth = Author.objects.get(id=1)
         auth.delete()
     except:
         print(删除失败)
     
     ```

2. 删除查询结果集

   - 步骤

     1. 查找查询结果集中满足条件的全部QuerySet查询集合对象
     2. 调用查询集合对象的delete()方法实现删除

   - 示例:

     ```python
     # 删除全部作者中，年龄大于65的全部信息
     auths = Author.objects.filter(age__gt=65)
     auths.delete()
     
     ```

### 聚合查询

- 聚合查询是指对一个数据表中的一个字段的数据进行部分或全部进行统计查询,查bookstore_book数据表中的全部书的平均价格，查询所有书的总个数等,都要使用聚合查询

1. 不带分组聚合

   - 不带分组的聚合查询是指导将全部数据进行集中统计查询

   - 聚合函数:

     - 定义模块: `django.db.models`
     - 用法: `from django.db.models import *`
     - 聚合函数: 
       - Sum, Avg, Count, Max, Min

   - 语法: 

     - MyModel.objects.aggregate(结果变量名=聚合函数('列'))

   - 返回结果:

     - 由 结果变量名和值组成的字典
     - 格式为:
       - `{"结果变量名": 值}

   - 示例:

     ```python
     # 得到所有书的平均价格
     from bookstore import models
     from django.db.models import Count
     result = models.Book.objects.aggregate(myAvg=Avg('price'))
     print("平均价格是:", result['myAvg'])
     print("result=", result)  # {"myAvg": 58.2}
     
     # 得到数据表里有多少本书
     from django.db.models import Count
     result = models.Book.objects.aggregate(mycnt=Count('title'))
     print("数据记录总个数是:", result['mycnt'])
     print("result=", result)  # {"mycnt": 10}
     
     
     ```

2. 分组聚合

   - 分组聚合是指通过计算查询结果中每一个对象所关联的对象集合，从而得出总计值(也可以是平均值或总和)，即为查询集的每一项生成聚合。

   - 语法: 

     - QuerySet.annotate(结果变量名=聚合函数('列'))

   - 用法步骤:

     1. 通过先用查询结果MyModel.objects.value. 查找查询要分组聚合的列

        - MyModel.objects.value('列1', '列2')

        - 如: 

          ```python
          pub_set = models.Book.objects.values('pub')
          print(books)  # <QuerySet [{'pub': '清华大学出版社'}, {'pub': '清华大学出版社'}, {'pub_hou {'pub': '机械工业出版社'}, {'pub': '清华大学出版社'}]>
          
          
          ```

     2. 通过返回结果的 QuerySet.annotate 方法分组聚合得到分组结果

        - QuerySet.annotate(名=聚合函数('列'))

        - 返回 QuerySet 结果集,内部存储结果的字典

        - 如:

          ```python
          pub_count_set = pub_set.annotate(myCount=Count('pub'))
          print(pub_count_set)  # <QuerySet [{'pub': '清华大学出版社', 'myCount': 7}, {'pub': '机械工业出版社', 'myCount': 3}]>
          
          ```

     - .values('查询列名')

   - 示例:

     - 得到哪儿个出版社共出版多少本书

     ```python
     def test_annotate(request):
        - from django.db.models import Count
     from . import models
     
         # 得到所有出版社的查询集合QuerySet
         pub_set = models.Book.objects.values('pub')
         # 根据出版社查询分组，出版社和Count的分组聚合查询集合
         pub_count_set = pub_set.annotate(myCount=Count('pub'))  # 返回查询集合
         for item in pub_count_set:
             print("出版社:", item['pub'], "图书有：", item['myCount'])
         return HttpResponse('请查看服务器端控制台获取结果')
     
     ```

### F对象   #优雅的查询语句

如果不用F对象则需要从数据库抓取全部的数据到本地

- 一个F对象代表数据库中某条记录的字段的信息

1. 作用:

   - 通常是对数据库中的字段值在不获取的情况下进行操作
   - 用于类属性(字段)之间的比较。

2. 用法

   - F对象在数据包 django.db.models 中，使用时需要先导入
     - `from django.db.models import F`

3. 语法:

   ```python
   from django.db.models import F
   F('列名')
   
   ```

4. 说明:

   - 一个 F() 对象代表了一个model的字段的值
   - F对象通常是对数据库中的字段值在不加载到内存中的情况下直接在数据库服务器端进行操作



5. 示例1

   - 更新Book实例中所有的零售价涨10元

   ```python
   models.Book.objects.all().update(market_price=F('market_price')+10)
   # 以下做法好于如下代码
   books = models.Book.objects.all()
   for book in books:
       book.update(market_price=book.marget_price+10)
       book.save()
   
   ```

6. 示例2

   - 对数据库中两个字段的值进行比较，列出哪儿些书的零售价高于定价?
- 
  
   ```python
   from django.db.models import F
   from bookstore import models
   books = models.Book.objects.filter(market_price__gt=F('price'))
   for book in books:
       print(book.title, '定价:', book.price, '现价:', book.market_price)
   
   ```

### Q对象 - Q()   #用于处理复杂的查询逻辑

- 当在获取查询结果集 使用复杂的逻辑或  `|` 、 逻辑非 `~` 等操作时可以借助于 Q对象进行操作

- 如: 想找出定价低于20元 或 清华大学出版社的全部书，可以写成

  ```python
  models.Book.objects.filter(Q(price__lt=20)|Q(pub="清华大学出版社"))
  
  # 此处表示的是"与关系",若要表示"或"关系,直接用","连接
  ```

- Q对象在 数据包 django.db.models 中。需要先导入再使用

  - `from django.db.models import Q`

1. 作用

   - 在条件中用来实现除 and(&) 以外的 or(|) 或 not(~) 操作

2. 运算符:

   - & 与操作
   - | 或操作
   - 〜 非操作

3. 语法

   ```python
   from django.db.models import Q
   Q(条件1)|Q(条件2)  # 条件1成立或条件2成立
   Q(条件1)&Q(条件2)  # 条件1和条件2同时成立
   Q(条件1)&~Q(条件2)  # 条件1成立且条件2不成立
   ...
   
   ```

4. 示例

   ```python
   from django.db.models import Q
   # 查找清华大学出版社的书或价格低于50的书
   models.Book.objects.filter(Q(market_price__lt=50) | Q(pub_house='清华大学出版社'))
   # 查找不是机械工业出版社的书且价格低于50的书
   models.Book.objects.filter(Q(market_price__lt=50) & ~Q(pub_house='机械工业出版社'))
   
   ```

### 原生的数据库操作方法

- 使用MyModel.objects.raw()进行 数据库查询操作查询

  - 在django中，可以使用模型管理器的raw方法来执行select语句进行数据查询

  1. 语法: 
     - `MyModel.objects.raw(sql语句)`
  2. 用法
     - `MyModel.objects.raw('sql语句')`
  3. 返回值:
     - QuerySet 集合对象

4. 示例

   ```python
   books = models.Book.objects.raw('select * from bookstore_book')
   
   ```

for book in books:
        print(book)
    ```

- 使用django中的游标cursor对数据库进行 增删改操作

  - 在Django中可以使用 如UPDATE,DELETE等SQL语句对数据库进行操作。

  - 在Django中使用上述非查询语句必须使用游标进行操作

  - 使用步骤:

    1. 导入cursor所在的包

       - Django中的游标cursor定义在 django.db.connection包中，使用前需要先导入
       - 如：
         - `from django.db import connection`

    2. 用创建cursor类的构造函数创建cursor对象，再使用cursor对象的excute方法进行操作,为保证在出现异常时能释放cursor资源,通常使用with语句进行创建操作

       

       - 如:
       
         ```python
         from django.db import connection
         with connection.cursor() as cur:
             cur.execute('执行SQL语句')
     
         ```

    - 示例
    
      ```python
      # 用SQL语句将id 为 10的 书的出版社改为 "XXX出版社"
      from django.db import connection
      with connection.cursor() as cur: 
          cur.execute('update bookstore_book set pub_house="XXX出版社" where id=10;')
      
      with connection.cursor() as cur:
          # 删除 id为1的一条记录
          cur.execute('delete from bookstore_book where id=10;')
      
      ```







day05



# 《Django Web框架教学笔记》day05

- 讲师: 魏明择
- 时间: 2019



## admin 后台数据库管理

- django 提供了比较完善的后台管理数据库的接口，可供开发过程中调用和测试使用

- django 会搜集所有已注册的模型类，为这些模型类提拱数据管理界面，供开发者使用

- 使用步骤:

  1. 创建后台管理帐号:

     - 后台管理--创建管理员帐号

       - `$ python3 manage.py createsuperuser`            
       - 根据提示完成注册,参考如下:

       ```shell
       $ python3 manage.py createsuperuser
       Username (leave blank to use 'tarena'): tarena  # 此处输入用户名
       Email address: laowei@tedu.cn  # 此处输入邮箱
       Password: # 此处输入密码(密码要复杂些，否则会提示密码太简单)
       Password (again): # 再次输入重复密码
       Superuser created successfully.
       $ 
       ```

  2. 用注册的帐号登陆后台管理界面

     - 后台管理的登录地址:
       - <http://127.0.0.1:8000/admin>

### 自定义后台管理数据表

- 若要自己定义的模型类也能在 `/admin` 后台管理界中显示和管理，需要将自己的类注册到后台管理界面

- 添加自己定义模型类的后台管理数据表的,需要用`admin.site.register(自定义模型类)` 方法进行注册

  - 配置步骤如下:

    1. 在应用app中的admin.py中导入注册要管理的模型models类, 如:

       ```python
       from . import models
       ```

    2. 调用 admin.site.register 方法进行注册,如:

       ```python
       from django.contrib import admin
       admin.site.register(自定义模型类)
       ```

  - 如: 在 bookstore/admin.py 添加如下代码对Book类进行管理

  - 示例:

    ```python
    # file: bookstore/admin.py
    from django.contrib import admin
    # Register your models here.
    
    from . import models
    ...
    admin.site.register(models.Book)  # 将Book类注册为可管理页面
    ```

### 修改后台Models的展现形式

- 在admin后台管理数据库中对自定义的数据记录都展示为 `XXXX object` 类型的记录，不便于阅读和判断

- 在用户自定义的模型类中可以重写 `def __str__(self):` 方法解决显示问题,如:

  - 在 自定义模型类中重写 __str__(self) 方法返回显示文字内容:

  ```python
  class Book(models.Model):
      ...
      def __str__(self):
          return "书名" + self.title
  ```

### 模型管理器类

- 作用:

  - 为后台管理界面添加便于操作的新功能。

- 说明:

  - 后台管理器类须继承自 `django.contrib.admin` 里的 `ModelAdmin` 类

- 模型管理器的使用方法:

  1. 在 `<应用app>/admin.py` 里定义模型管理器类

     ```python
     class XXXX_Manager(admin.ModelAdmin):
         ......
     ```

  2. 注册管理器与模型类关联

     ```python
     from django.contrib import admin
     from . import models
     admin.site.register(models.YYYY, XXXX_Manager) # 注册models.YYYY 模型类与 管理器类 XXXX_Manager 关联
     ```

  - 示例:

    ```python
    # file : bookstore/admin.py
    from django.contrib import admin
    from . import models
    
    class BookAdmin(admin.ModelAdmin):
        list_display = ['id', 'title', 'price', 'market_price']
    
    admin.site.register(models.Book, BookAdmin)
    ```

    - 进入<http://127.0.0.1:8000/admin/bookstore/book/> 查看显示方式和以前有所不同

- 模型管理器类ModelAdmin中实现的高级管理功能

  1. list_display 去控制哪些字段会显示在Admin 的修改列表页面中。
  2. list_display_links 可以控制list_display中的字段是否应该链接到对象的“更改”页面。
  3. list_filter 设置激活Admin 修改列表页面右侧栏中的过滤器
  4. search_fields 设置启用Admin 更改列表页面上的搜索框。 
  5. list_editable 设置为模型上的字段名称列表，这将允许在更改列表页面上进行编辑。
  6. 其它参见<https://docs.djangoproject.com/en/1.11/ref/contrib/admin/>

### 数据库表管理

1. 修改模型类字段的显示名字

   - 模型类各字段的第一个参数为 verbose_name,此字段显示的名字会在后台数据库管理页面显示

   - 通过 verbose_name 字段选项,修改显示名称示例如下：

     ```python
     title = models.CharField(
         max_length = 30,
         verbose_name='显示名称'
     )
     
     ```

2. 通过Meta内嵌类 定义模型类的属性及展现形式

   - 模型类可以通过定义内部类class Meta 来重新定义当前模型类和数据表的一些属性信息

   - 用法格式如下:

     ```python
     class Book(models.Model):
         title = CharField(....)
         class Meta:
             1. db_table = '数据表名'
                 - 该模型所用的数据表的名称。(设置完成后需要立马更新同步数据库)
             2. verbose_name = '单数名'
                 - 给模型对象的一个易于理解的名称(单数),用于显示在/admin管理界面中
             3. verbose_name_plural = '复数名'
                 - 该对象复数形式的名称(复数),用于显示在/admin管理界面中
     
     ```

- 练习:
  - 将Book模型类 和 Author 模型类都加入后台管理
  - 制作一个AuthorManager管理器类，让后台管理Authors列表中显示作者的ID、姓名、年龄信息
  - 用后台管理程序 添加三条 Author 记录
  - 修改其中一条记录的年龄
  - 删除最后一条添加的记录
  - 将bookstore_author 数名表名称改为myauthor (需要重新迁移数据库)



## 数据表关联关系映射

- 在关系型数据库中，通常不会把所有数据都放在同一张表中，这样做会额外占用内存空间，
- 在关系列数据库中通常用表关联来解决数据库。
- 常用的表关联方式有三种:
  1. 一对一映射
     - 如: 一个身份证对应一个人
  2. 一对多映射
     - 如: 一个班级可以有多个学生
  3. 多对多映射
     - 如: 一个学生可以报多个课程，一个课程可以有多个学生学习

### 一对一映射

- 一对一是表示现实事物间存在的一对一的对应关系。
- 如:一个家庭只有一个户主，一个男人有一个妻子，一个人有一个唯一的指纹信息等

1. 语法

   ```python
   class A(model.Model):
       ...
   
   class B(model.Model):
       属性 = models.OneToOneField(A)
   
   ```

2. 用法示例

   1. 创建作家和作家妻子类

      ```python
      # file : xxxxxxxx/models.py
      from django.db import models
      
      class Author(models.Model):
          '''作家模型类'''
          name = models.CharField('作家', max_length=50)
      
      class Wife(models.Model):
          '''作家妻子模型类'''
          name = models.CharField("妻子", max_length=50)
          author = models.OneToOneField(Author)  # 增加一对一属性
      
      ```

   2. 查询

      - 在 Wife 对象中,通过 author 属性找到对应的author对象
      - 在 Author 对象中,通过 wife 属性找到对应的wife对象

   3. 创始一对一的数据记录

      ```python
      from . import models
      author1 = models.Author.objects.create(name='王老师')
      wife1 = models.Wife.objects.create(name='王夫人', author=author1)  # 关联王老师
      author2 = models.Author.objects.create(name='小泽老师')  # 一对一可以没有数据对应的数据 
      
      ```

   4. 一对一数据的相互获取

      1. 正向查询

         - 直接通过关联属性查询即可

         ```python
         # 通过 wife 找 author
         from . import models
         wife = models.Wife.objects.get(name='王夫人')
         print(wife.name, '的老公是', wife.author.name)
         
         ```

      2. 反向查询

         - 通过反向关联属性查询
         - 反向关联属性为`实例对象.引用类名(小写)`，如作家的反向引用为`作家对象.wife`
         - 当反向引用不存在时，则会触发异常

         ```python
         # 通过 author.wife 关联属性 找 wife,如果没有对应的wife刚触发异常
         author1 = models.Author.objects.get(name='王老师')
         print(author1.name, '的妻子是', author1.wife.name)
         author2 = models.Author.objects.get(name='小泽老师')
         try:
             print(author2.name, '的妻子是', author2.wife.name)
         except:
             print(author2.name, '还没有妻子')
         
         ```

- 作用:
  - 主要是解决常用数据不常用数据的存储问题,把经常加载的一个数据放在主表中，不常用数据放在另一个副表中，这样在访问主表数据时不需要加载副表中的数据以提高访问速度提高效率和节省内存空间,如经常把书的内容和书名建成两张表，因为在网站上经常访问书名等信息，但不需要得到书的内容。
- 练习:
  1. 创建一个Wife模型类,属性如下
     1. name 
     2. age 
  2. 在Wife类中增加一对一关联关系,引用 Author
  3. 同步回数据库并观察结果

### 一对多映射

- 一对多是表示现实事物间存在的一对多的对应关系。
- 如:一个学校有多个班级,一个班级有多个学生, 一本图书只能属于一个出版社,一个出版社允许出版多本图书

1. 用法语法

   - 当一个A类对象可以关联多个B类对象时

   ```python
   class A(model.Model):
       ...
   
   class B(model.Model):
       属性 = models.ForeignKey(多对一中"一"的模型类, ...)
   
   ```

2. 外键类ForeignKey 

   - 构造函数:

     ```python
     ForeignKey(to, on_delete, **options)
     
     ```

   - 常用参数:

     - on_delete
       1. models.CASCADE  级联删除。 Django模拟SQL约束ON DELETE CASCADE的行为，并删除包含ForeignKey的对象。
       2. models.PROTECT 抛出ProtectedError 以阻止被引用对象的删除;
       3. SET_NULL 设置ForeignKey null；只有null是True才有可能。
       4. SET_DEFAULT  将ForeignKey设置为其默认值；必须设置ForeignKey的默认值。
       5. ... 其它参请参考文档 <https://docs.djangoproject.com/en/1.11/ref/models/fields/#foreignkey> ForeignKey部分
     - `**options` 可以是常用的字段选项如:
       1. null
       2. unique等
       3. ...

3. 示例

   - 有二个出版社对应五本书的情况.
     1. `清华大学出版社` 有书
        1. C++
        2. Java
        3. Python
     2. `北京大学出版社` 有书
        1. 西游记
        2. 水浒

   1. 定义一对多类

      ```python
      # file: one2many/models.py
      from django.db import models
      class Publisher(models.Model):
          '''出版社'''
          name = models.CharField('名称', max_length=50, unique=True)
      
      class Book(models.Model):
          title = models.CharField('书名', max_length=50)
          publisher = models.ForeignKey(Publisher, null=True)
      
      
      ```

   - 创建一对多的对象

     ```python
     # file: xxxxx/views.py
     from . import models
     pub1 = models.Publisher.objects.create(name='清华大学出版社')
     models.Book.objects.create(title='C++', publisher=pub1)
     models.Book.objects.create(title='Java', publisher=pub1)
     models.Book.objects.create(title='Python', publisher=pub1)
     
     pub2 = models.Publisher.objects.create(name='北京大学出版社')
     models.Book.objects.create(title='西游记', publisher=pub2)
     models.Book.objects.create(title='水浒', publisher=pub2)
     
     ```

   - 查询:

     - 通过多查一

     ```python
     # 通过一本书找到对应的出版社
     abook = models.Book.objects.get(id=1)
     print(abook.title, '的出版社是:', abook.publisher.name)
     
     ```

     - 通过一查多

     ```python
     # 通过出版社查询对应的书
     pub1 = models.Publisher.objects.get(name='清华大学出版社')
     books = pub1.book_set.all()  # 通过book_set 获取pub1对应的多个Book数据对象
     # books = models.Book.objects.filter(publisher=pub1)  # 也可以采用此方式获取
     print("清华大学出版社的书有:")
     for book in books:
         print(book.title)
     
     ```

- 练习:
  1. 完成Book 和 Publisher 之间的一对多
  2. 查看数据库效果
  3. 登录到后台,查看Book实体

3. 数据查询

   1. 通过 Book 查询 Publisher

      ```
      通过 publisher 属性查询即可
      练习:
          查询 西游记 对应的出版社信息,打印在终端上
      
      ```

   2. 通过 Publisher 查询 对应的所有的 Books

      ```
      Django会在Publisher中增加一个属性来表示对对应的Book们的查询引用
      属性:book_set(MyModel.objects)
      
      ```

### 多对多映射

- 多对多表达对象之间多对多复杂关系，如: 每个人都有不同的学校(小学，初中，高中,...),每个学校都有不同的学生...

1. 语法

   - 在关联的两个类中的任意一个类中,增加:

   ```python
   属性 = models.ManyToManyField(MyModel)
   
   ```

2. 示例

   - 一个作者可以出版多本图书
   - 一本图书可以被多名作者同时编写

   ```python
   class Author(models.Model):
       ...
   
   class Book(models.Model):
       ...
       authors = models.ManyToManyField(Author)
   
   ```

3. 数据查询

   1. 通过 Book 查询对应的所有的 Authors

      ```python
      book.authors.all() -> 获取 book 对应的所有的author的信息
      book.authors.filter(age__gt=80) -> 获取book对应的作者中年龄大于80岁的作者的信息
      
      ```

   2. 通过 Author 查询对应的所有的Books

      - Django会生成一个关联属性 book_set 用于表示对对应的book的查询对象相关操作

      ```python
      author.book_set.all()
      author.book_set.filter()
      author.book_set.create(...)  # 创建新书并联作用author
      author.book_set.add(book)   # 添加已有的书为当前作者author
      author.book_set.clear()  # 删除author所有并联的书
      author.book_set.remove()  # 删除所author所有并联的书
      
      ```

4. 示例:

   - 多对多模型

   ```python
   class Author(models.Model):
       '''作家模型类'''
       name = models.CharField('作家', max_length=50)
       def __str__(self):
           return self.name
   class Book(models.Model):
       title = models.CharField('书名', max_length=50)
       author = models.ManyToManyField(Author, null=True)
       def __str__(self):
           return self.title
   
   ```

   - 多对多视图操作

   ```python
   from django.http import HttpResponse
   
   from . import models
   
   def many2many_init(request):
       # 创建两人个作者
       author1 = models.Author.objects.create(name='吕泽')
       author2 = models.Author.objects.create(name='魏老师')
   
       # 吕择和魏老师同时写了一本Python
       book11 = author1.book_set.create(title="Python")
       author2.book_set.add(book11)  #
   
       # 魏老师还写了两本书
       book21 = author2.book_set.create(title="C")  # 创建一本新书"C"
       book22 = author2.book_set.create(title="C++")  # 创建一本新书"C++"
   
       return HttpResponse("初始化成功")
   
   def show_many2many(request):
       authors = models.Author.objects.all()
       for auth in authors:
           print("作者:", auth.name, '发出版了', auth.book_set.count(), '本书: ')
           for book in books:
               print('    ', book.title)
       print("----显示书和作者的关系----")
       books = models.Book.objects.all()
       for book in books:
           auths = book.author.all()
           print(book.title, '的作者是:', '、'.join([str(x.name) for x in auths]))
       return HttpResponse("显示成功，请查看服务器端控制台终端")
   
   ```

   - 多对多最终的SQL结果

   ```sql
   mysql> select * from many2many_author;
   +----+-----------+
   | id | name      |
   +----+-----------+
   | 11 | 吕泽      |
   | 12 | 魏老师     |
   +----+-----------+
   2 rows in set (0.00 sec)
   
   mysql> select * from many2many_book;
   +----+--------+
   | id | title  |
   +----+--------+
   | 13 | Python |
   | 14 | C      |
   | 15 | C++    |
   +----+--------+
   3 rows in set (0.00 sec)
   
   mysql> select * from many2many_book_author;
   +----+---------+-----------+
   | id | book_id | author_id |
   +----+---------+-----------+
   | 17 |      13 |        11 |
   | 20 |      13 |        12 |
   | 18 |      14 |        12 |
   | 19 |      15 |        12 |
   +----+---------+-----------+
   4 rows in set (0.00 sec)
   
   ```

   - 示例示意图
     ![](images/manytomany.png)

## cookies 和 session

### cookies

- cookies是保存在客户端浏览器上的存储空间，通常用来记录浏览器端自己的信息和当前连接的确认信息

- cookies 在浏览器上是以键-值对的形式进行存储的，键和值都是以ASCII字符串的形存储(不能是中文字符串)

- cookies 的内部的数据会在每次访问此网址时都会携带到服务器端，如果cookies过大会降低响应速度

- 在Django 服务器端来设置 设置浏览器的COOKIE 必须通过 HttpResponse 对象来完成

- HttpResponse 关于COOKIE的方法

  - 添加、修改COOKIE
    - HttpResponse.set_cookie(key, value='', max_age=None, expires=None)
      - key:cookie的名字
      - value:cookie的值
      - max_age:cookie存活时间，秒为单位
      - expires:具体过期时间
      - 当不指定max_age和expires 时,关闭浏览器时此数据失效
  - 删除COOKIE
    - HttpResponse.delete_cookie(key)
    - 删除指定的key 的Cookie。 如果key 不存在则什么也不发生。

- Django中的cookies

  - 使用 响应对象HttpResponse 等 将cookie保存进客户端

    1. 方法1

       ```python
       from django.http import HttpResponse
       resp = HttpResponse()
       resp.set_cookie('cookies名', cookies值, 超期时间)
       
       ```

       - 如:

       ```python
       resp = HttpResponse()
       resp.set_cookie('myvar', "weimz", 超期时间)
       
       ```

    2. 方法二, 使用render对象

       ```python
       from django.shortcuts import render
       resp = render(request,'xxx.html',locals())
       resp.set_cookie('cookies名', cookies值, 超期时间)
       
       ```

  3. 获取cookie

     - 通过 request.COOKIES 绑定的字典(dict) 获取客户端的 COOKIES数据

       ```python
       value = request.COOKIES.get('cookies名', '没有值!')
       print("cookies名 = ", value)
       
       ```

  4. 注:

     - Chrome 浏览器 可能通过开发者工具的 `Application` >> `Storage` >> `Cookies` 查看和操作浏览器端所有的 Cookies 值

- cookies 示例

  - 以下示例均在视图函数中调用

  - 添加cookie

    ```python
    # 为浏览器添加键为 my_var1,值为123，过期时间为1个小时的cookie
    responds = HttpResponse("已添加 my_var1,值为123")
    responds.set_cookie('my_var1', 123, 3600)
    return responds
    
    ```

  - 修改cookie

    ```python
    # 为浏览器添加键为 my_var1,修改值为456，过期时间为2个小时的cookie
    responds = HttpResponse("已修改 my_var1,值为456")
    responds.set_cookie('my_var1', 456, 3600*2)
    return responds
    
    
    ```

  - 删除cookie

    ```python
    # 删除浏览器键为 my_var1的cookie
    responds = HttpResponse("已删除 my_var1")
    responds.delete_cookie('my_var1')
    return responds
    
    ```

  - 获取cookie

    ```python
    # 获取浏览器中 my_var变量对应的值
    value = request.COOKIES.get('my_var1', '没有值!')
    print("cookie my_var1 = ", value)
    return HttpResponse("my_var1:" + value)
    
    ```

- 综合练习:

  - 实现用户注册功能，界面如下:

    - 注册界面
      - ![](images/reg.png)

  - 要求 ：

    1. 创建一个 user 应用 实现注册逻辑,如:
       - `python3 manage.py startapp user`
    2. 如果用户注册成功，则用当前浏览器的cookies记录当前成功注册的用名名
    3. 注册时如果用户输入数据合法，则在数据库记中记录用户的用户名密码等数据

  - 模型类

    1. 用户模型类

       ```python
       class User(models.Model):
           username = models.CharField("用户名", max_length=30, unique=True)
           password = models.CharField("密码", max_length=30)
       
           def __str__(self):
               return "用户" + self.username
       
       ```

  - 登陆设计规范(在user应用中写代码)

    | 路由正则  | 视图函数               | 模板位置                     | 说明     |
    | --------- | ---------------------- | ---------------------------- | -------- |
    | /user/reg | def reg_view(request): | templates/user/register.html | 用户注册 |



### session 会话控制

- 什么是session

- session又名会话控制，是在服务器上开辟一段空间用于保留浏览器和服务器交互时的重要数据

- session的起源

  - http协议是无状态的：每次请求都是一次新的请求，不会记得之前通信的状态
  - 实现状态保持的方式：在客户端或服务器端存储与会话有关的数据
  - 推荐使用sesison方式，所有数据存储在服务器端

- 实现方式

  - 使用 session 需要在浏览器客户端启动 cookie，且用在cookie中存储sessionid
  - 每个客户端都可以在服务器端有一个独立的Session
  - 注意：不同的请求者之间不会共享这个数据，与请求者一一对应

- Django启用Session

  - 在 settings.py 文件中

  - 向 INSTALLED_APPS 列表中添加：

    ```python
    INSTALLED_APPS = [
        # 启用 sessions 应用
        'django.contrib.sessions',
    ]
    ```

  - 向 MIDDLEWARE_CLASSES 列表中添加：

    ```python
    MIDDLEWARE = [
        # 启用 Session 中间件
        'django.contrib.sessions.middleware.SessionMiddleware',
    ]
    ```

- session的基本操作:

  - session对于象是一个在似于字典的SessionStore类型的对象, 可以用类拟于字典的方式进行操作
  - session 只能够存储能够序列化的数据,如字典，列表等。

  1. 保存 session 的值到服务器
     - `request.session['KEY'] = VALUE`
  2. 获取session的值
     - `VALUE = request.session['KEY']`
     - `VALUE = request.session.get('KEY', 缺省值)`

  - 删除session的值
    - `del request.session['KEY']`
  - 在 settings.py 中有关 session 的设置
    1. SESSION_COOKIE_AGE
       - 作用: 指定sessionid在cookies中的保存时长(默认是2周)，如下:
       - `SESSION_COOKIE_AGE = 60 * 60 * 24 * 7 * 2`
    2. SESSION_EXPIRE_AT_BROWSER_CLOSE = True
       设置只要浏览器关闭时,session就失效(默认为False)
  - session 缺省配置
    - 模块
      - `import django.conf.global_settings`

- 注: 当使用session时需要迁移数据库,否则会出现错误

```sh
$ python3 manage.py makemigrations
$ python3 manage.py migrate
```




# 《Django Web框架教学笔记》day7
 - 讲师: 魏明择
 - 时间: 2019




## 中间件 Middleware
>可以把中间件理解为拦截插件,其优先级很高
>它是全局的部件,所有的请求和相应都可以经过中间件

- 中间件是 Django 请求/响应处理的钩子框架。它是一个轻量级的、低级的“插件”系统，用于全局改变 Django 的输入或输出。
- 每个中间件组件负责做一些特定的功能。例如，Django 包含一个中间件组件 AuthenticationMiddleware，它使用会话将用户与请求关联起来。
- 他的文档解释了中间件是如何工作的，如何激活中间件，以及如何编写自己的中间件。Django 具有一些内置的中间件，你可以直接使用。它们被记录在 built-in middleware reference 中。
- 中间件类:
    - 中间件类须继承自 `django.utils.deprecation.MiddlewareMixin`类
    - 中间件类须实现下列五个方法中的一个或多个:
        - `def process_request(self, request):` 执行视图之前被调用，在每个请求上调用，返回None或HttpResponse对象 
        >中间件return none 时表示可以进入下一步
        - `def process_view(self, request, callback, callback_args, callback_kwargs):` 调用视图之前被调用，在每个请求上调用，返回None或HttpResponse对象
        - `def process_response(self, request, response):` 所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象
        - `def process_exception(self, request, exception):` 当处理过程中抛出异常时调用，返回一个HttpResponse对象
        - `def process_template_response(self, request, response):` 在视图刚好执行完毕之后被调用，在每个请求上调用，返回实现了render方法的响应对象
    - 注： 中间件中的大多数方法在返回None时表示忽略当前操作进入下一项事件，当返回HttpResponese对象时表示此请求结果，直接返回给客户端

- 编写中间件类:
```python
# file : middleware/mymiddleware.py
from django.http import HttpResponse, Http404
from django.utils.deprecation import MiddlewareMixin

class MyMiddleWare(MiddlewareMixin):
    def process_request(self, request):
        print("中间件方法 process_request 被调用")

    def process_view(self, request, callback, callback_args, callback_kwargs):
        print("中间件方法 process_view 被调用")

    def process_response(self, request, response):
        print("中间件方法 process_response 被调用")
        return response

    def process_exception(self, request, exception):
        print("中间件方法 process_exception 被调用")

    def process_template_response(self, request, response):
        print("中间件方法 process_template_response 被调用")
        return response
```
- 注册中间件:
```python
# file : settings.py
MIDDLEWARE = [
    ...
    'middleware.mymiddleware.MyMiddleWare',
]
```
- 中间件的执行过程
    - ![](images/middleware.jpeg)


- 练习
    - 用中间件实现强制某个IP地址只能向/test 发送 5 次GET请求
    - 提示:
        - request.META['REMOTE_ADDR'] 可以得到远程客户端的IP地址
        - request.path_info 可以得到客户端访问的GET请求路由信息
    - 答案:
        ```python
        from django.http import HttpResponse, Http404
        from django.utils.deprecation import MiddlewareMixin
        import re
        class VisitLimit(MiddlewareMixin):
            '''此中间件限制一个IP地址对应的访问/user/login 的次数不能改过10次,超过后禁止使用'''
            visit_times = {}  # 此字典用于记录客户端IP地址有访问次数
            def process_request(self, request):
                ip_address = request.META['REMOTE_ADDR']  # 得到IP地址
                if not re.match('^/test', request.path_info):
                    return
                times = self.visit_times.get(ip_address, 0)
                print("IP:", ip_address, '已经访问过', times, '次!:', request.path_info)
                self.visit_times[ip_address] = times + 1
                if times < 5:
                    return

                return HttpResponse('你已经访问过' + str(times) + '次，您被禁止了')
        ```


### 跨站请求伪造保护 CSRF
- 跨站请求伪造攻击
    
    - 某些恶意网站上包含链接、表单按钮或者JavaScript，它们会利用登录过的用户在浏览器中的认证信息试图在你的网站上完成某些操作，这就是跨站请求伪造(CSRF，即Cross-Site Request Forgey)。 
- 说明:
    
- CSRF中间件和模板标签提供对跨站请求伪造简单易用的防护。 
    
- 作用:  
    
    - 不让其它表单提交到此 Django 服务器
- 解决方案:
    1. 取消 csrf 验证(不推荐)
        
        - 删除 settings.py 中 MIDDLEWARE 中的 `django.middleware.csrf.CsrfViewMiddleware` 的中间件
    3. 通过验证 csrf_token 验证
        ```python
        需要在表单中增加一个标签 
        {% csrf_token %}
        ```



## Django中的forms模块
- 在Django中提供了 forms 模块,用forms 模块可以自动生成form内部的表单控件,同时在服务器端可以用对象的形式接收并操作客户端表单元素，并能对表单的数据进行服务器端验证
- forms模块的作用
    - 可以用类来描述表单内部的控件，最终生成 HTML 格式的表单内容
    - 可以用 forms 模块进行表单验证

### 用form生成表单
- Form表单类示意：
    - Django Form 实现 Form 表单
        ```python
        class MySearch(forms.Form):
            input_text = forms.CharField(label = '请输入内容')
        ```
    - 此 form 表单生成的代码
        ```html
        <label for="id_input_text">请输入内容:</label>
        <input type="text" name="input_text" id="id_input_text" />
        ```

- 使用 forms 模块的步骤
    1. 在应用中创建 forms.py
    2. 导入 django 提供的 forms 模模
      
        - `from django import forms`
    3. 创建一个表单类，并在表单类内添加相应的控件
        ```python
            class Form表单类名(forms.Form):
                表单元素 = forms.Field类型(参数...)
                ...
        ```
    4. 创建表对象生成表单
        ```python
            form1 =  FormName()
            html = form1.as_p()  # html 绑定表单内部的input标签...
        ```
    5. 利用Form 类型的对象自动成表单内容
       ```html
           {{ form1.as_p }}
       ```

3. forms.Form 示例:
    1. 创建表单类
        ```python
        from django import forms

        class RegForm(forms.Form):
            username = forms.CharField(max_length=30, label='请输入用户名')
            password = forms.CharField(max_length=30, label='请输入密码')
            password2 = forms.CharField(max_length=20, label='请再次输入密码')
            ... ...
        ```
5. 字段参数
    1. label 
        - 控件前的文本
        >如果不填,则显示变量名为默认值
        
    2. widget
        - 指定小部件
    3. initial
        - 控件的初始值(主要针对文本框类型)
    4. required
        - 是否为必填项，值为(True/False)，默认为True

4. 在模板中解析form对象
    1. 方法
        1. 需要自定义 <form>
        2. 表单中的按钮需要自定义
    2. 解析form
        - 在 视图中创建form对象并发送到模板中解析.
        - 示例
            ```python
            form = XXXForm()
            return render(request,'xx.html',locals())
            ```
        1. 手动解析
            ```
            {% for field in form %}
                field : 表示的是form对象中的每个属性(控件)
                {{field.label}} : 表示的是label参数值
                {{field}} : 表示的就是控件
            {% endfor %}
            ```
    2. 自动解析
        1. {{form.as_p}}
            `将 form 中的每个属性(控件/文本)都使用p标记包裹起来再显示`
        2. {{form.as_ul}}
            ```
            将 form 中的每个属性(控件/文本)都使用li标记包裹起来再显示
            注意:必须手动提供ol 或 ul 标记
            ```
        3. {{form.as_table}}
            ```
            将 form 中的每个属性(控件/文本)都使用tr标记包裹起来再显示
            注意:必须手动提供table标记
            ```
    5. 通过 forms 对象获取表单数据
        1. 通过 forms.Form 子类的构造器来接收 post 数据
            - form = XXXForm(request.POST)
        2. 必须是 form 通过验证后,才能取值
            - form.is_valid()
                - 返回True:通过验证,可以取值
                - 返回False:暂未通过验证,则不能取值
        3. 通过 form.cleaned_data 字典的属性接收数据
            - form.cleaned_data : dict 类型

7. Field 内置小部件 - widget
    1. 什么是小部件
        - 表示的是生成到网页上的控件以及一些其他的html属性
        ```python
        message=forms.CharField(widget=forms.Textarea)
        upwd=forms.CharField(widget=forms.PasswordInput)
        ```
    2. 常用的小部件类型
        | widget名称 | 对应和type类值 |
        |-|-|
        | TextInput | type='text' |
        | PasswordInput | type='password' |
        | NumberInput | type="number" |
        | EmailInput | type="email" |
        | URLInput | type="url" |
        | HiddenInput | type="hidden" |
        | CheckboxInput | type="checkbox" |
        | CheckboxSelectMultiple | type="checkbox" |
        | RadioSelect  | type="radio" |
        | Textarea  | textarea标记 |
        | Select | select标记 |
        | SelectMultiple | select multiple 标记 |

3. 小部件的使用
    1. 继承自forms.Form
        1. 基本版
            1. 语法
                ```python
                属性 = forms.CharField() #无预选值使用
                    text,password,email,url,textarea,checkbox
                属性 = forms.ChoiceField() #有预选值使用
                    checkbox,radio,select

                属性 = forms.CharField(
                    label='xxx',
                    widget=forms.小部件类型
                )
                ```
            2. 示例:
                ```python
                upwd = forms.CharField(
                    label='用户密码',
                    widget=forms.PasswordInput
                )

                message = forms.CharField(
                    label='评论内容',
                    widget=forms.Textarea
                )
                ```

- 文档参见<https://docs.djangoproject.com/en/1.11/topics/forms/>


### Django之form表单验证
- django form 提供表单和字段验证
- 当在创建有不同的多个表单需要提交的网站时，用表单验证比较方便验证的封装
- 当调用form.is_valid() 返回True表示当前表单合法，当返回False说明表单验证出现问题
- 验证步骤:
    1. 先对form.XXXField() 参数值进行验证，比如:min_length,max_length,如果不符合form.is_valid()返回False
    2. 对各自from.clean_zzz属性名(self): 方法对相应属性进行验证,如果验证失败form.is_valid()返回False
    3. 调胳form.clean(self): 对表单的整体结构进行验证，如果验证失败form.is_valid()返回False
    4. 以上验证都成功 form.is_valid()返回True
- 验证方法:
    - def clean_xxx属性(self):
        - 验证失败必须抛出forms.ValidationError
        - 验证成功必须返回xxx属性的值
    - def clean(self):
        - 验证失败必须抛出forms.ValidationError
        - 验证成功必须返回 self.cleaned_data
- 文档参见<https://docs.djangoproject.com/en/1.11/ref/forms/validation/>

- 验证示例
```python
from django import forms
class RegisterForm(forms.Form):
    username = forms.CharField(label='用户名')
    password = forms.CharField(label='请输入密码', widget=forms.PasswordInput)
    password2 = forms.CharField(label='再次输入新密码', widget=forms.PasswordInput)

    def clean(self):
        pwd1 = self.cleaned_data['password']
        pwd2 = self.cleaned_data['password2']
        if pwd1 != pwd2:
            raise forms.ValidationError('两次密码不一致!')
        return self.cleaned_data  # 必须返回cleaned_data

    def clean_username(self):
        username = self.cleaned_data['username']
        if len(username) < 6:
            raise forms.ValidationError("用户名太短")
        return username
```



## 分页
- 分页是指在web页面有大量数据需要显示，为了阅读方便在每个页页中只显示部分数据。
- 好处:
    1. 方便阅读
    2. 减少数据提取量，减轻服务器压力。
- Django提供了Paginator类可以方便的实现分页功能 
- Paginator类位于`django.core.paginator` 模块中。

### Paginator对象
- 对象的构造方法
    - Paginator(object_list, per_page)
    - 参数
        - object_list 需要分类数据的对象列表
        - per_page 每页数据个数
    - 返回值:
        - 分页对象

- Paginator属性
    - count：需要分类数据的对象总数
    - num_pages：分页后的页面总数
    - page_range：从1开始的range对象, 用于记录当前面码数
    - per_page 每页数据的个数

- Paginator方法
    - Paginator.page(number)
        - 参数 number为页码信息(从1开始)
        - 返回当前number页对应的页信息
        - 如果提供的页码不存在，抛出InvalidPage异常

- Paginator异常exception
    - InvalidPage：当向page()传入一个无效的页码时抛出
    - PageNotAnInteger：当向page()传入一个不是整数的值时抛出
    - EmptyPage：当向page()提供一个有效值，但是那个页面上没有任何对象时抛出

### Page对象
- 创建对象
Paginator对象的page()方法返回Page对象，不需要手动构造
- Page对象属性
    - object_list：当前页上所有数据对象的列表
    - number：当前页的序号，从1开始
    - paginator：当前page对象相关的Paginator对象
- Page对象方法
    - has_next()：如果有下一页返回True
    - has_previous()：如果有上一页返回True
    - has_other_pages()：如果有上一页或下一页返回True
    - next_page_number()：返回下一页的页码，如果下一页不存在，抛出InvalidPage异常
    - previous_page_number()：返回上一页的页码，如果上一页不存在，抛出InvalidPage异常
    - len()：返回当前页面对象的个数
- 说明:
    - Page 对象是可迭代对象,可以用 for 语句来 访问当前页面中的每个对象

- 参考文档<https://docs.djangoproject.com/en/1.11/topics/pagination/>


- 分页示例:
    - 视图函数
    ```python
    from django.core.paginator import Paginator
    def book(request):
        bks = models.Book.objects.all()
        paginator = Paginator(bks, 10)
        print('当前对象的总个数是:', paginator.count)
        print('当前对象的面码范围是:', paginator.page_range)
        print('总页数是：', paginator.num_pages)
        print('每页最大个数:', paginator.per_page)

        cur_page = request.GET.get('page', 1)  # 得到默认的当前页
        page = paginator.page(cur_page)
        return render(request, 'bookstore/book.html', locals())
    ```
    - 模板设计
    ```html
    <html>
    <head>
        <title>分页显示</title>
    </head>
    <body>
    {% for b in page %}
        <div>{{ b.title }}</div>
    {% endfor %}

    {# 分页功能 #}
    {# 上一页功能 #}
    {% if page.has_previous %}
    <a href="{% url 'book' %}?page={{ page.previous_page_number }}">上一页</a>
    {% else %}
    上一页
    {% endif %}

    {% for p in paginator.page_range %}
        {% if p == page.number %}
            {{ p }}
        {% else %}
            <a href="{% url 'book' %}?page={{ p }}">{{ p }}</a>
        {% endif %}
    {% endfor %}

    {#下一页功能#}
    {% if page.has_next %}
    <a href="{% url 'book' %}?page={{ page.next_page_number }}">下一页</a>
    {% else %}
    下一页
    {% endif %}
    总页数: {{ page.len }}
    </body>
    </html>
    ```


## 文件上传
- 文件上传必须为POST提交方式
- 表单`<form>`中文件上传时必须有带有`enctype="multipart/form-data"` 时才会包含文件内容数据。
- 表单中用`<input type="file" name="xxx">`标签上传文件
    - 名字`xxx`对应`request.FILES['xxx']` 对应的内存缓冲文件流对象。可通能过`request.FILES['xxx']` 返回的对象获取上传文件数据
    - `file=request.FILES['xxx']` file 绑定文件流对象，可以通过文件流对象的如下信息获取文件数据
        file.name 文件名
        file.file 文件的字节流数据


- 上传文件的表单书写方式
    ```html
    <!-- file: index/templates/index/upload.html -->
    <html>
    <head>
        <meta charset="utf-8">
        <title>文件上传</title>
    </head>
    <body>
        <h3>上传文件</h3>
        <form method="post" action="/upload" enctype="multipart/form-data">
            <input type="file" name="myfile"/><br>
            <input type="submit" value="上传">
        </form>
    </body>
    </html>
    ```

- 在setting.py 中设置一个变量MEDIA_ROOT 用来记录上传文件的位置
    ```python
    # file : settings.py
    ...
    MEDIA_ROOT = os.path.join(BASE_DIR, 'static/files')
    ```
- 在当前项目文件夹下创建 `static/files` 文件夹
    ```shell
    $ mkdir -p static/files
    ```
- 添加路由及对应的处理函数
    ```python
    # file urls.py
    urlpatterns = [
        url(r'^admin/', admin.site.urls),
        url(r'^upload', views.upload_view)
    ]
    ```
- 上传文件的视图处理函数
    ```python
    # file views.py
    from django.http import HttpResponse, Http404
    from django.conf import settings
    import os

    def upload_view(request):
        if request.method == 'GET':
            return render(request, 'index/upload.html')
        elif request.method == "POST":
            a_file = request.FILES['myfile']
            print("上传文件名是:", a_file.name)

            filename =os.path.join(settings.MEDIA_ROOT, a_file.name)
            with open(filename, 'wb') as f:
                data = a_file.file.read()
                f.write(data)
                return HttpResponse("接收文件:" + a_file.name + "成功")
        raise Http404
    ```
- 访问地址: <http://127.0.0.1:8000/static/upload.html>




# 《Django Web框架教学笔记》
 - 讲师: 魏明择
 - 时间: 2019




## Django中的用户认证 (使用Django认证系统)
- Django带有一个用户认证系统。 它处理用户账号、组、权限以及基于cookie的用户会话。
- 作用:
    1. 添加普通用户和超级用户
    2. 修改密码

- 文档参见
    - <https://docs.djangoproject.com/en/1.11/topics/auth/>

- User模型类
    - 位置: `from django.contrib.auth.models import User`

- 默认user的基本属性有：
    | 属性名 |  类型 | 是否必选 |
    |-|-|-|
    | username | 用户名 | 是 |
    | password | 密码 | 是 |
    | email | 邮箱 | 可选 |
    | first_name | 名 |
    | last_name | 姓 |
    | is_superuser | 是否是管理员帐号(/admin) |
    | is_staff | 是否可以访问admin管理界面 |
    | is_active | 是否是活跃用户,默认True。一般不删除用户，而是将用户的is_active设为False。 |
    | last_login | 上一次的登录时间 |
    | date_joined | 用户创建的时间 |

- 数据库表现形式
```sql
mysql> use myauth;
mysql> desc auth_user;
+--------------+--------------+------+-----+---------+----------------+
| Field        | Type         | Null | Key | Default | Extra          |
+--------------+--------------+------+-----+---------+----------------+
| id           | int(11)      | NO   | PRI | NULL    | auto_increment |
| password     | varchar(128) | NO   |     | NULL    |                |
| last_login   | datetime(6)  | YES  |     | NULL    |                |
| is_superuser | tinyint(1)   | NO   |     | NULL    |                |
| username     | varchar(150) | NO   | UNI | NULL    |                |
| first_name   | varchar(30)  | NO   |     | NULL    |                |
| last_name    | varchar(30)  | NO   |     | NULL    |                |
| email        | varchar(254) | NO   |     | NULL    |                |
| is_staff     | tinyint(1)   | NO   |     | NULL    |                |
| is_active    | tinyint(1)   | NO   |     | NULL    |                |
| date_joined  | datetime(6)  | NO   |     | NULL    |                |
+--------------+--------------+------+-----+---------+----------------+
11 rows in set (0.00 sec)
```

### auth基本模型操作:
- 创建用户
    - 创建普通用户create_user
        ```python
        from django.contrib.auth import models
        user = models.User.objects.create_user(username='用户名', password='密码', email='邮箱',...)
        ...
        user.save()
        ```
    - 创建超级用户create_superuser
        ```python
        from django.contrib.auth import models
        user = models.User.objects.create_superuser(username='用户名', password='密码', email='邮箱',...)
        ...
        user.save()
        ```
- 删除用户
    ```python
    from django.contrib.auth import models
    try:
        user = models.User.objects.get(username='用户名')
        user.is_active = False  # 记当前用户无效
        user.save()
        print("删除普通用户成功！")
    except:
        print("删除普通用户失败")
    return HttpResponseRedirect('/user/info')
    ```
- 修改密码set_password
    ```python
    from django.contrib.auth import models
    try:
        user = models.User.objects.get(username='laowei')
        user.set_password('654321')
        user.save()
        return HttpResponse("修改密码成功！")
    except:
        return HttpResponse("修改密码失败！")
    ```
- 检查密码是否正确check_password
    ```python
    from django.contrib.auth import models
    try:
        user = models.User.objects.get(username='laowei')
        if user.check_password('654321'):  # 成功返回True,失败返回False
            return HttpResponse("密码正确")
        else:
            return HttpResponse("密码错误")
    except:
        return HttpResponse("没有此用户！")
    ```


## 项目部署
- 项目部署是指在软件开发完毕后，将开发机器上运行的开发板软件实际安装到服务器上进行长期运行
- 部署要分以下几个步骤进行
    1. 在安装机器上安装和配置同版本的数据库
    1. django 项目迁移(在安装机器上配置与开发环境相同的python版本及依懒的包)
    1. 用 uwsgi 替代`python3 manage.py runserver` 方法启动服务器
    1. 配置 nginx 反向代理服务器
    1. 用nginx 配置静态文件路径,解决静态路径问题

1. 安装同版本的数据库
    - 安装步骤略
2. django 项目迁移
    1. 安装python
        - `$ sudo apt install python3`
    2. 安装相同版本的包
        - 导出当前模块数据包的信息:
            - `$ pip3 freeze > package_list.txt`
        - 导入到另一台新主机
            - `$ pip3 install -r package_list.txt`
    3. 将当前项目源代码复制到运程主机上(scp 命令)
        - $ sudo scp -a 当前项目源代码 远程主机地址和文件夹


### WSGI Django工作环境部署
- WSGI (Web Server Gateway Interface)Web服务器网关接口，是Python应用程序或框架和Web服务器之间的一种接口，被广泛使用
- 它实现了WSGI协议、http等协议。Nginx中HttpUwsgiModule的作用是与uWSGI服务器进行交换。WSGI是一种Web服务器网关接口。

### uWSGI 网关接口配置 (ubuntu 18.04 配置)
- 使用 `python manage.py runserver` 通常只在开发和测试环境中使用。
- 当开发结束后，完善的项目代码需要在一个高效稳定的环境中运行，这时可以使用uWSGI
- uWSGI是WSGI的一种 ,它可以让Django、Flask等开发的web站点运行其中.

-  安装uWSGI
    - 在线安装 uwsgi
        ```shell
        $ sudo pip3 install uwsgi
        ```
    - 离线安装
        1. 在线下载安装包: 
            ```shell
            $ pip3 download uwsgi
            ```
            - 下载后的文件为 `uwsgi-2.0.18.tar.gz`
        2. 离线安装
            ```shell
            $ tar -xzvf uwsgi-2.0.18.tar.gz
            $ cd uwsgi-2.0.18
            $ sudo python3 setup.py install
            ```

- 配置uWSGI
    - 添加配置文件 `项目文件夹/uwsgi.ini`
        - 如: mysite1/uwsgi.ini
        ```ini
        [uwsgi]
        # 套接字方式的 IP地址:端口号
        # socket=127.0.0.1:8000
        # Http通信方式的 IP地址:端口号
        http=127.0.0.1:8000
        # 项目当前工作目录
        chdir=/home/weimz/.../my_project 这里需要换为项目文件夹的绝对路径
        # 项目中wsgi.py文件的目录，相对于当前工作目录
        wsgi-file=my_project/wsgi.py
        # 进程个数
        process=4
        # 每个进程的线程个数
        threads=2
        # 服务的pid记录文件
        pidfile=uwsgi.pid
        # 服务的目志文件位置
        daemonize=uwsgi.log
        ```
> 将debug = True改为debug = False
- uWSGI的运行管理
    - 启动 uwsgi
        ```shell
        $ cd 项目文件夹
        $ sudo uwsgi --ini 项目文件夹/uwsgi.ini
        ```
    - 停止 uwsgi
        ```shell
        $ cd 项目文件夹
        $ sudo uwsgi --stop uwsgi.pid
        ```
    - 说明:
      
        - 当uwsgi 启动后,当前django项目的程序已变成后台守护进程,在关闭当前终端时此进程也不会停止。
- 测试:
    - 在浏览器端输入<http://127.0.0.1:8000> 进行测试
    - 注意，此时端口号为8000

### nginx 反向代理配置
- Nginx是轻量级的高性能Web服务器，提供了诸如HTTP代理和反向代理、负载均衡、缓存等一系列重要特性，在实践之中使用广泛。
- C语言编写，执行效率高

- nginx 作用
    - 负载均衡， 多台服务器轮流处理请求
    - 反向代理
- 原理:
  
- 客户端请求nginx,再由nginx 请求 uwsgi, 运行django下的python代码
  
- ubuntu 下 nginx 安装
    $ sudo apt install nginx

- nginx 配置 
    - 修改nginx 的配置文件 /etc/nginx/sites-available/default
    ```
    # 在server节点下添加新的location项，指向uwsgi的ip与端口。
    server {
        ...
        location / {
            uwsgi_pass 127.0.0.1:8000;  # 重定向到127.0.0.1的8000端口
            include /etc/nginx/uwsgi_params; # 将所有的参数转到uwsgi下
        }
        ...
    }
    ```
- nginx服务控制
    ```shell
    $ sudo /etc/init.d/nginx start|stop|restart|status
    # 或
    $ sudo service nginx start|stop|restart|status
    ```
    > 通过 start,stop,restart,status 可能实现nginx服务的启动、停止、重启、查扑克状态等操作
- 修改uWSGI配置 
    - 修改`项目文件夹/uwsgi.ini`下的Http通信方式改为socket通信方式,如:
    ```ini
    [uwsgi]
    # 去掉如下
    # http=127.0.0.1:8000
    # 改为
    socket=127.0.0.1:8000
    ```
    - 重启uWSGI服务
    ```shell
    $ sudo uwsgi --stop uwsgi.pid
    $ sudo uwsgi --ini 项目文件夹/uwsgi.ini
    ```
```
    
- 测试:
    - 在浏览器端输入<http://127.0.0.1> 进行测试
    - 注意，此时端口号为80(nginx默认值)

### nginx 配置静态文件路径
- 解决静态路径问题
    ```ini
    # file : /etc/nginx/sites-available/default
    # 新添加location /static 路由配置，重定向到指定的绝对路径
    server {
        ...
        location /static {
            # root static文件夹所在的绝对路径,如:
            root /home/weimz/my_django_project; # 重定向/static请求的路径，这里改为你项目的文件夹
        }
        ...
    }
```
- 修改配置文件后需要重新启动 nginx 服务

### 404 界面
- 在模板文件夹内添加 404.html 模版，当视图触发Http404 异常时将会被显示
- 404.html 仅在发布版中(即setting.py 中的 DEBUG=False时) 才起作用
- 当向应处理函数触发Http404异常时就会跳转到404界面
    ```python
    from django.http import Http404
    def xxx_view(request):
        raise Http404  # 直接返回404
    ```
