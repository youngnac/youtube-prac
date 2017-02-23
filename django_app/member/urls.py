from django.conf.urls import url

from member import views

app_name = 'member'
urlpatterns = [
    url(r'^my-box/$', views.my_box_view, name='my-box'),
    url(r'^login/$', views.login_view, name='login'),
    url(r'^logout/$', views.logout_view, name='logout'),
    url(r'^sign-up/$', views.signup_view, name='sign-up'),
]
