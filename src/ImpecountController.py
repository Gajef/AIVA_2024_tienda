from SFTPController import SFTPController
from ProcessVideoController import ProcessVideoController
from CsvGeneratorController import CsvGeneratorController
from EmailController import EmailController
import os

class ImpecountController:
    def __init__(self):
        self.sftp = SFTPController()
        self.video_processor = ProcessVideoController()
        self.csv_generator = CsvGeneratorController()
        self.email = EmailController()

    def run_daily_pipeline(self):
        print("[1] Obteniendo videos del servidor...")
        videos_path = self.sftp.retrieve_last_videos()

        print("[2] Procesando video...")
        info = self.video_processor.count_people_frontal(videos_path[0])
'''
        print("[3] Generando CSV...")
        self.csv_generator.generate_csv(info)

        print("[4] Enviando email...")
        self.email.send_email(
            subject="Informe diario de afluencia",
            body=info,
            attachment_path=csv_path
        )

        print("[5] Eliminando video...")
        os.remove(video_path)
        return "✅ Proceso completo"
'''