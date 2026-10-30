from pathlib import Path
from bs4 import BeautifulSoup
import re,json
from pypdf import PdfReader
P=Path(__file__).resolve().parents[1]/'data'/'raw'
for name in ['bps_inflasi_lampung','bps_upah','bps_pengeluaran','bps_konsumsi_komoditas']:
    html=(P/(name+'.html')).read_text(encoding='utf-8')
    streams=[]
    for m in re.finditer(r'self\.__next_f\.push\((\[.*?\])\)',html):
        try:
            x=json.loads(m.group(1))
            if len(x)>1 and isinstance(x[1],str): streams.append(x[1])
        except json.JSONDecodeError: pass
    stream=''.join(streams); (P/(name+'_decoded.txt')).write_text(stream,encoding='utf-8')
    for m in re.finditer(r'\{"status":"OK"',stream):
        try:
            obj,_=json.JSONDecoder().raw_decode(stream[m.start():]); (P/(name+'_embedded.json')).write_text(json.dumps(obj,ensure_ascii=False,indent=2),encoding='utf-8'); print(name,list(obj),len(str(obj)))
        except json.JSONDecodeError: pass
for name in ['bps_lampung_2026_pdf','tapera_brosur']:
    f=P/(name+'.pdf')
    if f.exists():
        reader=PdfReader(f)
        pages=[f'\n=== PDF PAGE {i+1} ===\n'+(pg.extract_text() or '') for i,pg in enumerate(reader.pages)]
        (P/(name+'.txt')).write_text(''.join(pages),encoding='utf-8')
        print(name,'pages',len(pages),'metadata',reader.metadata)
        if name=='bps_lampung_2026_pdf':
            for i,p in enumerate(pages):
                if any(s.lower() in p.lower() for s in ['1.239.613','1 239 613','2.520.619','Rata-Rata Pengeluaran per Kapita Sebulan Menurut Kelompok']):
                    print('MATCH page',i+1,p[:500])
