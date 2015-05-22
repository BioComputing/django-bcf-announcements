from rest_framework import serializers
from rest_framework.exceptions import ParseError
from apps.core.serializers import UserSerializer
from .models import *


class SiteWideAnnouncementSerializer(serializers.ModelSerializer):
    creator = UserSerializer()

    class Meta:
        model = SiteWideAnnouncement
        fields = ('id', 'title', 'content', 'creator', 'creation_date', 'dismissal_type', 'publish_start', 'publish_end', 'importance', 'staff_only')


class TargetedAnnouncementSerializer(serializers.ModelSerializer):
    users = UserSerializer(many=True)
    creator = UserSerializer()

    class Meta:
        model = TargetedAnnouncement
        fields = ('id', 'title', 'content', 'creator', 'creation_date', 'dismissal_type', 'publish_start', 'publish_end', 'importance', 'users')


class AnnouncementSerializer(serializers.Serializer):

    def to_native(self, value):
        if isinstance(value, SiteWideAnnouncement):
            return SiteWideAnnouncementSerializer(instance=value).data
        if isinstance(value, TargetedAnnouncement):
            return TargetedAnnouncementSerializer(instance=value).data
        raise Exception('Unexpected type of object for AnnouncementSerializer')
