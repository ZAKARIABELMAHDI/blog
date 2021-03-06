from typing import List
from django.core import paginator
from django.db.models.query import QuerySet
from django.http import request
from django.shortcuts import render ,get_object_or_404
from django.core.paginator import Page, Paginator, EmptyPage,PageNotAnInteger
from django.views.generic import ListView
# Create your views here.
from .models import Post

class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
def post_list(request):
    posts = Post.published.all()
    object_list = Post.published.all()
    paginator = Paginator(object_list,3) #3 posts in each page
    page = request.GET.get('page')
    try:
        posts =paginator.page(page)
    except PageNotAnInteger:
        #if page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        #if page is out of range deliver  last page of results
        posts =paginator.page(paginator.num_pages)
    
    return render(request, 'blog/post/list.html',
                           {
                         'page': page,
                                'posts':posts
                       })
def post_detail(request, year, month, day, post):
                post = get_object_or_404(Post, slug=post,
                                                status='published',
                                                publish__year=year,
                                                publish__month=month,
                                                publish__day=day)
                return render(request,
                'blog/post/detail.html',
                {'post': post})