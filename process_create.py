#!C:\Users\nayoung\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi

form = cgi.FieldStorage()
title = form["title"].value
description = form['desc'].value

opened_file = open('data/'+title, 'w')
opened_file.write(description)

# Redirection
print("Location: index.py?id="+title)
print()
