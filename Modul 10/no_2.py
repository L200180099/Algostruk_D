import timeit
import random

def bestcase():
    print("===============================Best Case====================")
    for i in range(1):
        L = list(range(3000))
        awal = timeit.timeit()
        U = sorted(L)
        akhir = timeit.timeit()
        print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" %(len(L), akhir - awal))

# Average Case
def averagecase():
    print("===============================Average Case====================")
    for i in range(1):
        L = list(range(3000))
        random.shuffle(L)
        awal = timeit.timeit()
        U = sorted(L)
        akhir = timeit.timeit()
        print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" % (len(L), akhir - awal))

# worst case
def worstcase():
    print("===============================Worst Case====================")
    for i in range(1):
        L=list(range(3000))
        L=L[::-1]
        awal=timeit.timeit()
        U=sorted(L)
        akhir=timeit.timeit()
        print("mengurutkan %d bilangan,memerlukan waktu %8.7f detik" %(len(L), akhir - awal))


g = [13, 7, 5, 29, 19]          ## List Urut\
print("g = ", g)
g = sorted(g)
print("=========================Data urut")
print("g = ", g)
bestcase()
averagecase()
worstcase()
print("\n")

z = g[::-1]                      ## List data inputan terbalik
print("=========================Data terbalik")
print("data terbalik = ", z)
bestcase()
averagecase()
worstcase()
print("\n")

random.shuffle(g)               ## List data g acak (random shuffle)
print("=========================Data Acak")
print("data acak = ", g)
bestcase()
averagecase()
worstcase()
print("\n")



