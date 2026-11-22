"""Buat gambar hiasan (hero/about/svc/band/areaImg) tanpa no fon: crop 12% bawah dari img/<id>.jpg ke img/d/<id>.jpg."""
import json,os
from PIL import Image
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S=json.load(open(os.path.join(R,'_src/site.json')))
ids=set(S['hero'])|{S['about'],S['band']}|set(S['svc'])|set(S['areaImg'].values())
os.makedirs(os.path.join(R,'img/d'),exist_ok=True)
for i in ids:
    im=Image.open(os.path.join(R,'img',i+'.jpg')).convert('RGB'); W,H=im.size
    im=im.crop((0,0,W,int(H*0.88))); im.thumbnail((1600,1600),Image.LANCZOS); im.save(os.path.join(R,'img/d',i+'.jpg'),quality=86)
print('deco',len(ids))
