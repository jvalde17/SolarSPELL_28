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
print '<input type="submit" value = "Go to Main" >'
print '</form>'

#replace this with read_last_visited.py
#with samilar functionality as save_user.py
print '<form action = "\content/Language Arts/Voice of America (VOA)/VOA_Landing_Page.html" method =  "post">'
print '<input type="submit" value = "Go to last visited lesson">'
print '</form>'

