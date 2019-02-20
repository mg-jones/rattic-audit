#!/bin/bash

/bin/ln -s /etc/rattic-audit/rattic-audit.conf /etc/apache2/sites-available/rattic-audit.conf
/usr/sbin/a2enmod wsgi.load
/usr/sbin/a2ensite rattic-audit.conf
/etc/init.d/apache2 reload
