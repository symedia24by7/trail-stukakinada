from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from news.models import newsArticle, image
import mimetypes
import os


def index(request):
    return render(request, 'home.html')


def dashboard(request):
    if not auth.get_user(request).is_authenticated:
        return redirect('login')
    if request.method == "POST":
        news_name = request.POST["news_name"]
        news_body = request.POST["news_body"]
        news_date = request.POST["news_date"]

        if not news_body or not news_name or not news_date:
            return render(request, 'dashboard.html')

        res = newsArticle.objects.create(title=news_name, body=news_body, created_at=news_date)

        for f in request.FILES.getlist('news_images'):
            image.objects.create(tag=news_name, image=f)

        if res:
            return redirect('news')

    return render(request, 'dashboard.html')


def download(request, filename):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Define the full file path
    filepath = BASE_DIR + '/media/download/' + filename
    # Open the file for reading content
    path = open(filepath, 'rb')
    # Set the mime type
    mime_type, _ = mimetypes.guess_type(filepath)
    # Set the return value of the HttpResponse
    response = HttpResponse(path, content_type=mime_type)
    # Set the HTTP header for sending to browser
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    # Return the response value
    return response
