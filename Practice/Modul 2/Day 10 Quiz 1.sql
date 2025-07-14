
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

USE sakila;
WITH FilmRevenue AS (
    SELECT 
        f.film_id,
        f.title,
        c.name AS category_name,
        SUM(p.amount) AS total_revenue
    FROM 
        payment p
    JOIN 
        rental r ON p.rental_id = r.rental_id
    JOIN 
        inventory i ON r.inventory_id = i.inventory_id
    JOIN 
        film f ON i.film_id = f.film_id
    JOIN 
        film_category fc ON f.film_id = fc.film_id
    JOIN 
        category c ON fc.category_id = c.category_id
    GROUP BY 
        f.film_id, f.title, c.name
),
RankedFilms AS (
    SELECT *,
           RANK() OVER (PARTITION BY category_name ORDER BY total_revenue DESC) AS film_rank
    FROM FilmRevenue
)
SELECT film_id, title, category_name, total_revenue, film_rank
FROM RankedFilms
WHERE film_rank <= 3
ORDER BY category_name, film_rank;
