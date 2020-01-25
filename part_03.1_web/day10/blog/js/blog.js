// 针对某一个页面定义一个对象
// 使用对象空间的方式添加属性和方法
// 在onload事件中执行方法和调用属性
// 针对log页定义一个对象
var log = {
    startdt: "2019-08-05",
    enddt: "2019-09-05",
    updatedt: "2019-08-05",
    anchor: "alicinya",
}
// log.submit,中间层,专门提供功能
log.submit = {
    autohide: function (obj) {
        setTimeout(
            function () {
                obj.hide()
            }, 2000
        )
    }
}


// 绑定按钮的单机事件,表单提交时触发
function checkvalue() {
    // 获取元素对象,并保存在变量中
    var $form = $("#form01");
    var $username = $("#username");
    var $password = $("#password");
    var $err1 = $("#err1");
    var $err2 = $("#err2");
    var $btn = $(".btn>input");
    // 用户名和密码都不为空时,返回true
    if ($username.val() != "" && $password.val() != "") {
        console.log("111")
        return true
    }
    else {
        // 用户名为空的情况
        if ($username.val() == "") {
            $err1.show();
            log.submit.autohide($err1)
            return false;
        } else {
            // 密码为空的情况
            log.submit.autohide($err2)
            $err2.show();
            return false
        }
    }
}

//-----------------------------动态页面---------------------------------------------
// 增加文章列表
var listBlog={
    template:function(title,imgAddr,content,client){
        var html ="";
        html +='<div class="item">';
        html +='<div class="titile">';
        html +='<h3>'+title+'</h3>';
        html +='</div>';
        html +='<div class="con">';
        html +='<div class="cleft">';
        html +='<img src="'+imgAddr+'" alt="????">';
        html +='</div>';
        html +='<div class="cright">';
        html +='<p class="ptop">';
        html +=content;
        html +='</p>';
        html +='<p class="pbottom">';
        html +=client;
        html +='</p>';
        html +='</div>';
        html +='</div>';
        html +='</div>';
        return html
    }
}

var arrlistBlog=[
    {
        title:"魔导书Grimoire与爱丽丝",
        imgAddr:"img022.0.png",
        content:"爱丽丝在旧作中使用过一些看起来很强力的魔法,并且在《怪绮谈》EX关使用过魔导书Grimoire。至于实力上,由于她总是不认真对待决斗,所以没有办法看出她有多少实力。",
        client:"alisin 2018-11-24"
    },{
        title:"母猪的产后护理      >>>>>>>>>>张凯快来看啊<<<<<<<<<<",
        imgAddr:"img1122.jpg",
        content:"第一个专业:母猪产后护理学,比较实用 这个专业目前主要开设在少数的农林类高校中, 比如中国农业大学、南京农业大学等,顾名思义,这个专业就是专门为母猪“接生”处理...",
        client:"benshan_zhao 2009-09-09"
    }
]


//填充内容
for(var i=1; i>=0;i=i-1){
    var html = listBlog.template(arrlistBlog[i].title,arrlistBlog[i].imgAddr,arrlistBlog[i].content,arrlistBlog[i].client)
    $("#lst").append(html)
}


// ------------------------------动态页面demo-----------------------------------------------

var pics={
    template:function(u,n,t){
        var _html = "";
        _html+='<div class="item">';
        _html+='<div class="imgs" style="border:solid 1px red ">';
        _html+='<img src="'+u+'" alt="">';
        _html+='<h2 class="tip">'+t+'</h2>';
        _html+='</div>';
        _html+='</div>';
        return _html
    }
}

//d定义一个包含3个对象内容的图片数组
var arrPics =[
    {
        u:"b.jpg",
        n:"",
        t:"面对疾风吧"
    },{
        u:"b04.jpg",
        n:null,
        t:"jojo,我不做人啦!"
    },{
        u:"toppic01.jpg",
        n:undefined,
        t:"这也在你的计划之中吗,jojo!"
    }]
    //向模板中填充内容
    for(var j=0;j<arrPics.length;j++){
        var _HTML=pics.template(arrPics[j].u,arrPics[j].n,arrPics[j].t)
    //将模板元素追加到页面元素中
    $("#pics").append(_HTML)
    }
