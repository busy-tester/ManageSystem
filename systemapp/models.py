from django.db import models
from systemuser.models import BaseTable


# Create your models here.

class Member(BaseTable):
    """会员管理"""

    pay_type = (
        (1, "现金"),
        (2, "微信"),
        (3, "支付宝"),
        (4, "银行卡"),
    )

    member_card = models.CharField("会员卡号", max_length=30, null=False)
    member_name = models.CharField("会员姓名", max_length=30, null=False)
    member_birthday = models.DateField("会员生日", null=False)
    phone_number = models.CharField("手机号码", max_length=100, null=True, blank=True)
    card_money = models.CharField("开卡金额", max_length=100, null=True, blank=True)
    Available_integral = models.CharField("可用积分", max_length=100, null=True, blank=True)
    pay_type = models.IntegerField("支付类型", choices=pay_type, default=3)
    member_address = models.CharField("会员地址", max_length=100, null=True, blank=True)

    class Meta:
        verbose_name = '会员信息'
        db_table = "Member"


class Supplier(BaseTable):
    """供应商管理"""

    supplier_name = models.CharField('供应商名称', max_length=20, null=False)
    contacts = models.CharField('联系人', max_length=20, null=False)
    contacts_iphone = models.IntegerField("联系电话", null=True)
    remarks = models.CharField("备注", max_length=200, null=True)

    class Meta:
        verbose_name = "供应商信息"
        db_table = "Supplier"


class Goods(BaseTable):
    """商品管理"""

    name = models.CharField("商品名称", max_length=20, null=False)
    code = models.CharField("商品编码", max_length=50, null=False)
    specs = models.CharField("商品规格", max_length=30, null=True)
    retail_price = models.IntegerField('零售价', null=True)
    buying_price = models.IntegerField('进货价', null=True)
    amount = models.IntegerField("库存数量", null=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "商品信息"
        db_table = "Goods"


class Staff(BaseTable):
    """员工管理"""
    account = models.CharField("账号", max_length=20, null=False)
    name = models.CharField("姓名", max_length=10, null=False)
    age = models.IntegerField('年龄', null=True)
    iphone = models.IntegerField('电话', null=True)
    salary = models.IntegerField("薪酬", null=True, default=8000)
    entry_time = models.DateField("入职时间", null=True)

    class Meta:
        verbose_name = "员工信息"
        db_table = "Staff"
