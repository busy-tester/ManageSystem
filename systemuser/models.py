from django.db import models


# Create your models here.

class BaseTable(models.Model):
    """公共字段列，用于其他表继承这两个字段"""

    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('更新时间', auto_now=True)

    class Meta:
        abstract = True
        verbose_name = "公共字段表"
        db_table = "BaseTable"


class Account(BaseTable):
    """用户注册信息表"""

    username = models.CharField('用户名', max_length=20, unique=True, null=False)
    password = models.CharField('登录密码', max_length=20, null=False)
    nick_name = models.CharField('昵称', max_length=10, null=True)
    email = models.EmailField('用户邮箱', unique=True, null=False)

    class Meta:
        verbose_name = "用户信息"
        db_table = "Account"
