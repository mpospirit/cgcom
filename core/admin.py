from django.contrib import admin
from .models import BlogViews, GameReviews

# Register your models here.
admin.site.register(BlogViews)
admin.site.register(GameReviews)