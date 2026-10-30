from pathlib import Path
import json,re,itertools,hashlib
import pandas as pd
from bs4 import BeautifulSoup
from pypdf import PdfReader
ROOT=Path(__file__).resolve().parents[1]; RAW=ROOT/'data'/'raw'; DATA=ROOT/'data'/'processed'; DATA.mkdir(exist_ok=True)
manifest=json.loads((ROOT/'data'/'source_manifest.json').read_text())
def csv(rows,name): pd.DataFrame(rows).to_csv(DATA/(name+'.csv'),index=False,encoding='utf-8-sig')
def embedded(name): return json.loads((RAW/(name+'_embedded.json')).read_text(encoding='utf-8'))
# Preserve missing cells as missing, not zero. Keys follow dimensions explicitly.
a=embedded('bps_upah'); rows=[]
for geo,var,sector,yr,period in itertools.product(a['vervar'],a['var'],a['turvar'],a['tahun'],a['turtahun']):
    key=''.join(str(x['val']) for x in [geo,var,sector,yr,period]); val=a['datacontent'].get(key)
    rows.append(dict(province_code=geo['val'],province=geo['label'],year=int(yr['label']),period=period['label'],sector=sector['label'],wage_idr_month=val,missing=val is None,source_id='bps_upah',source_key=key,data_class='observed_aggregate'))
csv(rows,'bps_upah_2025')
a=embedded('bps_konsumsi_komoditas')['data'][1]; rows=[]
for r in a['data']:
    for cid,c in a['kolom'].items():
        vars=r.get('variables'); v=vars.get(cid) if isinstance(vars,dict) else None
        raw=v.get('value_raw') if v else None
        num=int(raw.replace('.','')) if raw and re.fullmatch(r'[\d.]+',raw) else None
        commodity=BeautifulSoup(r['label_raw'],'html.parser').get_text().strip()
        rows.append(dict(province='Lampung',period='2025-03',commodity=commodity,area=c['nama_variabel'].split(' - ')[-1],expenditure_idr_capita_month=num,raw_value=raw,data_class='observed_aggregate',source_id='bps_konsumsi_komoditas'))
csv(rows,'bps_pengeluaran_lampung_2025')
a=embedded('bps_inflasi_lampung'); rows=[]
for m in a['vervar']:
    if m['val']>12: continue
    key=f"{m['val']}20501260"; v=a['datacontent'].get(key)
    rows.append(dict(province='Lampung',period=f"2026-{m['val']:02}",value_percent=v,measure='inflation_table_unspecified_basis',interpretation='September 3.51 cross-checked as yoy; table metadata does not specify basis',source_id='bps_inflasi_lampung',source_key=key,data_class='observed_aggregate'))
csv(rows,'bps_inflasi_lampung_2026')
# Extract property type blocks, remove duplicate listing of same project/type/spec/price.
s=BeautifulSoup((RAW/'sikumbang_menara.html').read_bytes(),'html.parser'); txt=s.get_text(' ',strip=True)
pat=r'Tipe ([\d/]+) \((subsidi|komersil)\).*?Harga: Rp ([\d.]+).*?Luas Bangunan: (\d+)\s*m.*?Luas Lahan: (\d+)\s*m'
rows=[]
for typ,kind,price,building,land in re.findall(pat,txt):
    rows.append(dict(project_id='KLA0610282026T001',project='Menara Siger Residence',province='Lampung',regency='Lampung Selatan',district='Kalianda',village='Wai Lubuk',type=typ,segment=kind,price_idr=int(price.replace('.','')),building_m2=int(building),land_m2=int(land),snapshot_date='2026-10-30',listing_updated_date=None,source_id='sikumbang_menara',data_class='observed_asking_price'))
raw_count=len(rows); df=pd.DataFrame(rows).drop_duplicates(); assert len(df)==2 and raw_count==3
df.to_csv(DATA/'sikumbang_harga_lampung.csv',index=False,encoding='utf-8-sig')
# The total IHPR lines have clean spacing. Verify against visual page 5 separately.
r=PdfReader(RAW/'bi_shpr_pdf_retry.pdf'); texts=[p.extract_text() for p in r.pages]; (RAW/'bi_shpr_pdf_retry.txt').write_text('\n'.join(texts),encoding='utf-8')
t=texts[4]; total_lines=[line for line in t.splitlines() if line.startswith('T OT AL')]
national=[float(x.replace(',','.')) for x in re.findall(r'\d+,\d+',total_lines[0])]
lampung=[float(x.replace(',','.')) for x in re.findall(r'\d+,\d+',total_lines[2])]
assert len(national)==22 and len(lampung)==18,(len(national),len(lampung))
rows=[]
for location,vals,start in [('Nasional 18 kota',national,'2021Q1'),('Bandar Lampung',lampung,'2022Q1')]:
    for per,val in zip(pd.period_range(start,periods=len(vals),freq='Q'),vals):
        rows.append(dict(location=location,quarter=str(per),ihpr_total=val,base_year=2018,market='primary_developer_survey',source_id='bi_shpr_pdf_retry',locator='PDF page 5; Table 1 or 2; TOTAL row',data_class='observed_index'))
csv(rows,'bi_ihpr')
# Downloaded PDF cross-check and district table, kept as reported with explicit flag.
book=PdfReader(RAW/'bps_lampung_2026_pdf.pdf'); page=book.pages[732].extract_text(); district=[]
for line in page.splitlines():
    nums=re.findall(r'[\d.]+,\d\d',line)
    if len(nums)!=6: continue
    location=line[:line.find(nums[0])].strip()
    for year,j in [(2024,0),(2025,1)]:
        vals=[int(float(nums[k].replace('.','').replace(',','.'))) for k in [j,j+2,j+4]]
        district.append(dict(location=location,year=year,food_idr_capita_month=vals[0],nonfood_idr_capita_month=vals[1],total_idr_capita_month=vals[2],source_id='bps_lampung_2026_pdf',locator='PDF page733; printed685; Table11.3',quality_flag='province2025_equals_urban_total_conflicts_with_table11.1' if location=='Lampung' and year==2025 else 'table_contains_province_total_conflict',used_in_model=False))
csv(district,'bps_pengeluaran_kabupaten_as_reported')
csv([dict(province='Lampung',year=yr,total_idr_capita_month=val,source_id='bps_lampung_2026_pdf',locator='PDF page727; printed679; Figure11.1',data_class='observed_aggregate') for yr,val in zip(range(2021,2026),[1030579,1074987,1203017,1201473,1239613])],'bps_pengeluaran_history')
# Policy facts are separate from cashflow assumptions.
csv([
dict(parameter='flpp_rate_advertised',value=5,unit='percent_pa',source_id='tapera_flpp',note='Page says flat; model uses nominal annual annuity assumption, with flat sensitivity.'),
dict(parameter='flpp_dp_min',value=1,unit='percent_price',source_id='tapera_flpp',note='minimum advertised, not all upfront charges'),
dict(parameter='flpp_tenor_advertised',value=40,unit='years',source_id='tapera_flpp',note='current downloaded page; older brochure 20 years; actual bank approval required'),
dict(parameter='flpp_tenor_brochure',value=20,unit='years',source_id='tapera_brosur',note='2025/09 URL folder; publication day not shown'),
dict(parameter='flpp_income_cap_single_zone1',value=8500000,unit='idr_month',source_id='tapera_flpp',note='Lampung/Sumatera zone1; assumed constant in model'),
dict(parameter='mandiri_max_age_at_maturity',value=55,unit='years',source_id='mandiri_flpp',note='bank-specific; used as conservative eligibility scenario, not universal rule'),
dict(parameter='bi_kpr_rate_2026q2',value=7.44,unit='percent_pa',source_id='bi_shpr_pdf_retry',note='PDF page3; aggregate bank lending indicator; not personalized offer'),
], 'policy_reference')
for m in manifest:
    sid=m['source_id']; f=ROOT/m.get('raw_file','missing')
    if m['status'] in ['failed','blocked']: continue
    m['status']='downloaded_verified_content'
    if sid=='bps_pengeluaran': m.update(status='downloaded_no_table_data',extraction_note='Gagal Memuat Tabel; no observations used')
    if sid in ['bps_upah','bps_inflasi_lampung']: m['last_updated']=embedded(sid)['last_update']
    if sid=='bps_konsumsi_komoditas': m.update(reference_period='Susenas March 2025',table_created=a.get('table_created') if False else embedded(sid)['data'][1]['table_created'],extraction_note='Embedded source3 JSON; created field is response generation, not publication date')
    if sid=='bps_upah': m['reference_period']='February and August 2025; annual cells missing'
    if sid=='bps_inflasi_lampung': m.update(reference_period='January-September 2026',extraction_note='Basis missing in table; September verified yoy independently in official regional government page; no annual compounding of this series')
    if sid in ['bi_shpr_2026q2','bi_report_page','bi_shpr_pdf_retry']: m.update(published_date='2026-08-07',reference_period='2026Q2; historical annex 2021Q1-2026Q2 nationally; 2022Q1-2026Q2 city')
    if sid=='bps_publikasi_lampung': m.update(published_date='2026-02-27',revised_date='2026-10-27',reference_period='Multiple periods, predominantly 2025')
    if sid=='bps_lampung_2026_pdf': m.update(published_date='2026-02-27',revised_date='2026-10-27',pdf_creation_metadata='D:20261027152202+00',extraction_note='Table11.1 PDF730 cross-check; history Figure11.1 PDF727; district Table11.3 PDF733 retained as reported and excluded from model due province2025 conflict')
    if sid=='sikumbang_menara': m.update(reference_period='Snapshot 2026-10-30',extraction_note='3 raw blocks, 2 unique price/type/spec rows; no published/update date exposed; project ID is not publication date')
    if sid=='tapera_brosur': m.update(reference_period='Brochure in 2025/09 URL path; exact publication date unavailable',pdf_creation_metadata='D:20250425113057+07',extraction_note='PDF creation is not publication date; one page; 20-year brochure vs current page40 years')
(ROOT/'data'/'source_manifest.json').write_text(json.dumps(manifest,ensure_ascii=False,indent=2),encoding='utf-8')
pd.DataFrame(manifest).to_csv(ROOT/'data'/'source_manifest.csv',index=False,encoding='utf-8-sig')
print('Wrote',[(p.name,len(pd.read_csv(p))) for p in DATA.glob('*.csv')])
