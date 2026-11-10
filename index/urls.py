from index.views import *
from django.urls import path

urlpatterns = [
    path('', home_view, name='home'),
    path('contact/', contact_view, name='contact'),
    path('about/', about_view, name = 'about'),
    path('property/', property_view, name='property'),
    path('artcile/', article_view, name='article')
]
