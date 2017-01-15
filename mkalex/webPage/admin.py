from django.contrib import admin

# Register your models here.
from webPage.models import Article ,Tag

class article_tag(admin.ModelAdmin):#inline
    model=Tag
    filter_horizontal = ('tags',)

admin.site.register(Article,article_tag)
admin.site.register(Tag)
