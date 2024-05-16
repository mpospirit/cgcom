from django.contrib import admin
from .models import BlogViews, GameReviews, ToiletReview, AlbumReview, BookReview

# Register your models here.
admin.site.register(BlogViews)
admin.site.register(GameReviews)
admin.site.register(ToiletReview)
admin.site.register(AlbumReview)
admin.site.register(BookReview)