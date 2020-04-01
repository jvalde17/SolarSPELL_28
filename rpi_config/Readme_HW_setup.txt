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

sudo cp -a /etc/network/interfaces /etc/network/interfaces.orig
sudo nano /etc/network/interfaces and comment out the line containing wpa-conf in the wlan0 section, so that it looks like this:
allow-hotplug wlan0
iface wlan0 inet manual
#    wpa-conf /etc/wpa_supplicant/wpa_supplicant.conf

sudo nano /etc/hostapd/hostapd.conf:
# SPELL WiFi network configuration

# Use the Raspberry Pi 3's built-in WiFi device
interface=wlan0

# Use the nl80211 driver with the brcmfmac driver
driver=nl80211

# This is the name of the network
ssid=SPELL

# Use mode 802.11g for backwards compatibility with older devices
hw_mode=g

# Use channel 6
channel=6

# Disable WMM (QoS via traffic prioritization, which we don't need)
wmm_enabled=0

# Use open authentication (no password needed)
auth_algs=1
    