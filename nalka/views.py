from django.http import HttpResponse
from django.shortcuts import render
def posty (paramtetr):

    return render (paramtetr,'nalka/postyt.html',{})
# Create your views here.
