"""Quizsystem URL Configuration

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
from sys import path

from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.select, name='select'),
    url(r'^studregi/$', views.studregi, name='studregi'),
    url(r'^teachregi/$', views.teachregi, name='teachregi'),
    url(r'^studlogin$',auth_views.LoginView.as_view(template_name='registration/studlogin.html'), name='studlogin'),
   # url(r'^studlogin/$', auth_views.auth_login, {'template_name': 'registration/studlogin.html'} , name='studlogin'),
    url(r'^teachlogin$',auth_views.LoginView.as_view(template_name='registration/teachlogin.html'), name='teachlogin'),
   # url(r'^teachlogin/$', auth_views.LoginView, {'template_name': 'registration/teachlogin.html'} , name='teachlogin'),
    url(r'^logout/$',auth_views.LoginView.as_view(template_name='registration/logout.html'), name='logout'),
   # url(r'^logout/$', auth_views.LogoutView, {'template_name': 'registration/logout.html'}, name='logout'),
    url(r'^Quiz/', include('Quiz.urls')),
    url(r'^accounts/', include('allauth.urls')),
]
