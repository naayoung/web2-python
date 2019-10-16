#!C:\Users\nayoung\AppData\Local\Programs\Python\Python37-32\python.exe
import sys
import codecs
import cgi
import os
import view


print("Content-Type: text/html")
print()

# stdout의 인코딩을 UTF-8로 강제 변환
sys.stdout = codecs.getwriter("utf-8")(sys.stdout.detach())

form = cgi.FieldStorage()

if 'id' in form:
    pageID = form["id"].value
    description = open('data/'+pageID, 'r', encoding='UTF-8').read()
    update_link = '<a href="update.py?id={}">update</a>'.format(pageID)
    delete_action = '''
      <form action="process_delete.py" method="post">
          <input type="hidden" name="pageID" value="{}">
          <input type="submit" value="delete">
      </form>  
    '''.format(pageID)
else:
    pageID = 'Welcome'
    description = 'Hello, web'
    update_link = ''
    delete_action = ''

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
    {update_link}
    {delete_action}
    <h2>{title}</h2>
    <p>{desc}</p>
  </body>
</html>
'''.format(
    title=pageID,
    desc=description,
    listStr=view.getList(),
    update_link=update_link,
    delete_action=delete_action))
