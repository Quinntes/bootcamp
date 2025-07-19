# Code Completion

# == Program Manajemen Koleksi Film Favorit ==
# Tujuan: menyimpan dan menampilkan informasi film yang dimiliki pengguna


"""
============= Deskripsi Singkat Program =============

Program ini membantu pengguna mencatat daftar film favorit mereka, termasuk informasi:
- Judul
- Genre
- Tahun rilis

Data akan disimpan dalam sebuah list of dictionaries, dan peserta diminta melengkapi fungsi-fungsi utama seperti:
- Menambahkan film
- Menampilkan seluruh film
- Menampilkan film berdasarkan genre tertentu
"""


# List untuk menyimpan koleksi film (setiap film disimpan dalam dictionary)
koleksi_film = []

print("=== Selamat Datang di Program Koleksi Film ===")

# Program berjalan hingga pengguna memilih keluar
while True:
    print("\nMenu:")
    print("1. Tambah Film")
    print("2. Tampilkan Semua Film")
    print("3. Cari Film Berdasarkan Genre")
    print("4. Keluar")

    pilihan = input("Masukkan pilihan (1-4): ")

    if ...:
        print("\n== Tambah Film Baru ==")
        judul = input("Judul film: ")
        genre = input("Genre film: ")
        tahun = input("Tahun rilis: ")

        # TODO: Buat dictionary untuk menyimpan data film
        film_baru = {
            'judul': judul,
            'genre': genre,
            'tahun': tahun
        }

        # TODO: Tambahkan dictionary ke dalam koleksi_film
        koleksi_film.append(film_baru)
        print("Film berhasil ditambahkan!")

    elif pilihan == '2':
        print("\n== Daftar Koleksi Film ==")

        # TODO: Cek apakah koleksi kosong
        if len(koleksi_film) == 0:
            print("Belum ada film dalam koleksi.")
        else:
            print("Jumlah film:", len(koleksi_film))
            print("Berikut daftar film:")
            # TODO: Gunakan loop untuk menampilkan semua film
            # Format: "Judul (Genre, Tahun)"
            for film in koleksi_film:
                print(f"{film['judul']} ({film['genre']}, {film['tahun']})")

    elif pilihan == '3':
        print("\n== Cari Film Berdasarkan Genre ==")
        cari_genre = input("Masukkan genre yang ingin dicari: ").lower()
        ditemukan = False

        # TODO: Loop untuk mencari film dengan genre yang sesuai
        for film in koleksi_film:
            if film['genre'].lower() == cari_genre:
                print(f"{film['judul']} ({film['genre']}, {film['tahun']})")
                ditemukan = True

        if not ditemukan:
            print("Tidak ada film dengan genre tersebut.")

    elif ...:
        print("\nTerima kasih telah menggunakan program ini!")
        break

    else:
        print("Pilihan tidak valid. Silakan pilih 1 - 4.")
