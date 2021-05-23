from django import forms
from .models import Fuel

fuel_types = [('E10', 'E10'), ('U91', 'U91'), ('P95', 'P95'), ('P98', 'P98'), ('E95', 'E95')]

class FuelForm(forms.ModelForm):
    class Meta:
        model = Fuel
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Fuel Name'})}


class LocationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Suburb Name'}))
    postcode = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Postcode'}))
    #fuel_type = forms.CharField(label='Fuel type:', widget=forms.Select(attrs={'class': 'input'}, choices=fuel_types))
    fuel_type = forms.ChoiceField(choices=fuel_types)