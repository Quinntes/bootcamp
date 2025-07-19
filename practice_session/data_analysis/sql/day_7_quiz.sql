USE sakila;

-- 1. Tampilkan semua kolom dari tabel film (batasi 10 baris pertama).
SELECT *
FROM film
LIMIT 10;

-- 2. Tampilkan hanya kolom title dan release_year dari tabel film.
SELECT title, release_year
FROM film;

-- 3. Tampilkan 5 film dengan durasi (length) terpanjang.
SELECT title, length
FROM film
ORDER BY length DESC
LIMIT 5;

-- 4. Tampilkan semua film yang berdurasi lebih dari 120 menit.
SELECT title, length
FROM film
WHERE length > 120;

-- 5. Tampilkan semua film yang termasuk dalam kategori "PG-13".
SELECT title, rating
FROM film
WHERE rating = 'PG-13';

-- 6. Tampilkan semua film yang dirilis pada tahun 2006.
SELECT title, release_year
FROM film
WHERE release_year = 2006;

-- 7. Tampilkan film yang memiliki durasi antara 90 dan 100 menit.
SELECT title, length	
FROM film    -- atau bisa juga FROM sakila.length jadi ga usah run USE sakila;
WHERE length BETWEEN 90 AND 100;

-- 8. Tampilkan semua film yang memiliki rating “G”, “PG”, atau “PG-13”.
SELECT title, rating
FROM film
WHERE rating IN ('G', 'PG', 'PG-13');

-- 9. Tampilkan film yang memiliki judul mengandung kata “LOVE” (tidak case-sensitive).
SELECT title
FROM film
WHERE title LIKE '%LOVE%';

-- 10. Tampilkan film yang belum memiliki deskripsi (nilai description kosong/null).
SELECT title, description
FROM film
WHERE description IS NULL;
