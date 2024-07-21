from django.http.response import Http404
from django.shortcuts import render
from django.views import View
from django.core.exceptions import ObjectDoesNotExist

from blogs.models import Post


# Create your views here.


class PostList(View):
    def get(self, request, parent_template=None):
        return render(
            request,
            'blogs/post_list.html',
            {
                'post_list': Post._default_manager.all(),
                'parent_template': parent_template
            }
        )


def post_detail(request, month, year, slug, parent_template=None):
    try:
        got_post = Post._default_manager.filter(pub__date__year=year).filter(
            pub__date__month=month).get(slug__iexact=slug)
        return render(
            request,
            'blogs/post_detail.html',
            {'post': got_post, 'parent_template': parent_template})
    except ObjectDoesNotExist:
        raise Http404
