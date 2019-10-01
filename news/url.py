from django.conf.urls import url, include

from . import views

urlpatterns = [
    url(r'^$', views.news_today, name='TodayNews'),
    url(r'^archives/(\d{4}-\d{2}-\d{2})/$', views.past_day_news, name='pastNews')
]
