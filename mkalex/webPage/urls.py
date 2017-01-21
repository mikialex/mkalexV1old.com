from django.conf.urls import url

from . import views

app_name="webPage"#namespacing url names   used in tempalte url()
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^blog$', views.blog, name='blog'),
    url(r'^portfolio$', views.portfolio, name='portfolio'),
    url(r'^archive$', views.archive, name='archive'),
    url(r'^colleciton$', views.collection, name='collection'),
    url(r'^about$', views.about, name='about'),
]
