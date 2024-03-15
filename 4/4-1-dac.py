import RPi.GPIO as GPIO

dac = [8, 11, 7, 1, 0, 5 ,12, 6]

GPIO.setmode(GPIO.BCM)

GPIO.setup(dac, GPIO.OUT)

def dec2bin(num):
    number = [0 for i in range(len(dac))]

    d_num = num % 256

    bin_num = bin(d_num)

    i = -1
    while bin_num[i] != 'b':
        number[i] = int(bin_num[i])
        i -=1


    return number

try:
    while True:
        num = input("enter num from 0 to 255: ")
        try:
            num = int(num)
            if 0 <= num <= 255:
                GPIO.output(dac, dec2bin(num))
                voltage = float(num) / 256.0 * 3.3
                print(f"voltage: {voltage:.4} volt")
            else:
                if num < 0:
                    print("num have to be >=0....")
                elif num > 255:
                    print("num is out of range....")  
        except Exception:
            if num == "q": break
            print("U entered string....")

finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()
    print("EOP")