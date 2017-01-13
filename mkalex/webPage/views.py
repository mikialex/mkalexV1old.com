from django.shortcuts import render ,get_object_or_404

# Create your views here.
from django.http import HttpResponse ,Http404
from django.template import loader

from .models import Article

def index(request):
    template=loader.get_template('webPage/index.html')
    art=Article.objects.get(pk=1)
    content ={'name':art.title}
    return HttpResponse(template.render(content))
