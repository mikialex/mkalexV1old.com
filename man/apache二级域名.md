```
#服务器根目录
ServerRoot "/etc/httpd"

#端口
#Listen 12.34.56.78:80
Listen 80

#域名+端口来标识服务器，没有域名用ip也可以
#ServerName www.example.com:80

#不许访问根目录
<Directory />
    AllowOverride none
    Require all denied
</Directory>

# 文档目录
DocumentRoot "/var/www/html"

# 对 /var/www目录访问限制
<Directory "/var/www">
    AllowOverride None
    # Allow open access:
    Require all granted
</Directory>

# 对/var/www/html目录访问限制
<Directory "/var/www/html">
　　 Options Indexes FollowSymLinks
　　 AllowOverride None
 　　Require all granted
</Directory>

# 默认编码
AddDefaultCharset UTF-8

#EnableMMAP off
EnableSendfile on

# include进来其它配置文件

IncludeOptional conf.d/*.conf

```

```
<VirtualHost *:80>
  ServerAdmin kkk@kkk.com
  DocumentRoot /home/kkk/www/
  ServerName a.xxx.com
</VirtualHost>
```
