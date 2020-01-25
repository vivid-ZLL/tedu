#html优化
js,css,html在线压缩


#float使用笔记
当在多个同级元素中使用float时,float会与它的上一同级元素保持水平高度

-----------------------------------------------------------------------------
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>Document</title>
    <script src="blog/js/jquery.min.js"></script>
    <style>
        #d01{
            border: 1px red solid;
            width: 100px;
            height: 100px;
        }
        #d02{
            border: 1px red solid;
            width: 100px;
            height: 100px;
            float:right;
        }
        #d00{
            border: 1px red solid;
        }
        #d03{
            
            border: 10px red solid;
            width: 100px;
            height: 100px;
        }
    </style>
</head>

<body>
    <div style="width: 500px;height: 500px;" id="d00">
            <div id="d01"></div>
        <div id="d02"></div>
        <div id="d03"></div>
    </div>
    



    <script>

    </script>
</body>

</html>

--------------------------------------------------------------------

#三目运算测试
 var v = 0;
        var a = v ==""?true:false
        console.log(a) // a = true
        console.log(v)  //v = 0

#对齐快捷键
ctrl K + ctrl F
#折叠快捷键
ctrl K + ctrl 0
#展开快捷键
ctrl K + ctrl J
#笔记
console.log((1,2,3,4)===4)  结果为true

# 人为添加权重的方法
在css样式后加"!important",人为增加样式的权重

# RegExp 对象
RegExp 对象表示正则表达式，它是对字符串执行模式匹配的强大工具。

#js对象与jq对象
dom对象属于一种js对象
dom对象才能使用dom中的方法，jquery对象不可以使用dom中的方法，但 jquery对象提供
了一套更加完善的工具用于操作dom。

平时用到的jquery对象都是通过$()函数制造出来的，$()函数就是一个jquery对象的制造工厂。

注意：
如果获取的对象是 jquery对象，那么在变量前面加上$,这样方便容易识别出哪些是jquery对象。
举例：

var $variable = jquery对象;
如果获取的是dom对象，则定义如下:

var variable = dom对象

##js对象与jq对象对属性的操作

js对象
b.style.backgroundColor = "blue"

jq对象
$b.css("backgroundColor","red")





#JSON表示单个对象

​			1.使用 {} 表示单个对象

​			2.在 {} 中使用 key:value 的形式来表示属性(数据)

​			3.Key必须要用 " " 引起来

​			4.value如果是字符串的话，也需要用" "引起来

js里的json对象 -> 符合json规范的js对象
json字符串  -> 符合json规范的字符串

```javascript
    var obj = {
            "name":"王老师",
            "age" : 30,
            "gender" : "Unknown"
    }
```




#jQ抓取了复数对象之后返回的是什么?
与document.getElementsByTagName类似,返回的是包含数个div对象的数组,一个是jq对象一个是js对象

#js声明全局变量?
局部 JavaScript 变量
在 JavaScript 函数内部声明的变量（使用 var）是局部变量，所以只能在函数内部访问它。（该变量的作用域是局部的）。

您可以在不同的函数中使用名称相同的局部变量，因为只有声明过该变量的函数才能识别出该变量。

只要函数运行完毕，本地变量就会被删除。

全局 JavaScript 变量
在函数外声明的变量是全局变量，网页上的所有脚本和函数都能访问它。

JavaScript 变量的生存期
JavaScript 变量的生命期从它们被声明的时间开始。

局部变量会在函数运行以后被删除。

全局变量会在页面关闭后被删除。

向未声明的 JavaScript 变量分配值
如果您把值赋给尚未声明的变量，该变量将被自动作为 window 的一个属性。

这条语句：

carname="Volvo";
将声明 window 的一个属性 carname。

非严格模式下给未声明变量赋值创建的全局变量，是全局对象的可配置属性，可以删除。

var var1 = 1; // 不可配置全局属性
var2 = 2; // 没有使用 var 声明，可配置全局属性

console.log(this.var1); // 1
console.log(window.var1); // 1

delete var1; // false 无法删除
console.log(var1); //1

delete var2; 
console.log(delete var2); // true
console.log(var2); // 已经删除 报错变量未定义






直接量语法
/pattern/attributes
创建 RegExp 对象的语法：
new RegExp(pattern, attributes);
参数
参数 pattern 是一个字符串，指定了正则表达式的模式或其他正则表达式。

参数 attributes 是一个可选的字符串，包含属性 "g"、"i" 和 "m"，分别用于指定全局匹配、区分大小写的匹配和多行匹配。ECMAScript 标准化之前，不支持 m 属性。如果 pattern 是正则表达式，而不是字符串，则必须省略该参数。

返回值
一个新的 RegExp 对象，具有指定的模式和标志。如果参数 pattern 是正则表达式而不是字符串，那么 RegExp() 构造函数将用与指定的 RegExp 相同的模式和标志创建一个新的 RegExp 对象。

如果不用 new 运算符，而将 RegExp() 作为函数调用，那么它的行为与用 new 运算符调用时一样，只是当 pattern 是正则表达式时，它只返回 pattern，而不再创建一个新的 RegExp 对象。

抛出
SyntaxError - 如果 pattern 不是合法的正则表达式，或 attributes 含有 "g"、"i" 和 "m" 之外的字符，抛出该异常。

TypeError - 如果 pattern 是 RegExp 对象，但没有省略 attributes 参数，抛出该异常。

修饰符
```
修饰符	描述
i	执行对大小写不敏感的匹配。
g	执行全局匹配（查找所有匹配而非在找到第一个匹配后停止）。
m	执行多行匹配。
方括号
方括号用于查找某个范围内的字符：

表达式	描述
[abc]	查找方括号之间的任何字符。
[^abc]	查找任何不在方括号之间的字符。
[0-9]	查找任何从 0 至 9 的数字。
[a-z]	查找任何从小写 a 到小写 z 的字符。
[A-Z]	查找任何从大写 A 到大写 Z 的字符。
[A-z]	查找任何从大写 A 到小写 z 的字符。
[adgk]	查找给定集合内的任何字符。
[^adgk]	查找给定集合外的任何字符。
(red|blue|green)	查找任何指定的选项。
```


元字符
```
元字符（Metacharacter）是拥有特殊含义的字符：

元字符	描述
.	查找单个字符，除了换行和行结束符。
\w	查找单词字符。
\W	查找非单词字符。
\d	查找数字。
\D	查找非数字字符。
\s	查找空白字符。
\S	查找非空白字符。
\b	匹配单词边界。
\B	匹配非单词边界。
\0	查找 NUL 字符。
\n	查找换行符。
\f	查找换页符。
\r	查找回车符。
\t	查找制表符。
\v	查找垂直制表符。
\xxx	查找以八进制数 xxx 规定的字符。
\xdd	查找以十六进制数 dd 规定的字符。
\uxxxx	查找以十六进制数 xxxx 规定的 Unicode 字符。
```

量词
```
量词	描述
n+	匹配任何包含至少一个 n 的字符串。
n*	匹配任何包含零个或多个 n 的字符串。
n?	匹配任何包含零个或一个 n 的字符串。
n{X}	匹配包含 X 个 n 的序列的字符串。
n{X,Y}	匹配包含 X 至 Y 个 n 的序列的字符串。
n{X,}	匹配包含至少 X 个 n 的序列的字符串。
n$	匹配任何结尾为 n 的字符串。
^n	匹配任何开头为 n 的字符串。
?=n	匹配任何其后紧接指定字符串 n 的字符串。
?!n	匹配任何其后没有紧接指定字符串 n 的字符串。
RegExp 对象属性
属性	描述	FF	IE
global	RegExp 对象是否具有标志 g。	1	4
ignoreCase	RegExp 对象是否具有标志 i。	1	4
lastIndex	一个整数，标示开始下一次匹配的字符位置。	1	4
multiline	RegExp 对象是否具有标志 m。	1	4
source	正则表达式的源文本。	1	4
RegExp 对象方法
方法	描述	FF	IE
compile	编译正则表达式。	1	4
exec	检索字符串中指定的值。返回找到的值，并确定其位置。	1	4
test	检索字符串中指定的值。返回 true 或 false。	1	4
支持正则表达式的 String 对象的方法
方法	描述	FF	IE
search	检索与正则表达式相匹配的值。	1	4
match	找到一个或多个正则表达式的匹配。	1	4
replace	替换与正则表达式匹配的子串。	1	4
split	把字符串分割为字符串数组。	1	4
```





# JS 触发事件大全
事件	浏览器	

一般事件  
onclick     IE3、N2	鼠标点击时触发此事件	
ondblclick	IE4、N4	鼠标双击时触发此事件
onmousedown	IE4、N4	按下鼠标时触发此事件
onmouseup	IE4、N4	鼠标按下后松开鼠标时触发此事件
onmouseover	IE3、N2	当鼠标移动到某对象范围的上方时触发此事件
onmousemove	IE4、N4	鼠标移动时触发此事件
onmouseout	IE4、N3	当鼠标离开某对象范围时触发此事件
onkeypress	IE4、N4	当键盘上的某个键被按下并且释放时触发此事件.
onkeydown	IE4、N4	当键盘上某个按键被按下时触发此事件
onkeyup	IE4、N4	当键盘上某个按键被按放开时触发此事件

页面相关事件			
onabort	IE4、N3	图片在下载时被用户中断	
onbeforeunload	IE4、N	当前页面的内容将要被改变时触发此事件
onerror	IE4、N3	出现错误时触发此事件
onload	IE3、N2	页面内容完成时触发此事件
onmove	IE、N4	浏览器的窗口被移动时触发此事件
onresize	IE4、N4	当浏览器的窗口大小被改变时触发此事件
onscroll	IE4、N	浏览器的滚动条位置发生变化时触发此事件
onstop	IE5、N	浏览器的停止按钮被按下时触发此事件或者正在下载的文件被中断
onunload	IE3、N2	当前页面将被改变时触发此事件

表单相关事件			
onblur	IE3、N2	当前元素失去焦点时触发此事件	
onchange	IE3、N2	当前元素失去焦点并且元素的内容发生改变而触发此事件
onfocus	IE3 、N2	当某个元素获得焦点时触发此事件
onreset	IE4 、N3	当表单中RESET的属性被激发时触发此事件
onsubmit	IE3 、N2	一个表单被递交时触发此事件

滚动字幕事件			
onbounce	IE4、N	在Marquee内的内容移动至Marquee显示范围之外时触发此事件	
onfinish	IE4、N	当Marquee元素完成需要显示的内容后触发此事件
onstart	IE4、 N	当Marquee元素开始显示内容时触发此事件

编辑事件			
onbeforecopy	IE5、N	当页面当前的被选择内容将要复制到浏览者系统的剪贴板前触发此事件	
onbeforecut	IE5、 N	当页面中的一部分或者全部的内容将被移离当前页面[剪贴]并移动到浏览者的系统剪贴板时触发此事件
onbeforeeditfocus	IE5、N	当前元素将要进入编辑状态
onbeforepaste	IE5、 N	内容将要从浏览者的系统剪贴板传送[粘贴]到页面中时触发此事件
onbeforeupdate	IE5、 N	当浏览者粘贴系统剪贴板中的内容时通知目标对象
oncontextmenu	IE5、N	当浏览者按下鼠标右键出现菜单时或者通过键盘的按键触发页面菜单时触发的事件
oncopy	IE5、N	当页面当前的被选择内容被复制后触发此事件
oncut	IE5、N	当页面当前的被选择内容被剪切时触发此事件
ondrag	IE5、N	当某个对象被拖动时触发此事件 [活动事件]
ondragdrop	IE、N4	一个外部对象被鼠标拖进当前窗口或者帧
ondragend	IE5、N	当鼠标拖动结束时触发此事件，即鼠标的按钮被释放了
ondragenter	IE5、N	当对象被鼠标拖动的对象进入其容器范围内时触发此事件
ondragleave	IE5、N	当对象被鼠标拖动的对象离开其容器范围内时触发此事件
ondragover	IE5、N	当某被拖动的对象在另一对象容器范围内拖动时触发此事件
ondragstart	IE4、N	当某对象将被拖动时触发此事件
ondrop	IE5、N	在一个拖动过程中，释放鼠标键时触发此事件
onlosecapture	IE5、N	当元素失去鼠标移动所形成的选择焦点时触发此事件
onpaste	IE5、N	当内容被粘贴时触发此事件
onselect	IE4、N	当文本内容被选择时的事件
onselectstart	IE4、N	当文本内容选择将开始发生时触发的事件

数据绑定			
onafterupdate	IE4、N	当数据完成由数据源到对象的传送时触发此事件	
oncellchange	IE5、N	当数据来源发生变化时
ondataavailable	IE4、N	当数据接收完成时触发事件
ondatasetchanged	IE4、N	数据在数据源发生变化时触发的事件
ondatasetcomplete	IE4、N	当来子数据源的全部有效数据读取完毕时触发此事件
onerrorupdate	IE4、N	当使用onBeforeUpdate事件触发取消了数据传送时，代替onAfterUpdate事件
onrowenter	IE5、N	当前数据源的数据发生变化并且有新的有效数据时触发的事件
onrowexit	IE5、N	当前数据源的数据将要发生变化时触发的事件
onrowsdelete	IE5、N	当前数据记录将被删除时触发此事件
onrowsinserted	IE5、N	当前数据源将要插入新数据记录时触发此事件

外部事件			
onafterprint	IE5、N	当文档被打印后触发此事件	
onbeforeprint	IE5、N	当文档即将打印时触发此事件
onfilterchange	IE4、N	当某个对象的滤镜效果发生变化时触发的事件
onhelp	IE4、N	当浏览者按下F1或者浏览器的帮助选择时触发此事件
onpropertychange	IE5、N	当对象的属性之一发生变化时触发此事件
onreadystatechange	IE4、N	当对象的初始化属性值发生变化时触发此事件

* css、javascript与html的关系
>网页前台分三个层次
>内容,样式,行为
>这是最新网页设计的要素,w3c标准要求
>内容用html表现,
>样式用css规定
>行为用脚本控制
>html的作用基本就是把一整块的东西切成一小块一小块的,必要的就标识一下(如id,class)
>以方便css和脚本引用和控制相应内容
>css就是给这些小块内容排队的,规定谁站哪,怎么站.
>脚本就是让那些小块内容做事的 .比如页面的图片轮播.就是由脚本控制相应元素的css属性达到切换的目的
>而目前网页前台用的最多的脚本就是javascript.是ecma标准的一个实现.各种浏览器都能支持


* undefined与null的区别
>   转载自：http://www.ruanyifeng.com/blog/2014/03/undefined-vs-null.html
>   
>   大多数计算机语言，有且仅有一个表示"无"的值，比如，C语言的NULL，Java语言的null，Python语言的None，Ruby语言的nil。
>   
>   有点奇怪的是，JavaScript语言居然有两个表示"无"的值：undefined和null。这是为什么？
>   
>   undefined vs. null
>   
>   一、相似性
>   在JavaScript中，将一个变量赋值为undefined或null，老实说，几乎没区别。
>   
>   var a = undefined;
>   
>   var a = null;
>   
>   上面代码中，a变量分别被赋值为undefined和null，这两种写法几乎等价。
>   
>   undefined和null在if语句中，都会被自动转为false，相等运算符甚至直接报告两者相等。
>   
>   if (!undefined) 
>       console.log('undefined is false');
>   // undefined is false
>   if (!null) 
>       console.log('null is false');
>   // null is false
>   undefined == null
>   // true
>   上面代码说明，两者的行为是何等相似！
>   
>   既然undefined和null的含义与用法都差不多，为什么要同时设置两个这样的值，这不是无端增加JavaScript的复杂度，令初学者困扰吗？Google公司开发的JavaScript语言的替代品Dart语言，就明确规定只有null，没有undefined！
>   
>   二、历史原因
>   最近，我在读新书《Speaking JavaScript》时，意外发现了这个问题的答案！
>   
>   原来，这与JavaScript的历史有关。1995年JavaScript诞生时，最初像Java一样，只设置了null作为表示"无"的值。
>   
>   根据C语言的传统，null被设计成可以自动转为0。
>   
>   Number(null)
>   // 0
>   5 + null
>   // 5
>   但是，JavaScript的设计者Brendan Eich，觉得这样做还不够，有两个原因。
>   
>   首先，null像在Java里一样，被当成一个对象。但是，JavaScript的数据类型分成原始类型（primitive）和合成类型（complex）两大类，Brendan Eich觉得表示"无"的值最好不是对象。
>   
>   其次，JavaScript的最初版本没有包括错误处理机制，发生数据类型不匹配时，往往是自动转换类型或者默默地失败。Brendan Eich觉得，如果null自动转为0，很不容易发现错误。
>   
>   因此，Brendan Eich又设计了一个undefined。
>   
>   三、最初设计
>   JavaScript的最初版本是这样区分的：null是一个表示"无"的对象，转为数值时为0；undefined是一个表示"无"的原始值，转为数值时为NaN。
>   
>   Number(undefined)
>   // NaN
>   5 + undefined
>   // NaN
>   四、目前的用法
>   但是，上面这样的区分，在实践中很快就被证明不可行。目前，null和undefined基本是同义的，只有一些细微的差别。
>   
>   null表示"没有对象"，即该处不应该有值。典型用法是：
>   
>   （1） 作为函数的参数，表示该函数的参数不是对象。
>   
>   （2） 作为对象原型链的终点。
>   
>   Object.getPrototypeOf(Object.prototype)
>   // null
>   undefined表示"缺少值"，就是此处应该有一个值，但是还没有定义。典型用法是：
>   
>   （1）变量被声明了，但没有赋值时，就等于undefined。
>   
>   （2) 调用函数时，应该提供的参数没有提供，该参数等于undefined。
>   
>   （3）对象没有赋值的属性，该属性的值为undefined。
>   
>   （4）函数没有返回值时，默认返回undefined。

---------------------------------------------
授课老师 ：陶国荣 

联系方式 ： taogr@tedu.cn

授课阶段 ： Web前端基础

授课内容 ： HTML + CSS + JavaScript

------
[TOC]
# 一、Web前端介绍
## 1. 什么是网页
网页是基于浏览器的应用程序，是数据展示的载体.
##  2. 网页的组成
1. 浏览器
	- 向服务器发送用户请求指令
	- 接收并解析数据展示给用户
2. 服务器
    - 存储数据
    - 处理并响应请求
3. 协议
    - 规范数据在传输过程中的打包方式
## 3. 网页的优势

1. 即时响应
   - 更新服务端页面即完成更新
   - 客户端重新加载即兑现内容
2. 无需安装和更新
   - 无需安装任何应用软件
   - 只需要一个浏览器执行即可

## 4. 开发前的准备

1. 运行环境：浏览器，设置chrome为默认浏览器，作为网页文件的运行环境。
2. 调试工具：浏览器自带的调试工具，使用快捷键"F12"或右键"检查"打开。
3. 开发工具：不限，选用个人习惯的即可。（Sublime、VSCode、EditPlus、Webstrom等）


.html,.htm

# 二、 HTML语法介绍
## 1. HTML介绍
超文本标记语言浏览器能够识别和解析的语言，通过标签的形式构建页面结构和填充内容
## 2. 标签
标签也称为标记或元素，用于在网页中标记内容
1. 语法：标签使用< >为标志，标签名不区分大小写，推荐小写表示
2. 分类：
    - 双标签：成对出现，包含开始标签和结束标签。例：

    ```html
    <html></html>
    ```

    - 单标签：只有开始标签，没有结束标签，可以手动添加“/”表示闭合。例：

    ```html
    <br>
    <br/>
    ```
3. 标签属性：
	- 标签属性书写在开始标签中，使用空格与标签名隔开，用于设置当前标签的显示内容或者修饰显示效果。由属性名和属性值组成，属性值使用双引号表示。例：

    ```HTML
    <img src="imgs/img01.jpg">
    ```

	- 同一个标签中可以添加若干组标签属性，使用空格间隔。例：

    ```html
    <img src="imgs/img01.jpg" width="200px" height="200px">
    ```
## 3. 使用
1. 创建网页文件，使用.html或.htm作为文件后缀。
2. 添加网页的基本结构：
    ```html 
    <!doctype html>
    <html>
    	<head>
    		<title>网页标题</title>
    		<meta charset="utf-8">
    	</head>
    	<body>
             网页主体内容
    	</body>
    </html>
    ```
3. 标签嵌套
    在双标签中书写其他标签，称为标签嵌套
    
    - 嵌套结构中，外层元素称为父元素，内层元素称为子元素。
    - 多层嵌套结构中，所有外层元素统称为祖先元素，内层元素统称为后代元素。
    - 平级结构互为兄弟元素。
4. HTML语法规范
	- 标签名不区分大小写，建议使用小写。
	- 注释语法：
	```html
	<!-- 此处为注释 -->
	```
# 三、常用标签介绍
## 1. 基本结构解析
 ```html
<!-- 文档类型声明，便于浏览器正确解析标签及渲染样式 -->
<!doctype html> 
<!-- HTML文档开始的标志 -->
<html> 
   <!-- 头部设置，可在head中设置网页标题，引入外部的资源文件 -->
   <head>
       <!-- 设置网页标题，显示在网页选项卡上方 -->
       <title>网页标题</title>
       <!-- 设置网页字符编码 -->
       <meta charset="utf-8"> 
   </head>
   <!-- 网页主体部分，显示网页主要内容 -->
   <body> 
       网页主体内容
   </body>
</html><!-- 文档结束-->
 ```

## 2. body中常用标签
  - 文本标签
    - 标题标签：自带加粗效果，从h1到h6字体大小逐级递减
    ```html
     <h1>一级标题</h1>
     <h2>二级标题</h2>
     <h3>三级标题</h3>
     <h4>四级标题</h4>
     <h5>五级标题</h5>
     <h6>六级标题</h6>
    ```
    - 段落标签：
     ```html
     <p>段落文本</p>
     ```
    - 普通文本标签：
     ```html
     <b>加粗标签</b>
     <strong>强调标签，效果同b标签</strong>
     <i>斜体标签</i>
     <u>删除线标签</u>
     <span>行分区标签，用于对特殊文本特殊处理</span>
     <label>普通文本标签，常与表单控件结合实现文本与控件的绑定</label>
     ```
    - 换行标签：
     浏览器会忽略代码中的换行和空格，只显示为一个空格。想要实现页面中的换行，需要借助于换行标签。
     ```html
     <br>
     ```
    - 水平线标签，在页面中插入一条水平分割线
     ```html
     <hr>
     ```
    - 字符实体：
      
    
    ```
     使用 &lt; 在页面中呈现 "<"
     使用 &gt; 在页面中呈现 ">"
     使用 &nbsp; 在页面中呈现一个空格
     使用 &copy; 在页面中呈现版权符号"©"
     使用 &yen; 在页面中呈现人民币符号"￥"
    ```
  - 容器标签
    常用于页面结构划分，结合CSS实现网页布局
    
       ```html
       <div id="top">页面顶部区域</div>
       <div id="main">页面主体区域</div>
       <div id="bottom">页面底部区域</div>
       ```
  - 图片与超链接标签(内联 / 块 元素)
    - 图片标签 <img src="">：用于在网页中插入一张图片。
      1. 属性 src 用于给出图片的URL，必填。
      2. 属性 width/height 用于设置图片尺寸，取像素值，默认按照图片的原始尺寸显示。
      3. 属性 title 用于设置图片标题，鼠标悬停在图片上时显示
      4. 属性 alt 用于设置图片加载失败后的提示文本

      语法：
    ```html
    <img src="" width="" height="" title="" alt="">
    ```
    - 超链接标签：用户可以点击超链接实现跳转至其他页面
      1. 属性 href 用于设置目标文件的URL，必填。
      2. 属性 target用于设置目标文件的打开方式，默认在当前窗口打开。可以设置新建窗口打开目标文本(取"_blank")
      3. 属性href也可以指向某个id号属性的元素
    ```html
    <a href="http://www.taobao.com" target="_self">淘宝</a>
    <a href="http://www.baidu.com" target="_blank">百度</a>
    ```
## 3. 常用结构标签
  - 列表标签 
    - 无序列表
    默认用实心圆点标识列表项
     ```html
    <ul>
    	<li>list item 列表项</li> 
    	<li>list item 列表项</li>
    	<li>list item 列表项</li>
    </ul>
     ```
    - 有序列表
      默认使使用阿拉伯数字标识每条数据，可以使用start属性设置起始的值，默认为1
     ```html
     <ol>
      	<li>list item 列表项</li> 
      	<li>list item 列表项</li>
      	<li>list item 列表项</li>
      </ol>
     ```
    - 列表嵌套
    	在已有列表中嵌套添加另一个列表，常见于下拉菜单
     ```html
    <ol>
    	<li>
    		西游记
    		<ul>
    			<li>孙悟空</li>
    			<li>孙悟空</li>
    			<li>孙悟空</li>
    		</ul>
    	</li>
    </ol>
     ```

  - 表格标签
    - 表格由行和单元格组成，常用于直接的数据展示或辅助排版，基本结构如下：
    ```html
    <!-- 创建表格标签 -->
    <table>
    	 <!-- 创建行标签 -->
    	<tr>
    		<!-- 行中创建单元格以显示数据 -->
    		<td>姓名</td>
    		<td>年龄</td>
    		<td>班级</td>
    	</tr>
    	<tr>
    		<td>张三</td>
    		<td>20</td>
    		<td>一(1)班</td>
    	</tr>
    </table>
    ```
    - 单元格合并：用于调整表格结构，分为跨行合并和跨列合并，合并之后需要删除被合并的单元格，保证表格结构完整。
    
      | 单元格属性 | 作用           | 取值       |
      | ---------- | -------------- | ---------- |
      | colspan    | 跨列合并单元格 | 无单位数值 |
      | rowspan    | 跨行合并单元格 | 无单位数值 |
    
    - 合并示例代码：
    ```html
    <table border="1">
        <tr>
            <th>姓名</th>
            <td>李小明</td>
        </tr>
        <tr>
            <th rowspan="2">电话</th>
            <td>010-1234567</td>
        </tr>
        <tr>
            <td>13912321213</td>
        </tr>
    </table>
    
    <table border="1">
        <tr>
            <th>姓名</th>
            <th colspan="2">电话</th>
        </tr>
        <tr>
            <td>李小明</td>
            <td>010-1234567</td>
            <td>13912321213</td>
        </tr>
    </table>
    ```
  - 表单标签
    表单用于采集用户的信息并提交给服务器，由表单元素和表单控件组成。表单元素form负责提交数据给服务器，表单控件负责收集数据。
    
     - 表单使用<form></form>
    | 属性名   | 取值                                                         |
    | -------- | ------------------------------------------------------------ |
    | action   | 设置数据的提交地址                                           |
    | method   | 设置数据的提交方式，默认为get方式，可以设置为post            |
    | onsubmit | 设置表单数据提交时的触发事件的执行函数（事件绑定中详细介绍） |
    例如：
    ```html
    <form action="" method="" onsubmit="">
    	<!--此处为表单控件-->
    </form>
    ```
     - 表单控件使用（重点）
 表单控件用于采集用户信息，可设置以下标签属性
    
    |  属性名   |   取值  |
    | ---- | ---- |
    | type | 设置控件类型 |
    | name | 设置控件名称，最终与值一并发送给服务器 |
    | value | 设置控件的值 |
    | placeholder | 设置输入框中的提示文本 |
    | maxlength | 设置输入框中可输入的最大字符数 |
    | checked | 设置单选按钮或复选按钮的默认选中 |
    | selected | 设置下拉菜单的默认选中 |


# CSS 基础使用
## 一、CSS介绍
 CSS全称为层叠样式表 ，与HTML相辅相成，实现网页的排版布局与样式美化
## 二、CSS使用方式
### 1. 行内样式/内联样式(单一页面使用)
  借助于style标签属性，为当前的元素添加样式声明
  ```html
 <标签名 style="样式声明">
  ```
  CSS样式声明 : 由CSS属性和值组成
  例：

  ```html
 style="属性:值;属性:值;"
  ```
  常用CSS属性 :
  - 设置文本颜色 color:red;
  - 设置背景颜色 background-color:green;
  - 设置字体大小 font-size:32px;
### 2. 内嵌样式(少量页面中使用)
  借助于style标签，在HTML文档中嵌入CSS样式代码，可以实现CSS样式与HTML标签之间的分离。同时需借助于CSS选择器到HTML 中匹配元素并应用样式
  示例:

  ```
  <style>
     	选择器{
     	 	属性:值;
      		属性:值;
     	}
  </style>
  ```
  选择器 : 通过标签名或者某些属性值到页面中选取相应的元素，为其应用样式
  示例：
  ```css     					
/*标签选择器 : 根据标签名匹配所有的该元素*/  
p{
    color:red;
  }
  ```
### 3. 外链样式表(项目中使用)
  - 创建外部样式表文件 后缀使用.css
  - 在HTML文件中使用<link>标签引入外部样式表
  ```html
 <link rel="stylesheet" href="URL" type="text/css">
  

  ```
  - 样式表文件中借助选择器匹配元素应用样式
##  三、 样式表特征
### 1. 层叠性
多组CSS样式共同作用于一个元素
### 2. 继承性
后代元素可以继承祖先元素中的某些样式
例 : 大部分的文本属性都可以被继承

### 3. 样式表的优先级
优先级用来解决样式冲突问题。同一个元素的同一个样式(例如文本色)，在不同地方多次进行设置，最终选用哪一种样式？此时哪一种样式表的优先级高选用哪一种。
  - 离元素最近的样式优先级最高（就近原则）
  - 文档内嵌与外链样式表，优先级一致，看代码书写顺序，后来者居上
  - 浏览器默认样式和继承样式优先级较低
## 四、CSS 选择器
### 1. 作用
匹配文档中的某些元素为其应用样式
### 2. 分类 :
#### 1. 标签选择器
根据标签名匹配文档中所有该元素
语法 :
```css
标签名{
  属性:值;
}
特点:效率慢
    公用性强
```
#### 2. id选择器
根据元素的 id 属性值匹配文档中唯一的元素，id具有唯一性，不能重复使用
语法 :
```css
  #id属性值{
  
  }
  <p id = "p1...p2.....etc"></p>
  <div>id = "div1...div2.....etc"</div>
```
注意 :
  id属性值自定义,可以由数字，字母，下划线，- 组成，不能以数字开头;
  尽量见名知意，多个单词组成时，可以使用连接符，下划线，小驼峰表示
#### 3. class选择器/类选择器
根据元素的class属性值匹配相应的元素,class属性值可以重复使用,实现样式的复用
语法 :
```css
.class属性值 {
 	
}
```
特殊用法 :
 1. 类选择器与其他选择器结合使用
      注意标签与类选择器结合时,标签在前,类选择器在后
        	例 : a.c1{ }
 2. class属性值可以写多个,共同应用类选择器的样式
    	例 : 
        	.c1{  }
        	.c2{  }						
  	<p class="c1 c2"></p>
#### 4. 群组选择器
为一组元素统一设置样式
语法 :
```css
selector1,selector2,selector3{	
}
```
#### 5. 后代选择器
匹配满足选择器的所有后代元素(包含直接子元素和间接子元素)
语法 :
```css
selector1 selector2{
}
```
匹配selector1中所有满足selector2的后代元素
#### 6. 子代选择器
匹配满足选择器的所有直接子元素
语法 :
```css
selector1>selector2{
}
```
#### 7. 伪类选择器
为元素的不同状态分别设置样式,必须与基础选择器结合使用
分类 :
```
:link 	 超链接访问前的状态
:visited 超链接访问后的状态
:hover	 鼠标滑过时的状态
:active  鼠标点按不抬起时的状态(激活)
:focus	 焦点状态(文本框被编辑时就称为获取焦点)
```
使用 :
```css
a:link{
}
a:visited{
}
.c1:hover{ }
```
注意 :
  1. 超链接如果需要为四种状态分别设置样式,必须按照以下顺序书写
  ```css
  :link
  :visited
  :hover
  :active
  ```
  2. 超链接常用设置 :
  ```css
  a{
  	/*统一设置超链接默认样式(不分状态)*/
  }
  a:hover{
  	/*鼠标滑过时改样式*/
  }
  ```
### 3. 选择器的优先级
使用选择器为元素设置样式，发生样式冲突时，主要看选择器的权重，权重越大，优先级越高

| 选择器       | 权重 |
| ------------ | ---- |
| 标签选择器   | 1    |
| (伪)类选择器 | 10   |
| id选择器     | 100  |
| 行内样式     | 1000 |

复杂选择器(后代,子代,伪类)最终的权重为各个选择器权重值之和群组选择器权重以每个选择器单独的权重为准，不进行相加计算
例 :
```css
/*群组选择器之间互相独立，不影响优先级*/
body,h1,p{ /*标签选择器权重为 1 */
 color:red;
}
.c1 a{ /*当前组合选择器权重为 10+1  */
 color:green;
}
#d1>.c2{ /*当前组合选择器权重为 100+10 */
 color:blue;
}
```

## 五、标签分类及嵌套
### 1. 块元素
独占一行,不与元素共行;可以手动设置宽高,默认宽度与与父元素保持一致
例 : body div h1~h6 p ul ol li form table(默认尺寸由内容决定)

### 2. 行内元素
可以与其他元素共行显示;不能手动设置宽高,尺寸由内容决定
例 : span label b strong i s u sub sup a

### 3. 行内块元素
可以与其他元素共行显示,又能手动调整宽高
例 : img input button (表单控件)

### 4. 嵌套原则
1. 块元素中可以嵌套任意类型的元素
    p元素除外,段落标签只能嵌套行内元素,不能嵌套块元素
2. 行内元素中最好只嵌套行内或行内块元素

	

# 盒子模型

## 1.边框

### 1. 边框实现
语法：
```css
border:width style color;
```
边框样式为必填项，分为：

| 样式取值 | 含义     |
| -------- | -------- |
| solid    | 实线边框 |
| dotted   | 点线边框 |
| dashed   | 虚线边框 |
| double   | 双线边框 |

### 2. 单边框设置
分别设置某一方向的边框，取值：width style color;

| 属性          | 作用       |
| ------------- | ---------- |
| border-top    | 设置上边框 |
| border-bottom | 设置下边框 |
| border-left   | 设置左边框 |
| border-right  | 设置右边框 |


### 3. 网页三角标制作
1. 元素设置宽高为0
2. 统一设置四个方向透明边框
3. 调整某个方向边框可见色
### 4. 圆角边框
1. 属性：border-radius 指定圆角半径
2. 取值：像素值或百分比
3. 取值规律：
```
一个值 	表示统一设置上右下左
四个值 	表示分别设置上右下左
两个值 	表示分别设置上下 左右
三个值 	表示分别设置上右下，左右保持一致
```
### 5. 轮廓线
1. 属性：outline
1. 取值：width style color
1. 区别：边框实际占位，轮廓不占位
1. 特殊：取none可以取消文本输入框默认轮廓线
### 6. 盒阴影
1. 属性：box-shadow
1. 取值：h-shadow v-shadow blur spread color;
1. 使用：不管是浏览器窗口还是元素自身都可以构建坐标系，统一以左上角为原点，向右向下为X轴和Y轴的正方向
```
h-shadow 	取像素值，阴影的水平偏移距离
v-shadow 	取像素值，阴影的垂直偏移距离
blur 		取像素值，表示阴影的模糊程度，值越大越模糊
spread 		选填，取像素值，阴影的尺寸
color 		设置阴影颜色,默认为黑色
```
### 7. 盒模型概念

1. 在模型中，它规定了元素处理内容、内边距、边框和外边距的方式
2. 最内是内容，包围内容的是内边距，内边距的边缘是边框
3. 边框以外是外边距，外边距默认是透明的

## 3. 内边距

1. 属性：padding
2. 作用：调整元素内容框与边框之间的距离
3. 取值：单位是 px 或百分比，但不允许使用负值
```
20px;					一个值表示统一设置上右下左
20px 30px;				两个值表示分别设置(上下) (左右)
20px 30px 40px;			三个值表示分别设置上右下，左右保持一致
20px 30px 40px 50px;	表示分别设置上右下左
```
4. 单方向内边距,只能取一个值：
```
padding-top
padding-right
padding-bottom
padding-left
```
## 4. 外边距
1. 属性：margin

1. 作用：调整元素与元素之间的距离

1. 特殊：
    1）margin:0; 取消默认外边距
    2）margin:0 auto;左右自动外边距，实现元素在父元素范围内水平居中
    3）margin:-10px;元素位置的微调
    
1. 单方向外边距：只取一个值
   ```html
    margin-top
    margin-right
    margin-bottom
    margin-left
   ```
   
1. 外边距合并：
    		1）垂直相遇
      
        	1. 子元素的margin-top作用于父元素上
               
         2. 元素之间同时设置垂直方向的外边距，最终取较大的值
            包含合并
      
            当一个元素包含在另一个元素中时，它们的上和包含上/或下和包含下外边距也会发生合并
## 5. 元素最终尺寸的计算

1. 盒模型相关的属性会影响元素在文档中的实际占位，进而影响布局

2. 元素设置width/height指定的是内容框的大小
3. 最终尺寸 = width/height+padding+border+margin

## 6. 页面布局

默认布局方式，按照代码书写顺序及标签类型从上到下，从左到右依次显示

### 1. 浮动布局

主要用于设置块元素的水平排列

#### 1）属性

```
float
```

#### 2）取值 

可取 left 或 right，设置元素向左浮动或向右浮动

```css
float:left/right;
```

#### 3）特点

- 元素设置浮动会从原始位置脱流，向左或向右依次停靠在其他元素边缘，在文档中不再占位
- 元素设置浮动，就具有块元素的特征，可以手动调整宽高
- "文字环绕"：浮动元素遮挡正常元素的位置，无法遮挡正常内容的显示，内容围绕在浮动元素周围显示

#### 4）常见问题 

子元素全部设置浮动，导致父元素高度为0，影响父元素背景色和背景图片展示,影响页面布局

#### 5）解决

- 对于内容固定的元素，如果子元素都浮动，可以给父元素固定高度(例:导航栏)
- 在父元素的末尾添加空的块元素。设置 clear:both; 清除浮动
- 为父元素设置 overflow:hidden; 解决高度为0


# 一、布局方式
## 3. 定位布局
结合偏移属性调整元素的显示位置
#### 1）属性
position
#### 2） 取值
可取relative（相对定位）/ absolute（绝对定位）/ fixed（固定定位）
```css
postion:relative/absolute/fixed
```
#### 3）偏移属性
设置定位的元素可以使用偏移属性调整距离参照物的位置
```text
top   	距参照物的顶部
right	距参照物的右侧
bottom	距参照物的底部
left	距参照物的左侧
```
#### 4）分类 
+ relative 相对定位
```text
元素设置相对定位,可参照元素在文档中的原始位置进行偏移,不会脱离文档流
```
+ absolute 绝对定位
```text
1. 绝对定位的元素参照离他最近的已经定位的祖先元素进行偏移,如果没有,则参照窗口进行偏移
2. 绝对定位的元素会脱流,在文档中不占位,可以手动设置宽高
```
使用绝对定位 :
	"父相子绝" : 父元素设置相对定位,子元素绝对定位，参照已定位的父元素偏移.
+ fixed	固定定位
```text
  1. 参照窗口进行定位,不跟随网页滚动而滚动
  2. 脱离文档流
```
#### 5）堆叠次序 
元素发生堆叠时可以使用 z-index 属性调整已定位元素的显示位置，值越大元素越靠上：
+ 属性 : z-index
+ 取值 : 无单位的数值,数值越大,越靠上
+ 堆叠：
 1. 定位元素与文档中正常元素发生堆叠，永远是已定位元素在上
 2. 同为已定位元素发生堆叠，按照 HTML 代码的书写顺序，后来者居上
# 二、背景属性
## 1. 背景颜色
```css
background-color: red;
```
## 2. 背景图片相关
#### 1） 设置背景图片
```css
background-image : url("路径");
```
设置背景图片，指定图片路径，如果路径中出现中文或空格，需要加引号
#### 2） 设置背景图片的重复方式
默认背景图片从元素的左上角显示，如果图片尺寸与元素尺寸不匹配时，会出现以下情况：
1. 如果元素尺寸大于图片尺寸，会自动重复平铺，直至铺满整个元素
2. 如果元素尺寸小于图片尺寸，图片默认从元素左上角开始显示，超出部分不可见
```css
background-repeat:repeat/repeat-x/repeat-y/no-repeat
```
```text
取值 ：
	repeat  默认值，沿水平和垂直方向重复平铺
	repeat-x 沿X轴重复平铺
	repeat-y 沿Y轴重复平铺
	no-repeat 不重复平铺
```
#### 3） 设置背景图片的显示位置
默认显示在元素左上角
```css
background-position:x y;
```
取值方式 ：
```text
1. 像素值
	设置背景图片的在元素坐标系中的起点坐标
2. 方位值
	水平：left/center/right
	垂直：top/center/bottom
	注：如果只设置某一个方向的方位值，另外一个方向默认为center
```
精灵图技术 ：为了减少网络请求，可以将所有的小图标拼接在一张图片上，一次网络请求全部得到；借助于background-position 进行背景图片位置的调整，实现显示不同的图标
#### 4）设置背景图片的尺寸
```css
background-size:width height;
```
取值方式 ：
```text
1. 像素值
	1. 500px 500px; 同时指定宽高
	2. 500px;  指定宽度，高度自适应
2. 百分比
	百分比参照元素的尺寸进行计算
	1. 50% 50%; 根据元素宽高,分别计算图片的宽高
	2. 50%; 根据元素宽度计算图片宽高,图片高度等比例缩放
```

## 3. 背景属性简写
```css
background:color url("") repeat position;
```
注意 ：
1. 如果需要同时设置以上属性值，遵照相应顺序书写
2. background-size 单独设置
#  三、文本属性
## 1. 字体相关
#### 1） 设置字体大小
```css
font-size:20px;
```
#### 2）设置字体粗细程度
```css
font-weight:normal;
```
取值 ：
```text
1. normal（默认值）等价于400
2. bold   (加粗) 等价于700
```
#### 3）设置斜体
```css
font-style:italic;
```
#### 4） 设置字体名称
```css
font-family:Arial,"黑体"; 
```
取值 :
    1. 可以指定多个字体名称作为备选字体，使用逗号隔开
        
   2. 如果字体名称为中文，或者名称中出现了空格，必须使用引号

         例 :

```Css
font-family:Arial;
font-family:"黑体","Microsoft YaHei",Arial;
```

#### 5）字体属性简写
```css
font : style weight size family;
```
注意 :
       1. 如果四个属性值都必须设置，严格按照顺序书
       2. size family 是必填项

## 2. 文本样式
#### 1）文本颜色
```css
color:red;
```
#### 2） 文本装饰线
```css
text-decoration:none;
```
取值 :
    underline		  下划线
    overline		     上划线
    line-through 	 删除线
    none			       取消装饰线

#### 3）文本内容的水平对齐方式
```css
text-align:center;
```
取值 : 
```text
left(默认值)	左对齐
center		  居中对齐
right		  右对齐
```
#### 4）行高
```css
line-height:30px;
```
使用 :
    文本在当前行中永远垂直居中，可以借助行高调整文本在元素中的垂直显示位置
     	line-height = height 设置一行文本在元素中垂直居中
     	line-height > height 文本下移显示
     	line-height < height 文本靠上显示
     特殊 :
     	line-height可以采用无单位的数值，代表当前字体大小的倍数,以此计算行高


# 一、 JavaScript 概述
 ## 1. 什么是JavaScript
#### 	1) JavaScript 介绍
​		简称JS，是一种浏览器解释型语言，嵌套在HTML文件中交给浏览器解释执行。主要用来实现网页的动态效果，用户交互及前后端的数据传输等。
#### 	2) JavaScript 组成
1. 核心语法 - ECMAScript ES5-ES6 规范了JavaScript的基本语法
2. 浏览器对象模型 -BOM
     Browser Object Model，提供了一系列操作浏览器的方法
3. 文档对象模型 -DOM
     Document Object Model ，提供了一系列操作的文档的方法
## 2. 使用方式
1. 元素绑定事件
      + 事件 ：指用户的行为（单击，双击等）或元素的状态（输入框的焦点状态等）
      + 事件处理：元素监听某种事件并在事件发生后自动执行事件处理函数。
      + 常用事件：onclick (单击事件) 
      + 语法 ：将事件名称以标签属性的方式绑定到元素上，自定义事件处理。
      ```html
      <!--实现点击按钮在控制台输出-->
      <button onclick="console.log('Hello World');">点击</button>
      ```
2. 文档内嵌。使用<script type="text/javascript"></script>标签书写 JavaScript 代码
      + 语法 ：
      ```html
      <script type="text/javascript">
        alert("网页警告框");
      </script>
      ```
      + 注意 ：<script></script>标签可以书写在文档的任意位置，书写多次，一旦加载到script标签就会立即执行内部的JavaScript代码，因此不同的位置会影响代码最终的执行效果
3. 外部链接
      + 创建外部的JavaScript文件 XX.JavaScript，在HTML文档中使用<script src=""></script>引入
      ```html
      <script src="index.JavaScript"></script>
      ```
      + 注意 ：<script></script>既可以实现内嵌 JavaScript 代码，也可以实现引入外部的 JavaScript 文件，但是只能二选一。
4. JavaScript 输入语句
      + alert(""); 普通的网页弹框
      + prompt(""); 接收用户输入的弹框，返回用户输入的内容
      + console.log(); 控制台输出，多用于代码调试
      + document.write("<h1>Hello</h1>");实现在动态在网页中写入内容。
         1. 可以识别HTML标签,脚本代码可以在文档任何地方书写，如果是普通写入（不涉及事件），区分代码的书写位置插入
         2. 文档渲染结束后，再次执行此方法，会重写网页内容

# 二、DOM 事件处理

事件：指用户的行为或元素的状态。由指定元素监听相关的事件，并且绑定事件处理函数。
事件处理函数：元素监听事件，并在事件发生时自动执行的操作。

#### 1） 事件函数分类

1. 鼠标事件

```javascript
onclick		//单击
ondblclick	//双击
onmouseover	//鼠标移入
onmouseout	//鼠标移出
onmousemove	//鼠标移动
```

2. 文档或元素加载完毕

```javascript
onload		//元素或文档加载完毕
```

3. 表单控件状态监听

```javascript
onfocus 	//文本框获取焦点
onblur		//文本框失去焦点
oninput		//实时监听输入
onchange	//两次输入内容发生变化时触发,或元素状态改变时触发
onsubmit	//form元素监听,点击提交按钮后触发,通过返回值控制数据是否可以发送给服务器
```

#### 2）事件绑定方式

1. 内联方式
   将事件名称作为标签属性绑定到元素上
   例 :

```javascript
<button onclick="alert()">点击</button>
```

2. 动态绑定
   获取元素节点，动态添加事件
   例 :

```javascript
btn.onclick = function (){

};
```

#### 3）事件函数使用

1. onload
   常用于等待文档加载完毕再进行下一步操作
2. 鼠标事件
3. 表单事件
   onchange： 监听输入框前后内容是否发生变化;也可以监听按钮的选中状态
   onsubmit ：表单元素负责监听,允许返回布尔值,表示数据是否可以发送;返回true,允许发送;返回false,不允许提交

# 三、基础语法

## 1. 语法规范

1. JavaScript是由语句组成,语句由关键字，变量，常量，运算符，方法组成。
2. 分号可以作为语句结束的标志，也可以省略
3. JavaScript严格区分大小写
4. 注释语法
    单行注释使用 //
    多行注释使用 /* */
## 2. JavaScript的变量与常量
#### 1)  变量
1. 作用 : 用于存储程序运行过程中可动态修改的数据
2. 语法 : 使用关键var声明,自定义变量名
    ```javascript
    var a;		//变量声明
    a = 100;	//变量赋值
    var b = 200; //声明并赋值
    var m,n,k;	//同时声明多个变量
    var j = 10,c = 20; //同时声明并赋值多个变量
    注:不必声明变量类型
    ```
3. 命名规范 : 
      + 变量名，常量名，函数名，方法名自定义，可以由数字，字母，下划线，$组成，禁止以数字开头
      + 禁止与关键字冲突(var const function if else for while do break case switch return class)
      + 变量名严格区分大小写
      + 变量名尽量见名知意,多个单词组成采用小驼峰,例如："userName"
4. 使用注意 :
      + 变量如果省略var关键字,并且未赋值,直接访问会报错
      + 变量使用var关键字声明但未赋值,变量初始值为undefined
      + 变量省略var关键字声明,已被赋值,可正常使用.影响变量作用域

```
在js中定义变量的时候，我们习惯了用var，其实省略var也可以用的。

今天总结一下，使用var或省略var 定义变量的区别
1、var  私有变量，只能在当前js使用，或者在当前作用域使用，定义私有变量，不能delete；
2、省略var定义变量，如a = "sss", 定义了一个全局变量对象a，a没有被delete掉前，我们可以直接在浏览器console输入a即可看到结果，在任何一个js都可以调用这个对象，可以选择delete。
 
不建议省略var，省略var的时候要慎重
省略var会带来以下：
1.  语义不清楚。 
2.  团队开发时，容易覆盖掉其它作用域内的变量，引发异常。
3.  给window对象添加不必要成员，也就是给window带来不必要的污染，所以用完最好顺便delete掉，以免影响其他变量
```
#### 2)  常量 
1. 作用 : 存储一经定义就无法修改的数据
2. 语法 : 必须声明的同时赋值
      ```javascript
      const PI = 3.14;
      ```
3. 注意 :
    + 常量一经定义,不能修改,强制修改会报错
    + 命名规范同变量,为了区分变量,常量名采用全大写字母
4. 操作小数位
   toFixed(n); 保留小数点后 n 位
   使用 ：
   ```javascript
    var num = 3.1415926;
    //保留当前变量小数点后两位
    var res = num.toFixed(2); 
   ```
## 3. 数据类型
#### 1) 基本数据类型（简单数据类型）
1. number 数值类型
      + 整数
          1.   十进制表示
            ```javascript
             var a = 100;
            ```
            2. 八进制表示
               以0为前缀
            ```javascript
             var b = 021; //结果为十进制的 17
            ```
               使用 : 整数可以采用不同进制表示,在控制台输出时一律会按照十进制输出
      + 小数
          1. 小数点表示
          ```javascript
           var m = 1.2345;
          ```
          2. 科学计数法
             例 : 1.5e3
              e表示10为底,e后面的数值表示10的次方数
             1.5e3 等价于 1.5 * 10(3)
      
2. string 字符串类型
   字符串 : 由一个或多个字符组成,使用""或''表示，每一位字符都有对应的Unicode编码
   
   ```javascript
   var s = "100";
   var s1 = "张三";
   ```
3. boolean 布尔类型
     只有真和假两个值，布尔值与number值可以互相转换。true 为 1，false 为 0

     ```javascript
     var isSave = true;
     var isChecked = false;
     ```

4. undefined 
     特殊值，变量声明未赋值时显示undefined
     
     ```javascript
     var a;
     console.log(a);//undefined
     ```

5. null 空类型
     定义对象引用时使用null，表示对象为空
    （1）引用数据类型
                 主要指对象，函数等

​         （2）检测数据类型
​                   typeof  变量或表达式
​                   typeof (变量或表达式)

```javascript
var n = "asda";
console.log(typeof n);//string
console.log(typeof(n));//string
```

## 4. 数据类型转换
不同类型的数据参与运算时,需要转换类型
#### 1) 强制类型转换
1. 转换字符串类型
   方法 : toString()
   返回转换后的字符串
 ```javascript
 var a = 100;
 a = a.toString(); //"100"
 var b = true;
 b = b.toString(); //"true"
 ```
2. 转换number类型
    +  Number(param)
        参数为要进行数据类型转换的变量或值，返回转换后的结果:
        	如果转换成功,返回number值
        	如果转换失败,返回NaN,(Not a Number)，只要数据中存在非number字符,一律转换失败，返回 NaN
        isNaN() 判断字符串,含有任一非数字类则返回False
    + parseInt(param)
        参数为要解析的数据
            作用 : 从数据中解析整数值
            过程 :
                1. 如果参数为非字符串类型,会自动转成字符串
                2. 从左向右依次对每一位字符转number,转换失败则停止向后解析,返回结果
    + parseFloat(param)
    			作用 : 提取number值，包含整数和小数部分

#### 2) 隐式类型转换（自动转换）
1. 当字符串与其他数据类型进行"+"运算时，表示字符串的拼接，不再是数学运算
   转换规则 ：将非字符串类型的数据转换成字符串之后进行拼接，最终结果为字符串

2. 其他情况下，一律将操作数转number进行数学运算

## 5. 运算符

#### 1) 赋值运算符 
	= 将右边的值赋给左边变量

#### 2) 算数运算符
	+ - * / %  加 减 乘 除 取余

#### 3) 符合运算符
	+= -= *= /= %=

#### 4) 自增或自减运算符

	++ -- 变量的自增和自减指的是在自身基础上进行 +1或-1 的操作
注意：
+ 自增或自减运算符在单独与变量结合时，放前和放后没有区别
+ 如果自增或自减运算符与其他运算符结合使用，要区分前缀和后缀,做前缀，那就先++/--,再进行赋值或其他运算，如果做后缀，就先结合其他运算符，再进行++ / --
+ a++  结果是3,a=2
+ ++a  结果是3,a=3
#### 5) 关系运算符/比较运算符
	> < 
	>= <=
	==(相等) !=(相等)
	===(全等) !==(不全等)
1. 关系运算符用来判断表达式之间的关系,结果永远是布尔值 true/false
2. 使用
	+ 字符串与字符串之间的比较
	依次比较每位字符的Unicode码，只要某位字符比较出结果，就返回最终结果
	+ 其他情况
	一律将操作数转换为number进行数值比较，如果某一操作数无法转换number，则变成NaN参与比较运算，结果永远是false
3. 相等与全等
	+ 相等 : 不考虑数据类型，只做值的比较(包含自动类型转换)
	+ 全等 : 不会进行数据类型转换，要求数据类型一致并且值相等才判断全等

#### 6) 逻辑运算符 
1. && 逻辑与
    表达式同时成立，最终结果才为true；1则1
2. || 逻辑或
    表达式中只要有一个成立,最终结果即为true; 有1则1
3. ! 逻辑非
    对已有表达式的结果取反
    注意 : 除零值以外，所有值都为真
#### 7) 三目运算符
语法 :
```text
表达式1 ? 表达式2 : 表达式3;
```
过程 :
	判断表达式1是否成立,返回布尔值
	如果表达式1成立,执行表达式2;
	如果表达式1不成立,执行表达式3;

#JS逻辑控制
# 一、流程控制
## 1. 作用
控制代码的执行顺序
## 2. 分类
#### 1） 顺序结构
从上到下依次执行代码语句
#### 2） 分支/选择结构
##### 1. if语句
+ 简单if结构
  ``` text
  if(条件表达式){
  	表达式成立时执行的代码段
  }
  ```
  注意 : 除零值以外,其他值都为真，以下条件为假值false
  ```javascript
  if(0){}
  if(0.0){}
  if(""){} //空字符串
  if(undefined){}
  if(NaN){}
  if(null){}
  ```
  特殊写法 :
  	{ }可以省略,一旦省略，if语句只控制其后的第一行代码
+ if - else结构
	```text
	if(条件表达式){
  	//条件成立时执行
  }else{
  	//条件不成立时选择执行
  }
  ```
+ 多重分支结构
    ```javascript
      if(条件1){
   	//条件1成立时执行
      }else if(条件2){
   	//条件2成立时执行
      }else if(条件3){
   	//条件3成立时执行
      }...else{
   	//条件不成立时执行
      }
    ```

##### 2. switch语句
+ 语法 :
```javascript
switch(value){
	 case 值1 :
	 //value与值1匹配全等时,执行的代码段
	 break; //结束匹配
	 case 值2 :
	 //value与值2匹配全等时,执行的代码段
	 break;
	 case 值3 :
     //value与值3匹配全等时,执行的代码段
	 break;
	 default:
 	 //所有case匹配失败后默认执行的语句
 	 break;
}
```
+ 使用 :
```text
1. switch语句用于值的匹配,case用于列出所有可能的值;只有switch()表达式的值与case的值匹配全等时,才会执行case对应的代码段
2. break用于结束匹配,不再向后执行;可以省略,break一旦省略,会从当前匹配到的case开始,向后执行所有的代码语句,直至结束或碰到break跳出
3. default用来表示所有case都匹配失败的情况,一般写在末尾,做默认操作
4. 多个case共用代码段
  		case 值1:
  		case 值2:
  		case 值3:
  		//以上任意一个值匹配全等都会执行的代码段
```

##### 3. 循环结构
+ 作用
根据条件,重复执行某段代码
+ 分类
1. while循环
```text
定义循环变量;
  while(循环条件){
   条件满足时执行的代码段
   更新循环变量;
  }
```
2. do-while循环
```text
do{
	循环体;
	更新循环变量
}while(循环条件);
```
与while循环的区别 :
+ while循环先判断循环条件,条件成立才执行循环体
+ do-while循环不管条件是否成立,先执行一次循环体

3. for循环
```text
for(定义循环变量;循环条件;更新循环变量){
	循环体;
}
```
循环控制 :
	1. break 强制结束循环
	2. continue 结束当次循环,开始下一次循环
循环嵌套 :
    在循环中嵌套添加其他循环



# 一、函数
## 1） 作用 
  	封装一段待执行的代码
## 2）语法 
```javascript
  //函数声明
  function 函数名(参数列表){
  	函数体
  	return 返回值;
  }
  //函数调用
  函数名(参数列表);
```
##  3）使用 
  	函数名自定义，见名知意，命名规范参照变量的命名规范。普通函数以小写字母开头，用于区分构造函数(构造函数使用大写字母开头，定义类)
##  4）匿名函数
匿名函数：省略函数名的函数。语法为：
+ 匿名函数自执行
```javascript
 (function (形参){
  
 })(实参);
```
+ 定义变量接收匿名函数
```javascript
 var fn = function (){};
 fn(); //函数调用
```

## 5）作用域
JavaScript中作用域分为全局作用域和函数作用域，以函数的{ }作为划分作用域的依据
1. 全局变量和全局函数
    + 只要在函数外部使用var关键字定义的变量,或函数都是全局变量和全局函数,在任何地方都可以访问
    + 所有省略var关键字定义的变量,一律是全局变量
2. 局部变量/局部函数
	+ 在函数内部使用var关键字定义的变量为局部变量,函数内部定义的函数也为局部函数,只能在当前作用域中使用,外界无法访问
3. 作用域链
    	局部作用域中访问变量或函数,首先从当前作用域中查找,当前作用域中没有的话,向上级作用域中查找,直至全局作用域
# 二、 内置对象
查找、分割、匹配
  ## 1） 对象
  对象是由属性和方法组成的,使用点语法访问
  ## 2） Array 数组
  #### 1. 创建 
  #### 2. 特点 
+ 数组用于存储若干数据,自动为每位数据分配下标,从0开始
+ 数组中的元素不限数据类型,长度可以动态调整
+ 动态操作数组元素 ：根据元素下标读取或修改数组元素，arr[index]
#### 3. 属性和方法
1. 属性 : length 表示数组长度,可读可写
2. 方法 :
    + push(data)
    在数组的末尾添加一个或多个元素,多个元素之间使用逗号隔开
    返回添加之后的数组长度

    + pop()
    移除末尾元素
    返回被移除的元素

    + unshift(data)
    在数组的头部添加一个或多个元素
    返回添加之后的数组长度

    + shift()
    移除数组的第一个元素
    返回被移除的元素

    + toString()
    将数组转换成字符串类型
    返回字符串结果

    + join(param)
    将数组转换成字符串,可以指定元素之间的连接符,如果参数省略,默认按照逗号连接
    返回字符串

    + reverse()
    反转数组,倒序重排
    返回重排的数组,注意该方法直接修改原数组的结构

    + sort()
    对数组中元素排序,默认按照Unicode编码升序排列
    返回重排后的数组,直接修改原有数组
    参数 : 可选,自定义排序算法
    	例：
        ```javascript
        //自定义升序
        function sortASC(a,b){
          return a-b;
        }
        ```
       作用：作为参数传递到sort()中,会自动传入两个元素进行比较,如果a-b>0,交换元素的值,自定义升序排列
        ```javascript
        //自定义降序
        function sortDESC(a,b){
        	return b-a;
        }
        //如果返回值>0,交换元素的值,b-a表示降序排列
        ```
#### 4. 二维数组 
数组中的每个元素又是数组
```javascript
 var arr1 = [1,2,3];
 var arr2 = [[1,2],[3,4],[5,6,7]];
 //操作数组元素
 var r1 = arr2[0] //内层loadStu(){
 var num = r1[0]; //值 1loadStu(){
 //简写
 var num2 = arr2[1][0];
```
## 3）String 对象
#### 1. 创建 
```javascript
    var str = "100";
    var str2 = new String("hello");
```
#### 2. 特点 
字符串采用数组结构存储每位字符,自动为字符分配下标,从0开始
#### 3. 属性 
length ：获取字符串长度
#### 4. 方法 
+ 转换字母大小写
    toUpperCase() 转大写字母
    toLowerCase() 转小写字母
    返回转换后的字符串,不影响原始字符串

+ 获取字符或字符编码
    charAt(index)	   获取指定下标的字符
    charCodeAt(index)  获取指定下标的字符编码
    参数为指定的下标,可以省略,默认为0

+ 获取指定字符的下标

    + indexOf(str,fromIndex)
    作用 : 获取指定字符的下标,从前向后查询,找到即返回
    参数 :
    	str 表示要查找的字符串,必填
    	fromIndex 表示起始下标,默认为0
    返回 :
    	返回指定字符的下标,查找失败返回-1

    + lastIndexOf(str,fromIndex)
      作用 : 获取指定字符最后一次出现的下标,从后向前查找,找到即返回
      参数 :
      str 必填,表示要查找的内容
      fromIndex	选填,指定起始下标

+ 截取字符串
    substring(startIndex,endIndex)
    作用 : 根据指定的下标范围截取字符串,startIndex ~ endIndex-1
    参数 :
     startIndex	表示起始下标
     endIndex	表示结束下标,可以省略,省略表示截止末尾

+ substr(startIndex,len)

    作用：根据下标截取指定的字符串

+ 分割字符串
    split(param)
    作用 : 将字符串按照指定的字符进行分割,以数组形式返回分割结果
    参数 : 指定分隔符,必须是字符串中存在的字符,如果字符串中不存在,分割失败,仍然返回数组

+ 模式匹配
    
+ 正则表达式对象 RegExp
    
    RegExp : Regualr Expression
    
    1. 语法 ：
       var reg1 = /微软/ig;
       var reg2 = new RegExp('匹配模式','修饰符');
       正则表达式对象可以接收一个变量。
    
	2. 属性 ：
    
       lastIndex : 可读可写，表示下一次匹配的起始索引
       注意 ：
    
       1. 默认情况下，正则表达式对象不能重复调用方法，
          如果重复调用，结果会出错：
          由于 lastIndex 保存再一次匹配的起始下标，
          重复调用时，不能保证每次都从下标0开始
          验证，可以手动调整 lastIndex 为 0。
       2. 只有正则对象设置全局匹配 g ，该属性才起作用。
    
    3. 方法 ：
    
       test(str) :验证字符串中是否存在满足正则匹配模式的内容，存在则返回true，
    
       不存在返回false参数为要验证的字符串。
    
+ 作用 : 借助正则表达式实现字符串中固定格式内容的查找和替换
    正则表达式 :
     var reg1 = /字符模式/修饰符;
     修饰符 : 
      i :  ignorecase 忽略大小写
      g : global 全局范围
    字符串方法 :
    
    + match(regExp/subStr)
	作用 : 查找字符串中满足正则格式或满足指定字符串的内容
    	返回 : 数组,存放查找结果
    + replace(regExp/subStr,newStr)
      作用 : 根据正则表达式或字符串查找相关内容并进行替换
      返回 : 替换后的字符串,不影响原始字符串。

## 4)  Math 对象

#### 1. 定义

Math对象主要提供一些列数学运算的方法

#### 2. 属性

1. 圆周率 :  Math.PI
2. 自然对数 : Math.E

#### 3. 方法

1. Math.random();   生成0-1之间的随机数
2. Math.ceil(x);	     对x向上取整,忽略小数位,整数位+1
3. Math.floor(x);      对x向下取整,舍弃小数位,保留整数位
4. Math.round(x);    对x四舍五入取整数

## 5）日期对象

#### 1. 创建日期对象

      1. var date2 = new Date("2011/11/11");
      2. var date3 = new Date("2011/11/11 11:11:11");

#### 2. 日期对象方法

1. 读取或设置当前时间的毫秒数：getTime()
2. 获取时间分量
   - getFullYear()
   - getMonth()
   - getDate()


# 一、BOM
## 1. BOM 介绍 
BOM全称为“Browser Object Model”，浏览器对象模型。提供一系列操作浏览器的属性和方法。核心对象为window对象，不需要手动创建，跟随网页运行自动产生，直接使用，在使用时可以省略书写。
## 2.  window对象常用方法
#### 1）网页弹框
```javascript
alert()		//警告框
prompt()	//带输入框的弹框
confirm()	//确认框
```
#### 2）窗口的打开和关闭
```javascript
window.open("URL")	//新建窗口访问指定的URL
window.close()		//关闭当前窗口
```
#### 3）定时器方法
1. 间歇调用(周期性定时器)
   作用：每隔一段时间就执行一次代码
   开启定时器:
```javascript
var timerID = setInterval(function,interval);
/*
参数 :
 function : 需要执行的代码,可以传入函数名;或匿名函数
 interval : 时间间隔,默认以毫秒为单位 1s = 1000ms
返回值 : 返回定时器的ID,用于关闭定时器
*/
```
   关闭定时器 :
```javascript
//关闭指定id对应的定时器
clearInterval(timerID);
```
2. 超时调用(一次性定时器)
   作用：等待多久之后执行一次代码
```javascript
//开启超时调用:
var timerId = setTimeout(function,timeout);
//关闭超时调用:
clearTimeout(timerId);
```
## window 对象常用属性
window的大部分属性又是对象类型
#### 1）history
作用：保存当前窗口所访问过的URL
属性 : 
	length 表示当前窗口访问过的URL数量
方法 :
```Javascript
back() 对应浏览器窗口的后退按钮,访问前一个记录
forward() 对应前进按钮,访问记录中的下一个URL
go(n) 参数为number值,翻阅几条历史记录，正值表示前进,负值表示后退
```
#### 2）location
作用：保存当前窗口的地址栏信息(URL)
属性 :
    href 设置或读取当前窗口的地址栏信息
方法 :
    reload(param) 重载页面(刷新)
    参数为布尔值，默认为false，表示从缓存中加载，设置为true,强制从服务器根目录加载
#### 3）document
提供操作文档HTML 文档的方法，,参见DOM
# 二、DOM节点操作
DOM全称为“Document Object Model”，文档对象模型，提供操作HTML文档的方法。（注：每个html文件在浏览器中都视为一篇文档,操作文档实际就是操作页面元素。）
#### 1）节点对象
JS 会对html文档中的元素，属性，文本内容甚至注释进行封装，称为节点对象，提供相关的属性和方法。
#### 2）常用节点分类
+ 元素节点   ( 操作标签）
+ 属性节点（操作标签属性）
+ 文本节点（操作标签的文本内容）
#### 3）获取元素节点
1. 根据标签名获取元素节点列表
```javascript
var elems = document.getElementsByTagName("");
/*
参数 : 标签名
返回值 : 节点列表,需要从节点列表中获取具体的元素节点对象
*/
```
2. 根据class属性值获取元素节点列表
```JavaScript
var elems = document.getElementsByClassName("");
/*
参数 : 类名(class属性值)
返回值 : 节点列表
*/
```
3. 根据id属性值取元素节点
```javascript
var elem = document.getElementById("");
/*
参数 : id属性值
返回值 : 元素节点
*/
```
4. 根据name属性值取元素列表
```javascript
var elems = document.getElementsByName("");
/*
参数 : name属性值
返回 : 节点列表
*/
```
#### 4）操作元素内容
元素节点对象提供了以下属性来操作元素内容
```text
innerHTML : 读取或设置元素文本内容,可识别标签语法
innerText : 设置元素文本内容,不能识别标签语法
value : 读取或设置表单控件的值
```
#### 5）操作元素属性
1. 通过元素节点对象的方法操作标签属性
```javascript
elem.getAttribute("attrname");//根据指定的属性名返回对应属性值
elem.setAttribute("attrname","value");//为元素添加属性,参数为属性名和属性值
elem.removeAttribute("attrname");//移除指定属性
```
2. 标签属性都是元素节点对象的属性,可以使用点语法访问，例如：
```javascript
h1.id = "d1"; 		 //set 方法
console.log(h1.id);  //get 方法
h1.id = null;		//remove 方法
```
注意 :
+ 属性值以字符串表示
+ class属性需要更名为className,避免与关键字冲突,例如：
   h1.className = "c1 c2 c3";

#### 6）操作元素样式
1. 为元素添加id，class属性，对应选择器样式
2. 操作元素的行内样式,访问元素节点的style属性，获取样式对象；样式对象中包含CSS属性，使用点语法操作。
```javascript
p.style.color = "white";
p.style.width = "300px";
p.style.fontSize = "20px";
```
注意 :
+ 属性值以字符串形式给出,单位不能省略
+ 如果css属性名包含连接符,使用JS访问时,一律去掉连接符,改为驼峰. font-size -> fontSize  或者xx.style = "font-size : xxx"



# 一、jQuery简介
js 是动态的,难写
js 兼容性,有的浏览器没有BOM模型
jQ 写起来更快
## 1. 介绍 
jQuery是JS的工具库，对原生JS中的DOM操作、事件处理、包括数据处理和Ajax技术等进行封装,提供更完善,更便捷的方法。
## 2. 使用 
#### 1）引入
先引入jquery文件，才能使用jquery语法
#### 2）工厂函数 - $()
"$()"函数用于获取元素节点，创建元素节点或将原生JS对象转换为jquery对象,返回 jQuery 对象。jQuery 对象实际是一个类数组对象，包含了一系列 jQuery 操作的方法。
例 :
```javascript
 //$()获取元素节点,需传入字符串的选择器
 $("h1")
 $("#d1")
 $(".c1")
 $("body,h1,p")
```
#### 3）原生JS对象与jQuery对象
原生JS对象与jQuery对象的属性和方法不能混用。可以根据需要，互相转换 :
1. 原生JS转换jQuery对象
  $(原生对象)，返回 jQuery 对象
2. jQuery对象转换原生JS对象
    + 方法一 : 根据下标取元素,取出即为原生对象
      var div = $("div")[0];
    + 方法二 : 使用jQuery的get(index)取原生对象
      var div2 = $("div").get(0);
#### 4）jQuery获取元素
jQuery通过选择器获取元素，$("选择器")
选择器分类 :
1. 基础选择器
```text
标签选择器：$("div")
ID 选择器：$("#d1")
类选择器：$(".c1")
群组选择器：$("body,p,h1")
```
2. 层级选择器
```text
后代选择器： $("div .c1")
子代选择器： $("div>span")
相邻兄弟选择器： $("h1+p")  匹配选择器1后的第一个兄弟元素,同时要求兄弟元素满足选择器2
通用兄弟选择器： $("h1~h2") 匹配选择器1后所有满足选择器2的兄弟元素
```
3. 过滤选择器
   需要结合其他选择器使用。
```text
:first
  匹配第一个元素 例:$("p:first")
:last
  匹配最后一个元素 例:$("p:last")
:odd
  匹配奇数下标对应的元素
:even
  匹配偶数下标对应的元素
:eq(index)
  匹配指定下标的元素
:lt(index)
  匹配下标小于index的元素
:gt(index)
  匹配下标大于index的元素
:not(选择器)
  否定筛选,除()中选择器外,其他元素
```
4. 属性选择器
   属性选择器以[ ]为标志.
```text
1. [attrName]
  匹配包含指定属性的元素
2. [attrName=value]/[attrName="value"]
  匹配属性名=属性值的元素
3. [attrName^=value]
  匹配属性值以指定字符开头的元素
4. [attrName$=value]
  匹配属性值以指定字符结尾的元素
5. [attrName*=value]
  匹配属性值包含指定字符的元素
```
5. 子元素过滤选择器
```text
:first-child
   匹配第一个子元素
:last-child
   匹配最后一个子元素
:nth-child(n)
   匹配第n个子元素(n从1开始计数)
```
#### 5）操作元素内容
```javascript
html() //设置或读取标签内容,等价于原生innerHTML,可识别标签语法
text() //设置或读取标签内容,等价于innerText,不能识别标签
val()  //设置或读取表单元素的值,等价于原生value属性
```
#### 6）操作标签属性
1. attr("attrName","value")
    设置或读取标签属性
2. prop("attrName","value")
    设置或读取标签属性
    注意 :在设置或读取元素属性时,attr()和prop()基本没有区别;但是在读取或设置表单元素(按钮)的选中状态时,必须用prop()方法,attr()不会监听按钮选中状态的改变,只看标签属性checked是否书写
3. removeAttr("attrName")
    移除指定属性
#### 7）操作标签样式
1. 为元素添加id/class属性,对应选择器样式
2. 针对类选择器,提供操作class属性值的方法
```javascript
addClass("className")	//添加指定的类名
removeClass("className")//移除指定的类型,如果参数省略,表示清空class属性值
toggleClass("className")//结合用户行为,实现动态切换类名.如果当前元素存在指定类名,则移除;不存在则添加
```
3. 操作行内样式
```javascript
css("属性名","属性值")  //设置行内样式
css(JSON对象)			 //设置一组CSS样式
/*
JSON对象:常用数据传输格式
语法 :
   {
    "width":"200px",
    "height":"200px",
    "color":"red"
   }
 */
```
#### 8）根据层级结构获取元素
1. parent()
   返回父元素
2. parents('selector')
    返回满足选择器的祖先元素
3. children()/children("selector")
  返回所有直接子元素/返回满足选择器的直接子元素
4. find("selector")
   返回所有的后代元素(包含直接与间接)
5. next()/next("selector")
   返回下一个兄弟元素/返回下一个兄弟元素,必须满足选择器
6. prev()/prev("selector")
   返回前一个兄弟元素/返回前一个兄弟元素,要求满足选择器
7. siblings()/siblings("selector")
   返回所有的兄弟元素/满足选择器的所有兄弟元素
#### 9）元素的创建,添加,删除
1. 创建 
   使用$("标签语法")，返回创建好的元素
```javascript
var div = $("<div></div>");	//创建元素
div.html("动态创建").attr("id","d1").css("color","red"); //链式调用，设置内容和属性
var h1 = $("<h1 id='d1'>一级标题</h1>");	//创建的同时设置内容，属性和样式
```
2. 添加至页面 
   1）作为子元素添加
```javascript
$obj.append(newObj);	//在$obj的末尾添加子元素newObj
$obj.prepend(newObj);	//作为第一个子元素添加至$obj中
```
2）作为兄弟元素添加
```javascript
$obj.after(newObj);		//在$obj的后面添加兄弟元素
$obj.before(newObj);	//在$obj的前面添加兄弟元素
```
3）移除元素 
```javascript
$obj.remove();	//移除$obj
```
#### 10）jQuery事件处理
1. 文档加载完毕
   原生JS 方法：window.onload
   jQuery:
```javascript
//语法一 
$(document).ready(function (){
  //文档加载完毕后执行
})
//语法二 
$().ready(function (){
  //文档加载完毕后执行
})
//语法三 
$(function(){
  //文档加载完毕后执行
})
```
区别：
原生onload事件不能重复书写，会产生覆盖问题；jquery中对事件做了优化,可以重复书写ready方法,依次执行
2. 事件绑定方式
   事件名称省略 on 前缀
```javascript
  //on("事件名称"，function)
  $("div").on("click",function(){});
  //bind("事件名称",function)
  $("div").bind("click",function(){});
  //事件名作为方法名
  $("div").click(function(){});  
```
3. this表示事件的触发对象，在jquery中可以使用，注意转换类型。this为原生对象只能使用原生的属性和方法，可以使用$(this)转换为jquery对象，使用jquery方法。
                                                      
