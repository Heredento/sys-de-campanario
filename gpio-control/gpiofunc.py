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

for i in conteo: # funcion confifura como salida los pines en la lista 
        GPIO.setup(pines[i], GPIO.OUT)

mH = (7/8)
mL = (1/8)

# Funciones de utilidad principales
def allLow(x): # 0 Logico en todos los pines de salida de notas
    for i in conteo:
        GPIO.output(pines[i], False)
    time.sleep(x)

def s(x): # x = Tipo de silencio
    match x:
        case 0:
            pass
        case 1:
            y = tps*4
            time.sleep(y)

        case 2:
            y = tps*2
            time.sleep(y)

        case 3:
            y = tps*1
            time.sleep(y)

        case 4:
            y = tps*(1/2)
            time.sleep(y)

        case 5:
            y = tps*(1/4)
            time.sleep(y)

        case 6:
            y = tps*(1/8)
            time.sleep(y)

        case 7:
            y = tps*(1/16)
            time.sleep(y)


def mt(x): # Tipo de nota (tiempo), x = redonda, blanca, negra, corchea etc..
    
    match x:
        case 1:
            y = tps*4
            time.sleep(mH*y)
            allLow(mL*y)

        case 2:
            y = tps*2
            time.sleep(mH*y)
            allLow(mL*y)

        case 3:
            y = tps*1
            time.sleep(mH*y)
            allLow(mL*y)

        case 4:
            y = tps*(1/2)
            time.sleep(mH*y)
            allLow(mL*y)

        case 5:
            y = tps*(1/4)
            time.sleep(mH*y)
            allLow(mL*y)
        case 6:
            y = tps*(1/8)
            time.sleep(mH*y)
            allLow(mL*y)

        case 7:
            y = tps*(1/16)
            time.sleep(mH*y)
            allLow(mL*y)

def playNota(duracion, *notas): # Funcion para tocar x cantidad de notas + el tipo que es
    nota=list(notas)
    c = range(len(notas))
    for arg in c:
        GPIO.output(nota[arg], True)
    mt(duracion)

# Funcion principal, reproduce cantidad notas, configura su tiempo e indica si es o no silencio 
def play(modo=0, tipo=3, *notas): #*argv: notas a reproducir, usar C, D, E, F.. C_ como notas.
    match modo:
        case 0:
            s(tipo)
        case 1:
            playNota(tipo, *notas)
