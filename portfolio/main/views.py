from django.shortcuts import render
from django.conf import settings

def index(request):
    context = {
        "name": settings.DATA.get("name"),
        "about_me": settings.DATA.get("about_me"),
        "skills": settings.DATA.get("skills"),
    }
    return render(request, 'main/index.html', context)

def projects(request):
    context = {
        "projects": settings.DATA.get("projects"),
    }
    return render(request, 'main/projects.html', context)