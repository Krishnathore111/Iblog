from django.shortcuts import render
from .models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    # load all post from db
    posts=Post.objects.all()[:11]
    # print(posts)
    cats = Category.objects.all()
    data = {'posts':posts, 'cats':cats, 'user':request.user}
    return render(request,"home.html",data)

def get_post(request,url):
    post = Post.objects.get(url=url)
    cats = Category.objects.all()

    print(post)
    return render(request,'posts.html',{'post':post,'cats':cats})

def get_category(request,url):
    cat = Category.objects.get(url=url)
    posts = Post.objects.filter(cat = cat)
    return render(request,'category.html',{'cat':cat, "post":posts})

def about(request):
    return render(request,'about.html', {})