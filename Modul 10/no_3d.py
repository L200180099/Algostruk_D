import timeit
import matplotlib.pyplot as plt

## Ini fungsi nested loop yang akan diuji:

def no_d(n):
    i = n
    while i > 0:
        k = 2 + 2
        i = i // 2
         
## Ini fungsi pengujinya:
def uji_no_d(n):
    ls=[]
    jangkauan=range(1,n+1)
    siap = "from __main__ import no_d"
    for i in jangkauan:
##        print('i = ',i) #baris ini bisa dihidupkan atau dimatikan
        t=timeit.timeit("no_d(" +str(i) +")",setup=siap,number=1)
        ls.append(t)
    return ls

## Pemanggilan pengujian
n = 10
LS = uji_no_d(n)
## LS adalah list hasil uji kecepatan, dari n sedikit ke banyak.

## Menggambar grafik. dibawah ini saja yang diulang saat me-nyetel skala.
plt.plot(LS)    # Mem-plot hasil uji
skala=7700000   # <--------setel skala ini sesuai hasilmu
plt.plot([x*x/skala for x in range (1,n+1)]) # Grafik x^2 untuk pembanding
plt.show()      # Tunjukkan plotnya
