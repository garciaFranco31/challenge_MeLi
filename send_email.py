import smtplib
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials


def get_email_data():
    my_email = input('Type your email:')
    
    return my_email

def send_email(owner_email, file_name):
    MSG = f"Hola! se cambió la configuración de privacida del archivo {file_name} de público a privado"
    SUBJECT = "Cambio de cofiguración de privacidad"

    email_data = get_email_data()
    creds = Credentials.from_authorized_user_file('./files/credentials_module.json')

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email_data, creds)

    msg = MIMEText(MSG)
    msg["Subject"] = SUBJECT
    msg["From"] = email_data[0]
    msg["To"] = owner_email

    server.sendmail(email_data, owner_email, msg.as_string())
    server.quit()

send_email('francogarcia1331@gmail.com', 'hola.txt')