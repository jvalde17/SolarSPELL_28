# @author Jess Valdez
# @version April 2020
# Purpose - Cleans or resets content tracking table

import sqlite3

sqlite_file = '/var/www/db/SS_users.db'    # name of the sqlite database file
table_name1 = 'user'	# login table
table_name2 = 'browsed_page'	# browsing table

print 'Connecting to the database file'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

print 'clearing user table'
# Clear user table
c.execute('DELETE FROM {tn} '\
        .format(tn=table_name1) )

c.execute('DELETE FROM {tn} '\
        .format(tn=table_name2) )

# Committing changes and closing the connection to the database file
print 'changes committed.'
conn.commit()
conn.close()

print 'Done'