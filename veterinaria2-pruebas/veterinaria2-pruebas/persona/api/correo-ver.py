# Correo verificacion de cuenta


import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp-mail.outlook.com"
sender_email = "VeterinariaFielesAngelitos@outlook.com"
receiver_email = "yerson.porrasg@campusucc.edu.co"
password = 'Veterinaria123*'
message = """\
Subject: Bienvenido a la Veterinaria

Ingrese al siguiente link para verificar su cuenta http://127.0.0.1:8000."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)