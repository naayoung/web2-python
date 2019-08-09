#!C:\Users\nayoung\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi
print("Content-Type: text/html")
print()

form = cgi.FieldStorage()
if 'id' in form:
    pageID = form["id"].value
else:
    pageID = 'Welcome'

print('''<!DOCTYPE html>
<html>
  <head>
    <title>NaYoung-Welcome</title>
    <meta charset="euc-kr" />
  </head>
  <body>
    <h1><a href="index.py">WEB</a></h1>
    <ol>
      <li><a href="index.py?id=HTML">HTML</a></li>
      <li><a href="index.py?id=CSS">CSS</a></li>
      <li><a href="index.py?id=JavaScript">JavaScript</a></li>
    </ol>
    <h2>{title}</h2>
    <p>
      Welcome~ My name is NaYoung! This is
      <a href="https://www.naver.com/">naver</a>.
    </p>
    <p>
      This is my love song~ <br />
      <iframe
        width="560"
        height="315"
        src="https://youtu.be/52nfjRzIaj8"
        frameborder="0"
        allowfullscreen
      ></iframe>
    </p>
    <!--<img src="cookie.jpg" width="100%">-->
    <img src="cookie.jpg" width="200" />
    <p style="margin-top:40px;">
      <strong>Happy <u>NaYoung</u> world</strong>
    </p>
  </body>
</html>
'''.format(title=pageID))
