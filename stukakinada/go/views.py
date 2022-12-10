from django.shortcuts import render
from django.conf import settings
from .models import File

import os


def go(request):

    all_files = File.objects.all()

    return render(request, 'go.html', {'files': all_files})


def get_files(dir_path):
    res = []
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)

    return res
