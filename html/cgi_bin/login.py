#!/usr/bin/env python
# _*_ coding: UTF-8 _*_


# enable debugging
import cgitb
cgitb.enable()


print "Content-Type: text/html; charset=utf-8"
print
#print "Hello World!"

print '<h1>Welcome to SolarSPELL </h1>'
print '<form action = "save_user.py" method =  "post">'
print '<input type = "text" name = "userid" >'
print '<input type="submit" value = "Go to VoA" >'
print '<input type="submit" value = "Go to last visited lesson" formaction = "recall_last_visited_page.py" >'
print '</form>'


#with samilar functionality as save_user.py
#print '<form action = "recall_last_visited_page.py" method =  "post">'
#print '<input type="submit" value = "Go to last visited lesson">'
#print '</form>'
