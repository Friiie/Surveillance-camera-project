import os
import smtplib
import time
import database as db

import imghdr
from email.message import EmailMessage


def sendNotification(adresses):
	sender = "surveillance.camera.notice@gmail.com"
	msg = EmailMessage()
	msg['Subject'] = "Detection: " + time.ctime()
	msg['From'] = sender
	
	if adresses==False or len(adresses)==0:
		return False
	elif len(adresses) ==1:
		msg['To'] = adresses[0]
	else:
		msg['To'] = ", ".join(adresses)
	
	
	with open('system_notice.jpg', 'rb') as fp:
		img_data = fp.read()
		msg.add_attachment(	img_data,maintype='image',subtype=imghdr.what(None, img_data))
                            
	
	with smtplib.SMTP('smtp.gmail.com',587) as smtp:
		
		smtp.ehlo()
		smtp.starttls()
		smtp.ehlo()
		smtp.login(sender,'emailpassword')
		
		smtp.send_message(msg)
		print(">>  \033[92m60% mail sent\033[0m")





