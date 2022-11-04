from django.shortcuts import render
from news.models import newsArticle
# Create your views here.


def home(request):

    news : newsArticle = []

    if request.method == "POST":
        search_text = str(request.POST["search"]).lower()
        all_news = newsArticle.objects.all()
        for n in all_news:
            t = str(n.title).lower()
            if search_text in t:
                news.append(n)

        data = {"search": search_text, 'news': news}
        return render(request, 'home.html', {'data': data})
    return render(request, 'home.html')
