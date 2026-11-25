import pathlib
p = pathlib.Path('index.html')
t = p.read_text()
reviews = '''<h2>آراء الزبائن</h2><div style="display:grid;gap:12px">
<div style="background:#1e293b;padding:16px;border-radius:14px">⭐⭐⭐⭐⭐<br><b>أحمد - بنغازي</b><br>ركب لي كاميرات للبيت، شغل نظيف وسريع والسعر واضح من البداية.</div>
<div style="background:#1e293b;padding:16px;border-radius:14px">⭐⭐⭐⭐⭐<br><b>مريم - بنغازي</b><br>صمم لي موقع لمشروعي، الشغل طلع احترافي والتعامل راقي.</div>
<div style="background:#1e293b;padding:16px;border-radius:14px">⭐⭐⭐⭐⭐<br><b>محمد - بنغازي</b><br>ظبط لي شبكة المحل كلها، ومن يومها النت ثابت وما قطع.</div>
</div><br>'''
if 'آراء الزبائن' not in t:
    t = t.replace('<h2>اطلب خدمتك</h2>', reviews + '<h2>اطلب خدمتك</h2>')
p.write_text(t)
print('reviews done')
