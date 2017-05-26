# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Performer, Album, Rating


class AlbumInline(admin.StackedInline):
    model = Album
    extra = 1


class PerformerAdmin(admin.ModelAdmin):
    inlines = [AlbumInline]
    list_display = ['name', 'mean']


class RatingInline(admin.StackedInline):
    model = Rating
    extra = 1


class AlbumAdmin(admin.ModelAdmin):
    inlines = [RatingInline]
    list_display = ['performer', 'title', 'pub_year', 'mean']

admin.site.register(Performer, PerformerAdmin)
admin.site.register(Album, AlbumAdmin)
