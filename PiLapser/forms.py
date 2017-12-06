from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class timelapseFields(forms.Form):
    total_images = forms.IntegerField(label='Number of Photos: ')
    length = forms.IntegerField(label='Length of Movement (cm): ')
    interval = forms.IntegerField(label='Interval between photos: ')

    def clean_interval(self):
        interval = self.cleaned_data.get('interval', '')

        if interval < 1:
            raise forms.ValidationError("There must be at least a 1 second interval.")

    def clean_total_images(self):
        total_images = self.cleaned_data.get('total_images', '')

        if total_images < 2:
            raise forms.ValidationError("There must be at least 2 photos in the timelapse.")