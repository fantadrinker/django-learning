from django.http.response import Http404
from django.shortcuts import render

from blogs.models import Post

# Create your views here.

def post_list(request):
    return render(
            request,
            'blogs/post_list.html',
            { 'post_list': Post.objects.all() }
        )

def post_detail(request, month, year, slug):
    try:
        got_post = Post.objects.filter(pub__date__year=year).filter(pub__date__month=month).get(slug__iexact=slug)
        return render(
                request,
                'blogs/post_detail.html',
                { 'post': got_post })
    except Post.DoesNotExist:
        raise Http404
