from django.shortcuts import render
from django.http import HttpResponse
import json


# Create your views here.
def load_test(request):
    return render(request, 'load_test.html')


def load_test_server(request):
    return render(request, 'load_test_server.html')


def jquery_get(request):
    return render(request, 'jquery_get.html')


def jquery_get_server(request):
    age = request.GET.get('age', '没拿到age')
    uname = request.GET.get('uname', "没拿到uname")
    d = {'uname': uname, 'age': age}

    return HttpResponse(json.dumps(d), content_type='application/json')


def jquery_post(request):
    return render(request, 'jquery_post.html')


def jquery_post_server(request):
    # 此处的code 1201 是约定参数,用来表示传输情况
    if int(request.POST.get('age', 0)) > 100:
        d = {"msg": 'post age is so big', 'code': 1202}
        return HttpResponse(json.dumps(d), content_type='application/json')

    d = {"msg": 'post is ok', 'code': 1201}
    return HttpResponse(json.dumps(d), content_type='application/json')


def jquery_ajax(request):
    return render(request, 'jquery_ajax.html')


def jquery_ajax_server(request):
    import time
    time.sleep(3)
    d = {"name": 'alice', 'age': 18}

    return HttpResponse(json.dumps(d), content_type='application/json')


def jquery_ajax_user(request):
    return render(request, 'jquery_ajax_user.html')


def jquery_ajax_user_server(request):
    d01 = {"name": 'alice', 'age': 18}
    d02 = {"name": 'alicinya', 'age': 20}
    d = [d01, d02]

    return HttpResponse(json.dumps(d), content_type='application/json')


def cross(request):
    return render(request, "cross.html")


def cross_server(request):
    func = request.GET.get('callback')
    # 'print("str")'

    return HttpResponse(func + "('wo kua chu lai le hahaahahaha')")


def cross_server_json(request):
    d = {"name": "alice"}
    func = request.GET.get('callback')

    # json.dumps(d) -----> {"name": "alice"}

    return HttpResponse(func + "(" + json.dumps(d) + ")")
