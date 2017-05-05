from django.conf.urls import url,include

from . import views

from .models import Article,Recommended_article,Category
from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response

# Serializers define the API representation.
class ArticleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('url_name', 'title')

# ViewSets define the view behavior.
class ArticleViewSet(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer
    # def list(self, request):
    #     queryset = Article.objects.all()
    #     serializer = ArticleSerializer(queryset, many=True)
    #     return Response(serializer.data)



# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'article', ArticleViewSet,'article')




app_name="webPage"#namespacing url names   used in tempalte url()
urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
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
