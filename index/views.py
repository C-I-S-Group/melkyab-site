from django.shortcuts import render
from django.http import HttpResponse
from index.models import *
# Create your views here.


def home_view(request):
    posts = List_ads.objects.filter(status=1)

    context = {'posts':posts}
    return render(request,'index.html',context)






def contact_view(request):
    return render(request, 'contact.html')

def about_view(request):
    return render(request, 'about.html')

def magazine_view(request):
    return render(request, 'magazine.html')

def property_view(request):
    return render(request, 'property-1.html')

def article_view(request):
    return render(request, 'article-1.html')
