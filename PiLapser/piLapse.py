import RPi.GPIO as GPIO
from time import sleep
from subprocess import call

# Initialize the GPIO pins and stepper coils for movement
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

enable_pin = 18
coil_A_1_pin = 4
coil_A_2_pin = 17
coil_B_1_pin = 23
coil_B_2_pin = 24

coilSeq1 = [1, 0, 1, 0]
coilSeq2 = [0, 1, 1, 0]
coilSeq3 = [0, 1, 0, 1]
coilSeq4 = [1, 0, 0, 1]

GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)
GPIO.output(enable_pin, 1)

global status
status = "Timelapse not started yet."

def moveStepper(coilSequence):
    A1 = coilSequence[0]
    A2 = coilSequence[1]
    B1 = coilSequence[2]
    B2 = coilSequence[3]

    GPIO.output(coil_A_1_pin, A1)
    GPIO.output(coil_A_2_pin, A2)
    GPIO.output(coil_B_1_pin, B1)
    GPIO.output(coil_B_2_pin, B2)

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


def takePhoto(steps, shutter, direction):
    #call(["gphoto2", "--trigger-capture"])
    sleep(int(shutter))
    if (direction == '+'):
        moveForwards(int(steps))
    else:
        moveBackwards(int(steps))

def runTimelapse(shutter, interval, length, totalPhotos, direction):
    global status
    photosTaken = 0
    distance = length * 12
    steps = distance / totalPhotos
    for i in range(0, totalPhotos):
        takePhoto(steps, shutter, direction)
        status = "Photo's taken: %s, Photos Remaining: %s" % (i, (photosTaken - i))
        sleep(int(interval))
        photosTaken += 1

    print("Timelapse completed.")


def get_status():
    return status

