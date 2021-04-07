from django.db import models
import requests
import csv
import os

area_data = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'area.csv')
code_data = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'code.csv')

code_items = []
with open(code_data, 'r') as r:
    r = r.read()   
    t = r.split('\n')
    for i in t:
        code_items.append(tuple(i.split(',')))

code_items.pop()

AREA_CHOICE = (
    (1, '300m'),
    (2, '500m'),
    (3, '1000m'),
    (4, '2000m'),
    (5, '3000m'),
    )

CODE_CHOICE = tuple(code_items)

class SearchModel(models.Model):
    keyword = models.CharField(max_length=100)
    area = models.CharField(
        max_length = 100,
        choices = AREA_CHOICE,
    )
    genre = models.CharField(max_length=100, choices=CODE_CHOICE)