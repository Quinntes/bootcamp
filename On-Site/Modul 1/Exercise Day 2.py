# Soal 1
# Cara 1
# Menggunakan input untuk menentukan bilangan genap atau ganjil
angka = int(input('Masukkan angka:'))
if angka % 2 == 0:
    print('genap')
else:
    print('ganjil')

# cara 2
# Menggunakan f-string
angka = int(input('<masukkan angka:'))
print(f'Angka {angka} adalah {'genap' if angka % 2 == 0 else 'ganjil'}')

#Soal 2
massa = float(input('Masukkan massa (kg):'))
tinggi_cm = float(input('Masukkan tinggi (cm):'))

# #Konversi tinggi dari cm ke m
tinggi_m = tinggi_cm / 100
IMT = massa / tinggi_m**2

# # Cetak hasil IMT
print(f'\nmassa {massa} kg dan tinggi {tinggi_m} m')
print(f'IMT = {IMT}, ', end='')

# # Kondisi untuk menentukan kategori berat badan
if IMT < 18.5:
    print('berat badan kurang')
elif 18.5 <= IMT < 25:
    print('berat badan ideal')
elif 25 <= IMT < 30:
    print('berat badan berlebih')
elif 30 <= IMT < 40:
    print('berat badan sangat berlebih')
else:
    print('obesitas')

# Soal 3
# Harga buah per buah
harga_apel = 10000
harga_jeruk = 15000
harga_anggur = 20000

# Input jumlah buah dari user
jumlah_apel = int(input('Masukkan Jumlah Apel : '))
jumlah_jeruk = int(input('Masukkan Jumlah Jeruk : '))
jumlah_anggur = int(input('Masukkan Jumlah Anggur : '))

# Hitung total harga masing-masing
total_apel = jumlah_apel * harga_apel
total_jeruk = jumlah_jeruk * harga_jeruk
total_anggur = jumlah_anggur * harga_anggur

# Hitung total keseluruhan
total = total_apel + total_jeruk + total_anggur

# Cetak detail belanja
print("\nDetail Belanja")
print(f"Apel : {jumlah_apel} x {harga_apel} = {total_apel}")
print(f"Jeruk : {jumlah_jeruk} x {harga_jeruk} = {total_jeruk}")
print(f"Anggur : {jumlah_anggur} x {harga_anggur} = {total_anggur}")
print(f"Total : {total}")

# Input jumlah uang dari user
uang = int(input("\nMasukkan jumlah uang : "))

# Logika kondisi pembayaran
if uang < total:
    kekurangan = total - uang
    print(f"Transaksi anda dibatalkan, uangnya kurang sebesar {kekurangan}")
elif uang == total:
    print("Terima kasih")
else:  # uang > total
    kembalian = uang - total
    print("Terima kasih")
    print(f"Uang kembali anda : {kembalian}")