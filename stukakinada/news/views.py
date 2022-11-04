from django.shortcuts import render
from .models import newsArticle, image


def news(request):
    news_posts = newsArticle.objects.all()
    return render(request, 'news.html', {"posts": news_posts})


def post(request, pk):
    news_posts = newsArticle.objects.get(id=pk)
    images = image.objects.filter(tag=news_posts.title)
    data = {"posts": news_posts, 'news_images': images}
    return render(request, 'post.html', {"data": data})
