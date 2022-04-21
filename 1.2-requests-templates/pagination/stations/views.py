import csv

from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.urls import reverse


def index(request):
    return redirect(reverse('bus_stations'))


def bus_stations(request):
    page_num = int(request.GET.get('page', 1))
    bus_stations_lst = []
    with open('data-398-2018-08-30.csv', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            bus_stations_lst.append(row)
    paginator = Paginator(bus_stations_lst, 10)
    first_station_on_page = 10 * (page_num-1)
    context = {
        "bus_stations": bus_stations_lst[first_station_on_page:first_station_on_page+10],
        'page': paginator.get_page(page_num),
    }
    return render(request, 'stations/index.html', context)
