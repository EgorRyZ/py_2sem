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
    GPIO.setup(4, GPIO.IN)
    GPIO.setup(17, GPIO.OUT)
    GPIO.output(17, 1)
    while True:
        num = int(input('Enter value (-1 to exit) > 25'))
        if num == -1:
            exit()
        num2dac(num)
        print(num, "=", '%.2fV' % float(3.3 * num / 256))
        while 
        #print(GPIO.input(4))
finally:
    GPIO.output(gpio, 0)
    GPIO.cleanup(gpio)
    #GPIO.output([4, 17], 0)
    #GPIO.cleanup([4, 17])
