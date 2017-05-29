from django.conf.urls import url

from . import views
from . import check_limited

urlpatterns = [
    url(r'^test/', check_limited.test , name='test'),
    url(r'^checkLimited/(?P<action>\w[^/]+)', check_limited.do , name='do'),
    url(r'^', views.index, name='index'),
]
