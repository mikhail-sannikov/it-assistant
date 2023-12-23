from django.forms import ModelForm
from django import forms

from .models import Theme


class AddSummary(ModelForm):
    class Meta:
        model = Theme
        fields = ('summary', 'passed_theme')
        widgets = {
            'summary': forms.Textarea({'cols': 80, 'rows': 8}),
        }
