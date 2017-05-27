# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponseRedirect
from .models import Album, Rating, Performer
from django.views import generic


def index(request):
    return render(request, 'rating/index.html', {
        'albums': Album.objects.order_by('-pub_year'),
        'performers': Performer.objects.order_by('name')
    })


class AlbumDetailView(generic.DetailView):
    model = Album
    template_name = 'rating/album_detail.html'

    def get_context_data(self, **kwargs):
        context = super(AlbumDetailView, self).get_context_data(**kwargs)
        context['ratings'] = kwargs['object'].ratings()
        return context


class PerformerDetailView(generic.DetailView):
    model = Performer
    template_name = 'rating/performer_detail.html'

    def get_context_data(self, **kwargs):
        context = super(PerformerDetailView, self).get_context_data(**kwargs)
        context['albums'] = kwargs['object'].albums()
        return context


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
