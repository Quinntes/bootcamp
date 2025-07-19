# Soal 1
# Harga dan stok
harga_apel = 10000
harga_jeruk = 15000
harga_anggur = 20000

stok_apel = 10
stok_jeruk = 7
stok_anggur = 6

# Input jumlah Apel
while True:
    jumlah_apel = int(input('Masukkan jumlah Apel (maks 10): '))
    if jumlah_apel <= stok_apel:
        break
    print('Jumlah terlalu banyak!')

# Input jumlah Jeruk
while True:
    jml_jeruk = int(input('Masukkan jumlah Jeruk (maks 7): '))
    if jml_jeruk <= stok_jeruk:
        break
    print('Jumlah terlalu banyak!')

# Input jumlah Anggur
while True:
    jml_anggur = int(input('Masukkan jumlah Anggur (maks 6): '))
    if jml_anggur <= stok_anggur:
        break
    print('Jumlah terlalu banyak!')

# Hitung total
total_apel = jml_apel * harga_apel
total_jeruk = jml_jeruk * harga_jeruk
total_anggur = jml_anggur * harga_anggur
total = total_apel + total_jeruk + total_anggur

# Tampilkan detail
print('\nDetail Belanja:')
print(f'Apel   : {jml_apel} x {harga_apel} = {total_apel}')
print(f'Jeruk  : {jml_jeruk} x {harga_jeruk} = {total_jeruk}')
print(f'Anggur : {jml_anggur} x {harga_anggur} = {total_anggur}')
print(f'Total  : {total}')

# Proses pembayaran
while True:
    uang = int(input('\nMasukkan jumlah uang: '))
    if uang < total:
        kurang = total - uang
        print(f'Uang anda kurang sebesar {kurang}')
    else:
        kembalian = uang - total
        print('Terima kasih!')
        print(f'Uang kembali anda: {kembalian}')
        break
