t=open('index.html',encoding='utf-8').read()
old='<a href="#contact"'
new='''<a href="https://wa.me/249915066468" target="_blank" style="display:block;text-align:center;background:#25D366;color:white;padding:12px;border-radius:10px;margin-top:10px;text-decoration:none;font-weight:bold;">واتساب</a>
<a href="https://www.facebook.com/100081655952571" target="_blank" style="display:block;text-align:center;background:#1877F2;color:white;padding:12px;border-radius:10px;margin-top:10px;text-decoration:none;font-weight:bold;">فيسبوك</a>
<a href="mailto:mahualdin0@gmail.com" style="display:block;text-align:center;background:#333;color:white;padding:12px;border-radius:10px;margin-top:10px;text-decoration:none;font-weight:bold;">mahualdin0@gmail.com</a>
<a href="#contact"'''
if old in t:
    t=t.replace(old,new,1)
    open('index.html','w',encoding='utf-8').write(t)
    print('تمت الاضافة بنجاح')
else:
    print('ما لقيت الزر')
