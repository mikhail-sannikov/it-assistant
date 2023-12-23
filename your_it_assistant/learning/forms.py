from django.forms import ModelForm

from .models import EducationalResource


class AddSummary(ModelForm):
    class Meta:
        model = EducationalResource
        fields = ('summary',)
