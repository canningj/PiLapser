from django import forms
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _

class timelapseFields(forms.Form):
    total_images = forms.IntegerField(label='Number of Photos: ')
    length = forms.IntegerField(label='Length of Movement (cm): ')
    interval = forms.IntegerField(label='Interval between photos: ')
    shutter_speed = forms.IntegerField(label='Shutter speed of camera')
    direction = forms.CharField(label='Direction (+ or =')

    def field_validation(self):
        length = self.cleaned_data['length']
        direction = self.cleaned_data['direction']

        if length > 70:
            raise ValidationError(_('Length cannot exceed the length of the slider (70cm)'))

        if direction != ('+' or '-'):
            raise ValidationError(_('Direction must be "+" or "-"'))

        return length, direction

