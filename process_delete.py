#!C:\Users\nayoung\AppData\Local\Programs\Python\Python37-32\python.exe
import cgi
import os

form = cgi.FieldStorage()
pageID = form["pageID"].value

os.remove('data/'+pageID)

# Redirection
print("Location: index.py")
print()
