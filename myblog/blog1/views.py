#视图层
from django.shortcuts import render
def index(request):
    return render(request,'index.html')


import requests
import json

def home(request):
    # data = '“如果你想要去西班牙度蜜月或者跟人私奔的话，龙达是最适合的地方，全部城市目之所及都是浪漫的风景……”'
    # time = '2018-9-08 12:00:12'
    url = 'http://47.105.163.206:8002/blog/get?id=1'
    res = requests.get(url)
    content = json.loads(res.text)
    data = content['content']
    time = content['createTime']
    read_time = content['readTime']
    return render(request,'home.html',{'top1':data,'time':time,'read_time':read_time})

def articles(request):
    return render(request,'articles.html')

def albums(request):
    return render(request,'albums.html')

def article(request):
    return render(request,'articles/spain.html')

def comments(request):
    return render(request,'comments.html')
