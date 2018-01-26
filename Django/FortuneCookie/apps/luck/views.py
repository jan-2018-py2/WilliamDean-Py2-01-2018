# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import Proverb, Author
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    context = {
        'recent': Proverb.objects.recent_and_not()[0],
        'more': Proverb.objects.recent_and_not()[1]
    }
    return render(request, 'luck/index.html', context)

def add(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, 'luck/add.html', context)

def show(request, proverb_id):
    context = {
        'proverb': Proverb.objects.get(id=proverb_id)
    }
    return render(request, 'luck/show.html', context)

def create(request):
    errs = Proverb.objects.validate_proverb(request.POST)
    if errs:
        for e in errs:
            messages.error(request, e)
    else:
        proverb_id = proverb.objects.create_proverb(request.POST, request.session['user_id']).proverb.id
    return redirect('/proverbs/{}'.format(proverb_id))
