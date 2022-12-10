from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from news.models import newsArticle, newsImage
import mimetypes
import os


def index(request):
    return redirect('home')

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
