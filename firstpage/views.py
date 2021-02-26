from django.shortcuts import render, get_object_or_404
from .models import Post 

# Create your views here.

def post_list(requests):
    posts = Post.published.all()
    return render(requests, 'firstpage/post/list.html', {'posts' : posts})


def post_detail(requests, year, month, day, post):
    post = get_object_or_404(Post,
                              slug=post,
                              status='published',
                              publish__year = year,
                              publish__month = month,
                              publish__day = day
                              )

    return render(requests, 'firstpage/post/detail.html', {'post':post})
