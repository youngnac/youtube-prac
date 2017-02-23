from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from member.models import MyUser


# UserAdmin 상속해야 admin 역할 가능
from video.models import VideoInfo, BookMark


class MyUserAdmin(UserAdmin):
    pass


admin.site.register(MyUser, MyUserAdmin)
admin.site.register(VideoInfo)
admin.site.register(BookMark)
