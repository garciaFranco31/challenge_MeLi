import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from files.consts import SUBJECT

def send_email(owner_email, file_name):
    
    msg = MIMEMultipart()
    msg['From'] = "garciacfranco2001@gmail.com"
    msg['To'] = owner_email
    msg['Subject'] = SUBJECT

    msj = f"Hola! se cambió la configuración de privacida del archivo {file_name} de público a privado"

    msg.attach(MIMEText(msj, 'plain'))

    smtp_server = "smtp.gmail.com"
    smtp_port=587
    smtp_username = os.getenv("EMAIL_SENDER")
    smtp_password = os.getenv("PASSWORD_EMAIL")

    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(msg["From"], msg["To"], msg.as_string())
        server.quit()