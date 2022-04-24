Pinouts
https://pinout.xyz/

# Instrucciones para crear una partitura
1. Crear un archivo nombredepartitura.py en el directorio ../gpio-config
2. Antes de empezar pegar las siguientes líneas de código

        import time
        import RPi.GPIO as GPIO
        from gpiofunc import play, C, D, E, F, G, A, B, C_, utilidad, interrupcion
        import gpiofunc
        gpiofunc.tempo=90

En la línea de código ´´´gpiofunc.tempo=90´´´ podemos remplazar 90 por el tempo(BPM) de la partitura real.

Notas aclaratorias:
    - El campanario sólo puede tocar una octava, es decir las notas, DO, RE, MI, FA, SOL, LA, SI y DO de segunda escala.
    [IMPORTANTE] No se pueden usar notas medias, es decir sostenidas o bemoles, sólo las naturales. (Escala de DO Mayor)
    No se pueden tocar notas consecutivas en tiempos diferentes.
    Ejemplo:


<img src="https://github.com/Heredento/sys-de-campanario/blob/main/static/img/ejemplo-partitura.png?raw=true" width="500">
  

