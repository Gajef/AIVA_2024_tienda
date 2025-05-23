import smtplib
from email.message import EmailMessage
import os

class EmailController:
    def __init__(self, receiver_email):
        self.sender = "impecountsl@gmail.com"
        self.password = "bvpuntcfwrmxhwvz"  # contraseña de aplicación (sin espacios)
        self.receiver = receiver_email

    def send_email(self, subject, body, attachment):
        attachment_path = attachment.getPath()
        try:
            msg = EmailMessage()
            msg["Subject"] = subject
            msg["From"] = self.sender
            msg["To"] = self.receiver
            msg.set_content(body)

            with open(attachment_path, "rb") as f:
                msg.add_attachment(
                    f.read(),
                    maintype="application",
                    subtype="csv",
                    filename=os.path.basename(attachment_path)
                )

            with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                smtp.login(self.sender, self.password)
                smtp.send_message(msg)

            print("✅ Email enviado correctamente")
            return "OK"

        except Exception as e:
            print(f"❌ Error al enviar el email: {e}")
            return "ERROR"
