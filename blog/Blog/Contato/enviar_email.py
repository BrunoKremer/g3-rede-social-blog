import smtplib
import email.message
from django.conf import settings


def enviar_email_via_gmail(assunto, corpo_email, destinatario):
    """ Esta função envia emails utilizando a conta do Gmail """

    msg = email.message.Message()

    msg['Subject'] = assunto

    msg['From'] =settings.EMAIL_HOST_USER
    msg['To'] = destinatario

    password = settings.EMAIL_HOST_PASSWORD

    msg.add_header('Content-Type', 'text/html')

    msg.set_payload(corpo_email)

    s = smtplib.SMTP(settings.EMAIL_HOST)

    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado com sucesso')



