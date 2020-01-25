from django.db import models


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=30, null=False, unique=True,
                             verbose_name="书名")  # varchar(30)
    price = models.DecimalField(decimal_places=2,
                                max_digits=7,
                                verbose_name="价格",
                                default="88888")  # Decimal(7,2)
    market_price = models.DecimalField(decimal_places=2,
                                       max_digits=7, default=99999,
                                       verbose_name="市场价")
    pub = models.CharField(max_length=30, null=False,
                           verbose_name="出版社")
    # pub_date = models.DateField(auto_now_add=True)
    # 此条语句表示
    # - DateField.auto_now: 每次保存对象时，自动设置该字段为当前时间(取值:True/False)。
    # - DateField.auto_now_add: 当对象第一次被创建时自动设置当前时间(取值:True/False)。
    # - DateField.default: 设置当前时间(取值:字符串格式时间如: '2019-6-1')。


class Author(models.Model):
    name = models.CharField(max_length=20, null=False
                            , verbose_name="姓名")
    age = models.IntegerField(null=False, default=1,
                              verbose_name="年龄")
    email = models.EmailField(null=True,
                              )
