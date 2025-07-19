### Soal 1 ###

list1 = [1, 3, 4, 5]
list2 = [22, 17, 19, 20, 14]
list3 = [1, 3, 5]
list4 = [2, 4, 6]

def cek_ganjil_genap(angka):
    if angka % 2 == 0:
        return "Genap"
    else:
        return "Ganjil"

hasil1 = list(map(cek_ganjil_genap, list1))
hasil2 = list(map(cek_ganjil_genap, list2))
hasil3 = list(map(cek_ganjil_genap, list3))
hasil4 = list(map(cek_ganjil_genap, list4))

print(hasil1)
print(hasil2)
print(hasil3)
print(hasil4)


### Soal 2 ###
### Cara 1 ###
# Daftar harga
harga = [9100000, 9800000, 9500000, 10300000, 9300000]
# Filter untuk harga yang lebih tinggi dari 9.500.000
filter_harga = [h for h in harga if h >= 9500000]
# Menampilkan hasil
print("Hasil Filter:")
for h in filter_harga:
    print(h)

### Cara 2 ###
def filter_numbers(numbers, threshold):
    # Filter numbers greater than or equal to threshold
    return [num for num in numbers if num >= threshold]

# Daftar angka yang diberikan
numbers = [9100000, 9800000, 9500000, 10300000, 9300000]

# Threshold untuk filter
threshold = 9500000

# Memanggil fungsi filter
filtered_results = filter_numbers(numbers, threshold)

# Menampilkan hasil
print("Results:")
for result in filtered_results:
    print(result)

### Soal 3 ###
def tampilkan_menu():
    print('\nMenu:')
    print('1. Lihat Daftar Buah')
    print('2. Tambah Buah')
    print('3. Hapus Buah')
    print('4. Beli Buah')
    print('5. Keluar')

def lihat_daftar_buah(buah):
    print('\nDaftar Buah:')
    for i in range(len(buah)):
        print(f"{i + 1}. {buah[i]['nama']} - Stok: {buah[i]['stock']}, Harga: Rp{buah[i]['harga']}")

def tambah_buah(buah):
    while True:
        nama_baru = input('Masukkan nama buah baru: ')
        stock_baru = int(input('Masukkan stok buah: '))
        harga_baru = int(input('Masukkan harga buah: '))
        buah.append({'nama': nama_baru, 'stock': stock_baru, 'harga': harga_baru})
        print(f"{nama_baru} berhasil ditambahkan.")

        while True:
            tambah_lagi = input('Ingin menambahkan buah lain? (y/n): ')
            if tambah_lagi.lower() in ['y', 'n']:
                break
            else:
                print("Input tidak valid. Silakan masukkan 'y' untuk ya atau 'n' untuk tidak.")

        if tambah_lagi.lower() != 'y':
            break

def hapus_buah(buah):
    while True:
        lihat_daftar_buah(buah)
        while True:
            try:
                hapus = int(input('Masukkan nomor buah yang ingin dihapus: ')) - 1
                if 0 <= hapus < len(buah):
                    print(f"{buah[hapus]['nama']} berhasil dihapus.")
                    buah.pop(hapus)
                    break
                else:
                    print("Nomor tidak valid. Silakan masukkan nomor yang sesuai.")
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")

        while True:
            hapus_lagi = input('Ingin menghapus buah lain? (y/n): ')
            if hapus_lagi.lower() in ['y', 'n']:
                break
            else:
                print("Input tidak valid. Silakan masukkan 'y' untuk ya atau 'n' untuk tidak.")

        if hapus_lagi.lower() != 'y':
            break

def beli_buah(buah):
    keranjang = []
    while True:
        lihat_daftar_buah(buah)

        while True:
            try:
                pilih = int(input('\nMasukkan nomor buah yang ingin dibeli: ')) - 1
                if 0 <= pilih < len(buah):
                    break
                else:
                    print("Pilihan buah tidak tersedia. Silakan masukkan nomor yang sesuai.")
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")

        while True:
            try:
                jumlah = int(input(f"Berapa banyak {buah[pilih]['nama']} yang ingin dibeli? "))
                if jumlah > 0 and jumlah <= buah[pilih]['stock']:
                    buah[pilih]['stock'] -= jumlah
                    keranjang.append({
                        'nama': buah[pilih]['nama'],
                        'jumlah': jumlah,
                        'harga': buah[pilih]['harga']
                    })
                    print(f"{jumlah} {buah[pilih]['nama']} telah ditambahkan ke keranjang")
                    break
                else:
                    print("Jumlah tidak valid atau stok tidak cukup.")
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")

        while True:
            lanjut = input("\nIngin membeli buah lain? (y/n): ")
            if lanjut.lower() in ['y', 'n']:
                break
            else:
                print("Input tidak valid. Silakan masukkan 'y' untuk ya atau 'n' untuk tidak.")

        if lanjut.lower() != 'y':
            break

    # Proses pembayaran setelah semua dipilih
    if keranjang:
        print("\n=== RINCIAN PEMBELIAN ===")
        total_harga = 0
        for item in keranjang:
            subtotal = item['jumlah'] * item['harga']
            total_harga += subtotal
            print(f"{item['nama']} - {item['jumlah']} x Rp{item['harga']} = Rp{subtotal}")

        print(f"\nTOTAL HARGA: Rp{total_harga}")

        # Proses Pembayaran
        while True:
            try:
                pembayaran = int(input("Masukkan jumlah uang yang dibayarkan: Rp"))
                if pembayaran >= total_harga:
                    kembalian = pembayaran - total_harga
                    print(f"Pembayaran diterima. Kembalian Anda: Rp{kembalian}")
                    break
                else:
                    print("Uang yang dibayarkan tidak cukup. Silakan masukkan jumlah yang cukup.")
            except ValueError:
                print("Input tidak valid. Harap masukkan angka.")
    else:
        print("\nAnda belum membeli apapun")

def pasar_buah():
    print('=== SELAMAT DATANG DI PASAR BUAH ===')

    # Data buah awal
    buah = [
        {'nama': 'Apel', 'stock': 10, 'harga': 10000},
        {'nama': 'Jeruk', 'stock': 8, 'harga': 12000},
        {'nama': 'Anggur', 'stock': 5, 'harga': 15000}
    ]

    # Loop menu utama
    while True:
        tampilkan_menu()
        pilihan = input('Pilih menu (1-5): ')

        if pilihan == '1':
            lihat_daftar_buah(buah)

        elif pilihan == '2':
            tambah_buah(buah)

        elif pilihan == '3':
            hapus_buah(buah)

        elif pilihan == '4':
            beli_buah(buah)

        elif pilihan == '5':
            print('Terima kasih sudah datang ke Pasar Buah!')
            break

        else:
            print('Pilihan tidak valid. Silakan pilih menu 1-5.')

# Execute the main function
pasar_buah()
