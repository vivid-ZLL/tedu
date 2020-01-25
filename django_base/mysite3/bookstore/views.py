from django.shortcuts import render
from django.http import HttpResponse

from . import models


# Create your views here.
def add_view(request):
    # 添加图书的第一种方法：
    # try:
    #     abook = models.Book.objects.create(
    #         title = "C++",price = 68)
    #     return HttpResponse("添加图书成功")
    # except Exception as err:
    #     return  HttpResponse("添加图书失败")
    #  ----------------分割线-----------------------------

    # 添加图书的第二种方法
    # abook = models.Book(price=98)
    # abook.title = "西游记"
    # abook.save()  # 此处表示真正执行 sql 语句
    #
    # return HttpResponse("添加图书成功")
    # ----------------分割线----------------------

    if request.method == "GET":
        # pass 此处引用路径是对的，但不在template文件夹里
        return render(request,"add_book.html",)
    if request.method == "POST":

        title = request.POST.get("title","no")
        pub = request.POST.get("pub","no")
        price = request.POST.get("price","no")
        market_price = request.POST.get("market_price","no")



        try:
            abook = models.Book()
            abook.title = title
            abook.price = price
            abook.market_price = market_price
            abook.pub = pub
            abook.save()
        except Exception as err:
            print(err)
        return render(request, "add_book_res.html", )

def auth_view(request):
    if request.method == "GET":
        # pass 此处引用路径在template文件夹里
        return render(request,"add_auth.html",)

    if request.method == "POST":

        name = request.POST.get("name", "no")
        age = request.POST.get("age", "no")
        email = request.POST.get("email", "no")

        try:
            auth = models.Author()
            auth.age = age
            auth.email = email
            auth.name = name
            auth.save()
        except Exception as err:
            print(err)

        return render(request, "add_auth_res.html", )