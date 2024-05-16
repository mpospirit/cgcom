from django.urls import path

from . import views

app_name = "core"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    # path("projects/", views.projects, name="projects"),
    # path("skills/", views.skills, name="skills"),
    path("tech-stack/", views.tech_stack, name="tech_stack"),
    path("art/", views.art, name="art"),
    path("reviews/", views.reviews, name="reviews"),
    path("reviews/game/", views.game_reviews, name="game_reviews"),
    path("reviews/toilet/", views.toilet_reviews, name="toilet_reviews"),
    path("reviews/album/", views.album_reviews, name="album_reviews"),
    path("reviews/city/", views.city_reviews, name="city_reviews"),
    path("reviews/book/", views.book_reviews, name="book_reviews"),
    path("thesis/", views.thesis, name="thesis"),
    path("blog/", views.blog, name="blog"),
    path("blog/example/", views.blog_example, name="blog_example"),
    path("blog/creating-lottie-animations-for-the-web-using-after-effects/", views.blog_lottie, name="blog_lottie"),
    path("blog/google-foobar-challenge-solutions-with-animations/", views.blog_foobar, name="blog_foobar"),
]