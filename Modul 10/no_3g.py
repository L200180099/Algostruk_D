import timeit
import matplotlib.pyplot as plt

## Ini fungsi nested loop yang akan diuji:

def no_g(n):               
    for i in range(n):
        if i % 3 == 0:
            for j in range( n // 2) :
                j += j
        elif i % 2 == 0:
            for j in range(5) :
                j += j
        else:
            for j in range(n) :
                j += j
         
## Ini fungsi pengujinya:
def uji_no_g(n):
    ls=[]
    jangkauan=range(1,n+1)
    siap = "from __main__ import no_g"
    for i in jangkauan:
##        print('i = ',i) #baris ini bisa dihidupkan atau dimatikan
        t=timeit.timeit("no_g(" +str(i) +")",setup=siap,number=1)
        ls.append(t)
    return ls

## Pemanggilan pengujian
n = 10
LS = uji_no_g(n)
## LS adalah list hasil uji kecepatan, dari n sedikit ke banyak.

## Menggambar grafik. dibawah ini saja yang diulang saat me-nyetel skala.
plt.plot(LS)    # Mem-plot hasil uji
skala=7700000   # <--------setel skala ini sesuai hasilm	u
plt.plot([x*x/skala for x in range (1,n+1)]) # Grafik x^2 untuk pembanding
plt.show()      # Tunjukkan plotnya
	
