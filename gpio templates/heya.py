
import time

#¿Porqué no existe el SWITCH_CASE? AAAA
def tiempo(x):
    if x is 1: # Redonda
        e = 4*tps
        time.sleep(e)

    elif x is 2: # Blanca
        e = 2*tps
        time.sleep(e)

    elif x is 3: # Negra
        e = 1*tps
        time.sleep(e)

    elif x is 4: # Corchea
        e = (1/2)*tps
        time.sleep(e)

    elif x is 5: # Semicorchea
        e = (1/4)*tps
        time.sleep(e)

    elif x is 6: # Fusa
        e = (1/8)*tps
        time.sleep(e)

    elif x is 7: # Semifusa
        e = (1/16)*tps
        time.sleep(e)

def modo():
    if y is 0: # Silencio
        print("Nota apagada por x tiempo")

    elif y is 1: # Nota
        print("Nota m encendida por x tiempo")



def bpm(t):
    tps = t/60
    return tps


def f1(func):
    t = func
    time.sleep(t)
    print (f"Han pasado {t}s")



def C(d, m): #d: tipo de nota | m: si es silencio o nota
    







# time.sleep(tpb*4)
# time.sleep(tpb*2)
# time.sleep(tpb*1)
# time.sleep(tpb*(1/2))
# time.sleep(tpb*(1/4))
# time.sleep(tpb*(1/8))
# time.sleep(tpb*(1/16))
# time.sleep(tpb*(1/32))



# def f1(func):
#     def wrapper(*args, **kwargs):
#         print("Iniciado")
#         val = func(*args, **kwargs)
#         print("Terminado")
#         return val

#     return wrapper


# @f1
# def f(a, b=9):
#     print(a, b)

# @f1
# def add(x, y):
#     return x+y


# add(4, 5)
