
import json
import os

from django.shortcuts import render
from django.shortcuts import redirect
from django.views.generic import FormView, CreateView
import requests
from dotenv import load_dotenv
from django.urls import reverse_lazy, reverse
from urllib.parse import urlencode
import logging
import inspect
import pprint

from .models import SearchModel
from .forms import SearchForm

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), '.env')
load_dotenv(dotenv_path)


gurume_search_api_key = os.environ['RECURIT_API_KEY']
gurume_search_url = 'http://webservice.recruit.co.jp/hotpepper/gourmet/v1/'

area_data = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'area.csv')
area_items = []
with open(area_data, 'r') as r:
    r = r.read()   
    t = r.split('\n')
    for i in t:
        area_items.append(tuple(i.split(',')))


def map_func(request):
    if request.method == 'POST':
            lat, lng = request.POST['current'].replace('　', '').replace('\r', '').replace('\n', ',').split(',')
            
            info = {
                'key': gurume_search_api_key,
                'range': request.POST['area'],
                'lat': lat,
                'lng': lng,
                'format': 'json',
                'count': 100,
                'genre': request.POST['genre'],
            }
            print(info)
            responce = requests.get(gurume_search_url, info)
            responce_json = responce.json()
            json_data = responce_json['results']['shop']
            if json_data:
                shop_data = []
                for i in json_data:
                    shop_data.append({
                        'name': i['name'],
                        'lat': i['lat'],
                        'lng': i['lng'],
                        'access': i['access'],
                        'address': i['address'],
                        'photo': i['photo']['pc']['l'],
                        'urls': i['urls']['pc'],
                    })
            else:
                redirect_url = reverse('search')
                parameter = urlencode({
                    'data_is_none': '店舗が存在しません'
                })
                url = f'{redirect_url}?{parameter}'
                return redirect(url)
    
    return render(request, 'map.html', {'shop_data': shop_data, 'center_lat': lat, 'center_lng': lng})

def search_func(request):
    form = SearchForm()
    if 'data_is_none' in request.GET:
        return render(request, 'search.html', {
            'form': form,
            'data_is_none': request.GET['data_is_none'],
            })
    logging.info(request)
    return render(request, 'search.html', {'form': form})
    
    

    
    
