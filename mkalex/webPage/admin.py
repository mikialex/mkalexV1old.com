from django.contrib import admin

# Register your models here.
from webPage.models import Article ,Tag,Recommended_article,Category,Cheet_sheet_project,Cheet_sheet_item

class article_tag(admin.ModelAdmin):#inline
    model=Tag
    filter_horizontal = ('tags',)


admin.site.register(Article,article_tag)
admin.site.register(Tag)
admin.site.register(Recommended_article)
admin.site.register(Category)
admin.site.register(Cheet_sheet_project)
admin.site.register(Cheet_sheet_item)
