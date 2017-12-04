from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import timelapseFields
from time import sleep

from .piLapse import runTimelapse, moveForwards, moveBackwards, get_status, cancel_lapse

@csrf_exempt
def move_pos(request):
    if request.method == 'POST':
        print("got move_pos")
        moveForwards(50)

        return HttpResponse("Moving +...")

    else:
        return render(request, 'piLapse.html')

@csrf_exempt
def move_neg(request):
    if request.method == 'POST':
        print("got move_neg")
        moveBackwards(50)

        return HttpResponse("Moving -...")
    else:
        return render(request, 'piLapse.html')

@csrf_exempt
def cancel(request):
    if request.method == 'POST':
        cancel_lapse()
        return render(request, 'piLapse.html')


@csrf_exempt
def get_fields(request):
    # Process the field data if it's a POST request
    if request.method == 'POST':
        form = timelapseFields(request.POST)
        # check to see if user input is valid
        if form.is_valid():
            # get all the fields that have been populated on the page and print them
            length = request.POST.get('length', '')
            total_images = request.POST.get('total_images', '')
            interval = request.POST.get('interval', '')
            direction = request.POST.get('direction', '')

            sleep(10)
            runTimelapse(int(interval), int(length), int(total_images), direction)
            return render(request, 'completed.html')


    # Otherwise, it is most likely a GET request so create the field.
    else:
        form = timelapseFields()

    return render(request, 'piLapse.html', {'form': form})

@csrf_exempt
def status(request):
    return HttpResponse(str(get_status()))

@csrf_exempt
def render_status(request):
    return render(request, 'status.html')

@csrf_exempt
def completion(request):
    return render(request, 'completed.html')

@csrf_exempt
def camera_error(request):
    return render(request, 'camera_error.html')
