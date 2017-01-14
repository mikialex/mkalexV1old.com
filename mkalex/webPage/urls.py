from django.conf.urls import url

from . import views

app_name="webPage"#namespacing url names   used in tempalte url()
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog$', views.blog, name='blog'),
    url(r'^portfolio$', views.blog, name='portfolio'),
]
