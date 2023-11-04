import smtplib # Import smtplib for the actual sending function
from email.message import EmailMessage
import ssl

def sendEmail(body):
    smtpServer = "smtp.gmail.com"
    port = 465 #SSL
    smtpUser = "infoTexter3@gmail.com"
    smtpPass = "taaguyrmwvghoatu"

    sender = "infotexter3@gmail.com"
    receivers = ["5136007416@vzwpix.com", "8594621474@mms.att.net"]
    # receivers = ["5136007416@vzwpix.com"]
    # receivers = ["lildenzil@gmail.com"]

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
