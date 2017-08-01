"""
This script can be used to send email from any linux server and comes with an option to add attachments.
The script has been configured to use gmail smtp sever for the from email address and can be easily modified to suit
whichever smtp server you want to leverage to send a mail from that address.

Before using the script, visit the below links and enable the given options so google lets you send mail remotely -

https://myaccount.google.com/lesssecureapps
https://accounts.google.com/displayunlockcaptcha

__author__ : sanjayvarmarudraraju
__github__ : www.github.com/sanjayvr
"""


import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

# The from address has to be gmail id as the smtp has been configured to gmail
from_address = "@gmail.com"
to_address = "enter the to email address"

msg = MIMEMultipart()

msg['From'] = from_address
msg['To'] = to_address
msg['Subject'] = "enter the subject of the email here"
body = "enter the body of the email here"
msg.attach(MIMEText(body, 'plain'))

filename = "filename with extension here"
attachment = open(filename, "rb")
part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(from_address, "enter password of the from email address here")
text = msg.as_string()
server.sendmail(from_address, to_address, text)
server.quit()
