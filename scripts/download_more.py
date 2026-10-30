from download_sources import download,ROOT,RAW
import json,concurrent.futures
items={
'bi_report_page':'https://www.bi.go.id/id/publikasi/laporan/Pages/SHPR_Tw_II_2026.aspx',
'bps_publikasi_lampung':'https://lampung.bps.go.id/id/publication/2026/02/27/71de40a96c9fb7130aae19e3/provinsi-lampung-dalam-angka-2026.html',
'bps_konsumsi_komoditas':'https://lampung.bps.go.id/id/statistics-table/3/VTJaSFFtWklXVnBYZVdSREwyczJlbm93UWpVM1FUMDkjMw%3D%3D/rata-rata-pengeluaran-per-kapita-sebulan-menurut-kelompok-komoditas-dan-klasifikasi-desa-di-provinsi-lampung--rupiah---2023.html?year=2025',
}
if __name__=='__main__':
    r=list(concurrent.futures.ThreadPoolExecutor(max_workers=3).map(download,items.items()))
    p=ROOT/'data'/'source_manifest.json'; m=json.loads(p.read_text()); m.extend(r); p.write_text(json.dumps(m,indent=2),encoding='utf-8')
    for x in r:
        print(x['source_id'],x['status'],x.get('bytes'))
        lp=RAW/(x['source_id']+'_links.json')
        if lp.exists():
            for y in json.loads(lp.read_text(encoding='utf-8')):
                if any(z in y['href'].lower() for z in ['.pdf','download','unduh']): print(y)
