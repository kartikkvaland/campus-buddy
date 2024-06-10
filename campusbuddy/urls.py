"""
URL configuration for campusbuddy project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include 
from buddy.views import *
from buddy import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [ 
    path('admin/', admin.site.urls),
    path('home',index,name='home'),
    # path('play1/',play1,name='play11'),
    path('play1/<int:pk>/', views.play1, name='play11'),
    path('play2/',play2),
    path('upload/',upload,name='upload'),
    path('',login,name='login'),
    path('register/',views.register,name='register'),
    path('videos/', list_videos, name='video_list'),

   
]

if settings.DEBUG:
    urlpatterns+= static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)