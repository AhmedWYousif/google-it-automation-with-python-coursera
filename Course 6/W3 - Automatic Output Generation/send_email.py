from email.message import EmailMessage
import os.path
import mimetypes
import smtplib
from smtplib import SMTPAuthenticationError
import getpass
from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph, Spacer, Table, Image
from reportlab.lib.styles import getSampleStyleSheet


message = EmailMessage()

sender = "me@example.com"
recipient = "you@example.com"

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)

body = """Hey there! I'm learning to send emails using Python!"""

message.set_content(body)

attachment_path = "/tmp/example.png"
attachment_filename = os.path.basename(attachment_path)
mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)

with open(attachment_path, 'rb') as ap:
    message.add_attachment(ap.read(), maintype=mime_type, subtype=mime_subtype, filename=os.path.basename(attachment_path))

mail_server = smtplib.SMTP('localhost')
mail_server = smtplib.SMTP_SSL('smtp.example.com')
mail_server.set_debuglevel(1)

mail_pass = getpass.getpass('Password? ')

try:
    mail_server.login(sender, mail_pass)
except SMTPAuthenticationError as ex :
    print("fail to login")

mail_server.send_message(message)
mail_server.quit()

print(message)


report = SimpleDocTemplate("/tmp/report.pdf")
styles = getSampleStyleSheet()
report_title = Paragraph("A Complete Inventory of My Fruit", styles["h1"])

report.build([report_title])