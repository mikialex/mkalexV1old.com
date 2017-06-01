```shell
在v1下
#激活虚拟环境
source ENV3.6/bin/activate  

cd mkalex

样式开发
sass --watch ./webPage/static/assets/sass/main.scss:./webPage/static/assets/css/main.css
sass --watch --sourcemap=none ./webPage/static/assets/sass/main.scss:./webPage/static/assets/css/main.css

起服务器
python manage.py runserver
```


```shell
静态前端页面开发环境配置 deprecated
    jekyll build --watch

    cd _site
    browser-sync start --server --files "**/*.css,**/*.html"
```
