from django.shortcuts import render
from django.conf import settings

import os


def go(request):
    path = settings.MEDIA_ROOT + '\\download'
    files = get_files(path)
    return render(request, 'go.html', {'files': files})


def get_files(dir_path):
    res = []
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)

    return res
