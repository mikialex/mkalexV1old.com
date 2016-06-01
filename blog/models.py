from __future__ import unicode_literals

from django.db import models

#from django.utils.encoding import python_2_unicode_compatible


# Create your models here.


#@python_2_unicode_compatible 
class Article(models.Model):
	article_title = models.CharField(max_length=100)
	content_path=models.FilePathField()
	viewed=models.IntegerField()
	id = models.AutoField(primary_key=True)


