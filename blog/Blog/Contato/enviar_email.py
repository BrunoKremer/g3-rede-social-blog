import smtplib
import email.message
import email_settings


def enviar_email_via_gmail(assunto, corpo_email, destinatario):
    """ Esta função envia emails utilizando a conta do Gmail """

    msg = email.message.Message()

    msg['Subject'] = assunto

    msg['From'] = email_settings.GMAIL_FROM
    msg['To'] = destinatario

    password = email_settings.GMAIL_SENHA

    msg.add_header('Content-Type', 'text/html')

    msg.set_payload(corpo_email)

    s = smtplib.SMTP(email_settings.GMAIL_SMTP)

    s.starttls()

    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
    print('Email enviado com sucesso')


enviar_email_via_gmail("Ola Meu Primeiro email", "<p>corpo email<p><br><br>", "seu email")