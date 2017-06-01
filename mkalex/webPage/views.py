#coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render ,get_object_or_404
# from django.db.models import Count

from django.core.paginator import Paginator ,EmptyPage,PageNotAnInteger

# Create your views here.
from django.http import HttpResponse ,Http404
from django.template import loader

from .models import Article,Recommended_article,Category

from markdown2 import Markdown
markdowner = Markdown()
blog_assets_base='/static/image/blog/'

def set_url(markdown_text,url_name):
    return markdown_text.replace("{#base#}",blog_assets_base+url_name+'/')

def get_right_col():

    category_list=list(Category.objects.all())
    def count_category_num(category):
        return {'name':category.name,
        'num':Article.objects.filter(category_id=category.id).count(),
        'id':category.id}
    categoryAll=map(count_category_num,category_list)

    right_col_data={
        'category':categoryAll,
        'num2016':Article.objects.filter(publish_time__year=2016).count(),
        'num2017':Article.objects.filter(publish_time__year=2017).count(),
        'num_all':Article.objects.all().count(),
        'Recommended_article_list':map(lambda x:Article.objects.get(pk=x.article_id),Recommended_article.objects.all())
    }
    return right_col_data










def index(request):
    template=loader.get_template('webPage/pages/index.jinja')
    content ={
        'page_title':'Index',
        'right_col_data':get_right_col(),
    }
    return HttpResponse(template.render(content))




#blog home page
def blog(request):
    template=loader.get_template('webPage/pages/blog/blog_list.jinja')
    article_list = Article.objects.all()
    page = request.GET.get('page')  # 获取页码
    paginator = Paginator(article_list, 6)  # 实例化一个分页对象
    try:
        article_list = paginator.page(page)  # 获取某页对应的记录
    except PageNotAnInteger:  # 如果页码不是个整数
        article_list = paginator.page(1)  # 取第一页的记录
    except EmptyPage:  # 如果页码太大，没有相应的记录
        article_list = paginator.page(paginator.num_pages)  # 取最后一页的记录
    content={
        'page_title':'Blog',
        'list':article_list,
        'right_col_data':get_right_col(),
    }
    return HttpResponse(template.render(content))



def blog_detail(request,name):
    template=loader.get_template('webPage/pages/blog/blog_detail.jinja')
    article = get_object_or_404(Article,url_name=name)
    pv=article.page_view+1;
    Article.objects.filter(url_name=name).update(page_view=pv)
    content_html=markdowner.convert(set_url(article.content,article.url_name))
    content={
        'page_title':article.title,
        'page_subtitle':article.sub_title,
        'content':content_html,
        'right_col_data':get_right_col(),
    }
    return HttpResponse(template.render(content))




def blog_year_archive(request,year):
    template=loader.get_template('webPage/pages/blog/blog_list_without_pagination.jinja')
    article_list = Article.objects.filter(publish_time__year=year)
    content={
        'page_title':'Blog in '+year,
        'list':article_list,
        'right_col_data':get_right_col(),
    }
    return HttpResponse(template.render(content))
    return HttpResponse(template.render(content))



def blog_category_archive(request,category_id):
    template=loader.get_template('webPage/pages/blog/blog_list_without_pagination.jinja')
    article_list = Article.objects.filter(category_id=category_id)
    category_name=get_object_or_404(Category,id=category_id).name
    content={
        'page_title':u'Blog 的 '+ category_name+ u' 子分类',
        'list':article_list,
        'right_col_data':get_right_col(),
    }
    return HttpResponse(template.render(content))
    return HttpResponse(template.render(content))





def portfolio(request):
    template=loader.get_template('webPage/pages/portfolio/portfolio-page.jinja')
    content={
        'page_title':'Portfolio',
        'right_col_data':get_right_col(),
    }
    return HttpResponse(template.render(content))


def archive(request):
    template=loader.get_template('webPage/spa-index-deploy/index.jinja')
    content={
        # 'page_title':'Archive',
        # 'right_col_data':get_right_col(),
    }
    return HttpResponse(template.render(content))

def cheetSheet(request):
    template=loader.get_template('webPage/spa-index-deploy/index.jinja')
    content={
        # 'page_title':'Archive',
        # 'right_col_data':get_right_col(),
    }
    return HttpResponse(template.render(content))



def collection(request):
    template=loader.get_template('webPage/pages/collection.jinja')
    content={
        'page_title':'Collection',
        'right_col_data':get_right_col(),
    }
    return HttpResponse(template.render(content))



def about(request):
    template=loader.get_template('webPage/pages/about.jinja')
    content={
        'page_title':'Meta',
        'right_col_data':get_right_col(),
    }
    return HttpResponse(template.render(content))


def theone(request):
    template=loader.get_template('webPage/pages/theone.jinja')
    content={
        # 'page_title':'Meta',
        # 'right_col_data':get_right_col(),
    }
    return HttpResponse(template.render(content))


def page_not_found(request):
    template=loader.get_template('webPage/pages/error-page/404.jinja')
    return HttpResponse(template.render())

def page_error(request):
    template=loader.get_template('webPage/pages/error-page/500.jinja')
    return HttpResponse(template.render())
