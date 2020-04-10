# @author Jess Valdez (jvalde17@asu.edu)
# @version April 2020
# Purpose - Creates a new SQLite SolarSPELL tracking database

import sqlite3

sqlite_file = '/var/www/db/SS_users.db'    # name of the sqlite database file
table_name1 = 'user'	# login table
table_name2 = 'browsed_page'	# browsing table
t1_c1 = 'userid' # name of the column
t1_c2 = 'date_login' # name of the column
t1_c3 = 'time_login' # name of the column
field_type = 'TEXT'  # column data type

t2_c1 = 'userid' # name of the column
t2_c2 = 'date_access' # name of the column
t2_c3 = 'time_access' # name of the column
t2_c4 = 'page' # name of the column

print 'Connecting to the database file'
conn = sqlite3.connect(sqlite_file)
c = conn.cursor()

print 'creating user table'
# Creating a new SQLite table with 1 column
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_name1, nf=t1_c1, ft=field_type) )

# A) Adding a new column without a row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name1, cn=t1_c2, ct=field_type))

# A) Adding a new column without a row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name1, cn=t1_c3, ct=field_type))


print 'creating browsing table'
# Creating a second table with 1 column and set it as PRIMARY KEY
# note that PRIMARY KEY column must consist of unique values!
c.execute('CREATE TABLE {tn} ({nf} {ft})'\
        .format(tn=table_name2, nf=t2_c1, ft=field_type))

# A) Adding a new column without a row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name2, cn=t2_c2, ct=field_type))

# A) Adding a new column without a row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name2, cn=t2_c3, ct=field_type))

# A) Adding a new column without a row value
c.execute("ALTER TABLE {tn} ADD COLUMN '{cn}' {ct}"\
        .format(tn=table_name2, cn=t2_c4, ct=field_type))

# Committing changes and closing the connection to the database file
print 'changes committed.'
conn.commit()
conn.close()

print 'Done'