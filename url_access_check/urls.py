from django.conf.urls import patterns, url
from views import UserURLCheck

urlpatterns = patterns('',
    url(r'^url$', UserURLCheck.as_view()),
)