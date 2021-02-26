from django.shortcuts import render, get_object_or_404
from .models import Post 
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

# Create your views here.

def post_list(request):
    posts = Post.published.all()

    paginator = Paginator(posts, 3)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request,
                  'firstpage/post/list.html', 
                  {'posts' : posts, 'page':page}
                 )


def post_detail(requests, year, month, day, post):
    post = get_object_or_404(Post,
                              slug=post,
                              status='published',
                              publish__year = year,
                              publish__month = month,
                              publish__day = day
                              )

    return render(requests, 'firstpage/post/detail.html', {'post':post})
