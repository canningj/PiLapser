import RPi.GPIO as GPIO
from time import sleep
from subprocess import call

inProgress = True

totalPhotos = input("Enter the number of photos: ")
shutter = input("Shutter speed of camera: ")
interval = input("Interval between photos: ")
steps = input("Steps between each photo: ")
direction = input("Move left or right (1 for left): ")

photosTaken = 0

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

enable_pin = 18
coil_A_1_pin = 4
coil_A_2_pin = 17
coil_B_1_pin = 23
coil_B_2_pin = 24

Seq[0] = []
Seq[0] = [1, 0, 1, 0]
Seq[1] = [0, 1, 1, 0]
Seq[2] = [0, 1, 0, 1]
Seq[3] = [1, 0, 0, 1]

GPIO.setup(enable_pin, GPIO.OUT)
GPIO.setup(coil_A_1_pin, GPIO.OUT)
GPIO.setup(coil_A_2_pin, GPIO.OUT)
GPIO.setup(coil_B_1_pin, GPIO.OUT)
GPIO.setup(coil_B_2_pin, GPIO.OUT)

GPIO.output(enable_pin, 1)

def moveStepper(coilSequence):
    A1 = coilSequence[0]
    A2 = coilSequence[1]
    B1 = coilSequence[2]
    B2 = coilSequence[3]

    GPIO.output(coil_A_1_pin, A1)
    GPIO.output(coil_A_2_pin, A2)
    GPIO.output(coil_B_1_pin, B1)
    GPIO.output(coil_B_2_pin, B2)

def moveForward(steps):
    for i in range(0, steps):
        moveStepper(Seq[0])
        sleep(0.009)
        moveStepper(Seq[1])
        sleep(0.009)
        moveStepper(Seq[2])
        sleep(0.009)
        moveStepper(Seq[3])
        sleep(0.009)

def moveBackwards(steps):
    for i in range(0, steps):
        moveStepper(Seq[3])
        sleep(0.009)
        moveStepper(Seq[2])
        sleep(0.009)
        moveStepper(Seq[1])
        sleep(0.009)
        moveStepper(Seq[0])
        sleep(0.009)


def takePhoto(photosTaken):
    #call(["gphoto2", "--trigger-capture"])
    print("Current photo: %s, Total Photos: %s" % (totalPhotos, photosTaken))
    sleep(int(shutter))
    if (int(direction) == '1'):
        moveForward(int(steps))
    else:
        moveBackwards(int(steps))
    sleep(int(interval))
    photosTaken += 1


while (inProgress):

    if (photosTaken < totalPhotos):
        takePhoto(photosTaken)

    else:
        inProgress = False
        print("Sequence finished")
