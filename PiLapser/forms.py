from django import forms

class totalImages(forms.Form):
    total_images = forms.IntegerField(label='# of photos: ')

class stepCount(forms.Form):
    step_count = forms.IntegerField(label='# of Steps: ')