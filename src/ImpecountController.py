from SFTPController import SFTPController
from VideoController import VideoController
from CsvGeneratorController import CsvGeneratorController
from EmailController import EmailController
import os
from datetime import datetime, timedelta

class ImpecountController:
    def __init__(self):
        self.sftp = SFTPController()
        self.video_processor = VideoController()
        self.csv_generator = CsvGeneratorController()
        self.email = EmailController()

    def run_daily_pipeline(self):
        print("[1] Obteniendo videos del servidor...")
        videos_path = self.sftp.retrieve_last_videos()

        print("[2] Procesando video...")
        info = self.video_processor.count_people_frontal(videos_path[0])

        print("[3] Generando CSV...")
        csv_path = self.csv_generator.generate_csv(info)

        # Obtener la fecha del día anterior
        ayer = (datetime.now() - timedelta(days=1)).strftime("%d/%m/%Y")

        print("[4] Enviando email...")
        status = self.email.send_email(
            subject="Informe diario de afluencia",
            body=f"Analítica del día {ayer}",
            attachment_path=csv_path
        )

        if status == "OK":
            print("📩 Envío del informe completado con éxito.")
        else:
            print("⚠️ Hubo un problema al enviar el informe por email.")
'''
        print("[5] Eliminando video...")
        os.remove(video_path)
        return "✅ Proceso completo"
'''