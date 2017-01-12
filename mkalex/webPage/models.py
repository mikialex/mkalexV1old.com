from django.db import models

# Create your models here.

class Article(models.Model):
    title =models.CharField(max_length=100)  #题目
    category =models.CharField(max_length=20,blank=True) #标签

    publish_time=models.DateTimeField(auto_now_add=True) #发布日期
    revise_time=models.DateTimeField(auto_now_add=True) #发布日期

    content_type=models.CharField(max_length=20) #文档类型
    content=models.TextField(blank=True)

    def __str__(self):
        return self.title

    class Meta:#时间下降排序
        ordering=['-publish_time']
