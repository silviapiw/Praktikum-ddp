# membuat dictionary menggunakan { key:value }
data_diri = {"nama" : "Silvia"}
print(data_diri["nama"])

# untuk mengakses value nya saja, menggunakan function values()
nilai = {"firda":89,"inaya":78,"fawwaz":90,"rahmah":75}

for i in nilai.values():
    print(i)

# cetak key saja menggunakan keys()
for i in nilai.keys():
    print(i)
    
# cetak key dan value menggunakan items()
for nama,skor in nilai.items():
    print(nama, ":",skor)