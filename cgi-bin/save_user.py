#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

#import os
import time
from datetime import datetime
import sqlite3
import sys
import cgi
import cgitb
cgitb.enable()

print "Content-Type: text/html; charset=utf-8"
print


form = cgi.FieldStorage()
userlogged =  form.getvalue('userid')
if not userlogged : 
	userlogged = '######'


#with open("mylog.log", "a") as f:
#	f.write(userlogged)
#	f.write("\n")


def testprint():
	print "hello there"
	print userlogged

 
#meta_str = '<meta http-equiv = "refresh" content = "0; url = /content/Language Arts/Voice of America (VOA)/VOA_Landing_Page.html?user={}" />'.format(userlogged)  
meta_str = '<meta http-equiv = "refresh" content = "0; url = /content/Language Arts/Voice of America (VOA)/VOA_Landing_Page.html" />' 
def goToMainUrl():
	print '<html>'
	print '<head>'
	print meta_str
	#print '<meta http-equiv = "refresh" content = "0; url = /content/Language Arts/Voice of America (VOA)/VOA_Landing_Page.html>'
	print '</head>'
	print '</html>'

def saveCurrentUserToTable():
	unix = int(time.time())
	#today = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
	#curtime = time.time()
	today= 'na'
	curtime = datetime.now()  
	#print("Today's date :", today)
	#print("Current time : ", curtime)
	#print("Current user:", userlogged)
	conn = sqlite3.connect('/var/www/db/SS_users.db')
	print "Opened database successfully";
	
	conn.execute("INSERT INTO user (userid, date_login, time_login) \
      VALUES (?,?,?)", (userlogged, today, curtime));

	conn.commit()
	print "Records created successfully";
	conn.close()
	print "db closed";

#testprint()
saveCurrentUserToTable()
goToMainUrl()


