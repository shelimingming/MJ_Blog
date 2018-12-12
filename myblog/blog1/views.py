# 视图层
from django.shortcuts import render
from blog1 import http
import requests
import json


# 主页
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
    return render(request, 'home.html', {'top1': data, 'time': time, 'read_time': 5})


# 所有文章页面
def articles(request):
    return render(request, 'articles.html')


# 相册页面
def albums(request):
    return render(request, 'albums.html')


# 留言页面
def comments(request):
    return render(request, 'comments.html')


# 单文章
def article(request):
    title = 'Hola,Spain'
    content = '“如果你想要去西班牙度蜜月或者跟人私奔的话，龙达是最适合的地方，全部城市目之所及都是浪漫的风景……”选择龙达的原因只因为他是海明威口中的私奔之城。整个城市都在悬崖峭壁之上，小镇的老城区和新城区通过新桥连接起来。'
    return render(request, 'articles/article.html', {'title': title, 'content': content})


# 登录
def login(request):
    concat = request.POST
    username = concat.get('username')
    password = concat.get('password')
    keep = concat.get('keep') # 下次是否自动登录
    print(username, password, keep)

    url = "http://47.105.163.206:8003/user/login?username=" + username + "&password=" + password;
    user = http.get(url)
    print(user)

    if (user):
        print("登录成功")
        request.session['user'] = user
        #如果keep不为None，设置seesion
        if keep:
            #一个月后失效，以秒为单位
            request.session.set_expiry(60*60*24*30)
        else:
            #关闭浏览器就会失效
            request.session.set_expiry(0)

        return render(request, 'home.html')
    else:
        print("用户名密码错误")


# 退出登录
def logout(request):
    request.session['user'] = None
    return render(request, 'home.html')
