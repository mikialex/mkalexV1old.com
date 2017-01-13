

```shell
静态前端页面开发环境配置
    jekyll build --watch

    cd _site
    browser-sync start --server --files "**/*.css,**/*.html"
```

```shell
环境配置

#安装virtualenv
pip install virtualenv  
#创建虚拟环境
virtualenv -p /usr/local/bin/python3.6 ENV3.6  

#激活虚拟环境
source ENV3.6/bin/activate  
#查看当前环境下的安装包
pip list  


安装django
pip install django
```

```shell
项目创建
django-admin startproject mkalex

创建app
python manage.py startapp webPage

开发服务器 默认端口8000
python manage.py runserver 8000

```

```shell
数据库

#mysqldb不支持python3.x 最佳替代为mysqlclient,但安装失败
#使用pymysql代替。
pip3 install pymysql

#需要在project/project/__init__.py中加入
import pymysql
pymysql.install_as_MySQLdb()

#启动mysql服务器
mysql.server start


python manage.py makemigrations
python manage.py migrate

```

```shell
模版引擎
pip install Jinja2


```

```shell
添加管理员
$ python manage.py createsuperuser


```
