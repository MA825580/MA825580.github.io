with open('index.html', encoding='utf-8') as f:
    html = f.read()

cv = """
<h2>السيرة الذاتية</h2>
<div class="card">
<p><b>الاسم:</b> محوالدين قعفر موسى - Mahualdeen Gafar Mosa</p>
<p><b>المجال:</b> مطور مواقع | بناء مواقع شخصية ومواقع أعمال</p>
</div>

<h2>التعليم</h2>
<div class="card">
<p>مجمع نور اليقين الإسلامي - بدوس</p>
<p>مدرسة الإمام المهدي الابتدائية - الدمازين</p>
<p>مدرسة الجانديل الثانوية - الدمازين</p>
<p>أكاديمية العلوم الصحية - الدمازين</p>
<p>أكاديمية نتووركات - القاهرة</p>
<p>دبلوم لغات البرمجة</p>
</div>

<h2>الخبرة</h2>
<div class="card">
<p>بناء مواقع شخصية ومواقع أعمال سريعة ونظيفة</p>
<p>مشاريع حرة - Freelance</p>
<p>نشر وإدارة المواقع على GitHub Pages</p>
</div>

"""

if 'السيرة الذاتية' not in html:
    html = html.replace('<h2>اطلب موقعك</h2>', cv + '<h2>اطلب موقعك</h2>')
    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(html)
    print('تمت الإضافة بنجاح')
else:
    print('السيرة موجودة أصلا')
