from django import forms
from .models import Fuel


class FuelForm(forms.ModelForm):
    class Meta:
        model = Fuel
        fields = ['name']
        widgets = {'name': forms.TextInput(attrs={'class': 'input', 'placeholder': 'Fuel Name'})}


class LocationForm(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Suburb Name'}))
    postcode = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Postcode'}))
