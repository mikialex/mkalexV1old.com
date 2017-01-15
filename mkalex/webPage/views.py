from django.shortcuts import render ,get_object_or_404

# Create your views here.
from django.http import HttpResponse ,Http404
from django.template import loader

from .models import Article,Recommended_article

def index(request):
    template=loader.get_template('webPage/index.jinja')
    art=get_object_or_404(Article,pk=1)
    content ={'name':art.title}
    return HttpResponse(template.render(content))



#block home page
def blog(request):
    template=loader.get_template('webPage/blog.jinja')
    article_list = Article.objects.all()
    Recommended_article_list=Recommended_article.objects.all()
    content={
        'list':article_list,
        'rec_list':Recommended_article_list,
    }
    return HttpResponse(template.render(content))
