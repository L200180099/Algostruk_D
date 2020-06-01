##Nomor 1
##def cetakSiku(x):
##    for i in range(x):
##        for j in range(i+1):
##            print("*",end="")
##        print()

##Nomor 2
##def persegi(x,y):
##   for i in range(x):
##      if i==0 or i==x-1:
##             print("@"*y)
##      else:
##        print("@"+" "*(y-2)+"@")

##Nomor 3
##def jumlahHurufVokal(s):
##    vok = "aiueo"
##    jumlah = 0
##    for i in s:
##        if i.lower() in vok:
##            jumlah += 1
##    return (len(s),jumlah)

##Nomor 4
##def jumlahHurufKonsonan(s):
##    vok = "aiueo"
##    jumlah = 0
##    for i  in s:
##        if i.lower() not in vok:
##            jumlah += 1
##    return (len(s),jumlah)

##Nomor 5
##def rerata(b):
##    jumlah = 0
##    for i in b:
##        jumlah += i
##    return jumlah/len(b)

##Nomor 6
##for i in range (2,1000):
##    d=2
##    while i%d!=0:
##        if d==(i-1):
##            print (i)
##        d=d+1

##Nomor 7
def faktorPrima(x):
    a=[]
    b=2
    while b<=x:
        if x%b==0:
            x/=b
            a.append(b)
        else:
            b+=1
    print(a)

faktorPrima(10)
faktorPrima(120)
faktorPrima(19)

##Nomor 8
##def apakahTerkandung(a,b):
##    if a in b:
##        print("True")
##    else:
##        print("False")
##
## h = 'do'
## k = 'Indonesia tanah air beta'
## apakahTerkandung(h,k)
## apakahTerkandung('pusaka',k)

##Nomor 9
##for i in range(1,100):
##    if ((i%3)==0) and ((i%5)==0):
##        print("Python UMS")
##    elif (i%3) == 0 :
##        print("Python")
##    elif (i%5) == 0 :
##        print("UMS")
##    else:
##        print(i)

##Nomor 10
##from math import sqrt as s
##def selesaikanABC(a,b,c):
##    a=float(a)
##    b=float(b)
##    c=float(c)
## 
##    D=(b**2)-(4*a*c)
##    if D>0:
##        x1=(-b+s(D))/(2*a)
##        x2=(-b-s(D))/(2*a)
##        hasil=(x1,x2)
##        print (hasil)
##    else:
##        print ("Determinannya negatif. Persamaan tidak mempunyai akar real")
##


##Nomor 11
##def apakahKabisat(x):
##    if (x % 4) == 0:
##        if (x % 100) == 0:
##            if (x % 400) == 0:
##                print ("Tahun Kabisat")
##            else:
##                print ("Bukan Tahun Kabisat")
##        else:
##            print ("Tahun Kabisat")
##    else:
##        print ("Bukan Tahun Kabisat")
##
##apakahKabisat(1896)
##apakahKabisat(1897)
##apakahKabisat(1900)
##apakahKabisat(2000)
##apakahKabisat(2004)
##apakahKabisat(2100)
##apakahKabisat(2400)

##Nomor 12
##from random import*
##
##x = randint(1, 100)
##print("saya menyimpan sebuah angka bulat antara 1 sampai 100. Coba tebak")
##while True :
##    a=int(input("masukan tebakan:>"))
##    if a<x:
##        print("tebakan anda terlalu kecil. Coba lagi")
##    elif a>x:
##        print("tebakan anda terlalu besar. Coba lagi")
##    else :
##        print("tebakan anda benar")
##        break

##Nomor 13
##def katakan(a):
##    angka=("","satu","dua","tiga","empat","lima","enam","tujuh","delapan","sembilan","sepuluh","sebelas")
##    hasil=""
##    n=int(a)
##    if n >=0 and n<=11:
##        hasil=hasil+angka[n]
##    elif n<20:
##        hasil=angka[(n%10)]+" belas"
##    elif n<100:
##        hasil=katakan(n/10)+" puluh "+katakan(n%10)
##    elif n<200:
##        hasil="seratus "+katakan(n-100)
##    elif n<1000:
##        hasil=katakan(n/100)+" ratus "+katakan(n%100)
##    elif n<2000:
##        hasil="seribu "+katakan(n-1000)
##    elif n<1000000:
##        hasil=katakan(n/1000)+" ribu "+katakan(n%1000)
##    elif n<1000000000:
##        hasil=katakan(n/1000000)+" juta "+katakan(n%1000000)
##    return hasil
##
##print(katakan(3125750))

##Nomor 14
##def formatRupiah(x):
##    a=str(x)
##    b=""
##    i = -1
##    while i>= -len(a):
##        if((i+1)%3==0 and (i+1)!=0):
##            b="."+b
##        b=a[i]+b
##        i-=1
##    return "Rp "+b
##
##print(formatRupiah(1500))
##print(formatRupiah(2560000))
