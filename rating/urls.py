from django.conf.urls import url

from . import views

app_name = 'rating'
urlpatterns = [
    url(r'^$', views.index, name='index'),
]