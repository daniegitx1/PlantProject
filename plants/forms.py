# plants/forms.py

from django import forms
from .models import PlantsData


class PlantForm(forms.ModelForm):
    class Meta:
        model = PlantsData
        fields = ['id', 'name']  # Include both the 'id' and 'name' fields
        widgets = {'id': forms.HiddenInput()}  # Hide the 'id' field in the form
