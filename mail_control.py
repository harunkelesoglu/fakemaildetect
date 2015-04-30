
#-*- coding: utf-8 -*-
import os
import re

check_mail_addr = ''
mail_from_addr = ''

for dirname,dirnames,filenames in os.walk('/home/harun/mail/new'):
    for filename in filenames:
        mail_name = os.path.join(dirname,filename)
 maili = open(mail_name,'r')
 allmail = maili.read()
 allmail = str(allmail)
 regex = re.match(r'Return-Path: <(.*)>',allmail,re.M|re.I)
 if regex:
  check_mail_addr = regex.group(1)
 #maili.close()

 match = re.search('From: (.*)',allmail)
 if match:
  mail_from_addr = match.group(1)

 if(check_mail_addr!=mail_from_addr):
   xx ='Sahte mail adresi, bu maili gönderen kişinin gerçek mail adresi: '+check_mail_addr+"'dur\n"
  print xx
  with open(mail_name,'a') as mailx:
   mailx.write(xx)

 maili.close()
 #print check_mail_addr+' - '+mail_from_addr
