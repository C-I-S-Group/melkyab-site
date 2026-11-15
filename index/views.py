from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from index.models import *
from index.forms import FormConntact
# Create your views here.


def home_view(request):
    posts = List_ads.objects.filter(status=1)

    context = {'posts':posts}
    return render(request,'index.html',context)

def property_view(request,pid):
    posts = List_ads.objects.filter(status=1)
    post = get_object_or_404(posts,pk=pid)
    context = {'post':post}
    return render(request,'property-1.html',context)


def contact_view(request):
    if request.method =='POST':
        form = FormConntact(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = FormConntact()
    context = {"form":form}
    return render(request,'contact.html',context)

def about_view(request):
    return render(request, 'about.html')


def article_view(request):
    return render(request, 'article-1.html')
