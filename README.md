# Sistema de campanario automatizado
Desarrollo de un sistema de conexión Raspberry-Python.


## Idea
El objetivo principal:
    Desarrollar un sistema que permita automatizar el sistema horario del reloj cuando sucedan incovenientes que vuelven los cambios de horas inevitables; El reloj se retrasa o adelanta tiempo y deseamos que vuelva a la hora normal sin tener que hacerlo manualmente.

El objetivo secundario es desarrollar una página web que permita agendar eventos y seleccionar partituras-scripts reproducibles en el campanario.

Metas:
    1. Reproducir melodías personalizadas en el campanario en horas agendadas.
    2. Desarrollar un control manual mediante la página web sin necesidad de tocar el hardware.
    3. Crear una librería para el desarrollo de partituras implementables al campanario mediante scripts.

## Instalación
En la consola instalar los paquetes presentados dentro consola:

1. RPi.GPIO: exclusivo para el control de pines en Raspberry. NO INSTALAR EN OTROS DISPOSITIVOS EXCEPTO RASPBERRY
        
        pip install RPi.GPIO

2. Flask: paquete para desarrollo web
        
        pip install Flask

3. schedule: facilita agendar eventos
        
        pip install schedule 
    
4. psycopg2: base de datos PostgreSQL implementada localmente para guardar events agendados
        
        pip install psycopg2


## Disclaimer

    El codigo se mantiene en producción y muchas plantillas de apoyo pueden ser encontradas.
    Actuamente en desarrollo.
    Usuario en aprendizaje!
    No sé cómo usar Github apropiadamente.