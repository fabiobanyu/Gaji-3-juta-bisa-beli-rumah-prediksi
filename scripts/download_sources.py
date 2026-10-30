from pathlib import Path
import requests, json, hashlib, datetime, concurrent.futures
from bs4 import BeautifulSoup

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/'data'/'raw'; RAW.mkdir(parents=True,exist_ok=True)
SOURCES={
'bps_pengeluaran':'https://lampung.bps.go.id/id/statistics-table/3/V1ZKMWVrSTNOek5ZZUZOcVZEZGFValJvV0hWalFUMDkjMw%3D%3D/monthly-average-of-food-and-non-food-expenditure-per-capita-in-urban-and-rural-areas-by-regency-municipality-in-lampung-province--rupiahs---2023.html',
'bps_upah':'https://www.bps.go.id/id/statistics-table/2/MjQ3NSMy/rata-rata-upah-gaji-bersih-sebulan-buruh-karyawan-pegawai-menurut-provinsi-dan-lapangan-pekerjaan-utama-di-17-sektor--rupiah-.html',
'bps_inflasi_lampung':'https://lampung.bps.go.id/id/statistics-table/2/MjA1IzI%3D/inflasi.html',
'bi_shpr_2026q2':'https://www.bi.go.id/id/publikasi/ruang-media/news-release/pages/sp_2815226.aspx',
'sikumbang_menara':'https://sikumbang.tapera.go.id/lokasi-perumahan/KLA0610282026T001',
'tapera_flpp':'https://www.tapera.go.id/kpr-flpp/',
'tapera_brosur':'https://www.tapera.go.id/wp-content/uploads/2025/09/mitra-brosur.pdf',
'mandiri_flpp':'https://www.bankmandiri.co.id/in/kredit-pemilikan-rumah-bersubsidi',
'pkp_tenor':'https://pkp.go.id/berita/detail/setujui-tenor-kpr-flpp-hingga-40-tahun-pemerintah-pertahankan-suku-bunga-rumah-subsidi-5-persen-dan-rusun-subsidi-6-persen',
}
def download(item):
    sid,url=item
    record=dict(source_id=sid,url_requested=url,retrieved_at_utc=datetime.datetime.now(datetime.timezone.utc).isoformat(),research_as_of='2026-10-30',published_date=None,reference_period=None)
    try:
        r=requests.get(url,timeout=50,headers={'User-Agent':'Mozilla/5.0 (Fabio Banyu Cyto academic affordability research)'})
        ext='.pdf' if r.content.startswith(b'%PDF') else '.html'
        dest=RAW/(sid+ext); dest.write_bytes(r.content)
        soup=BeautifulSoup(r.content,'html.parser') if ext=='.html' else None
        txt=soup.get_text('\n',strip=True) if soup else ''
        if soup: (RAW/(sid+'.txt')).write_text(txt,encoding='utf-8')
        rejected=any(x in txt.lower() for x in ['requested url was rejected','access denied','just a moment...','verify you are human'])
        record.update(http_status=r.status_code,final_url=r.url,content_type=r.headers.get('Content-Type'),bytes=len(r.content),sha256=hashlib.sha256(r.content).hexdigest(),raw_file=str(dest.relative_to(ROOT)).replace('\\','/'),status='blocked' if rejected or not r.ok else 'downloaded_unreviewed')
        if soup:
            links=[{'text':a.get_text(' ',strip=True),'href':requests.compat.urljoin(r.url,a['href'])} for a in soup.select('a[href]')]
            (RAW/(sid+'_links.json')).write_text(json.dumps(links,ensure_ascii=False,indent=2),encoding='utf-8')
    except Exception as e: record.update(status='failed',error=str(e))
    return record
if __name__=='__main__':
    results=list(concurrent.futures.ThreadPoolExecutor(max_workers=6).map(download,SOURCES.items()))
    (ROOT/'data'/'source_manifest.json').write_text(json.dumps(results,ensure_ascii=False,indent=2),encoding='utf-8')
    print(json.dumps(results,ensure_ascii=False,indent=2))
