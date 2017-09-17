from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.utils import timezone


# Create your views here.
from blog.models import Post


def new_view(request):
    paula_posts = Post.objects.all().order_by('published_date')
    return render(request, 'Paula/paula_post_list.html', {'paula_posts': paula_posts})


def post_remove_all(request):
    Post.objects.all().delete()
    # paula_posts = Post.objects.all().order_by('published_date')
    # return render(request, 'Paula/paula_post_list.html', {'paula_posts': paula_posts})
    return redirect('new_view')
