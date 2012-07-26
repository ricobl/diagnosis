from django.conf.urls import patterns, url
from views import ManualURLCheck, ServerURLCheck

urlpatterns = patterns('',
    url(r'^url/manual$', ManualURLCheck.as_view()),
    url(r'^url/server$', ServerURLCheck.as_view()),
)