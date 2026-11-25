import pathlib
p = pathlib.Path('index.html')
t = p.read_text()
btn = '''<a href="https://wa.me/249915066438?text=السلام عليكم، داير استفسر عن خدمة" target="_blank" style="position:fixed;bottom:20px;left:20px;background:#25D366;color:white;width:60px;height:60px;border-radius:50%;display:flex;align-items:center;justify-content:center;font-size:30px;text-decoration:none;z-index:999;box-shadow:0 4px 15px rgba(0,0,0,.4)">💬</a></body>'''
if 'wa.me/249915066438?text=السلام عليكم، داير استفسر' not in t:
    t = t.replace('</body>', btn)
p.write_text(t)
print('wa btn done')
