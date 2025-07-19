USE sakila;

-- Dari tabel “payment”, tampilkan 10 baris data customer id, rental id, amount, dan payment date!
SELECT customer_id, rental_id, amount, payment_date
FROM payment
LIMIT 10;


-- Dari tabel “film”, tampilkan 10 judul film, tahun release, dan durasi rental dimana judul film yang ditampilkan yang dimulai dengan huruf “S”!
SELECT title, release_year, rental_duration
FROM film
WHERE title LIKE 'S%'
LIMIT 10;


-- Dari tabel “film”, tampilkan durasi rental, banyaknya film setiap durasi rental, dan rata-rata durasi film!
-- Kelompokkan jumlah film dan rata-rata durasi film berdasarkan durasi rentalnya!
-- Karena rata-rata durasi film angka desimal, bulatkan 2 angka di belakang koma!
SELECT rental_duration AS durasi_rental,
       COUNT(*) AS jumlah_film,
       ROUND(AVG(length), 2) AS rata_rata_durasi
FROM film
GROUP BY rental_duration
ORDER BY rental_duration ASC;

-- Dari tabel “film”, tampilkan title, durasi film, dan rating yang durasi filmnya lebih dari rata-rata durasi film total!
-- Tampilkan 25 data yang diurutkan dari durasi terlama!
SELECT title, length, rating
FROM film
WHERE length > (SELECT AVG(length) FROM film)
ORDER BY length DESC
LIMIT 25;


-- Dari tabel “film”, tampilkan rating, Replacement Cost tertinggi, Rental Rate Terendah, dan Rata-Rata Durasi dan kelompokkan berdasarkan rating film!
SELECT rating,
       MAX(replacement_cost) AS replacement_cost_tertinggi,
       MIN(rental_rate) AS rental_rate_terendah,
       AVG(length) AS rata_rata_durasi
FROM film
GROUP BY rating
ORDER BY rating;


-- Tampilkan 15 daftar film yang memiliki huruf “K” pada akhir pada title, lalu tampilkan title, durasi, serta Bahasa pada film!
-- Sebagai catatan, lakukan join terlebih dahulu dari tabel “film” dan tabel “language”!
SELECT f.title, f.length, l.name AS bahasa
FROM film f
JOIN language l ON f.language_id = l.language_id
WHERE f.title LIKE '%K'
LIMIT 15;


-- Tampilkan Judul Film (dari tabel “film”), First Name (dari tabel “actor”), dan Last Name (Dari tabel “actor”) dari actor yang memiliki “actor_id” = 14!
-- Sebagai catatan, lakukan join table terlebih dahulu antara tabel “film”, “film_actor”, dan “actor”!
SELECT f.title, a.first_name, a.last_name
FROM film f
JOIN film_actor fa ON f.film_id = fa.film_id
JOIN actor a ON fa.actor_id = a.actor_id
WHERE a.actor_id = 14;


-- Dari tabel "city“, tampilkan city dan country id!
-- Tampilkan hanya city atau kota yang namanya ada huruf "d" di posisi mana pun dan diakhiri huruf “a”!
-- Tampilkan 15 data yang diurutkan berdasarkan city-nya secara ascending!
SELECT city, country_id
FROM city
WHERE city LIKE '%d%a'
ORDER BY city ASC
LIMIT 15;


-- Tampilkan nama genre (name dari tabel “category”) dan jumlah banyaknya film di setiap genrenya!
-- Lakukan join terlebih dahulu antara tabel “film”, “film_category”, dan “category”!
-- Urutkan berdasarkan jumlah film di setiap kategorinya secara ascending!
SELECT c.name AS genre,
       COUNT(f.film_id) AS jumlah_film
FROM category c
JOIN film_category fc ON c.category_id = fc.category_id
JOIN film f ON fc.film_id = f.film_id
GROUP BY c.name
ORDER BY jumlah_film ASC;


-- Dari tabel “film”, tampilkan title, description, length, serta rating!
-- Tampilkan 10 judul film yang diakhiri huruf ‘h’ dan durasinya di atas durasi rata-rata!
-- Urutkan berdasarkan judulnya secara ascending!
SELECT title, description, length, rating
FROM film
WHERE title LIKE '%h'
  AND length > (SELECT AVG(length) FROM film)
ORDER BY title ASC
LIMIT 10;