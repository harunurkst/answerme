from django.conf.urls import url

from question import views
from allauth.account import views as allauth_views

app_name = 'question' # app namespace for url revers

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_question/$', views.add_question, name = 'add_question'),
    url(r'^detail/(?P<pk>\d+)/$', views.question_detail, name='detail'),

    url(r'^subscribe/(?P<question_id>\d+)/', views.subscribe_question, name='subscribe'),
    url(r'^unsubscribe/(?P<question_id>\d+)/', views.unsubscribe_question, name='unsubscribe'),

    url(r'^accounts/login/home/', views.Name, name='home'),
    url(r"^accounts/login/$", allauth_views.login, name="account_login"),
    url(r"^accounts/logout/$", allauth_views.logout, name="account_logout"),
    url(r"facebook/", views.FacebookLogin, name='FacebookLogin'),
]
