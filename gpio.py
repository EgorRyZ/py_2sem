Python 3.9.2 (tags/v3.9.2:1a79785, Feb 19 2021, 13:44:55) [MSC v.1928 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
gpio = [24, 25, 8, 7, 12, 16, 20, 21]

def lightUp(ledNumber, period):
    GPIO.setup(gpio[ledNumber], GPIO.OUT)
    GPIO.output(gpio[ledNumber], 1)
    time.sleep(period)
    GPIO.output(gpio[ledNumber], 0)
    GPIO.cleanup(gpio[ledNumber])
None

def lightUp2(ledNumber, period):
    GPIO.setup(gpio, GPIO.OUT)
    GPIO.output(gpio, 1)
    GPIO.output(gpio[ledNumber], 0)
    time.sleep(period)
    GPIO.output(gpio, 0)
    GPIO.cleanup(gpio)
None

def blink(ledNumber, blinkCount, blinkPeriod):
    i = 0
    while i < blinkCount:
        i = i + 1
        lightUp(ledNumber, blinkPeriod)
        time.sleep(blinkPeriod)
None

def runningLight(count, period):
    k = 0
    i = 0
    while i < count:
        lightUp(k, 1)
        if k == 7:
          k = -1
        i = i + 1
        k = k + 1
None

def runningDark(count, period):
    k = 0
    i = 0
    while i < count:
        lightUp2(k, 1)
        if k == 7:
          k = -1
        i = i + 1
        k = k + 1
None

def decToBinList(decNumber):
    i = 0
    binary = [0, 0, 0, 0, 0, 0, 0, 0]
    while i < 7:
        binary[i] = decNumber / (2 ** (7 - i))
        decNumber = decNumber / 2
        i = i + 1
    print binary
None

def decToBinList(decNumber):
    i = 0
    binary = [0, 0, 0, 0, 0, 0, 0, 0]
    while i < 7:
        binary[7 - i] = decNumber % 2
        decNumber = decNumber // 2
        i = i + 1
    print(binary)
None

#blink(2, 10, 1)
#runningLight(10, 1)
#runningDark(10, 1)
#decToBinList(3)
#decToBinList(3)