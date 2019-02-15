from django import forms
from .models import resto

class Form(forms.ModelForm): #tampilin view form reservasi
    class Meta:
        model = resto
        fields = '__all__'