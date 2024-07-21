from django.shortcuts import get_object_or_404, render

from .models import Startup, Tag


def tag_list(request):
    tag_list = Tag._default_manager.all()
    return render(
            request,
            'startups/tag_list.html',
            { 'tag_list': tag_list })


def tag_detail(request, slug):
    tag = get_object_or_404(Tag, slug__iexact=slug)
    return render(
            request,
            'startups/tag_detail.html',
            { 'tag': tag })

def startups_list(request):
    startup_list = Startup._default_manager.all()
    return render(
            request,
            'startups/startup_list.html',
            { 'startup_list' : startup_list }
            )

def startup_detail(request, slug):
    startup = get_object_or_404(
            Startup,
            slug__iexact=slug)
    return render(
            request,
            'startups/startup_detail.html',
            { 'startup': startup })
