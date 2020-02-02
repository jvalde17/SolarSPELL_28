# SolarSPELL_28
ASU SER-401 Team 28

Fall 2019 - Spring 2020

Team Members:
Curtis Smith,
Jess Valdez,
Catherine Khongsaly,
Christopher Risser,
Tony Conrad

Dev branch created 10-10-2019
 
## Configuring Apache to support Python 
Edit --> /etc/apache2/sites-enabled/000-default.conf

Add directory tag as below:

<Directory /var/www/html>
       Options +ExecCGI
       AddHandler cgi-script .py
</Directory>
