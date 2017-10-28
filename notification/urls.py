from django.conf.urls import url

from notification import views


app_name = 'notification' # app namespace for url revers

urlpatterns = [
    url(r'^all/$', views.all_notifications, name='all_notifications'),
    url(r'^unread/$', views.unread_notifications, name='unread_notifications'),

    url(r'^(?P<notification_id>\d+)/read/$', views.read_notification, name='read_notification'),
    url(r'^(?P<notification_id>\d+)/mark_as_read/$', views.mark_as_read, name='mark_as_read'),
    url(r'^(?P<notification_id>\d+)/mark_as_unread/$', views.mark_as_unread, name='mark_as_unread'),
    url(r'^mark_as_read_all_notifications/$', views.mark_as_read_all_notifications, name='mark_as_read_all_notifications'),
]
