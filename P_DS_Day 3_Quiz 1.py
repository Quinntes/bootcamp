# Code Completion
# Program Cetak Gaji Harian Bertahap

# Deskripsi
# Program ini akan meminta pengguna memasukkan jumlah hari kerja. 
# Untuk setiap hari, program menampilkan gaji harian yang tetap, lalu menghitung total gaji kumulatif. 
# Jika pada hari tertentu pengguna memasukkan "0", perhitungan berhenti menggunakan `break`.

print("=== Program Gaji Harian ===")

# TODO: Ambil input nama pegawai
# nama = ...
nama = input("Masukkan nama pegawai: ")

# TODO: Ambil jumlah hari kerja yang direncanakan
# total_hari = ...
total_hari = int(input("Masukkan jumlah hari kerja yang direncanakan: "))

print(f"Selamat datang, {nama.upper()}!")
print("Masukkan gaji harian selama bekerja.\nMasukkan 0 jika ingin berhenti lebih awal.\n")

# Inisialisasi hari dan total gaji
hari_ke = 1
total_gaji = 0

# TODO: Gunakan perulangan while untuk iterasi setiap hari
# while ...
while hari_ke <= total_hari:

    # TODO: Cetak hari ke berapa
    print(f"Hari ke-{hari_ke}: ")

    # TODO: Input gaji hari ini
    gaji_input = int(input("Masukkan gaji hari ini: "))

    # TODO: Jika input == 0, hentikan dengan break
    if gaji_input == 0:
        print("Perhitungan dihentikan lebih awal.")
        break

    # TODO: Tambahkan ke total gaji
    total_gaji += gaji_input

    # Tambah hari ke-nya
    hari_ke += 1

# TODO: Cetak hasil total gaji
print(f"Total gaji yang diterima oleh {nama.title()} adalah: Rp{total_gaji}")