from django.conf.urls import url

from tagory import views


app_name = 'tagory' # app namespace for url revers

urlpatterns = [
    url(r'^tags/$', views.all_tags, 'all_tags'),
    url(r'^categories/$', views.all_categories, 'all_categories'),
   ]
