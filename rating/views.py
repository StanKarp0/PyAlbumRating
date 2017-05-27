# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
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
