import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def enviar_email_alerta(assunto, corpo, config_email):
    msg = MIMEMultipart()
    msg['From'] = config_email['@@']
    msg['To'] = config_email['@@']
    msg['Subject'] = assunto

    msg.attach(MIMEText(corpo, 'plain'))

    try:
        server = smtplib.SMTP(config_email['smtp'], config_email['@@'])
        server.starttls()
        server.login(config_email['remetente'], config_email['@@'])
        server.send_message(msg)
        server.quit()
        print("✅ E-mail enviado com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao enviar e-mail: {e}")
