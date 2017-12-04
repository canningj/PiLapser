from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class timelapseFields(forms.Form):
    total_images = forms.IntegerField(label='Number of Photos: ')
    length = forms.IntegerField(label='Length of Movement (cm): ')
    interval = forms.IntegerField(label='Interval between photos: ')
