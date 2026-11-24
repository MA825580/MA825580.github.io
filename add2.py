t=open('index.html',encoding='utf-8').read()
new='''<div style="text-align:center;padding:20px;">
<a href="https://wa.me/249915066468" target="_blank" style="display:block;background:#25D366;color:white;padding:12px;border-radius:10px;margin:10px;text-decoration:none;font-weight:bold;">واتساب</a>
<a href="https://www.facebook.com/100081655952571" target="_blank" style="display:block;background:#1877F2;color:white;padding:12px;border-radius:10px;margin:10px;text-decoration:none;font-weight:bold;">فيسبوك</a>
<a href="mailto:mahualdin0@gmail.com" style="display:block;background:#333;color:white;padding:12px;border-radius:10px;margin:10px;text-decoration:none;font-weight:bold;">mahualdin0@gmail.com</a>
</div>
<footer>'''
t=t.replace('<footer>',new,1)
open('index.html','w',encoding='utf-8').write(t)
print('تمت الاضافة بنجاح')
