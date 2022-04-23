import time
import RPi.GPIO as GPIO
from gpiofunc import play, C, D, E, F, G, A, B, C_, pines, conteo

def interrupcion():
    print("Partitura interrumpida")
    GPIO.cleanup()

def utilidad():
    print("Configuración:")
    print(f"{pines}")
    print(f"C, D, E, F, G, A, B, C+")
    print(f"Empezando script midi..")

try:
    utilidad()    
    time.sleep(3)
    play(1, 4, E)
    play(1, 4, G)
    play(1, 4, A)
    play(1, 4, C_)
    play(1, 5, B)
    play(1, 5, A)
    play(1, 4, G)
    play(1, 3, A)

    time.sleep(0.1)
    for y in range(6,0):
        print(f"Terminando en {y}")
        time.sleep(1)

    GPIO.cleanup()


except KeyboardInterrupt:
    print("Partitura interrumpida")
    GPIO.cleanup()


