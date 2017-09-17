from django.conf.urls import url, include
from . import views
urlpatterns =[
url(r'^posty$',views.posty, name="posty"),
]