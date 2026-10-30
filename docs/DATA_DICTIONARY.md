# Kamus data

Semua nilai IDR nominal. Kategori provenance: observed_aggregate=BPS agregat survei; observed_index=BI indeks; observed_asking_price=harga listing SiKumbang. Angka masa depan di model adalah assumed_parameter, hasil di results adalah simulated_output. Tidak ada tabel hasil simulasi dicampur ke observasi.

| Berkas data/processed | Unit baris dan kolom penting | Missing / batas |
|---|---|---|
| bps_upah_2025.csv | provinsi×sektor×periode2025; wage_idr_month rupiah/bulan; source_key dimensi asli | Tahunan dan sel tak tersedia kosong, missing=True; jangan jumlahkan sektor/mean tanpa bobot |
| bps_pengeluaran_lampung_2025.csv | komoditas×kota/desa/kota+desa; expenditure_idr_capita_month rupiah/orang/bulan; raw_value mempertahankan format asli | Baris judul makanan/bukanmakanan kosong; total/subtotal bukan item tambahan |
| bps_pengeluaran_history.csv | total Lampung×tahun2021–2025; rupiah/orang/bulan | Agregat Susenas, bukan IHK/biaya individu |
| bps_pengeluaran_kabupaten_as_reported.csv | kabupaten/provinsi×2024/2025, makanan/nonmakanan/total | Disimpan sebagaimana tabel11.3; masalah totalprovinsi2025; used_in_model=False |
| bps_inflasi_lampung_2026.csv | bulan2026; value_percent; metadata basis belumditentukan | Oktober–Desember kosong; jangan isikan0/kompaun yoy |
| bi_ihpr.csv | lokasi×triwulan; ihpr_total; base_year2018 | Nasional18kota vs BandarLampung; awalperiodenya berbeda; ini indeks, bukanRp |
| sikumbang_harga_lampung.csv | proyek×tipe×segmenunik; price_idr; building_m2; land_m2 | listing_updated_date kosong; snapshot_date tanggalakses |
| policy_reference.csv | parameterpublik×sumber | Ketentuanprogram/indikatorbunga bukanobservasipersonal; bedakan flat/anuitas |

Metadata URL, tanggalaksesUTC, tanggalrilis/pembaruan/revisi, periodeobservasi, tipeberkas, bytes, SHA256 dan status unduhan tersedia pada data/source_manifest.json/csv. Tanggalnull berarti tidak diketahui. Tidak ditebak dariID atau hakciptafooter.

| Berkas results | Arti |
|---|---|
| deterministic.csv | 4alternatif profilcontoh; dp_ready_month hanya DPminimum+biaya+cadangan; purchase_month syaratmasuklengkap; scheduled_payoff_age hanyaKPR |
| deterministic_monthly.csv | jejakbulanan4alternatif; harga/saldo/gaji/cicilan; setelahbeli saldo berubah ke sisa dana |
| monte_carlo_paths.csv | 10.000jalur×4alternatif; path_id sama berarti jalurekonomi sama; kosong purchase_month berarti tidaktercapai hingga40tahun |
| monte_carlo_policy_jump_paths.csv | tambahan10.000jalur dengan ketidakpastianharga setarasubsidi |
| summary.csv | probabilitas0–1; waktu dalamtahun; p_by_age_X meliputi≤usiaX; median_years_success_only kondisional; median_years_all_paths memasukkan right-censoring dan kosong bila<50%berhasil |
| sensitivity.csv | ubahsatuasumsi; NaN=takberhasil; 30/40tahun tetapmemakai batasusia55 kecuali variabeldiubah |
| mortgage_sensitivity.csv | cicilanmatematis anuitas danflat dari DPminimum; bukanjaminanprodukbank |
| backtest_folds.csv / backtest_summary.csv | expandingwindow minimal8periode, horizon1triwulan; MAE poinindeks, sMAPE persen |
| validation.csv | asersi dan status; kegagalanprogram akan menghentikan proses |
| observed_context.csv / download_audit.csv | ringkasankonteksdan auditstatusunduhan |

assumptions.json mendokumentasikan semua parameter BASE yang digunakan. wage_sd/cost_sd/house_sd/return_sd adalah simpanganbaku absolut tingkatpertumbuhantahunan (0.06=6poinpersentase). saving_return neto, fee bukan tarifresmi. Model menganggaptidakada utanglain dan danaawal0. Class hasil tidak setara probabilitasempiris.
