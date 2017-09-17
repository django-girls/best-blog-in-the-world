from django.http import HttpResponse
from django.shortcuts import render, redirect

from blog.models import Post
from 

def posty (parametr):

    return render (parametr,'nalka/postyt.html',{'posty':Post.objects.all()})

def usun (argu):
    Post.objects.all().delete()
    return redirect ('posty')


