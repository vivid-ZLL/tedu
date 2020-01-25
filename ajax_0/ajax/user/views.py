import json

from django.shortcuts import render
from django.http import HttpResponse, JsonResponse

# Create your views here.
from user.models import User


def xhr(request):
    return render(request, 'xhr.html')


def get_xhr_server(request):
    if request.method == "POST":
        return HttpResponse('this is ajax POST request')
    if request.method == "GET":
        return HttpResponse('this is ajax GET request')


def get_xhr(request):
    msg = '请输入用户名'
    return render(request, 'get-xhr.html',locals())


def register(request):
    if request.method == "GET":
        return render(request, 'register.html')
    elif request.method == "POST":
        uname = request.POST.get('uname')
        if not uname:
            return HttpResponse('请输入用户名')
        pwd = request.POST.get('pwd')
        if not pwd:
            return HttpResponse('请输入密码')
        nickname = request.POST.get('nickname')
        if not nickname:
            return HttpResponse('请输入昵称')

        try:
            print("okokokokokok")
            User.objects.create(name=uname, pwd=pwd, nickname=nickname)
        except Exception as e:
            print(e)
            return HttpResponse("注册失败,请稍后重试")

        return HttpResponse('注册成功')


def checkunme(request):
    # 1 获取ajax传过来的用户名
    uname = request.GET.get('uname')
    # 2 校验用户名是否存在
    users = User.objects.filter(uname=uname)
    print(users)

    if users:
        return HttpResponse("1")
    return HttpResponse("OK")


def make_post(request):
    if request.method == "GET":
        return render(request, 'make_post.html')
    elif request.method == "POST":
        # 获取表单数据
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        return HttpResponse("your post is ok!!! %s %s" % (uname, pwd))
    else:
        raise Exception


def get_user(request):
    return render(request, 'get_user.html')


def get_user_server(request):
    users = User.objects.all()
    msg = ''
    for u in users:
        msg += '%s_%s_%s|' % (u.uname, u.pwd, u.nickname)
    last_msg = msg[:-1]
    return HttpResponse(last_msg)


def json_obj(request):
    return render(request, 'json_obj.html')


def json_dumps(request):
    # 1, 生成单个对象的json字符串/序列化  -> obj - str
    # 反序列化  -> str -> obj
    dic = {
        'uname': 'LiLi',
        'uage': '30'
    }

    json_str = json.dumps(dic)

    # 生成多个对象的json字符串

    s = [
        {
            'uname': 'LiLi',
            "uage": 30
        }, {
            'uname': 'Panghu',
            'uage': '30'
        }

    ]
    #  -----------json.dumps 转容器为json字符串-------
    # 参数sort_keys,让输出的json串有序
    # 参数separators,('xx','xx'),第一个参数指的是每一个键值对之间用当前参数分隔;
    #                           第二个参数指的是每一个键值对之间的键和值用当前参数分割
    json_str_arr = json.dumps(s, separators=(',', ':'))

    #  --------django v1 ----------------
    # from django.core import serializers
    # users = User.objects.all()
    # json_str_all = serializers.serialize("json", users)
    #
    # return HttpResponse(json_str_all, content_type='application/json')

    # ----django v2-----------------
    # return JsonResponse({"code": 998, "data":{}})

    l = []
    users = User.objects.all()
    d = {}
    for i in users:
        d['nickname'] = i.nickname
        l.append(d)

    return HttpResponse(json_str_arr)
