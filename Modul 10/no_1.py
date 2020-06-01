import timeit
import random

print(" - jumlahkan_cara_1 - ")
def jumlahkan_cara_1(n):
    hasilnya = 0
    for i in range(1, n+1):
        hasilnya = hasilnya + i
        return hasilnya
        
def uji_jumlahkan_cara_1(n):
    ls=[]
    jangkauan=range(1,n+1)
    siap = "from __main__ import jumlahkan_cara_1"
    for i in jangkauan:
##        print('i = ',i) #baris ini bisa dihidupkan atau dimatikan
        t=timeit.timeit("jumlahkan_cara_1(" +str(i) +")",setup=siap,number=1)
        ls.append(t)
        print(ls)

print("==================================================================")
print(" ")
print(" - jumlahkan_cara_2 - ")

def jumlahkan_cara_2(n):
    return ( n*(n + 1) )/2

for i in range(5): # mengulang lima kali
    awal = timeit.timeit() # menandai awal kerja
    h = jumlahkan_cara_2(10000) # menjumlah 1 sampai sepuluh ribu
    akhir = timeit.timeit() # menandai akhir kerja, lalu mencetak
    print("Jumlah adalah %d, memerlukan %9.8f detik" % (h, akhir-awal))



def insertionsort(A):
    n = len(A)
    for i in range (1,n):
        nilai = A[i]
        pos = i
        while pos > 0 and nilai < A[pos-1]:
            A[pos] = A[pos-1]
            pos = pos-1
        A[pos] = nilai
        
print(" ")
print("===========================Insertion Sort=========================")
print(" - average case scenario -")

for i in range(5):
    L = list(range(3000))
    random.shuffle(L) # Mengacak posisi elemen di list
    awal = timeit.timeit()
    U = insertionsort(L)
    akhir = timeit.timeit()
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L),akhir-awal))

print("==================================================================")
print(" ")
print(" - worst case scenario - ")


for i in range(5):
    L = list(range(3000)) 
    L = L[::-1] # Membalik urutan elemen di list
    awal = timeit.timeit()
    U = insertionsort(L)
    akhir = timeit.timeit()
    print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L),akhir-awal))

print("==================================================================")
print(" ")
print(" - best case scenario - ")

for i in range(5):
    L = list(range(3000))

    awal = timeit.timeit()
    U = insertionsort(L)
    akhir = timeit.timeit()
print("Mengurutkan %d bilangan, memerlukan %8.7f detik" % (len(L),akhir-awal))


