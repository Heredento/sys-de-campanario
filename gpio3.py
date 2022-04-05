#import GPIO library
import RPi.GPIO as GPIO
#import time

GPIO.setwarnings(False)

#set GPIO numbering mode and define inputs
wp = 18 #working pin
rp = 16 #reading pin

GPIO.setmode(GPIO.BOARD)
GPIO.setup(wp, GPIO.OUT, initial=GPIO.LOW)
GPIO.setup(rp, GPIO.IN)

try:

    while (True):
        if GPIO.input(wp)==0:
            print("Circuito abierto!")
        else:
            print("Circuito Cerrado")

finally: #Presionando CTRL + C reproduce esta acción
    GPIO.cleanup()