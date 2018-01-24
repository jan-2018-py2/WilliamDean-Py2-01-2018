from __future__ import unicode_literals
from .models import Subject
from django.contrib.messages import error
from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    context = {
        "subjects": Subject.objects.all()
    }
    return render(request, 'subjects/index.html', context)

def create(request):
    errors = Subject.objects.validate(request.POST)
    if errors:
        for err in errors:
            error(request, err)
    else:
        Subject.objects.create(
            name=request.POST['name'],
            desc=request.POST['desc']
        )
    return redirect('/')

def confirm(request, subject_id):
    context = {
        "subject": Subject.objects.get(id=subject_id)
    }
    return render(request, 'subjects/confirm.html', context)

def delete(request, subject_id):
    Subject.objects.get(id=subject_id).delete()
    return redirect('/')