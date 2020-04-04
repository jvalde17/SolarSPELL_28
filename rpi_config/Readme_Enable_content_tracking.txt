Configuring Apache to support Python
Edit --> /etc/apache2/sites-enabled/000-default.conf

Add/modify directory tag as below:

   <Directory /var/www/html>

   Options +ExecCGI
   
   AddHandler cgi-script .py
   
   </Directory>
Restart Apache by using the following command:

    sudo service apache restart
Enable cgi to allow python scripts to run inside Apache hosted directory

   sudo a2dismod mpm_event
   sudo a2enmod mpm_prefork cgi