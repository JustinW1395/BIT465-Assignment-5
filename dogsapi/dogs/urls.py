"""DogsApi URL Configuration
The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import re_path
from dogs import views

urlpatterns = [
    re_path(r'^$', 
        views.ApiRoot.as_view(), 
        name=views.ApiRoot.name),
    re_path(r'^dogs/$', 
        views.DogList.as_view(), 
        name=views.DogList.name),
    re_path(r'^dogs/(?P<pk>[0-9]+)/$', 
        views.DogDetail.as_view(), 
        name=views.DogDetail.name),
    re_path(r'^breeds/$', 
        views.BreedList.as_view(), 
        name=views.BreedList.name),
    re_path(r'^breeds/(?P<pk>[0-9]+)/$', 
        views.BreedDetail.as_view(), 
        name=views.BreedDetail.name),
]