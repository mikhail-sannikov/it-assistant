from django.forms import ModelForm
from django import forms

from .models import UserThemeData


class AddSummary(ModelForm):
    class Meta:
        model = UserThemeData
        fields = ('summary', 'passed_theme')
        widgets = {
            'summary': forms.Textarea({'cols': 80, 'rows': 8}),
        }
