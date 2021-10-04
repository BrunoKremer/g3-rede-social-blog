import smtplib
import email.message
import Blog.local_settings
from Blog.settings import EMAIL_HOST, EMAIL_HOST_PASSWORD, EMAIL_HOST_USER

def enviar_email_via_gmail(assunto, corpo_email, destinatario):
    """ Esta função envia emails utilizando a conta do Gmail """
    msg = email.message.Message()
    msg['Subject'] = assunto
    msg['From'] = EMAIL_HOST_USER 
    msg['To'] = destinatario
    password = EMAIL_HOST_PASSWORD
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)     
    s = smtplib.SMTP(EMAIL_HOST)
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    # print('Email enviado com sucesso')

# enviar_email_via_gmail("Ola Meu Primeiro email", "<p>corpo email<p><br><br>", "equipeinfo@gmail.com")
# habilitar para testar envio de emails na inicialização do sistema.
