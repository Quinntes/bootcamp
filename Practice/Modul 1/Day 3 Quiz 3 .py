# Buat program
# ================================================
# PROGRAM PEMANTAUAN KONSUMSI AIR HARIAN
# ================================================

# Deskripsi:
# Program ini digunakan oleh pengguna untuk mencatat dan mengevaluasi jumlah air
# yang dikonsumsi setiap hari dalam periode pemantauan tertentu.
# Program meminta input pengguna dan mengevaluasi konsumsi air harian berdasarkan target.

# Fitur program:
# 1. Meminta input:
#    - Nama pengguna
#    - Target konsumsi air per hari (liter)
#    - Jumlah hari pemantauan

# 2. Untuk setiap hari:
#    - Meminta input konsumsi air (liter)
#    - Jika konsumsi == 0:
#        - Cetak "Hari ini kamu lupa minum, lanjut besok."
#        - Gunakan `continue` untuk melanjutkan ke hari berikutnya
#    - Jika konsumsi > 5:
#        - Cetak "Terlalu banyak konsumsi! Program dihentikan."
#        - Gunakan `break` untuk menghentikan program
#    - Jika konsumsi valid (antara 0 dan 5 liter):
#        - Jika konsumsi >= target → Cetak "Target tercapai!"
#        - Jika konsumsi < target  → Cetak "Kurang minum."

# 3. Setelah loop selesai:
#    - Hitung total konsumsi air dari hari-hari yang valid
#    - Hitung rata-rata konsumsi harian dari hari-hari valid

# 4. Tampilkan laporan ringkas (summary report) berisi:
#    - Nama pengguna
#    - Jumlah hari terpantau valid
#    - Total konsumsi air
#    - Rata-rata konsumsi per hari

# Catatan penting:
# Tidak boleh menggunakan list, tuple, atau tipe data koleksi lainnya.
# Materi terbatas pada: variabel, input, tipe data dasar, perhitungan, loop, if, break, continue


"""Contoh output yang diharapkan

=== Pemantauan Konsumsi Air Harian ===

Masukkan nama: Rina
Target konsumsi per hari (liter): 2
Jumlah hari pemantauan: 3

Hari ke-1
Masukkan konsumsi air hari ini: 2.5
Target tercapai!

Hari ke-2
Masukkan konsumsi air hari ini: 0
Hari ini kamu lupa minum, lanjut besok.

Hari ke-3
Masukkan konsumsi air hari ini: 6
Terlalu banyak konsumsi! Program dihentikan.

=== Summary Report ===
Nama: Rina
Jumlah hari terpantau: 2
Total konsumsi air: 4.0 liter
Rata-rata konsumsi: 2.0 liter/hari
"""

# Buat kode anda disini

print("=== Pemantauan Konsumsi Air Harian ===")

# Input nama pengguna
nama = input("Masukkan nama: ")

# Input target konsumsi air per hari
target_konsumsi = float(input("Target konsumsi per hari (liter): "))

# Input jumlah hari pemantauan
jumlah_hari = int(input("Jumlah hari pemantauan: "))

# Inisialisasi variabel untuk total konsumsi dan jumlah hari terpantau
total_konsumsi = 0.0
jumlah_hari_terpantau = 0

# Loop untuk setiap hari pemantauan
for hari in range(1, jumlah_hari + 1):
    print(f"\nHari ke-{hari}")
    
    # Input konsumsi air hari ini
    konsumsi = float(input("Masukkan konsumsi air hari ini (liter): "))
    
    # Jika konsumsi == 0, lanjut ke hari berikutnya
    if konsumsi == 0:
        print("Hari ini kamu lupa minum, lanjut besok.")
        continue

    # Jika konsumsi != 0, hentikan program
    if konsumsi < 0:
        print("Kurang minum!")
        break
    
    # Jika konsumsi > 5, hentikan program
    if konsumsi > 5:
        print("Terlalu banyak konsumsi! Program dihentikan.")
        break
    
    # Jika konsumsi valid, evaluasi terhadap target
    if konsumsi >= target_konsumsi:
        print("Target tercapai!")
    else:
        print("Kurang minum.")
    
    # Tambahkan konsumsi ke total dan hitung jumlah hari terpantau
    total_konsumsi += konsumsi
    jumlah_hari_terpantau += 1

# Setelah loop selesai, hitung rata-rata konsumsi
if jumlah_hari_terpantau > 0:
    rata_rata_konsumsi = total_konsumsi / jumlah_hari_terpantau
else:
    rata_rata_konsumsi = 0

# Tampilkan laporan ringkas
print("\n=== Summary Report ===")
print(f"Nama: {nama}")
print(f"Jumlah hari terpantau: {jumlah_hari_terpantau}")
print(f"Total konsumsi air: {total_konsumsi} liter")
print(f"Rata-rata konsumsi: {rata_rata_konsumsi:.2f} liter/hari")
# End of program
# ================================================
