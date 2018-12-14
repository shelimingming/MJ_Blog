# 视图层
from django.shortcuts import render, redirect
from blog1 import http as hp


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
    request.session['url'] = request.path
    # request.session['login_stat'] = '1'
    return render(request, 'home.html', {'top1': data, 'time': time, 'read_time': 5})


# 所有文章页面
def articles(request):
    request.session['url'] = request.path
    return render(request, 'articles.html')


# 相册页面
def albums(request):
    request.session['url'] = request.path
    return render(request, 'albums.html')


# 留言页面
def comments(request):
    comments = []
    floor = 1
    if request.method == 'POST':
        concat = request.POST
        message = concat.get('message')
        if request.session.get('user', False) and message:
            request.session['message'] = None
            # 插入数据库
            comment = {}
            comment['user'] = 'Jumboo'
            comment['message'] = message
            comment['floor'] = floor
            comment['date'] = '2018-12-10' + '\t' + '15:11:32'
            comments.append(comment)
            floor += 1
            print('comment')
            #前端处理
        # else:
        #     request.session['message'] = message.strip()

    # 从数据库中读取评论数据
    for i in range(floor, floor + 3):
        comment = {}
        comment['user'] = 'Jumboo'
        comment['message'] = '博主最帅！！！！'
        comment['floor'] = i
        comment['date'] = '2018-12-10' + '\t' + '15:11:32'
        comments.append(comment)
    request.session['url'] = request.path
    return render(request, 'comments.html', {'comments': comments})


# 单文章
def article(request):
    title = 'Hola,Spain'
    content = '“如果你想要去西班牙度蜜月或者跟人私奔的话，龙达是最适合的地方，全部城市目之所及都是浪漫的风景……”选择龙达的原因只因为他是海明威口中的私奔之城。整个城市都在悬崖峭壁之上，小镇的老城区和新城区通过新桥连接起来。'
    request.session['url'] = request.path
    return render(request, 'articles/article.html', {'title': title, 'content': content})


# 跳转到注册界面
def goToRegisterPage(request):
    return render(request, 'login/register.html')


# 注册
def register(request):
    concat = request.POST
    email = concat.get('email')
    acct = concat.get('acct')
    name = concat.get('name')
    mobile = concat.get('mobile')
    password = concat.get('password')
    re_password = concat.get('re_password')
    print(email, acct, name, mobile, password, re_password)

    body = {"acct": acct, "name": name, "mobile": mobile, "email": email, "password": password}

    # 发送http post请求
    url = "http://47.105.163.206:8003/user/register"
    hp.post(url, body)
    pre_url = request.session.get('url')
    return redirect(pre_url)


# 登录
def login(request):
    try:
        # request.session['login_stat'] = None
        concat = request.POST
        username = concat.get('username')
        password = concat.get('password')
        keep = concat.get('keep')  # 下次是否自动登录
        print(username, password, keep)
        pre_url = request.session.get('url')
        if username and password:
            url = "http://47.105.163.206:8003/user/login?username=" + username + "&password=" + password
            user = hp.get(url)
            print(user)
            if (user):
                print("登录成功")
                request.session['user'] = user
                # 如果keep不为None，设置seesion
                if keep:
                    # 一个月后失效，以秒为单位
                    request.session.set_expiry(60 * 60 * 24 * 30)
                else:
                    # 关闭浏览器就会失效
                    request.session.set_expiry(0)
                request.session['login_stat'] = '1'
            else:
                request.session['login_stat'] = '0'
                print("用户名密码错误")
        # else:
        #         #     print("用户名密码不能为空")
        #         #     request.session['login_stat'] = -1
        return redirect(pre_url)
    except:
        request.session['login_stat'] = '-1'
        print("连接异常")
        return redirect(pre_url)



# 退出登录
def logout(request):
    # request.session['user'] = None
    pre_url = request.session.get('url')
    request.session.pop('user')
    request.session['login_stat']='1'
    return redirect(pre_url)


def loginClose(request):
    pre_url = request.session.get('url')
    request.session['login_stat'] = '1'
    return redirect(pre_url)