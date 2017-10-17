import RPi.GPIO as GPIO
import time
from subprocess import call

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

enable_pin = 18
coil_A_1_pin = 4
coil_A_2_pin = 17
coil_B_1_pin = 23
coil_B_2_pin = 24

StepCount = 4
Seq = range(0, StepCount)
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
        time.sleep(0.009)
        moveStepper(Seq[1])
        time.sleep(0.009)
        moveStepper(Seq[2])
        time.sleep(0.009)
        moveStepper(Seq[3])
        time.sleep(0.009)

def moveBackwards(steps):
    for i in range(0, steps):
        moveStepper(Seq[3])
        time.sleep(0.009)
        moveStepper(Seq[2])
        time.sleep(0.009)
        moveStepper(Seq[1])
        time.sleep(0.009)
        moveStepper(Seq[0])
        time.sleep(0.009)

while True:
  steps = raw_input("Steps forward: ")
  moveForward(int(steps))
  steps = raw_input("Steps backwards:  ")
  moveBackwards(int(steps))