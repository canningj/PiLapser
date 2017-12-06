from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .forms import timelapseFields
from .piLapse import runTimelapse, moveForwards, moveBackwards, get_status, cancel_lapse

# Move the camera in 50 steps in the positive direction
@csrf_exempt
def move_pos(request):
    if request.method == 'POST':
        print("got move_pos")
        moveForwards(50)

        return HttpResponse("Moving +...")

    else:
        return render(request, 'piLapse.html')

# Move the camera in 50 steps in the negative direction
@csrf_exempt
def move_neg(request):
    if request.method == 'POST':
        print("got move_neg")
        moveBackwards(50)

        return HttpResponse("Moving -...")
    else:
        return render(request, 'piLapse.html')

# Cancel an ongoing timelapse
@csrf_exempt
def cancel(request):
    if request.method == 'POST':
        cancel_lapse()
        return render(request, 'piLapse.html')

# Parse the data from a timelapse form when user presses submit
@csrf_exempt
def get_fields(request):
    form = timelapseFields()
    # Process the field data if it's a POST request
    if request.method == 'POST':
        form = timelapseFields(request.POST)

        # check to see if user input is valid
        if form.is_valid():
            # get all the fields that have been populated on the page
            length = request.POST.get('length', '')
            total_images = request.POST.get('total_images', '')
            interval = request.POST.get('interval', '')

            # create a timelapse with the given parameters
            runTimelapse(int(interval), int(length), int(total_images))
            # render the completed page once the timelapse is finished
            return render(request, 'completed.html')

    return render(request, 'piLapse.html', {'form': form})

# Obtain the current status of a timelapse
@csrf_exempt
def status(request):
    return HttpResponse(str(get_status()))

# Display the current status of a timelapse
@csrf_exempt
def render_status(request):
    return render(request, 'status.html')

# Render the page for timelapse completion
@csrf_exempt
def completion(request):
    return render(request, 'completed.html')

# Render the camera error page
@csrf_exempt
def camera_error(request):
    return render(request, 'camera_error.html')
