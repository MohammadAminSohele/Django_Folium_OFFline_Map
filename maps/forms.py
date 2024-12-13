from django import forms

from .models import MBTiles

class CoordinatesForm(forms.Form):
    # lat=forms.FloatField(label='Latitude')
    # long=forms.FloatField(label='Longitude')
    lat=forms.FloatField(
        widget=forms.TextInput(attrs={'placeholder':'طول مختصات خود را وارد کنید','class': 'form-control'}),
        label='طول جفرافیایی'
    )
    long=forms.FloatField(
        widget=forms.TextInput(attrs={'placeholder':'عرض مختصات خود را وارد کنید','class': 'form-control'}),
        label='عرض جفرافیایی'
    )