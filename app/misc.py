#app/misc.py
import smtplib
from email.mime.text import MIMEText
import configparser
import os

def load_config(config_file=os.path.join(os.path.dirname(__file__), 'config', 'config.ini')):
    try:
        config = configparser.ConfigParser()
        config.read(config_file)
        return config
    except Exception as e:
        error_message = f'Error loading config: {e}'
        print(error_message)
        return None

def send_email(subject, body, recipients):
   config = load_config()
   if config:
      SMTP_USER = (config['General']['smtp_user'])
      SMTP_PASS = (config['General']['smtp_pass'])

   msg = MIMEText(body)
   msg['Subject'] = subject
   msg['From'] = SMTP_USER
   msg['To'] = ", ".join(recipients)
   with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
      smtp_server.login(SMTP_USER, SMTP_PASS)
      smtp_server.sendmail(SMTP_USER, recipients, msg.as_string())
   print("Message sent!")