from django.conf.urls import url, patterns
from django.contrib import admin
from .api import *


admin.autodiscover()

urlpatterns = patterns(
    (r'^api/announcement/(?P<pk>\d+)/dismiss$', AnnouncementDismiss.as_view()),
    (r'^api/announcements$', AnnouncementList.as_view()),
)
