from __future__ import unicode_literals
from .models import User
from django.shortcuts import render, redirect
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'fortune/index.html')

def register(request):
    result = User.objects.validate_registration(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id 
    messages.success(request, "Successfully registered")
    return redirect('/welcome')

def login(request):
    result = User.objects.validate_login(request.POST)
    if type(result) == list:
        for err in result:
            messages.error(request, err)
        return redirect('/')
    request.session['user_id'] = result.id 
    messages.success(request, "Successfully logged in!")
    return redirect('/welcome')

def welcome(request):
    try:
        request.session['user_id']
    except KeyError:
        return redirect('/')
    context = {
        'user': User.objects.get(id=request.session['user_id'])
    }
    return render(request, 'fortune/welcome.html', context)

def show(request, user_id):
    user = User.objects.get(id=user_id)