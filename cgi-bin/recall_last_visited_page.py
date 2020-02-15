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


form = cgi.FieldStorage()
userlogged =  form.getvalue('userid')
if not userlogged : 
	userlogged = '########'


conn = sqlite3.connect('../../db/SS_users.db')
c = conn.cursor()
#print "Opened database successfully";

def testprint():
	print "hello there "
	print userlogged


def goToLastVisitedUrl(page):
	meta_str = ''
	if 'Lesson' in page:
		if 'Level_2' in page: #Level 2
			meta_str = '<meta http-equiv = "refresh" content = "0; url = /content/Language%20Arts/Voice%20of%20America%20%28VOA%29/Let%27s%20Learn%20English%202/{}"/>'.format(page)  
		else: #Level 1
			meta_str = '<meta http-equiv = "refresh" content = "0; url = /content/Language%20Arts/Voice%20of%20America%20%28VOA%29/Let%27s%20Learn%20English/{}"/>'.format(page)  

	if 'unit' in page: # teach
		meta_str = '<meta http-equiv = "refresh" content = "0; url = /content/Language%20Arts/Voice%20of%20America%20%28VOA%29/Let%27s%20Teach%20English/{}"/>'.format(page)  
	
	if 'PROTOTYPE' in page:
		meta_str = '<meta http-equiv = "refresh" content = "0; url = /content/Language%20Arts/Voice%20of%20America%20%28VOA%29/PROTOTYPE/{}"/>'.format(page)  
	
	print '<html>'
	print '<head>'
	print meta_str
	print '</head>'
	print '</html>'

def goToVoAHome():
	meta_str = '<meta http-equiv = "refresh" content = "0; url = /content/Language Arts/Voice of America (VOA)/VOA_Landing_Page.html" />' 
	print '<html>'
	print '<head>'
	print meta_str
	print '</head>'
	print '</html>'

def read_from_db():
    c.execute('SELECT * FROM browsed_page WHERE userid = ?', (userlogged,))
    #data = c.fetchall()[-1]
    data = c.fetchall()
    if len(str(data)) > 5:
    	data = data[-1]	#grab the most recent record
    return str(data)


def cleanPageStr(str):
	cleanStr = str.strip(')]')
	cleanStr = cleanStr.replace('u','')
	cleanStr = cleanStr.replace('\'','')
	cleanStr = cleanStr.replace(" ","")
	return cleanStr

def saveCurrentUserToTable():
	unix = int(time.time())
	today= 'na'
	curtime = datetime.now()  
	
	c.execute("INSERT INTO user (userid, date_login, time_login) \
      VALUES (?,?,?)", (userlogged, today, curtime));

	conn.commit()
	#print "Records created successfully";


#testprint()
saveCurrentUserToTable()
if userlogged == '########':
	goToVoAHome()
	c.close
	conn.close()


mydat = read_from_db()

dat_array = mydat.split(',')
print dat_array
print 'Length of mydat = ' + str(len(mydat)) 

#uncomment below for release
if len(mydat) > 5:
	mpage = cleanPageStr(dat_array[3])
	goToLastVisitedUrl(mpage)
	c.close
	conn.close()
else :
	print 'No history'
	goToVoAHome()
	c.close
	conn.close()
	


