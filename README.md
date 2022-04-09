# Sistema de campanario automatizado
Desarrollo de un sistema de conexión Raspberry-Arduino impulsado por lenguaje de programación C++ y Python.


## Idea
El objetivo principal es desarrollar un sistema que permita automatizar el sistema de configuración de horas cuando existen problemas de electricidad; El reloj se retrasa una cierta cantidad de minutos y deseamos que vuelva a la hora normal sin tener que hacerlo manualmente.

El objetivo secundario es desarrollar una página web que tenga la función de lectura de estados del raspberry conectado y el arduino a la vez.
La página web es un sistema de calendario y recordatorio que permite agendar acciones dentro del campanario:
    1. Tocar el campanario a horas específicas agendadas.
    2. Reproducir melodías de una octava mediante código de arduino.

La raspberry se encarga de hostear una página web local dentro de la institución, del mismo modo permite la comunicación directa con Arduino.
El arduino tiene la función de:
    1. Funcionar como controlador y protección para relés conectados a las campanas de la institución.
    2. Ser un de-multiplexor decimal de cuatro entradas a ocho salidas (máximas 15, 7 no utilizadas) que corresponden a las notas musicales

La página web debe ser  impulsada por código de Python por el módulo de Flask y otros internos. 
    Qué el código sea orientado mediante Python facilita la comunicación con el Raspberry gracias al módulo RPi como GPIO.


## Notas
    Actuamente en desarrollo.
    Usuario en aprendizaje!
    No sé cómo usar Github apropiadamente.