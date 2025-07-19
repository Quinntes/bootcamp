-- =====================================================
-- Analisis Retensi Pelanggan Berdasarkan Kategori Film
-- =====================================================

/* Deskripsi
Tim marketing ingin mengetahui kategori film mana yang paling disukai oleh pelanggan aktif. 
Pelanggan dianggap aktif jika melakukan minimal 10 transaksi rental. Tujuan Anda:
1. Identifikasi pelanggan aktif menggunakan subquery
2. Gabungkan transaksi rental dengan film dan kategorinya
3. Hitung jumlah rental per kategori hanya dari pelanggan aktif
4. Tampilkan 5 kategori film dengan jumlah rental tertinggi dari pelanggan aktif */

USE sakila

SELECT c.name AS category_name,
       COUNT(r.rental_id) AS total_rental
FROM customer cu
-- Gabung ke tabel rental
JOIN rental r ON cu.customer_id = r.customer_id
-- Gabung ke inventory untuk akses film_id
JOIN inventory i ON r.inventory_id = i.inventory_id
-- Gabung ke tabel film
JOIN film f ON i.film_id = f.film_id
-- Gabung ke film_category untuk akses kategori
JOIN film_category fc ON f.film_id = fc.film_id
-- Gabung ke category untuk nama genre
JOIN category c ON fc.category_id = c.category_id
-- Filter hanya pelanggan yang aktif (minimal 10 transaksi)
WHERE cu.customer_id IN (
    SELECT customer_id
    FROM rental
    GROUP BY customer_id
    HAVING COUNT(rental_id) >= 10
)
-- Hitung jumlah rental per kategori
GROUP BY c.name
-- Urutkan dari yang paling banyak
ORDER BY total_rental DESC
-- Ambil hanya 5 teratas
LIMIT 5;