# Configuración
import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)
GPIO.setup (11,GPIO.OUT)

#GPIO.output(11,True)

tempo = 120
tps = tempo/60

pines = [8, 10, 12, 16, 18, 22, 24, 26]

C = pines[0]
D = pines[1]
E = pines[2]
F = pines[3]
G = pines[4]
A = pines[5]
B = pines[6]
C_ = pines[7]

sc = tps*(1/4)
redon = tps*4

#constantes y funciones extra
def allLow(x):
    for i in pines:
        GPIO.output(pines[i], False)
    time.sleep(x)
    


def t(x): # Modo de nota
    time.sleep((4/5)*x)
    allLow((1/5)*x)

def s(x): # Modo de silencio
    print("Funcion para apagar todas las salidas aquí jaja")
    time.sleep(x)

## "Partitura en código"
try:
    for y in range(3):
        allLow(1)
        print("Iniciando")

        GPIO.output(A,True)
        t(sc)
        GPIO.output(G,True)
        t(sc)
        GPIO.output(D,True)
        t(sc)
        GPIO.output(E,True)
        GPIO.output(C_,True)
        t(redon)

    time.sleep(3)
    GPIO.cleanup()



finally:
    GPIO.cleanup()
