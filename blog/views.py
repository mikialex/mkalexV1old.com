from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.template import Context
from django.template import loader,Template

from django.http import Http404
import datetime
import MySQLdb

# Create your views here.


def main(request):
	t=loader.get_template('blog/main.html')
	c=Context({"name":"mk"})
	html=t.render(c);
	return HttpResponse(html)


def articleList(request):
	t=loader.get_template('blog/article.html')
	html=t.render()
	return HttpResponse(html)