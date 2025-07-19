-- Evaluasi Kategori Negara Berdasarkan Populasi dan Harapan Hidup
-- Database: world
-- Tabel: country
-- Konteks: Sebagai seorang Data Analyst di organisasi internasional, kamu diminta mengelompokkan negara-negara berdasarkan 
--          populasi dan harapan hidup serta menilai kelompok negara mana yang memiliki stabilitas demografis yang lebih baik.

/* Deskripsi
Tampilkan data agregat berdasarkan kategori berikut:
1. pop_group:
	- 'Small' untuk populasi < 1 juta
    - 'Medium' untuk populasi 1–50 juta
    - 'Large' untuk populasi > 50 juta

2. life_status:
	- 'High' jika life expectancy ≥ 75
    - 'Moderate' jika antara 60–74.9
    - 'Low' jika < 60

3. Hitung:
	- Jumlah negara (total_negara)
    - Rata-rata life expectancy (avg_life_exp)
    - Rata-rata GNP (avg_gnp)

4. Filter hanya kombinasi kategori yang punya rata-rata harapan hidup di atas 78 tahun

5. Urutkan berdasarkan jumlah negara terbanyak */

-- Your Code Here ...
USE world;
SELECT 
    CASE 
        WHEN population < 1000000 THEN 'Small'
        WHEN population BETWEEN 1000000 AND 50000000 THEN 'Medium'
        ELSE 'Large'
    END AS pop_group,
    
    CASE 
        WHEN lifeexpectancy >= 75 THEN 'High'
        WHEN lifeexpectancy >= 60 THEN 'Moderate'
        ELSE 'Low'
    END AS life_status,
    
    COUNT(*) AS total_negara,
    ROUND(AVG(lifeexpectancy), 2) AS avg_life_exp,
    ROUND(AVG(gnp), 2) AS avg_gnp

FROM country

WHERE lifeexpectancy IS NOT NULL  -- Pastikan data harapan hidup valid

GROUP BY pop_group, life_status

HAVING AVG(lifeexpectancy) > 78

ORDER BY total_negara DESC;

