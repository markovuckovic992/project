# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone

from django.db import models

class Match(models.Model):
    home = models.CharField(max_length=30)
    away = models.CharField(max_length=30)
    time = models.DateTimeField(default=timezone.now)
    league = models.ForeignKey(League)
    provider = models.ForeignKey(BettingProvider)

    home_win = models.FloatField(default=1.0)
    away_win = models.FloatField(default=1.0)
    no_win = models.FloatField(default=1.0)

    # rest of data


class BettingProvider(models.Model):
    provider_name = models.CharField(max_length=15)

    # rest of data

class League(models.Model):
    name = models.CharField(max_length=15)
    sport = models.ForeignKey(Sports)
    country = models.ForeignKey(Country)

class Sports(models.Model):
    name = models.CharField(max_length=15)
    short_name = models.CharField(max_length=3)

class Country(models.Model):
    name = models.CharField(max_length=25)
