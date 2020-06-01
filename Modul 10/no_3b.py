import timeit
import matplotlib.pyplot as plt

## Ini fungsi nested loop yang akan diuji:

def b(n):
    test = 0                    
    for i in range(n):
        for j in range(i):
            test = test + i * j
            
## Ini fungsi pengujinya:
def uji_b(n):
    ls=[]
    jangkauan=range(1,n+1)
    siap = "from __main__ import b"
    for i in jangkauan:
##        print('i = ',i) #baris ini bisa dihidupkan atau dimatikan
        t=timeit.timeit("b(" +str(i) +")",setup=siap,number=1)
        ls.append(t)
    return ls

## Pemanggilan pengujian
n = 1000
LS = uji_b(n)
## LS adalah list hasil uji kecepatan, dari n sedikit ke banyak.

## Menggambar grafik. dibawah ini saja yang diulang saat me-nyetel skala.
plt.plot(LS)    # Mem-plot hasil uji
skala=7700000   # <--------setel skala ini sesuai hasilmu
plt.plot([x*x/skala for x in range (1,n+1)]) # Grafik x^2 untuk pembanding
plt.show()      # Tunjukkan plotnya
