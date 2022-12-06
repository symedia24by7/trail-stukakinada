from django.contrib import admin
from .models import newsArticle, newsImage

# Register your models here.
admin.site.register(newsArticle)
admin.site.register(newsImage)

