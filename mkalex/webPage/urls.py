from django.conf.urls import url

from . import views

app_name="webPage"#namespacing url names   used in tempalte url()
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog$', views.blog, name='blog'),
    url(r'^blog/year/(?P<year>[0-9]{4})/$', views.blog_year_archive, name='blog_year_archive'),
    url(r'^blog/category/(?P<category_id>[0-9]+)/$', views.blog_category_archive, name='blog_category_archive'),
    url(r'^blog/detail/(?P<name>[^/]+)/$', views.blog_detail, name='blog_detail'),
    url(r'^portfolio$', views.portfolio, name='portfolio'),
    url(r'^archive$', views.archive, name='archive'),
    url(r'^colleciton$', views.collection, name='collection'),
    url(r'^cheetSheet$', views.cheetSheet, name='cheetSheet'),
    url(r'^about$', views.about, name='about'),
]
