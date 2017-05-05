from .models import Article,Recommended_article,Category
from .serializer import ArticleListSerializer ,ArticleDetailSerializer

from rest_framework import routers, serializers, viewsets
from rest_framework.response import Response
from rest_framework import generics


# ViewSets define the view behavior.
class ArticleListViewSet(generics.ListAPIView):
    # queryset = Article.objects.all()
    serializer_class = ArticleListSerializer
    http_method_names = ['get']
    def get_queryset(self):
        queryset = Article.objects.all()
        # url_name = self.request.query_params.get('url_name')
        # queryset = queryset.filter(url_name=url_name)
        return queryset

class ArticleViewSet(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer
    lookup_field='url_name'
    http_method_names = ['get']
    def get_object(self):
        queryset = Article.objects.all()
        url_name = self.request.query_params.get('url_name')
        obj = queryset.get(url_name=url_name)
        return obj
