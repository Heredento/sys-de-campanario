import time
from gpiofunc import play, C, D, E, F, G, A, B, C_

try:
    print(f"Empenzando script midi")
    time.sleep(3)
    play(1, 4, E)
    play(1, 4, G)
    play(1, 4, A)
    play(1, 4, C_)
    play(1, 5, B)
    play(1, 5, A)
    play(1, 4, G)
    play(1, 3, A)

    for i in range(6):
        print(f"Terminando en {i}")
        time.sleep(1)
    GPIO.cleanup()
finally:
    GPIO.cleanup()


