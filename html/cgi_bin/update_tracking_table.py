#!/usr/bin/env python
# _*_ coding: UTF-8 _*_

import sys
import cgi
import time
import datetime
import sqlite3

# enable debugging
import cgitb
cgitb.enable()

print "Content-Type: text/html; charset=utf-8"
print

#if len(sys.argv) > 1:
#  output = sys.argv[1]
#else:
#  output = "no argument found"
#print 'Updating tracking table'

lesson_user = str(sys.argv[1])
inp = lesson_user.split(':')
#for temp in inp:
#	print temp

lesson_page = inp[0]
userid = inp[1]

#
def redirectToCallingUrl():
	meta_str = '<meta http-equiv = "refresh" content = "0; url = \content/Language Arts/Voice of America (VOA)/Let%27s Learn English/{}" />'.format(lesson_page)
	print '<html>'
	print '<head>'
	print meta_str
	print '</head>'
	print '</html>'

def updateBrowsingTable():
	unix = int(time.time())
	today = str(datetime.datetime.fromtimestamp(unix).strftime('%Y-%m-%d %H:%M:%S'))
	curtime = time.time()
	print("Today's date :", today)
	print("Current time : ", curtime)
	print("Current user:", userid)
	conn = sqlite3.connect('../../db/SS_users.db')
	print "Opened database successfully";
	
	conn.execute("INSERT INTO browsed_page (userid, date_access, time_access, page) \
      VALUES (?,?,?,?)", (userid, today, curtime, lesson_page));

	conn.commit()
	print "Records created successfully";
	conn.close()
	print "db closed";


updateBrowsingTable()
redirectToCallingUrl()






