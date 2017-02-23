from django.conf import settings
from django.db import models


class VideoInfo(models.Model):
    keyword = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    channel_title = models.CharField(max_length=30)
    channel_id = models.CharField(max_length=30, default="none")
    video_id = models.CharField(max_length=30)
    published_date = models.DateTimeField()


class BookMark(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, )
    video = models.ForeignKey(VideoInfo, )
    bookmarked_date = models.DateTimeField(auto_now_add=True, blank=True)
