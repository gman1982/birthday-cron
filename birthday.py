#!/usr/bin/python
# -*- coding: utf-8 -*-
# encoding=utf8
import sys
reload(sys)
sys.setdefaultencoding('utf8')

import smtplib

from datetime import datetime
from email.mime.text import MIMEText
from email.header import Header

blist = open("birthday.lst","r")

now = datetime.now()
mm=str(now.month)
dd=str(now.day)

for line in blist:
  line_split = line.rstrip().split(";")
  if len(line_split)>1:
    salutation = line_split[0]
    addr = line_split[1]
    bd = line_split[2]
    bm = line_split[3]
    if int(dd) == int(bd) and int(mm) == int(bm):
      msg =  salutation+",\n\n"
      msg +=  u"zu Deinem Geburtstag wünsche ich Dir alles Gute, Glück und Erfolg!\n"
      msg +=  u"Dein\n\n"
      msg +=  u"xxx"
      print msg
      
      mime_msg = MIMEText(msg.encode('utf-8'), 'plain', 'utf-8')
      mime_msg['Subject'] = Header(('Alles Gute zum Geburtstag').encode('utf-8'), 'utf-8')
      s = smtplib.SMTP_SSL("smtp.bla.invalid:465")
      s.login('email@bla.invalid','qwertzuiop')
      s.sendmail('email@bla.invalid', addr, mime_msg.as_string())
      s.quit
     
