from django.conf.urls import url

from video import views

app_name = "video"
urlpatterns = [
    url(r'^search/$', views.search_video_view, name="search_video"),
    url(r'^search/put-box/(?P<video>.+)$', views.video_add_view, name="put-box-view"),
    url(r'^search/remove/(?P<video>.+)$', views.remove_view, name="remove-view"),
    url(r'^search/remove/(?P<video>.+)$', views.search_remove_view, name="search-remove-view"),
]


