from __future__ import unicode_literals
from django.shortcuts import HttpResponse, redirect

# Create your views here.
def index(request):
    return HttpResponse("placeholder to display a list of all the users later")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new user")

def create(request):
    return redirect('/users')

def show(request, user_id):
    return HttpResponse("placeholder to display user {}".format(user_id))

def edit(request, user_id):
    return HttpResponse("placeholder to edit user {}".format(user_id))

def delete(request, user_id):
    return redirect('/users')