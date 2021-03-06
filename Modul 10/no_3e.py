import timeit
import matplotlib.pyplot as plt

## Ini fungsi nested loop yang akan diuji:

def no_e(n):               
    for i in range(n):
        for j in range(n):
            for k in range(n) :
                m = i + j + k + 2019
         
## Ini fungsi pengujinya:
def uji_no_e(n):
    ls=[]
    jangkauan=range(1,n+1)
    siap = "from __main__ import no_e"
    for i in jangkauan:
##        print('i = ',i) #baris ini bisa dihidupkan atau dimatikan
        t=timeit.timeit("no_e(" +str(i) +")",setup=siap,number=1)
        ls.append(t)
    return ls

## Pemanggilan pengujian
n = 10
LS = uji_no_e(n)
## LS adalah list hasil uji kecepatan, dari n sedikit ke banyak.

## Menggambar grafik. dibawah ini saja yang diulang saat me-nyetel skala.
plt.plot(LS)    # Mem-plot hasil uji
skala=7700000   # <--------setel skala ini sesuai hasilmu
plt.plot([x*x/skala for x in range (1,n+1)]) # Grafik x^2 untuk pembanding
plt.show()      # Tunjukkan plotnya
	
