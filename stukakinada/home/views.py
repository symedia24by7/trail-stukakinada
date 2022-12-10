from django.shortcuts import render
from news.models import newsArticle, newsImage
from events.models import event, eventImage
from go.models import File
from django.conf import settings
import os

def home(request):

    news_list = newsArticle.objects.all()
    events = event.objects.all()

    rev_list_news = list(news_list)
    rev_list_events = list(events)

    rev_list_news.reverse()
    rev_list_events.reverse()

    if len(rev_list_news) > 3:
        final_list_news = [rev_list_news[0], rev_list_news[1], rev_list_news[2]]
    else:
        final_list_news = rev_list_news

    if len(rev_list_events) > 3:
        final_list_events = [rev_list_events[0], rev_list_events[1], rev_list_events[2]]
    else:
        final_list_events = rev_list_events


    for p in final_list_events:
        eventImages = eventImage.objects.filter(tag=p.title)
        if(len(eventImages)>0):
            p.img = eventImages[0]

    n1ImgObj : ImageObject = ImageObject("", "")
    e1ImgObj : ImageObject = ImageObject("" ,"")

    for i in final_list_news:
        n1Images = newsImage.objects.filter(tag=i.title)
        if len(n1Images) >= 1:
            n1ImgObj = ImageObject(n1Images[0], "/news/" + str(i.id))
            break

    for i in final_list_events:
        e1Images = eventImage.objects.filter(tag=i.title)
        if len(e1Images) >= 1:
            e1ImgObj = ImageObject(e1Images[0], "/events/" + str(i.id))
            break

    files : File = []

    all_files = File.objects.all()
    rev_files = list(all_files)
    rev_files.reverse()

    final_files = []

    if len(rev_files) > 6:
        final_files = [rev_files[0], rev_files[1], rev_files[2], rev_files[3], rev_files[4], rev_files[5]]
    else:
        final_files = rev_files

    data = {'posts': final_list_news,
            'events': final_list_events,
            'files': final_files,
            "caro_news": n1ImgObj,
            "caro_events": e1ImgObj}

    return render(request, 'home.html', {'data': data})


def search(request):
    news = []
    events = []
    files = []
    if request.method == "GET":
        search_text = str(request.GET["q"]).lower()
        all_news = newsArticle.objects.all()
        all_events = event.objects.all()
        all_files = File.objects.all()
        for n in all_news:
            t = str(n.title).lower()
            if search_text in t:
                news.append(n)
        for e in all_events:
            t = str(e.title).lower()
            if search_text in t:
                events.append(e)
        for f in all_files:
            t = str(f.filename).lower()
            if search_text in t:
                files.append(f)

        data = {"search": search_text, 'news': news, 'events' : events, 'files' : files}
        return render(request, 'search.html', {'data': data})

    return render(request, 'search.html')

def get_files(dir_path):
    res = []
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
            res.append(path)

    return res

class ImageObject:
    def __init__(self, image, link):
        self.image = image
        self.link = link