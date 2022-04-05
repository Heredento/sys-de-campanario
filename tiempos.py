import time
bps=2

def bpm(x):
    bps = x / 60
    return bps

class t:
    def redonda(i):
        for a in range(i):
            time.sleep(bps)

    def blanca(i):
        time.sleep(bps / 2)

    def negra(i):
        time.sleep(bps / 4)

    def corchea(i):
        time.sleep(bps / 16)

    def semicorchea(i):
        time.sleep(bps / 32)

    def fusa(i):
        time.sleep(bps / 64)

    def semifusa(i):
        time.sleep(bps / 128)

ti=5
bpm(60)
print(f"BPM: {bps*60}")
for i in range(ti):
    t.redonda(ti)
    print(f"Repeticion de redonda: {i+1}")
    print(bps)