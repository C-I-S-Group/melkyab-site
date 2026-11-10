from .views import *
from django.urls import path

app_name = 'magazine'

urlpatterns = [
    path('', magazine_view, name = 'home'),
]
