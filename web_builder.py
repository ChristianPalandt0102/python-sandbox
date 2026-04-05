import os

HTML = """
<html>
<head>
<title>Sandbox Dashboard</title>
</head>
<body>
<h1>Sandbox Controller</h1>
<div id="boxes"></div>

<script>
fetch('/status')
.then(r=>r.json())
.then(d=>{
 document.getElementById("boxes").innerHTML =
 JSON.stringify(d,null,2);
});
</script>
</body>
</html>
"""

def build():
    os.makedirs("web/build", exist_ok=True)
    open("web/build/index.html","w").write(HTML)
