#coding=utf-8
from __future__ import unicode_literals
from django.shortcuts import render ,get_object_or_404
# from django.db.models import Count

from django.core.paginator import Paginator ,EmptyPage,PageNotAnInteger

# Create your views here.
from django.http import HttpResponse ,Http404
from django.template import loader


from markdown2 import Markdown


def friendsIknow(request):
    template=loader.get_template('webPage/pages/friendsIknow.jinja')
    content={
    }
    return HttpResponse(template.render(content))


def contact(request):
    template=loader.get_template('webPage/pages/contact.jinja')
    content={
    }
    return HttpResponse(template.render(content))

def copyright(request):
    template=loader.get_template('webPage/pages/copyright.jinja')
    content={
    }
    return HttpResponse(template.render(content))
