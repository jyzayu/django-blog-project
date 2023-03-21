from django.shortcuts import render

from django_prj.blog.models import Post


# Create your views here.

def index(request):
    posts = Post.Objects.all().order_by('-pk')

    return render(
        request,
        'blog/index.html',
        {
            'posts': posts,
        }
    )
#
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#
#     return render(
#         request,
#         'blog/single_post_page.html',
#
#     )