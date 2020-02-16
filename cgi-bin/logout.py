#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

import time
from datetime import datetime
import sqlite3
import sys
import cgi
import cgitb
cgitb.enable()

print "Content-Type: text/html; charset=utf-8"
print

# 1. Update user table -- set it as "&xoxososoIPassedtheRainsinAfrica"
# 2. Redirect to LoginPanel


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


def saveDummyUserToTable():
	unix = int(time.time())
	today= 'na'
	curtime = datetime.now()  
	conn = sqlite3.connect('../../db/SS_users.db')
	print "Opened database successfully";
	
	conn.execute("INSERT INTO user (userid, date_login, time_login) \
      VALUES (?,?,?)", ('&xoxososoIPassedtheRainsinAfrica', today, curtime));

	conn.commit()
	print "Records created successfully";
	conn.close()
	print "db closed";

#testprint()
saveDummyUserToTable()
goToLogin()