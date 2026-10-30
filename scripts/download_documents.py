from download_sources import download,ROOT,RAW
import json,concurrent.futures
items={}
for parent,child in [('bi_report_page','bi_shpr_pdf'),('bps_publikasi_lampung','bps_lampung_2026_pdf')]:
    links=json.loads((RAW/(parent+'_links.json')).read_text(encoding='utf-8'))
    matches=[x for x in links if '.pdf' in x['href'].lower() or 'download.php' in x['href']]
    if matches: items[child]=matches[0]['href']
if __name__=='__main__':
    r=list(concurrent.futures.ThreadPoolExecutor(max_workers=2).map(download,items.items()))
    p=ROOT/'data'/'source_manifest.json'; m=json.loads(p.read_text()); m.extend(r); p.write_text(json.dumps(m,indent=2),encoding='utf-8')
    for x in r: print(x['source_id'],x['status'],x.get('bytes'),x.get('content_type'))
