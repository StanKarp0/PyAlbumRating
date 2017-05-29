# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.db.models import Count, Q
from django.core.validators import MinValueValidator, MaxValueValidator


class Performer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def mean(self):
        t = Rating.objects.filter(album__performer_id=self.pk).aggregate(models.Avg('rating'))['rating__avg']
        return ("%2.3f" % float(t)) if t else "-"

    def albums(self):
        return self.album_set.order_by('-pub_year')

    def albums_count(self):
        return self.album_set.order_by('-pub_year').count()


class Album(models.Model):
    performer = models.ForeignKey(Performer)
    title = models.CharField(max_length=50)
    pub_year = models.IntegerField()

    def mean(self):
        res = self.rating_set.aggregate(models.Avg('rating'))['rating__avg']
        return res if res else "-"

    def ratings(self):
        return self.rating_set.order_by('date')

    def rating_count(self):
        return self.rating_set.count()

    @staticmethod
    def rated():
        rated_id = Rating.objects.values('album').annotate(count=Count('album')).values_list('album', flat=True)
        return Album.objects.filter(pk__in=rated_id).order_by('-pub_year')

    @staticmethod
    def unrated():
        rated_id = Rating.objects.values('album').annotate(count=Count('album')).values_list('album', flat=True)
        return Album.objects.filter(~Q(pk__in=rated_id)).order_by('-pub_year')

    def __str__(self):
        return self.performer.name + " - " + self.title


class Rating(models.Model):
    date = models.DateField(auto_now=True)
    album = models.ForeignKey(Album)
    rating = models.FloatField(validators=[MinValueValidator(0.), MaxValueValidator(10.)])
    style = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)

    def __str__(self):
        return self.album.performer.name + " - " + self.album.title + " - " + self.rating
