# Fabio Banyu Cyto: Gaji Rp3 Juta, Kapan Bisa Beli Rumah?

Studi skenario Lampung, **30 Oktober 2026**. Data historis, ketentuan program, asumsi masa depan, dan hasil simulasi dipisahkan. Angka hasil di bawah merupakan proyeksi bersyarat, bukan prediksi resmi BPS/BI atau keputusan kredit bank.

## Jawaban utama

Untuk profil contoh berusia 23 tahun, gaji bersih Rp3 juta dan biaya hidup Rp2,1 juta per bulan, skenario dasar mencapai syarat finansial KPR rumah Rp166 juta setelah **2 tahun 9 bulan**. Hasil ini mengasumsikan gaji naik 4% per tahun, biaya naik 3%, harga setara subsidi tetap, dan bunga anuitas nominal 5% selama 20 tahun.

DP aktual saat masuk sekitar **Rp15,05 juta**, karena tabungan yang tersedia dipakai untuk memperbesar DP. Cicilan awal sekitar **Rp996 ribu per bulan**, dengan biaya awal Rp4,98 juta dan dana darurat sekitar Rp13,67 juta tetap diperhitungkan. Usia masuk sekitar 25 tahun 9 bulan; pelunasan terjadwal pada usia 45 tahun 9 bulan.

| Alternatif | Waktu mencapai syarat pembelian | Usia saat membeli |
|---|---|---|
| KPR rumah subsidi, anuitas 20 tahun | 2 tahun 9 bulan | 25 tahun 9 bulan |
| Tunai rumah dengan harga setara subsidi | 10 tahun 9 bulan | 33 tahun 9 bulan |
| Tunai rumah komersial | 24 tahun 8 bulan | 47 tahun 8 bulan |
| KPR rumah komersial, tenor 20 tahun | Tidak tercapai dengan batas usia lunas 55 tahun | Kesempatan masuk berakhir pada usia 35 tahun |

Harga komersial awal Rp350 juta tumbuh menjadi sekitar Rp725,6 juta pada saat pembelian tunai. Jika batas usia lunas dalam skenario komersial diganti menjadi 65 tahun, syarat KPR tercapai setelah **19 tahun 10 bulan**. Artinya, hasil “tidak tercapai” bergantung pada ketentuan usia yang dipilih, bukan berarti mustahil seumur hidup.

Perbedaan bunga sangat berpengaruh: halaman Tapera yang tersimpan menulis “5% flat”. Bila benar-benar dihitung dengan metode flat, waktu KPR subsidi menjadi **4 tahun 5 bulan**, dibandingkan **2 tahun 9 bulan** dengan anuitas. Kedua perhitungan tersedia; angka anuitas tidak disajikan sebagai penafsiran pasti kontrak bank.

## Data nyata yang berhasil diperoleh

| indicator                               |         value | unit            | source_id              |
|:----------------------------------------|--------------:|:----------------|:-----------------------|
| Upah rata-rata Lampung Agustus2025      |   2.52062e+06 | IDR/bulan       | bps_upah               |
| Pengeluaran perkapita Lampung Maret2025 |   1.23961e+06 | IDR/orang/bulan | bps_konsumsi_komoditas |
| IHPR Bandar Lampung2026Q2               | 105.48        | indeks2018=100  | bi_shpr_pdf_retry      |
| Harga penawaran subsidi Kalianda        |   1.66e+08    | IDR/unit        | sikumbang_menara       |
| Harga penawaran komersial Kalianda      |   3.5e+08     | IDR/unit        | sikumbang_menara       |

- **BPS upah 2025:** provinsi × sektor × Februari/Agustus/Tahunan. Upah rata-rata Lampung Agustus 2025 Rp2.520.619 adalah rata-rata buruh/karyawan/pegawai. Ini bukan UMP, median, atau pertumbuhan gaji orang yang sama. Sel tahunan yang tidak tersedia tetap kosong.
- **BPS Susenas Maret 2025:** pengeluaran menurut komoditas dan kota/desa. Total Lampung Rp1.239.613 per orang per bulan; perkotaan Rp1.494.565. Keduanya mencakup seluruh penduduk dan tidak dijadikan anggaran otomatis pekerja lajang. Riwayat total Lampung 2021–2025 juga disimpan.
- **BI SHPR:** total IHPR nasional 2021Q1–2026Q2 sebanyak 22 triwulan dan Bandar Lampung 2022Q1–2026Q2 sebanyak 18 triwulan, dasar 2018=100. Bandar Lampung 2025Q2 dan 2026Q2 sama-sama 105,48 pada presisi terbitan. Indeks pasar primer dari survei pengembang ini bukan harga unit di Kalianda atau indeks khusus rumah subsidi.
- **SiKumbang:** satu proyek Menara Siger Residence, Wai Lubuk, Kalianda, Lampung Selatan. Tipe subsidi 36/80 ditawarkan Rp166 juta dan komersial 50/90 Rp350 juta. Tiga blok tampilan menjadi dua baris unik setelah duplikasi dibuang. Harga penawaran bukan transaksi final, bukan rata-rata Lampung, dan unitnya berbeda luas.
- **BP Tapera:** halaman FLPP terkini dan PDF brosur satu halaman berhasil disimpan. Halaman menyebut tenor hingga 40 tahun, sedangkan brosur lama 20 tahun. Simulasi utama memakai tenor 20 tahun sebagai pilihan analisis, bukan klaim batas maksimum program terbaru.

## Verifikasi sumber, tanggal, dan kualitas

| source                  | status                      |            bytes | reference_period                                                      | published   | updated             | revised    |
|:------------------------|:----------------------------|-----------------:|:----------------------------------------------------------------------|:------------|:--------------------|:-----------|
| bps_pengeluaran         | downloaded_no_table_data    |  97609           | nan                                                                   | nan         | nan                 | nan        |
| bps_upah                | downloaded_verified_content | 141898           | February and August 2025; annual cells missing                        | nan         | 2026-07-14 14:13:08 | nan        |
| bps_inflasi_lampung     | downloaded_verified_content | 112876           | January-September 2026                                                | nan         | 2026-10-03 07:52:34 | nan        |
| bi_shpr_2026q2          | downloaded_verified_content | 664287           | 2026Q2; historical annex 2021Q1-2026Q2 nationally; 2022Q1-2026Q2 city | 2026-08-07  | nan                 | nan        |
| sikumbang_menara        | downloaded_verified_content |  17139           | Snapshot 2026-10-30                                                   | nan         | nan                 | nan        |
| tapera_flpp             | downloaded_verified_content | 246737           | nan                                                                   | nan         | nan                 | nan        |
| tapera_brosur           | downloaded_verified_content |      3.57e+06    | Brochure in 2025/09 URL path; exact publication date unavailable      | nan         | nan                 | nan        |
| mandiri_flpp            | downloaded_verified_content | 144622           | nan                                                                   | nan         | nan                 | nan        |
| pkp_tenor               | downloaded_verified_content | 101996           | nan                                                                   | nan         | nan                 | nan        |
| bi_report_page          | downloaded_verified_content | 646462           | 2026Q2; historical annex 2021Q1-2026Q2 nationally; 2022Q1-2026Q2 city | 2026-08-07  | nan                 | nan        |
| bps_publikasi_lampung   | downloaded_verified_content | 125990           | Multiple periods, predominantly 2025                                  | 2026-02-27  | nan                 | 2026-10-27 |
| bps_konsumsi_komoditas  | downloaded_verified_content | 121894           | Susenas March 2025                                                    | nan         | nan                 | nan        |
| bi_shpr_pdf             | failed                      |    nan           | nan                                                                   | nan         | nan                 | nan        |
| bps_lampung_2026_pdf    | downloaded_verified_content |      2.6812e+07  | nan                                                                   | 2026-02-27  | nan                 | 2026-10-27 |
| bi_shpr_pdf_retry       | downloaded_verified_content |      1.98692e+06 | 2026Q2; historical annex 2021Q1-2026Q2 nationally; 2022Q1-2026Q2 city | 2026-08-07  | nan                 | nan        |
| pemprov_inflasi_sep2026 | blocked                     |   5941           | nan                                                                   | nan         | nan                 | nan        |

Setiap berkas tersimpan memiliki URL asal dan akhir, waktu akses UTC, jenis berkas, ukuran byte, SHA256, dan status pada `data/source_manifest.json`. Tanggal publikasi yang tidak diketahui dibiarkan kosong. Tanggal akses tidak diperlakukan sebagai periode observasi.

Temuan audit yang memengaruhi penggunaan data:

1. Tabel BPS pengeluaran kabupaten dari tautan awal mengembalikan **Gagal Memuat Tabel**, walaupun HTTP 200. Tidak ada observasi diambil darinya. Tabel komoditas dan PDF resmi menjadi pengganti.
2. Unduhan PDF BI pertama terputus; percobaan ulang berhasil. Kegagalan pertama tetap tercatat. Kolom tahun dan baris indeks diperiksa secara visual pada halaman 5 PDF.
3. *Lampung Dalam Angka 2026* dirilis 27 Februari 2026, direvisi 27 Oktober 2026. Metadata pembuatan PDF juga menunjukkan 27 Oktober 2026. Tabel 11.1 halaman cetak 682/PDF 730 cocok dengan tabel komoditas: total Lampung Rp1.239.613. Namun, Tabel 11.3 halaman cetak 685/PDF 733 menulis Rp1.494.565 pada baris total Lampung 2025, sama dengan angka perkotaan pada Tabel 11.1. **Ketidaksesuaian tidak diperbaiki diam-diam:** tabel kabupaten disimpan sebagaimana terbit dengan penanda kualitas, dan tidak dipakai dalam model.
4. Tabel inflasi BPS menyimpan sembilan angka Januari–September 2026, tetapi metadatanya tidak menjelaskan basis yoy/mtm. Angka disimpan dengan basis belum ditentukan; tidak dikompaun sebagai inflasi tahunan. September 3,51 cocok dengan berita resmi Pemprov yang menyebut yoy, tetapi unduhan langsung Pemprov diblokir. Berkas lokal Pemprov hanya berisi halaman blokir. **Kenaikan biaya hidup 3% tetap asumsi**, bukan hasil kalibrasi deret ini.
5. Folder URL brosur Tapera memuat 2025/09; metadata pembuatan PDF bertanggal 25 April 2025. Keduanya tidak dianggap tanggal publikasi yang terverifikasi. Halaman program dan listing tidak memperlihatkan tanggal pembaruan yang dapat digunakan. ID proyek juga tidak ditafsirkan sebagai tanggal.

## Asumsi keuangan

| Parameter | Nilai dan status |
|---|---|
| Profil awal | Usia 23 tahun, gaji bersih Rp3 juta/bulan, tabungan Rp0; seluruhnya profil contoh |
| Anggaran awal | Rp2,1 juta: sewa Rp600 ribu, makan Rp750 ribu, transport Rp250 ribu, listrik/data Rp150 ribu, pribadi/kesehatan Rp200 ribu, lainnya Rp150 ribu; asumsi, bukan hasil survei pekerja |
| Pertumbuhan tahunan | Gaji 4%, biaya hidup dan sewa 3%, imbal hasil tabungan neto 3%; asumsi |
| Harga rumah | Harga awal dari listing nyata; harga setara subsidi tetap, komersial naik 3% per tahun; perubahan masa depan adalah asumsi |
| Dana darurat | Enam bulan biaya hidup sebelum membeli; tidak digunakan sebagai DP |
| Biaya awal | Tambahan 3% harga subsidi atau 5% komersial; parameter gabungan, bukan tarif pajak/notaris resmi |
| DP | Minimum 1% subsidi mengikuti iklan program; 20% komersial adalah asumsi. Tabungan di atas biaya awal dan cadangan dipakai menambah DP |
| Subsidi | Bunga nominal 5% tetap, anuitas dalam kasus utama; metode flat diuji terpisah. Bantuan SBUM tidak dikurangkan agar tidak menghitung bantuan dua kali |
| Komersial | Bunga 10% tetap tiga tahun, kemudian disesuaikan tahunan; penilaian awal juga menggunakan bunga uji 13%. Indikator BI 7,44% hanya pembanding agregat, bukan penawaran personal |
| Biaya setelah membeli | Sewa berhenti; komponen lain tetap; pemeliharaan 0,5% harga beli per tahun dan naik mengikuti biaya hidup. Diasumsikan tidak ada tambahan biaya perjalanan |
| Anggaran cicilan | Maksimum 30% gaji, sekaligus menyisakan arus kas minimal 10% gaji setelah cicilan dan biaya hidup/perawatan |
| Kelayakan contoh | Usia saat lunas maksimum 55 tahun mengikuti contoh halaman Mandiri, bukan semua bank; penghasilan lajang FLPP Zona 1 maksimum Rp8,5 juta/bulan dibekukan nominal dalam model |
| Syarat nonfinansial | Rumah pertama, belum menerima subsidi, riwayat kerja memadai, dan tidak punya utang lain diasumsikan terpenuhi; persetujuan kredit tidak dimodelkan |
| Horizon | Akumulasi 40 tahun; tenor utama KPR 20 tahun; tenor 30/40 diuji dengan pembatas usia yang sama |

Kasus tunai dengan harga setara subsidi adalah pembanding matematis. Model tidak menjamin akses pembelian subsidi secara tunai, stok proyek, atau harga kebijakan yang sama selama puluhan tahun.

## Cara perhitungan

Sebelum membeli, setiap akhir bulan saldo diperbarui sebagai:

`B_t = B_(t−1) × (1 + r_t) + gaji_t − biaya_hidup_t`.

Tingkat pertumbuhan tahunan dikonversi secara geometrik menjadi bulanan. Bunga KPR nominal dibagi 12. Defisit mengurangi saldo dan tidak dihapus menjadi nol; model tidak mengarang sumber utang untuk menutupnya.

Tunai membutuhkan harga rumah, biaya awal, dan sisa dana darurat. KPR membutuhkan DP minimum, biaya awal, cadangan, kecukupan cicilan, serta syarat umur/penghasilan. Seluruh tabungan yang tersedia di atas biaya awal dan cadangan dapat memperbesar DP. Angsuran anuitas: `A = P × i / [1 − (1+i)^(-n)]`; flat: `A = P/n + P×i`.

Pembelian terjadi pada akhir bulan; cicilan pertama bulan berikutnya. Keempat alternatif adalah dunia pembanding terpisah, bukan empat pembelian oleh orang yang sama. Model tidak melihat gaji masa depan ketika memutuskan waktu masuk.

Sesudah KPR, pokok, bunga, pengeluaran, dan saldo diperbarui hingga lunas. Bunga komersial berubah setelah 36 cicilan, lalu setiap 12 bulan; cicilan dihitung ulang memakai sisa pokok dan tenor. **Kegagalan likuiditas** berarti saldo negatif setidaknya sekali. **Pelanggaran anggaran** berarti cicilan melampaui 30% gaji atau sisa arus kas kurang dari 10% gaji setidaknya sekali. Pelanggaran anggaran tidak otomatis berarti gagal bayar. Pengujian keberlanjutan ini hanya untuk KPR; model tunai tidak menilai arus kas kehidupan setelah pembelian.

## Monte Carlo: distribusi asumsi dan hasil

Sebanyak **10.000 jalur × 40 tahun**, seed `20261030`. Pertumbuhan setiap tahun diambil dari distribusi normal yang dipotong batas, kemudian dikompaun bulanan dalam tahun itu. Tidak ada korelasi antartahun. Semua parameter distribusi di bawah adalah asumsi, bukan hasil estimasi volatilitas BPS/BI.

| Driver | Rata-rata sebelum pemotongan | Simpangan baku | Batas |
|---|---:|---:|---|
| Gaji | 4% | 6 poin persentase | −20% sampai 25% |
| Biaya hidup/sewa | 3% | 1,5 poin persentase | −2% sampai 15% |
| Harga komersial | 3% | 4 poin persentase | −10% sampai 20% |
| Imbal hasil tabungan neto | 3% | 1 poin persentase | 0% sampai 10% |
| Bunga floating komersial | 10% | 1,5 poin persentase | 6% sampai 15% |

Korelasi gaji–biaya 0,30; gaji–harga 0,20; biaya–harga 0,25. Matriks positif definit; return dan bunga independen dari driver lain. Jalur ekonomi dipakai bersama untuk membandingkan keempat alternatif.

Kasus utama mempertahankan harga subsidi. Eksperimen tambahan memberi peluang asumsi 20% setiap tahun untuk kenaikan harga setara subsidi 5%, yang disebar bulanan dalam tahun tersebut. Ini bukan estimasi probabilitas perubahan kebijakan pemerintah.

Tabel berikut menggunakan persen untuk peluang; waktu dalam tahun. Median dan P10–P90 hanya mencakup jalur yang berhasil dalam 40 tahun. Itu bukan interval keyakinan atau median seluruh pekerja. Median seluruh jalur dengan censoring tersedia terpisah pada `summary.csv` dan kosong bila keberhasilan di bawah 50%.

| segment    | method   |   p_by_age_30 |   p_by_age_35 |   p_by_age_40 |   p_success_40y |   median_years_success_only |   p10_years_success_only |   p90_years_success_only |
|:-----------|:---------|--------------:|--------------:|--------------:|----------------:|----------------------------:|-------------------------:|-------------------------:|
| commercial | cash     |          0    |          0.13 |          7.83 |           84.71 |                       23.75 |                    17.25 |                    34    |
| commercial | kpr      |          0    |          3.87 |          3.87 |            3.87 |                       11.25 |                     9.92 |                    11.92 |
| subsidy    | cash     |          0.34 |         65.52 |         92.3  |           99.11 |                       11    |                     8.58 |                    15.75 |
| subsidy    | kpr      |         96.71 |         98.97 |         98.97 |           98.97 |                        2.75 |                     1.83 |                     4.58 |

KPR subsidi mencapai kriteria masuk sebelum/saat usia 30 pada **96,71% jalur**. Median waktu jalur berhasil 2,75 tahun; P10–P90 sekitar 1,83–4,58 tahun. Namun, **32,01% jalur yang masuk kemudian melanggar anggaran**, dan sekitar **0,18% mengalami saldo negatif**, setidaknya sekali selama masa cicilan. Syarat masuk tidak menjamin anggaran selalu longgar setelahnya.

Dengan eksperimen lonjakan harga subsidi, peluang masuk sebelum/saat usia 30 turun menjadi **94,94%**, sementara peluang tunai sebelum/saat usia 40 turun dari **92,30% menjadi 87,41%**.

Peluang tersebut berlaku dalam model dengan pekerjaan berkelanjutan, penghapusan sewa, DP bertambah, dan asumsi pertumbuhan di atas. Ini bukan persentase pekerja Lampung yang akan disetujui bank. Pada tenor 20 tahun dan batas usia lunas 55, peluang masuk berhenti bertambah setelah usia 35.

Ketidakpastian pengambilan sampel Monte Carlo lebih kecil daripada ketidakpastian asumsi: standar error proporsi `sqrt[p(1−p)/10000]`, maksimum 0,5 poin persentase. Rentang sekitar 95% akibat pengambilan sampel saja maksimum ±0,98 poin. Mengubah asumsi ekonomi dapat mengubah hasil jauh lebih besar.

## Validasi dan batas prediksi

**16 pemeriksaan otomatis lulus**, meliputi anuitas, bunga nol, amortisasi, arah perubahan bunga/tenor, hasil tunai statis 185/389 bulan, kesamaan replikasi deterministik, seed, defisit, aset awal, duplikasi, dan rekonsiliasi subtotal pengeluaran dengan toleransi pembulatan Rp1. Log tersedia pada `results/validation.csv`. Masalah kualitas sumber tetap dicatat meskipun pemeriksaan perhitungan lulus.

Deret IHPR diuji dengan expanding window, minimal delapan triwulan pelatihan dan satu triwulan pengujian. Model pembanding: nilai terakhir (naive) dan perubahan rata-rata sejak awal (drift). Tidak ada pengacakan urutan waktu atau penggunaan data masa depan.

| location         | model   |   n |   mae_index_points |   smape_percent |
|:-----------------|:--------|----:|-------------------:|----------------:|
| Bandar Lampung   | drift   |  10 |           0.376577 |       0.356626  |
| Bandar Lampung   | naive   |  10 |           0.033    |       0.0313346 |
| Nasional 18 kota | drift   |  14 |           0.158651 |       0.144675  |
| Nasional 18 kota | naive   |  14 |           0.327857 |       0.301953  |

Model naive Bandar Lampung lebih baik dalam sampel pendek yang relatif datar. Ini tidak membuktikan harga akan tetap selama 40 tahun. Backtest hanya menguji indeks BI, **tidak memvalidasi probabilitas Monte Carlo, harga Kalianda, atau kelayakan kredit personal**. Tidak dipaksakan model ARIMA/ML untuk membuat ramalan jangka panjang dari sampel yang tidak memadai.

Belum tersedia dalam paket ini: data transaksi berulang per unit, sampel harga representatif, survei biaya pekerja lajang, riwayat gaji individu, skor kredit, atau distribusi kehilangan pekerjaan. Model belum mencakup PHK, penambahan tanggungan, THR, bantuan keluarga, renovasi besar, biaya pindah, depresiasi rumah, dan perubahan aturan/usia/penghasilan bank. Karena itu, hasil harus disebut **simulasi skenario keterjangkauan**, bukan prediksi empiris yang sudah terkalibrasi.

## Alur carousel Fabio Banyu Cyto

Judul: **“Gaji Rp3 Juta: DP Rumah Cepat Terkumpul, Cicilannya Aman?”**

1. Tampilkan profil contoh: gaji bersih Rp3 juta, usia 23, biaya hidup Rp2,1 juta, tabungan awal nol.
2. Perlihatkan dua listing nyata Kalianda: Rp166 juta dan Rp350 juta; jelaskan bahwa ini bukan harga rata-rata Lampung.
3. Bedakan DP minimum Rp1,66 juta dari kebutuhan dana awal, biaya transaksi, dan dana darurat.
4. Cicilan anuitas 20 tahun dengan DP minimum sekitar Rp1,085 juta, melebihi 30% gaji awal. Jelaskan asumsi bunga.
5. DP bertambah dan gaji naik 4% dalam skenario dasar menghasilkan waktu 33 bulan; itu bukan janji persetujuan bank.
6. Tunai 10 tahun 9 bulan berlaku dalam skenario harga setara subsidi tetap dan gaji meningkat.
7. Tampilkan variasi Monte Carlo beserta pelanggaran anggaran setelah masuk, bukan hanya angka keberhasilan.
8. Akhiri dengan sumber, tanggal, asumsi, dan tautan notebook. Hindari klaim “97% pekerja Lampung pasti punya rumah”.

## Sumber resmi dan status akses

- [bps_pengeluaran](https://lampung.bps.go.id/id/statistics-table/3/V1ZKMWVrSTNOek5ZZUZOcVZEZGFValJvV0hWalFUMDkjMw%3D%3D/monthly-average-of-food-and-non-food-expenditure-per-capita-in-urban-and-rural-areas-by-regency-municipality-in-lampung-province--rupiahs---2023.html) — downloaded_no_table_data.
- [bps_upah](https://www.bps.go.id/id/statistics-table/2/MjQ3NSMy/rata-rata-upah-gaji-bersih-sebulan-buruh-karyawan-pegawai-menurut-provinsi-dan-lapangan-pekerjaan-utama-di-17-sektor--rupiah-.html) — downloaded_verified_content.
- [bps_inflasi_lampung](https://lampung.bps.go.id/id/statistics-table/2/MjA1IzI%3D/inflasi.html) — downloaded_verified_content.
- [bi_shpr_2026q2](https://www.bi.go.id/id/publikasi/ruang-media/news-release/pages/sp_2815226.aspx) — downloaded_verified_content.
- [sikumbang_menara](https://sikumbang.tapera.go.id/lokasi-perumahan/KLA0610282026T001) — downloaded_verified_content.
- [tapera_flpp](https://www.tapera.go.id/kpr-flpp/) — downloaded_verified_content.
- [tapera_brosur](https://www.tapera.go.id/wp-content/uploads/2025/09/mitra-brosur.pdf) — downloaded_verified_content.
- [mandiri_flpp](https://www.bankmandiri.co.id/in/kredit-pemilikan-rumah-bersubsidi) — downloaded_verified_content.
- [pkp_tenor](https://pkp.go.id/berita/detail/setujui-tenor-kpr-flpp-hingga-40-tahun-pemerintah-pertahankan-suku-bunga-rumah-subsidi-5-persen-dan-rusun-subsidi-6-persen) — downloaded_verified_content.
- [bi_report_page](https://www.bi.go.id/id/publikasi/laporan/Pages/SHPR_Tw_II_2026.aspx) — downloaded_verified_content.
- [bps_publikasi_lampung](https://lampung.bps.go.id/id/publication/2026/02/27/71de40a96c9fb7130aae19e3/provinsi-lampung-dalam-angka-2026.html) — downloaded_verified_content.
- [bps_konsumsi_komoditas](https://lampung.bps.go.id/id/statistics-table/3/VTJaSFFtWklXVnBYZVdSREwyczJlbm93UWpVM1FUMDkjMw%3D%3D/rata-rata-pengeluaran-per-kapita-sebulan-menurut-kelompok-komoditas-dan-klasifikasi-desa-di-provinsi-lampung--rupiah---2023.html?year=2025) — downloaded_verified_content.
- [bi_shpr_pdf](https://www.bi.go.id/id/publikasi/laporan/Documents/SHPR_Tw_II_2026.pdf) — failed.
- [bps_lampung_2026_pdf](https://webapi.bps.go.id/download.php?f=AQAD9WkkUfVaS7L_XrKOrJuLyrD4HheUKiCoog4u04YM5sneaPSK35BLaCCqBt5eOp5HazECLya2_0ZYd2yyPUumox8IE-q00UEEgpNOCWUVYsndhTJgJL7si_iP4v44KHJd1QU2og0yaObWBi4rXAZzzbi2OUkaCO4hgAG7nas3H8vUArYd9zudArhT-DpyChYw1-F8BA6om__nd2hJTv_EghB5OOdbP9Mj0Upt6RdsODrzLbm10K3Eppjh5P8AbQIM7f96fG8WV7AHA95zw6sh3-4Mgiso8LlbobPOSyIV) — downloaded_verified_content.
- [bi_shpr_pdf_retry](https://www.bi.go.id/id/publikasi/laporan/Documents/SHPR_Tw_II_2026.pdf) — downloaded_verified_content.
- [pemprov_inflasi_sep2026](https://www.lampungprov.go.id/index.php/detail-post/inflasi-lampung-terendah-di-sumatera-gubernur-mirza-tegaskan-harga-dijaga) — blocked.
