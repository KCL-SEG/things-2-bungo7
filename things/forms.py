"""Forms of the project."""

from django.core.validators import MinValueValidator, MaxValueValidator
from django import forms

class ThingForm(forms.Form):
    
    name = forms.CharField(label = 'name', max_length=35)
    description = forms.CharField(widget=forms.Textarea(attrs={"maxlength":"120"}),)
    quantity = forms.IntegerField(
        label = 'quantity',
        validators=[MinValueValidator(0),MaxValueValidator(50)]
    )

    #created_at = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M:%S'], widget=forms.DateTimeInput(format='%d/%m/%Y %H:%M:%S'))

    
