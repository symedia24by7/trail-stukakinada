from django.shortcuts import render
from .models import newsArticle, newsImage


def news(request):
    news_posts = newsArticle.objects.all()

    length = len(news_posts)
    mid_len = length // 2
    first_half = news_posts[:mid_len]
    second_half = news_posts[mid_len:]
    data = {"first": first_half, "second": second_half}
    return render(request, 'news.html', {"data": data})


def post(request, pk):
    news_posts = newsArticle.objects.get(id=pk)
    images = newsImage.objects.filter(tag=news_posts.title)
    data = {"posts": news_posts, 'news_images': images}
    return render(request, 'newsPost.html', {"data": data})
