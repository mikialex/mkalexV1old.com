from django.db import models

# Create your models here.

class Tag(models.Model):
    name=models.CharField(max_length=100,unique=True)#标签名

    def __str__(self):
        return self.name

class Article(models.Model):
    title =models.CharField(max_length=100)  #题目
    sub_title =models.CharField(max_length=100,blank=True)  #副标题
    category =models.CharField(max_length=20,blank=True) #分类
    tags=models.ManyToManyField(Tag,blank=True)

    publish_time=models.DateTimeField(auto_now_add=True) #发布日期
    revise_time=models.DateTimeField(auto_now_add=True) #发布日期

    content_type=models.CharField(max_length=20) #文档类型
    content=models.TextField(blank=True)#文档内容

    page_view=models.IntegerField(default=0)#访客计数

    def __str__(self):
        return self.title

    class Meta:#时间下降排序
        ordering=['-publish_time']


# class Article_Tag(models.Model):
#     article=models.ForeignKey(Person, on_delete=models.CASCADE)
#     tag=models.ForeignKey(Tag,on_delete=models.CASCADE)
#

class Recommended_article(models.Model):#推荐文章列表
    article=models.OneToOneField(
    Article,
    on_delete=models.CASCADE,
    related_name='is_recommended',
    null=True,
    )

    def __str__(self):
        return self.article.title
