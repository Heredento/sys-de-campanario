import time
import datetime
x = datetime.datetime.now()
print(x)


def contarTiempo(correrFuncion):
    st = time.time()
    correrFuncion()
    et = time.time()
    tEjecucion = round(et-st, 2)
    print(f"Tiempo en función: {tEjecucion}")
    return tEjecucion

