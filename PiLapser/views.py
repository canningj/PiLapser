from django.shortcuts import render
from django.views.generic import TemplateView
from .piLapse import moveForward

from .forms import stepCount

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

def get_stepCount(request):
    if request.method == 'POST':
        form = stepCount(request.POST)
        # check to see if user input is valid (if it's an integer)
        if form.is_valid():
            steps = request.POST.get('step_count', '')
            result = moveForward(int(steps))
            # redirect to a status page for the timelapse sequence:
            return render(request, 'index.html', {'result': result})

    else:
        form = stepCount()

    return render(request, 'piLapse.html', {'form': form})
