--- String Pattern & Filtering ---
--- 1.	Menemukan film yang judulnya dimulai dengan huruf 'A'.
SELECT *
FROM films
WHERE title LIKE 'A%';
--- 2.	Menemukan customer yang terdaftar antara tahun 2005–2006.
SELECT *
FROM customers
WHERE registration_year BETWEEN 2005 AND 2006;


--- Sorting (Pengurutan) ---
--- 3.	Menampilkan 10 film pertama berdasarkan urutan alfabet.
SELECT *
FROM films
ORDER BY title ASC
LIMIT 10;


--- Grouping & Aggregation ---
--- 4.	Mengelompokkan jumlah customer berdasarkan status aktif.
SELECT active_status, COUNT(*) AS customer_count 
FROM customers 
GROUP BY active_status;
--- 5.	Menampilkan jumlah film per rating.
SELECT rating, COUNT(*) AS film_count 
FROM films 
GROUP BY rating;
--- 6.	Menampilkan kategori dengan jumlah film lebih dari 100.
SELECT category, COUNT(*) AS film_count 
FROM films 
GROUP BY category 
HAVING COUNT(*) > 100;


--- Built-in Functions ---
--- 7.	Menampilkan rata-rata durasi film (dalam menit).
SELECT AVG(duration) AS average_duration 
FROM films;
--- 8.	Menampilkan durasi film terpendek dan terpanjang.
SELECT MIN(duration) AS shortest_duration, MAX(duration) AS longest_duration 
FROM films;
--- 9.	Menghitung jumlah karakter pada judul film.
SELECT title, LENGTH(title) AS title_length 
FROM films;
--- 10.	Menampilkan judul film dalam huruf kapital.
SELECT UPPER(title) AS title_uppercase 
FROM films;


--- Date & Time Functions ---
--- 11.	Menampilkan tahun pendaftaran customer.
SELECT customer_id, YEAR(registration_date) AS registration_year 
FROM customers;
--- 12.	Menampilkan bulan pendaftaran customer.
SELECT customer_id, MONTH(registration_date) AS registration_month 
FROM customers;
--- 13.	Menghitung umur data customer (dalam tahun).
SELECT customer_id, TIMESTAMPDIFF(YEAR, registration_date, CURDATE()) AS customer_age 
FROM customers;


--- Subqueries ---
--- 14.	Menampilkan film dengan durasi di atas rata-rata.
SELECT * 
FROM films 
WHERE duration > (SELECT AVG(duration) 
                  FROM films);
--- 15.	Menghitung jumlah kategori per film.
SELECT film_id, COUNT(category_id) AS category_count 
FROM film_categories 
GROUP BY film_id;
--- 16.	Menampilkan 10 customer dengan jumlah rental terbanyak.
SELECT customer_id, COUNT(rental_id) AS rental_count 
FROM rentals 
GROUP BY customer_id 
ORDER BY rental_count DESC 
LIMIT 10;


--- Join Operations ---
--- 17.	Menampilkan id_film, nama film dan jumlah kategorinya.
SELECT f.id AS film_id, f.title, COUNT(fc.category_id) AS category_count
FROM films f
LEFT JOIN film_categories fc ON f.id = fc.film_id
GROUP BY f.id, f.title;
--- 18.	Menampilkan total pembayaran per customer.
SELECT customer_id, SUM(payment_amount) AS total_payment 
FROM payments 
GROUP BY customer_id;
--- 19.	Menampilkan semua customer, termasuk yang belum pernah menyewa.
SELECT c.*, COUNT(r.rental_id) AS rental_count
FROM customers c
LEFT JOIN rentals r ON c.id = r.customer_id
GROUP BY c.id;
--- 20.	Menampilkan pasangan customer yang daftar di tahun sama.
SELECT a.id AS customer1_id, b.id AS customer2_id
FROM customers a, customers b
WHERE a.registration_year = b.registration_year AND a.id <> b.id;

--- CTE (Common Table Expression) ---
--- 21.	Menampilkan top 10 customer dengan total pembayaran terbanyak.
WITH CustomerPayments AS (
    SELECT customer_id, SUM(payment_amount) AS total_payment
    FROM payments
    GROUP BY customer_id
)
SELECT * 
FROM CustomerPayments 
ORDER BY total_payment DESC 
LIMIT 10;

--- Window Functions ---
--- 22.	Menampilkan rata-rata pembayaran per customer.
SELECT customer_id, AVG(payment_amount) OVER (PARTITION BY customer_id) AS average_payment
FROM payments;
--- 23.	Menampilkan peringkat pembayaran customer 'Mary' (dengan RANK).
SELECT customer_id, payment_amount, RANK() OVER (ORDER BY payment_amount DESC) AS payment_rank
FROM payments
WHERE customer_name = 'Mary';
--- 24.	Membagi pembayaran ke dalam 4 kuartil dari customer 'Mary'.
SELECT payment_amount, NTILE(4) OVER (ORDER BY payment_amount) AS quartile
FROM payments
WHERE customer_name = 'Mary';
--- 25.	Menghitung moving average untuk 3 pembayaran terakhir  dari customer 'Mary'.
SELECT payment_date, payment_amount, 
       AVG(payment_amount) OVER (ORDER BY payment_date ROWS BETWEEN 2 PRECEDING AND CURRENT ROW) AS moving_average
FROM payments
WHERE customer_name = 'Mary';
