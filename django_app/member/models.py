from django.contrib.auth.models import AbstractUser
from django.db import models

from video.models import VideoInfo


# class MyUser(AbstractUser):
#     my_video = models.ManyToManyField(VideoInfo, symmetrical=False, related_name="video_set")
#
#     def add_to_box(self, video):
#         return self.my_video.add(video)

class MyUser(AbstractUser):
    my_video = models.ManyToManyField('video.VideoInfo',
                                      through='video.BookMark',
                                      symmetrical=False,

                                      )

    def add_to_box(self, video):
        return self.bookmark_set.create(video=video)
