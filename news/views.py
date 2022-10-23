from django.shortcuts import render
from .models import News
# Create your views here.

def newsView(request):
    news_obj = News.objects.all()
    context = {
        'newss': news_obj
    }
    return render(request,'news/news.html', context)