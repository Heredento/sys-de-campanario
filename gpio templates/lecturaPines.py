# Configuración
import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)


pines = [8, 10, 12, 16, 18, 22, 24, 26]

GPIO.setup (11,GPIO.OUT)

#GPIO.output(11,True)

tempo = 90
tps = tempo/60



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
conteo=range(len(pines))
#constantes y funciones extra

for i in conteo:
        GPIO.setup(pines[i], GPIO.OUT)

def allLow(x):
    for i in conteo:
        GPIO.output(pines[i], False)
    time.sleep(x)
    

def t(x): # Modo de nota
    time.sleep((4/5)*x)
    allLow((1/5)*x)

def s(x): # Modo de silencio
    print("Silencio: {x}")
    time.sleep(x)

## "Partitura en código"
try:
    allLow(1)
    for y in conteo:
        GPIO.output(pines[y],True)
        print(f"PIN: {pines[y]} | Indice: {y}")
        t(redon)
    s(redon)

    print("Apagando...")
    time.sleep(1)
    GPIO.cleanup()



finally:
    GPIO.cleanup()
