from django.conf.urls import  url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^subjects/create$', views.create),
    url(r'^subjects/(?P<subject_id>\d+)/confirm$', views.confirm),
    url(r'^subjects/(?P<subject_id>\d+)/delete$', views.delete)
]