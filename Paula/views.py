from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def new_view(request):
    return render(request, 'Paula/post_list.html', {})