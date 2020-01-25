# file: mysite1/views.py
import json

from django.http import HttpResponse, JsonResponse


def index_view(request):  # 此处request参数与self类似,用于绑定请求
    html = "<h1>这是首页</h1>"
    return HttpResponse(html)


def page1_view(request):
    html = "<h1>这是编号为1的网页</h1>"
    return HttpResponse(html)


def page2_view(request):
    html = "<h1>这是编号为2的网页</h1>"
    return HttpResponse(html)


def pagen_view(request, n):
    html = "<h1>这是编号为%s的网页</h1>" % n
    return HttpResponse(html)


def math_view(request, n01, operator, n02):
    n01 = int(n01)
    n02 = int(n02)
    if operator == "add":
        result = n01 + n02
    elif operator == "sub":
        result = n01 - n02
    elif operator == "mul":
        result = n01 * n02
    else:
        result = "出错喽!!!!"
    html = "<h1>页面显示结果:%s</h1>" % result
    return HttpResponse(html)


def person_view(request, **kwargs):
    s = str(kwargs)
    return HttpResponse(s)


def birthday_view(request, y, m, d):
    if len(y) == 2:
        y, d = d, y
    html = "<h1>生日为:%s年%s月%s日</h1>" % (y, m, d)
    return HttpResponse(html)


def mypage_view(request):
    """此视图函数用来示意得到GET请求中的查询参数
        .../mypage?a=100&b=200
    """
    if request.method == "GET":
        # a=request.GET["a"]
        a = request.GET.get("a", "没有对应的值")

        html = a
        return HttpResponse(html)
    else:
        return HttpResponse("当前不是get请求")


def msg_view(request):
    msg = request.POST.get('x')
    print(msg)
    return HttpResponse('hello')


def connectdb_view(request):
    msg = {
        'x': 1,
        'y': 2,
        'z': 3
    }
    msg = json.dumps(msg)
    return HttpResponse(msg)
