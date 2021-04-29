import RPi.GPIO as GPIO
from time import sleep
from Led import *
led=Led()

from ADC import *
adc=Adc()

channel = 26
GPIO.setmode(GPIO.BCM)
GPIO.setup(channel, GPIO.IN)

def inputLow(channel):
    led.ledIndex(0x01,0,155,155)
    led.ledIndex(0x02,0,155,155)
    led.ledIndex(0x04,0,155,155)
    led.ledIndex(0x08,0,151,155)
    led.ledIndex(0x10,0,155,155)
    led.ledIndex(0x20,0,155,155)
    led.ledIndex(0x40,0,155,155)
    led.ledIndex(0x80,0,155,155)
    time.sleep(.01)

    led.ledIndex(0x01,0,0,0)
    led.ledIndex(0x02,0,0,0)
    led.ledIndex(0x04,0,0,0)
    led.ledIndex(0x08,0,0,0)
    led.ledIndex(0x10,0,0,0)
    led.ledIndex(0x20,0,0,0)
    led.ledIndex(0x40,0,0,0)
    led.ledIndex(0x80,0,0,0)
    

GPIO.add_event_detect(channel, GPIO.FALLING, callback=inputLow, bouncetime=5)

if __name__ == '__main__':
    import sys
    if len(sys.argv) < 2:
        print("Please indicate what you would like to run")
        exit()
    if sys.argv[1] == 'Dance':
        var = 0
        while True:
            if var == 0:
                print("lets party")
                var = var+ 1
            sleep(.1)
    elif sys.argv[1] == 'Volts':
            power = adc.recvADC(2)
            print("The battery voltage is " + str(power*3)+"V")
