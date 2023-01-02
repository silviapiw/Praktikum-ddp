class Mahasiswa :
    nim = ""
    nama = ""
    rombel = ""

    def __init__(self, nim, nama, rombel):
        self.nim = nim
        self.nama = nama
        self.rombel = rombel

    def welcome (self):
        print("Hallo", self.nama, "Di STT Terpadu Nurul Fikri")

    def lulus(self, nilai):
        if(nilai > 90):
            print("Lulus")
        else:
            print("Tidak Lulus")

mhs1 = Mahasiswa("0110222136","Silvia","TI13")
#mhs1.nama = "Silvia"
#mhs1.nim = "0110222136"
#mhs1.rombel = "TI13"



print("Nama Mahasiswa :", mhs1.nama)
print("NIM            :",mhs1.nim)
print("Rombel         :", mhs1.rombel)
mhs1.lulus(91)
print(mhs1.welcome())



