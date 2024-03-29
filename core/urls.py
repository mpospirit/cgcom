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
    path("thesis/", views.thesis, name="thesis"),
    path("blog/", views.blog, name="blog"),
    path("blog/example/", views.blog_example, name="blog_example"),
    path("blog/creating-lottie-animations-for-the-web-using-after-effects/", views.blog_lottie, name="blog_lottie"),
]