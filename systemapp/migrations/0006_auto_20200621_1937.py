# Generated by Django 3.0.7 on 2020-06-21 11:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('systemapp', '0005_auto_20200619_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='supplier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='supplier_goods', to='systemapp.Supplier'),
        ),
    ]
