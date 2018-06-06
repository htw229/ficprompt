"""ficprompt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from ficpromptapp import views

urlpatterns = [
    # admin #
    url(r'^admin/', include(admin.site.urls)),
    url(r'^chaining/', include('smart_selects.urls')),


    url(r'^$', views.home, name='home'),
    url(r'^robots.txt', views.robotstxt, name='robotstxt'),

    #MAINTENANCE#
    # comment out to enable live site
    # don't comment out 'LIVE PROMPTS'
    # first url will precede all subsequent
    # url(r'^chubbyprompts/', views.maintenance),


    #LIVE PROMPTS#
    url(r'^chubbyprompts/', views.chubbypromptsview, {
        'url': '/chubbyprompts/',
        'n': 1,
        'debug': False
    }),

    url(r'^chubbypromptsselectplot/', views.chubbypromptsselectplotview, {
        'url': '/chubbypromptsselectplot/',
        'n': 1,
        'debug': True
    }),


    #TESTING#
    url(r'^testprompts/chubbyprompts/', views.chubbypromptsview, {
        'url': '/testprompts/chubbyprompts/',
        'n': 10,
        'debug': True
    }),

    url(r'^testprompts/ficprompts/', views.ficpromptsview, {
        'url': '/testprompts/ficprompts/',
        'n': 10,
        'debug': True,
    }),

    url(r'^testprompts/chubbyficprompts/', views.chubbyficpromptsview, {
        'url': '/testprompts/chubbyficprompts/',
        'n': 10,
        'debug': True,
    }),


    #TEXT CONVOS
    url(r'^textsforao3/', views.textsforao3view, {
        'url': '/textsforao3/',
        'debug': True,
    }),

    #REDIRECTS#
    url(r'^ckprompts/', views.ckprompts, name='ckprompts'),
]