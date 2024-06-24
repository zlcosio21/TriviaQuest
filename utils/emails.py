from django.core.mail import EmailMessage
from dotenv import load_dotenv
import os


# Variable Environments
load_dotenv()
EMAIL = os.getenv("EMAIL")


# Send of Emails
def send_email_register(username, email):
    subject  = "Mensaje desde Trivia Quest"
    message_body  = f"El usuario con nombre {username}, ha registrado su cuenta, con correo {email} \n\n"
    recipient  = email

    user_email = EmailMessage(subject, message_body, "",[recipient], reply_to=[EMAIL])
    user_email.send()

    own_email = EmailMessage(subject, message_body, "",[EMAIL], reply_to=[recipient])
    own_email.send()
