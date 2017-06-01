#coding=utf-8
from django.db import models

# Create your models here.

class Tag(models.Model):
    name=models.CharField(max_length=100,unique=True)#标签名

    def __unicode__(self):
        return self.name

class Category(models.Model):
    name=models.CharField(max_length=100,unique=True)#分类名
    def __unicode__(self):
        return self.name


class Article(models.Model):
    # url_name=models.CharField(max_length=100,unique=True)
    url_name=models.CharField(max_length=100,unique=True)

    title =models.CharField(max_length=100)  #题目
    sub_title =models.CharField(max_length=100,blank=True)  #副标题
    # category =models.CharField(max_length=20,blank=True) #分类
    category=models.ForeignKey(Category,null=True)
    tags=models.ManyToManyField(Tag,blank=True)

    publish_time=models.DateTimeField() #发布日期
    revise_time=models.DateTimeField() #发布日期

    content_type=models.CharField(max_length=20) #文档类型
    content=models.TextField(blank=True)#文档内容

    page_view=models.IntegerField(default=0)#访客计数
    has_cover=models.BooleanField(default=False)#是否有封面，封面文件应当位于blog对应文件名下cover.png

    def __unicode__(self):
        return self.title

    class Meta:#时间下降排序
        ordering=['-publish_time']


class Portfolio(models.Model):
    # url_name=models.CharField(max_length=100,unique=True)
    url_name=models.CharField(max_length=100,unique=True)

    name =models.CharField(max_length=100)  #题目
    describe =models.CharField(max_length=100,blank=True)  #副标题

    publish_time=models.DateTimeField() #发布日期

    content_type=models.CharField(max_length=20) #文档类型
    content=models.TextField(blank=True)#文档内容

    page_view=models.IntegerField(default=0)#访客计数
    has_cover=models.BooleanField(default=True)#是否有封面，封面文件应当位于blog对应文件名下cover.png

    def __unicode__(self):
        return self.name

    class Meta:#时间下降排序
        ordering=['-publish_time']




# class Article_Tag(models.Model):
#     article=models.ForeignKey(Person, on_delete=models.CASCADE)
#     tag=models.ForeignKey(Tag,on_delete=models.CASCADE)
#


class Recommended_article(models.Model):#推荐文章列表 one to one 仅作为演示 不推荐
    article=models.OneToOneField(
    Article,
    on_delete=models.CASCADE,
    related_name='is_recommended',
    null=True,
    )

    def __unicode__(self):
        return self.article.title




##########################cheet-sheet project

class Cheet_sheet_project(models.Model):#cheet-sheet项目表
    name=models.CharField(max_length=100,unique=True)#项目名
    url_name=models.CharField(max_length=100,unique=True)#项目静态资源url
    def __unicode__(self):
        return self.name

class Cheet_sheet_item(models.Model):#cheet-sheet 条目
    content=models.TextField(blank=True)#文档内容
    name=models.CharField(max_length=100,unique=True)#条目名
    url_name=models.CharField(max_length=100,unique=True)#条目静态资源url
    project=models.ForeignKey(Cheet_sheet_project)
    def __unicode__(self):
        return self.name
