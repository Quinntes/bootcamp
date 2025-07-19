# Diberikan data mahasiswa dalam bentuk list of tuple.
# Setiap tuple berisi: (nama, nilai)

mahasiswa = [
    ("Ani", 80),
    ("Budi", 70),
    ("Citra", 85),
    ("Dedi", 65),
    ("Eka", 90)
]

# TUGAS:
# 1. Cetak nama mahasiswa yang memiliki nilai di atas 75.
# 2. Hitung dan cetak rata-rata nilai dari semua mahasiswa.

# 1. Cetak mahasiswa dengan nilai > 75:
# for data in mahasiswa:
#     nama = data[0]
#     nilai = data[1]
#     if nilai > 76:
#         print(nama)

for nama, nilai in mahasiswa:
    if nilai > 75:
        print(nama)

# 2. Hitung rata-rata nilai mahasiswa:
list_nilai = [nilai for _, nilai in mahasiswa]
rata_rata = sum(list_nilai) / len(list_nilai)
print(list_nilai)
print(rata_rata)



