from django.urls import path
from . import views

urlpatterns = [
    path('events', views.events, name='events'),
    path('events/<str:pk>', views.eventPost, name='eventPost')
]
