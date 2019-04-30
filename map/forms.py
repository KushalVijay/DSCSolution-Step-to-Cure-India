from django import forms
from .models import City

class Searchform(forms.ModelForm):

    class Meta:
        model = City
        fields = ['place_name']

    def clean(self):
        place_name = self.cleaned_data.get('place_name')

        data = self.cleaned_data
        return data
