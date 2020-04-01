sudo apt-get update
sudo apt-get install byobu htop
sudo apt-get install etckeeper

sudo raspi-config
    select "1 Expand Filesystem"
    select "3 Boot Options"
        select "B1 Console"
    select "5 Internationalisation Options"
        select "I1 Change Locale"
            scroll down to "en_GB.UTF-8 UTF-8" and press space to deselect
            scroll down to "en_US.UTF-8 UTF-8" and press space to select
            press okay
            next screen asks for "Default locale for the system environment", select "en_US.UTF-8"
    select "5 Internationalisation Options"
        select "I2 Change Timezone"
            next screen asks for "Geographic area", select "US"
            next screen asks for "Time zone", select "Pacific-New"
    select "5 Internationalisation Options"
        select "I4 Change Wi-fi Country"
            scroll down and select "US United States"
    select "Finish"
        next screen asks "Would you like to reboot now?", select "Yes"

sudo apt-get install apache2 php5 libapache2-mod-php5

sudo apt-get install dnsmasq hostapd

sudo cp -a /etc/dhcpcd.conf /etc/dhcpcd.conf.orig

append these lines to the end of /etc/dhcpcd.conf:
interface wlan0
    static ip_address=10.10.10.10/24