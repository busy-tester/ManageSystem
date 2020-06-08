# Generated by Django 3.0.7 on 2020-06-07 01:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('member_card', models.CharField(max_length=30, verbose_name='会员卡号')),
                ('member_name', models.CharField(max_length=30, verbose_name='会员姓名')),
                ('member_birthday', models.DateField(null=True, verbose_name='会员生日')),
                ('phone_number', models.IntegerField(null=True, verbose_name='手机号码')),
                ('card_money', models.IntegerField(null=True, verbose_name='开卡金额')),
                ('Available_integral', models.IntegerField(null=True, verbose_name='可用积分')),
                ('pay_type', models.IntegerField(choices=[(1, '现金'), (2, '微信'), (3, '支付宝'), (4, '银行卡')], default=3, verbose_name='支付类型')),
                ('member_address', models.CharField(max_length=100, null=True, verbose_name='会员地址')),
            ],
            options={
                'verbose_name': '会员信息',
                'db_table': 'Member',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('account', models.CharField(max_length=20, verbose_name='账号')),
                ('name', models.CharField(max_length=10, verbose_name='姓名')),
                ('age', models.IntegerField(null=True, verbose_name='年龄')),
                ('iphone', models.IntegerField(null=True, verbose_name='电话')),
                ('salary', models.IntegerField(default=8000, null=True, verbose_name='薪酬')),
                ('entry_time', models.DateField(null=True, verbose_name='入职时间')),
            ],
            options={
                'verbose_name': '员工信息',
                'db_table': 'Staff',
            },
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('supplier_name', models.CharField(max_length=20, verbose_name='供应商名称')),
                ('contacts', models.CharField(max_length=20, verbose_name='联系人')),
                ('contacts_iphone', models.IntegerField(null=True, verbose_name='联系电话')),
                ('remarks', models.CharField(max_length=200, null=True, verbose_name='备注')),
            ],
            options={
                'verbose_name': '供应商信息',
                'db_table': 'Supplier',
            },
        ),
        migrations.CreateModel(
            name='Goods',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(auto_now_add=True, verbose_name='创建时间')),
                ('update_time', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
                ('name', models.CharField(max_length=20, verbose_name='商品名称')),
                ('code', models.CharField(max_length=50, verbose_name='商品编码')),
                ('specs', models.CharField(max_length=30, null=True, verbose_name='商品规格')),
                ('retail_price', models.IntegerField(null=True, verbose_name='零售价')),
                ('buying_price', models.IntegerField(null=True, verbose_name='进货价')),
                ('amount', models.IntegerField(null=True, verbose_name='库存数量')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='systemapp.Supplier')),
            ],
            options={
                'verbose_name': '商品信息',
                'db_table': 'Goods',
            },
        ),
    ]
