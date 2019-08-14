#!C:\Users\nayoung\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi
import os

form = cgi.FieldStorage()
pageID = form["pageID"].value
title = form["title"].value
description = form['desc'].value

opened_file = open('data/'+pageID, 'w')
opened_file.write(description)
opened_file.close()

os.rename('data/'+pageID, 'data/'+title)

# Redirection
print("Location: index.py?id="+title)
print()
