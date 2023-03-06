"""employeedatapro URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from employeedataapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('data',views.generatingData),
    path('fetch',views.fetchingData, name='fetch'),
    path('bhubneswar',views.bhubneswar,name='bhubneswar'),
    path('benglore',views.benglore,name='benglore'),
    path('hyderabad',views.hyderabad,name='hyderabad'),
    path('pune',views.pune,name='pune'),
    path('',views.mainPage,name='mainPage')
    
]
