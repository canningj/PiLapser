from django.shortcuts import render
from django.views.generic import TemplateView
from piLapse import moveForward

from .forms import totalImages

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'piLapse.html', context=None)

def get_totalImages(request):
    if request.method == 'POST':
        form = totalImages(request.POST)
        # check to see if user input is valid (if it's an integer)
        if form.is_valid():
            result = moveForward(20)
            # redirect to a status page for the timelapse sequence:
            return render(request, 'piLapse.html', {'result': result})

    else:
        form = totalImages()

    return render(request, 'piLapse.html', {'form': form})
