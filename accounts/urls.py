from django.conf.urls import url

from accounts import views


app_name = 'accounts' # app namespace for url revers

urlpatterns = [
    url(r'^profile/$', views.dashboard, name='profile'),
    url(r'^profile/edit/$', views.update_profile, name='edit_profile'),

    url(r'^login/$', views.user_login, name='login'),  # account/login
    url(r'^logout/$', views.user_logout, name='logout'),

]
