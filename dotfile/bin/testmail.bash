#!/bin/bash
# -*- coding:utf-8 -*-
sendEmail -f 29167610@qq.com -t roover.wd@gmail.com \
-u this is the test tile -m “this is a test message” \
-s smtp.gmail.com \
-o tls=yes \
-xu roover.wd -xp wangdian

#mail -s "hello" roover.wd@gmail.com < .wgetrc

# SendEmail is a lightweight, completly command line based, SMTP
# email agent.It was designed to be used in bash scripts, Perl
# programs, and web sites, but it is also quite useful in many
# other contexts.SendEmail is written in Perl

# Install sendemail in debian lenny

#     #apt-get install sendemail

# This will complete the installation.

# If you are using Debian Etch you need to compile sendemail from
# source
# Preparing your system

#     #apt-get install libio-socket-ssl-perl libnet-ssleay-perl
#     perl

# Download latest version from here

#     wget http://caspian.dotconf.net/menu/Software/SendEmail/
#     sendEmail-v1.55.tar.gz

# Uncompress the .tar.gz

# #tar zxvf /tmp/sendEmail-v1.55.tar.gz

# #cd /tmp/sendEmail-v1.55

# Copy the sendEmail script to /usr/local/bin

# #cp /tmp/sendEmail-v1.55/sendEmail  /usr/local/bin

# Make sure its executable

# #chmod +x /usr/local/bin/sendEmail

# Sendemail Examples

# Simple Email Using Gmail Account

# sendEmail -f my.account@gmail.com -t myself@domain.tld \
# -u this is the test tile -m “this is a test message” \
# -s smtp.gmail.com \
# -o tls=yes \
# -xu usernameonly -xp mypasswd

# “usernameonly” must not contain @gmail.com only the username.

# Simple Email

# sendEmail -f myaddress@isp.net \
# -t myfriend@isp.net \
# -s relay.isp.net \
# -u “Test email” \
# -m “Hi , this is a test email.”

# Sending to mutiple people

# sendEmail -f myaddress@isp.net \
# -t “admin <admin@isp.net>” user1@isp.net user2@isp.net \
# -s relay.isp.net \
# -u “Test email” \
# -m “Hi this is a test email.”

# Sending to multiple people using cc and bcc recipients

# (notice the different way we specified multiple To recipients,
# you can do this for cc and bcc as well)

# sendEmail -f myaddress@isp.net \
# -t admin@isp.net;user1@isp.net;user2@isp.net \
# -cc user2@isp.net tom@isp.net jess@isp.net \
# -bcc ra@isp.net dub@isp.net kay@isp.net \
# -s relay.isp.net \
# -u “Test email with cc and bcc recipients” \
# -m “Hi his is a test email.”

# Sending to multiple people with multiple attachments

# sendEmail -f myaddress@isp.net \
# -t admin@isp.net \
# -cc user1@isp.net user2@isp.net user3@isp.net \
# -s relay.isp.net \
# -u “Test email with cc and bcc recipients” \
# -m “Hi this is a test email.” \
# -a /mnt/storage/document.sxw “/root/My Documents/Work
# Schedule.kwd”

# Sending an email with the contents of a file as the message body

# cat /tmp/file.txt | sendEmail -f myaddress@isp.net \
# -t admin@isp.net \
# -s relay.isp.net \
# -u “Test email with contents of file”

# Sending an email with the contents of a file as the message body
# (method 2)

# sendEmail -f myaddress@isp.net \
# -t admin@isp.net \
# -s relay.isp.net \
# -o message-file=/tmp/file.txt \
# -u “Test email with contents of file”

# Sending an html email: (make sure your html file has <html> at
# the beginning)

# cat /tmp/file.html | sendEmail -f myaddress@isp.net \
# -t admin@isp.net \
# -s relay.isp.net \
# -u “Test email with html content”

# Send Short Message Service (SMS)/text message to a cellular
# phone

# Simple Text Message Sent To Cellular Phone Using Gmail Account

# ./sendEmail -f usernameonly@gmail.com -t 2123334444@txt.att.net
# \
# -m This is an SMS message from Linux.\
# -o tls=auto \
# -s smtp.gmail.com \
# -xu usernameonly -xp mypasswd

# Providers

# What’s my SMS Email address?

# AT&T 10DigitPhoneNumber@txt.att.net
# Example: 9055556543@txt.att.net
# Cingular 10DigitPhoneNumber@cingularme.com
# Metrocall 10DigitPhoneNumber@page.metrocall.com
# Nextel 10DigitPhoneNumber@messaging.nextel.com
# Sprint PCS 10DigitPhoneNumber@messaging.sprintpcs.com
# T-Mobile 10DigitPhoneNumber@tmomail.net
# Verizon 10DigitPhoneNumber@vtext.com
# ALLTEL 10DigitPhoneNumber@message.alltel.com