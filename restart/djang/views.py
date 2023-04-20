from django.http import HttpResponse
from django.shortcuts import render
from .models import *

data = [{'title':'Главная страница', 'url_name':'index'},
       {'title':'О сайте', 'url_name':'about'},
       {'title':'Помощь', 'url_name': 'help'},
]


def index(request):
    model = Post
    context = {
        'data':data
    }
    return render(request, 'djang/base.html', context = context)

def about(request):
    return render(request, 'djang/about.html', {'data': data})


def help(request):
    return render(request, 'djang/help.html', {'data':data})
    


# Create your views here.
