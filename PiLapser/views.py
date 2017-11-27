from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from .forms import timelapseFields
from multiprocessing import Process

from .piLapse import runTimelapse, moveForwards, moveBackwards, get_status

@csrf_exempt
def move_pos(request):
    if request.method == 'GET':
        print("got move_pos")
        moveForwards(50)

        return HttpResponse("Moving +...")

    else:
        return render(request, 'index.html')

def move_neg(request):
    if request.method == 'GET':
        print("got move_neg")
        moveBackwards(50)

        return HttpResponse("Moving -...")
    else:
        return render(request, 'index.html')

@csrf_exempt
def get_fields(request):
    # Process the field data if it's a POST request
    if request.method == 'POST':
        form = timelapseFields(request.POST)
        print(request.flavour)
        # check to see if user input is valid
        if form.is_valid():
            # get all the fields that have been populated on the page and print them
            length = request.POST.get('length', '')
            shutter_speed = request.POST.get('shutter_speed', '')
            total_images = request.POST.get('total_images', '')
            interval = request.POST.get('interval', '')
            direction = request.POST.get('direction', '')

            # Run the timelapse with the specified parameters

            p1 = Process(runTimelapse(int(shutter_speed), int(interval), int(length), int(total_images), direction))
            p1.start()
            p2 = Process(render(request, 'status.html'))
            p2.start()
            p1.join()
            p2.join()
            return HttpResponse("Timelapse complete")
            #return HttpResponse("New timelapse initiated... \n"
            #                    "Details: \n Moving "
            #                    + direction + length + "cm. " + "Shutter speed = "
            #                    + shutter_speed + ". Total images = " + total_images +
            #                    ".  Interval length = " + interval)

    # Otherwise, it is most likely a GET request so create the field.
    else:
        form = timelapseFields()
        print(request.flavour)

    if request.flavour == 'mobile':
        return render(request, 'piLapse_m.html', {'form': form})
    else:
        return render(request, 'piLapse.html', {'form': form})

def status(request):
    return get_status()
