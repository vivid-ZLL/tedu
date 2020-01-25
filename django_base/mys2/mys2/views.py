from django.http import HttpResponse, JsonResponse
from django.shortcuts import render


def sum_view(request):
    if request.method == "GET":
        try:
            s01 = int(request.GET.get('start'))
            e01 = int(request.GET.get('stop'))
            r01 = int(request.GET.get('range'))
            result = sum(range(s01, e01 + 1, r01))
            res = f"""
            <h1>开始值为:{s01}</h1>
            <h1>结束值为:{e01}</h1>
            <h1>步长为:{r01}</h1>
            <h1>结果为:{result}</h1>
            """
            return HttpResponse(res)
        except Exception as e:
            return HttpResponse(e)


def login_view(request):
    if request.method == 'GET':
        html = """
        <form action ="/login/" method="post">
        用户名:<input name="username" type="text">  
        <input type="submit" value="登录">
        </form>
        """
        return HttpResponse(html)

    # 此处html  name 属性即为键,input内容即为值,形成多值字典{"username",["alice"]}

    # 同样的路由可以接受不同的请求
    if request.method == "POST":
        name = request.POST.get('username')

        return HttpResponse("您输入的用户名是:" + name)


def login2_view(request):
    if request.method == "GET":
        return render(request, 'mylogin.html')
    if request.method == "POST":
        username = request.POST.get('username')
        passwd = request.POST.get('passwd')
        return HttpResponse('你输入的用户名是{},密码是{}'.format(username, passwd))


def test2_view(request):
    x = 998
    return render(request, 'mytemp.html', locals())


def connectdb_view(request):
    if request.method == 'POST':
        res = request.POST
        print(res)
        # print(request.META)
        return JsonResponse({'name':'alice'})
