from django.conf.urls import url, include

from . import views

urlpatterns = [
    url('^$', views.welcome, name='welcome'),
    url(r'^today/$', views.news_of_day, name='TodayNews'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$', views.past_day_news, name='pastNews')

]
