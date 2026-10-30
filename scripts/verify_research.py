"""Validate the published research snapshot without downloading or rerunning Monte Carlo."""
from pathlib import Path
import hashlib,json,sys
import pandas as pd
import nbformat

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import model

def main():
    manifest=json.loads((ROOT/'data/source_manifest.json').read_text(encoding='utf-8'))
    checked=0
    for record in manifest:
        if record.get('raw_file'):
            path=ROOT/record['raw_file']
            assert path.exists(),path
            assert path.stat().st_size==record['bytes'],path
            assert hashlib.sha256(path.read_bytes()).hexdigest()==record['sha256'],path
            checked+=1
    notebook=nbformat.read(ROOT/'analisis_lampung.ipynb',as_version=4)
    nbformat.validate(notebook)
    assert all(c.execution_count is not None for c in notebook.cells if c.cell_type=='code')
    assert not any(o.output_type=='error' for c in notebook.cells if c.cell_type=='code' for o in c.outputs)
    for name in ['monte_carlo_paths.csv','monte_carlo_policy_jump_paths.csv']:
        data=pd.read_csv(ROOT/'results'/name)
        assert len(data)==40000,name
        assert data.groupby(['segment','method']).size().eq(10000).all(),name
        entered=data[(data.method=='kpr')&data.purchase_age.notna()]
        assert (entered.scheduled_payoff_age<=55+1e-8).all(),name
    checks=model.validation()
    print(f'PASS: {checked} source hashes, notebook outputs, Monte Carlo snapshot, {len(checks)} model checks.')

if __name__=='__main__': main()
