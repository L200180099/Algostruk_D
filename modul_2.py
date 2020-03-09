#No 1
##class Pesan(object):
##
##    def __init__(self, sebuahString):
##        self.teks = sebuahString
##    def cetakIni(self):
##        print(self.teks)
##    def cetakPakaiHurufKapital(self):
##        print(str.upper(self.teks))
##    def cetakPakaiHurufKecil(self):
##        print(str.lower(str.teks))
##    def jumKar(self):
##        return len(self.teks)
##    def cetakJumlahKarakterku(self):
##        print('Kalimatku mempunyai', len(self.teks), 'karakter.')
##    def perbarui(self,stringBaru):
##        self.teks = stringBaru
##    def apakahTerkandung(self, string):
##        if string in self.teks:
##            return True
##        else:
##            return False
##    def hitungKonsonan(self):
##        kon = 0
##        x = self.teks
##        vokal = "aiueoAIUEO"
##        for i in x:
##            if i not in vokal:
##                kon += 1
##        return kon
##    def hitungVokal(self):
##        vok = 0
##        x = self.teks
##        vokal = 'aiueoAIUEO'
##        for i in x:
##            if i in vokal:
##                vok += 1
##        return vok
    
##
##class sembarangKelas(object):
##    def metodeSatu(self):
##        pass
##    def metodeSembilan(self,stringBaru):
##        pass
##


####        class Manusia(object):
####            keadaan = 'lapar'
####            def __init__(self, nama):
####                self.nama = nama
####            def ucapkanSalam(self):
####                print("Salam, namaku", self.nama)
####            def makan(self,s):
####                print("saya baru saja makan",s)
####                self.keadaan = 'kenyang'
####            def olahraga(self, s):
####                print("saya baru saja latihan", k)
####                self.keadaan = 'lapar'
####            def mengalikanDenganDua(self, s):
####                return n*2

#No 3, 4, 5
##a = input('masukkan nama:')
##b = input('masukkan nim:')
##c = input('masukkan kota tinggal:')
##d = input('masukkan uang saku:')
##e = []
##class Mahasiswa(Manusia):
##    mk =[]
##    def __init__(self, nama, NIM,kota,us):
##        self.nama = nama
##        self.NIM = NIM
##        self.kotaTinggal = kota
##        self.uangSaku = us
##    def __str__(self):
##        s = self.nama + ', NIM '+str(self.NIM) \
##            + '. Tinggal di' +self.kotaTinggal \
##            + '. uang saku Rp ' + str(self.uangSaku) \
##            + ' tiap bulannya.'
##        return s
##    def ambilNama(self):
##        return self.nama
##    def ambilNIM(self):
##        return self.uangSaku
##    def makan(self,s):
##        print("Saya baru saja makan",s,"sambil belajar.")
##        self.keadaan = 'kenyang'
##    def perbaruiKotaTinggal(self, kotaBaru):
##        self.kotaTinggal = kotaBaru
##    def ambilKotaTinggal(self):
##        return self.kotaTinggal
##    def ambilUangSaku(self):
##        return self.uangSaku
##    def TambahUangSaku(self, tambahan):
##        self.uangSaku = self.uangSaku + tambahan
##    def ambilmk(self, ambil):
##        return self.mk.append(ambil)
##    def hapusmk(self, hapus):
##        return self.mk.remove(hapus)
        
##m1 = Mahasiswa('Jamil', 234, 'Surakarta', 250000)
##m2 = Mahasiswa('Andi', 365, 'Magelang', 2750000)
##m3 = Mahasiswa('Sri', 676, 'Yogyakarta', 240000)
##m4 = Mahasiswa(a,b,c,d)
##print(m4)

##no 6
##class SiswaSMA(Manusia):
##    def __init__ (self,nama,NIM,jurusan):
##        self.nm = nama
##        self.nimm = NIM
##        self.jur = jurusan
##    
##    def __str__ (self):
##        x=self.nm+' kelas '+self.kelas+' jurusan '+self.jur
##        return x
##    
##    def ambilnama(self):
##        return self.nm
##    
##    def ambiljur(self):
##        return self.jur
##    
##    def gantijurusan(self,x):
##        self.jur = x
##    
##    def ambilk(self):
##        return self.kls
##    
##    def gantik(self,x):
##        self.kls = x
##
##x = SiswaSMA('Nadya Ayu Widya',19,'Pangkalan Bun')
##print(x.ambilnama())
##print(x.ambiljur())
##x.gantijurusan('Informatika')
##print(x.ambiljur())
##


