#### Soal 1
numbers = [41, 5, 1, 3, 89, 32]

# Asumsikan nilai pertama sebagai min dan max
min_val = numbers[0]
max_val = numbers[0]

# Cek satu per satu
for i in numbers:
    if i < min_val:
        min_val = i
    if i > max_val:
        max_val = i

print("Numbers =", numbers)
print("Minimum value =", min_val)
print("Maximum value =", max_val)

#### Soal 2
numbers = [41, 5, 1, 3, 89, 32]

print("List Sebelum Di Sort =", numbers)

# Bubble sort manual
for i in range(len(numbers)):
    for j in range(len(numbers) - 1):
        if numbers[j] > numbers[j + 1]:
            temp = numbers[j]
            numbers[j] = numbers[j + 1]
            numbers[j + 1] = temp

print("List Setelah Di Sort =", numbers)

##### Soal 3
# Data awal
nama = ['Apel', 'Jeruk', 'Anggur']
stok = [20, 15, 25]
harga = [10000, 15000, 20000]

# Loop program
while True:
    print("\nSelamat Datang di Pasar Buah\n")
    print("List Menu :")
    print("1. Menampilkan Daftar Buah")
    print("2. Menambah Buah")
    print("3. Menghapus Buah")
    print("4. Membeli Buah")
    print("5. Exit Program")
    menu = int(input("Masukkan angka Menu yang ingin dijalankan : "))

    if menu == 1:
        print("\nDaftar Buah")
        print("Index | Nama     | Stock | Harga")
        for i in range(len(nama)):
            print(i, "   |", nama[i], " "*(8-len(nama[i])), "|", stok[i], "   |", harga[i])

    elif menu == 2:
        nama_baru = input("Masukkan nama buah: ")
        stok_baru = int(input("Masukkan stok: "))
        harga_baru = int(input("Masukkan harga: "))
        nama.append(nama_baru)
        stok.append(stok_baru)
        harga.append(harga_baru)
        print("Buah berhasil ditambahkan.")

    elif menu == 3:
        index_hapus = int(input("Masukkan index buah yang ingin dihapus: "))
        if index_hapus >= 0 and index_hapus < len(nama):
            del nama[index_hapus]
            del stok[index_hapus]
            del harga[index_hapus]
            print("Buah berhasil dihapus.")
        else:
            print("Index tidak ditemukan.")

    elif menu == 4:
        index_beli = int(input("Masukkan index buah yang ingin dibeli: "))
        jumlah_beli = int(input("Masukkan jumlah yang ingin dibeli: "))
        if index_beli >= 0 and index_beli < len(nama):
            if stok[index_beli] >= jumlah_beli:
                total = jumlah_beli * harga[index_beli]
                stok[index_beli] -= jumlah_beli
                print("Total harga =", total)
                print("Terima kasih sudah membeli", nama[index_beli])
            else:
                print("Stok tidak cukup.")
        else:
            print("Index tidak ditemukan.")

    elif menu == 5:
        print("Program selesai.")
        break

    else:
        print("Menu tidak valid.")
