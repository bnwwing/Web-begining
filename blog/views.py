from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from . import models
from django.contrib import auth
from django.contrib.auth.models import User

def login(request):
    return render(request,'blog/login.html')

def log_action(request):
    if request.method=='POST':
        username = request.POST.get('u', 'username')
        password = request.POST.get('p', 'password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            articles = models.Article.objects.all()
            return render(request, 'blog/index.html', {'articles': articles})
        else:
            return JsonResponse({'message':"username or password is error!!"})


def regist_action(request):
    username=request.POST.get('u','username')
    password=request.POST.get('p','password')
    result=User.objects.filter(username=username)
    if result:
        return JsonResponse({'messaae':'username is already exits!!'})
    User.objects.create_user(username=username,password=password)
    return JsonResponse({'username':username,'message':'regist ok!'})



def index(request):
    #实例化一个模型对象，其中主键值为1
    articles=models.Article.objects.all()
    return render(request,'blog/index.html',{'articles':articles})

def article_page(request,article_id):
    article=models.Article.objects.get(pk=article_id)
    return render(request,'blog/article_page.html',{'article':article})

def edit_page(request,article_id):
    if str(article_id)=='0':
        return render(request,'blog/edit_page.html')
    else:
        article=models.Article.objects.get(pk=article_id)
        return render(request,'blog/edit_page.html',{'article':article})

def edit_action(request):
    title=request.POST.get('title','TITLE')
    content=request.POST.get('content','CONTENT')
    article_id=request.POST.get('article_id','0')

    if article_id=='0':
        models.Article.objects.create(title=title, content=content)
        # 返回主页
        articles = models.Article.objects.all()
        return render(request, 'blog/index.html', {'articles': articles})
    else:
        article=models.Article.objects.get(pk=article_id)
        article.title=title
        article.content=content
        article.save()
        return render(request,'blog/article_page.html',{'article':article})

def deleteArticle(request,article_id):
    models.Article.objects.filter(id=article_id).delete()
    articles = models.Article.objects.all()
    return render(request, 'blog/index.html', {'articles': articles})


