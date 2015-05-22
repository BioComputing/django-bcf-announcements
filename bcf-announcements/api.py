from django.conf import settings
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.db.models import Q

from itertools import chain

from rest_framework import generics
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import permissions

from .serializers import *


AUTH_USER_MODEL = get_user_model()


class AnnouncementList(generics.ListAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def get(self, request, format=None):
        user = get_object_or_404(AUTH_USER_MODEL, id=request.user.id)
        now = timezone.now()
        # need the actual ids of the announcements we're dismissing.
        dismissals = user.announcement_dismissals.all().values('announcement')
        if user.is_staff:
            site_announcements = SiteWideAnnouncement.objects.exclude(announcement_ptr__in=dismissals).filter(Q(publish_start__lte=now, publish_end__gt=now) | Q(publish_start__lte=now, publish_end=None))
        else:
            site_announcements = SiteWideAnnouncement.objects.exclude(announcement_ptr__in=dismissals).filter(staff_only=False, publish_start__lte=now, publish_end__gt=now)
        targeted_announcements = user.targeted_announcements.exclude(announcement_ptr__in=dismissals).filter(publish_start__lte=now, publish_end__gt=now)
        # itertools chaining for getting separate model class instances in a single list.
        announcements = [f for f in chain(site_announcements, targeted_announcements)]
        serializer = AnnouncementSerializer(announcements, many=True)
        return Response(serializer.data)


class AnnouncementDismiss(generics.CreateAPIView):
    permission_classes = (permissions.IsAuthenticated,)

    def post(self, request, pk, format=None):
        with transaction.atomic():
            announcement_type = request.DATA['type']
            if announcement_type == 'sitewideannouncement':
                announcement = SiteWideAnnouncement.objects.get(pk=pk)
            elif announcement_type == 'targetedannouncement':
                announcement = TargetedAnnouncement.objects.get(pk=pk)
            if announcement.dismissal_type is not 'none':
                Dismissal.objects.create(user_id=request.user.id, announcement=announcement)
                return Response('Announcement {} has been dismissed for user {}.'.format(announcement.title, request.user.username), status=200)  # TODO maybe return object
            else:
                return Response(status=401)  # TODO maybe send better error description.
