# == PROGRAM KOLEKSI BUKU DIGITAL ==
# Catatan: Program ini memiliki beberapa BUG — perbaiki agar dapat berjalan dengan baik.

# Contoh Output
"""
== KOLEKSI BUKU DIGITAL ==
Masukkan jumlah buku yang ingin dicatat: 2

--- Input Buku ke-1 ---
Judul buku: Deep Work
Nama penulis: Cal Newport
Tahun terbit: 2016
Jumlah halaman: 296

--- Input Buku ke-2 ---
Judul buku: Atomic Habits
Nama penulis: James Clear
Tahun terbit: 2018
Jumlah halaman: 320

== Daftar Buku Tercatat ==
------------------------------
Judul: Deep Work
Penulis: Cal Newport
Tahun: 2016
Halaman: 296
------------------------------
Judul: Atomic Habits
Penulis: James Clear
Tahun: 2018
Halaman: 320

== Statistik Koleksi ==
Total halaman semua buku: 616
Rata-rata halaman per buku: 308
Buku tertua: 'Deep Work' (2016)
"""

print("== KOLEKSI BUKU DIGITAL ==")

buku_koleksi = []  # Menggunakan list untuk menyimpan koleksi buku

jumlah_buku = int(input("Masukkan jumlah buku yang ingin dicatat: "))

for i in range(jumlah_buku):
    print(f"\n--- Input Buku ke-{i+1} ---")
    judul = input("Judul buku: ")
    penulis = input("Nama penulis: ")
    tahun = int(input("Tahun terbit: "))
    halaman = int(input("Jumlah halaman: "))  # Mengubah input menjadi integer

    buku = {
        "judul": judul,
        "penulis": penulis,
        "tahun": tahun,
        "halaman": halaman
    }

    buku_koleksi.append(buku)  # Menggunakan append untuk menambahkan buku

# === TAMPILKAN SEMUA DATA ===
print("\n== Daftar Buku Tercatat ==")
if len(buku_koleksi) == 0:  # Memeriksa jumlah buku dengan len()
    print("Tidak ada buku.")
else:
    for data in buku_koleksi:
        print("-" * 30)
        print("Judul:", data["judul"])  # Menggunakan kunci yang benar
        print("Penulis:", data["penulis"])
        print("Tahun:", data["tahun"])
        print("Halaman:", data["halaman"])

# === Statistik Koleksi ===
print("\n== Statistik Koleksi ==")
total_halaman = 0
tahun_terlama = 9999
judul_terlama = ""

for buku in buku_koleksi:
    total_halaman += buku["halaman"]  # Menggunakan += untuk menambahkan halaman
    if buku["tahun"] < tahun_terlama:  # Menggunakan < untuk menemukan tahun terlama
        tahun_terlama = buku["tahun"]
        judul_terlama = buku["judul"]
rata_rata = total_halaman / jumlah_buku if jumlah_buku > 0 else 0  # Menghindari pembagian dengan nol 

print(f"\nTotal halaman semua buku: {total_halaman}")
print(f"Rata-rata halaman per buku: {round(rata_rata)}")
print(f"Buku tertua: '{judul_terlama}' ({tahun_terlama})")
