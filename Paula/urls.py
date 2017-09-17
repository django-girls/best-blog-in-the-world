from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new_view$', views.new_view, name='new_view'),
]