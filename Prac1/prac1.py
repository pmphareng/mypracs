#!/usr/bin/python3
"""
Python Practical Template
Keegan Crankshaw
Readjust this Docstring as follows:
Names: Petersen Phihlela
Student Number: PHHPET001
Prac: Prac 1
Date: 04/07/2019
"""

# import Relevant Librares
import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
btn1 =7
btn2 =12
led1 =11
led2 =16
led3 =18
powerLed =37
GPIO.setup(btn1, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(btn2, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(led1, GPIO.OUT)
GPIO.setup(led2, GPIO.OUT)
GPIO.setup(led3, GPIO.OUT)
GPIO.setup(powerLed, GPIO.OUT)

c=0

def count_up(channel): #Count up callback
    print("Counting up")
    global c

    c = (c+1)%8 
    
    # Bit shift to power the LEDs
    GPIO.output(led1, (c>>0) & 1)
    GPIO.output(led2, (c>>1) & 1)
    GPIO.output(led3, (c>>2) & 1)

def count_down(channel): # Count down callback 
    print("Counting down")
    global c
    
    c = (c-1)%8
    
    # Bit shift 
    GPIO.output(led1, (c>>0) & 1)
    GPIO.output(led2, (c>>1) & 1)
    GPIO.output(led3, (c>>2) & 1)

GPIO.add_event_detect(7, GPIO.FALLING,  callback=count_up, bouncetime=200)
GPIO.add_event_detect(12, GPIO.FALLING, callback=count_down, bouncetime=200)

# Logic that you write
def main():
    GPIO.output(powerLed, True)
    #GPIO.output(led1, False)
    #GPIO.output(led2,False)
    #GPIO.output(led3, False)

# Only run the functions if 
if __name__ == "__main__":
    # Make sure the GPIO is stopped correctly
    try:
        while True:
            main()
    except KeyboardInterrupt:
        print("Exiting gracefully")
        # Turn off your GPIOs here
        GPIO.cleanup()
    except e:
        GPIO.cleanup()
        print("Some other error occurred")
        print(e.message)
