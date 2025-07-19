# =====================================================
# BUAT PROGRAM
# PROGRAM MANAJEMEN INVENTARIS GUDANG
# =====================================================

# Deskripsi:
# Program ini digunakan untuk mencatat, menghitung, dan mengevaluasi
# data barang dalam gudang. Setiap barang memiliki:
# - nama barang
# - jumlah stok
# - harga per unit

# Fitur Program:
# 1. Tambah data barang:
#    - Meminta input nama, stok, dan harga barang
#    - Menyimpan ke dalam daftar inventaris

# 2. Hitung total nilai inventaris:
#    - Total = jumlah stok × harga untuk semua barang

# 3. Tampilkan barang dengan stok rendah (< 10):
#    - Menampilkan daftar barang dengan stok di bawah 10 unit

# 4. Cari barang termahal:
#    - Menentukan barang dengan harga tertinggi
#    - Gunakan fungsi `max()` dan lambda expression

# 5. Program berjalan berulang sampai pengguna memilih keluar

# Catatan penting:
# - Gunakan struktur data list of dictionary
# - Setiap fitur ditangani oleh fungsi terpisah
# - Fokus pada penggunaan fungsi, loop, input, if-else, lambda


"""Contoh output yang diharapkan

=== Menu Gudang ===
1. Tambah Barang
2. Total Nilai Inventaris
3. Tampilkan Barang Stok Rendah
4. Cari Barang Termahal
5. Keluar
Pilih menu: 1

Nama barang: Mouse
Stok barang: 8
Harga per unit: 85000
Barang 'Mouse' ditambahkan.

=== Menu Gudang ===
1. Tambah Barang
2. Total Nilai Inventaris
3. Tampilkan Barang Stok Rendah
4. Cari Barang Termahal
5. Keluar
Pilih menu: 1

Nama barang: Monitor
Stok barang: 15
Harga per unit: 1750000
Barang 'Monitor' ditambahkan.

=== Menu Gudang ===
Pilih menu: 2
Total nilai inventaris: Rp27.050.000

=== Menu Gudang ===
Pilih menu: 3
Barang dengan stok rendah (<10):
- Mouse (Stok: 8)

=== Menu Gudang ===
Pilih menu: 4
Barang termahal: Monitor (Rp1.750.000)

=== Menu Gudang ===
Pilih menu: 5
Terima kasih. Program selesai.

"""

# Buat kode anda di bawah ini

# =====================================================
# PROGRAM MANAJEMEN INVENTARIS GUDANG
# =====================================================

# Deskripsi:
# Program ini digunakan untuk mencatat, menghitung, dan mengevaluasi
# data barang dalam gudang. Setiap barang memiliki:
# - nama barang
# - jumlah stok
# - harga per unit

# Daftar inventaris
inventaris = []

def tambah_barang():
    nama_barang = input("Nama barang: ")
    stok_barang = int(input("Stok barang: "))
    harga_per_unit = int(input("Harga per unit: "))
    inventaris.append({
        'nama': nama_barang,
        'stok': stok_barang,
        'harga': harga_per_unit
    })
    print(f"Barang '{nama_barang}' ditambahkan.")

def total_nilai_inventaris():
    total = sum(item['stok'] * item['harga'] for item in inventaris)
    print(f"Total nilai inventaris: Rp{total:,}")

def tampilkan_barang_stok_rendah():
    barang_rendah = [item for item in inventaris if item['stok'] < 10]
    if barang_rendah:
        print("Barang dengan stok rendah (<10):")
        for item in barang_rendah:
            print(f"- {item['nama']} (Stok: {item['stok']})")
    else:
        print("Tidak ada barang dengan stok rendah.")

def cari_barang_termahal():
    if inventaris:
        barang_termahal = max(inventaris, key=lambda item: item['harga'])
        print(f"Barang termahal: {barang_termahal['nama']} (Rp{barang_termahal['harga']:,})")
    else:
        print("Inventaris kosong.")

def main():
    while True:
        print("\n=== Menu Gudang ===")
        print("1. Tambah Barang")
        print("2. Total Nilai Inventaris")
        print("3. Tampilkan Barang Stok Rendah")
        print("4. Cari Barang Termahal")
        print("5. Keluar")
        pilihan = input("Pilih menu: ")

        if pilihan == '1':
            tambah_barang()
        elif pilihan == '2':
            total_nilai_inventaris()
        elif pilihan == '3':
            tampilkan_barang_stok_rendah()
        elif pilihan == '4':
            cari_barang_termahal()
        elif pilihan == '5':
            print("Terima kasih. Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Menjalankan program
if __name__ == "__main__":
    main()
