print('=== SELAMAT DATANG DI PASAR BUAH ===')

# Data buah awal
buah = [
    {'nama': 'Apel', 'stock': 10, 'harga': 10000},
    {'nama': 'Jeruk', 'stock': 8, 'harga': 12000},
    {'nama': 'Anggur', 'stock': 5, 'harga': 15000}
]

# Loop menu utama
while True:
    print('\nMenu:')
    print('1. Lihat Daftar Buah')
    print('2. Tambah Buah')
    print('3. Hapus Buah')
    print('4. Beli Buah')
    print('5. Keluar')

    pilihan = input('Pilih menu (1-5): ')

    # Lihat Daftar Buah
    if pilihan == '1':
        print('\nDaftar Buah:')
        for i in range(len(buah)):
            print(f"{i + 1}. {buah[i]['nama']} - Stok: {buah[i]['stock']}, Harga: Rp{buah[i]['harga']}")

    # Tambah Buah
    elif pilihan == '2':
        while True:
            nama_baru = input('Masukkan nama buah baru: ')
            stock_baru = int(input('Masukkan stok buah: '))
            harga_baru = int(input('Masukkan harga buah: '))
            buah.append({'nama': nama_baru, 'stock': stock_baru, 'harga': harga_baru})
            print(f"{nama_baru} berhasil ditambahkan.")

            tambah_lagi = input('Ingin menambahkan buah lain? (y/n): ')
            if tambah_lagi.lower() != 'y':
                break

    # Hapus Buah
    elif pilihan == '3':
        while True:
            print('\nDaftar Buah:')
            for i in range(len(buah)):
                print(f"{i + 1}. {buah[i]['nama']}")
            hapus = int(input('Masukkan nomor buah yang ingin dihapus: ')) - 1
            if hapus >= 0 and hapus < len(buah):
                print(f"{buah[hapus]['nama']} berhasil dihapus.")
                buah.pop(hapus)
            else:
                print("Nomor tidak valid.")
            hapus_lagi = input('Ingin menghapus buah lain? (y/n): ')
            if hapus_lagi.lower() != 'y':
                break

    # Beli Buah
    elif pilihan == '4':
        keranjang = []  # Untuk menyimpan sementara buah yang dibeli
        while True:
            print('\nDaftar Buah:')
            for i in range(len(buah)):
                print(f"{i + 1}. {buah[i]['nama']} - Stok: {buah[i]['stock']}, Harga: Rp{buah[i]['harga']}")
            
            pilih = int(input('\nMasukkan nomor buah yang ingin dibeli: ')) - 1
            if 0 <= pilih < len(buah):
                jumlah = int(input(f"Berapa banyak {buah[pilih]['nama']} yang ingin dibeli? "))
                if jumlah > 0 and jumlah <= buah[pilih]['stock']:
                    # Update stok di database utama
                    buah[pilih]['stock'] -= jumlah
                    
                    # Tambahkan ke keranjang
                    keranjang.append({
                        'nama': buah[pilih]['nama'],
                        'jumlah': jumlah,
                        'harga': buah[pilih]['harga']
                    })
                    print(f"{jumlah} {buah[pilih]['nama']} telah ditambahkan ke keranjang")
                else:
                    print("Jumlah tidak valid atau stok tidak cukup.")
            else:
                print("Pilihan buah tidak tersedia.")

            lanjut = input("\nIngin membeli buah lain? (y/n): ")
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
                pembayaran = int(input("Masukkan jumlah uang yang dibayarkan: Rp"))
                if pembayaran >= total_harga:
                    kembalian = pembayaran - total_harga
                    print(f"Pembayaran diterima. Kembalian Anda: Rp{kembalian}")
                    break
                else:
                    print("Uang yang dibayarkan tidak cukup. Silakan masukkan jumlah yang cukup.")
        else:
            print("\nAnda belum membeli apapun")

    # Keluar
    elif pilihan == '5':
            print('Terima kasih sudah datang ke Pasar Buah!')
            break

    # Input salah
    else:
        print('Pilihan tidak valid. Silakan pilih menu 1-5.')
