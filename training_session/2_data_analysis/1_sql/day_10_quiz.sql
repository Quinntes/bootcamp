USE sakila;

--- String Pattern & Filtering ---
--- 1.	Menemukan film yang judulnya dimulai dengan huruf 'A'.
SELECT *
FROM film
WHERE title LIKE 'A%';
--- 2.	Menemukan customer yang terdaftar antara tahun 2005–2006.
SELECT *
FROM customer
WHERE YEAR(create_date) BETWEEN 2005 AND 2006;


--- Sorting (Pengurutan) ---
--- 3.	Menampilkan 10 film pertama berdasarkan urutan alfabet.
SELECT *
FROM film
ORDER BY title ASC
LIMIT 10;


--- Grouping & Aggregation ---
--- 4.	Mengelompokkan jumlah customer berdasarkan status aktif.
SELECT ACTIVE, COUNT(*) AS customer_count 
FROM customer
GROUP BY active;
--- 5.	Menampilkan jumlah film per rating.
SELECT rating, COUNT(*) AS film_count 
FROM film 
GROUP BY rating;
--- 6.	Menampilkan kategori dengan jumlah film lebih dari 100.
SELECT category_id, COUNT(*) AS film_count
FROM film_category
GROUP BY category_id
HAVING COUNT(*) > 100;


--- Built-in Functions ---
--- 7.	Menampilkan rata-rata durasi film (dalam menit).
SELECT AVG(length) AS average_duration 
FROM film;
--- 8.	Menampilkan durasi film terpendek dan terpanjang.
SELECT MIN(length) AS shortest_duration, MAX(length) AS longest_duration 
FROM film;
--- 9.	Menghitung jumlah karakter pada judul film.
SELECT title, LENGTH(title) AS title_length 
FROM film;
--- 10. Menampilkan judul film dalam huruf kapital.
SELECT UPPER(title) AS title_uppercase 
FROM film;


--- Date & Time Functions ---
--- 11. Menampilkan tahun pendaftaran customer.
SELECT CONCAT(first_name, ' ', last_name) customer_id, YEAR(create_date) AS registration_year 
FROM customer;
--- 12. Menampilkan bulan pendaftaran customer.
SELECT CONCAT(first_name, ' ', last_name), MONTH(create_date) AS registration_month 
FROM customer;
--- 13. Menghitung umur data customer (dalam tahun).
SELECT CONCAT(first_name, ' ', last_name), TIMESTAMPDIFF(YEAR, create_date, CURDATE()) AS customer_age 
FROM customer;


--- Subqueries ---
--- 14. Menampilkan film dengan durasi di atas rata-rata.
SELECT * 
FROM film 
WHERE length > (SELECT AVG(length) 
                  FROM film);
--- 15. Menghitung jumlah kategori per film.
SELECT film_id, COUNT(*) AS category_count
FROM film_category
GROUP BY film_id;

--- 16. Menampilkan 10 customer dengan jumlah rental terbanyak.
SELECT customer_id, COUNT(*) AS rental_count
FROM rental
GROUP BY customer_id
ORDER BY rental_count DESC
LIMIT 10;


--- Join Operations ---
--- 17. Menampilkan id_film, nama film dan jumlah kategorinya.
SELECT f.film_id, f.title, COUNT(fc.category_id) AS category_count
FROM film f
LEFT JOIN film_category fc ON f.film_id = fc.film_id
GROUP BY f.film_id, f.title;
--- 18. Menampilkan total pembayaran per customer.
SELECT customer_id, SUM(amount) AS total_payment 
FROM payment 
GROUP BY customer_id;
--- 19. Menampilkan semua customer, termasuk yang belum pernah menyewa.
SELECT c.*, COUNT(r.rental_id) AS rental_count
FROM customer c
LEFT JOIN rental r ON c.customer_id = r.customer_id
GROUP BY c.customer_id;
--- 20. Menampilkan pasangan customer yang daftar di tahun sama.
SELECT a.customer_id AS customer1_id, b.customer_id AS customer2_id
FROM customer a
JOIN customer b ON YEAR(a.create_date) = YEAR(b.create_date)
WHERE a.customer_id < b.customer_id;

--- CTE (Common Table Expression) ---
--- 21. Menampilkan top 10 customer dengan total pembayaran terbanyak.
WITH CustomerPayments AS (
    SELECT customer_id, SUM(amount) AS total_payment
    FROM payment
    GROUP BY customer_id
)
SELECT * 
FROM CustomerPayments 
ORDER BY total_payment DESC 
LIMIT 10;

--- Window Functions ---
--- 22. Menampilkan rata-rata pembayaran per customer.
-- Cara 1
SELECT customer_id, payment_id, amount,
       AVG(amount) OVER (PARTITION BY customer_id) AS average_payment
FROM payment;

-- Cara 2
SELECT c.customer_id, c.first_name, p.payment_id, p.amount,
       AVG(amount) OVER (PARTITION BY customer_id) AS rata_rata
FROM customer c 
JOIN payment p ON c.customer_id = p.payment_id
LIMIT 300;

--- 23. Menampilkan peringkat pembayaran customer 'Mary' (dengan RANK).
SELECT p.customer_id, p.amount, 
       RANK() OVER (ORDER BY p.amount DESC) AS payment_rank
FROM payment p
JOIN customer c ON p.customer_id = c.customer_id
WHERE c.first_name = 'Mary';

--- 24. Membagi pembayaran ke dalam 4 kuartil dari customer 'Mary'.
SELECT p.amount, 
       NTILE(4) OVER (ORDER BY p.amount) AS quartile
FROM payment p
JOIN customer c ON p.customer_id = c.customer_id
WHERE c.first_name = 'Mary';
--- 25. Menghitung moving average untuk 3 pembayaran terakhir  dari customer 'Mary'.
SELECT c.customer_id, c.first_name, p.payment_id, p.amount,
       AVG(p.amount) OVER (PARTITION BY p.customer_id
       ORDER BY p.payment_date ASC
       ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS rata_rata
FROM customer c
JOIN payment p ON c.customer_id = p.customer_id
WHERE c.first_name = 'Mary';

