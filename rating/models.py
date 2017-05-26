# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Performer(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def mean(self):
        return Rating.objects.filter(album__performer_id=self.pk).aggregate(models.Avg('rating'))['rating__avg']


class Album(models.Model):
    performer = models.ForeignKey(Performer)
    title = models.CharField(max_length=50)
    pub_year = models.IntegerField()

    def mean(self):
        return Rating.objects.filter(album__id=self.pk).aggregate(models.Avg('rating'))['rating__avg']


class Rating(models.Model):
    album = models.ForeignKey(Album)
    rating = models.FloatField(validators=[MinValueValidator(0.), MaxValueValidator(10.)])
    style = models.CharField(max_length=50)
    desc = models.CharField(max_length=500)
