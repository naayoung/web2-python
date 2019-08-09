#!C:\Users\nayoung\AppData\Local\Programs\Python\Python37-32\python.exe
import sys
import codecs
import cgi

print("Content-Type: text/html")
print()

# stdout의 인코딩을 UTF-8로 강제 변환
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()

if 'id' in form:
    pageID = form["id"].value
    description = open('data/'+pageID, 'r', encoding='UTF-8').read()
else:
    pageID = 'Welcome'
    description = 'Hello, web'

print('''<!DOCTYPE html>
<html>
  <head>
    <title>NaYoung-Welcome</title>
    <meta charset="utf-8" />
  </head>
  <body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
      <li><a href="index.py?id=HTML">HTML</a></li>
      <li><a href="index.py?id=CSS">CSS</a></li>
      <li><a href="index.py?id=JavaScript">JavaScript</a></li>
    </ol>
    <h2>{title}</h2>
    <p>{desc}</p>
  </body>
</html>
'''.format(title=pageID, desc=description))
