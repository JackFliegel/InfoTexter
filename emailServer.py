import smtplib # Import smtplib for the actual sending function
from email.message import EmailMessage
import ssl
import os
from dotenv import load_dotenv
import json

load_dotenv() # load .env 
# Variables
phoneNumbers = json.loads(os.getenv('PHONE_NUMBERS'))
senderEmail = os.getenv('SENDER_EMAIL')
senderPass = os.getenv('SENDER_PWD')

def sendEmail(body):
    smtpServer = "smtp.gmail.com" # change if not using gmail smtp
    port = 465 #SSL
    smtpUser = senderEmail
    smtpPass = senderPass

    sender = senderEmail
    receivers = phoneNumbers

    subject = "Daily Report"
    message = body

    em = EmailMessage()
    em["From"] = sender
    em["To"] = receivers
    em["Subject"] = subject
    em.set_content(message)

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(smtpServer, port, context=context) as smtp:
        smtp.login(smtpUser, smtpPass)
        smtp.sendmail(smtpUser, receivers, em.as_string())
