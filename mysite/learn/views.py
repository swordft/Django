# coding:utf-8
from django.http import HttpResponse

def index(request):
    return HttpResponse(u"欢迎光临 喵老湿课堂")

# Create your views here.
