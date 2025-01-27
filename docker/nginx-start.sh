#!/bin/sh
/usr/sbin/fcgiwrap -s unix:/var/run/fcgiwrap.socket &
chown www-data:www-data /var/run/fcgiwrap.socket
chmod 660 /var/run/fcgiwrap.socket
nginx -g 'daemon off;'