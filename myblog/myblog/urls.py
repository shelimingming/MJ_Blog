"""myblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.conf.urls import url
from blog1.views import index,articles,albums,home,article,comments,articles_page,comments_page,albums_page
urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$',index,name='index'),
    url('^home$',home,name='home'),
    url('^articles$',articles,name='articles'),
    url('^articles/article$',article,name='articles_page'),
    url('^articles/articles_page$',articles_page,name='articles_page'),
    url('^albums$',albums,name='albums'),
    url('^albums/albums_page$',albums_page,name='albums_page'),
    url('^comments$',comments,name='comments'),
    url('^comments/comments_page$',comments_page,name='comments_page'),
    url('^articles/comments$',comments_page,name='comments_page'),


]
