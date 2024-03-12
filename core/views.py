from django.shortcuts import render
from django.http import HttpResponse
from django_user_agents.utils import get_user_agent
from datetime import datetime
from .models import BlogViews


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
        blogId=1, 
        dateCreated=datetime.now(),
        ipAddress=ip, 
        userAgent=user_agent
    )

    # Calculating the total number of views
    total_views = BlogViews.objects.filter(blogId=1).count()

    # Passing the total number of views to the template
    context = {
        "total_views": total_views
    }
    
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
        blogId=2, 
        dateCreated=datetime.now(),
        ipAddress=ip, 
        userAgent=user_agent
    )

    # Calculating the total number of views
    total_views = BlogViews.objects.filter(blogId=2).count()

    # Passing the total number of views to the template
    context = {
        "total_views": total_views
    }
    # If the user is a mobile device, rendering the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/blog/blog_lottie.html", context)
    # Otherwise, rendering the desktop template
    else:
        return render(request, "blog/blog_lottie.html", context)


def custom_404(request, exception):
    return render(request, "404.html", locals(), status=404)
