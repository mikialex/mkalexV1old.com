http://www.jianshu.com/p/8a2163db7ab5

```
 yum install httpd-devel
 yum install mod_wsgi
```
 在httpd.conf文件中添加以下内容
```
 LoadModule  wsgi_module modules/mod_wsgi.so
```

升级python3

http://www.jianshu.com/p/8bd6e0695d7f
```
yum groupinstall 'Development Tools'
yum install zlib-devel bzip2-devel openssl-devel ncurses-devel sqlite-devel readline-devel tk-devel gdbm-devel db4-devel libpcap-devel xz-devel libcurl-devel

wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tar.xz
tar Jxvf Python-3.5.1.tar.xz
 cd Python-3.5.1
 ./configure --prefix=/usr/local/python3
 make && make install

```
