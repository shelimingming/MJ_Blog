#视图层
from django.shortcuts import render
def index(request):

    return render(request,'index.html',{'page':'home'})


import requests
import json

#主页
def home(request):
    data = '“如果你想要去西班牙度蜜月或者跟人私奔的话，龙达是最适合的地方，全部城市目之所及都是浪漫的风景……”'
    time = '2018-9-08 12:00:12'

    # REST接口
    url = 'http://47.105.163.206:8002/blog/get?id=1'
    # res = requests.get(url)
    # content = json.loads(res.text)
    # data = content['content']
    # time = content['createTime']
    # read_time = content['readTime']
    return render(request,'home.html',{'top1':data,'time':time,'read_time':5})

#所有文章页面
def articles_page(request):
    return render(request,'articles.html')


def articles(request):
    return render(request,'index.html',{'page':'articles/articles_page'})

#相册页面
def albums(request):
    return render(request,'index.html',{'page':'albums/albums_page'})

def albums_page(request):
    return render(request,'albums.html')

#留言页面
def comments(request):
    return render(request,'index.html',{'page':'comments/comments_page'})

def comments_page(request):
    request_type = request.method
    if request_type:
        print(1234)

    return render(request,'comments.html')

#单文章
def article(request):
    title = 'Hola,Spain'
    return render(request,'articles/spain.html',{'title':title})


