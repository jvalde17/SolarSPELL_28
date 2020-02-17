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

def checkForCurrentUser():
	print 'reading db for current user'
	cur_user = '??????'
	return cur_user

def timeDiff(t_then):
	unix = int(time.time())
	then = datetime.strptime(t_then, '%Y-%m-%d %H:%M:%S.%f') 
	now = datetime.now()                    
	duration = now - then                         # For build-in functions
	nduration = str(duration).split(':')
	t1 = nduration[0] #hours
	if 'day' in t1:
		t2 = t1.split(',')
		t3 = t2[0]
		t3 = t3.strip('s')
		t3 = t3.strip('day')
		t3 = t3.replace(" ","")
		return int(t3) * 24
	return int(t1)	

#get time now, compare to time from current user
def read_user_db():
	conn = sqlite3.connect('/var/www/db/SS_users.db')
	c = conn.cursor()
	print "Opened database successfully";
	t = ('Jess',);
	last_row = c.execute('select * from user').fetchall()[-1]
	print "....Done reading db"
	c.close
	conn.close()
	return str(last_row)

def cleanNameStr(str):
	cleanStr = str.replace('(', '')
	cleanStr = cleanStr.replace('u','')
	cleanStr = cleanStr.replace('\'','')
	cleanStr = cleanStr.replace(" ","")
	return cleanStr

def cleanDateTimeStr(str):
	cleanStr = str.replace(')', '')
	cleanStr = cleanStr.replace('u','')
	cleanStr = cleanStr.replace('\'','')
	cleanStr = cleanStr.strip()
	return cleanStr


dat = read_user_db()
dat_list = dat.split(',')
last_user = dat_list[0]
dateTime_last_user = dat_list[2]

print dateTime_last_user
l_user = ''

if len(dat) > 3:
	l_user = cleanNameStr(last_user)
	dt_l_user = cleanDateTimeStr(dateTime_last_user)
	print l_user
	print dt_l_user

#get time diff in hours
diff = timeDiff(dt_l_user)

valid_user = 0
if diff < 5:
	valid_user = 1
	userid = l_user
	print 'Yes, we have a logged user! :' + userid
	updateBrowsingTable()
else:
	print "No, user is logged!"


redirectToCallingUrl()	