## Django+DRF写的会员管理系统

* 使用DRF写的前后端分离的项目，有注册，登录，会员，供应商，商品等的增删改查，可以练习接口自动化。
* ManageSystemWeb为前端页面，使用 Vue+element-ui，搭配使用，效果更佳。

##  本地启动
___安装依赖项___
* pipenv install

***进入虚拟环境***
* pipenv shell

***迁移数据库***
1. 创建数据库，settings 里进行配置数据库
2. python manage.py makemigrations
3. python manage.py migrate

***启动项目***

* python manage.py runserver
