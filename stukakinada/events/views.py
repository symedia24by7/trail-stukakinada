from django.shortcuts import render
from .models import event, eventImage


def events(request):
    events = event.objects.all()
    length = len(events)
    mid_len = length // 2
    first_half = events[:mid_len]
    second_half = events[mid_len:]
    data = {"first": first_half, "second": second_half}
    return render(request, 'events.html', {'data': data})


def eventPost(request, pk):
    event_post = event.objects.get(id=pk)
    images = eventImage.objects.filter(tag=event_post.title)
    data = {"posts": event_post, 'news_images': images}
    return render(request, 'eventPost.html', {"data": data})
