from django.conf.urls import url

from . import views

app_name = 'rating'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumDetailView.as_view(), name='album_detail'),
    url(r'^performer/(?P<pk>[0-9]+)/$', views.PerformerDetailView.as_view(), name='performer_detail'),
]