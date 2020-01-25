from django.http import HttpResponse
from django.shortcuts import render


def sum_view(request):
    """
    http://127.0.0.1:8000/sum?start=1&stop=101&step=1
    """
    if request.method == "GET":
        try:
            start = request.GET.get("start", "")
            start = int(start)
            stop = request.GET["stop"]
            stop = int(stop)
            step = request.GET.get("step", "2")
            step = int(step)
            mysum = sum(range(start, stop, step))
            html = "和是: %d" % mysum
            return HttpResponse(html)
        except Exception as err:
            return HttpResponse("您的查询请求是无效的")


login_form_html = """
<form action ="/login" method="post">
    用户名:<input name="username" type="text">  
    <input type="submit" value="登录">
</form>
"""


# 此处html  name 属性即为键,input内容即为值,形成多值字典{"username",["alice"]}

# 同样的路由可以接受不同的请求
def login_view(request):
    if request.method == "GET":
        return HttpResponse(login_form_html)
    elif request.method == "POST":
        name = request.POST.get("username", "属性错误")  # post拿的信息{"username",["alice"]}
        html = "姓名" + name
        return HttpResponse(html)


def login2_view(request):
    if request.method == "GET":
        # # 返回生成的 html 给浏览器
        #
        # # 方法1 加载模块
        # from django.template import loader
        # t = loader.get_template("mylogin.html")
        # # 2. 用模板生成html
        # html = t.render({"name": "tarena"})  # 此处将{{name}}的值动态改成了tarana
        # # 将html返回给浏览器
        # return HttpResponse(html)

        # -------------------------------------------
        # 格式2
        from django.shortcuts import render
        return render(request, "mylogin.html", {"name": "alice"})


def mytemp_view(request):
    # 格式 1
    # dic = {
    #     "x":10
    # }
    # return render(request,"mytemp.html",dic)

    # 格式2
    x = 998

    return render(request, "mytemp.html", locals())


def mycal_view(request):
    if request.method == "GET":
        return render(request, "mycal.html")

    elif request.method == "POST":
        x = request.POST.get("x", "属性错误")
        y = request.POST.get("y", "属性错误")
        op = request.POST.get("op", "属性错误")
        if op == "add":
            z = int(x) + int(y)
        elif op == "sub":
            z = int(x) - int(y)
        elif op == "mul":
            z = int(x) * int(y)
        elif op == "div":
            z = int(x) / int(y)
        aa = request.POST.get("", "属性错误")

        return render(request, "mycal.html", locals())


def for_view(request):
    lst = ["北京", "上海", "天津", "成都"]
    s = "<i>Hello World</i>"
    n = 100
    return render(request, "for.html", locals())


def index_view(request):
    return render(request, "base.html")


def sport_view(request):
    return render(request, "sport.html")


def news_view(request):
    return render(request, "news.html")

