from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.db.models import F
from django.db.models import Q

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
        return render(request, "bookstore/add_book.html", )
    elif request.method == "POST":
        title = request.POST.get("title", "no")
        pub = request.POST.get("pub", "no")
        price = request.POST.get("price", "no")
        market_price = request.POST.get("market_price", "no")
        try:
            abook = models.Book()
            abook.title = title
            abook.price = price
            abook.market_price = market_price
            abook.pub = pub
            abook.save()
        except Exception as err:
            print(err)
            return HttpResponse("图书添加失败,错误信息:  " + str(err))
        return render(request, "bookstore/add_book_res.html", )


def auth_view(request):
    if request.method == "GET":
        # pass 此处引用路径在template文件夹里
        return render(request, "bookstore/add_auth.html", )

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

        return render(request, "bookstore/add_auth_res.html", )


def list_view(request):
    if request.method == "GET":
        books = models.Book.objects.all()
        """print(books)  -->  <QuerySet [<Book: Book object>,
                                         <Book: Book object>, ...
                                        self.title = python3...                            
        """

        """
        >条件<查询价格大于50举例
        books = models.Book.objects.filter(price__gt=50)
                                    查询谓词
                                        __gt: >xx
                                        __contains: %xx%
        """

        # >排除<价格大于40且有清华大学字符的
        # books = models.Book.objects.exclude(pub__contains="清华大学",
        #                                     market_price__gt = 40)

        return render(request, "bookstore/list_book.html", locals())


def authlis_view(request):
    if request.method == "GET":
        # 获取全部数据
        #  authors = models.Author.objects.all()

        authors = models.Author.objects.all()

    return render(request, "bookstore/list_auth.html", locals())


def mod_view(request, id):
    try:
        abook = models.Book.objects.get(id=id)
    except:
        HttpResponse("没有id为%s的数据记录" % id)

    if request.method == "GET":
        return render(request, "bookstore/mod.html", locals())

    elif request.method == "POST":
        market_price = float(request.POST.get("market_price", "0"))

        abook.market_price = market_price
        abook.save()

        return HttpResponseRedirect(id)


def highly_mod_view(request, id):
    try:
        abook = models.Book.objects.get(id=id)
    except:
        HttpResponse("没有id为%s的数据记录" % id)

    if request.method == "GET":
        return render(request, "bookstore/highly_mod.html", locals())

    elif request.method == "POST":
        title = request.POST.get("title", "no")
        pub = request.POST.get("pub", "no")
        price = request.POST.get("price", "no")
        market_price = request.POST.get("market_price", "no")

        abook.title = title
        abook.price = price
        abook.market_price = market_price
        abook.pub = pub
        abook.save()

        # return render(request, "bookstore/highly_mod.html", locals())

        return render(request, "bookstore/mod_book_res.html")
        # return HttpResponse("图书修改成功")


def del_view(request, id):
    try:
        abook = models.Book.objects.get(id=id)
    except Exception as err:
        return HttpResponse("删除失败")
    abook.delete()
    return HttpResponseRedirect('/bookstore/list')


def plist_view(request):
    if request.method == "GET":
        books = models.Book.objects.all()
        return render(request, "bookstore/plist.html", locals())

    elif request.method == "POST":
        p_limit = request.POST.get("p_limit", "no")
        books = models.Book.objects.filter(market_price__lt=p_limit)
        msg = "<h1>市场价小于%s的图书列表:</h1>" % p_limit
        return render(request, "bookstore/plist.html", locals())


def clist_view(request):
    if request.method == "GET":
        books = models.Book.objects.all()
        return render(request, "bookstore/clist.html", locals())

    elif request.method == "POST":
        content = request.POST.get("content", "no")
        books = models.Book.objects.filter(title__contains=content)
        msg = "<h1>内容包含%s的图书列表:</h1>" % content
        return render(request, "bookstore/plist.html", locals())

def bar_list_view(request):
    if request.method == "GET":
        books = models.Book.objects.all()
        return render(request, "bookstore/bar_list.html", locals())

    elif request.method == "POST":
        books = models.Book.objects.filter(market_price__lt=F('price'))
        msg = "<h1>降价的图书列表:</h1>"
        return render(request, "bookstore/bar_list.html", locals())

def xxxlist_view(request):
    if request.method == "GET":
        books = models.Book.objects.all()
        return render(request, "bookstore/xxxlist.html", locals())

    elif request.method == "POST":
        books = models.Book.objects.filter(
            Q(pub="清华大学出版社")
            &Q(price__lt=50))
        msg = "<h1>不是'清华大学出版社' 且 价格小于50元的图书列表:</h1>"
        return render(request, "bookstore/bar_list.html", locals())