#In order to enable content tracking feature of SolarSPELL, the python req library must be installed

sudo apt-get install -y python-requests


#Configuring Apache to support Python
#Edit --> /etc/apache2/sites-enabled/000-default.conf

#Add/modify directory tag as below:

   <Directory /var/www/html>

   Options +ExecCGI
   
   AddHandler cgi-script .py
   
   </Directory>

#Enable cgi to allow python scripts to run inside Apache hosted directory

   sudo a2dismod mpm_event
   sudo a2enmod mpm_prefork cgi

#Restart Apache by using the following command:

    sudo service apache restart

#Backend code that must be loaded in /usr/lib/cgi-bin
#1. save_user.py
#2. update_tracking_table.py
#3. logout.py
#4. recall_last_visited_page.py
#5. create_tracking_db.py

#During initial setup, run create_tracking_db.py to create the database file SS_users.db
#located in /www/db/