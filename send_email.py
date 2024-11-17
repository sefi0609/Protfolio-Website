import smtplib
import ssl
import os

host = 'smtp.gmail.com'
port = 465

username = os.getenv('email_address')

context = ssl.create_default_context()


def send_email(message):
    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, os.getenv('Portfolio'))
        server.sendmail(username, username, message)
