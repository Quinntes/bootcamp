# Program CRUD - Data Pasien Rumah Sakit Hewan 

# ========================
# Bagian 1: Data Awal & Tampilan Menu
# ========================

Data_Pasien = [
    {'ID Hewan': 'H001', 'Nama Hewan': 'Birong', 'Usia': 24, 'Jenis Hewan': 'Kucing', 'Jenis Kelamin': 'Betina', 'Diagnosis': 'Cacingan'},
    {'ID Hewan': 'H002', 'Nama Hewan': 'Bagong', 'Usia': 60, 'Jenis Hewan': 'Anjing', 'Jenis Kelamin': 'Jantan', 'Diagnosis': 'Radang Tenggorokan'},
    {'ID Hewan': 'H003', 'Nama Hewan': 'Cemong', 'Usia': 12, 'Jenis Hewan': 'Kucing', 'Jenis Kelamin': 'Jantan', 'Diagnosis': 'Cacingan'},
    {'ID Hewan': 'H004', 'Nama Hewan': 'Dodo', 'Usia': 36, 'Jenis Hewan': 'Kucing', 'Jenis Kelamin': 'Jantan', 'Diagnosis': 'Luka Terbuka'},
    {'ID Hewan': 'H005', 'Nama Hewan': 'Euis', 'Usia': 18, 'Jenis Hewan': 'Anjing', 'Jenis Kelamin': 'Betina', 'Diagnosis': 'Radang Tenggorokan'},
    {'ID Hewan': 'H006', 'Nama Hewan': 'Fufu', 'Usia': 6, 'Jenis Hewan': 'Kelinci', 'Jenis Kelamin': 'Betina', 'Diagnosis': 'Pencernaan'},
    {'ID Hewan': 'H007', 'Nama Hewan': 'Gogo', 'Usia': 8, 'Jenis Hewan': 'Kelinci', 'Jenis Kelamin': 'Jantan', 'Diagnosis': 'Pencernaan'},
    {'ID Hewan': 'H008', 'Nama Hewan': 'Hera', 'Usia': 20, 'Jenis Hewan': 'Kucing', 'Jenis Kelamin': 'Betina', 'Diagnosis': 'Cacingan'},
    {'ID Hewan': 'H009', 'Nama Hewan': 'Iro', 'Usia': 30, 'Jenis Hewan': 'Anjing', 'Jenis Kelamin': 'Jantan', 'Diagnosis': 'Kulit Gatal'}
]

def Tampilkan_Menu():
    '''
    Menampilkan pilihan menu utama CRUD.
    Memudahkan pengguna untuk memilih fitur Report, Tambah, Ubah, Hapus, atau Keluar.
    '''
    print('\n============= Data Pasien Rumah Sakit Hewan =============')
    print('1. Report Data Hewan')
    print('2. Menambahkan Data Hewan')
    print('3. Mengubah Data Hewan')
    print('4. Menghapus Data Hewan')
    print('5. Exit')

# ========================
# Bagian 2: Fungsi-Fungsi Bantuan
# ========================

def Format_Usia_Tampil(total_bulan):
    '''
      Mengonversi total bulan usia menjadi format teks seperti:
    - 8 bulan -> '8 bulan'
    - 24 bulan -> '2 tahun'
    - 27 bulan -> '2 tahun 3 bulan'
    '''
    if total_bulan < 0:
        return 'Usia tidak valid'
    if total_bulan < 12:
        return f'{total_bulan} bulan'
    else:
        tahun = total_bulan // 12
        bulan = total_bulan % 12
        if bulan == 0:
            return f'{tahun} tahun'
        else:
            return f'{tahun} tahun {bulan} bulan'

def Tampilkan_Tabel(list_data):
    '''
    MMenampilkan data hewan dalam format tabel dengan lebar kolom diagnosis.
    '''
    if not list_data:
        print('\n**** Tidak Ada Data Untuk Ditampilkan ****')
        return False
    
    # Menghitung lebar maksimum yang dibutuhkan untuk kolom diagnosis
    lebar_diagnosis = len('Diagnosis') # Lebar minimum adalah judulnya sendiri
    for hewan in list_data:
        if len(hewan['Diagnosis']) > lebar_diagnosis:
            lebar_diagnosis = len(hewan['Diagnosis'])

    # Menghitung total lebar tabel secara dinamis
    total_lebar = 10 + 15 + 15 + 15 + 13 + lebar_diagnosis + 15 # Tambahan spasi pemisah
    
    print('\n' + '=' * total_lebar)
    # Menggunakan variabel lebar_diagnosis untuk mengatur format header
    print(f'{"ID Hewan":<10} | {"Nama Hewan":<15} | {"Usia":<15} | {"Jenis Hewan":<15} | {"Jenis Kelamin":<13} | {"Diagnosis":<{lebar_diagnosis}}')
    print('=' * total_lebar)
    for hewan in list_data:
        usia_tampil = Format_Usia_Tampil(hewan['Usia'])
        # Menggunakan variabel lebar_diagnosis agar data dan header sejajar
        print(f"{hewan['ID Hewan']:<10} | {hewan['Nama Hewan']:<15} | {usia_tampil:<15} | {hewan['Jenis Hewan']:<15} | {hewan['Jenis Kelamin']:<13} | {hewan['Diagnosis']:<{lebar_diagnosis}}")
    print('=' * total_lebar)
    return True

def Cari_Hewan_by_ID(id_dicari):
    '''
    Mengembalikan data dictionary hewan sesuai ID.
    Jika tidak ditemukan, return None.
    '''
    for hewan in Data_Pasien:
        if hewan['ID Hewan'] == id_dicari:
            return hewan
    return None

def Minta_Konfirmasi(pesan):
    '''
    Meminta pengguna mengonfirmasi tindakan (y/n) dengan validasi input.
    '''
    while True:
        pilihan = input(f'{pesan} (y/n): ').lower()
        if pilihan in ['y', 'n']:
            return pilihan == 'y'
        else:
            print("Input tidak valid. Silakan masukkan 'y' atau 'n'.")

def Input_Usia():
    '''
      Meminta input usia dari pengguna dalam format:
    - 'X tahun Y bulan'
    - 'X tahun'
    - 'Y bulan'
    - atau angka saja yang dianggap sebagai bulan
    Mengembalikan usia total dalam bulan (int).
    '''
    while True:
        input_str = input("Masukkan Usia (contoh: '3 tahun 2 bulan', '5 tahun', atau '8 bulan'): ").lower()
        tahun = 0
        bulan = 0

        try:
            if 'tahun' in input_str and 'bulan' in input_str:
                # Contoh: '2 tahun 3 bulan'
                bagian_tahun = input_str.split('tahun')[0].strip()
                bagian_bulan = input_str.split('tahun')[1].split('bulan')[0].strip()
                tahun = int(bagian_tahun)
                bulan = int(bagian_bulan)

            elif 'tahun' in input_str:
                # Contoh: '4 tahun'
                bagian_tahun = input_str.split('tahun')[0].strip()
                tahun = int(bagian_tahun)

            elif 'bulan' in input_str:
                # Contoh: '7 bulan'
                bagian_bulan = input_str.split('bulan')[0].strip()
                bulan = int(bagian_bulan)

            else:
                # Jika input hanya angka, anggap sebagai bulan
                bulan = int(input_str.strip())
                print(f"(Input '{input_str}' dianggap sebagai {bulan} bulan)")

            # Validasi nilai akhir
            if tahun < 0:
                print('Tahun tidak boleh negatif.')
                continue
            if bulan < 0 or bulan >= 12:
                print('Bulan harus antara 0 sampai 11.')
                continue

            return tahun * 12 + bulan

        except (ValueError, IndexError):
            print("Format Input Tidak Valid. Contoh yang Benar: '2 tahun 6 bulan', '4 tahun', '9 bulan'")

def Input_Jenis_Kelamin():
    '''
    Menampilkan pilihan jenis kelamin untuk input valid (1 atau 2).
    Mengembalikan string 'Jantan' atau 'Betina'.
    '''
    while True:
        print('Pilih Jenis Kelamin:')
        print('1. Jantan')
        print('2. Betina')
        pilihan = input('Masukkan pilihan (1/2): ')
        if pilihan == '1':
            return 'Jantan'
        elif pilihan == '2':
            return 'Betina'
        else:
            print("Input tidak valid. Harap masukkan '1' atau '2'.")

def Input_Teks_Huruf(prompt):
    '''
    Fungsi 'spesialis' untuk meminta input yang hanya berisi huruf dan spasi.
    '''
    while True:
        teks = input(prompt).title()
        # Memastikan input tidak kosong dan hanya berisi huruf/spasi
        if teks.strip() and all(char.isalpha() or char.isspace() for char in teks):
            return teks
        else:
            print('Input Tidak Valid. Harap Hanya Masukkan Huruf dan Tidak Boleh Kosong.')

def Input_Teks_Bebas(prompt):
    '''Fungsi untuk meminta input teks apa pun, asal tidak kosong.'''
    while True:
        teks = input(prompt)
        if teks.strip(): # Memastikan input tidak hanya spasi kosong
            return teks
        else:
            print('Input Tidak Boleh Kosong.')

def Buat_ID_Otomatis():
    '''
    Menghasilkan ID baru otomatis (misal: H003 setelah H002).
    Berdasarkan data terakhir dalam list data_pasien.
    '''
    if not Data_Pasien:
        return 'H001'
    id_terakhir = Data_Pasien[-1]['ID Hewan']
    nomor_terakhir = int(id_terakhir[1:])
    nomor_baru = nomor_terakhir + 1
    if nomor_baru < 10:
        nomor_string = '00' + str(nomor_baru)
    elif nomor_baru < 100:
        nomor_string = '0' + str(nomor_baru)
    else:
        nomor_string = str(nomor_baru)
    id_baru = f'H{nomor_string}'
    return id_baru

def Tampilkan_Statistik(Data_Pasien):
    print('\n===== Statistik Ringan Data Hewan =====')

    # Jumlah total hewan
    jumlah_total = len(Data_Pasien)
    print(f"{'Total Hewan':<30}: {jumlah_total} ekor")

    # Jumlah berdasarkan Jenis Hewan
    jumlah_per_jenis_hewan = {}
    for hewan in Data_Pasien:
        jenis = hewan['Jenis Hewan']
        if jenis in jumlah_per_jenis_hewan:
            jumlah_per_jenis_hewan[jenis] += 1
        else:
            jumlah_per_jenis_hewan[jenis] = 1

    print(f"\n{'Jumlah Berdasarkan Jenis Hewan':<30}")
    for jenis, jumlah in jumlah_per_jenis_hewan.items():
        print(f"  - {jenis:<25}: {jumlah} ekor")

    # Jumlah berdasarkan Jenis Kelamin
    jumlah_per_jenis_kelamin = {}
    for hewan in Data_Pasien:
        kelamin = hewan['Jenis Kelamin']
        if kelamin in jumlah_per_jenis_kelamin:
            jumlah_per_jenis_kelamin[kelamin] += 1
        else:
            jumlah_per_jenis_kelamin[kelamin] = 1

    print(f"\n{'Jumlah Berdasarkan Jenis Kelamin':<30}")
    for kelamin, jumlah in jumlah_per_jenis_kelamin.items():
        print(f"  - {kelamin:<25}: {jumlah} ekor")

    # Usia Rata-rata per Jenis Hewan
    usia_per_jenis = {}
    hitung_per_jenis = {}
    for hewan in Data_Pasien:
        jenis = hewan['Jenis Hewan']
        usia = hewan['Usia']
        if jenis in usia_per_jenis:
            usia_per_jenis[jenis] += usia
            hitung_per_jenis[jenis] += 1
        else:
            usia_per_jenis[jenis] = usia
            hitung_per_jenis[jenis] = 1

    print(f"\n{'Rata-rata Usia per Jenis Hewan':<30}")
    for jenis in usia_per_jenis:
        rata2 = usia_per_jenis[jenis] / hitung_per_jenis[jenis]
        print(f"  - {jenis:<25}: {round(rata2, 1)} bulan")

    # Jumlah Berdasarkan Diagnosis
    jumlah_per_diagnosis = {}
    for hewan in Data_Pasien:
        diagnosis = hewan['Diagnosis']
        if diagnosis in jumlah_per_diagnosis:
            jumlah_per_diagnosis[diagnosis] += 1
        else:
            jumlah_per_diagnosis[diagnosis] = 1

    print(f"\n{'Jumlah Berdasarkan Diagnosis':<30}")
    for diagnosis, jumlah in jumlah_per_diagnosis.items():
        print(f"  - {diagnosis:<25}: {jumlah} kasus")

    # Diagnosis Terbanyak
    if jumlah_per_diagnosis:
        diagnosis_terbanyak = ''
        jumlah_terbanyak = 0
        for diagnosis, jumlah in jumlah_per_diagnosis.items():
            if jumlah > jumlah_terbanyak:
                diagnosis_terbanyak = diagnosis
                jumlah_terbanyak = jumlah

        print(f"\n{'Diagnosis Terbanyak':<30}: {diagnosis_terbanyak} ({jumlah_terbanyak} kasus)")

# ========================
# Bagian 3: Fungsi-Fungsi Menu Utama
# ========================

def Menu_Lihat_Data():
    '''Mengelola semua logika yang berhubungan dengan melihat data.'''
    while True:
        print('\n+++++++ Report Data Hewan +++++++')
        print('1. Report Seluruh Data')
        print('2. Report Data Tertentu (berdasarkan ID)')
        print('3. Cari Berdasarkan Nama Hewan')
        print('4. Statistik Data Hewan')
        print('0. Kembali Ke Menu Utama')
        pilihan = input('Silakan Pilih Sub Menu [1-4] atau [0]: ')

        if pilihan == '1':
            # Menampilkan seluruh data dalam bentuk tabel
            Tampilkan_Tabel(Data_Pasien)
        elif pilihan == '2':
            # Menampilkan data berdasarkan ID Hewan
            if not Data_Pasien:
                print('\n**** Tidak ada Data Hewan ****'); 
                continue
            id_cari = input('Masukkan ID Hewan: ').upper()
            hewan = Cari_Hewan_by_ID(id_cari)
            if hewan:
                print(f'\nData untuk ID {id_cari} ditemukan:')
                usia_tampil = Format_Usia_Tampil(hewan['Usia'])
                print(f"  {'ID Hewan':<15}: {hewan['ID Hewan']}")
                print(f"  {'Nama Hewan':<15}: {hewan['Nama Hewan']}")
                print(f"  {'Usia':<15}: {usia_tampil}")
                print(f"  {'Jenis Hewan':<15}: {hewan['Jenis Hewan']}")
                print(f"  {'Jenis Kelamin':<15}: {hewan['Jenis Kelamin']}")
                print(f"  {'Diagnosis':<15}: {hewan['Diagnosis']}")
            else:
                print(f'\n**** Data Hewan dengan ID {id_cari} Tidak Ditemukan ****')
        
        elif pilihan == '3':
             # Menampilkan data berdasarkan pencarian Nama Hewan
            if not Data_Pasien:
                print('\n**** Tidak ada Data Hewan ****'); 
                continue
            nama_cari = input('Masukkan Nama Hewan yang dicari: ').lower()
            hasil_pencarian = []
            for hewan in Data_Pasien:
                if nama_cari in hewan['Nama Hewan'].lower():
                    hasil_pencarian.append(hewan)
            
            if hasil_pencarian:
                print(f"\nMenampilkan hasil pencarian untuk '{nama_cari}':")
                Tampilkan_Tabel(hasil_pencarian)
            else:
                print(f"\n**** Tidak ditemukan hewan dengan nama yang mengandung '{nama_cari}' ****")

        elif pilihan == '4':
            # Menampilkan statistik ringan
            if not Data_Pasien:
                print('\n**** Tidak ada Data Hewan ****'); 
                continue
            Tampilkan_Statistik(Data_Pasien)

        elif pilihan == '0':
            break
        else:
            print('\n***** Pilihan yang Anda Masukkan Salah *****')

def Menu_Tambah_Data():
    '''
    Menyediakan fitur untuk menambahkan data pasien hewan baru.
    ID Hewan akan dibuat otomatis.
    Pengguna diminta mengisi nama, usia, jenis hewan, jenis kelamin, dan diagnosis.
    Program akan menanyakan konfirmasi sebelum menyimpan.
    '''
    while True:
        print('\n+++++++ Menambah Data Hewan +++++++')
        print('1. Tambah Data Hewan Baru')
        print('2. Tambah Beberapa Data Sekaligus')
        print('0. Kembali Ke Menu Utama')
        pilihan = input('Silakan Pilih Sub Menu [1-2] atau [0]: ')

        if pilihan == '1':
            id_baru = Buat_ID_Otomatis()
            print(f'\nID Hewan baru akan dibuat secara otomatis: {id_baru}')
            hewan_baru = {
                'ID Hewan': id_baru,
                'Nama Hewan': Input_Teks_Huruf('Masukkan Nama Hewan: '),
                'Usia': Input_Usia(),
                'Jenis Hewan': Input_Teks_Huruf('Masukkan Jenis Hewan: '),
                'Jenis Kelamin': Input_Jenis_Kelamin(),
                'Diagnosis': Input_Teks_Bebas('Masukkan Diagnosis Hewan: ')
            }
            if Minta_Konfirmasi('Apakah Data akan disimpan?'):
                Data_Pasien.append(hewan_baru)
                print('\n>> Data Hewan Berhasil Tersimpan <<')
            else:
                print('\n>> Data tidak jadi disimpan <<')
        elif pilihan == '2':
            jumlah_input = input('Berapa banyak data yang ingin ditambahkan?: ')
            if jumlah_input.isdigit():
                jumlah = int(jumlah_input)
                for i in range(jumlah):
                    print(f'\n>> Data ke-{i+1}')
                    id_baru = Buat_ID_Otomatis()
                    hewan_baru = {
                        'ID Hewan': id_baru,
                        'Nama Hewan': Input_Teks_Huruf('Masukkan Nama Hewan: '),
                        'Usia': Input_Usia(),
                        'Jenis Hewan': Input_Teks_Huruf('Masukkan Jenis Hewan: '),
                        'Jenis Kelamin': Input_Jenis_Kelamin(),
                        'Diagnosis': Input_Teks_Bebas('Masukkan Diagnosis Hewan: ')
                    }
                    if Minta_Konfirmasi('Apakah Data ini akan disimpan?'):
                        Data_Pasien.append(hewan_baru)
                        print('>> Data Berhasil Ditambahkan <<')
                    else:
                        print('>> Data Tidak Jadi Ditambahkan <<')
                print('\n>> Proses Penambahan Data Selesai <<')
            else:
                print('Input jumlah tidak valid. Harap masukkan angka yang benar.')
        elif pilihan == '0':
            break
        else:
            print('\n***** Pilihan yang Anda Masukkan Salah *****')

def Menu_Ubah_Data():
    '''
    Menyediakan fitur untuk mengubah salah satu kolom data hewan berdasarkan ID
    atau secara massal (diagnosis).
    '''
    while True:
        print('\n--------- Mengubah Data Hewan ---------')
        print('1. Ubah Data Hewan')
        print('2. Ubah Diagnosis Secara Massal')
        print('0. Kembali Ke Menu Utama')
        pilihan = input('Silakan Pilih Sub Menu [1-2] atau [0]: ')

        if pilihan == '1':
            if not Tampilkan_Tabel(Data_Pasien): continue
            id_cari = input('Masukkan ID Hewan yang akan diubah: ').upper()
            hewan = Cari_Hewan_by_ID(id_cari)

            if not hewan:
                print(f'\n**** Data Hewan dengan ID {id_cari} tidak ditemukan ****')
                continue

            print(f"\nData yang akan diubah: Nama: {hewan['Nama Hewan']}, Diagnosis: {hewan['Diagnosis']}")
            if not Minta_Konfirmasi('Lanjutkan mengubah data ini?'):
                print('\n>> Update Dibatalkan <<')
                continue

            kolom_mapping = {
                'nama': 'Nama Hewan', 'usia': 'Usia', 'jenis hewan': 'Jenis Hewan',
                'jenis kelamin': 'Jenis Kelamin', 'diagnosis': 'Diagnosis'
            }
            while True:
                kolom_input = input('Masukkan nama kolom yang ingin diubah (Nama/Usia/Jenis Hewan/Jenis Kelamin/Diagnosis): ').lower()
                if kolom_input in kolom_mapping:
                    break
                else:
                    print('\n**** Nama Kolom Tidak Valid. Coba Lagi. ****')
            
            key_to_update = kolom_mapping[kolom_input]
            nilai_lama = hewan[key_to_update]

            print(f"Nilai lama untuk '{key_to_update}': {Format_Usia_Tampil(nilai_lama) if key_to_update == 'Usia' else nilai_lama}")

            if key_to_update == 'Usia':
                nilai_baru = Input_Usia()
            elif key_to_update == 'Jenis Kelamin':
                nilai_baru = Input_Jenis_Kelamin()
            elif key_to_update in ['Nama Hewan', 'Jenis Hewan']:
                nilai_baru = Input_Teks_Huruf(f'Masukkan {key_to_update} baru: ')
            else: # Untuk Diagnosis
                nilai_baru = Input_Teks_Bebas(f'Masukkan {key_to_update} baru: ')

            nilai_tampil = Format_Usia_Tampil(nilai_baru) if key_to_update == 'Usia' else nilai_baru
            if Minta_Konfirmasi(f"Apakah Anda Yakin Ingin Mengubah {key_to_update} Menjadi '{nilai_tampil}'?"):
                hewan[key_to_update] = nilai_baru
                print('\n>> Data Berhasil Terupdate <<')
                print('Data setelah diubah:')
                Tampilkan_Tabel([hewan])
            else:
                print('\n>> Update Tidak Jadi Dilakukan <<')

        elif pilihan == '2':
            if not Data_Pasien: print('\n**** Tidak ada Data Hewan ****'); continue
            
            diagnosis_lama = input('Masukkan diagnosis yang ingin diubah (tidak peka huruf besar/kecil): ')
            
            # Cari dulu data yang cocok
            data_cocok = []
            for hewan in Data_Pasien:
                if hewan['Diagnosis'].lower() == diagnosis_lama.lower():
                    data_cocok.append(hewan)

            if not data_cocok:
                print(f'>> Tidak ditemukan data dengan diagnosis "{diagnosis_lama}" <<')
                continue

            print(f'\nDitemukan {len(data_cocok)} data yang cocok:')
            Tampilkan_Tabel(data_cocok)

            diagnosis_baru = Input_Teks_Bebas('Ganti menjadi diagnosis baru: ')
            
            if Minta_Konfirmasi(f'Yakin ingin mengubah {len(data_cocok)} data tersebut menjadi "{diagnosis_baru}"?'):
                jumlah_diubah = 0
                for hewan in Data_Pasien:
                    if hewan['Diagnosis'].lower() == diagnosis_lama.lower():
                        hewan['Diagnosis'] = diagnosis_baru
                        jumlah_diubah += 1
                print(f'>> {jumlah_diubah} data berhasil diperbarui <<')
            else:
                print('>> Perubahan dibatalkan <<')

        elif pilihan == '0':
            break
        else:
            print('\n***** Pilihan yang Anda Masukkan Salah *****')

def Menu_Hapus_Data():
    '''
    Menyediakan fitur untuk menghapus data hewan berdasarkan ID.
    Program akan meminta konfirmasi sebelum data benar-benar dihapus.
    '''
    while True:
        print('\n--------- Menghapus Data Hewan ---------')
        print('1. Hapus Data Hewan')
        print('2. Hapus Semua Data (Reset)')
        print('0. Kembali Ke Menu Utama')
        pilihan = input('Silakan Pilih Sub Menu [1-2] atau [0]: ')

        if pilihan == '1':
            if not Tampilkan_Tabel(Data_Pasien): continue
            id_hapus = input('Masukkan ID Hewan yang Akan Dihapus: ').upper()
            hewan = Cari_Hewan_by_ID(id_hapus)

            if not hewan:
                print(f'\n**** Data Hewan dengan ID {id_hapus} Tidak Ditemukan ****')
                continue

            if Minta_Konfirmasi(f"Yakin ingin menghapus data {hewan['Nama Hewan']} (ID: {hewan['ID Hewan']})?"):
                Data_Pasien.remove(hewan)
                print('\n>> Data Berhasil Dihapus <<')
            else:
                print('\n>> Data Tidak Jadi Dihapus <<')
        elif pilihan == '2':
            if Minta_Konfirmasi('Yakin ingin menghapus semua data?'):
                Data_Pasien.clear()
                print('>> Semua data berhasil dihapus <<')
        elif pilihan == '0':
            break
        else:
            print('\n***** Pilihan yang Anda Masukkan Salah *****')

# ========================
# Bagian 4: Program Utama
# ========================

def Main():
    '''
    Fungsi utama yang menjadi 'jantung' program.
    Menampilkan menu dan menangani alur utama.
    Akan terus berjalan hingga pengguna memilih keluar.
    '''
    while True:
        Tampilkan_Menu()
        pilihan = input('Silakan Pilih Main Menu [1-5]: ')

        if pilihan == '1':
            Menu_Lihat_Data()
        elif pilihan == '2':
            Menu_Tambah_Data()
        elif pilihan == '3':
            Menu_Ubah_Data()
        elif pilihan == '4':
            Menu_Hapus_Data()
        elif pilihan == '5':
            print('\nTerima Kasih Telah Menggunakan Program ANABUL!!!')
            break
        else:
            print('\n***** Pilihan yang Anda Masukkan Salah *************')

# Baris ini adalah 'pintu masuk' standar untuk program Python.
# Artinya: 'Hanya jalankan fungsi main() jika file ini dieksekusi secara langsung'.
if __name__ == '__main__':
    Main()
