#!/bin/sh
spawn-fcgi -s /var/run/fcgiwrap.socket -M 0660 -u www-data -g www-data /usr/sbin/fcgiwrap &
nginx -g 'daemon off;'