from django.conf.urls import url

from question import views


app_name = 'question' #url namespace for this app

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^add_question/$', views.add_question, name = 'add_question'),
    url(r'^detail/(?P<pk>\d+)/$', views.QuestionDetail.as_view(), name='detail'),
]
