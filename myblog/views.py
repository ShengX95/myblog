from django.shortcuts import render, render_to_response
from .models import Article, Tag, Classification, Author
from django.template import RequestContext
from django.http import HttpResponse
# Create your views here.
def test(request):
    blogs = Article.objects.all().order_by('-publish_time')
    author = Author.objects.get(id=1)
    return render_to_response('myblog/test.html', {'blogs': blogs, 'author': author}, RequestContext(request))

def blog_list(request):
    blogs = Article.objects.all().order_by('-publish_time')
    author = Author.objects.get(id=1)
    classification = Classification.objects.all()
    return render_to_response('myblog/index.html', {'blogs': blogs, 'author': author, 'classification': classification}, RequestContext(request))


def blog_detail(request, id):
    blog = Article.objects.get(id=id)
    return render_to_response('myblog/detail.html', {'blog': blog}, RequestContext(request))


def classification_list(request, classname):
	classid = Classification.objects.get(english_name=classname)
	blogs = Article.objects.filter(classification=classid.id)
	author = Author.objects.get(id=1)
	classification = Classification.objects.all()
	return render_to_response('myblog/index.html', {'blogs': blogs, 'author': author, 'classification': classification}, RequestContext(request))
	# return HttpResponse("classid:"+str(classid.id))

