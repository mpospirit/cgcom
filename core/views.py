from django.shortcuts import render
from django.http import HttpResponse
from django_user_agents.utils import get_user_agent
from datetime import datetime
from .models import BlogViews, GameReviews, ToiletReview, AlbumReview, BookReview
from .utils import cat_human_translator


def index(request):
    user_agent = get_user_agent(request)
    # If the user is a mobile device, rendering the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/index.html", locals())
    # Otherwise, rendering the desktop template
    else:
        return render(request, "index.html", locals())


def about(request):
    user_agent = get_user_agent(request)
    # If the user is a mobile device, rendering the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/about.html", locals())
    # Otherwise, rendering the desktop template
    else:
        return render(request, "about.html", locals())


# def projects(request):
#     user_agent = get_user_agent(request)
#     # If the user is a mobile device, rendering the mobile template
#     if user_agent.is_mobile or user_agent.is_tablet:
#         return render(request, "mobile/projects.html", locals())
#     # Otherwise, rendering the desktop template
#     else:
#         return render(request, "projects.html", locals())

# def skills(request):
#     user_agent = get_user_agent(request)
#     # If the user is a mobile device, rendering the mobile template
#     if user_agent.is_mobile or user_agent.is_tablet:
#         return render(request, "mobile/skills.html", locals())
#     # Otherwise, rendering the desktop template
#     else:
#         return render(request, "skills.html", locals())


def tech_stack(request):
    user_agent = get_user_agent(request)
    # If the user is a mobile device, rendering the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/techstack.html", locals())
    # Otherwise, rendering the desktop template
    else:
        return render(request, "techstack.html", locals())


def art(request):
    user_agent = get_user_agent(request)
    # If the user is a mobile device, rendering the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/art.html", locals())
    # Otherwise, rendering the desktop template
    else:
        return render(request, "art.html", locals())


def reviews(request):
    user_agent = get_user_agent(request)

    game_reviews_count = GameReviews.objects.all().count()
    toilet_reviews_count = ToiletReview.objects.all().count()
    album_reviews_count = AlbumReview.objects.all().count()
    city_reviews_count = 0
    book_reviews_count = BookReview.objects.all().count()

    context = {"game_reviews_count": game_reviews_count,
               "toilet_reviews_count": toilet_reviews_count,
               "album_reviews_count": album_reviews_count,
               "city_reviews_count": city_reviews_count,
                "book_reviews_count": book_reviews_count}

    # If the user is a mobile device, rendering the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/reviews/reviews.html", context)
    # Otherwise, rendering the desktop template
    else:
        return render(request, "reviews/reviews.html", context)


def game_reviews(request):
    user_agent = get_user_agent(request)

    game_reviews = GameReviews.objects.all()
    # Ordering the reviews by the rating in ascending order
    game_reviews = sorted(game_reviews, key=lambda x: x.overallRating, reverse=False)

    context = {"game_reviews": game_reviews}

    # If the user is a mobile device, rendering the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/reviews/game_reviews.html", context)
    # Otherwise, rendering the desktop template
    else:
        return render(request, "reviews/game_reviews.html", context)
    

def toilet_reviews(request):
    user_agent = get_user_agent(request)

    toilet_reviews = ToiletReview.objects.all()
    # Ordering the reviews by the rating in ascending order
    toilet_reviews = sorted(toilet_reviews, key=lambda x: x.overallRating, reverse=False)

    context = {"toilet_reviews": toilet_reviews}
    # If the user is a mobile device, rendering the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/reviews/toilet_reviews.html", context)
    # Otherwise, rendering the desktop template
    else:
        return render(request, "reviews/toilet_reviews.html", context)
    

def album_reviews(request):
    user_agent = get_user_agent(request)

    album_reviews = AlbumReview.objects.all()
    # Ordering the reviews by the rating in ascending order
    album_reviews = sorted(album_reviews, key=lambda x: x.overallRating, reverse=False)

    context = {"album_reviews": album_reviews}
    # If the user is a mobile device, rendering the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/reviews/album_reviews.html", context)
    # Otherwise, rendering the desktop template
    else:
        return render(request, "reviews/album_reviews.html", context)
    

def city_reviews(request):
    user_agent = get_user_agent(request)
    # If the user is a mobile device, rendering the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/reviews/city_reviews.html", locals())
    # Otherwise, rendering the desktop template
    else:
        return render(request, "reviews/city_reviews.html", locals())
    

def book_reviews(request):
    user_agent = get_user_agent(request)

    book_reviews = BookReview.objects.all()
    # Ordering the reviews by the rating in ascending order
    book_reviews = sorted(book_reviews, key=lambda x: x.overallRating, reverse=False)

    context = {"book_reviews": book_reviews}
    # If the user is a mobile device, rendering the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/reviews/book_reviews.html", context)
    # Otherwise, rendering the desktop template
    else:
        return render(request, "reviews/book_reviews.html", context)
    

def thesis(request):
    user_agent = get_user_agent(request)

    # Getting the user's IP address
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")

    # Saving the user's IP address and user agent to the database
    BlogViews.objects.create(
        blogId=1, dateCreated=datetime.now(), ipAddress=ip, userAgent=user_agent
    )

    # Calculating the total number of views
    total_views = BlogViews.objects.filter(blogId=1).count()

    # Passing the total number of views to the template
    context = {"total_views": total_views}

    # If the user is a mobile device, rendering the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/thesis.html", context)
    # Otherwise, rendering the desktop template
    else:
        return render(request, "thesis.html", context)


def blog(request):
    user_agent = get_user_agent(request)
    # If the user is a mobile device, rendering the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/blog/blog.html", locals())
    # Otherwise, rendering the desktop template
    else:
        return render(request, "blog/blog.html", locals())


def blog_example(request):
    user_agent = get_user_agent(request)
    # If the user is a mobile device, rendering the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/blog/blog_example.html", locals())
    # Otherwise, rendering the desktop template
    else:
        return render(request, "blog/blog_example.html", locals())


def blog_lottie(request):
    user_agent = get_user_agent(request)

    # Getting the user's IP address
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")

    # Saving the user's IP address and user agent to the database
    BlogViews.objects.create(
        blogId=2, dateCreated=datetime.now(), ipAddress=ip, userAgent=user_agent
    )

    # Calculating the total number of views
    total_views = BlogViews.objects.filter(blogId=2).count()

    # Passing the total number of views to the template
    context = {"total_views": total_views}
    # If the user is a mobile device, rendering the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/blog/blog_lottie.html", context)
    # Otherwise, rendering the desktop template
    else:
        return render(request, "blog/blog_lottie.html", context)


def blog_foobar(request):
    user_agent = get_user_agent(request)

    # Getting the user's IP address
    x_forwarded_for = request.META.get("HTTP_X_FORWARDED_FOR")
    if x_forwarded_for:
        ip = x_forwarded_for.split(",")[0]
    else:
        ip = request.META.get("REMOTE_ADDR")

    # Saving the user's IP address and user agent to the database
    BlogViews.objects.create(
        blogId=3, dateCreated=datetime.now(), ipAddress=ip, userAgent=user_agent
    )

    # Calculating the total number of views
    total_views = BlogViews.objects.filter(blogId=3).count()

    # Passing the total number of views to the template
    context = {"total_views": total_views}
    # If the user is a mobile device, rendering the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/blog/blog_foobar.html", context)
    # Otherwise, rendering the desktop template
    else:
        return render(request, "blog/blog_foobar.html", context)
    

def playground(request):
    user_agent = get_user_agent(request)
    # If the user is a mobile device, rendering the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/playground/playground.html", locals())
    # Otherwise, rendering the desktop template
    else:
        return render(request, "playground/playground.html", locals())


def playground_cat_translator(request):
    user_agent = get_user_agent(request)

    if request.method == 'POST':
        text = request.POST.get('text')
        mode = request.POST.get('mode')

        translated_text = cat_human_translator(text, mode)

        context = {"translated_text": translated_text,
                   "text": text,}

        if user_agent.is_mobile or user_agent.is_tablet:
            return render(request, "mobile/playground/cat_translator.html", context)
        else:
            return render(request, "playground/cat_translator.html", context)
        
    # If the user is a mobile device, rendering the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/playground/cat_translator.html", locals())
    # Otherwise, rendering the desktop template
    else:
        return render(request, "playground/cat_translator.html", locals())

def custom_404(request, exception):
    return render(request, "404.html", locals(), status=404)