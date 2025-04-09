import smtplib
from email.message import EmailMessage

class EmailController:
    def __init__(self):
        self.sender = "example@gmail.com"  # cambia por tu cuenta
        self.password = "app-password"     # usa contraseña de app si es Gmail
        self.receiver = "cliente@tienda.com"

    def send_email(self, subject, body, attachment_path):
        msg = EmailMessage()
        msg["Subject"] = subject
        msg["From"] = self.sender
        msg["To"] = self.receiver
        msg.set_content(body)

        with open(attachment_path, "rb") as f:
            msg.add_attachment(f.read(), maintype="application", subtype="csv", filename=attachment_path)

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
            smtp.login(self.sender, self.password)
            smtp.send_message(msg)

        return "Email sent"
