from django import forms

class totalImages(forms.Form):
    total_images = forms.IntegerField(label='# of photos: ', name="totalImages")
