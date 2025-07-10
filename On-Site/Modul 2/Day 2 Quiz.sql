USE world;

-- 3 negara dengan jumlah penduduk di atas 200 juta
SELECT name, population
FROM country
WHERE population > 200000000
LIMIT 3;

-- nama nama negara unik di benua asia mengandung kata 'stan'
SELECT name
FROM country
WHERE continent = 'asia' AND name LIKE '%stan%';

-- jumlah negara di benua afrika dan rata rata luas wilayah
SELECT COUNT(*) AS jumlah_negara, AVG(surfacearea) AS rata_rata_luas
FROM country
WHERE continent = 'africa';

-- 5 negara dengan jumlah penduduk terbanyak di dunia sertakan nama dan jumlah penduduknya
SELECT name, population
FROM country
ORDER BY population DESC
LIMIT 5;

-- negara berdasarkan benua dan menampilkan jumlah negara dan total populasi per benua
SELECT continent, COUNT(*) AS jumlah_negara, SUM(population) AS total_populasi
FROM country
GROUP BY continent;