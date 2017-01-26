# centos7部署mysql

安装mysql
```
yum install mysql
yum install mysql-devel
yum install mariadb-server mariadb


systemctl start mariadb  #启动MariaDB

systemctl stop mariadb  #停止MariaDB

systemctl restart mariadb  #重启MariaDB

systemctl enable mariadb  #设置开机启动

```
<hr>
http://www.cnblogs.com/starof/p/4680083.html

修改/etc/my.cnf 下的mysql配置文件，最后加入
```
default-character-set =utf8
```
<hr>
修改设置mysql root 密码
```
mysqladmin -u root password "newpass"
mysqladmin -u root password oldpass "newpass"
```
<hr>

http://putian.blog.51cto.com/1722818/1287959

添加远程登录权限
```
mysql -u root -p #登录

mysql> select host,user from user; #查看用户的权限情况
mysql> Grant all privileges on *.* to 'root'@'%' identified by 'password' with grant option;
#(%表示是所有的外部机器，如果指定某一台机，就将%改为相应的机器名；‘root’则是指要使用的用户名，里面的password需要自己修改成root的密码)
mysql> flush privileges;  #(运行此句才生效，或者重启MySQL)
```
<hr>
