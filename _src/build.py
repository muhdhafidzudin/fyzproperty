"""Build index.html from _src/template.html + _src/site.json.
Images live in img/<id>.jpg (full) and img/t/<id>.jpg (thumb). Run: python3 _src/build.py"""
import json,os
R=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S=json.load(open(os.path.join(R,'_src/site.json')))
f=lambda i:'img/'+i+'.jpg'
D={'settings':S['settings'],'listings':S['listings'],'imgBase':'img/',
   'hero':[f(i) for i in S['hero']],'about':f(S['about']),'svc':[f(i) for i in S['svc']],'band':f(S['band']),
   'areaImg':{k:'img/t/'+v+'.jpg' for k,v in S['areaImg'].items()}}
url='https://muhdhafidzudin.github.io/fyzproperty/'
desc='FYZ PROPERTY — One Stop Centre hartanah Kedah & Perlis. Rumah subsale, projek baru dan tanah di Kota Setar, Sungai Petani, Kubang Pasu, Pendang, Baling & Kangar. WhatsApp 012-569 0675.'
head=f'''<title>FYZ PROPERTY | Rumah Dijual Kedah &amp; Perlis — Subsale, Projek Baru, Tanah</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="website"><meta property="og:site_name" content="FYZ PROPERTY"><meta property="og:title" content="FYZ PROPERTY — Rumah Dijual Kedah &amp; Perlis">
<meta property="og:description" content="{desc}"><meta property="og:url" content="{url}"><meta property="og:image" content="{url}{f(S['hero'][0])}">
<meta name="twitter:card" content="summary_large_image">
<link rel="icon" href="data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 64 64'%3E%3Crect width='64' height='64' rx='14' fill='%230B1B33'/%3E%3Cpath d='M14 34 32 18l18 16v14H14z' fill='none' stroke='%23C9A24A' stroke-width='5' stroke-linejoin='round'/%3E%3C/svg%3E">
<script type="application/ld+json">{{"@context":"https://schema.org","@type":"RealEstateAgent","name":"FYZ PROPERTY","url":"{url}","telephone":"+60125690675","areaServed":["Kedah","Perlis"],"image":"{url}{f(S['hero'][0])}"}}</script>'''
# crawlable list of listings for Google (hidden visually, real links)
items=''.join(f'<li><a href="#l-{l["id"]}">{l["tajuk"]} — {l.get("jenis","")}, {l["daerah"]}, {l["negeri"]}</a></li>' for l in S['listings'])
seo=f'<noscript><ul>{items}</ul></noscript>'
t=open(os.path.join(R,'_src/template.html')).read()
t=t.replace('<title>FYZ PROPERTY</title>',head,1).replace('/*DATA*/',json.dumps(D,ensure_ascii=False).replace('</','<\\/'),1).replace('<footer>',seo+'\n<footer>',1)
open(os.path.join(R,'index.html'),'w').write(t)
print('built',len(S['listings']),'listings')
