import RPi.GPIO as GPIO
from time import sleep

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)

dac = [8, 11, 7, 1, 0, 5, 12, 6]
comp = 14
troyka = 13

GPIO.setup(dac, GPIO.OUT)
GPIO.setup(troyka, GPIO.OUT, initial=GPIO.HIGH)
GPIO.setup(comp, GPIO.IN)

def dec2bin(num):
    number = [0 for i in range(len(dac))]

    d_num = num % 256

    bin_num = bin(d_num)

    i = -1
    while bin_num[i] != 'b':
        number[i] = int(bin_num[i])
        i -= 1

    return number

def adc():
    k = 0
    p = 0

    
    for i in range(len(dac)):
        pow2 = 2**(len(dac) - i - 1)

        k = p + pow2
        dac_val = dec2bin(k)
        GPIO.output(dac, dac_val)

        sleep(0.01)
        comp_val = GPIO.input(comp)

        if comp_val == 0:
            p = k
    return p

try:
    while True:
        i = adc()
        voltage = i * 3.3 / 256.0
        if i: print("{:.2f}V".format(voltage))
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")
    