from django.conf.urls import url,include
from .views_api import ArticleViewSet ,ArticleListViewSet

app_name="webPageApi"#namespacing url names   used in tempalte url()
urlpatterns = [
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url('^article/', ArticleViewSet.as_view()),
    url('^articleList/', ArticleListViewSet.as_view()),
]
