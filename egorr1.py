import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
gpio = [10, 9, 11, 5, 6, 13, 19, 26]

def decToBinList(decNumber):
    i = 0
    binary = [0, 0, 0, 0, 0, 0, 0, 0]
    while i < 8:
        binary[i] = decNumber % 2
        decNumber = decNumber // 2
        i = i + 1
    return binary

def num2dac(value):
    binary = [0, 0, 0, 0, 0, 0, 0, 0]
    binary = decToBinList(value)
    GPIO.setup(gpio, GPIO.OUT)
    GPIO.output(gpio, binary)
None
try:
    while True:
        num = int(input('Enter number(-1 to exit): '))
        if num == -1:
            exit()
        num2dac(num)
finally:
    GPIO.output(gpio, 0)
    GPIO.cleanup(gpio)