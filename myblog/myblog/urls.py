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
from blog1.views import articles, albums, home, article, comments, goToRegisterPage, register, login, logout,loginClose

urlpatterns = [
    path('admin/', admin.site.urls),

    # 主页url配置
    url('^$', home, name='index'),
    url('^home$', home, name='home'),
    url('^articles$', articles, name='articles'),
    url('^albums$', albums, name='albums'),
    url('^comments$', comments, name='comments'),

    # 登录、注册
    url('^goToRegisterPage$', goToRegisterPage, name='goToRegisterPage'),
    url('^register$', register, name='register'),
    url('^login$', login, name='login'),
    url('^logout$', logout, name='logout'),
    url('^loginClose$', loginClose, name='loginClose'),



    # 二级子页面配置
    url('^articles/article$', article, name='article'),

]
