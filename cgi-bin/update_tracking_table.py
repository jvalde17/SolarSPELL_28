#!/usr/bin/env python

import Cookie, os, time
from datetime import datetime
import sqlite3
import sys
import cgi
import cgitb
cgitb.enable()

print "Content-Type: text/html; charset=utf-8"
print

cookie = Cookie.SimpleCookie()

print cookie
print 'Content-Type: text/html\n'

print '<html><body>'
print '<p>Server time is', time.asctime(time.localtime()), '</p>'
username = ''
# The returned cookie is available in the os.environ dictionary
cookie_string = os.environ.get('HTTP_COOKIE')

# The first time the page is run there will be no cookies
if not cookie_string:
    print '<p>First visit or cookies disabled</p>'

else: # Run the page twice to retrieve the cookie
    print '<p>The returned cookie string was "' + cookie_string + '"</p>'

    # load() parses the cookie string
    cookie.load(cookie_string)
    # Use the value attribute of the cookie to get it
    #lastvisit = float(cookie['lastvisit'].value)
    username = cookie['userid'].value

    print '<p>You are :',
    print username, '</p>'

print '</body></html>'


lesson_user = str(sys.argv[1])
inp = lesson_user.split(':')

lesson_page = inp[0]
userid = ''

print 'Hello!'

def redirectToCallingUrl():
	meta_str = ''
	if 'Lesson' in lesson_page:
		if 'Level_2' in lesson_page: #Level 2
			meta_str = '<meta http-equiv = "refresh" content = "0; url = /content/Language%20Arts/Voice%20of%20America%20%28VOA%29/Let%27s%20Learn%20English%202/{}?name={}"/>'.format(lesson_page, userid) 
		else: #Level 1
			meta_str = '<meta http-equiv = "refresh" content = "0; url = /content/Language%20Arts/Voice%20of%20America%20%28VOA%29/Let%27s%20Learn%20English/{}?name={}"/>'.format(lesson_page, userid)

	if 'unit' in lesson_page: # teach
		meta_str = '<meta http-equiv = "refresh" content = "0; url = /content/Language%20Arts/Voice%20of%20America%20%28VOA%29/Let%27s%20Teach%20English/{}?name={}"/>'.format(lesson_page, userid)
	
	if 'PROTOTYPE' in lesson_page:
		meta_str = '<meta http-equiv = "refresh" content = "0; url = /content/Language%20Arts/Voice%20of%20America%20%28VOA%29/PROTOTYPE/{}?name={}"/>'.format(lesson_page, userid)
	
	print '<html>'
	print '<head>'
	print meta_str
	print '</head>'
	print '</html>'


def updateBrowsingTable():
	unix = int(time.time())
	today= 'na'
	curtime = datetime.now()  
	conn = sqlite3.connect('/var/www/db/SS_users.db')

	conn.execute("INSERT INTO browsed_page (userid, date_access, time_access, page) \
      VALUES (?,?,?,?)", (userid, today, curtime, lesson_page));

	conn.commit()
	conn.close()

if username:
	if '##' not in username:
		userid = username
		updateBrowsingTable()


redirectToCallingUrl()