
-- ************************************************************
-- [SAKILA] Top 3 Film Terlaris per Kategori
-- Tujuan: Temukan 3 film dengan pendapatan tertinggi per kategori
-- Teknik: CTE, JOIN, Window Function (RANK)
-- ************************************************************

/* Deskripsi 
Manajemen ingin mengetahui 3 film dengan total pendapatan tertinggi di tiap kategori film.
Anda diminta menyusun laporan:
- Gabungkan transaksi pembayaran dengan film dan kategorinya
- Hitung total pendapatan per film
- Gunakan window function untuk mencari 3 film terlaris di setiap kategori (tanpa LIMIT) */

/* 3 Query
1. Menghitung total revenue dari tiap film (multi table)
2. Bikin ranking setiap film di setiap kategori berdasarkan total revenue (Query 1)
3. Filter (Query 2) ranking <= 3 */
