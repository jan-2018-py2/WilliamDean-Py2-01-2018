
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^login$', views.login),
    url(r'^register$', views.register),
    url(r'^welcome$', views.welcome),
    url(r'^user/(?P<user_id>\d+)$', views.show)
]
