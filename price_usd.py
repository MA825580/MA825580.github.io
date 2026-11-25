import pathlib
p = pathlib.Path('index.html')
t = p.read_text()
prices = '''<h2>أسعار تقريبية</h2><div style="background:#0f172a;padding:18px;border-radius:14px;text-align:right;line-height:2">
<div>تركيب شبكات: <b>من 30$</b></div>
<div>تركيب كاميرات: <b>من 25$ للكاميرا</b></div>
<div>أمن سيبراني: <b>من 40$</b></div>
<div>تصميم موقع: <b>من 70$</b></div>
<div>إنشاء تطبيق: <b>من 160$</b></div>
<div>بوت واتساب: <b>من 50$</b></div>
<div style="font-size:13px;opacity:.8">السعر النهائي حسب المعاينة والمكان.</div>
</div><br>'''
if 'أسعار تقريبية' not in t:
    t = t.replace('<h2>اطلب خدمتك</h2>', prices + '<h2>اطلب خدمتك</h2>')
p.write_text(t)
print('usd done')
