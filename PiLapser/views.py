from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import timelapseFields

#from .piLapse import runTimelapse

class HomePageView(TemplateView):
    def get(self, request, **kwargs):
        return render(request, 'index.html', context=None)

@csrf_exempt
def fields(request):
    length = request.POST.get('length', '')
    shutter_speed = request.POST.get('shutter_speed', '')
    total_images = request.POST.get('total_images', '')
    interval = request.POST.get('interval', '')
    direction = request.POST.get('direction', '')

    return HttpResponse("Move " + length + "cm " + direction + ".  Shutter speed = "
                        + shutter_speed + ". Total images = " + total_images +
                        ".  Interval length : " + interval)

@csrf_exempt
def get_fields(request):
    # Process the field data if it's a POST request
    if request.method == 'POST':
        form = timelapseFields(request.POST)
        # check to see if user input is valid
        if form.is_valid():
            # get all the fields that have been populated on the page and print them
            length = request.POST.get('length', '')
            shutter_speed = request.POST.get('shutter_speed', '')
            total_images = request.POST.get('total_images', '')
            interval = request.POST.get('interval', '')
            direction = request.POST.get('direction', '')

            # Run the timelapse with the specified parameters
            # runTimelapse(shutter_speed, interval, length, total_images, direction)

            return HttpResponse("New timelapse initiated... \n"
                                "Details: \n Moving "
                                + direction + length + "cm. " + "Shutter speed = "
                                + shutter_speed + ". Total images = " + total_images +
                                ".  Interval length = " + interval)

    # Otherwise, it is most likely a GET request so create the field.
    else:
        form = timelapseFields()
        print("not working.")

    return render(request, 'piLapse.html', {'form': form})