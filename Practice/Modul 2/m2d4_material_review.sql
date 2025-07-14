-- ============================================
-- REVIEW MATERI CTE, WINDOW FUNCTION, SLIDING WINDOWS
-- Database: sakila
-- ============================================

-- =====================================================
-- 1. CTE (Common Table Expression)
-- =====================================================
-- CTE digunakan untuk:
-- - Menyederhanakan query kompleks
-- - Menghindari pengulangan subquery
-- - Membuat kode lebih modular
-- - Cocok digunakan saat hasil sementara ingin digunakan berulang

-- STUDI KASUS:
-- Kita ingin mencari rata-rata pembayaran per customer,
-- lalu ambil hanya customer yang total pembayarannya > rata-rata.
-- Menggunakan CTE karena tidak bisa diselesaikan dengan 1 level query biasa.

-- WITH nama_table AS (Query) SELECT * FROM ...
-- WITH nama_table1 AS (Query1), nama_table2 AS (Query2) SELECT * FROM ...
USE sakila;

-- Cara satu 
WITH payment_summary AS (
    SELECT customer_id, SUM(amount) AS total_payment
    FROM payment
    GROUP BY customer_id
),
average_payment AS (
    SELECT AVG(total_payment) AS avg_payment
    FROM payment_summary
)
SELECT 
    ps.customer_id,
    c.first_name,
    c.last_name,
    ps.total_payment,
    ap.avg_payment
FROM payment_summary ps
JOIN customer c ON ps.customer_id = c.customer_id
JOIN average_payment ap ON ps.total_payment > ap.avg_payment;

-- Cara dua 
WITH payment_summary AS (
    SELECT customer_id, SUM(amount) AS total_payment
    FROM payment
    GROUP BY customer_id
)
SELECT 
    ps.customer_id,
    c.first_name,
    c.last_name,
    ps.total_payment
FROM payment_summary ps
JOIN customer c ON ps.customer_id = c.customer_id
WHERE ps.total_payment > (SELECT AVG(total_payment) AS avg_payment FROM payment_summary);


-- =====================================================
-- 2. WINDOW FUNCTION
-- =====================================================
-- Window Function digunakan untuk menghitung nilai agregat
-- TANPA mengurangi jumlah baris (berbeda dengan GROUP BY).

-- Fungsi-fungsi umum Window:
-- - ROW_NUMBER(): Memberi nomor unik berdasarkan urutan
-- - RANK(): Memberi ranking, bisa loncat
-- - DENSE_RANK(): Ranking tanpa loncatan
-- - NTILE(n): Membagi ke dalam n grup kuartil/percentile
-- - LAG()/LEAD(): Ambil nilai sebelumnya/sesudahnya
-- - FIRST_VALUE()/LAST_VALUE(): Ambil nilai awal/akhir dalam window
-- - SUM(), AVG(), MIN(), MAX(): Bisa digunakan sebagai agregat jendela

-- STUDI KASUS 1:
-- Ambil 3 pembayaran terakhir (terbaru) dari masing-masing customer.
-- Ideal memakai ROW_NUMBER() agar bisa filter baris tertentu.
WITH ranked_payment AS (
    SELECT 
        customer_id,
        payment_id,
        payment_date,
        amount,
        ROW_NUMBER() OVER(PARTITION BY customer_id ORDER BY payment_date DESC) AS rn
    FROM payment
)
SELECT *
FROM ranked_payment
WHERE rn <= 3
ORDER BY customer_id, rn;

-- STUDI KASUS 2:
-- Kelompokkan customer berdasarkan kuartil total pembayarannya.
-- Gunakan NTILE untuk membagi ke N kuartil.
WITH customer_payment AS (
    SELECT customer_id, SUM(amount) AS total_payment
    FROM payment
    GROUP BY customer_id
)
SELECT 
    customer_id,
    total_payment,
    NTILE(4) OVER (ORDER BY total_payment DESC) AS payment_quartile
FROM customer_payment
ORDER BY total_payment;

-- =====================================================
-- 3. SLIDING WINDOWS
-- =====================================================
-- Sliding Window memungkinkan analisis nilai berdasarkan frame dinamis.
-- Frame dinyatakan sebagai: 
-- ROWS BETWEEN ... AND ...
-- OVER (ROWS BETWEEN ... AND ...)
-- Penjelasan istilah:
-- - CURRENT ROW: baris saat ini
-- - X PRECEDING: X baris sebelum current
-- - X FOLLOWING: X baris setelah current
-- - UNBOUNDED PRECEDING: dari baris paling awal
-- - UNBOUNDED FOLLOWING: hingga baris paling akhir

-- STUDI KASUS: Kumulatif total pembayaran per customer
SELECT 
    customer_id,
    payment_date,
    amount,
    SUM(amount) OVER (
        PARTITION BY customer_id 
        ORDER BY payment_date 
        ROWS BETWEEN UNBOUNDED PRECEDING AND CURRENT ROW
    ) AS cumulative_payment
FROM payment
ORDER BY customer_id, payment_date;

-- STUDI KASUS: Rata-rata 3 transaksi terakhir
SELECT 
    customer_id,
    payment_date,
    amount,
    ROUND(AVG(amount) OVER (
        PARTITION BY customer_id 
        ORDER BY payment_date 
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ), 2) AS moving_avg_last_3
FROM payment
ORDER BY customer_id, payment_date;

-- STUDI KASUS: Selisih jumlah pembayaran dengan transaksi sebelumnya
SELECT 
    customer_id,
    payment_id,
    amount,
    LAG(amount) OVER (
        PARTITION BY customer_id 
        ORDER BY payment_date
    ) AS previous_amount,
    amount - LAG(amount) OVER (
        PARTITION BY customer_id 
        ORDER BY payment_date
    ) AS difference
FROM payment
ORDER BY customer_id, payment_date;

-- =====================================================
-- PENUTUP
-- =====================================================
-- Gunakan CTE saat:
--    - Subquery kompleks
--    - Analisis bertahap
-- Gunakan Window Function saat:
--    - Perlu nilai agregat tanpa hilangkan baris
--    - Analisis per baris tapi butuh konteks sekeliling
-- Gunakan Sliding Windows saat:
--    - Perlu akumulasi, perbandingan, atau trend waktu
