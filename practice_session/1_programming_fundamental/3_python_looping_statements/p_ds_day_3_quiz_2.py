# Debuging
# Rekap Gaji Mingguan Pegawai Shift

# Deskripsi 
# Program ini bertujuan untuk:
# 1. Meminta input nama pegawai, jumlah hari kerja, dan tarif per jam.
# 2. Untuk setiap hari, meminta input jumlah jam kerja.
# 3. Jika jam kerja == 0, hari dianggap libur → continue
# 4. Jika jam kerja > 12, program dihentikan karena overload → break
# 5. Jika jam kerja > 8 tapi ≤ 12, dianggap lembur, kelebihan jam dikali tarif 1.5×
# 6. Total gaji dihitung dan ditampilkan di akhir program

print("=== PROGRAM REKAP GAJI MINGGUAN v3 ===")

nama = input("Masukkan nama pegawai: ")
hari_kerja = int(input("Jumlah hari kerja minggu ini: "))
tarif_per_jam = int(input("Tarif per jam (contoh: 20000): "))

gaji_total = 0
hari = 1

while hari <= hari_kerja:
    print("Hari ke-", hari)
    jam_kerja = int(input("Masukkan jumlah jam kerja (0 jika libur): "))

    if jam_kerja == 0:
        print("Hari libur. Lanjut ke hari berikutnya.\n")
        hari += 1
        continue

    if jam_kerja > 12:
        print("Jam kerja melebihi batas maksimum! Program dihentikan.\n")
        break

    if jam_kerja > 8:
        lembur = jam_kerja - 8
        gaji_harian = (tarif_per_jam * 8) + (tarif_per_jam * 1.5 * lembur)
    else:
        gaji_harian = tarif_per_jam * jam_kerja

    gaji_total += gaji_harian
    hari += 1 


print("Total gaji minggu ini untuk", nama.upper(), "adalah Rp", gaji_total)
