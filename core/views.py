from django.shortcuts import render
from django.http import HttpResponse
from django_user_agents.utils import get_user_agent

def index(request):
    user_agent = get_user_agent(request)
    # If the user is a mobile device, render the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/index.html", locals())
    # Otherwise, render the desktop template
    else:
        return render(request, "index.html", locals())

def about(request):
    user_agent = get_user_agent(request)
    # If the user is a mobile device, render the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/about.html", locals())
    # Otherwise, render the desktop template
    else:
        return render(request, "about.html", locals())

# def projects(request):
#     user_agent = get_user_agent(request)
#     # If the user is a mobile device, render the mobile template
#     if user_agent.is_mobile or user_agent.is_tablet:
#         return render(request, "mobile/projects.html", locals())
#     # Otherwise, render the desktop template
#     else:
#         return render(request, "projects.html", locals())

# def skills(request):
#     user_agent = get_user_agent(request)
#     # If the user is a mobile device, render the mobile template
#     if user_agent.is_mobile or user_agent.is_tablet:
#         return render(request, "mobile/skills.html", locals())
#     # Otherwise, render the desktop template
#     else:
#         return render(request, "skills.html", locals())

def art(request):
    user_agent = get_user_agent(request)
    # If the user is a mobile device, render the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/art.html", locals())
    # Otherwise, render the desktop template
    else:
        return render(request, "art.html", locals())

def thesis(request):
    user_agent = get_user_agent(request)
    # If the user is a mobile device, render the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/thesis.html", locals())
    # Otherwise, render the desktop template
    else:
        return render(request, "thesis.html", locals())
    
def blog(request):
    user_agent = get_user_agent(request)
    # If the user is a mobile device, render the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/blog/blog.html", locals())
    # Otherwise, render the desktop template
    else:
        return render(request, "blog/blog.html", locals())

def blog_example(request):
    user_agent = get_user_agent(request)
    # If the user is a mobile device, render the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/blog/blog_example.html", locals())
    # Otherwise, render the desktop template
    else:
        return render(request, "blog/blog_example.html", locals())
    
def blog_lottie(request):
    user_agent = get_user_agent(request)
    # If the user is a mobile device, render the mobile template
    if user_agent.is_mobile or user_agent.is_tablet:
        return render(request, "mobile/blog/blog_lottie.html", locals())
    # Otherwise, render the desktop template
    else:
        return render(request, "blog/blog_lottie.html", locals())
    
def custom_404(request, exception):
    return render(request, "404.html", locals(), status=404)