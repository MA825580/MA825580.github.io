import pathlib
p = pathlib.Path('index.html')
t = p.read_text()
old = '</body>'
new = '''<script>
var b = [...document.querySelectorAll("button")].find(x=>x.textContent.includes("ارسل الطلب"));
if(b){ b.onclick = function(){
var s = document.getElementById("s").value;
var a = document.getElementById("a").value;
var d = document.getElementById("d").value;
var m = "السلام عليكم، داير خدمة: " + s + " | المنطقة: " + a + " | التفاصيل: " + d;
window.open("https://wa.me/249915066438?text=" + encodeURIComponent(m), "_blank");
}}
</script></body>'''
t = t.replace(old, new)
p.write_text(t)
print('fixed')
