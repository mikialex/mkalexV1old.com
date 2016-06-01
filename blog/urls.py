from django.conf.urls import url

from . import views

#register namespace
app_name='blog'

urlpatterns = [


    url(r'^$', views.main, name='main'),
    url(r'^article/$',views.articleList,name='articleList')
    # url(r'^$', views.index, name='index'),
    # url(r'^times/$', views.current_datetime,name='current_datetime'),
    # url(r'^times/plus/(\d{1,2})/$', views.hours_ahead,name='hou'),
    # # ex: /polls/5/
    # url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # # ex: /polls/5/results/
    # url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # # ex: /polls/5/vote/
    # url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]