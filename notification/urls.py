from django.conf.urls import url

from notification import views


app_name = 'notification' # app namespace for url revers

urlpatterns = [
    url(r'^(?P<notification_id>\d+)/mark_read/$', views.mark_as_read, name='mark_read'),
    url(r'^(?P<notification_id>\d+)/mark_unread/$', views.mark_as_unread, name='mark_unread'),
]
