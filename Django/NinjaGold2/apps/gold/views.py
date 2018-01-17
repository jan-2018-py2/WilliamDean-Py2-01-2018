from __future__ import unicode_literals
from datetime import datetime
from django.shortcuts import render, redirect
import random
# Create your views here.
def index(request):
    try:
        request.session['total']
    except KeyError:
        request.session['total'] = 0
    return render(request, "gold/index.html")

def process(request, building_type):
    this_gold = 0
    action = 'earned'
    if building_type == 'farm':
        this_gold = random.randrange(13,28)
    elif building_type == 'cave':
        this_gold = random.randrange(7,11)
    elif building_type == 'house':
        this_gold = random.randrange(1,8)
    else:
        this_gold = random.randrange(-60, 78)
        if this_gold < 0:
            action = 'lost'
    timestamp = datetime.now().strftime("%Y/%m/%d %-I:%M%p")
    this_log = {
        'class': action,
        'message': "You {} {} golds from the {} ({})".format(action, abs(this_gold), building_type, timestamp)
    }
    try:
        log_list = request.session['logs']
    except KeyError:
        log_list = []

    request.session['total'] += this_gold

    log_list.append(this_log)
    request.session['logs'] = log_list

    return redirect('/')