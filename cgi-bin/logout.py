#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

import time, Cookie
from datetime import datetime
import sqlite3
import sys
import cgi
import cgitb
cgitb.enable()

#print "Content-Type: text/html; charset=utf-8"
#print


# Instantiate a SimpleCookie object
cookie = Cookie.SimpleCookie()

# The SimpleCookie instance is a mapping
cookie['userid'] = '######'

# Output the HTTP message containing the cookie
print cookie
print 'Content-Type: text/html\n'

print '<html><body>'
print 'User is', '######'
print '</body></html>'

def testprint():
	print "Logout sequence"

#
def goToLogin():
	print ">>>>go to login"
	meta_str = '<meta http-equiv = "refresh" content = "0; url = /content/Language Arts/Voice of America (VOA)/VoA_Login.html" />' 
	print '<html>'
	print '<head>'
	print meta_str
	print '</head>'
	print '</html>'

#saveDummyUserToTable is deprecated in favor inserting a Dummy Cookie but kept here for future use.
def saveDummyUserToTable():
	unix = int(time.time())
	today= 'na'
	curtime = datetime.now()  
	conn = sqlite3.connect('/var/www/db/SS_users.db')
	print "Opened database successfully";
	
	conn.execute("INSERT INTO user (userid, date_login, time_login) \
      VALUES (?,?,?)", ('&xoxososoIPassedtheRainsinAfrica', today, curtime));

	conn.commit()
	print "Records created successfully";
	conn.close()
	print "db closed";

#testprint()
#saveDummyUserToTable()
goToLogin()