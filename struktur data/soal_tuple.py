# data tuple tidak dapat diubah (imutable)
# soal

gorengan = ("Bakwan","Combro","Misro")          # index 0
sop = ("Sop Iga","Sop Buntut","Sop Kaki")       # index 1
nasi = ("Nasi Uduk","Nasi Goreng","Nasi Rames") # index 2

# tuple di dalam tuple
makanan = (gorengan,sop,nasi)

# cetak gorengan
print(makanan[0])

for i in makanan[0]:
    print(i)

# cetak sop buntut
print(makanan[1][1])

# cetak nasi rames
print(makanan[2][2])

# cetak semuanya dan keluarkan 
for i in makanan:
    for detail in i:
        print(detail)

