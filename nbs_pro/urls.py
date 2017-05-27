from django.conf.urls import url

from . import views
from .model import check

urlpatterns = [
    url(r'^check', views.check , name='check'),
    url(r'^do', check.do , name='do'),
    url(r'^', views.index, name='index'),
]
