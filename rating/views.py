# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import Album, Rating, Performer
from django.views import generic
from django.db.models import Q


class IndexView(generic.CreateView):
    model = Performer
    fields = ['name']
    template_name = 'rating/index.html'

    def get_success_url(self):
        return reverse('rating:index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['albums_rated'] = Album.rated()
        context['albums_unrated'] = Album.unrated()
        context['performers'] = Performer.objects.order_by('name')
        context['ratings'] = Rating.objects.order_by('-date')
        return context


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'rating/album_detail.html'


class AlbumUpdateView(generic.UpdateView):
    model = Album
    fields = ['performer', 'title', 'pub_year']
    template_name = 'rating/album_update.html'

    def get_success_url(self):
        return reverse('rating:album_detail', args=(self.kwargs['pk'],))


class AlbumUnratedView(generic.ListView):
    model = Album
    template_name = 'rating/album_list_view.html'

    def get_queryset(self):
        qs = super(AlbumUnratedView, self).get_queryset()
        return qs.filter(rating=None)

    def get_context_data(self, **kwargs):
        context = super(AlbumUnratedView, self).get_context_data(**kwargs)
        context['title'] = 'Unrated albums'
        return context


class AlbumRatedView(generic.ListView):
    model = Album
    template_name = 'rating/album_list_view.html'

    def get_queryset(self):
        qs = super(AlbumRatedView, self).get_queryset()
        return qs.filter(~Q(rating=None))

    def get_context_data(self, **kwargs):
        context = super(AlbumRatedView, self).get_context_data(**kwargs)
        context['title'] = 'Rated albums'
        return context


class RatingUpdateView(generic.UpdateView):
    model = Rating
    fields = ['rating', 'style', 'desc']
    template_name = 'rating/rating_update.html'

    def get_success_url(self):
        album_id = get_object_or_404(Rating, pk=self.kwargs['pk']).album.pk
        return reverse('rating:album_detail', args=(album_id, ))


class RatingListView(generic.ListView):
    model = Rating
    template_name = 'rating/rating_list.html'


class PerformerDetailView(generic.DetailView):
    model = Performer
    template_name = 'rating/performer_detail.html'


class PerformerUpdateView(generic.UpdateView):
    model = Performer
    fields = ['name']
    template_name = 'rating/performer_update.html'

    def get_success_url(self):
        return reverse('rating:performer_detail', args=(self.kwargs['pk'], ))


def performer_add(request):
    p = Performer(name=request.POST['name'])
    p.save()
    return HttpResponseRedirect(reverse('rating:performer_detail', args=(p.pk,)))


def album_add(request, performer_id):
    Album(
        performer=get_object_or_404(Performer, pk=performer_id),
        title=request.POST['title'],
        pub_year=request.POST['year']
    ).save()
    return HttpResponseRedirect(reverse('rating:performer_detail', args=(performer_id,)))


def album_rate(request, album_id):
    Rating(
        album=get_object_or_404(Album, pk=album_id),
        rating=request.POST['rating'],
        style=request.POST['style'],
        desc=request.POST['desc']
    ).save()
    return HttpResponseRedirect(reverse('rating:album_detail', args=(album_id,)))


def rate_delete(request, rate_id):
    rate = get_object_or_404(Rating, pk=rate_id)
    album_id = rate.album.pk
    rate.delete()
    return HttpResponseRedirect(reverse('rating:album_detail', args=(album_id,)))


def performer_delete(request, pk):
    get_object_or_404(Performer, pk=pk).delete()
    return HttpResponseRedirect(reverse('rating:index'))


def album_delete(request, pk):
    get_object_or_404(Album, pk=pk).delete()
    return HttpResponseRedirect(reverse('rating:index'))
