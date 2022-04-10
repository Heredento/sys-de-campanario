# Configuración
import RPi.GPIO as GPIO
import time 
GPIO.setwarnings(False)
GPIO.setmode (GPIO.BOARD)


# Definiciones de salidas Raspberry y sus notas
pines = [8, 10, 12, 16, 18, 22, 24, 26]
# 8: Do, 10: Re.. 26: Do mayor
tempo = 90
tps = tempo/60
conteo=range(len(pines))

C = pines[0]
D = pines[1]
E = pines[2]
F = pines[3]
G = pines[4]
A = pines[5]
B = pines[6]
C_ = pines[7]

for i in conteo: # lista pines aplica como salida en raspberry 
        GPIO.setup(pines[i], GPIO.OUT)

# Funciones de utilidad principales
def allLow(x): # 0 Logico en todos los pines de salida de notas
    for i in conteo:
        GPIO.output(pines[i], False)
    time.sleep(x)

def s(x): # x = Tipo de silencio
    if x == 1:
        y = tps*4
        time.sleep(y)
    
    elif x == 2:
        y = tps*2
        time.sleep(y)
        
    elif x == 3:
        y = tps*1
        time.sleep(y)

    elif x == 4:
        y = tps*(1/2)
        time.sleep(y)

    elif x == 5:
        y = tps*(1/4)
        time.sleep(y)
    
    elif x == 6:
        y = tps*(1/8)
        time.sleep(y)

    
    time.sleep(x)

def mt(x): # Tipo de nota (tiempo), x = redonda, blanca, negra, corchea etc..
    mH = (7/8)
    mL = (1/8)
    #Me duele que no existan los switch-case en python
    if x == 1:
        y = tps*4
        time.sleep(mH*y)
        allLow(mL*y)

    elif x == 2:
        y = tps*2
        time.sleep(mH*y)
        allLow(mL*y)

    elif x == 3:
        y = tps*1
        time.sleep(mH*y)
        allLow(mL*y)

    elif x == 4:
        y = tps*(1/2)
        time.sleep(mH*y)
        allLow(mL*y)

    elif x == 5:
        y = tps*(1/4)
        time.sleep(mH*y)
        allLow(mL*y)

    elif x == 6:
        y = tps*(1/8)
        time.sleep(mH*y)
        allLow(mL*y)

    elif x == 7:
        y = tps*(1/16)
        time.sleep(mH*y)
        allLow(mL*y)

def playNota(duracion, *argv): # Funcion para tocar x cantidad de notas + el tipo que es
    for arg in argv:
        GPIO.output(pines[i], True)
    mt(duracion)

# Funcion principal, reproduce cantidad notas, configura su tiempo e indica si es o no silencio 
def play(modo, tipo, *argv): #*argv: notas a reproducir, usar C, D, E, F.. C_ como notas.
    if (modo==0):
        s(tipo)
    elif (modo==1):
        playNota(tipo, *argv)
        



