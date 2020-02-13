#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

import sys
import cgi
import time
from datetime import datetime
import sqlite3

# enable debugging
import cgitb
cgitb.enable()

print "Content-Type: text/html; charset=utf-8"
print


lesson_user = str(sys.argv[1])
inp = lesson_user.split(':')


lesson_page = inp[0]
userid = ''

def updateBrowsingTable():
	unix = int(time.time())
	today= 'na'
	curtime = datetime.now()  
	conn = sqlite3.connect('/var/www/db/SS_users.db')

	conn.execute("INSERT INTO browsed_page (userid, date_access, time_access, page) \
      VALUES (?,?,?,?)", (userid, today, curtime, lesson_page));

	conn.commit()
	conn.close()

	