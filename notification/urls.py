from django.conf.urls import url

from notification import views


app_name = 'notification' # app namespace for url revers

urlpatterns = [
    url(r'^$', views.notifications, name='notifications'),

    url(r'^(?P<notification_id>\d+)/mark_read/$', views.mark_as_read, name='mark_read'),
    url(r'^remove_all_notifications/$', views.remove_all_notifications, name='remove_all'),
]
