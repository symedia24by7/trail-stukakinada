from django.shortcuts import render
from news.models import newsArticle, newsImage
from events.models import event, eventImage
from django.conf import settings
import os

def home(request):

    news_list = newsArticle.objects.all()
    events = event.objects.all()


    path = settings.MEDIA_ROOT + '\\download'
    files = get_files(path)

    rev_list_news = list(news_list)
    rev_list_events = list(events)
    rev_list_pdfs = list(files)

    rev_list_news.reverse()
    rev_list_events.reverse()
    rev_list_pdfs.reverse()

    if len(rev_list_news) > 3:
        final_list_news = [rev_list_news[0], rev_list_news[1], rev_list_news[2]]
    else:
        final_list_news = rev_list_news

    if len(rev_list_events) > 3:
        final_list_events = [rev_list_events[0], rev_list_events[1], rev_list_events[2]]
    else:
        final_list_events = rev_list_events

    if len(rev_list_pdfs) > 6:
        pdfs = [rev_list_pdfs[0], rev_list_pdfs[1], rev_list_pdfs[2], rev_list_pdfs[3], rev_list_pdfs[4], rev_list_pdfs[5]]
    else:
        pdfs = rev_list_pdfs

    length = len(pdfs)
    mid_index = length // 2
    first_half = pdfs[:mid_index]
    second_half = pdfs[mid_index:]

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

    data = {'posts': final_list_news,
            'events': final_list_events,
            'files_p1': first_half,
            "files_p2": second_half,
            "caro_news": n1ImgObj,
            "caro_events": e1ImgObj}

    return render(request, 'home.html', {'data': data})


def search(request):
    news: newsArticle = []
    if request.method == "POST":
        search_text = str(request.POST["search"]).lower()
        all_news = newsArticle.objects.all()
        for n in all_news:
            t = str(n.title).lower()
            if search_text in t:
                news.append(n)

        data = {"search": search_text, 'news': news}
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