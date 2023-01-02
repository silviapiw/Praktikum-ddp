class Person:
    nama = ""
    gender = ""
    umur = 0 

    def __init__(self, nama, gender, umur):
        self.nama = nama
        self.gender = gender
        self.umur = umur
    
    def cetak (self):
        print("Nama          :", self.nama)
        print("Jenis Kelamin :", self.gender)
        print("Umur          :", self.umur)