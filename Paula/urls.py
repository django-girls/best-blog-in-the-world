from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^new_view$', views.new_view, name='new_view'),
    url(r'^post_remove_all$', views.post_remove_all, name='post_remove_all'),
]