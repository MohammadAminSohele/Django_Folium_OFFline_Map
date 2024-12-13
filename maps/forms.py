from django import forms

from .models import MBTiles

class CoordinatesForm(forms.Form):
    lat=forms.FloatField(label='Latitude')
    long=forms.FloatField(label='Longitude')