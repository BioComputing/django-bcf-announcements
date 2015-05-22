from django.contrib import admin
from .models import *


class SiteWideAnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'creator', 'creation_date', 'publish_start', 'publish_end', 'importance', 'dismissal_type',)
    search_fields = ('title', 'content',)


class TargetedAnnouncementAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'content', 'creator', 'creation_date', 'publish_start', 'publish_end', 'importance', 'dismissal_type',)
    search_fields = ('title', 'content',)


class DismissalAdmin(admin.ModelAdmin):
    list_display = ('id', 'user',)
    search_fields = ('id', 'user',)

admin.site.register(SiteWideAnnouncement, SiteWideAnnouncementAdmin)
admin.site.register(TargetedAnnouncement, TargetedAnnouncementAdmin)
admin.site.register(Dismissal, DismissalAdmin)
