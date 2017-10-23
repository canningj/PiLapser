import RPi.GPIO as GPIO
from time import sleep
from subprocess import call

inProgress = True

# totalPhotos = input("Enter the number of photos: ")
# shutter = input("Shutter speed of camera: ")
# interval = input("Interval between photos: ")
# steps = input("Steps between each photo: ")
# direction = input("Move left or right (1 for left): ")

# Hardcoding values for testing purposes
totalPhotos = 3
shutter = 1
interval = 1
steps = 3
direction = 1

photosTaken = 0

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



def takePhoto():
    call(["gphoto2", "--trigger-capture"])
    print("Current photo: %s, Total Photos: %s" % (totalPhotos, photosTaken))
    sleep(int(shutter))
    if (int(direction) == '1'):
        moveForward(int(steps))
    else:
        moveBackwards(int(steps))
    sleep(int(interval))



while (inProgress):

    if (photosTaken < int(totalPhotos)):
        takePhoto()
        photosTaken += 1

    else:
        inProgress = False
        print("Sequence finished")
