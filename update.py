#!C:\Users\nayoung\AppData\Local\Programs\Python\Python37-32\python.exe
import sys
import codecs
import cgi
import os

files = os.listdir('data')
listStr = ''
for item in files:
    listStr = listStr + \
        '<li><a href="index.py?id={name}">{name}</a></li>'.format(name=item)

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
      {listStr}
    </ol>
    <a href="create.py">create</a>
    <form action="process_update.py" method="post">
      <input type="hidden" name="pageID" value="{form_default_title}">
      <p><input type="text" name="title" placeholder="title" value="{form_default_title}"></p>
      <p><textarea rows="4" name="desc" placeholder="description">{form_default_description}</textarea></p>
      <p><input type="submit"></p>
    </form>
  </body>
</html>
'''.format(title=pageID, desc=description, listStr=listStr, form_default_title=pageID, form_default_description=description))
