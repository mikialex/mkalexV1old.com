from rest_framework import serializers
from .models import Cheet_sheet_project,Cheet_sheet_item
from .models import Article,Recommended_article,Category

# class Cheet_sheet_project_Serializer(serializers.ModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ('name', 'url_name')


# Serializers define the API representation.
class ArticleListSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('url_name', 'title')

class ArticleDetailSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Article
        fields = ('url_name', 'title','sub_title','content')
