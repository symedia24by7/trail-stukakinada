from django.shortcuts import render, redirect
from django.contrib.auth.models import auth
from news.models import newsArticle, newsImage
from events.models import event, eventImage
from go.models import File
# Create your views here.

def news(request):
    if not auth.get_user(request).is_superuser:
        return redirect('home')

    if request.method == "POST":
        news_name = request.POST["news_name"]
        news_body = request.POST["news_body"]
        news_date = request.POST["news_date"]

        if not news_body or not news_name or not news_date:
            return render(request, 'upload_news.html')

        res = newsArticle.objects.create(title=news_name, body=news_body, created_at=news_date)

        for f in request.FILES.getlist('news_images'):
            newsImage.objects.create(tag=news_name, image=f)

        if res:
            return redirect('news')

    return render(request, 'upload_news.html')

def events(request):
    if not auth.get_user(request).is_superuser:
        return redirect('home')
    if request.method == "POST":
        event_name = request.POST["event_name"]
        event_body = request.POST["event_body"]
        event_date = request.POST["event_date"]

        if not event_name or not event_body or not event_date:
            return render(request, 'upload_events.html')

        res = event.objects.create(title=event_name, body=event_body, created_at=event_date)

        for f in request.FILES.getlist('event_images'):
            eventImage.objects.create(tag=event_name, image=f)

        if res:
            return redirect('events')
    return render(request, 'upload_events.html')


def file(request):
    if not auth.get_user(request).is_superuser:
        return redirect('home')

    if request.method == "POST":
        file_name = request.POST["file_name"]
        file_file = request.FILES["file_file"]

        if not file_name or not file_file:
            return redirect("file")

        res = File.objects.create(filename=file_name, file=file_file)

        if res:
            return redirect("go")


    return render(request, 'upload_file.html')