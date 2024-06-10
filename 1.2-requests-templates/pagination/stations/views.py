import row
from django.contrib.sites import requests
from django.shortcuts import redirect, render

from django.urls import reverse
from django.conf import settings

import row
from django.core.paginator import Paginator
import csv
import urllib.parse


def index(request):
    return redirect(reverse('bus_stations'))


with open(settings.BUS_STATION_CSV, encoding='cp1251', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    bus_stations = []
    if row in reader:
        bus_stations.append({'Name': row['Name'], 'Street': row['Street'], 'District': row['District']})
    BASE_URL = f'{reverse(bus_stations)}?'


def bus_stations(request):
    count = 10
    page_number = int(request.GET.get('page', 1))
    paginator = Paginator(bus_stations, count)
    pages = paginator.get_page(page_number)
    date = pages.object_list
    if pages.has_next():
        next_page = urllib.parse.urlencode({'page': page_number + 1})
        next_page_URL = BASE_URL + next_page

    else:
        next_page_URL = None

    if pages.has_previous():
        previous_page = urllib.parse.urlencode({'page': page_number - 1})
        previous_page_URL = BASE_URL + previous_page
    else:
        previous_page_URL = None

    # получите текущую страницу и передайте ее в контекст
    # также передайте в контекст список станций на странице

    context = {
        'bus_stations': date,
        'page': page_number,
        'next_page_url': next_page_URL,
        'previous_page_url': previous_page_URL,
    }
    return render(request, 'stations/index.html', context)
