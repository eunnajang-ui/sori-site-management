"""template.html 의 __DATA__ 자리에 데이터(JSON)를 넣어 index.html 을 만든다.
사용: python make_page.py sample_data.json index.html
회사 안에서는 실제 원자료(엑셀)에서 만든 data.json 을 넣는다 (docs/데이터구조.md 참고).
"""
import sys, pathlib
here = pathlib.Path(__file__).parent
data = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else here / 'sample_data.json').read_text(encoding='utf-8')
out = pathlib.Path(sys.argv[2] if len(sys.argv) > 2 else here / 'index.html')
tpl = (here / 'template.html').read_text(encoding='utf-8')
out.write_text(tpl.replace('__DATA__', data.replace('</', '<\\/')), encoding='utf-8')
print('written', out)
