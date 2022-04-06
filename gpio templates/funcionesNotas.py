import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)
GPIO.setup (11,GPIO.OUT)

def tiempo_musical(t):
    # Duración de nota pulsada para evitar silencios inexistentes
    GPIO.output(11, True)
    time.sleep((7/4)*t)
    GPIO.output(11, False)
    time.sleep((1/4)*t)


def play(nota, seleccion_tiempo):
    if (nota=="C"):
        


    

def mHzClock(bpm, seleccion):
    bcs=60/bpm
    if (seleccion==1):
        t=bcs*4
        loop(t)

    elif (seleccion==2):
        t=bcs*2
        loop(t)

    elif (seleccion==3):
        t=bcs*1
        loop(t)

    elif (seleccion==4):
        t=bcs*(1/2)
        loop(t)

    elif (seleccion==5):
        t=bcs*(1/4)
        loop(t)

    elif (seleccion==0):
        print("Seleccion: 0")

    
try:
    while(True):
        

finally:
    GPIO.cleanup()

# while True:
#     GPIO.output(11,True)
#     time.sleep(2)
#     print("Encendido!")
#     GPIO.output(11,False)
#     time.sleep(2) 
#     print("Apagado!")
