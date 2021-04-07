import os

from django import forms 

from .models import SearchModel


genre_data = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'code.csv')


genre_items = []
with open(genre_data, 'r') as r:
    r = r.read()   
    t = r.split('\n')
    for i in t:
        genre_items.append(tuple(i.split(',')))
    del genre_items[-1:]


AREA_CHOICE = (
    (1, '300m'),
    (2, '500m'),
    (3, '1000m'),
    (4, '2000m'),
    (5, '3000m'),
    )

class SearchForm(forms.Form):
    genre = forms.ChoiceField(choices=tuple(genre_items))
    area = forms.ChoiceField(choices=AREA_CHOICE)

    # def __init__(self): 
    #     super().__init__(*args, **kwargs)
    #     self.fields['genre'].widget.attrs["class"] = "genre_field"

    
    
    
    
    
    
    
    
    
    # class Meta:
    #     model = SearchModel
    #     fields = ('genre', 'area')
    #     widgets = {
    #         'genre': TextInput(attrs={'class': 'genre_class'}),
    #         'area': TextInput(attrs={'class': 'area_class'}),
    #     }



