from django.conf.urls import url

from . import views

app_name = 'rating'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^album/(?P<pk>[0-9]+)/$', views.AlbumDetailView.as_view(), name='album_detail'),
    url(r'^album/add/(?P<performer_id>[0-9]+)/$', views.album_add, name='add_album'),
    url(r'^album/rate/(?P<album_id>[0-9]+)/$', views.album_rate, name='rate_album'),
    url(r'^album/update/(?P<pk>[0-9]+)/$', views.AlbumUpdateView.as_view(), name='update_album'),
    url(r'^album/delete/(?P<pk>[0-9]+)/$', views.album_delete, name='delete_album'),
    url(r'^rate/(?P<pk>[0-9]+)/update$', views.RatingUpdateView.as_view(), name='rate_update'),
    url(r'^rate/(?P<rate_id>[0-9]+)/delete$', views.rate_delete, name='rate_delete'),
    url(r'^performer/(?P<pk>[0-9]+)/$', views.PerformerDetailView.as_view(), name='performer_detail'),
    url(r'^performer/add/$', views.performer_add, name='add_performer'),
    url(r'^performer/delete/(?P<pk>[0-9]+)$', views.performer_delete, name='delete_performer'),
    url(r'^performer/update/(?P<pk>[0-9]+)/$', views.PerformerUpdateView.as_view(), name='update_performer'),
]