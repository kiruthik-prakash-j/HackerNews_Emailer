import os
import smtplib  # send the mail
from email.mime.multipart import MIMEMultipart  # email body
from email.mime.text import MIMEText
import datetime  # system date and time manipulation
from dotenv import load_dotenv
import receiver

load_dotenv()

now = datetime.datetime.now()

SERVER = os.getenv('SMTP_SERVER')
PORT = os.getenv('SMTP_PORT')  # your port number
FROM = os.getenv('EMAIL_ID')  # your from email id
TO = receiver.get_list()  # your to email ids # can be a list
PASS = os.getenv('EMAIL_PASSWORD')  # your email id's password


def compose_mail(content):
    print('Composing Email...')
    msg = MIMEMultipart()
    msg['Subject'] = 'Top News Stories HN [Automated Email]' + ' ' + str(now.day) + '-' + str(now.month) + '-' + str(
        now.year)
    msg['From'] = FROM
    msg['To'] = ', '.join(TO)
    msg.attach(MIMEText(content, 'html'))
    return msg


def send_mail(content):
    msg = compose_mail(content)
    print('Initiating Server...')
    server = smtplib.SMTP(SERVER, PORT)
    try:
        server.set_debuglevel(0)  # Want to see error message set to 1 if not set to 0
        server.ehlo()
        server.starttls()
        server.login(FROM, PASS)
        server.sendmail(FROM, TO, msg.as_string())
        print('Email Sent...')

    except smtplib.SMTPAuthenticationError as e:
        print('SMTP Authentication Error' + str(e))

    finally:
        print('Closing the Server...')
        server.quit()
