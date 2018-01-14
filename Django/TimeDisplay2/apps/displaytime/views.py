from __future__ import unicode_literals
import pytz

from django.utils import timezone
from django.shortcuts import render
from django.utils.deprecation import MiddlewareMixin
# Create your views here.
class TimezonMiddleware(MiddlewareMixin):
    def process_request(self, request):
        tzname = request.session.get('django_timezone')
        if tzname:
            timezone.activate(pytz.timezone(tzname))
        else:
            timezone.deactivate()
            
def index(request):
    context = {
        "time": timezone.now()
    }
    return render(request, 'displaytime/index.html', context)