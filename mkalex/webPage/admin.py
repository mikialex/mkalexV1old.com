from django.contrib import admin

# Register your models here.

from . import models

class article_tag(admin.ModelAdmin):#inline
    model=models.Tag
    filter_horizontal = ('tags',)


admin.site.register(models.Article,article_tag)
admin.site.register(models.Portfolio)
admin.site.register(models.Tag)
admin.site.register(models.Recommended_article)
admin.site.register(models.Category)
admin.site.register(models.Cheet_sheet_project)
admin.site.register(models.Cheet_sheet_item)
