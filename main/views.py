from django.shortcuts import render, redirect
from .models import Post

def home(request):
    posts = Post.objects.all()
    return render(request, 'home.html', {'posts': posts})

def go_link(request, id):
    post = Post.objects.get(id=id)
    return redirect(post.link)

# 👉 THÊM LẠI 2 HÀM NÀY
def register_redirect(request):
    return redirect('https://www.cm8828.com/home/register?id=524250198')

def login_redirect(request):
    return redirect('https://www.cm8828.com/home/register?id=524250198')

def register_code (request):
    return redirect('https://t.me/phatcodengaunhien')

def register_tele (request):
    return redirect('https://t.me/phanchungsanhu95')