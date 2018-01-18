from __future__ import unicode_literals
from django.shortcuts import HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("placeholder to display a list of all the surveys later")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new survey")

def create(request):
    return redirect('/surveys')

def show(request, survey_id):
    return HttpResponse("placeholder to display survey {}".format(survey_id))

def edit(request, survey_id):
    return HttpResponse("placeholder to edit survey {}".format(survey_id))

def delete(request, survey_id):
    return redirect('/surveys')