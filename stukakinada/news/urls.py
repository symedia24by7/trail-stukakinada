from django.urls import path
from . import views

urlpatterns = [
    path('news', views.news, name='news'),
    path('post/<str:pk>', views.post, name='post')
]