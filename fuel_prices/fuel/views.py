from django.shortcuts import render
import requests
import datetime
from .forms import FuelForm, LocationForm
import sqlite3
from .models import Fuel, PostcodesGeo


# Create your views here.


def index(request):
    url = "https://api.onegov.nsw.gov.au/oauth/client_credential/accesstoken"
    querystring = {"grant_type": "client_credentials"}
    headers = {
        'content-type': "application/json",
        'authorization': "Basic YmlONmx6SUtWTkMxVjV3NW9BQWVLcllLR3J6ZmxXNkw6QTEzRERDTEs0QUdPS1ltMA=="
    }
    r = requests.request("GET", url, headers=headers, params=querystring).json()
    token = r['access_token']

    location = LocationForm()
    station_info = []
    context = {'form': location, 'station_info': station_info}
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            suburb = form.cleaned_data['name']
            postcode = form.cleaned_data['postcode']
            fuel_type = form.cleaned_data['fuel_type']
            try:
                s = PostcodesGeo.objects.get(postcode=postcode, suburb__iexact=suburb)
                url = "https://api.onegov.nsw.gov.au/FuelPriceCheck/v1/fuel/prices/nearby"
                payload = dict(fueltype=str(fuel_type), brand=[], namedlocation=postcode, latitude=str(s.latitude),
                               longitude=str(s.longitude),
                               radius="", sortby="price", sortascending="true")
                headers = {
                    'content-type': "application/json; charset=utf-8",
                    'authorization': 'Bearer ' + str(token),
                    'apikey': 'biN6lzIKVNC1V5w5oAAeKrYKGrzflW6L',
                    'transactionid': "1",
                    'requesttimestamp': str(datetime.datetime.now())
                }

                response = requests.request("POST", url, data=str(payload), headers=headers).json()
                stations = response['stations']
                prices = response['prices']
                for i in range(len(stations)):
                    info = {
                        'brand': stations[i]['brand'],
                        'name': stations[i]['name'],
                        'address': stations[i]['address'],
                        'distance': stations[i]['location']['distance'],
                        'price': prices[i]['price']
                    }
                    station_info.append(info)
            except:
                context['error'] = 'no result matches your input'
        else:
            context['error'] = 'postcode should be numeric'

    return render(request, 'fuel/fuel.html', context)
