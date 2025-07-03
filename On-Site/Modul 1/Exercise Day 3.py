# Soal 1
# Mencari nilai terkecil dan terbesar
number = [41, 5, 1, 3, 89, 32]
min_value = min(number)
max_value = max(number)
print('minimum value', min_value)
print('maximum value', max_value)

# Soal 2
# Mengurutkan dari kecil ke besar
## Cara 1
number.sort()
print(number)
number.reverse()
print(number)

### Cara 2
number.sort(reverse = True)
print(number)

# Soal 3
# Membuat Sistem Belanja
# Data awal buah
buah = [
    {'nama': 'Apel', 'stock': 20, 'harga': 10000},
    {'nama': 'Jeruk', 'stock': 15, 'harga': 15000},
    {'nama': 'Anggur', 'stock': 25, 'harga': 20000}
]

while True:
    print('\nSelamat Datang di Pasar Buah')
    print('\nList Menu : ')
    print('1. Menampilkan Daftar Buah')
    print('2. Menambah Buah')
    print('3. Menghapus Buah')
    print('4. Membeli Buah')
    print('5. Keluar')
    
    pilihan = input('Masukkan angka Menu yang ingin dijalankan: ')
    
    # Menu 1: Menampilkan Daftar Buah
    if pilihan == '1':
        print('\nDaftar Buah')
        print('Index | Nama | Stock | Harga')
        for i in range(len(buah)):
            print(f'{i} | {buah[i]['nama']} {buah[i]['stock']} | {buah[i]['harga']}')
    
    # Menu 2: Menambah Buah
    elif pilihan == '2':
        nama = input('Masukkan Nama Buah: ')
        stock = int(input('Masukkan Stock Buah: '))
        harga = int(input('Masukkan Harga Buah: '))
        buah.append({'nama': nama, 'stock': stock, 'harga': harga})
        print('\nDaftar Buah')
        print('Index | Nama | Stock | Harga')
        for i in range(len(buah)):
            print(f'{i} | {buah[i]['nama']} {buah[i]['stock']} | {buah[i]['harga']}')
    
    # Menu 3: Menghapus Buah
    elif pilihan == '3':
        # Tampilkan daftar buah dulu
        print('\nDaftar Buah')
        print('Index | Nama | Stock | Harga')
        for i in range(len(buah)):
            print(f'{i} | {buah[i]['nama']} {buah[i]['stock']} | {buah[i]['harga']}')
        
        index = int(input('\nMasukkan index buah yang ingin dihapus : '))
        if 0 <= index < len(buah):
            del buah[index]
            print('\nDaftar Buah')
            print('Index | Nama | Stock | Harga')
            for i in range(len(buah)):
                print(f'{i} | {buah[i]['nama']} {buah[i]['stock']} | {buah[i]['harga']}')
        else:
            print('Index tidak valid!')

    # Menu 4: Membeli Buah
    elif pilihan == '4':
        keranjang = []
        total_pembelian = 0
        beli_lagi = True
        
        while beli_lagi:
            # Menampilkan Daftar Buah
            print('\nDaftar Buah')
            print('Index | Nama | Stock | Harga')
            for i in range(len(buah)):
                print(f'{i} | {buah[i]['nama']} {buah[i]['stock']} | {buah[i]['harga']}')
            
            # Menginput index
            index = int(input('\nMasukkan index buah yang ingin dibeli : '))
            
            # Validasi index
            if index < 0 or index >= len(buah):
                print('Index tidak valid!')
                continue
            
            # Menginput jumlah
            jumlah = int(input('Masukkan jumlah yang ingin dibeli : '))
            
            # Validasi jumlah tidak boleh negatif
            if jumlah < 0:
                print('Jumlah tidak boleh negatif!')
                continue
            
            # Jika jumlah 0
            if jumlah == 0:
                print('Pembelian untuk buah ini dibatalkan')
            
            # Cek stok jika jumlah > 0
            elif jumlah > buah[index]['stock']:
                print(f'Stock tidak cukup, stock {buah[index]['nama']} tinggal {buah[index]['stock']}')
            
            # Jika jumlah > 0 dan stok cukup
            else:
                # Kurangi stok dan tambah ke keranjang
                buah[index]['stock'] -= jumlah
                keranjang.append({
                    'nama': buah[index]['nama'],
                    'qty': jumlah,
                    'harga': buah[index]['harga']
                })
                total_pembelian += jumlah
            
            # Tampilkan keranjang
            print('\nIsi Keranjang :')
            print('Nama | Qty | Harga')
            if keranjang:
                for item in keranjang:
                    print(f'{item['nama']} | {item['qty']} | {item['harga']}')
            else:
                print('Keranjang kosong')
            
            # Nanya 'Mau beli yang lain?' hanya jika ada pembelian yang berhasil
            if jumlah > 0 and jumlah <= buah[index]['stock']:
                lanjut = input('Mau beli yang lain? (ya/tidak) = ')
                if lanjut.lower() != 'ya':
                    beli_lagi = False
            # Untuk kasus jumlah 0 atau stok tidak cukup, langsung lanjut tanpa nanya
            else:
                continue
        
        # Cek apakah ada pembelian atau tidak
        if total_pembelian == 0:
            print('Tidak ada pembelian yang dilakukan')
        else:
            # Proses pembayaran
            print('\nDaftar Belanja :')
            print('Nama | Qty | Harga | Total Harga')
            total_harga = 0
            for item in keranjang:
                item_total = item['qty'] * item['harga']
                total_harga += item_total
                print(f'{item['nama']} | {item['qty']} | {item['harga']} | {item_total}')
            
            print(f'Total Yang Harus Dibayar = {total_harga}')
            while True:
                uang = int(input('Masukkan jumlah uang : '))
                
                if uang < total_harga:
                    kekurangan = total_harga - uang
                    print(f'Uang tidak cukup! Anda masih kekurangan {kekurangan}. Silakan tambahkan kekurangan tersebut.')
                else:
                    print('Terima kasih')
                    print(f'\nUang kembali anda : {uang - total_harga}')
                    break
                
    # Menu 5: Exit Program
    elif pilihan == '5':
        print('Terima kasih telah berbelanja!')
        break
    else:
        print('Pilihan tidak valid!')