from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse

#from .piLapse import moveForward

from .forms import stepCount

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

@csrf_exempt
def get_move(request):
    print(request.POST)
    dir = request.POST.get('direction','')
    return HttpResponse("we moved " + dir)

@csrf_exempt
def get_stepCount(request):
    if request.method == 'POST':
        form = stepCount(request.POST)
        # check to see if user input is valid (if it's an integer)
        if form.is_valid():
            # get all the fields that have been populated on the page and print them
            steps = request.POST.get('step_count', '')
            speed = request.POST.get('shutter_speed', '')
            images = request.POST.get('total_images', '')
            interval = request.POST.get('interval', '')
            direction = request.POST.get('direction', '')
            # result = moveForward(int(steps))
            print("Move " + steps + " steps " + direction + ".  Shutter speed = "
                  + speed + ". Total images = " + images + ".  Interval length : " + interval)
            result = "yahoo!"
            # redirect to a status page for the timelapse sequence:
            return render(request, 'index.html', {'result': result})

    else:
        form = stepCount()

    return render(request, 'piLapse.html', {'form': form})
