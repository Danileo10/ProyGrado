# Correo cambio contraseña

import smtplib, ssl

port = 587  # For starttls
smtp_server = "smtp-mail.outlook.com"
sender_email = "VeterinariaFielesAngelitos@outlook.com"
receiver_email = "VeterinariaFielesAngelitos@outlook.com"
password = 'Veterinaria123*'
message = """\
Subject: Agendamiento de cita

Su cita fue agendada con exito."""

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)