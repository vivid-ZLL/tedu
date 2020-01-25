from django.utils.deprecation import MiddlewareMixin
from django.http import HttpResponse
from django.http import Http404


class MyMW(MiddlewareMixin):
    def process_request(self, request):
        print("中间件 process_request方法被调用!")
        if request.path == '/aaaa':
            return HttpResponse("当前路由是:/aaaa")


class VisitLimit(MiddlewareMixin):
    visit_times = {}  # 此字典的键为ip地址,值为此ip地址的访问次数

    def process_request(self, request):
        ip = request.META["REMOTE_ADDR"]  # 得到客户端的IP
        if request.path_info != '/test':
            return None
        times = self.visit_times.get(ip, 0)  # 获取以前的访问次数
        print("ip", ip, "已访问过", times, "次")
        self.visit_times[ip] = times + 1
        if times < 5:
            return None
        return HttpResponse("您已访问过"+str(times)+"次")
