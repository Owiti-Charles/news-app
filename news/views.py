from django.shortcuts import render, redirect
from django.http import HttpResponse, Http404
import datetime as dt

from .models import Articles


def welcome(request):
    return render(request, 'welcome.html')


def news_today(request):
    date = dt.date.today()
    news = Articles.today_news()
    print(news)
    return render(request, 'all-news/today-news.html', {"date": date, 'news': news})


def past_day_news(request, past_date):
    try:
        date = dt.datetime.strptime(past_date, '%Y-%m-%d').date()
    except ValueError:
        raise Http404()
        assert False
    if date == dt.date.today():
        return redirect(news_today())
    news = Articles.days_news()
    return render(request, 'all-news/past-news.html', {"date": date, 'news': news})


def search_results(request):
    pass
