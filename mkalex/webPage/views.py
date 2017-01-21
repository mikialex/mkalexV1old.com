from django.shortcuts import render ,get_object_or_404

# Create your views here.
from django.http import HttpResponse ,Http404
from django.template import loader

from .models import Article,Recommended_article

def index(request):
    template=loader.get_template('webPage/index.jinja')
    art=get_object_or_404(Article,pk=1)
    content ={
        'page_title':'Index',
        'name':art.title
    }
    return HttpResponse(template.render(content))



def blog(request):
    template=loader.get_template('webPage/blog.jinja')
    article_list = Article.objects.all()
    Recommended_article_list=Recommended_article.objects.all()
    content={
        'page_title':'Blog',
        'list':article_list,
        'rec_list':Recommended_article_list,
    }
    return HttpResponse(template.render(content))

#blog home page
def portfolio(request):
    template=loader.get_template('webPage/portfolio.jinja')
    content={
        'page_title':'Portfolio',
    }
    return HttpResponse(template.render(content))


def archive(request):
    template=loader.get_template('webPage/archive.jinja')
    content={
        'page_title':'Archive',
    }
    return HttpResponse(template.render(content))



def collection(request):
    template=loader.get_template('webPage/collection.jinja')
    content={
        'page_title':'Collection',
    }
    return HttpResponse(template.render(content))



def about(request):
    template=loader.get_template('webPage/about.jinja')
    content={
        'page_title':'Meta',
    }
    return HttpResponse(template.render(content))
