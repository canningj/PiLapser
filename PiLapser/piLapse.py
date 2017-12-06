import RPi.GPIO as GPIO
from time import sleep
from subprocess import call

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Set which GPIO pins to use
enable_pin = 18
coil_A_1_pin = 4
coil_A_2_pin = 17
coil_B_1_pin = 23
coil_B_2_pin = 24

# Set the coil powering sequences
coilSeq1 = [1, 0, 1, 0]
coilSeq2 = [0, 1, 1, 0]
coilSeq3 = [0, 1, 0, 1]
coilSeq4 = [1, 0, 0, 1]

# Set up GPIO channels for usage
GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
GPIO.output(enable_pin, 1)

# Global variables for storing the current status and cancel boolean
global status, cancel

# Set an initial status and cancel value
status = "Timelapse not started yet."
cancel = False

# Move the stepper by passing in each coil sequence for powering
def moveStepper(coilSequence):
    A1 = coilSequence[0]
    A2 = coilSequence[1]
    B1 = coilSequence[2]
    B2 = coilSequence[3]

    GPIO.output(coil_A_1_pin, A1)
    GPIO.output(coil_A_2_pin, A2)
    GPIO.output(coil_B_1_pin, B1)
    GPIO.output(coil_B_2_pin, B2)

# Move the camera forwards (+)
# Parameter: Amount of steps to move
def moveForwards(steps):
    for i in range(0, steps):
        moveStepper(coilSeq1)
        sleep(0.009)
        moveStepper(coilSeq2)
        sleep(0.009)
        moveStepper(coilSeq3)
        sleep(0.009)
        moveStepper(coilSeq4)
        sleep(0.009)

# Move the camera backwards (-)
# Parameter: Amount of steps to move
def moveBackwards(steps):
    for i in range(0, steps):
        moveStepper(coilSeq4)
        sleep(0.009)
        moveStepper(coilSeq3)
        sleep(0.009)
        moveStepper(coilSeq2)
        sleep(0.009)
        moveStepper(coilSeq1)
        sleep(0.009)

# Begin a new timelapse with the form data passed in by Django
# Parameters: Photo interval, length of movements, total # of photos
def runTimelapse(interval, length, totalPhotos):
    global status, cancel
    # Set cancel to false in case a timelapse had been cancelled previously
    cancel = False
    photosTaken = 0

    # Determine which direction to move depending on length value
    if length < 0:
        direction = "-"
    else:
        direction = "+"

    # Use positive length value for movement
    length = abs(length)

    # 12 steps = 1cm of movement
    # Determine the amount of steps to move
    distance = length * 12

    # Calculate how many steps to move between each photo
    steps = distance / (totalPhotos-1)
    status = "Timelapse initiated."

    for i in range(1, totalPhotos):
        if (cancel == True):
            status = "Timelapse cancelled"
            return
        # Trigger camera to take photo
        call(["gphoto2", "--trigger-capture"])
        photosTaken += 1

        # Update timelapse status
        status = "Photos taken: %s, Photos Remaining: %s, Distance Moved: %s" \
                 % (i, (totalPhotos - i), ((steps*i)/12))
        sleep(1)

        # Move camera after photo has been taken
        if (direction == '+'):
            moveForwards(int(steps))
        else:
            moveBackwards(int(steps))
         # Wait for the specified amount of time
        sleep(int(interval))

    call(["gphoto2", "--trigger-capture"])
    status = "Timelapse completed."
    return

# Return the status for display on the application
def get_status():
    return status

# Cancel the current timelapse by altering the cancel boolean
def cancel_lapse():
    global cancel
    cancel = True;

