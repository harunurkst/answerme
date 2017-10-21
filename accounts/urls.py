from django.conf.urls import url

from accounts import views


app_name = 'accounts' # app namespace for url revers

urlpatterns = [
    url(r'^dashboard/$', views.dashboard, name='dashboard'),
    url(r'^dashboard/edit_profile/$', views.update_profile, name='edit_profile'),
]