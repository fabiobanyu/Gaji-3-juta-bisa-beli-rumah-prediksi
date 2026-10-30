# Reproduksi analisis

Penulis proyek: Fabio Banyu Cyto. Snapshot penelitian: 30 Oktober 2026.

1. Instal paket pada requirements.txt, idealnya dalam lingkungan Python terpisah. Versi lingkungan asli tersedia di environment.json.
2. Dari folder utama, jalankan python scripts/verify_research.py untuk memeriksa sumber dan hitungan dasar.
3. Jalankan python model.py untuk membentuk kembali asumsi tercatat, tabel hasil, sensitivitas, backtest, dan empat grafik. Proses ini menimpa hasil turunan di results/ dan figures/.
4. Alternatif: buka analisis_lampung.ipynb dan Run All. Notebook memiliki kode model lengkap dan hasil tersimpan. Perubahan di model.py tidak otomatis menyinkronkan kode yang disalin dalam notebook, sehingga perubahan metode harus memperbarui keduanya.

Analisis luring tidak memerlukan unduhan baru. assumptions.json adalah catatan parameter, bukan konfigurasi yang dibaca otomatis. Ubah BASE sebelum menjalankan ulang. Angka masa depan adalah asumsi dan hasil simulasi.

## Memperbarui sumber secara sengaja

Simpan snapshot lama terlebih dahulu. Skrip download_sources.py, download_more.py, dan download_documents.py mengambil sumber resmi dan menulis manifest. inspect_sources.py mengekstrak JSON tertanam dan PDF; buku BPS besar sehingga pemrosesan bisa memerlukan waktu. prepare_data.py membentuk CSV.

Situs dan tautan dapat berubah. Rangkaian skrip ini merekam prosedur penelitian, bukan layanan pembaruan otomatis yang dijamin. Snapshot saat ini memakai bi_shpr_pdf_retry.pdf karena unduhan BI pertama terputus. Setelah unduhan baru, periksa nama PDF dan manifest, lalu sesuaikan referensi pada prepare_data.py jika perlu. Jangan menganggap HTTP200 berarti data tabel berhasil diperoleh.

Hasil backtest hanya mengevaluasi prediksi satu triwulan indeks BI. Hal itu tidak memvalidasi probabilitas Monte Carlo atau keputusan bank. Semua masalah sumber yang diketahui disimpan pada results/data_quality.csv.
