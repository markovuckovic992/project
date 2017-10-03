# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.http import HttpResponse
from django.views import View
from django.shortcuts import render

from administration.models import Match


class IndexView(View):
    template = 'index.html'
    data = {}

    def get(self, request):
        matches = Match.objects.getInitialData()
        self.data = {
            'matches': matches
        }
        return render(request, self.template, self.data)
