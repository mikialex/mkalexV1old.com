from django.shortcuts import render ,get_object_or_404
# from django.db.models import Count

# Create your views here.
from django.http import HttpResponse ,Http404
from django.template import loader

from .models import Article,Recommended_article,Category

from markdown2 import Markdown
markdowner = Markdown()
blog_assets_base='/static/image/blog/'
def set_url(markdown_text):
    return markdown_text.replace("{#base#}",blog_assets_base)

def get_right_col():
    right_col_data={
        'num2016':Article.objects.filter(publish_time__year=2016).count(),
        'num2017':Article.objects.filter(publish_time__year=2017).count(),
        'Recommended_article_list':map(lambda x:Article.objects.get(pk=x.article_id),Recommended_article.objects.all())
    }
    return right_col_data










def index(request):
    template=loader.get_template('webPage/index.jinja')
    content ={
        'page_title':'Index',
        'right_col_data':get_right_col(),
    }
    return HttpResponse(template.render(content))




#blog home page
def blog(request):
    template=loader.get_template('webPage/blog.jinja')
    article_list = Article.objects.all()
    category=Category.objects.all()
    content={
        'page_title':'Blog',
        'list':article_list,
        'right_col_data':get_right_col(),
    }
    return HttpResponse(template.render(content))



def blog_detail(request,id):
    template=loader.get_template('webPage/blog_detail.jinja')
    article = Article.objects.get(pk=id);
    # Recommended_article_list=Recommended_article.objects.all()
    content_html=markdowner.convert(set_url(article.content))
    content={
        'page_title':'Blog',
        # 'list':article_list,
        'content':content_html,
        'right_col_data':get_right_col(),
    }
    return HttpResponse(template.render(content))




def blog_year_archive(request,year):
    pass
    # template=loader.get_template('webPage/blog_detail.jinja')
    # article_list = Article.objects.all()
    # # Recommended_article_list=Recommended_article.objects.all()
    # content={
    #     'page_title':'jkjkjkjkjkjkjkjkjkjk',
    #     # 'list':article_list,
    #     # 'rec_list':Recommended_article_list,
    # }
    # return HttpResponse(template.render(content))
    # return HttpResponse(template.render(content))



def portfolio(request):
    template=loader.get_template('webPage/portfolio.jinja')
    content={
        'page_title':'Portfolio',
        'right_col_data':get_right_col(),
    }
    return HttpResponse(template.render(content))


def archive(request):
    template=loader.get_template('webPage/archive.jinja')
    content={
        'page_title':'Archive',
        'right_col_data':get_right_col(),
    }
    return HttpResponse(template.render(content))



def collection(request):
    template=loader.get_template('webPage/collection.jinja')
    content={
        'page_title':'Collection',
        'right_col_data':get_right_col(),
    }
    return HttpResponse(template.render(content))



def about(request):
    template=loader.get_template('webPage/about.jinja')
    content={
        'page_title':'Meta',
        'right_col_data':get_right_col(),
    }
    return HttpResponse(template.render(content))
