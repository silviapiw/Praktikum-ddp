# membuat list dengan menggunakan kurung siku
buah = ["Mangga","Melon","Anggur","Jeruk"]

# untuk mengaksesnya menggunakan indeks
# indeks dimulai dari 0
print(buah[0])

# menambah list dengan append()
buah.append("Semangka")
print(buah)

# mengubah list
buah[1] = "Duku"
print(buah)

# menghapus list dengan del 
del buah[1]
print(buah)

# mengambil data terakhir sekaligus menghapus dengan pop()
print(buah.pop())

# mengetahui jumlah data dengan fungsi len()
print(len(buah))

# menyisipkan data sesuai indeks yang diinginkan
buah.insert(1,"Duku")
print(buah)

# mengambil seluruh data dari list menggunakan perulangan for
for i in buah: #["Mangga","Melon","Anggur","Jeruk"]
    # aksi yang akan dilakukan
    print("Buah",i)

# soal
# List makanan dengan 2 dimensi
List_makanan = [
    ["Bakwan","Tempe","Tahu"],
    ["Nasi Uduk","Nasi Pecel","Sate Padang"]
]

# print nasi pecel
print(List_makanan[1][1])

# print tahu
print(List_makanan[0][2])

# mengeluarkan data list didalam list
for i in List_makanan[0]:
    print("List Makanan",i)
for i in List_makanan[1]:
    print(i)

for makanan in List_makanan:
    # aksi untuk for pertama
    for detail_makanan in makanan:
        # aksi untuk for kedua
        print(detail_makanan)

# hanya print index 1
for index1 in List_makanan[1]:
    print(index1)