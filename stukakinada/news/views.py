from django.shortcuts import render
from .models import News_Post
# Create your views here.


def news(request):
    news_posts = News_Post.objects.all()
    return render(request, 'news.html', {"posts": news_posts})


def post(request, pk):
    news_posts = News_Post.objects.get(id=pk)
    return render(request, 'post.html', {"posts": news_posts})
