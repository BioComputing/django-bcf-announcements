from django.db import models
from django.conf import settings
from django.utils import timezone
import choices


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL')


class Announcement(models.Model):
    """
    A single announcement.
    """

    title = models.CharField(max_length=50)
    content = models.TextField()
    creator = models.ForeignKey(AUTH_USER_MODEL, verbose_name="creator")
    creation_date = models.DateTimeField(auto_now_add=True)
    dismissal_type = models.CharField(max_length=20, choices=choices.DISMISSAL_CHOICES, default='none')
    publish_start = models.DateTimeField(default=timezone.now, blank=True)
    publish_end = models.DateTimeField(blank=True, null=True)
    importance = models.CharField(max_length=40, verbose_name="Importance", choices=choices.IMPORTANCE_CHOICES, default='Normal')

    def __unicode__(self):
        return self.title

    class Meta:
        verbose_name = "announcement"
        verbose_name_plural = "announcements"


class SiteWideAnnouncement(Announcement):
    staff_only = models.BooleanField(default=False)


class TargetedAnnouncement(Announcement):
    users = models.ManyToManyField(AUTH_USER_MODEL, related_name='targeted_announcements')


class Dismissal(models.Model):
    user = models.ForeignKey(AUTH_USER_MODEL, related_name="announcement_dismissals")
    announcement = models.ForeignKey(Announcement, related_name="dismissals")
    dismissed_at = models.DateTimeField(auto_now_add=True)
