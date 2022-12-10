from django.urls import path
from . import views

urlpatterns = [
    path('upload/news', views.news, name='upload_news'),
    path('upload/events', views.events, name='upload_events'),
    path('upload/file', views.file, name='upload_file'),

]